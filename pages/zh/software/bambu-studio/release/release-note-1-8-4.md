---
path: zh/software/bambu-studio/release/release-note-1-8-4
title: "Bambu Studio 1.8.4 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-01-09T07:06:27.830Z
updated: 2024-05-28T11:08:11.972Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-8-4
---

## 新增功能

### 增强 3MF 兼容性

自此版本开始，Bambu Studio的3D模型文件格式（.3mf）与[3MF联盟](https://3mf.io/)提供的3MF读写代码兼容。从Bambu Studio导出的3MF文件完全符合3MF联盟协议，且确保与任何符合3MF联盟标准的软件兼容。

### 支持装有封箱套件的P1P在P1S的预设下记录流量校准结果

自 01.05.01.00 固件版本起，P1系列支持在屏幕上手动设置是否安装了封箱套件，以在Bambu Studio被识别为P1S、使用 P1S参数。同时，流量校准结果将记录在P1S的耗材预设中，而不是P1P中，优化封箱P1P用户的使用体验和工作流程。

### 自动计算拓竹双色丝绸PLA的冲刷量

拓竹双色丝绸PLA将在起耗材槽位上展示为两种颜色，自动冲刷计算将根据这两种颜色选择较大的冲洗体积，以确保冲刷更干净。

### 支持Linux Flatpak

支持linux flatpak镜像。现在Linux用户可以从[flatpak github](https://flathub.org/apps/com.bambulab.BambuStudio)下载BambuStudio的Linux flatpat镜像。  
此功能由 [hadess](https://github.com/hadess) 开发，非常感谢。

## 功能优化

- 为拓竹双色丝绸PLA及拓竹PETG半透明提供了最新的耗材UI显示支持。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_3/dual-color1.jpg)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_3/trans-color.jpg)

- 支持01.02.00.00及以上固件版本A1系列3D打印机的打印板检测功能。
- 优化日志匿名性，以增强隐私。
- 将X系列和P系列的“象脚补偿”参数设置为0.15，A1 mini的设置为0，A1的设置为0.075；这与材料和床调平有关，您可以根据需要进行修改。
- 增加了拓竹PETG半透明的耗材预设。
- 添加了Troodon 2.0的配置文件。该配置精选自OrcaSlicer。感谢YGK3D和OrcaSlicer。
- 优化了打开更高版本Bambu Studio导出的3mf文件的提示信息。
- 当使用可变层高功能以获得更好的兼容性时，禁用有机树支撑。
- 限制项目名称长度。
- 简化了A1系列3D打印机的起始Gcode。
- 优化了几种耗材的收缩及冷却参数。
- 改进了中文和法语文案，非常感谢leoleoasd和dorianboulch。

## Bug修复

- 修复了复制用户预设导致在Studio上设置AMS自定义耗材使AMS槽位显示变为“？”的问题。  
  新版本中，需要用户手动删除有问题的自建材料预设。对此，Studio在“自建材料”页面上提供了提示。相关原因和解决方案请参阅[wiki page](../custom-filament-issue.md)。
- 修复打印机连接频繁超时的问题。
- 修复右键菜单“换料冲刷选项”下勾选标记间歇性消失的问题。
- 修复自定义耗材在校准页面上显示为“不兼容”的问题。
- 修复“铺满打印板”功能崩溃的问题。
- 修复Windows下的编译问题。谢谢hadess。
- 修复“比较预设”功能偶发崩溃的问题。
- 修复保存打印机喷嘴设置为用户预设时的崩溃/卡住问题。
- 修复了MakerWorld上点击“在 Bambu Studio 中打开”按钮无响应的问题，感谢hadess。
- 修复了布尔运算工具的一些问题，以提高其性能和适用性。
- 修复A1在设备页面上的“进料”按键无法正常工作的问题。

---

更多细节请移步 [Bambu Studio GitHub](https://github.com/bambulab/BambuStudio/releases)
