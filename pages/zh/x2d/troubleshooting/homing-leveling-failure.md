---
path: zh/x2d/troubleshooting/homing-leveling-failure
title: "X2D 回零&调平失败故障排查"
description: "本文将详细为您介绍可能会导致 X2D 回零&调平失败的原因以及解决方案。"
tags: ["x2d"]
created: 2026-05-18T12:05:22.207Z
updated: 2026-05-29T07:19:19.862Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/homing-leveling-failure
---

## 回零&调平

**打印机回零：** 在回零过程中，X 轴（工具头移动）和 Y 轴（热床移动）依靠各自的电机检测负载，来判断是否到达各自的运动边界。而 Z 轴方向的回零则是热床上升，让喷嘴触碰热床，通过涡流线圈传感器来检测喷嘴是否碰到了热床。

**打印机调平：** 调平可以补偿由于热床不平或者装配歪斜而导致的喷嘴与热床之间的距离波动，保证喷嘴与热床的距离在热床不同位置上都尽量一致，以获取更好的首层打印质量。

左右涡流线圈分布：

![x2deddy.jpg](https://wiki.bambulab.com/x2d/troubleshooting/homing-leveling-failure/x2deddy.jpg)

## 故障现象

设备通常会弹出“Z 轴电机转动受阻”或“涡流线圈灵敏度异常”的报错。

1. 对于“Z 轴电机”，这需要排查 Z 轴传动部分（电机、皮带、丝杆）是否存在异物，以及打印机仓内是否存在异物。
2. 对于“涡流传感器”，通常只需要调整涡流线圈位置即可，少数情况可能会是涡流线圈受损。

## 排查步骤

### 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### Z 轴电机报错

#### 检查异物

检查 Z 轴滑块上是否存在异物并清理。

![pixpin_2026-05-20_18-19-56.jpg](https://wiki.bambulab.com/x2d/troubleshooting/homing-leveling-failure/pixpin_2026-05-20_18-19-56.jpg)  
![pixpin_2026-05-20_18-20-27.jpg](https://wiki.bambulab.com/x2d/troubleshooting/homing-leveling-failure/pixpin_2026-05-20_18-20-27.jpg)

**取下顶盖玻璃，倾斜打印机。** 检查 Z 皮带、Z 轴同步轮上是否有异物并清理。

![pixpin_2026-05-20_18-19-23.jpg](https://wiki.bambulab.com/x2d/troubleshooting/homing-leveling-failure/pixpin_2026-05-20_18-19-23.jpg)  
![pixpin_2026-05-20_18-18-31.jpg](https://wiki.bambulab.com/x2d/troubleshooting/homing-leveling-failure/pixpin_2026-05-20_18-18-31.jpg)

确保没有异物后，可尝试拉动 Z 皮带，观察热床是否能够向上移动。若拉动皮带感受到了明显阻力，则可能需要[更换 Z 电机](../../p2s/maintenance/replace-z-motor.md)。

#### 检查热床

若 Z 皮带与某一个 Z 同步轮之间出现打滑，会导致热床的三个角落高度不一致。这样回零过程中偏高的一端可能会挤压框架，导致 Z 电机转动受阻。

**操作步骤：**

关机后手动推拉 Z 皮带，控制热床紧贴底板。

> 倾斜打印机即可，放倒仅为展示操作。

![13_013.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/13_013.webp)

观察左右滑块是否紧贴底板。

|  |  |
| --- | --- |
| pixpin_2026-05-26_17-04-03.jpg | pixpin_2026-05-26_17-03-23.jpg |

后侧滑块需拆除背板观察，请参考[更换 X2D 的背板](../maintenance/replace-rear-panel.md)。

![pixpin_2026-05-26_17-02-50.jpg](https://wiki.bambulab.com/x2d/troubleshooting/homing-leveling-failure/pixpin_2026-05-26_17-02-50.jpg)

若某一侧滑块无法紧贴底板，就需要[重新安装 Z 皮带](../../p2s/maintenance/replace-z-belt.md)。

### 涡流线圈报错

1. 对于 **“频率偏低/偏高”** 的报错，请根据以下内容进行排查。

- [HMS\_0300-2500-0001-0001: 右挤出机的涡流传感器频率过低，可能喷嘴未安装或喷嘴散热片距离传感器过远。](hmscode/0300_2500_0001_0001.md)
- [HMS\_0300-2600-0001-0001：左挤出机涡流传感器信号频率过低，可能传感器安装位置过远或传感器已松脱。](hmscode/0300_2600_0001_0001.md)

2. 对于 **“频率异常”** 的报错，请先尝试根据[更换 X2D 工具头电路板](../maintenance/replace-th-board.md)重新安装涡流传感器插头(1 号和 4 号)；若故障依旧，请联系我们的技术团队为您提供帮助。

| 序号 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 接口说明 | 左涡流线圈 | 左霍尔检测板 | 右霍尔检测板 | 右涡流线圈 |

![connector.jpg](https://wiki.bambulab.com/x2d/maintenance/replace-th-board/connector.jpg)

## 功能验证

点击屏幕，重新进行回中。若设备完成回零，则问题解决。

![](https://public-cdn.bblmw.com/wiki/new/x2d/troubleshooting/hmscode/0300_2500_0001_0001/004.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
