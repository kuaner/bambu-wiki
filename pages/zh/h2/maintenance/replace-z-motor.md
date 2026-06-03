---
path: zh/h2/maintenance/replace-z-motor
title: "更换 H2 系列 Z 电机"
description: "本文介绍了如何更换 H2 系列 Z 电机"
tags: []
created: 2025-03-25T02:09:15.286Z
updated: 2026-03-13T03:23:41.164Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-z-motor
---

## Z 电机

Z 电机是安装在打印机背部，用于驱动热床完成 Z 方向移动的电机。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-14.png)

**Z 电机的备件包含以下：**

1. Z 电机 \* 1
2. M3x8 螺丝 - 用于固定 Z 电机 \* 4

## 何时更换

- 电机烧坏
- 经 Bambu Lab 技术支持确认需要更换电机

## 所需的工具和材料

1. 新的 Z 电机
2. H2.0 内六角扳手
3. M3x35x8 \* 4（您可以使用开箱时固定热床的螺丝）

**更换 H2D Z 电机所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板 |  |  | 12 |
| ST3x8 |  | 用于固定背板 |  |  | 11 |
| ST3x12 |  | 用于固定料盘支架底座 |  |  | 2 |
| M3x6 |  | 用于固定 Z 张紧器滑块和张紧器盖 |  |  | 1 |
| M3x8 |  | 用于固定 Z 电机 |  |  | 4 |
| M3x35x8 |  | 用于固定 Z 滑块 |  |  | 4 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

## 移除 Z 电机

### 步骤 1：下降热床并锁定 Z 轴滑块

1. **下降热床**

**电机可以使用的情况：**

通过屏幕来控制热床，将热床下降至打印机底部。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-5.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-6.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-7.png)

降低热床后关闭打印机电源，并断开电源连接。

**如果电机无法使用：**

您可以稍微倾斜打印机，拉动 Z 轴皮带将热床下降到底部。

注：您可以先来回拉动皮带，确认下降的方向。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-8.png)

2. **固定 Z 轴滑块**

锁入 4 颗辅助螺丝（M3x35x8）固定 4 个 Z 轴滑块。

> 注：您可以使用开箱的时候固定热床的螺丝。  
> ![z-fix-v](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/z-fix-v.jpg)

### 步骤 2：移除背板

您可以参阅这篇 Wiki 来移除打印机背板：

[更换 H2D 背板](replace-rear-panel.md)

### 步骤 3：断开 Z 电机连接线

当移除背板后，您可以将电机线缆从内衬的卡扣中移除，然后将电机连接线从 MC 板上断开连接。如果在接口处有硅胶，您可以使用镊子将硅胶去除，然后再将连接线与 MC 板断开。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-13.png)

### 步骤 4：松 Z 轴张紧器

1. 将打印机侧放，释放张紧器扭簧的长臂，使用 H2.0 内六角扳手拧松一颗张紧器固定螺丝（M3x6），解除张紧弹簧的张紧状态；

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-12.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-11.png)

- 您可以将 Z 皮带从 Z 电机主动轴的边缘取出，便于后续移除 Z 电机。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-10.png)

### 步骤 5：移除 Z 电机

使用 H2.0 内六角扳手移除四颗 Z 电机固定螺丝（M3x8）。

这四颗螺丝比较紧，建议使用较好的 H2.0 内六角扳手来移除，避免螺丝滑丝。**当开始移除最后一颗螺丝的时候，请用手扶着电机，避免电机跌落。**螺丝移除后您可以直接将电机取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-9.png)

## 安装 Z 电机

### 步骤 1：将 Z 电机装回

将新的 Z 电机对准打印机上的孔位，然后使用 H2.0 内六角扳手依次拧紧四颗固定螺丝（M3x8）。**在拧的时候请用手扶着 Z 电机，避免电机掉落。**

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/img_v3_02js_16d86ea0-fbde-430b-8a0b-82e056f9f89g.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-26.png)

### 步骤 2：安装 Z 轴张紧器

先将 Z 皮带套进 Z 电机主动轴，然将 Z 轴张紧器扭簧的长臂卡到位，使用 H2.0 内六角扳手拧紧一颗张紧器滑块固定螺丝（M3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-28.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-24.png)

注：

- 在装回扭簧的时候，请检查短臂是否卡在 Z 轴张紧器滑块前段；
- 请检查扭簧是否完全套在轴上，如果没有请按回。在按回扭簧的时候可能会由于震动导致 Z 轴张紧器滑块里面的螺母掉出，您可以使用一小节 PTFE 管（或其他物品）来堵住螺母，防止螺母掉出。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-27.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-25.png)

### 步骤 3：连接线缆和解锁 Z 轴滑块

1. 将打印机正放，将 Z 电机连接线与 MC 板连接，并将线缆扣入左内衬的线扣中；

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-21.png)

2. 然后使用 H2.0 内六角扳手移除四颗 Z 轴滑块固定螺丝（M3x35x8），移除螺丝后将打印机稍稍倾斜，来回拉动 Z 皮带，确认热床是否可以上下移动。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-motor/image-23.png)

### 步骤 4：安装背板

您可以参考这篇 Wiki 来安装打印机背板：

[更换 H2D 背板](replace-rear-panel.md)

## 如何验证成功

连接电源并打开打印机，点击回中检查打印机是否可以正常回中。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
