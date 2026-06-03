---
path: zh/software/bambu-studio/release/release-note-2-1-1
title: "Bambu Studio 2.1.1 版本说明"
description: ""
tags: ["bambu studio"]
created: 2025-06-16T09:22:51.436Z
updated: 2025-06-16T12:15:49.692Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-1-1
---

V2.1.1 是基于 V2.1.0 的一个版本，主要修复了在 V2.1.0 中发现的部分问题。

## 改进

1. 支持为单个零件设置独立流量比率（开发者模式选项），感谢 [@RyanHir](https://github.com/RyanHir) 的贡献。  
   ![cn-1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_1/cn-1.png)

## Bug 修复

1. 修复了 H2D 进行流量校准时热床未与腔温同步加热的问题。（[#7054](https://github.com/bambulab/BambuStudio/issues/7054)）
2. 修复了在非打印板区域错误生成 Brim 的问题。（[#7088](https://github.com/bambulab/BambuStudio/issues/7088)）
3. 修复了部分情况下Brim与Skirt重叠的问题。
4. 修复了在普通支撑模式下，部分有狭窄悬垂区域的模型使用支撑材料时的切片崩溃问题。（[#7204](https://github.com/bambulab/BambuStudio/issues/7204)）
5. 修复了单个多色零件在逐件打印模式下的切片错误问题。（[#7121](https://github.com/bambulab/BambuStudio/issues/7121), [#7092](https://github.com/bambulab/BambuStudio/issues/7092), [#7146](https://github.com/bambulab/BambuStudio/issues/7146), [#7183](https://github.com/bambulab/BambuStudio/issues/7183), [#7229](https://github.com/bambulab/BambuStudio/issues/7229), [#7247](https://github.com/bambulab/BambuStudio/issues/7247)）
6. 修复了第三方预设同步后可能导致崩溃的问题，并修复了部分参数的解析与显示错误，暂时关闭了相应的冲刷温度参数选项。
7. 修复了若干文案和拼写错误，感谢 [@eried](https://github.com/eried) 和 [@maximeconnolly](https://github.com/maximeconnolly) 的贡献。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
