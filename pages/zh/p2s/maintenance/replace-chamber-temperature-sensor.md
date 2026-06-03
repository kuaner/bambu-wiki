---
path: zh/p2s/maintenance/replace-chamber-temperature-sensor
title: "更换 P2S 腔温检测传感器"
description: "本文介绍了如何更换 P2S 腔温检测传感器"
tags: []
created: 2025-10-14T12:55:35.158Z
updated: 2025-10-14T12:55:36.387Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-chamber-temperature-sensor
---

## 腔温检测传感器

腔温检测传感器是安装在打印机前横梁内侧，用于检测打印机腔内温度的带固定支架 NTC 。

配件包装内包含：

1. 腔温检测传感器 \* 1
2. BT3x6 螺丝 \* 2

## 何时更换

1. 腔温检测传感器连接线损坏；
2. 腔温报错。

## 工具和材料

1. 新的腔温检测传感器
2. H2.0 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除腔温检测传感器

### 第 1 步 - 断开连接线缆

打开 AP 板盖检修端，从 AP 板上断开腔温检测传感器的连接线。

![01_open_the_service_end_of_the_ap_board_cover_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-led-light-front/01_open_the_service_end_of_the_ap_board_cover_001.png)  
![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/01_001.png)

### 第 2 步 - 移除腔温检测传感器

在前横梁内侧找到腔温检测传感器，使用 H2.0 内六角扳手移除两颗腔温检测传感器固定螺丝（BT3x6），然后即可移除腔温检测传感器。  
![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/03_003.png)  
![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/05_005.png)

## 安装腔温检测传感器

### 第 1 步 - 安装腔温检测传感器

将新的腔温检测传感器与打印机横梁上的螺丝孔位对齐，使用 H2.0 内六角扳手拧紧两颗固定螺丝（BT3x6）。

> 在拧第一颗螺丝时请用手扶住腔温检测传感器，并在两颗螺丝都拧上后再统一锁紧。

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/02_002.png)

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/03_003.png)

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/05_005.png)

### 第 2 步 - 连接线缆

将腔温检测传感器线缆沿着横梁穿至 AP 板一侧，将连接线与 AP 板连接，并将 AP 板盖检修端重新扣紧。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/04_004.png)

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-chamber-temperature-sensor/01_001.png)

![01_open_the_service_end_of_the_ap_board_cover_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-led-light-front/01_open_the_service_end_of_the_ap_board_cover_001.png)

## 如何验证成功

连接电源并打开打印机，检查打印机腔温是否显示正常。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（工作日 9:00-21:00；节假日 9:00-18:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
