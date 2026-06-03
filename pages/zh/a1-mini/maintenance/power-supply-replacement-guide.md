---
path: zh/a1-mini/maintenance/power-supply-replacement-guide
title: "A1 mini 电源更换指南"
description: "本指南介绍如何更换 A1 mini 打印机电源模块"
tags: ["a1 mini"]
created: 2025-02-21T07:38:44.445Z
updated: 2025-02-25T08:32:39.816Z
source: https://wiki.bambulab.com/zh/a1-mini/maintenance/power-supply-replacement-guide
---

## 电源模块

本指南中，我们将展示 A1 mini 电源模块的更换过程。

![](https://wiki.bambulab.com/a1m/power-supply/a1_mini_power_supply.jpg)

## 何时使用

- 打印机无法开机
- 拓竹技术支持建议更换

## 所需工具和材料

- 新的电源模块
- H2.0 内六角扳手
- PH2 十字螺丝刀
- 20 分钟

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除步骤

### 1. 移除打印机底盖

将打印机正面朝下放置，方便操作打印机底部。

卸下固定底盖的 16 颗螺丝。**请注意区分螺丝 15 和 16**，在重装底盖时需避免混淆。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_bottom_cover_screws_for_a1_mini.jpeg)

卸下螺丝后，可轻轻撬出底盖。

### 2. 移除塑料卡扣

小心取下固定塑料卡扣的 3 颗螺丝。注意 3 号螺丝位于侧面。

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_plastic_wire_cover.jpeg)

### 3. 松开电源端子

如下图所示，松开电源模块端子；  
只需松开即可移除线缆，不用完全移除，方便后续收纳。

![](https://wiki.bambulab.com/a1m/power-supply/loosen_the_power_supply_terminal_screws.jpeg)

### 4. 移除电源螺丝

移除电源的 3 个螺丝。注意 3 号螺丝位于侧面。

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_3_power_supply_screws.jpeg)

### 5. 移除电源

从右侧握住电源，断开左侧的电源模块端子，小心将电源拉出，确保不要损坏或断开周围的任何线缆。

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_power_supply.jpeg)

## 安装步骤

### 1. 安装新的电源模块

轻轻将电源左侧插入，确保不要损坏电源周围的任何电线。

![](https://wiki.bambulab.com/a1m/power-supply/insert_the_power_supply.jpeg)

### 2. 重新连接电源模块线缆

小心地重新连接电源端子线缆，如下所示，并**拧紧螺丝。**

1. 交流火线  
2. 交流零线  
3. 地线  
4. -V 主线负极线缆  
5. +V 主板正极线缆

![](https://wiki.bambulab.com/a1m/power-supply/loosen_the_power_supply_terminal_screws.jpeg)

> 注意：如上图所示接好全部线缆之后，确保线缆接头固定到位且没有松动。

### 3. 安装电源螺丝

将 3 个电源螺丝拧入塑料卡扣内。**避免过度拧紧，否则可能会损坏塑料螺纹。**

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_3_power_supply_screws.jpeg)

### 4. 安装塑料卡扣的固定螺丝

按照图中所示排列热床电缆和电源线，然后将 3 个螺丝拧入塑料卡扣内。**避免过度拧紧，否则可能会损坏塑料螺纹。**

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_plastic_wire_cover.jpeg)

### 5. 整理线缆

安装底盖前，请确保 MC 板线路布线正确，以免干扰 MC 板风扇，如下图所示。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/a1_mini_board_and_wire_managemet.jpg)

### 6. 安装后盖

首先拧紧螺丝 15 和 16，然后继续安装其他螺丝，同时避免拧得太紧。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_bottom_cover_screws_for_a1_mini.jpeg)

## 功能验证

为了确保打印机可以正常工作，完成所有安装后可以通电并打开电源开关测试；  
打印机可正常开机并点亮显示屏，则表明安装正确。

## 潜在问题和解决方案

如果您在安装新电源时遇到问题，请检查下列潜在问题和解决方案：

### 打印机无法开机

确认电源线安装正确，如[步骤2](#step2) ，重新连接主板电源端子线缆。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
