---
path: zh/p3c/maintenance/replace-chamber-liner-back-right
title: "P3C 右后内衬更换指南"
description: "本指南主要介绍更换 P3C 左后内衬的具体操作方式。"
tags: []
created: 2026-11-24T14:07:00.935Z
updated: 2026-11-24T14:07:00.935Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-chamber-liner-back-right
---

## 右后内衬

简述：右内衬是位于打印机后部右侧的塑料支架，用于承载 MC 板、AC 板、电源模块等电路元件及废料滑梯、吐料组件等配件。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/001.png)

## 何时更换

打印机左内衬出现变形或损坏。

## 所需工具和材料

- 右后内衬
- H2.0 内六角扳手
- 十字螺丝刀

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

## 移除右后内衬

### 步骤 1. 移除背板

请参考WIKI：[背板更换指南](replace-back-panel.md) ，完成 6-pin 接口板/缓冲器和背板的移除。

![004.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/004.png)

### 步骤 2. 移除右侧板

请参考wiki：[P3C 侧板更换指南](replace-side-panel-left.md)，移除右侧板。

![005.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/005.png)

### 步骤 3. 移除废料滑梯

使用 H2.0 内六角扳手，移除滑梯的 1 颗螺丝，取下滑梯。

|  |  |
| --- | --- |
| 006.png | 007.png |

### 步骤 4. 移除 MC 板、AC 板、电源模块

请参考Wiki，逐一将 MC 板、AC 板、电源模块移除；

MC 板：[P3C MC 板更换指南](replace-mc-board.md)

AC 板：[P3C AC 板更换指南](replace-ac-board.md)

电源模块：[P3C 电源更换指南](replace-power-supply.md)

![008.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/008.jpg)

### 步骤 5. 松出线缆

将右后内衬上方穿线孔中的线缆松出到穿线孔外；然后将 Z 电机线缆从内衬下方线槽中松出。

|  |  |
| --- | --- |
| 009.jpg | 010.jpg |
| 011.jpg |

### 步骤 6. 移除右后内衬

使用 H2.0 内六角扳手移除图示内衬上下共 6 颗粗牙螺丝；

|  |  |
| --- | --- |
| 012.jpg | 013.jpg |

随后使用 H2.0 内六角扳手移除图示内衬侧面的 3 颗细牙螺丝，即可将内衬从侧面位置移除。

|  |  |
| --- | --- |
| 014.jpg | 015.jpg |

### 步骤 7. 移除吐料组件

使用 H2.0 内六角扳手，移除吐料组件与内衬的 3 颗固定螺丝，随后向上提起并移除吐料组件。

|  |  |
| --- | --- |
| 016.jpg | 017.jpg |

## 安装右后内衬

### 步骤 1. 安装吐料组件

将吐料组件装回到内衬上，并使用 H2.0 内六角扳手，锁入吐料组件与内衬的 3 颗固定螺丝。

|  |  |
| --- | --- |
| 018.jpg | 019.jpg |

### 步骤 2. 安装右后内衬

将内衬从侧面位置放入打印机腔内，使用 H2.0 内六角扳手锁入图示内衬侧面的 3 颗细牙螺丝；

|  |  |
| --- | --- |
| 020.jpg | 021.jpg |

使用 H2.0 内六角扳手锁入图示内衬上下共 6 颗粗牙螺丝；

|  |  |
| --- | --- |
| 022.jpg | 023.jpg |

### 步骤 3. 整理线缆

将 MC 板端接口 “Y、5、11” 线缆穿过内衬上方的穿线孔；然后将 Z 电机线缆穿过内衬下方线槽，埋入内衬线扣中；

|  |  |
| --- | --- |
| 024.jpg | 025.jpg |
| 026.jpg |

### 步骤 4. 安装 MC 板、AC 板、电源模块

请参考Wiki，逐一将 MC 板、AC 板、电源模块装回内衬，并将线缆接头重新连接到电路板接口中。

MC 板：[P3C MC 板更换指南](replace-mc-board.md)

AC 板：[P3C AC 板更换指南](replace-ac-board.md)

电源模块：[P3C 电源更换指南](replace-power-supply.md)

![027.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/027.jpg)

### 步骤 5. 安装废料滑梯

将滑梯装回到内衬，并使用 H2.0 内六角扳手，锁入滑梯的 1 颗螺丝。

|  |  |
| --- | --- |
| 028.png | 029.png |

### 步骤 6. 安装右侧板

请参考wiki：[P3C 侧板更换指南](replace-side-panel-left.md)，安装右侧板。

![030.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/030.png)

### 步骤 7. 安装背板

您可以参考WIKI：[背板更换指南](replace-back-panel.md) ，完成背板和其他配件的安装。

![031.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-chamber-liner-back-right/zh/031.png)

## 功能验证

接上打印机电源，开启打印机，在屏幕上操作，运行校准流程，如成功校准，说明上述操作成功。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
