---
path: zh/h2/maintenance/replace-usb-c-cable
title: "更换 H2D & H2C USB-C 数据线"
description: "本文介绍了如何更换 H2D & H2C USB-C 数据线"
tags: []
created: 2025-03-25T02:22:33.836Z
updated: 2026-03-13T03:19:30.136Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-usb-c-cable
---

## USB-C 数据线

USB-C 数据线用于连接 TH 板和 AP 板。

|  |  |
| --- | --- |
| 新版数据线（左侧变为 L 型接口） | 旧版数据线 |

**USB-C 数据线的备件包含以下：**

1. USB-C 数据线 \* 1

## 何时更换

- USB-C 数据线损坏；
- 经过 Bambu Lab 官方技术支持确认需要更换。

## 所需的工具和材料

- 新的 USB-C 数据线
- H2.0 内六角扳手
- H1.5 内六角扳手

**更换 H2D USB-C 数据线所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定部件冷却风扇风道 |  |  |  | 4 |
|  |  | 用于固定缓冲器 |  |  |  | 4 |
| BT2.6x8 |  | 用于固定部件冷却风扇 |  |  |  | 2 |
|  |  | 用于固定 TH 板 |  |  |  | 2 |
|  |  | 用于固定 AP 板盖 |  |  |  | 1 |
| BT3x20 |  | 用于固定部件冷却风扇 |  |  |  | 2 |
| M1.6x4 |  | 用于固定挤出接口板 |  |  |  | 2 |
| BT2.6x8 |  | 用于固定 TH 板 |  |  |  | 2 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除 USB-C 数据线

### 步骤 1：移除 TH 板

由于 USB-C 线连接在 TH 板的背面，因此您需要先将 TH 板松开，然后才能将 USB-C 线从 TH 板上拔出。您可以参考这篇 Wiki 来移除 TH 板，您仅需参考到 TH 板与 USB-C 线缆断开连接的步骤即可。

[更换 H2D 挤出接口板/TH 板/FPC 排线](replace-H2D-TH-board.md)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image.png)

### 步骤 2：移除 AP 板盖

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-1.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-2.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-3.png)

### 步骤 3：移除缓冲器

按住料管支架上的气动接头，移除与打印机背面连接的两根 PTFE 管，使用 H2.0 内六角扳手移除四颗固定螺丝（BT3x8），将缓冲器松开后即可看见缓冲器下面的 USB-C 数据线。

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-26.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/img_v3_02jk_c4cc88a6-9a52-4dcf-b74a-b83026f4ef3g.jpg)

### 步骤 4：移除 USB-C 数据线

1. 从 AP 板上将 USB-C 数据线断开连接，然后将 USB-C 数据线从上盖的线扣中取出；

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-25.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-24.png)

- 将拖链上的线扣取下，然后将拖链从上盖上取下，将 USB-C 数据线从拖链中取出。

> 注：如果 USB-C 数据线被压在 TH 板自带的线缆下方，您可以将这两根线缆一起从拖链中取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-22.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-15.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-16.png)

## 安装 USB-C 数据线

### 步骤 1：连接 AP 板

将新的 USB-C 数据线与 AP 板连接，然后将线缆依次卡入线扣中。

> 注意：A 字这一头与 AP 板连接，并且 A 字朝外！

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-17.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-18.png)

### 步骤 2：安装 USB-C 线缆和拖链

1. 将 USB-C 数据线和 MC-TH 线缆继续装入拖链中，将线缆装入拖链的一半即可，以便于可以将两个拖链卡扣都安装在拖链上，同时可以留有一定的空间，便于与 TH 板连接。然后将拖链尾部装入上盖中；

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-19.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/img_v3_02ip_bf08e9d1-94a8-4b62-b4b1-869308e1fd6g.jpg)

- 将 USB-C 数据线与 TH 板连接。

> 注意：请参考此图的方向，T 字朝外！！

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/img_v3_02ip_bbbddca6-ad93-4543-8846-2e0dd0b9305g.jpg)

- 转动拖链底座，将缺口与工具头中框上的缺口对齐，将 MC-TH 线缆和 USB-C 数据线扣入拖链底座和工具头中框；

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-20.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-21.png)

- 将剩余的 MC-TH 电源通讯转接线和 USB-C 数据线装入拖链中，将拖链与拖链底座重新连接，并将卡扣扣回拖链上（分别安装在第 8 和第 18 节拖链上 —— 从工具头开始数）；

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-38.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-37.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-36.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-39.png)

### 步骤 3：安装 TH 板

您可以参考这篇 Wiki 来将 TH 板重新安装至工具头上：

[更换 H2D 挤出接口板/TH 板/FPC 排线](replace-H2D-TH-board.md)

### 步骤 4：安装缓冲器

将缓冲对准螺丝孔位后，使用 H2.0 内六角扳手拧紧四颗固定螺丝（BT3×8），最后重新将两根 PTFE 管与缓冲器连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-40.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/img_v3_02jg_890a6a92-b160-46f5-84d0-f3e670cee9fg.jpg)

### 步骤 5：安装 AP 板盖

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-27.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-usb-c-cable/image-28.png)

## 如何验证成功

连接电源并打开打印机，发起打印无报错即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
