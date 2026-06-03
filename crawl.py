#!/usr/bin/env python3
"""
Bambu Lab Wiki Crawler
Crawls wiki.bambulab.com pages, converts to LLM-friendly markdown.

Smart by default: only crawls new or changed pages (via sitemap lastmod).
Discovers pages not in sitemap via internal link scanning.

Usage:
  # Crawl all zh pages (only new/changed)
  python3 crawl.py -p 'zh/.*'

  # With link discovery (finds pages missing from sitemap)
  python3 crawl.py -p 'zh/.*' --discover

  # Seed a new product page not yet in sitemap
  python3 crawl.py -p 'zh/.*' --seed 'zh/a2l' --discover

  # Force re-crawl everything
  python3 crawl.py -p 'zh/.*' --force

  # Only X1 pages
  python3 crawl.py -p 'zh/x1/.*'

  # Custom concurrency & rate
  python3 crawl.py -p 'zh/.*' -c 3 -d 1.0

  # Retry failed pages
  python3 crawl.py -p 'zh/.*' --retry
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

import aiohttp
from markdownify import markdownify as md

SITEMAP_URL = "https://wiki.bambulab.com/sitemap.xml"
BASE_URL = "https://wiki.bambulab.com"

# Regex patterns for extracting data from HTML
RE_PAGE_TAG = re.compile(r'<page\s+([^>]+)>', re.DOTALL)
RE_CONTENTS = re.compile(r'<template slot="contents">(.*?)</template>', re.DOTALL)
RE_ATTR = re.compile(r'([\w-]+)=["\']([^"\']*)["\']')


def parse_sitemap(xml_text: str) -> list[dict]:
    """Parse sitemap XML, return list of {url, lastmod}."""
    entries = []
    for m in re.finditer(
        r'<url>\s*<loc>(.*?)</loc>\s*(?:<lastmod>(.*?)</lastmod>)?\s*</url>',
        xml_text, re.DOTALL
    ):
        url = m.group(1).strip()
        lastmod = (m.group(2) or "").strip()
        entries.append({"url": url, "lastmod": lastmod})
    return entries


def parse_page_attrs(attr_str: str) -> dict:
    """Parse attributes from the <page ...> tag."""
    attrs = {}
    for m in RE_ATTR.finditer(attr_str):
        key = m.group(1).strip(":")
        val = m.group(2)
        val = val.replace("&quot;", '"').replace("&amp;", "&")
        val = val.replace("&lt;", "<").replace("&gt;", ">")
        attrs[key] = val
    return attrs


def extract_content(html: str) -> tuple[dict, str]:
    """Extract page metadata and content from HTML."""
    page_match = RE_PAGE_TAG.search(html)
    if not page_match:
        return {}, ""
    attrs = parse_page_attrs(page_match.group(1))
    content_html = ""
    m = RE_CONTENTS.search(html)
    if m:
        content_html = m.group(1)
    return attrs, content_html


def rewrite_internal_links(content_md: str, page_path: str,
                           known_paths: set[str]) -> str:
    """Rewrite internal wiki links to local .md relative paths."""
    WIKI_PREFIX = "https://wiki.bambulab.com/"

    def replace_link(m):
        text = m.group(1)
        url = m.group(2)
        if not url.startswith(WIKI_PREFIX):
            return m.group(0)
        target = url[len(WIKI_PREFIX):]
        if target not in known_paths:
            return m.group(0)
        current_parts = page_path.split("/")
        target_parts = target.split("/")
        common = 0
        for a, b in zip(current_parts, target_parts):
            if a == b:
                common += 1
            else:
                break
        up_count = max(0, len(current_parts) - common - 1)
        rel_parts = [".."] * up_count + target_parts[common:]
        rel_path = "/".join(rel_parts) + ".md"
        return f"[{text}]({rel_path})"

    return re.sub(
        r'(?<!!)\[([^\]]*)\]\((https://wiki\.bambulab\.com/[^)]+)\)',
        replace_link, content_md
    )


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean markdown."""
    if not html:
        return ""
    html = re.sub(r'<a[^>]*class="toc-anchor"[^>]*>.*?</a>', '', html)
    html = re.sub(r'\s+style="[^"]*"', '', html)
    html = re.sub(r'<img\s+src="/', f'<img src="{BASE_URL}/', html)
    html = re.sub(r'<a\s+href="/', f'<a href="{BASE_URL}/', html)
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
    result = md(html, heading_style="ATX", bullets="-")
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip()


