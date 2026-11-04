---
path: zh/h3c/maintenance/replace-2012-flexfeed-motor
title: "变距电机更换指南"
description: ""
tags: []
created: 2026-11-03T12:47:47.089Z
updated: 2026-11-03T12:47:48.218Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-2012-flexfeed-motor
---

## 变距电机

安装在工具头上且装有变距凸轮的电机，它通过凸轮主动调整从动轮组件与挤出主动轮之间的距离，从而兼容不同规格的工具。

|  |  |
| --- | --- |
| 图 | 图 |

## 何时更换

电机报错或连接排线损坏。

## 工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手
- 专用套筒

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-flexfeed-motor/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除变距电机

### 第 1 步 移除工具头前盖和顶盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 移除工具头前盖和顶盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-flexfeed-motor/zh/23__________2521_extruder_servo_motor_replacement_guide_3857e0ee6a.jpg)

### 第 2 步 移除从动轮组件

请参考 WIKI：[从动轮组件更换指南](replace-idler-assembly.md)， 移除从动轮组件。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-flexfeed-motor/zh/40__________2012_flexfeed_motor_replacement_guide_f4dc98e7db.jpg)

### 第 3 步 移除挤出主板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)， 松开变距电机排线和移除 TH 板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-flexfeed-motor/zh/40__________2012_flexfeed_motor_replacement_guide_b852131f62.jpg)

### 第 4 步 移除变距电机

取下变距凸轮前方的轴承（如有），用 H1.5 内六角扳手移除 3 颗螺丝。

|  |  |
| --- | --- |
| 图 | 图 |

从挤出接口板连接器处将变距电机的排线往下塞，同时从工具头背面握住变距电机，向后移除变距电机。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装变距电机

### 第 1 步 安装变距电机

电机的连接器对着拖链支架的位置，将电机装入工具头中，并将电机排线从接口板左侧的过线孔伸出。

|  |  |
| --- | --- |
| 图 | 图 |

按住电机，从凸轮一侧锁入 3 颗螺丝固定电机，连接电机排线到挤出接口板，合上盖子。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 调整凸轮位置，检查轴承

安装从动轮组件前，先确认变距凸轮处于以下位置状态，确认是位于下图所示的状态。同时检查轴承：变距凸轮或从动轮组件两个位置须且只须有一个轴承，多了要移除，少了要增加。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 安装从动轮组件

请参考 WIKI：[从动轮组件更换指南](replace-idler-assembly.md)， 安装从动轮组件。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-flexfeed-motor/zh/23__________2521_extruder_servo_motor_replacement_guide_3857e0ee6a.jpg)

### 第 4 步 安装 TH 板和后盖

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)，安装 TH 板和工具头后盖。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 5 步 安装工具头前盖和顶盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 安装工具头顶盖和前盖。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-flexfeed-motor/zh/40__________2012_flexfeed_motor_replacement_guide_5494848a85.jpg)

### 第 6 步 运行标定 （仅更换时用）

> 注意：如果不是更换需要重新标定的配件，请不要运行 Gcode, 可能会导致损坏或出现不可预知的错误。

更换该组件后需要进行标定，请参考 WIKI ：[锁紧和变距电机未进行过机械行程标定，请在标定后再执行其他操作](../troubleshooting/hmscode/0800_1A00_0001_0008.md) 完成标定操作。

## 功能验证

1. 如果是更换配件，设置好打印机后，标定通过即可。
2. 如果是拆装过配件，执行一次夹持工具，操作完成即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
