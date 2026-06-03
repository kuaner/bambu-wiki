---
path: zh/p2s/maintenance/install-auxiliary-part-cooling-fan-left
title: "加装 P2S 辅助部件冷却风扇"
description: "本文介绍了如何为 P2S 加装辅助部件冷却风扇。"
tags: []
created: 2025-10-14T13:15:15.239Z
updated: 2026-03-11T06:07:25.432Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/install-auxiliary-part-cooling-fan-left
---

## 辅助部件冷却风扇 （左）

辅助部件冷却风扇（左）是一个强大的 12W 冷却风扇，属于选配的配件，它安装在腔室的左侧，为高速打印提供了更好的冷却条件。

## 何时更换

- 叶片损坏；
- 风扇电机故障；
- 风扇异响

## 所需的工具和材料

1. 辅助部件冷却风扇（左）
2. H2.0 内六角扳手

> **重要提醒：**  
> 首批准备的辅助部件冷却风扇（左），所赠送的螺丝偏长，用力拧到底会导致侧板有凸起。在安装时，请将螺丝拧至与硅胶刚好接触的状态即可，风扇本身贴附有双面胶，可以保证固定效果。

|  |  |
| --- | --- |
|  |  |

![screw_view.png](https://wiki.bambulab.com/p2s/maintenance/aux_part_cooling_fan/screw_view.png)

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 加装辅助部件冷却风扇

### 步骤 1：下降热床

倾斜打印机，拉动 Z 轴皮带，下降热床，将安装辅助部件冷却风扇（左）的位置完全显露出来。

|  |  |
| --- | --- |
|  |  |

### 步骤 2：移除背板

您可以参考这篇 Wiki 来移除背板： [更换 P2S 背板](replace-rear-panel.md)  
![rear_panel_removed_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/adaptive_airflow_switching_unit/rear_panel_removed_003.png)

### 步骤 3：安装辅助部件冷却风扇

1. 撕掉风扇上的双面胶保护纸；

![tear_off.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/tear_off.png)

2. 根据螺柱位将风扇安装到位，使用 H2.0 内六角板搜拧入三颗螺丝。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/01_001.png)  
![screw_view.png](https://wiki.bambulab.com/p2s/maintenance/aux_part_cooling_fan/screw_view.png)

### 步骤 4：连接风扇电缆

1. 将风扇电缆穿过侧面板和内搁板之间的间隙；

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/02_002.png)

2. 将电缆与 MC 板连接；

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/03_003.png)

3. 整理线缆：从 MC 板一侧拉动线缆，然后将线缆贴住横梁。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/04_004.png)

### 步骤 5：安装背板

您可以参考这篇 Wiki 将背板重新装回：[更换 P2S 背板](replace-rear-panel.md)

## 移除辅助部件冷却风扇

### 步骤 1：下降热床

倾斜打印机，拉动 Z 轴皮带，下降热床，将辅助部件冷却风扇完全显露出来。

### 步骤 2：移除背板

您可以参考这篇 Wiki 来移除背板： [更换 P2S 背板](replace-rear-panel.md)

### 步骤 3：断开辅助部件冷却风扇线缆

在 MC 板上将辅助部件冷却风扇连接线断开连接。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/03_003.png)

### 步骤 4：移除辅助部件冷却风扇

1. 使用 H2.0 内六角扳手移除三颗风扇固定螺丝；

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/01_001.png)

2. 然后用力将还有双面胶固定的风扇与侧板分离。

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/06_006.png)

3. 将风扇电缆拉出，取下辅助部件冷却风扇。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/install-auxiliary-part-cooling-fan-left/05_005.png)

## 如何验证成功

连接电源线并开启电源，在屏幕上点击辅助部件冷却风扇图标，开启辅助部件冷却风扇。如果辅助部件冷却风扇按预期工作，那么更换完成。

如果您遇到任何问题，请先回溯您的步骤并检查线缆是否连接正常，然后再次检查是否可以正常使用。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（工作日 9:00-21:00；节假日 9:00-18:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
