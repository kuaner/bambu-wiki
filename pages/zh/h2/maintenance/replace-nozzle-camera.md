---
path: zh/h2/maintenance/replace-nozzle-camera
title: "更换 H2D & H2C 喷嘴摄像头"
description: "本文介绍如何更换 H2D & H2C 喷嘴摄像头"
tags: []
created: 2025-03-25T08:22:35.808Z
updated: 2026-05-28T09:15:19.443Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-nozzle-camera
---

> **隐私提示**：请确保摄像头已正确安装，使摄像头视野正确朝向打印机腔体，以避免对打印区域或喷嘴的检测出现问题。

H2D 在工具头上配备了喷嘴相机，用于检测异常的打印状态，包括裹头、空打和炒面检测。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-13.png)

## 何时更换

- 喷嘴摄像头故障

## 所需的工具和材料

1. 新的喷嘴摄像头
2. H2.0 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系[在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 拆解步骤

本指南的拆装步骤截取自完整的工具头拆装指南，实际上在更换喷嘴摄像头时，并不需要拆除PTFE管、工具头前盖以及左右热端，请按需拆装。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/20250221-180451.jpg)

### 步骤 1：移除部件冷却风扇风道

使用 H2.0 内六角扳手移除四颗固定螺丝（BT3x8）

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-10.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-12.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-8.png)

握住部件冷却风扇风道尾部，小心向下将风道取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-9.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-11.png)

### 步骤 2：移除部件冷却风扇

使用 H2.0 内六角扳手移除四颗固定螺丝（BT3x20 方框标记，BT2.6x8 圆圈标记）。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-1.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-2.png)

撕掉插头上的醋酸胶布，拔掉插头。可将撕下的胶带留在电路板上，便于后续安装。

**请注意，这种类型的插头应该沿插头所在平面向上小心用力推出，而不是沿着电缆方向拉出。请按照视频中的操作进行，以避免损坏插头。**

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-3.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-4.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-5.png)

### 步骤 3：移除挤出接口板

依次拔掉挤出接口板上的切换电机插头、挤出主板插头、右热端加热组件插头、左热端加热组件插头及其泡棉（插头位于挤出主板，泡棉位于挤出接口板）以及升降电机插头。请注意FPC线缆是被卡扣压住的，需要先解锁卡扣，再拔出FPC线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-6.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-7.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-14.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-15.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-16.png)

撕开左热端加热组件插头的泡棉时，建议先松开插头，再从下往上撕开，这样可以确保泡棉的完整性。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-17.png)

拧下挤出接口板上的两颗固定螺丝，一只手捏住接口板两侧，然后另一只手在接口板靠近切换电机插头的地方轻轻晃动，以取出挤出接口板。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-19.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-20.png)

### 步骤 4：移除喷嘴摄像头

喷嘴摄像头的FPC线沾在升降电机后盖上，在拆除之前先使用镊子拉出一部分预留的FPC线，留出用手指穿过并握住FPC线的空间。然后松开喷嘴摄像头的插座卡扣，并用手逐渐松开FPC线，最后断开FPC线。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-21.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-22.png)

拧下两颗喷嘴摄像头的固定螺丝，拆下喷嘴摄像头。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-24.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-25.png)

## 安装步骤

### 步骤 1：安装喷嘴摄像头

拧入喷嘴摄像头的两颗固定螺丝。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-26.png)

将喷嘴摄像头FPC线缆重新插入插头中，请确保FPC线缆的头部完全进入插头中（白线处于水平状态，代表FPC线缆插入到位），再扣合插座。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-27.png)

使用镊子将下半部分预留的FPC线缆收纳进喷嘴摄像头上方的空隙中。然后用手按压FPC线缆，使其平整地贴合在升降电机后盖上。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-28.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-29.png)

### 步骤 2：安装挤出接口板

挤出接口板的背面有两根金属柱，将其对准挤出主板上的金属孔并插入，一边轻轻晃动一边向后推，确保挤出接口板安装到位。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-30.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-31.png)

然后拧入挤出接口板上的两颗固定螺丝。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-32.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-33.png)

将侧面的挤出霍尔转接线收纳进挤出主板和挤出接口板的缝隙中，然后依次重新连接升降电机连接线、左热端加热组件插头、右热端加热组件插头、挤出主板连接线、切换电机连接线。

在连接升降电机、挤出主板和切换电机连接线时，请确保FPC线缆的头部完全进入插头中（这3根FPC的插头均有一根横线，横线处于水平表示FPC线缆插入到位），再扣合插座。最后用手指轻轻折叠一下FPC线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-34.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-35.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-36.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-37.png)

在连接左右热端加热组件插头时，需要合理规划走线。将左热端加热组件线缆依次穿过下方和背面的线槽，防止线缆松散难以整理。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-38.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-39.png)

然后将左热端加热组件插头插入挤出主板对应的接口，再将泡棉重新压紧。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-40.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-41.png)

连接右热端加热组件时，同样先将右热端加热组件线缆穿过背面的线槽，再将插头插入挤出主板。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-42.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-43.png)

### 步骤 3：安装部件冷却风扇

金属面朝上，对齐接口后，向下压入部件冷却风扇插头，并贴回醋酸胶布。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-44.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-45.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-46.png)

对准螺丝孔，盖回部件冷却风扇，拧入 4 颗固定螺丝。（BT3x20 方框标记，BT2.6x8 圆圈标记）

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-47.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-48.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-49.png)

### 步骤 4：安装部件冷却风扇风道

左热端加热组件线缆需要安装在理线槽中，在安装风道前，先将加热组件线缆压入理线槽，避免风道压住线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-50.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-51.png)

先安装前1/4风道，这样可以使后半部分风道更容易倾斜，从而避开喷嘴摄像头的干涉。然后抓住后半部分风道向上推入。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-52.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-53.png)

推入后，再分别往外掰风道的两侧，将风道的两侧卡在工具头上，然后将风道用力往上卡紧。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-54.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-55.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-56.png)

接下来往前推入前部分风道的顶部，使其完全贴合，不留缝隙。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-57.png)

使用 H2.0 内六角扳手拧紧四颗固定螺丝（BT3x8）

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-58.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-59.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-camera/image-60.png)

## 如何验证成功

启动打印机并发起打印，观察打印机工作过程中是否会出现喷嘴摄像头相关的报错，如果没有任何错误，说明喷嘴摄像头安装正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
