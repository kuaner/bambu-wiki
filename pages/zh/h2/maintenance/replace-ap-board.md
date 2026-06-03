---
path: zh/h2/maintenance/replace-ap-board
title: "更换 H2D & H2C AP 板"
description: "本文介绍了如何更换 H2D & H2C AP 板"
tags: []
created: 2025-03-25T01:38:23.621Z
updated: 2026-05-22T03:58:50.248Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-ap-board
---

## AP 板

AP 板的全称是指应用处理器主板（Application Processor Main Board），它是打印机内处理信息交互的电路板。它为打印机提供了一个独立的操作环境，并支持打印机应用所需的所有系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-13.png)

AP 板的备件包含如下：

AP 板 \* 1

BT3x5 螺丝 - 用于固定 AP 板 \* 4

## 何时更换

需要联系 Bambu Lab 技术支持来确定打印机已出现的问题是否源于 AP 板。

## 所需的工具和材料

- 新的 AP 板
- H2.0 内六角扳手

经过我们的验证，取消地线对功能没有任何影响。某些版本中包含地线，某些版本不包含地线，存在两种版本共存。请根据您收到的版本来决定是否需要拆装AP板上的地线。

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

如果你觉得拆装AP板盖有困难，可以参考这篇wiki中的相关部分视频步骤来进行操作（[点击此处跳转](replace-x-axis-assembly.md)）。

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-6.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-8.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-5.png)

### 步骤 3：断开电缆

依次拔下 AP 板上的连接电缆。

> 如果 USB-C 数据线较难拔下，可等待螺丝拧下后再拔出。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image.png)

> 以下插头在拆装过程中如有疑问，可通过该篇 [打印机连接线缆的插头拆装](../../knowledge-sharing/printer-electronic-connectors-guide.md) 了解该类型的拆装方式。

1. **屏幕排线：**

您可以扣开屏幕连接线上的卡扣，将屏幕连接线抽出。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-11.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-10.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-12.png)

2. **左右 LED 灯连接线（蓝色：右 LED 灯；红色：左 LED 灯）：**

您可以按住 LED 灯连接线接头的卡扣，然后将连接线拔出。

> 左/右 LED 灯的连接线（红/蓝）均可参考相同的方法拔出。

3. **Wifi 天线：**

您可以用手直接向外扣开 Wifi 天线的卡扣，以解锁 Wifi 天线。

4. **USB 接口板：**

将插头上的白胶清理干净后，按住插头顶部的卡扣，然后将连接线向外拔出。

5. **MC-AP 线缆（通信）：**

您可以按住 MC-AP 线缆的卡扣，然后将连接线向外拔出。

6. **MC-AP 线缆（供电）：**

您可以按住 MC-AP 线缆的卡扣，然后将连接线向外拔出。

7. **实况摄像头连接线：**

将实况摄像头连接线与 AP 板连接的卡扣扣开，然后将实况摄像头连接线从 AP 板上的接口中取出；

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-3.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-4.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/img_v3_02jc_852be5cd-8d87-4192-a074-f711ee60b2ag.jpg)

8. **USB-C 数据线**

将 USB-C 数据线平行于 AP 板的方向拔出。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-2.png)

经过我们的验证，取消地线对功能没有任何影响。某些版本中包含地线，某些版本不包含地线，存在两种版本共存。请根据您收到的版本来决定是否需要拆装AP板上的地线。

如果您的 AP 板左下角固定螺丝处有地线，您可以在移除 AP 板固定螺丝时将地线与 AP 板分开。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-1.png)

### 步骤 4：取下 AP 板

使用 H2.0 内六角扳手拧下 4 颗固定螺丝（BT3×5），然后取下 AP 板。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-28.png)

> 取下 AP 板后请检查设备原装的 MC-AP 线缆，与新 AP 版自带的 MC-AP 线缆是否完全一致。如线芯数量不同，请参考[更换 H2 系列 MC-AP 线](replace-mc-ap-cable.md)更换（两种线缆的功能、效果完全一致）。

> |  |  |
> | --- | --- |
> | 线芯少 | 线芯多 |

## 安装 AP 板

### 步骤 1：装回 AP 板

将 AP 板对准上框上的螺丝孔位，使用 H2.0 内六角扳手拧紧 4 颗固定螺丝（BT3x5）。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-27.png)

如果您的 AP 板左下角固定螺丝处有地线，您可以在安装 AP 板左下角的固定螺丝时将地线和 AP 板锁在一起。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-23.png)

### 步骤 2：连接电缆

依次装回 AP 板上的连接电缆。

为避免在连接线缆时互相干涉，可以将线缆分左右两部分来连接：

对于左侧线缆，可按照此顺序连接：1 -> 2（蓝 -> 红）-> 3 -> 4；

对于右侧线缆，可按照此顺序连接：7 -> 8 -> 6 -> 5。

> 注意：连接 USB-C 数据线的时候需要确保 A 字的一面朝外。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-24.png)

1. 屏幕排线
2. 左右 LED 灯连接线（蓝色：右 LED 灯；红色：左 LED 灯）
3. Wifi 天线
4. USB 接口板
5. MC-AP 线缆（通信）
6. MC-AP 线缆（供电）
7. 实况摄像头连接线
8. USB-C 数据线

### 步骤 3：装回 AP 板盖

> 注意：安装 AP 板盖前，需检查线缆是否阻碍 PTFE 管路，避免影响后续 PTFE 管的安装。
>
> ![20250408-115319.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/20250408-115319.jpg)

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-26.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-25.png)

## 如何验证成功

### 根据电路板灯语判断

**正常状态：AP 板指示灯快速闪烁（左）、常亮（右）**

在拧回所有螺丝前，可先预装或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，灯语正常，再拧回螺丝，这样可以避免返工。

<https://public-cdn.bblmw.com/wiki/H2D/AP3.mp4>

您也可以在安装了 AP 板盖后，在特定的角度透过 AP 板盖的散热孔来观察指示灯。

<https://public-cdn.bblmw.com/wiki/H2D/AP4.mp4>

### 连接电源线并打开电源，发起打印，检查是否有报错。

如有报错，请检查 AP 板上所有电缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 附录

**更换 H2D AP 板所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT2.6x8 |  | 用于固定 AP 板盖 |  |  | 1 |
| BT3x5 |  | 用于固定 AP 板 |  |  | 4 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
