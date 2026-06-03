---
path: zh/p2s/maintenance/replace-ap-board
title: "更换 P2S AP 板"
description: ""
tags: []
created: 2025-10-14T12:50:13.586Z
updated: 2026-05-21T13:37:31.399Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-ap-board
---

## AP 板

AP 板的全称是应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/dlb051.jpg)

- **AP 板的备件包含如下：**

1. AP 板 \* 1
2. M3x4.5 螺丝 \* 4
3. 散热硅脂 \* 1

- **连接器介绍：**

![ap_connectors_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap_connectors_007.png)

## 何时更换

1. AP 板出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
2. 经 Bambu Lab 技术支持分析需更换 AP 板。

## 所需的工具头和材料

1. 新的 AP 板
2. H2.0 内六角扳手
3. H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 AP 板

### 步骤 1：移除料管支架

参考 [更换料管支架](replace-ptfe-tube-bracket.md) 的指引，移除料管支架。  
![ptfe_tube_bracket_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/ptfe_tube_bracket_002.png)

### 步骤 2：移除 AP 板盖

揭开 AP 板盖检修端，从 AP 板上断开左 LED 灯连接线；

![led_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/led_001.png)

使用 H1.5 内六角扳手移除 2 颗 AP 板盖固定螺丝（BT2x8）；

![ap_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap_002.png)

握住 AP 板盖连接拖链的一端，向右侧方向拉出 AP 板盖。在拉出时请用左手托住 AP 板左侧，当右侧拖链端拉出时，左手扶住 AP板盖，避免 AP 板盖跌落。

> **易损提示：请勿从前端直接掰开 AP 板盖，会导致 AP 板盖折断！**

![ap1_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap1_003.png)

![ap2_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap2_004.png)

### 步骤 3：移除 AP 板

将 AP 板上的连接线依次断开。

- 屏幕排线和实况相机的排线需先解开卡扣，再移除排线；
- 其他带锁扣的线缆需先按住插头上的卡扣解锁再移除。

![ap0_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap0_001.png)

| 序号 | 接口 | 序号 | 接口 |
| --- | --- | --- | --- |
| 1 | 屏幕连接线 | 6 | LED 补光灯 - 左 |
| 2 | 腔温传感器 | 7 | Wifi 天线 |
| 3 | 前门检测开关 | 8 | MC-AP 线（通信） |
| 4 | LED 灯 - 前 | 9 | MC-AP 线（供电） |
| 5 | U 盘接口组件 | 10 | 实况摄像头 |

使用 H2.0 内六角扳手移除四颗固定螺丝（M3x4.5），然后即可将 AP 板取出。  
![ap0_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap0_002.png)  
![ap0_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap0_003.png)

## 安装 AP 板

### 步骤 1：安装 AP 板

在新的 AP 板背面的屏蔽罩表面涂布散热硅脂。  
![apply_grease.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/apply_grease.png)

将 AP 板底部的缺口对准横梁上的插槽，然后将 AP 板推入横梁中，使用 H2.0 内六角扳手拧紧四颗固定螺丝（M3x4.5）。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/05_005.png)

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/06_006.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/02_002.png)

依次将 AP 板上的连接线依次重新连接。

- 屏幕排线和摄像头排线需将线缆插入接头中，然后扣上卡扣；
- 其他线缆将插入直接插入，确保完全插到位即可。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/01_001.png)

### 步骤 2：安装 AP 板盖

沿着安装槽将 AP 板盖拖链一侧推到位（可使用内六角扳手确认螺丝孔对齐），在推动 AP 板的时候，请用手扶着 AP 板盖左侧，并将左侧的卡扣卡入框架中。

|  |  |
| --- | --- |
|  |  |

将 LED 补光灯 - 左的连接线插入 AP 板，并将检修端扣紧。

![led_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/led_001.png)

![ap3_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap3_007.png)

使用 H1.5 内六角扳锁紧 2 颗螺丝（BT2x8）。

![ap_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board-cover-and-led-light-left/ap_002.png)

### 步骤 3：安装料管支架

请参考 [更换料管支架](replace-ptfe-tube-bracket.md) 的指引，将料管支架重新装回。  
![ptfe_tube_bracket_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/ptfe_tube_bracket_002.png)

### 步骤 4：绑定新序列号（SN）

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 如何验证成功

连接电源，打开打印机，检查是否可以正常发起打印。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
