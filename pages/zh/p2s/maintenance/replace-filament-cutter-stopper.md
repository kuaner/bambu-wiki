---
path: zh/p2s/maintenance/replace-filament-cutter-stopper
title: "更换 P2S 切刀顶杆组件和跳齿修复指引"
description: "本文介绍了如何更换 P2S 切刀顶杆组件和跳齿修复。"
tags: []
created: 2025-10-14T12:59:29.201Z
updated: 2026-08-10T03:27:44.056Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-filament-cutter-stopper
---

## 切刀顶杆组件

P2S 的切刀顶杆组件是安装在打印机腔内左侧，用于顶住切刀刀柄，实现切断耗材功能的配件。

|  |  |
| --- | --- |
|  |  |
| 一版本 | 二版本 |

该组件于近期完成设计升级。为便于说明，本指南将升级后的组件称为二版本，升级前的组件称为一版本，两者主要区别在于跳齿问题的处理方式：

- 二版本：优化了结构设计，若出现跳齿可手动修复，无需更换整个组件。
- 一版本：不支持手动修复，功能失效时需更换整个组件。

## 何时适用

切刀顶杆功能失效、错位

## 所需的工具和材料

- 切刀顶杆组件
- H2.0 内六角扳手
- H1.5 内六角扳手

> 为了更清晰地展示螺丝的位置，我们在拆除左侧板的情况下进行了拍摄；实际更换时，无需拆除左侧板。

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除切刀顶杆组件

### 步骤 1：移除料管支架

参考 [更换料管支架](replace-ptfe-tube-bracket.md) 的指引，移除料管支架。  
![ptfe_tube_bracket_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/ptfe_tube_bracket_002.png)

### 步骤 2：移除 AP 板盖

揭开 AP 板盖检修端，从 AP 板上断开左 LED 灯连接线；

![led_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/led_001.png)  
使用 H1.5 内六角扳手移除 2 颗 AP 板盖固定螺丝（BT2x8）；  
![ap_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap_002.png)  
握住 AP 板盖连接拖链的一端，向右侧方向拉出 AP 板盖。在拉出时请用左手托住 AP 板左侧，当右侧拖链端拉出时，左手扶住 AP 板盖，避免 AP 板盖跌落。

> **易损提示：请勿从前端直接掰开 AP 板盖，会导致 AP 板盖折断！**

![拔出ap板盖1_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap1_003.png)

![拔出ap板盖2_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap2_004.png)

### 步骤 3：移除切刀顶杆组件

将工具头移向右前方，盖板搭在合适位置即可。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_5.jpg)

使用 H2.0 内六角扳手的**短端**移除切刀顶杆组件上方的 1 颗螺丝。

> 请勿使用长端斜向拧螺丝，否则可能导致螺丝滑丝。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_3.jpg)  
再移除切刀顶杆组件底部的 2 颗螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_6.jpg)

用手从下方顶起切刀顶杆组件的转轴，将其从打印机框架上取下。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_1.jpg)

## 跳齿修复

本章节步骤适用于**二版**顶杆组件。一版请跳过本章节，更换新的切刀顶杆组件。

如下图，一二版齿条位置的设计不同，可据此判断：**一版（左）；二版（右）**。

![new_vs_old.png](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/new_vs_old.png)

首先，检查顶杆是否能够正常弹出。若无法像下方正常示例一样弹出，则需要修复跳齿问题。

**正常状态**：拨动摆杆 1，摆杆 1 位置在最下方时，2 处顶杆垂直弹出。

|  |  |
| --- | --- |
|  |  |

**异常状态：**

1. 摆杆 1 位置在最下方时，2 处顶杆**弹出不到位**，不垂直于组件，如下左图。
2. 摆杆 1 位置在最下方时，2 处顶杆**不弹出**，如下右图。

|  |  |
| --- | --- |
|  |  |

**跳齿修复：**

左手将摆杆固定在最下方的位置，右手轻微用力拨动顶杆，使其垂直于组件。

|  |  |
| --- | --- |
|  |  |

调整完毕后，拨动摆杆，顶杆正常弹出，即为修复成功。

![normal.webp](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/normal.webp)

修复成功后，按照下方安装步骤将组件装回。

## 安装切刀顶杆组件

### 步骤 1：安装切刀顶杆组件

调整线缆位置，避免安装切刀顶杆时挤压线缆。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_8.jpg)  
将切刀顶杆组件放置在打印机框架上。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_7.jpg)  
安装切刀顶杆组件上方的 1 颗螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_4.jpg)  
安装切刀顶杆组件底部的 2 颗螺丝。

![](https://wiki.bambulab.com/p2s/maintenance/replace-filament-cutter-stopper/1_6.jpg)

### 步骤 2：安装 AP 板盖

沿着安装槽将 AP 板盖拖链一侧推到位（可使用内六角扳手确认螺丝孔对齐），在推动 AP 板的时候，请用手扶着 AP 板盖左侧，并将左侧的卡扣卡入框架中。

![装回ap板盖1_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap1_005.png)  
![装回ap板盖2_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap2_006.png)  
![装回ap板盖3_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap3_007.png)  
将 LED 补光灯 - 左的连接线插入 AP 板，并将检修端扣紧。

![led_补光灯接口_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/led_001.png)  
使用 H1.5 内六角扳手锁紧 2 颗螺丝（BT2x8）。  
![ap_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap_002.png)

### 步骤 3：安装料管支架

请参考 [更换料管支架](replace-ptfe-tube-bracket.md) 的指引，将料管支架重新装回。  
![ptfe_tube_bracket_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/ptfe_tube_bracket_002.png)

## 如何验证成功

连接电源，打开打印机，手动上料后，执行一次退料操作，能正常完成则更换成功。

如果您遇到任何问题，请先回溯您的步骤并检查安装位置以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
