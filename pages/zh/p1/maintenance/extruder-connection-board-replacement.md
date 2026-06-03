---
path: zh/p1/maintenance/extruder-connection-board-replacement
title: "更换P1系列挤出接口板"
description: "本指南介绍如何更换 P1系列打印机上的挤出接口板。"
tags: []
created: 2025-07-30T08:11:59.165Z
updated: 2026-02-11T08:50:06.611Z
source: https://wiki.bambulab.com/zh/p1/maintenance/extruder-connection-board-replacement
---

## 挤出接口板-P1

![p1挤出接口板.jpg](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/p1%E6%8C%A4%E5%87%BA%E6%8E%A5%E5%8F%A3%E6%9D%BF.jpg)

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 工具

- 新的挤出接口板
- H1.5 内六角扳手

## 准备工作

已完成退料，**关闭电源**。

> **警告**：请确保所有热端/工具头的更换操作均在**断电状态**下进行。在电源开启时拔插任何连接器可能导致短路，从而对工具头电路板造成**永久性损坏**。

## 拆除步骤

### **第 1 步** 移除工具头前壳组件

如图所示，从工具头的下方两侧握住前壳，然后轻轻拉出。此时外壳仍通过冷却风扇线缆与机体相连。

![toolhead_cover_removal.jpg](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/toolhead_cover_removal.jpg)

拔下黑色的冷却风扇线缆，分离前壳，将前壳放到一旁备用。

![toolhead_cover_fan_connector_removal.jpg](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/toolhead_cover_fan_connector_removal.jpg)

### **第 2 步 -** 移除接口板

移除接口板前，首先要断开连接在板子上的连接器，接口板上有四个连接器，如下图所示。

![extruder_connection_board_annotated.png](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_connection_board_annotated.png)

1. FPC 排线（连接挤出机接线板与 TH 板）
2. 霍尔开关排线
3. 热端风扇线
4. 热端加热器热敏电阻线

接下来，断开上面提到的四个连接器。

热敏电阻线和热端风扇线（底部两个）可以使用与冷却风扇连接器相同的方法断开。

![nozzle_connector_removal.jpg](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/nozzle_connector_removal.jpg)

FPC 排线（1）和霍尔开关排线（2）可按照下图所示的方法，从连接器上与排线相反的一侧轻轻撬起进行断开。

![extruder_connection_board_connector_removal_1.png](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_connection_board_connector_removal_1.png)

断开所有连接后，小心地将风扇线（3）和热端传感器线（4）从理线夹中取出，以便将它们移到一旁。

![extruder_board_wires_removed_from_routing.jpg](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_board_wires_removed_from_routing.jpg)

然后使用 H1.5 内六角扳手拆下两颗螺丝并取下接口板。轻轻地将电路板左右晃动并取出。

![extruder_connection_board_screw_removal.png](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_connection_board_screw_removal.png)

## 安装步骤

### **第 1 步 -** 安装挤出接口板

在安装新的接口板时，请注意下图所示的两个定位孔，确保不要夹到连接板后方的松散导线或接头。请特别注意下方动图中的安装角度和位置，避免夹到后方松散的线缆。

将连接板从左侧以轻微倾斜的角度插入。然后将连接板压平贴合在工具头上，轻轻晃动并向右移动，使其越过右上方的定位销（该定位销位于工具头外壳磁铁的后方）。

下方的动图演示了如何将连接板正确安装到定位销上。

![extruder_board_placement.gif](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_board_placement.gif)

对准后，重新安装两颗螺丝。

![extruder_connection_board_screw_removal.png](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_connection_board_screw_removal.png)

### **第 2 步 -** 重新连接线缆

在对齐连接器时，请小心地将它们对准，小心推入。切勿用力强行将连接器压入插座，如遇阻力，如果不能顺利插入，请重新对齐后再轻轻尝试。

先重新连接底部的热端加热器热敏电阻连接器，然后连接其上方的热端风扇连接器。接着，重新连接顶部的排线连接器。

> 请注意：排线连接器正确对齐时，两端应齐平，中间有约 1 毫米间隙，如下图所示。

![extruder_connection_board_ribbon_connector_gap.png](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/extruder_connection_board_ribbon_connector_gap.png)

### **第 3 步 -** 安装工具头前壳组件

将风扇线缆重新连接到挤出机连接板，然后对齐上角位置，利用磁吸将前壳复位安装。

|  |  |
| --- | --- |
|  |  |

安装步骤在下面动图也有展示：

![attach_front_cover_a65a7d0c23.gif](https://wiki.bambulab.com/p1/maintenance/extruder-connection-board/attach_front_cover_a65a7d0c23.gif)

## 如何验证完成

1. 目视检查挤出机连接板的安装位置以及各连接器是否牢固、对齐无误。

2. 启动打印机，运行设备校准流程，如果校准过程顺利通过，说明操作成功。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/calibration2.jpg)|

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
