---
path: zh/h2s/maintenance/replace-ap-board
title: "AP 板更换指南"
description: ""
tags: []
created: 2025-08-24T10:45:32.515Z
updated: 2026-04-16T01:43:18.555Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-ap-board
---

## AP 板

AP 板的全称是指应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

![](https://wiki.bambulab.com/h2s/maintenance/image.png)

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
| BT3x5 |  | 用于固定USB-C理线扣 |  |  | 1 |

**注意事项：**

1. **更换了 AP 板的机器，在首次开机时，应跳过绑定机器的步骤。**

> 由于新的 SN 未注册，无法进行绑定操作，只有在 SN 注册后才能成功绑定。

- **在确认更换完成后，还需要进行 SN 的替换，请联系 Bambu Lab 技术支持并同时提供新、旧 SN 以完成 SN 替换。新旧AP板的SN获取方式参考此文：[如何查找序列号及注册新序列号](../../general/find-sn.md)，建议在更换AP板之前先拍照保存AP板的SN。**

![](https://wiki.bambulab.com/h2s/maintenance/image-4.png)

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除 AP 板

### 步骤 1：关闭电源

关闭打印机电源后拔下电源线，并取下上盖玻璃。

### 步骤 2：取下 AP 板盖

- 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），打开 AP 板盖；
- 如果你觉得拆装AP板盖有困难，可以参考这篇wiki中的相关部分视频步骤来进行操作（[点击此处跳转](../../h2/maintenance/replace-x-axis-assembly.md)）。

|  |  |
| --- | --- |
|  |  |

- 从靠近前门的一侧取下 AP 板盖。

![](https://wiki.bambulab.com/h2s/maintenance/image-7.png)

### 步骤 3：断开电缆

依次拔下 AP 板上的 1-9 号插头。

|  |  |
| --- | --- |
|  |  |

1. 屏幕排线
2. USB 接口板
3. 左LED灯连接线（红色插头）
4. 右LED灯连接线（蓝色插头）
5. MC-AP 线缆（通信）
6. MC-AP 线缆（供电）
7. TH供电线缆（借AP中转）
8. USB-C 数据线
9. 实况摄像头连接线

左下角螺丝连接了一根接地线缆

**拔插头建议**:

- #1, #9这类 FPC 排线插头需要先抠开卡扣，再抽出 FPC 排线。请参考下图，先抠开卡扣，再抽出排线。

![remove_fpc_cable.webp](https://wiki.bambulab.com/h2s/maintenance/remove_fpc_cable.webp)

- 拔插 #2, #3, #4, #5, 排线插头时，需要按压解锁再拔出插头。另外，2号插头使用了电子硅胶进行加固，拔插头前，可以使用镊子等工具刮掉硅胶。此硅胶主要是用于加固，防止运输过程松脱，如果后续连接插头后，没有出现U盘读写异常，可以不用补打硅胶。

![](https://wiki.bambulab.com/h2s/maintenance/remove-buckle-plug.webp)

- 拔出#8 USB-C 数据线之前，需要先拧出理线卡扣的螺丝，从靠近AP板附近的卡扣中抽出USB-C线缆。

|  |  |
| --- | --- |
|  |  |

这一步可以先不断开wifi天线插头，待拧下螺丝，取下板子后，再断开插头。

### 步骤 4：取下 AP 板并拆下wifi天线座子

使用 H2.0 内六角扳手拧下 4 颗固定螺丝（BT3×5），然后取下 AP 板，断开wifi天线插头。

AP 板左下角固定螺丝有连接接地线，可以只拧 下AP 板这端的4颗螺丝（红色圆圈标记），与机箱框架相连的螺丝（绿色圆圈标记）可以保持原状。

![](https://wiki.bambulab.com/h2s/maintenance/image-11.png)

![](https://wiki.bambulab.com/h2s/maintenance/remove-wifi-plug.webp)

## 安装 AP 板

## 步骤 1：连接wifi天线插头，并装回 AP 板

按照下图的示意图，对准孔位后，压入连接wifi天线插头

![](https://wiki.bambulab.com/h2s/maintenance/install-wifi-plug.webp)

将 AP 板对准上框上的螺丝孔位，注意整理线缆，并避开wifi天线，不要压住线缆。

![](https://wiki.bambulab.com/h2s/maintenance/install-ap-board.webp)

，使用 H2.0 内六角扳手拧紧 4 颗固定螺丝（BT3x5），AP 板左下角固定螺丝处有地线，**在安装 AP 板左下角的固定螺丝时需要将地线和 AP 板锁在一起。**

![](https://wiki.bambulab.com/h2s/maintenance/image-12.png)

![](https://wiki.bambulab.com/h2s/maintenance/image-13.png)

### 步骤 2：连接电缆

连接 AP 板上的插头。

![](https://wiki.bambulab.com/h2s/maintenance/image-14.png)

1. 屏幕排线
2. USB 接口板
3. 左LED灯连接线（红色插头）
4. 右LED灯连接线（蓝色插头）
5. MC-AP 线缆（通信）
6. MC-AP 线缆（供电）
7. TH供电线缆（借AP中转）
8. USB-C 数据线
9. 实况摄像头连接线

左下角螺丝连接了一根接地线缆

**插插头要求**:

1. USB-C 数据线（#8）插入时需要确保“A”字样的一面朝向机箱内，插头插到位后整理线缆（该插头比较紧，需要用一点力往前插入，整理线缆时注意不要扯松插头）。

![](https://wiki.bambulab.com/h2s/maintenance/image-15.png)

![insert-USB.webp](https://wiki.bambulab.com/h2s/maintenance/insert-usb.webp)

锁入USB-C线缆理线扣的螺丝

![](https://wiki.bambulab.com/h2s/maintenance/image-16.png)

- 屏幕排线（#1） 和实况摄像头连接线（#9），排线左右两边的小耳朵需要嵌入插座中。#1 和 #9 需要将“AP”字样的一面朝向机箱内。在扣好卡扣后，卡扣平整无翘边。

![](https://wiki.bambulab.com/h2s/maintenance/image-17.png)

![](https://wiki.bambulab.com/h2s/maintenance/image-18.png)

- #2，#3, #4，#5，#6，#7按照卡扣的方向插入即可，确保插头连接到位。其中#2如果残胶过多，可以先试用镊子去除部分残胶，以保证插头顺利插到位。

![install-left-plug.webp](https://wiki.bambulab.com/h2s/maintenance/install-left-plug.webp)

![](https://wiki.bambulab.com/h2s/maintenance/insert-th-power.webp)

### 步骤 3：装回 AP 板盖

> 注意：安装 AP 板盖前，需检查线缆是否阻碍 PTFE 管路，避免影响后续 PTFE 管的安装。
>
> ![](https://wiki.bambulab.com/h2s/maintenance/image-19.png)

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

|  |  |
| --- | --- |
|  |  |

## 如何验证成功

连接电源线并打开电源。发起打印，检查是否有报错。

否则，请检查 AP 板上所有电缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
