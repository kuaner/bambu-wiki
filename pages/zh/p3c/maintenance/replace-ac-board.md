---
path: zh/p3c/maintenance/replace-ac-board
title: "P3C AC 板更换指南"
description: "本文介绍了如何更换 P3C AC 板"
tags: []
created: 2026-11-24T14:06:09.232Z
updated: 2026-11-24T14:06:09.232Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-ac-board
---

### AC 板

简述：AC 板是安装在打印机左内衬中，用于给热床提供交流电输入的电路板。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ac-board/zh/001.png)

AC 板连接器说明如下：  
![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ac-board/zh/002.png)

| 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- |
| 1 | MC 板（通信） | 3 | AC 板电源（蓝色） |
| 2 | AC 板电源（棕色） | 4 | 热床（供电） |

## 何时更换

- AC 板上有明显的烧毁或损坏；
- 热床无法正常加热时可能需要更换 AC 板。

## 所需工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手
- 十字螺丝刀

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 AC 板

### 步骤 1. 移除背板与废料滑梯

您可以参考WIKI：[P3C 废料滑梯更换指南](replace-purge-chute.md)，移除背板及滑梯。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ac-board/zh/003.png)

### 步骤 2. 断开线缆

揭开电源线保护盖，使用十字螺丝刀拧松图示 2 颗螺丝，取下 AC 板 2 根电源线；

|  |  |
| --- | --- |
| 004.png | 005.png |

将插簧硅胶保护套向后推出露出插簧，使用内六角扳手轻顶插簧上的卡扣并向外拔出。

|  |  |
| --- | --- |
| 006.png | 007.webp |

按压线缆端子以解锁卡扣，断开 MC-AC 通信线连接器。

|  |  |
| --- | --- |
| 008.png | 009.png |

### 步骤 3. 移除 AC 板

使用 H1.5 内六角扳手，移除 AC 板 2 颗固定螺丝，随后取下 AC 板。

|  |  |
| --- | --- |
| 010.png | 011.png |

## 安装 AC 板

### 步骤 1. 安装 AC 板

将 AC 板卡入图示内衬上的两处限位结构中；

|  |  |
| --- | --- |
| 012.png | 013.png |

随后使用 H1.5 内六角扳手锁入 2 颗螺丝固定。

![014.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ac-board/zh/014.png)

### 步骤 2. 连接线缆

将 MC-AC 板信号线插入 AC 板接口，然后将热床电源线插簧插回 AC 板接口；

|  |  |
| --- | --- |
| 015.png | 016.png |

将 AC 板电源线 U 型端子卡入电源压线螺丝方形金属片下方，随后使用十字螺丝刀拧紧螺丝，最后盖上电源保护盖。

|  |  |
| --- | --- |
| 017.webp | 018.png |

### 步骤 3. 安装废料滑梯与背板

您可以参考WIKI：[P3C 废料滑梯更换指南](replace-purge-chute.md)，安装废料滑梯和背板。

![019.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ac-board/zh/019.png)

## 功能验证

连接电源线并启动打印机，设置热床温度为 50 ℃，确认热床温度能升高到目标值。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
