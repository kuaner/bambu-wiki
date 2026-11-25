---
path: zh/p3c/maintenance/replace-mc-board
title: "P3C MC 板更换指南"
description: "本文介绍了如何更换 P3C MC 板"
tags: []
created: 2026-11-24T14:06:07.831Z
updated: 2026-11-24T14:06:07.831Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-mc-board
---

## MC 板

简述：MC板的全称是 Main Control Board，中文通常称为 “主控板” ，它是一块集成了微处理器、各种驱动芯片、接口和电路的印刷电路板。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-mc-board/zh/001.png)

**MC 板连接器说明如下：**（红色 “X” 标识的两个连接器不可用，请忽略。）

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-mc-board/zh/002.png)

| **序号** | **连接对象** | **序号** | **连接对象** | **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 后自适应风道组件转接板 | 6 | AP-MC USB通信线 | 11 | 闪切挂架控制板 | 16 | 空 |
| 2 | AP-MC 板信号线 | 7 | AP板电源 | 12 | 空 | X | A 电机 |
| 3 | 空 | 8 | 辅助部件冷却风扇（右） | 13 | AC板信号线 | Y | B 电机 |
| 4 | 6pin接口板/缓冲器 | 9 | 空 | 14 | 空 | Z | Z 电机 |
| 5 | 打印头控制转接板 | 10 | MC 板电源 | 15 | 热床信号线 |  |  |

## 何时更换

- MC 板外观存在明显的元器件或连接器损坏；
- 经拓竹专业技术检测确认是 MC 板所关联的故障。

## 所需工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手
- MC 板

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 MC 板

### 步骤 1. 移除背板

您可以参考WIKI：[P3C 背板更换指南](replace-back-panel.md) ，完成 6-pin 接口板/缓冲器和背板的移除。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-mc-board/zh/003.png)

### 步骤 2. 移除废料滑梯

使用 H2.0 内六角扳手，移除滑梯的 1 颗螺丝，取下滑梯。

|  |  |
| --- | --- |
| 004.png | 005.png |

### 步骤 3. 断开线缆

按压 MC 板上的线缆端子以解锁卡扣，逐一拔掉 MC 板上**除了 5 号接头以外**的其他全部线缆接头。

|  |  |
| --- | --- |
| 006.png | 007.png |

### 步骤 4. 移除 MC 板

使用 H1.5 内六角扳手，移除 MC 板 6 颗螺丝，将 MC 板松出，随后用镊子清理干净 5 号端子上的白胶后，拔除 5 号线缆移除 MC 板。

|  |  |
| --- | --- |
| 008.png | 009.png |

## 安装 MC 板

### 步骤 1. 安装 MC 板

将 MC 板安装到右内衬上，使用 H2.0 内六角扳手锁入 6 颗固定螺丝。

|  |  |
| --- | --- |
| 010.png | 011.png |

### 步骤 2. 连接线缆

将线缆接头逐一插入 MC 板端接口。

|  |  |
| --- | --- |
| 012.png | 013.png |

### 步骤 3. 安装废料滑梯

对齐右内衬上的安装卡扣，将废料滑梯安装到吐料组件的下方；

|  |  |
| --- | --- |
| 014.png | 015.png |

随后使用 H2.0 内六角扳手锁入废料滑梯 1 颗固定螺丝。

![016.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-mc-board/zh/016.png)

### 步骤 4. 安装背板

您可以参考WIKI[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的安装。

![017.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-mc-board/zh/017.png)

## 功能验证

连接电源线并启动打印机，执行一次打印机回零的操作，确认能执行并通过。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
