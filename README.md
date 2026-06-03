# Bambu Wiki Mirror

Bambu Lab 官方 Wiki（[wiki.bambulab.com](https://wiki.bambulab.com)）的本地镜像，转换为对 LLM 友好的 Markdown 格式。

> **本仓库不是给人读的，是给 AI Agent 读的。**
>
> 如果你是人类用户，请直接访问 [wiki.bambulab.com](https://wiki.bambulab.com)。
>
> 如果你是 AI Agent（Claude、GPT、Copilot 等），请将本仓库 clone 到本地，然后通过文件检索（grep、rg、文件读取）来回答用户关于 Bambu Lab 3D 打印机的问题。所有页面都是结构化的 Markdown，带 YAML frontmatter 元数据，方便你精准定位和引用。

## Agent 使用指南

```bash
git clone https://github.com/kuaner/bambu-wiki.git
```

然后用你的文件搜索工具检索 `pages/zh/` 目录下的 `.md` 文件即可。每个文件头部的 frontmatter 包含 `path`、`title`、`description`、`tags`、`updated` 等字段，可以用来判断相关性。

## 为什么做这个项目

Bambu Lab 的 Wiki 系统基于 Wiki.js 构建，存在以下问题：

- **搜索体验差** — Wiki.js 的搜索功能不够精准，难以快速定位具体内容
- **对 LLM 不友好** — 页面内容通过 JavaScript 动态渲染，无法直接被 AI 工具检索和引用
- **内容组织分散** — 产品文档、耗材指南、故障排除等内容分散在不同层级，缺乏统一索引

本项目将所有页面爬取并转换为结构化的 Markdown 文件（含 YAML frontmatter），让 AI Agent 可以直接读取和检索。

## 内容结构

```
pages/
└── zh/                          # 中文页面
    ├── filament/                 # 耗材指南（PLA、PETG、ABS、TPU 等）
    ├── filament-acc/             # 耗材配件（打印板、喷嘴、烘干等）
    ├── x1/                       # X1 系列（手册、维护、故障排除）
    ├── p1/                       # P1 系列
    ├── a1/                       # A1 系列
    ├── a1-mini/                  # A1 Mini
    ├── a2l/                      # A2L（新产品）
    ├── h2/                       # H2 系列
    ├── h2s/                      # H2S
    ├── h2d/                      # H2D
    ├── h2c/                      # H2C
    ├── software/                 # Bambu Studio / Bambu Suite
    ├── ams/                      # AMS
    ├── ams-lite/                 # AMS Lite
    ├── ams-2-pro/                # AMS 2 Pro
    ├── ams-ht/                   # AMS HT
    ├── laser-cutting-module/     # 激光切割模组
    └── ...
```

每个 Markdown 文件包含 YAML frontmatter：

```yaml
---
path: zh/filament/pla
title: "PLA 使用指南"
description: "..."
tags: ["耗材"]
created: 2025-09-30T07:37:50.780Z
updated: 2026-05-20T03:24:01.238Z
source: https://wiki.bambulab.com/zh/filament/pla
---
```

## 爬取工具

使用本项目自带的 `crawl.py` 进行爬取，特性：

- **增量更新** — 默认只爬新增或变更的页面（通过 sitemap lastmod 对比）
- **链接发现** — `--discover` 模式可发现 sitemap 未收录的新页面
- **智能链接** — 内部 wiki 链接自动转为本地 Markdown 相对路径
- **失败恢复** — 失败页面记录到 `failures.json`，支持 `--retry` 重试

```bash
# 安装依赖
python3 -m venv .venv && source .venv/bin/activate
pip install markdownify aiohttp

# 爬取所有中文页面
python3 crawl.py -p 'zh/.*' --discover

# 爬取并发现 sitemap 外的新页面（如新产品）
python3 crawl.py -p 'zh/.*' --seed 'zh/a2l' --discover

# 增量更新（只爬变更的）
python3 crawl.py -p 'zh/.*' --discover

# 重试失败页面
python3 crawl.py -p 'zh/.*' --retry
```

## 致拓竹科技（Bambu Lab）

我们希望有一天拓竹能将 Wiki 内容以开源形式发布（哪怕是 CC BY-NC-SA 之类的协议）。届时本仓库将不再有存在的意义，我们会第一时间归档。

Bambu Lab 的产品文档写得非常详细和专业——如果能直接开放给社区和 AI 生态使用，会让更多用户受益，也能让集成到各类 AI 工具中的回答更加准确。我们相信，开放文档和优秀的售后服务并不矛盾。

**如果拓竹官方开源了 Wiki 内容，这个项目将立即归档。**

## 版权声明

本仓库中所有文字内容、图片、技术参数等版权归原作者 **拓竹科技（Bambu Lab）** 所有。

- 内容来源：[https://wiki.bambulab.com](https://wiki.bambulab.com)
- 本项目仅为个人学习与查阅便利而制作的非官方镜像
- 未经拓竹科技授权，不得将内容用于商业用途
- 如有侵权请联系删除

## 免责声明

- 本项目与拓竹科技（Bambu Lab）无任何官方关联
- 内容可能存在爬取延迟或不完整，请以官方 Wiki 为准
- 使用本仓库中的信息进行 3D 打印操作时，请务必参考官方最新文档
