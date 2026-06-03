---
path: zh/h2/troubleshooting/nozzle-offset-calibration-failure
title: "0300-4010：H2D/H2D Pro/H2C"
description: ""
tags: []
created: 2025-12-23T08:20:28.404Z
updated: 2025-12-31T11:15:59.557Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/nozzle-offset-calibration-failure
---

## 故障描述

如果打印机进行打印时，用到了两个喷嘴，则需要确保两个喷嘴的定位完全一致，才保证良好的打印质量。当两个喷嘴的定位出现偏移，则可能导致打印的时候模型出现错位、层移问题。喷嘴偏移校准包含Z轴方向、XY轴方向偏移校准。

### 校准失败可能的原因有：

- 喷嘴有残料遗留
- 偏移校准传感器上有残料遗留
- 喷嘴没正确安装

> **重要提醒 ！**  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排故措施

### 步骤1. 检查热端喷嘴或热床上是否粘有耗材

喷嘴的Z方向的偏移校准，是利用两个喷嘴分别在热床表面触碰一下，像回零一样触热床，打印机获得触碰时热床的Z坐标，坐标之差就是Z偏移值。热端喷嘴或热床上粘有耗材时喷嘴偏移校准会失败

请检查热端喷嘴或热床上是否粘有耗材，若有耗材残留，请清理后重新执行喷嘴偏移校准。

#### 清理热端喷嘴上残留耗材或者其他异物

手动将热端温度调整至当前打印耗材对应的工作温度；待热端温度稳定后，使用镊子或无纺布擦除残留耗材。

![20251229-145313.jpg](https://wiki.bambulab.com/h2c/20251229-145313.jpg)

#### 清理热床上残存耗材

用刮刀刮去打印板上残留的耗材。

![filament.png](https://wiki.bambulab.com/h2/troubleshooting/calibrate-failed/filament.png)

### 步骤2. 检查偏移校准传感器上是否粘有耗材

喷嘴的XY方向的偏移校准，是利用喷嘴和热床后面的**喷嘴偏移校准传感器**进行的。在热床内侧凸起的部分，右边的黑色小块就是XY偏移校准传感器（如下图红框中所示）。请检查此处是否粘有耗材，若有耗材残留，请清理后重新执行喷嘴偏移校准。  
![calibrationsensor.png](https://wiki.bambulab.com/h2/troubleshooting/calibrate-failed/calibrationsensor.png)

喷嘴的XY方向的偏移校准，是利用喷嘴和热床后面的**喷嘴偏移校准传感器**进行的。在热床内侧凸起的部分，右边的黑色小块就是XY偏移校准传感器（如下图红框中所示）。请检查此处是否粘有耗材，若有耗材残留，请清理后重新执行喷嘴偏移校准。

### 步骤3. 检查喷嘴状态

请正确安装左右热端。使喷嘴完全贴合喷嘴，将右边的卡扣向下扣牢。

![](https://wiki.bambulab.com/h2/17.%E6%89%A3%E7%B4%A7%E5%8D%A1%E6%89%A3.webp)

注意，图左的卡扣错误锁紧是因为同时向下拨动拨片与卡扣，导致拨片错误卡进了卡扣中。因此，请务必将左边的拨片完全贴合喷嘴后，再去拨动右边的卡扣。

|  |  |
| --- | --- |
| ams_int_board_1 | pry_up_the_interface_board |

对于H2C右侧感应热端，请向左推动感应热端锁紧拉柄确保感应热端被锁紧。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend/019.webp)

### 步骤4. 重新校准

完成以上排查步骤后，请在打印机屏幕上点击**重新校准**。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
