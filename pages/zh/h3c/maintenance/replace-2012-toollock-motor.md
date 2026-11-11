---
path: zh/h3c/maintenance/replace-2012-toollock-motor
title: "锁紧电机更换指南"
description: ""
tags: []
created: 2026-11-03T13:06:53.807Z
updated: 2026-11-10T08:47:04.049Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-2012-toollock-motor
---

## 锁紧电机

安装在工具头上，用于驱动锁紧组件对工具进行锁定和解除锁定的电机。  
![img_0ff69c1d1c70.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-toollock-motor/zh/img_0ff69c1d1c70.jpg)

## 何时更换

电机报错或连接排线损坏。

## 工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手
- 专用套筒

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![img_01457bbe50f0.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-toollock-motor/zh/img_01457bbe50f0.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除锁紧电机

### 第 1 步 移除工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，移除工具头外壳。  
![img_e35ed3089c67.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-toollock-motor/zh/img_e35ed3089c67.jpg)

### 第 2 步 移除 TH 板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)，移除 TH 板，并松开挤出接口板右侧的锁紧电机排线。

|  |  |
| --- | --- |
| img_97dbde8395af.jpg | img_64e229f704a1.jpg |

### 第 3 步 移除锁紧插销

用 H1.5 内六角扳手移除 1 颗银色螺丝，将专用套筒安装到 H2.0 内六角扳手上。

|  |  |
| --- | --- |
| img_64ae9277ebfb.jpg | img_b069e031a928.jpg |

通过专用套筒顺时针拧动锁紧电机的转轴，将锁紧插销向左退出，然后用手将其拔下。

|  |  |
| --- | --- |
| img_e67d9b28cd7f.jpg | img_4f0a3c2cc7ef.jpg |

### 第 4 步 移除锁紧电机

用 H1.5 内六角扳手移除 3 颗螺丝，从工具头背面握住锁紧电机的同时，另一只手将电机排线从挤出接口板的缺口处向下退，移除锁紧电机。

|  |  |
| --- | --- |
| img_ff7f9e15c8eb.jpg | img_49c3bbb5958e.jpg |

> 温馨提示：如果 2 号位置的螺丝被挤出从动轮干涉，请使用专用套筒拧动变距电机的转轴，使螺丝帽完全露出。

向后拉扯排线时不要用力过大，同时请注意电机转轴上有个轴承，避免跌落。

|  |  |
| --- | --- |
| img_8a0f9359e1a6.jpg | img_5b6880aa62b6.jpg |

## 安装锁紧电机

### 第 1 步 安装锁紧电机

安装 1 个轴承到电机的转轴上，然后将锁紧电机从工具头背面装入，注意拉起电机排线做好避让。

|  |  |
| --- | --- |
| img_5b6880aa62b6.jpg | img_06f2e96558a7.jpg |

安装电机时，锁紧电机连接器处的弧形与挤出电机配合，在工具头前面用手感觉电机的转轴位置，使电机能安装到底。

|  |  |
| --- | --- |
| img_dbe8ead86935.jpg | img_e99d9cb8edbf.jpg |

锁入 3 颗螺丝固定锁紧电机，并整理好电机排线，使排线从挤出接口板的缺口处伸出。

|  |  |
| --- | --- |
| img_ff7f9e15c8eb.jpg | img_401622e760b2.jpg |

将排线连接到连接器上，排线上的白线与连接器边沿齐平，然后合上盖子，并贴上胶布加固。

|  |  |
| --- | --- |
| img_4856ba84c405.jpg | img_52540750eec4.jpg |

### 第 2 步 安装锁紧插销

检查拆下来的锁紧插销，根据定期维护的要求（参考 WIKI：[拓竹H3C 打印机定期维护](periodic-maintenance.md)），有必要时，如图所示添加专用的润滑脂，然后安装到插槽上。

|  |  |
| --- | --- |
| img_bf16879603ff.jpg | img_f94ecb61b020.jpg |

专用润滑脂：

|  |  |
| --- | --- |
| img_6dd05153b735.jpg | img_c093e9bb5337.jpg |

用手抵着插销，使用专用套筒逆时针旋转锁紧电机转轴，让插销继续向右滑动，锁入 1 颗银色限位螺丝。

|  |  |
| --- | --- |
| img_1cbc3dc5df74.jpg | img_64ae9277ebfb.jpg |

### 第 3 步 安装 TH 板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)，安装 TH 板。  
![img_ef5498ea4733.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-toollock-motor/zh/img_ef5498ea4733.jpg)

### 第 4 步 安装工具头前盖和顶盖

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)，装回工具头的所有外壳。  
![img_e6f862449e77.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-2012-toollock-motor/zh/img_e6f862449e77.jpg)

### 第 5 步 运行标定 （仅更换时用）

> 注意：如果不是更换需要重新标定的配件，请不要运行 Gcode, 可能会导致损坏或出现不可预知的错误。

更换该组件后需要进行标定，请参考 WIKI ：[锁紧和变距电机未进行过机械行程标定，请在标定后再执行其他操作](../troubleshooting/hmscode/0800_1A00_0001_0008.md) 完成标定操作。

## 功能验证

1. 如果是更换配件，设置好打印机后，标定通过即可。
2. 如果是拆装过配件，执行一次夹持工具，操作完成即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
