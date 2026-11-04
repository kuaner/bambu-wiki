---
path: zh/h3c/maintenance/replace-2521-extruder-servo-motor
title: "挤出电机更换指南"
description: ""
tags: []
created: 2026-11-03T12:47:57.310Z
updated: 2026-11-03T12:47:58.368Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-2521-extruder-servo-motor
---

## 挤出电机

|  |  |
| --- | --- |
| 图 | 图 |

## 工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手
- 专用套筒

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2521-extruder-servo-motor/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除挤出电机

### 第 1 步 移除工具头前盖和顶盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 移除工具头前盖和顶盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2521-extruder-servo-motor/zh/23__________2521_extruder_servo_motor_replacement_guide_3857e0ee6a.jpg)

### 第 2 步 调整从动轮组件位置

在 H2.0 内六角扳手上装上专用套筒，拧动变矩凸轮，使从动轮处于最大作业间距位置，完全露出挤出电机的螺丝。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 移除 TH 板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)， 移除 TH 板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2521-extruder-servo-motor/zh/23__________2521_extruder_servo_motor_replacement_guide_916c916247.jpg)

### 第 4 步 移除挤出电机

用 H1.5 内六角扳手移除 1 颗轴承螺丝（含垫圈）和 3 颗电机固定螺丝。

> 重要：
>
> 1. 轴承螺丝上的弹片不可缺少，请注意保管，并确保在组装时有带上弹片；
> 2. 弹片的方向：三点式的弹片（如图），触点必须朝向轴承；四点式弹片，不用区分方向。

|  |  |
| --- | --- |
| 图 | 图 |

用扳手穿过轴承推电机转轴，将挤出电机向后松出，取下挤出电机（轴承可以保留在支架上）。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装挤出电机

### 第 1 步 安装挤出电机

确认轴承已安装在支架上，将挤出电机从工具头背面装入，如下图所示，电机上的连接器朝向工具头左上角（从后向前看）。前面的手可以协助调整电机转轴的位置，使其从轴承中穿过，也避免轴承被掉落。

|  |  |
| --- | --- |
| 图 | 图 |

先锁入 3 颗螺丝固定电机，然后再锁入轴承螺丝（含垫圈）

|  |  |
| --- | --- |
| 图 | 图 |

> 重要：轴承螺丝上的垫圈不能缺少，请注意保管，并确保在组装时有带上垫圈，垫圈的触点朝向轴承。

### 第 2 步 安装 TH 板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)，安装 TH 板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2521-extruder-servo-motor/zh/01__________2012_toollock_motor_replacement_guide_ef5498ea47.jpg)

### 第 3 步 安装工具头前盖和顶盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，装回工具头的所有外壳。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2521-extruder-servo-motor/zh/01__________2012_toollock_motor_replacement_guide_e6f862449e.jpg)

## 功能验证

连接电源，启动打印机，夹持打印头并进行挤出，确认耗材能正常挤出。  
如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
