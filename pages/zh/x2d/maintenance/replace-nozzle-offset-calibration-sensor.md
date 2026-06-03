---
path: zh/x2d/maintenance/replace-nozzle-offset-calibration-sensor
title: "更换 X2D 喷嘴偏移校准器"
description: "本文介绍了如何更换 X2D 喷嘴偏移校准器及擦嘴钢片"
tags: []
created: 2026-04-14T13:10:00.974Z
updated: 2026-04-14T13:10:02.003Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-nozzle-offset-calibration-sensor
---

## 喷嘴偏移校准传感器

喷嘴偏移校准传感器安装在热床的后方，可以对两个热端的位置进行校准，保证良好的打印质量。  
![fac226.png](https://public-cdn.bblmw.com/wiki/new/x2d/sku_pics/fac226.png)

## 适用打印机型号

X2D

## 何时更换

- 当两个喷嘴的定位出现偏移，导致打印时模型出现错位、层移,并且通过喷嘴偏移校准也无法恢复。
- 经 Bambu Lab 官方技术支持确认需更换喷嘴偏移校准传感器。

## 所需要的工具和材料

- 新的喷嘴偏移校准传感器
- H1.5 内六角扳手
- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除喷嘴偏移校准传感器

### 步骤 1. 调整热床位置

在屏幕点击“运动 XYZ”，然后点击“工具头回中”。

|  |  |
| --- | --- |
|  |  |

等待工具头回中完成后，再点击一次热床 向上10 图标。  
![003_lift_10mm_chinese_version.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-nozzle-offset-calibration-sensor/003_lift_10mm_chinese_version.png)

### 步骤 2. 移除喷嘴偏移校准传感器

移除喷嘴偏移校准器的 2 颗螺丝，  
![004_remove_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-nozzle-offset-calibration-sensor/004_remove_screws.png)

移除喷嘴偏移校准传感器的线缆，可以使用螺丝刀按压线缆卡扣，移除线缆。

|  |  |
| --- | --- |
|  |  |

## 安装喷嘴偏移校准传感器

安装喷嘴偏移校准传感器的线缆，

|  |  |
| --- | --- |
|  |  |

安装喷嘴偏移校准器的 2 颗螺丝。  
![004_remove_screws.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-nozzle-offset-calibration-sensor/004_remove_screws.png)

## 移除擦嘴钢片

移除喷嘴偏移校准器右边的 1 颗螺丝，然后轻轻将擦嘴钢片取下。  
![007_remove_wiper.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-nozzle-offset-calibration-sensor/007_remove_wiper.png)

## 安装擦嘴钢片

将擦嘴钢片安装到喷嘴偏移校准器右侧，然后锁 1 颗螺丝。  
![007_remove_wiper.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace-nozzle-offset-calibration-sensor/007_remove_wiper.png)

## 功能验证

连接电源并打开打印机，发起打印，没有报错即可。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
