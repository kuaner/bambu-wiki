---
path: zh/h2d-pro/maintenance/replace-wireless-network-board
title: "更换 H2D Pro 无线网口板"
description: "本文介绍了如何更换 H2D Pro 无线网口板"
tags: []
created: 2025-08-08T03:58:31.906Z
updated: 2025-08-11T11:58:05.647Z
source: https://wiki.bambulab.com/zh/h2d-pro/maintenance/replace-wireless-network-board
---

## 无线网口板

无线网口板通过 Wi-Fi 技术实现打印机主板与电脑、手机的远程连接。通过无线的方式实现打印机 G-code 文件传输、实时监控打印状态、升级等功能。该方式优势在于灵活部署。

![wireless_network_board_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/wireless_network_board_001.png)

无线网口板的备件包含如下：

1. 无线网口板及其排线\* 1
2. BT3x5 螺丝 - 用于固定 无线网口板 \* 1

## 何时更换

需要联系 Bambu Lab 技术支持来确定打印机已出现的问题是否源于无线网口板。

## 所需的工具和材料

1. 新的无线网口板
2. H2.0 内六角扳手

**更换 H2D 无线网口板所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT2.6x8 |  | 用于固定 AP 板盖 |  |  | 1 |
| BT3x5 |  | 用于固定无线网口板 |  |  | 1 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)，我们将及时回复并为您提供所需的帮助。

## 移除无线网口板

### 步骤 1：关闭电源

关闭打印机电源后拔下电源线，并取下上盖玻璃。

### 步骤 2：取下 AP 板盖

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），打开 AP 板盖；

> 您可以参考[这篇 wiki](../../h2/maintenance/replace-x-axis-assembly.md) 中的拆除 AP 板盖相关部分视频步骤来进行操作。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-5_031.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-4_030.png)

2. 从靠近前门的一侧取下 AP 板盖。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-3_023.png)

### 步骤 3：断开 AP 板上的无线网口板插头

打开卡扣，拔下 AP 板上的无线网口插头。

![unplug_002.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/unplug_002.webp)

### 步骤 4：取下无线网口板

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT3×5）;

![remove_one_screw_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/remove_one_screw_001.png)

2. 翻转无线网口板；

> 注意，翻转时请勿大力拉扯，以免损坏 WiFi 天线。

![turn_the_board_over_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/turn_the_board_over_001.webp)

3. 断开 WiFi 天线插头。

![disconnect_wifi_connector_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/disconnect_wifi_connector_001.webp)

## 安装无线网口板

### 步骤 1：安装无线网口板

1. 压入 WiFi 天线插头。

![connect_wifi_connector_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/connect_wifi_connector_001.webp)

2. 连接 WiFi 天线插头后，翻转无线网口板，利用定位槽和定位螺丝孔，将无线网口板安装到位。

![turn_the_board_over_for_installation_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/turn_the_board_over_for_installation_001.webp)

![install_the_borad_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/install_the_borad_001.webp)

3. 检查无线网口板附近的走线，确保无线网口板的塑料边框没有压住周边线缆后，锁入 1 颗固定螺丝。

![install_one_screw_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/install_one_screw_001.png)

### 步骤 2：连接 AP 板上的无线网口板插头

插回排线，扣好卡扣。请注意，排线左右两边的小耳朵需要嵌入插座中，扣好卡扣后，卡扣平整且没有一边翘起来。

![insert_the_cable_back_001.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/insert_the_cable_back_001.webp)

### 步骤 3：装回 AP 板盖

> 注意：安装 AP 板盖前，需检查线缆是否阻碍 PTFE 管路，避免影响后续 PTFE 管的安装。

![ptfe_tube_route_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/ptfe_tube_route_001.png)

1. 从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-24_017.png)

2. 使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-23_016.png)

## 如何验证成功

连接电源线并打开电源。连接无线网络，检查网络是否异常。您也可以通过开关无线网络，验证无线网络开关是否正常。

|  |
| --- |
| 无线网络物理开关 本文拆装步骤演示的机器为测试验证的工程样机，故无开关丝印。 |

否则，请检查 WiFi 天线线缆和无线网口板电缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
