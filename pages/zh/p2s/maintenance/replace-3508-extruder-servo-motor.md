---
path: zh/p2s/maintenance/replace-3508-extruder-servo-motor
title: "更换 P2S 挤出电机"
description: "本文介绍如何更换  P2S 的挤出电机"
tags: []
created: 2025-10-14T12:49:59.135Z
updated: 2026-04-13T02:22:40.655Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-3508-extruder-servo-motor
---

## 挤出电机

P2S 使用的挤出电机是拓竹自研的高精度伺服电机，它能精确控制耗材的进给、停止和回抽，是保证打印质量和成功率的关键部件。  
![fam018_1.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fam018_1.jpg)  
配件包装内包含挤出电机和固定螺丝

1. X3508 挤出电机 \* 1；
2. M2.5x5 螺丝 \* 2

## 何时更换

挤出电机损坏，无法运转。

## 所需的工具和材料

1. 新的 X3508 挤出电机
2. M2.5x5 螺丝 \* 2
3. H2.0 内六角扳手
4. H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除挤出电机

### 步骤 1：移除工具头外壳

请参考 [更换工具头外壳](replace-toolhead-housing.md) 这篇WIKI，将工具头的外壳拆除。

![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

### 步骤 2：移除挤出机

请参考 [更换挤出机配件](replace-extruder-components.md) 这篇WIKI，移除挤出机。  
![remove_extruder_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-3508-extruder-servo-motor/remove_extruder_003.png)

### 步骤 3：移除 TH 板

请参考 [更换工具头电路板](replace-th-boards-and-fpc-cable.md) 这篇WIKI，移除 TH 板。  
![th_board_removed_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-3508-extruder-servo-motor/th_board_removed_004.png)

### 步骤 4：移除挤出电机

使用 H2.0 内六角扳手移除两颗挤出电机固定螺丝（M2.5x5），然后将挤出电机从工具头上取出。

|  |  |
| --- | --- |
|  |  |

## 安装挤出电机

### 步骤 1：安装挤出电机

参考下图的安装方向（挤出电机连接线朝左），将挤出电机安装至工具头上。然后使用 H2.0 内六角扳手拧紧两颗挤出电机固定螺丝（M2.5x5）。

**注：请用手按住挤出电机，防止挤出电机掉落。**

|  |  |
| --- | --- |
|  |  |

### 步骤 2：安装 TH 板

请参考 [更换工具头电路板](replace-th-boards-and-fpc-cable.md) 这篇WIKI，安装 TH 板。  
![th_board_installed_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-3508-extruder-servo-motor/th_board_installed_005.png)

### 步骤 3：安装挤出机

请参考 [更换挤出机配件](replace-extruder-components.md) 这篇WIKI，安装挤出机。  
![extruder_installed_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-3508-extruder-servo-motor/extruder_installed_004.png)

### 步骤 4：安装工具头外壳

参考 [更换工具头外壳](replace-toolhead-housing.md) 的内容，安装好工具头外壳。  
![close_front_cover_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/close_front_cover_002.png)

## 如何验证成功

连接电源，打开打印机，检查挤出机是否可以正常挤出。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
