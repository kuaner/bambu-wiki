---
path: zh/h2d-pro/maintenance/replace-wifi-antenna
title: "更换 H2D Pro WiFi 天线"
description: "本文介绍了如何更换 H2D Pro WiFi 天线"
tags: []
created: 2025-08-08T04:15:40.230Z
updated: 2025-08-11T11:59:44.141Z
source: https://wiki.bambulab.com/zh/h2d-pro/maintenance/replace-wifi-antenna
---

## WiFi 天线

WiFi 天线安装在 H2D Pro上框盖中，是用于增强无线网络信号的电子配件。

**WiFi 天线的备件包含：**

- WiFi 天线

## 何时更换

- WiFi 天线损坏
- WiFi 信号不稳定或较弱

## 所需的工具和材料

- 新的 WiFi 天线
- H2.0 内六角扳手

**更换 H2D WiFi 天线所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT2x12 |  | 用于固定前面盖 | front_cover_screw_001.png |  | 1 |
| BT2.6x8 |  | 用于固定 AP 板盖 | ap_board_screw_001.png |  | 1 |

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)，我们将及时回复并为您提供所需的帮助。

## 移除 WiFi 天线

### 步骤 1：移除前面盖

您可以参考这篇 Wiki 来移除前面盖，将前面盖拆下后您无需继续将前面盖和屏幕分离。

[更换 H2D 前面盖](../../h2/maintenance/replace-front-cover.md)

### 步骤 2：松开无线网口板并断开 WiFi 天线插头

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT3×5）;

![remove_one_screw_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/remove_one_screw_001.png)

2. 翻转无线网口板；

> 注意，翻转时请勿大力拉扯，以免损坏 WiFi 天线。

![turn_the_board_over_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/turn_the_board_over_001.webp)

3. 断开 WiFi 天线插头。

![disconnect_wifi_connector_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/disconnect_wifi_connector_001.webp)

### 步骤 3：取下 WiFi 天线

将 WiFi 天线依次从胶布和线扣中取出。

[](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-wifi-antenna/remove_wifi_antenna_1_003.mp4)

![wifi_antenna_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-wifi-antenna/wifi_antenna_001.png)

您需要按住线扣一侧，然后拿出 WiFi 天线线缆，从线扣的缝隙中取出，并将 WiFi 天线从前面盖上撕下即可移除。

[](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-wifi-antenna/remove_wifi_antenna_2_001.mp4)

## 安装 WiFi 天线

### 步骤 1：装回 WiFi 天线

1. 将新 WiFi 天线的背胶撕下，将 WiFi 天线线缆依次扣入线扣中；

[](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-wifi-antenna/install_wifi_antenna_1_001.mp4)

2. 然后将 WiFi 天线参考原位置贴回。

[](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/maintenance/replace-wifi-antenna/install_wifi_antenna_2_001.mp4)

### 步骤 2：连接WiFi天线插头，并装回无线网口板

1. 压入 WiFi 天线插头。

![connect_wifi_connector_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/connect_wifi_connector_001.webp)

2. 连接 WiFi 天线插头后，翻转无线网口板，利用定位槽和定位螺丝孔，将无线网口板安装到位。

![turn_the_board_over_for_installation_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/turn_the_board_over_for_installation_001.webp)

![install_the_borad_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/install_the_borad_001.webp)

3. 检查无线网口板附近的走线，确保无线网口板的塑料边框没有压住周边线缆后，锁入 1 颗固定螺丝。

![install_one_screw_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/install_one_screw_001.png)

### 步骤 3：装回前面盖

您可以参考这篇 Wiki 来安装前面盖：

[更换 H2D 前面盖](../../h2/maintenance/replace-front-cover.md)

## 如何验证完成/成功

打开打印机电源，将打印机连接到网络点击测速，确认功能是否正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
