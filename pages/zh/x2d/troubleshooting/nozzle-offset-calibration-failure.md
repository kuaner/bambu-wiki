---
path: zh/x2d/troubleshooting/nozzle-offset-calibration-failure
title: "0300-4010：X2D"
description: ""
tags: []
created: 2026-07-01T09:02:14.322Z
updated: 2026-07-02T02:40:44.365Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/nozzle-offset-calibration-failure
---

## 故障描述

如果打印机进行打印时，用到了两个喷嘴，则需要确保两个喷嘴的定位完全一致，才保证良好的打印质量。当两个喷嘴的定位出现偏移，则可能导致打印的时候模型出现错位、层移问题。喷嘴偏移校准包含Z轴方向、XY轴方向偏移校准。

### 校准失败可能的原因有：

- 喷嘴有残料遗留
- 偏移校准传感器上有残料遗留
- 喷嘴没正确安装

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排故措施

### 步骤1. 检查热端

1. 请检查热端喷嘴或热床上是否粘有耗材，若有耗材残留，请将热端温度调整至耗材对应的工作温度，使用镊子或无纺布擦除残留耗材，清理后重新执行喷嘴偏移校准。

   ![filament.png](https://wiki.bambulab.com/h2/troubleshooting/calibrate-failed/filament.png)
2. 若热端和热床上没有耗材残留，请重新安装左右热端。在热端完全贴合加热组件后，将卡扣向下扣牢。

   ![](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_hotend_and_sock/position_check.jpg)

### 步骤2. 检查偏移校准传感器

喷嘴的XY方向的偏移校准，是利用喷嘴和热床后面的**喷嘴偏移校准传感器**进行的。在热床内侧凸起的部分，黑色小块就是XY偏移校准传感器（如下图红框中所示）。请检查此处是否粘有耗材，若有耗材残留，请清理后重新执行喷嘴偏移校准。

![pixpin_2026-07-01_16-47-01.jpg](https://wiki.bambulab.com/x2d/troubleshooting/nozzle-offset-calibration-failure/pixpin_2026-07-01_16-47-01.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
