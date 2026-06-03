---
path: zh/p2s/maintenance/replace-door-sensor
title: "更换 P2S/X2D  开门检测开关"
description: "本文介绍了如何更换 P2S/X2D  开门检测开关"
tags: []
created: 2025-10-14T12:50:23.214Z
updated: 2026-04-21T02:50:42.970Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-door-sensor
---

## 开门检测开关

开门检测开关是安装在打印机前立柱内侧的一块小尺寸电路板，用于检查玻璃前门的开合状态。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac161.jpg)  
**配件包装内包含：**

1. 开门检测开关 \* 1；
2. ST2x3.5 螺丝 \* 1

注：配件内不包含连接线，如果发现线缆损坏，需要准备**打印机线材包**进行线缆更换。

## 何时更换

- 开门检测功能失效或一直提示前门打开，且连接线缆无明显损伤。

## 工具和材料

1. 新的开门检测开关
2. H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 检查前门提手的磁铁

### 第 1 步 - 移除前门提手

打开前门，用 H2.0 内六角扳手移除固定前门提手的 2 颗螺丝，提手会自然脱落。  
![2_screws_002.png](https://wiki.bambulab.com/p2s/maintenance/replace-front-glass-door-handle/2_screws_002.png)

### 第 2 步 - 检查磁铁是否完好

如果方形磁铁遗失或因为前门提手损坏而无法被固定住，请更换新的前门提手。  
![remove_the_handle_003.png](https://wiki.bambulab.com/p2s/maintenance/replace-front-glass-door-handle/remove_the_handle_003.png)

## 移除开门检测开关

打开玻璃前面，在右侧门框上找到检测开关，使用 H1.5 内六角扳手移除一颗螺丝（ST2x3.5）。

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/02_002.png)

揭开检测开关处硅胶条，撕下黑色胶布。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/03_003.png)

按住线缆接头的卡扣，断开连接线，取下前门检测开关。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/04_004.png)

## 安装开门检测开关

将线缆连接到前门检测开关的连接器上。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/05_005.png)

将前门检测开关上的螺丝孔与前立柱内侧的螺丝孔对齐，使用 H1.5 内六角扳手拧紧一颗固定螺丝（ST2x3.5）。

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/07_007.png)

揭开检测开关处的硅胶条，重新贴上黑色胶布。

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/08_008.png)

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-door-sensor/09_009.png)

## 如何验证成功

由于前门检测功能要在工作状态下才生效，可以在有打印任务时进行确认。  
在打印机打印过程中，打开并关闭玻璃前门，确认开门提示在打开门时有弹出，并在关上前门后消失。

如果您遇到任何问题，请先回溯您操作的步骤确认开门检测开关的连接线是否连接正常，并确认缆线是否有破损，没问题后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