def url_to_path(url: str) -> str:
    """Extract the wiki path from a full URL."""
    return url.replace(BASE_URL + "/", "")


def save_page(out_dir: Path, page_path: str, attrs: dict, content_md: str):
    """Save a page as markdown with YAML frontmatter."""
    file_path = out_dir / (page_path + ".md")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    title = attrs.get("title", "")
    description = attrs.get("description", "")
    tags_raw = attrs.get("tags", "[]")
    try:
        tags = [t.get("tag", t) if isinstance(t, dict) else t
                for t in json.loads(tags_raw)]
    except (json.JSONDecodeError, TypeError):
        tags = []
    updated = attrs.get("updated-at", "")
    created = attrs.get("created-at", "")
    source = f"{BASE_URL}/{page_path}"
    frontmatter = f"""\
---
path: {page_path}
title: "{title}"
description: "{description}"
tags: {json.dumps(tags, ensure_ascii=False)}
created: {created}
updated: {updated}
source: {source}
---

"""
    file_path.write_text(frontmatter + content_md + "\n", encoding="utf-8")


async def fetch_page(session: aiohttp.ClientSession, url: str,
                     semaphore: asyncio.Semaphore, delay: float) -> tuple[str, str, int]:
    """Fetch a single page. Returns (url, html, status)."""
    async with semaphore:
        if delay > 0:
            await asyncio.sleep(delay)
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                html = await resp.text()
                return url, html, resp.status
        except Exception:
            return url, "", 0


async def crawl(urls: list[str], concurrency: int, delay: float,
                out_dir: Path, known_paths: set[str]
                ) -> tuple[dict[str, str], dict[str, str]]:
    """
    Crawl all URLs, save pages.
    Returns (manifest, failures).
    """
    if not urls:
        return {}, {}
    semaphore = asyncio.Semaphore(concurrency)
    manifest = {}
    failures = {}
    total = len(urls)
    done = 0
    errors = 0

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [fetch_page(session, url, semaphore, delay) for url in urls]

        for coro in asyncio.as_completed(tasks):
            url, html, status = await coro
            page_path = url_to_path(url)
            done += 1

            if status != 200 or not html:
                errors += 1
                reason = f"HTTP {status}" if status else "timeout/error"
                failures[page_path] = reason
                print(f"  [{done}/{total}] FAIL ({reason}) {page_path}")
                continue

            attrs, content_html = extract_content(html)
            if not content_html:
                errors += 1
                failures[page_path] = "no content"
                print(f"  [{done}/{total}] SKIP (no content) {page_path}")
                continue

            content_md = html_to_markdown(content_html)
            content_md = rewrite_internal_links(content_md, page_path, known_paths)
            save_page(out_dir, page_path, attrs, content_md)
            manifest[page_path] = attrs.get("updated-at", "")

            if done % 50 == 0 or done == total:
                print(f"  [{done}/{total}] OK ({errors} errors)")

    return manifest, failures


def load_json(path: Path) -> dict:
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def discover_links(out_dir: Path, manifest: dict, known_paths: set[str],
                   lang_prefix: str) -> set[str]:
    """Scan all .md files for internal links not yet crawled or in sitemap."""
    internal_re = re.compile(
        r'https://wiki\.bambulab\.com/(' + re.escape(lang_prefix) + r'/[^\s\)\"]+)'
    )
    relative_re = re.compile(r'\]\(([^)]+\.md)\)')
    discovered = set()
    all_known = known_paths | set(manifest.keys())

    for md_file in out_dir.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        rel = md_file.relative_to(out_dir)
        file_dir = rel.parent

        for m in internal_re.finditer(text):
            link_path = m.group(1).split("#")[0].split("?")[0]
            if link_path not in all_known and "/staging/" not in link_path:
                discovered.add(link_path)

        for m in relative_re.finditer(text):
            link = m.group(1)
            target = (file_dir / link).resolve()
            try:
                target_rel = target.relative_to(out_dir.resolve())
            except ValueError:
                continue
            wiki_path = str(target_rel).replace(".md", "")
            if not (out_dir / target_rel).exists() \
                    and wiki_path not in all_known \
                    and "/staging/" not in wiki_path:
                discovered.add(wiki_path)

    return discovered


