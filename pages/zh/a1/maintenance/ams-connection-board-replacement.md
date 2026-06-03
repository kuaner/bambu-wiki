---
path: zh/a1/maintenance/ams-connection-board-replacement
title: "A1 AMS 接口板更换指南"
description: "本指南提供更换 AMS 接口板的详细步骤。"
tags: ["a1"]
created: 2025-09-25T02:50:32.124Z
updated: 2025-12-24T12:18:39.725Z
source: https://wiki.bambulab.com/zh/a1/maintenance/ams-connection-board-replacement
---

## AMS 接口板

AMS 接口板是安装在 A1 打印机底座上的一块电路板，它为 AMS 提供 24V 的直流电源，并处理 AMS 和打印机之间的通信连接。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/1.ams_接口板.png)

## 何时更换

AMS 接口板的电源输出不正常，AMS 出现电源或通信故障时，有很大可能需要更换 AMS 接口板。

## 所需工具和材料

- 一块新的 AMS 接口板
- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> ***❗❗ 重要提醒***
>
> *在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。*
>
> *在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。*
>
> *如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。*

## 拆卸步骤

### 步骤 1 ：关闭电源，取下电源线

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/2.1关闭电源.png)

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/2.2拔下电源线.png)

### 步骤 2 ：移除 AMS lite

按紧线缆接口底端，断开 AMS lite 的 4-pin 线。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/3.1拔下ams_lite连接线.png)

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/3.2_ams_lite连接线.png)

### 步骤 3 ：移除后底盖

用 H2.0 内六角扳手拧下 6 颗红色标记螺丝，移除后底盖。

![](https://wiki.bambulab.com/a1/4.1_底座.jpg)

### 步骤 4 ：取下 AMS 接口板

1. 断开连接电缆。
2. 用 H1.5 内六角扳手移除 2 颗螺丝。
3. 取下 AMS 接口板。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/5.2_拧下两颗螺丝.png)

## 安装步骤

### 步骤 1 ：安装 AMS 接口板

1. 确认对齐位置后，将新的 AMS 接口板装入，略微用力按压直至完全到位，然后再插上连接电缆。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/6.2安装ams接口板（2）.png)

- 用 H1.5 内六角扳手锁紧 2 颗螺丝进行固定。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/7.拧紧两颗螺丝.png)

### 步骤 2 ：装回后底盖

1. 确认对齐位置后，用力按压，听到咔哒声即安装到位。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/8_装回后底盖.jpg)

- 用 H2.0 内六角扳手锁紧 6 颗螺丝进行固定。

![](https://wiki.bambulab.com/a1/4.1_底座.jpg)

## 验证功能

连接电源线并启动电源。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/10.1_验证功能（打开电源）.jpg)

在显示屏上，点击“**耗材**”，如下所示，屏幕将显示 AMS 控制面板。按下“**进料**”按钮开始进料，如果该过程没有任何错误地完成，AMS 接口板更换完成并成功。

![](https://wiki.bambulab.com/a1/maintenance/ams-connection-board-replacement/10.2验证功能（显示屏）.jpg)

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
