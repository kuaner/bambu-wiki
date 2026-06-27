---
path: zh/software/bambu-studio/release/release-note-2-7-1-62
title: "Bambu Studio 2.7.1.62版本说明"
description: ""
tags: []
created: 2026-06-16T14:08:49.311Z
updated: 2026-06-17T08:30:56.670Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-7-1-62
---

本版本基于 2.7.1 Public Release，针对部分MacOS版本中出现的Studio启动缓慢问题进行了优化，受影响的MacOS用户请尽快升级。此外，本版本还包含若干其他问题的修复。

## Bug修复

1. 针对部分MacOS版本可能出现的启动缓慢问题进行了修复，感谢[@BenJule](https://github.com/BenJule)的贡献。偏好设置中增加了耗材管理启用/关闭的选项，针对MacOS该选项默认关闭。

![screenshot-20260617-zn155046.png](https://wiki.bambulab.com/software/bambu-studio/release-note/2-7-1-62/screenshot-20260617-zn155046.png)

2. 修复了MacOS用户（MacOS 27及以上版本除外）网络插件安装失败的问题。

3. 修复了叠色打印中部分场景跨z高度涂色打印时可能出现的路径规划错误。

4. 修复了X2D耗材变轨器的UI闪烁的问题。

5. 修复了涂色工具中“连接相同颜色”的功能异常。

6. 修复了部分场景下设备页闪退、卡死的问题。

7. 修复了打开部分MakerWorld模型后崩溃的错误，再次感谢[@BenJule](https://github.com/BenJule)。