async def main():
    parser = argparse.ArgumentParser(
        description="Crawl Bambu Lab Wiki to markdown")
    parser.add_argument("--pattern", "-p", required=True,
                        help="Regex to filter URLs (e.g. 'zh/.*' or 'zh/x1/.*')")
    parser.add_argument("--output", "-o", default="pages",
                        help="Output directory (default: pages)")
    parser.add_argument("--concurrency", "-c", type=int, default=5,
                        help="Max concurrent requests (default: 5)")
    parser.add_argument("--delay", "-d", type=float, default=0.5,
                        help="Delay between requests in seconds (default: 0.5)")
    parser.add_argument("--force", "-f", action="store_true",
                        help="Force re-crawl all pages (ignore manifest)")
    parser.add_argument("--retry", "-r", action="store_true",
                        help="Retry previously failed pages only")
    parser.add_argument("--discover", "-D", action="store_true",
                        help="Discover pages via internal links not in sitemap")
    parser.add_argument("--seed", "-s", nargs="*", default=[],
                        help="Additional seed URLs to crawl (e.g. 'zh/a2l')")
    parser.add_argument("--limit", "-l", type=int, default=0,
                        help="Limit number of pages (0 = no limit, for testing)")
    args = parser.parse_args()

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    failures_path = out_dir / "failures.json"

    # --- Load existing state ---
    manifest = load_json(manifest_path)
    failures = load_json(failures_path)
    if manifest:
        print(f"Existing manifest: {len(manifest)} pages")

    # --- Fetch sitemap ---
    print("Fetching sitemap...")
    async with aiohttp.ClientSession() as session:
        async with session.get(SITEMAP_URL) as resp:
            sitemap_xml = await resp.text()
    entries = parse_sitemap(sitemap_xml)
    print(f"Sitemap: {len(entries)} total URLs")

    # All known sitemap paths (for link rewriting, all languages)
    known_paths = {url_to_path(e["url"]) for e in entries}

    # --- Retry mode ---
    if args.retry:
        if not failures:
            print("No failed pages to retry.")
            return
        print(f"Retrying {len(failures)} failed pages...")
        retry_urls = [f"{BASE_URL}/{p}" for p in failures]
        recovered, new_failures = await crawl(
            retry_urls, args.concurrency, args.delay, out_dir, known_paths
        )
        print(f"  Recovered: {len(recovered)}, Still failing: {len(new_failures)}")
        manifest.update(recovered)
        save_json(manifest_path, manifest)
        if new_failures:
            save_json(failures_path, new_failures)
        else:
            failures_path.unlink(missing_ok=True)
            print("All pages recovered!")
        return

    # --- Filter sitemap by pattern ---
    pattern = re.compile(args.pattern)
    filtered = [e for e in entries
                if pattern.search(url_to_path(e["url"]))
                and "/staging/" not in url_to_path(e["url"])]
    print(f"Matched: {len(filtered)} URLs (staging excluded)")

    # --- Smart diff: only crawl new or changed pages ---
    if args.force:
        to_crawl = [e["url"] for e in filtered]
        print(f"Force mode: will crawl all {len(to_crawl)} pages")
    else:
        to_crawl = []
        skipped = 0
        for e in filtered:
            path = url_to_path(e["url"])
            if manifest.get(path) == e["lastmod"]:
                skipped += 1
            else:
                to_crawl.append(e["url"])
        print(f"Up-to-date: {skipped}, To crawl: {len(to_crawl)}")

    # --- Add seed URLs ---
    if args.seed:
        seed_urls = []
        for s in args.seed:
            url = s if s.startswith("http") else f"{BASE_URL}/{s}"
            path = url_to_path(url)
            # Skip if already in manifest (unless --force)
            if not args.force and path in manifest:
                continue
            seed_urls.append(url)
        if seed_urls:
            to_crawl.extend(seed_urls)
            print(f"Added {len(seed_urls)} seed URLs")

    if args.limit > 0:
        to_crawl = to_crawl[:args.limit]
        print(f"Limited to {args.limit} pages")

    # --- Crawl ---
    if to_crawl:
        print(f"\nCrawling {len(to_crawl)} pages "
              f"(concurrency={args.concurrency}, delay={args.delay}s)...")
        start = time.time()
        new_manifest, new_failures = await crawl(
            to_crawl, args.concurrency, args.delay, out_dir, known_paths
        )
        elapsed = time.time() - start
        print(f"\nDone in {elapsed:.1f}s")
        if new_failures:
            print(f"  Failed: {len(new_failures)} pages")

        manifest.update(new_manifest)
        failures.update(new_failures)
        # Remove from failures any pages that succeeded this run
        for p in new_manifest:
            failures.pop(p, None)
    else:
        new_manifest = {}
        new_failures = {}
        print("\nAll pages up-to-date.")

    # --- Discover phase ---
    if args.discover and manifest:
        lang_prefix = ""
        sample = next(iter(manifest))
        parts = sample.split("/")
        if len(parts) >= 2:
            lang_prefix = parts[0]
        if not lang_prefix:
            print("\nDiscover: can't determine language, skipping.")
        else:
            print(f"\n--- Discovering orphan pages ({lang_prefix}/*) ---")

            # Multi-level BFS discovery
            all_new = {}
            level = 1
            while True:
                discovered = discover_links(
                    out_dir, manifest, known_paths, lang_prefix
                )
                if not discovered:
                    print("No more pages to discover.")
                    break

                print(f"Level {level}: found {len(discovered)} new pages")
                for p in sorted(discovered)[:10]:
                    print(f"  {p}")
                if len(discovered) > 10:
                    print(f"  ... and {len(discovered) - 10} more")

                urls = [f"{BASE_URL}/{p}" for p in discovered]
                d_manifest, d_failures = await crawl(
                    urls, args.concurrency, args.delay, out_dir, known_paths
                )
                manifest.update(d_manifest)
                failures.update(d_failures)
                for p in d_manifest:
                    failures.pop(p, None)
                all_new.update(d_manifest)

                if not d_manifest:
                    print("No new pages could be fetched. Stopping discovery.")
                    break
                level += 1

            if all_new:
                print(f"\nDiscovery total: {len(all_new)} new pages")
            # Update known_paths with discovered pages for link rewriting
            known_paths.update(all_new.keys())

    # --- Save state ---
    save_json(manifest_path, manifest)
    print(f"\nManifest: {len(manifest)} pages -> {manifest_path}")

    if failures:
        save_json(failures_path, failures)
        print(f"Failures: {len(failures)} pages -> {failures_path}")
        print("  Run with --retry to re-attempt")
    else:
        failures_path.unlink(missing_ok=True)

    # Cleanup: remove local .md files whose paths are no longer in manifest
    # (pages that were deleted from the wiki)
    if manifest and not args.force:
        local_files = {str(f.relative_to(out_dir)).removesuffix(".md")
                       for f in out_dir.rglob("*.md")
                       if f.name != "manifest.json" and f.name != "failures.json"}
        orphaned = local_files - set(manifest.keys())
        for path in orphaned:
            f = out_dir / (path + ".md")
            f.unlink(missing_ok=True)
            # Try to clean up empty parent dirs
            try:
                f.parent.rmdir()
            except OSError:
                pass
        if orphaned:
            print(f"Cleaned up {len(orphaned)} deleted pages")


if __name__ == "__main__":
    asyncio.run(main())
