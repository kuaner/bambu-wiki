---
path: zh/software/bambu-studio/release/release-note-2-8-2-61
title: "Bambu Studio 2.8.2.61 版本说明"
description: ""
tags: []
created: 2026-08-21T06:21:59.278Z
updated: 2026-08-21T06:21:59.278Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-8-2-61
---

Bambu Studio **2.8.2.61** 是基于前序版本的小幅优化更新，主要修复了部分已知问题，并改进了一些功能体验。

## 修复

1. 修复部分makerlab生成器无法访问的问题（注意：浮雕生成器下载模型后可能存在导入延迟，后续makerlab后端直接线上修复）
2. 修复了未登录状态下访问 MakerWorld 时，未正常弹出登录窗口的问题。
3. 修复了旧版本 3MF 文件在点击“同步打印机信息”后，挤出机数量仍显示为 0，并进一步导致切片异常的问题。
4. 在准备页面左侧的耗材列表中新增或删除耗材时，列表将自动定位到末尾，避免在耗材列表较长时，用户误以为操作未生效。
5. 修复了弱网环境下 LAN 模式偶发闪退的问题。
6. 更新了 X2D 和 H 系列机型的预设，修复部分异常参数值，避免预设加载或使用异常。
