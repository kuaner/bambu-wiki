---
path: zh/p1/maintenance/wifi-antenna
title: "更换WIFI天线"
description: "拆装P1P打印机WIFI天线的操作步骤"
tags: []
created: 2023-06-02T03:32:02.967Z
updated: 2024-10-24T02:12:55.059Z
source: https://wiki.bambulab.com/zh/p1/maintenance/wifi-antenna
---

## WIFI 天线

WIFI 天线是用于增强无线网络信号电子配件，P1 系列打印机的 WIFI 天线安装在前面盖内侧并连接至 AP 主板。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/wifi.jpg)

检索关键字：

更换 WIFI 天线、P1P WIFI 天线

## 何时更换

1. WIFI 天线线缆或连接器损坏。

2. WIFI 信号不稳定或较弱，且 Bambu Lab 服务团队通过 log 分析确认是 WIFI 天线的问题。

## 工具和材料

- 新的 WIFI 天线
- H2.0/H1.5 内六角扳手
- 镊子
- 螺丝刀

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 拆除旧 WIFI 天线

### **步骤 1. 移除屏幕、前面盖**

参考 [屏幕组件](screen.md)  和 [前面盖](front-cover.md) 的相关内容，移除屏幕和前面盖。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/front_cover_removed.jpg)

### 步骤 2. 移除密封泡棉

用手移除密封泡棉，注意不要过于用力，避免损坏 AP 主板上的元器件。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/foam.jpg)

### **步骤 3.** 移除螺丝

1. **断电后，可直接用螺丝刀翘起 WIFI 天线**，断开连接。
2. 用 H2.0 内六角扳手移除 4 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/1_connector_4_screws.jpg)

### **步骤 4.** 移除 WIFI 天线

将 AP 主板从横梁中松出，取下 WIFI 天线。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/remove_the_wifi_antenna.jpg)

## 安装新的 WIFI 天线

### **步骤 1. 穿 WIFI 天线**

将 WIFI 天线穿过过线孔。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/install_the_wifi_antenna.jpg)

### 步骤 2. 安装 AP 主板

根据 AP 主板上的安装槽，安装 AP 主板，注意避让 WIFI 天线电缆。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/install_the_ap_board1.jpg)

### **步骤 3.** 锁螺丝固定

锁入 4 颗螺丝，连接好 WIFI 天线。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/1_connector_4_screws.jpg)

### **步骤 4.** 贴附密封泡棉

将密封泡棉贴附好。

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/foam.jpg)

### 步骤 5. 安装前面盖、屏幕

参考  [前面盖](front-cover.md) 和  [屏幕组件](screen.md) 的相关内容，安装前面盖和屏幕。

![](https://wiki.bambulab.com/p1/maintenance/front-cover/display_installed.jpg)

## 功能确认

打开打印机电源，按绑定打印的流程操作一次设备绑定，能正常绑定打印机，则说明 WIFI 信号正常。

否则，请再次检查所有连接并重试。如果仍然不行，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
