---
path: zh/h2/troubleshooting/homing-leveling-failure
title: "H2D 回零&调平失败故障排查"
description: "本文将详细为您介绍可能会导致 H2D 回零&调平失败的原因以及解决方案。"
tags: []
created: 2025-06-17T04:16:05.264Z
updated: 2025-06-25T03:04:43.443Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/homing-leveling-failure
---

## 回零&调平

**打印机回零：** XYZ 轴通过检测各个轴的限位，从而确定工具头在三维空间中的零点坐标。在回零过程中，X 轴（工具头移动）和 Y 轴（热床移动）依靠各自的电机检测负载，来判断是否到达各自的运动边界。而 Z 轴方向的回零则是工具头下降，让喷嘴触碰热床，涡流传感器检测喷嘴是否碰到了热床。

**打印机调平：** 调平可以补偿由于热床不平或者装配歪斜而导致的喷嘴与热床之间的距离波动，保证喷嘴与热床的距离在热床不同位置上都尽量一致，以获取更好的首层打印质量。

打印机的回中和调平功能主要依赖于两个涡流线圈：左侧涡流线圈位于加热组件后方，右侧涡流线圈则位于加热组件上方。  
![image-119.png](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/image-119.png)

## 问题现象

常见的回零报错信息包括 **“挤出力传感器频率过低”或“频率过高”**，这通常表示喷嘴位置异常或传感器位置异常。

![频率过低.jpg](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/%E9%A2%91%E7%8E%87%E8%BF%87%E4%BD%8E.jpg)

当出现 **“挤出机力传感器信号异常，可能是传感器或 MC-TH 通讯异常”** 的报错时，可能是原因包括接头接触不良或涡流传感器损坏。

> 若左右喷嘴均无法正常回零，则更可能是 MC-TH 通讯异常所致。

![传感器异常.jpg](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/%E4%BC%A0%E6%84%9F%E5%99%A8%E5%BC%82%E5%B8%B8.jpg)

> 注意：当您在屏幕、Bambu Studio 或 Handy 中执行回零操作时，如果喷嘴温度较高，打印机将优先执行 XY 轴回零，待喷嘴温度降至 140°C 后，才会下降喷嘴触碰热床，如果等待时间过长，可能是热端温控异常，观察是否有温控相关的HMS。

## 排查流程

![pixpin_2025-06-17_19-31-55.png](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/pixpin_2025-06-17_19-31-55.png)

## 详细排查步骤

### 检查喷嘴安装状态

请务必检查喷嘴，确保热端喷嘴与热端加热器紧密贴合，并且锁紧卡扣已扣紧，以保证热端无松动。

|  |  |
| --- | --- |
| 喷嘴错误安装 | 喷嘴正确安装 |

同时，请确认喷嘴固定卡扣无断裂或变形的情况。

![20250617-195008.jpg](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/20250617-195008.jpg)

### 调换喷嘴组件

如果已确认喷嘴组件安装正常，我们建议您调换左右喷嘴，并再次执行回零操作，观察是否仍出现报错。

详细更换步骤可以参考：[H2D 热端更换指南](../maintenance/replace-hotend.md)

![xyz.png](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/xyz.png)

如果回零测试通过，您需要着重检查原喷嘴是否存在损坏，并考虑更换新的喷嘴组件。如果回零测试仍然失败，则可能是传感器故障，请根据以下步骤继续进行故障排查。

> 提示： 鉴于左右涡流线圈的安装位置不同，排查方式也有所区别。若您的问题出在左侧喷嘴，可点击[此链接快速跳转至相应部分](#intro)。

### 右喷嘴涡流线圈故障排查

**检查涡流线圈外观**

移除喷嘴组件后，您会看到涡流线圈被一层黑色醋酸胶带覆盖。请检查线圈是否有裸露或受损的情况。如果线圈受损，则需要更换该涡流线圈。

![20250617-165810.jpg](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/20250617-165810.jpg)

> 注意：请勿撕下黑色醋酸胶带，以免导致线圈断裂。

**重新插拔右涡流线圈**

> H2D挤出主板上的涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于PCB面方向用力抬起以解锁插头**。切勿沿线缆方向用力，以免损坏插头。  
> ![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

如果涡流线圈外观正常，则可能是**涡流线圈接头松动或接触不良**。此时，您需要重新插拔涡流线圈的连接线。

插拔接头需要移除部件**散热风扇和挤出接口板**，详细插拔步骤可参考 [H2D 左右涡流线圈更换指南](../maintenance/replace-nozzle-eddy-sensor.md)。

#### 部件冷却风扇视频指南

移除部件散热风扇后和挤出主板后，撕掉贴在右涡流线圈接口上的胶布，然后将右涡流线圈连接线沿着插头所在的平面向外推出，并重新安装。

![](https://wiki.bambulab.com/h2/maintenance/replace-nozzle-eddy-sensor/image-35.png)

完成后可以再次进行回零进行测试，如果依旧存在故障，建议您联系[拓竹技术支持](https://bambulab.cn/zh-cn/my/support/tickets/create)并提交打印机近期日志。

### 左涡流线圈故障排查

左侧涡流线圈位于工具头内部，通常不易出现破损或断裂。然而，可能会出现位置偏移或接头接触不良。

首先，您可以尝试重新插拔左涡流线圈接头。移除[部件冷却风道](../maintenance/replace-part-cooling-fan-air-duct.md)即可对左涡流线圈进行插拔。

> 注意：插拔接头必须断电操作。

![左涡流.jpg](https://wiki.bambulab.com/h2/troubleshooting/homing-leveling-failure/20250617-174411.jpg)

> H2D挤出主板上的涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于PCB面方向用力抬起以解锁插头**。切勿沿线缆方向用力，以免损坏插头。  
> ![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

重新插拔后，您可以再次对左侧喷嘴进行回零测试。如果问题依旧存在，则可能是涡流线圈位置出现偏移，建议您重新安装左侧涡流线圈。

**重新安装左侧涡流线圈**

左涡流线圈与升降滑块之间的理想距离约为 0.2mm。重新安装前，您需要准备一小片对折的 A4 纸，其对折后的厚度约为 0.2mm。

详细的拆装步骤可参考 [H2D 左右涡流线圈更换指南](../maintenance/replace-nozzle-eddy-sensor.md)。

将 A4 纸插入左涡流线圈与升降滑块之间，用手按住左涡流线圈，然后拉动 A4 纸，检查 A4 纸是否能刚好滑动（存在轻微阻力但容易取出）。如果可以顺利滑动，再使用 H2.0 内六角扳手拧紧固定螺丝。

在拧紧螺丝的过程中，请保持按住左涡流线圈的手稳定，避免位置发生变化。螺丝拧紧后，将 A4 纸取出。

|  |  |
| --- | --- |
|  |  |

重新安装完成后，请再次进行回零测试，检查是否已解决报错。如果故障仍然存在，建议您联系[拓竹技术支持](https://bambulab.cn/zh-cn/my/support/tickets/create)并提交打印机近期日志。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
