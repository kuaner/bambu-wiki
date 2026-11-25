---
path: zh/p3c/maintenance/replace-chamber-liner-back-left
title: "P3C 左后内衬更换指南"
description: "本指南主要介绍更换 P3C 左后内衬的具体操作方式。"
tags: []
created: 2026-11-24T14:06:56.629Z
updated: 2026-11-24T14:06:56.629Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-chamber-liner-back-left
---

## 左后内衬

简述：左后内衬是位于打印机左侧后部的塑料支架，用于承载空气滤芯、滤芯盖、后自适应风扇、风道等配件。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-left/zh/001.png)

## 何时更换

打印机左内衬出现变形或损坏。

## 所需工具和材料

- 左后内衬
- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> - 为了避免热床干涉内衬的移除，请在拆装前启动打印机，在屏幕上点击下降热床的图标，将热床下降到底部。
>
> |  |  |
> | --- | --- |
> | 002.png | 003.png |
>
> - 本指南是在已移除 AMS 的情况下操作的，请参考WIKI: [AMS 3P（舱体和支架一体） 拆装指南](replace-ams3p.md) 完成将 AMS 从打印机上移除和安装的操作。

## 移除左后内衬

### 步骤 1. 移除背板

请参考WIKI：[背板更换指南](replace-back-panel.md) ，完成 6-pin 接口板/缓冲器和背板的移除。

![004.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-left/zh/004.png)

### 步骤 2. 移除左侧板

请参考wiki：[P3C 侧板更换指南](replace-side-panel-left.md)，移除左侧板。

![005.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-left/zh/005.png)

### 步骤 3. 松出线缆

使用 H2.0 内六角扳手，移除滑梯的 1 颗螺丝，取下滑梯。

|  |  |
| --- | --- |
| 006.png | 007.png |

按压 MC 板端 2、6、7 号接头解锁卡扣并断开连接，将线缆从理线扣中松出，并最终将 2、6、7 号线缆松出到内衬穿线孔外。

|  |  |
| --- | --- |
| 008.jpg | 009.jpg |

### 步骤 4. 移除后自适应风道与风扇

请参考Wiki：[P3C 后自适应风道组件更换指南](replace-adaptive-airflow-duct-back.md)、[P3C 后自适应风扇更换指南](replace-adaptive-airflow-fan-back.md)，移除后自适应风道和风扇。

|  |  |
| --- | --- |
| 010.jpg | 011.jpg |

### 步骤 5. 移除空气滤芯盖和滤芯

用 H2.0 内六角扳手撬起滤芯盖，将滤芯盖移除；随后拖动空气滤芯的拉带，将滤芯移除。

|  |  |
| --- | --- |
| 012.png | 013.jpg |

### 步骤 6. 移除左后内衬

使用 H2.0 内六角扳手移除内衬与底座连接的 3 颗螺丝；随后再移除内衬上方的 3 颗螺丝；

|  |  |
| --- | --- |
| 014.jpg | 015.jpg |

使用 H2.0 内六角扳手移除左后内衬侧面的 3 颗**细牙**螺丝；随后从侧面将左后内衬移除。

|  |  |
| --- | --- |
| 016.jpg | 017.jpg |

## 安装左后内衬

### 步骤 1. 安装左后内衬

将左后内衬从侧面放入打印机腔内，预装到位。（左后内衬为塑料材质，韧性较好。安装时如与打印机框架发生干涉，可轻微扳动内衬，使其就位）

|  |  |
| --- | --- |
| 018.jpg | 019.jpg |

### 步骤 2. 安装空气滤芯与滤芯盖

将滤芯安装到内衬上，有拉带的一面面向打印机腔内一侧；然后将空气滤芯盖 3 个卡扣对准内衬上的安装槽装入，随后按压滤芯盖直至发出咔哒声表示安装到位。

|  |  |
| --- | --- |
| 020.png | 021.png |

### 步骤 3. 安装后自适应风扇与风道

请参考Wiki：[P3C 后自适应风道组件更换指南](replace-adaptive-airflow-duct-back.md)、[P3C 后自适应风扇更换指南](replace-adaptive-airflow-fan-back.md)，安装后自适应风道和风扇。

|  |  |
| --- | --- |
| 022.jpg | 023.jpg |

### 步骤 4. 整理线缆

将 Z 电机线缆埋入到内衬下方的理线槽中，然后将 2、6、7 线缆穿过内衬上的穿线孔，并整理到理线扣中；

|  |  |
| --- | --- |
| 024.jpg | 025.jpg |

将线缆插入到 MC 板上对应的 2、6、7 号接口中；随后安装废料滑梯，并锁入 1 颗螺丝固定。

|  |  |
| --- | --- |
| 026.jpg | 027.png |

### 步骤 5. 安装左侧板

请参考wiki：[P3C 侧板更换指南](replace-side-panel-left.md)，安装左侧板。

![028.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-left/zh/028.png)

### 步骤 6. 安装背板

您可以参考WIKI：[背板更换指南](replace-back-panel.md) ，完成背板和其他配件的安装。

![029.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-left/zh/029.png)

## 功能验证

接上打印机电源，开启打印机，在屏幕上操作，运行校准流程，如成功校准，说明上述操作成功。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
