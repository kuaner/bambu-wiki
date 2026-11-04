---
path: zh/h3c/maintenance/replace-nozzle-eddy-sensor
title: "涡流线圈更换指南"
description: ""
tags: []
created: 2026-11-03T12:47:25.361Z
updated: 2026-11-03T12:47:26.403Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-nozzle-eddy-sensor
---

## 涡流线圈

涡流线圈是安装在工具头的左前侧，用于实现关联校准功能的配件。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-eddy-sensor/zh/82__________nozzle_eddy_sensor_replacement_guide_2c6efab604.jpg)

## 何时更换

- 涡流线圈出现物理损坏；
- Z轴回零、热床调平失败，经技术分析为涡流线圈故障。

## 工具和材料

- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-eddy-sensor/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除涡流线圈

### 第 1 步 移除工具头前盖和顶盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 移除工具头前盖和顶盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-eddy-sensor/zh/23__________2521_extruder_servo_motor_replacement_guide_3857e0ee6a.jpg)

### 第 2 步 移除涡流线圈

用 H1.5 内六角扳手移除 1 颗螺丝，取下金属压片。

|  |  |
| --- | --- |
| 图 | 图 |

用 H1.5 内六角扳手移除 2 颗螺丝，松开涡流线圈支架。

|  |  |
| --- | --- |
| 图 | 图 |

沿着线缆的路径，将线缆从卡扣中松出，然后将插头从挤出接口板上断开，移除涡流线圈。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装涡流线圈

### 第 1 步 安装涡流线圈

将涡流线圈的插头连接到挤出接口板的连接器上，沿着布线路径将线缆压入卡扣中。

|  |  |
| --- | --- |
| 图 | 图 |

将线圈座子安装到滑车上，注意线圈朝外。用手临时按着，锁入 2 颗螺丝固定线圈座。

|  |  |
| --- | --- |
| 图 | 图 |

装回金属压片，锁入 1 颗螺丝固定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-eddy-sensor/zh/82__________nozzle_eddy_sensor_replacement_guide_dca063584c.jpg)

### 第 2 步 安装工具头顶盖和前盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 安装工具头顶盖和前盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-nozzle-eddy-sensor/zh/40__________2012_flexfeed_motor_replacement_guide_5494848a85.jpg)

## 功能验证

启动打印机，执行一次 Z 轴回零操作，确认没有报错。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
