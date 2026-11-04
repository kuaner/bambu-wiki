---
path: zh/h3c/maintenance/replace-rack-lift-motor
title: "挂架升降电机更换指南"
description: ""
tags: []
created: 2026-11-03T12:45:29.814Z
updated: 2026-11-03T12:48:30.501Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-rack-lift-motor
---

## 挂架升降电机

安装在闪切挂架上，用于抬升或下降泊位组件的电机。

|  |  |
| --- | --- |
| 图 | 图 |

## 闪切挂架框架

构成闪切挂架主体的金属框架\*\*。\*\*

## 何时更换

- 明确的电机故障，如电机报错或产品明显的异响；
- 框架变形

## 工具和材料

- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-rack-lift-motor/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 闪切挂架的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。

## 移除挂架升降电机 / 闪切挂架框架

### 第 1 步 移除闪切挂架

请参考 WIKI：[闪切挂架更换指南](replace-swaptek-rack.md)，将闪切挂架从打印机上移除。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-rack-lift-motor/zh/05_____________chamber_hall_sensor_pack_replacement_guide_a9db373bc4.jpg)

### 第 2 步 移除挂架升降电机

将闪功挂架放置在平台上，用手撕开电机旁边的遮挡片，露出联轴器。

|  |  |
| --- | --- |
| 图 | 图 |

手动调整升降位置，使连轴器的顶丝露出，用 H2.0 内六角扳手拧松靠近电机一侧的 2 颗顶丝\*\*（一般拧松 3~4 圈即可，不需要取下顶丝）\*\*。

|  |  |
| --- | --- |
| 图 | 图 |

竖向放置挂架并使升降电机位于上方，用 H2.0 内六角扳手移除 4 颗螺丝，取下挂架升降电机。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-rack-lift-motor/zh/64____________rack_lift_motor_replacement_guide_79ccb2e3b3.jpg)

### 第 3 步 移除泊位组件（更换闪切挂架框架时用）

用 H1.5 内六角扳手移除 3 颗螺丝，可移除 1 个泊位组件。同样的操作，将余下的 8 个泊位组件都移除，就是需要更换的闪切挂架框架\*\*。\*\*

|  |  |
| --- | --- |
| 图 | 图 |

## 安装挂架升降电机

### 第 1 步 安装泊位组件（更换闪切挂架框架时用）

将 9 个泊位组件依次安装到闪切挂架框架上：对齐安装定位柱，逐个安装并锁入 3 颗螺丝固定。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 调整挂架升降电机的转轴位置

手动旋转电机转轴，使转轴的平口面朝向与电机连接器相反的方向，目的是为了在将电机安装到挂架上后，能看到平口面，以确保有一颗顶丝是顶在平口面上的。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-rack-lift-motor/zh/64____________rack_lift_motor_replacement_guide_e595fab74f.jpg)

### 第 3 步 安装挂架升降电机

竖向放置闪切挂架，对齐螺丝孔位置将电机安装到挂架上，锁入 4 颗螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-rack-lift-motor/zh/64____________rack_lift_motor_replacement_guide_79ccb2e3b3.jpg)

向箭头所示方向扳动联轴器，使电机转轴的平口面能明显展示。拉动挂架使联轴器转动，直至其中 1 颗顶级位于电机转轴的平口面上。

|  |  |
| --- | --- |
| 图 | 图 |

保持顶丝的朝向不变，向电机一侧推动挂架，将联轴器复位，然后锁紧这颗顶丝。拉动挂架将另 1 颗顶丝也显露出来并锁紧。

|  |  |
| --- | --- |
| 图 | 图 |

重新贴回遮挡片。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 4 步 安装闪切挂架

请参考 WIKI：[闪切挂架更换指南](replace-swaptek-rack.md)，将闪切挂架重新装回打印机。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-rack-lift-motor/zh/05_____________chamber_hall_sensor_pack_replacement_guide_9c3e5bdefb.jpg)

## 功能验证

启动打印机，执行一次挂架对位校准，能正常完成却可。

|  |  |
| --- | --- |
| 图 | 图 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
