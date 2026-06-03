---
path: zh/software/bambu-studio/release/release-note-1-7-6
title: "Bambu Studio 1.7.6 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-09-22T02:24:56.692Z
updated: 2024-05-28T10:58:58.944Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7-6
---

这个Bambu Studio版本主要基于[1.7.4](release-note-1-7-4.md) 支持了 A1 mini，同时也优化和修复了一些问题。

## 新增功能

### 支持 Bambu Lab A1 mini

在这里可以添加Add Bambu Lab A1 mini 的打印机预设

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_6/a1_mini_1.png)

Bambu Lab A1 mini 的设备页

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_6/a1_mini_2.png)

### 如下图所示，添加小圆盘到内置模型中，可被用作耳状裙边（Ear Brim）

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_6/brim_ear_model.png)

### 在开发者模式下，现在可以修改第三方打印机热床

这是PrusaSlicer 已用的功能，我们将他加回来了。感谢PrusaSlicer!

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_6/set_bed_shape.png)

### 添加了z-hop upper boundary 和 z-hop lower boundary，设置后z-hop只在两个参数之间时生效

这是PrusaSlicer 已用的功能，我们将他加回来了。感谢PrusaSlicer!

<https://github.com/bambulab/BambuStudio/issues/77>
  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_6/z_hop_boundary.png)

## 优化

添加第三方打印机Tronxy

感谢 github用户 erabus04的贡献。

<https://github.com/bambulab/BambuStudio/issues/2355>

当前打印机为第三方打印机时，添加缩略图到Gcode中

<https://github.com/bambulab/BambuStudio/issues/2166>

Add ModelIO support on macOS, by Merikesh Dev（ https://github.com/merikesh）

<https://github.com/bambulab/BambuStudio/issues/2439>

在自动流量挤出标定时，增加 0.2mm 0.6mm 0.8mm 的喷嘴直径 (需配合X1/X1C固件版本 OTA version 01.06.05.00)

开发者模式的选项将在重启Studio后仍然生效

<https://github.com/bambulab/BambuStudio/issues/2259>

新OpenSSL到3.1版本，更新zlib到1.2.13，更新expat到2.5，解决潜在的安全隐患

<https://github.com/bambulab/BambuStudio/issues/1843>

将Skirt距离的上限修改为 50mm

<https://github.com/bambulab/BambuStudio/issues/2318>

支持预设在线升级

优化自动排列功能的空间利用率

调整了自动排列的对象间距

## 修复

修复在顶壳层数较小、熨烫类型均为实心的情况下，产生了多余熨烫层的问题  
<https://github.com/bambulab/BambuStudio/issues/2250>

修复模型边缘较短时的崩溃问题  
<https://github.com/bambulab/BambuStudio/issues/2283>

对于P系列打印机，优先使用LAN通道实现媒体流播放  
<https://github.com/bambulab/BambuStudio/issues/2162>
<https://github.com/bambulab/BambuStudio/issues/2091>

用户登录后，卸载默认的耗材预设和工艺预设
