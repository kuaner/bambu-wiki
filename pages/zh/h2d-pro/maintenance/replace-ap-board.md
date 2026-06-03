---
path: zh/h2d-pro/maintenance/replace-ap-board
title: "更换 H2D Pro AP 板"
description: ""
tags: []
created: 2025-08-08T09:21:09.040Z
updated: 2026-05-21T13:33:29.876Z
source: https://wiki.bambulab.com/zh/h2d-pro/maintenance/replace-ap-board
---

## AP 板

AP 板的全称是指应用处理器主板（Application Processor Mainboard），它是打印机内处理信息交互的电路板。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

![ap_board_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/ap_board_001.png)

AP 板的备件包含如下：

1. AP 板 \* 1
2. BT3x5 螺丝 - 用于固定 AP 板 \* 4

## 何时更换

需要联系 Bambu Lab 技术支持来确定打印机已出现的问题是否源于 AP 板。

## 所需的工具和材料

1. 新的 AP 板
2. H2.0 内六角扳手

**更换 H2D AP 板所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT2.6x8 |  | 用于固定 AP 板盖 |  |  | 1 |
| BT3x5 |  | 用于固定 AP 板 |  |  | 4 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换了 AP 板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 移除 AP 板

### 步骤 1：关闭电源

关闭打印机电源后拔下电源线，并取下上盖玻璃。

### 步骤 2：取下 AP 板盖

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），打开 AP 板盖；

> 您可以参考[这篇 wiki](../../h2/maintenance/replace-x-axis-assembly.md) 中的拆除 AP 板盖相关部分视频步骤来进行操作。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/image_043.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/image-1_001.png)

2. 从靠近前门的一侧取下 AP 板盖。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-3_023.png)

### 步骤 3：断开电缆

依次拔下 AP 板上的 1-10 号插头。

![unplug_1-10_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/unplug_1-10_001.png)

![unplug_all_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/unplug_all_001.png)

1. 屏幕排线
2. 无线网口板
3. 左LED灯连接线（红色插头）
4. 右LED灯连接线（蓝色插头）
5. USB 接口板
6. MC-AP 线缆（通信）
7. MC-AP 线缆（供电）
8. 有线网口板
9. USB-C 数据线
10. 实况摄像头连接线

**拔插头建议**:

- 拔 #1, #2, #10 这类 FPC 排线插头需要先抠开卡扣，再抽出 FPC 排线。
- 拔 #3, #4, #5, #6, #8 排线插头时，需要按压解锁插头再拔出插头。请参考以下视频操作。

[unplugging\_suggestions\_1\_002.mp4](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/unplugging_suggestions_1_002.mp4)

[unplugging\_suggestions\_2\_002.mp4](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/unplugging_suggestions_2_002.mp4)

- 如果 #9 USB-C 数据线较难拔出，可稍微用力，将线缆往打印机前方推动。

![unplugging_suggestions_3_001.webp](https://wiki.bambulab.com/h2/h2d-pro/unplugging_suggestions_3_001.webp)

- 增加线长后，再拉住这段线缆往打印机后方稍微用力，将 USB-C 数据线平行于 AP 板的方向拔出。

![unplugging_suggestions_4_001.webp](https://wiki.bambulab.com/h2/h2d-pro/unplugging_suggestions_4_001.webp)

### 步骤 4：取下 AP 板

使用 H2.0 内六角扳手拧下 4 颗固定螺丝（BT3×5），然后取下 AP 板。  
AP 板左下角固定螺丝有连接接地线，可以只拧 下 AP 板这端的 4 颗螺丝（红色圆圈标记），与机箱框架相连的螺丝可以保持原状。

![screws_for_apboard_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/screws_for_apboard_001.png)

![unplug_all_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/unplug_all_001.png)

## 安装 AP 板

### 步骤 1：装回 AP 板

将 AP 板对准上框上的螺丝孔位，使用 H2.0 内六角扳手拧紧 4 颗固定螺丝（BT3x5）。  
AP 板左下角固定螺丝处有地线，在安装 AP 板左下角的固定螺丝时需要将地线和 AP 板锁在一起。

![screws_for_apboard_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/screws_for_apboard_001.png)

![ground_wire_screw_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/ground_wire_screw_001.png)

### 步骤 2：连接电缆

连接 AP 板上的插头。

![unplug_1-10_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-ap-board/unplug_1-10_001.png)

1. 屏幕排线
2. 无线网口板
3. 左LED灯连接线（红色插头）
4. 右LED灯连接线（蓝色插头）
5. USB 接口板
6. MC-AP 线缆（通信）
7. MC-AP 线缆（供电）
8. 有线网口板
9. USB-C 数据线
10. 实况摄像头连接线

**插插头要求**:

- USB-C 数据线（#9）插入时需要确保“A”字样的一面朝向机箱内。该插头比较紧，需要用一点力往前插入。

![plugging_suggestions_1_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_1_001.webp)

- 插头插到位后整理线缆。整理线缆时注意不要扯松插头。

![plugging_suggestions_2_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_2_001.webp)

- 屏幕排线（#1），无线网口板 (#2) 和实况摄像头连接线（#10），排线左右两边的小耳朵需要嵌入插座中。#1 和 #10 需要将“AP”字样的一面朝向机箱内，并保证扣好卡扣后，卡扣平整无翘边。

![plugging_suggestions_6_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_6_001.webp)

![plugging_suggestions_7_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_7_001.webp)

![plugging_suggestions_3_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_3_001.webp)

- 插 #3, #4, #5, #6, #8 排线插头时，需要注意对准卡扣方向插入。

![plugging_suggestions_4_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_4_001.webp)

![plugging_suggestions_5_001.webp](https://wiki.bambulab.com/h2/h2d-pro/plugging_suggestions_5_001.webp)

### 步骤 3：装回 AP 板盖

> 注意：安装 AP 板盖前，需检查线缆是否阻碍 PTFE 管路，避免影响后续 PTFE 管的安装。

![ptfe_tube_route_001.png](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/ptfe_tube_route_001.png)

1. 从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-24_017.png)

2. 使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2d-pro/replace-wireless-network-board/image-23_016.png)

## 如何验证成功

连接电源线并打开电源。发起打印，检查是否有报错。

否则，请检查 AP 板上所有电缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
