---
path: zh/p3c/maintenance/replace-tool-control-bridge-board
title: "P3C 打印头控制转接板更换指南"
description: "本文介绍了如何更换 P3C 打印头控制转接板"
tags: []
created: 2026-11-24T14:06:30.322Z
updated: 2026-11-24T14:29:29.496Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-tool-control-bridge-board
---

### 打印头控制转接板

简述：安装在打印机后侧，连接 AMS 3P 和打印机 MC 板的中继电路板。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-tool-control-bridge-board/zh/001.png)

## 何时更换

- 线缆或连接器出现物理损坏
- 经拓竹科技技术人员排查，确认是转接板故障的

## 所需工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手
- 打印头控制转接板

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 顶部连接器直接连接到 AMS 3P，请参考 WIKI：[AMS 3P（舱体和支架一体） 拆装指南](replace-ams3p.md)的步骤 4 将 AMS 3P 的连接线断开后再继续。本指南的照片均在已移除 AMS 3P 的场景下拍摄，不影响具体的操作步骤。
>
> |  |  |
> | --- | --- |
> | 002.png | 003.png |

## 移除打印头控制转接板

### 步骤 1. 移除背板

您可以参考WIKI[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的移除。

![004.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-tool-control-bridge-board/zh/004.png)

### 步骤 2. 松出打印头控制转接板

使用撬棒或扳手对准螺丝孔位置，轻轻撬起打印头控制转接板盖，随后将其取下；

|  |  |
| --- | --- |
| 005.png | 006.png |

使用 H1.5 内六角扳手移除打印头控制转接板 2 颗螺丝，并将转接板与其底座一并松出；

|  |  |
| --- | --- |
| 007.png | 008.png |

### 步骤 3. 移除废料滑梯

使用 H2.0 内六角扳手，移除滑梯的 1 颗螺丝，取下滑梯。

|  |  |
| --- | --- |
| 009.png | 010.png |

### 步骤 4. 断开线缆连接

按压 MC 板上的线缆端子以解锁卡扣，逐一拔掉 MC 板上**除了 5 号接头以外**的其他全部线缆接头。

|  |  |
| --- | --- |
| 011.png | 012.png |

使用 H1.5 内六角扳手，移除 MC 板 6 颗螺丝，将 MC 板松出，随后用镊子清理干净 5 号端子上的白胶后，拔除 5 号线缆。

|  |  |
| --- | --- |
| 013.png | 014.png |

### 步骤 5. 移除线缆

沿图示方向将 5 号线缆提起，使打印头控制转接板与线缆一并从金属框架的穿线孔中移除。

![015.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-tool-control-bridge-board/zh/015.png)

## 安装打印头控制转接板

### 步骤 1. 安装 MC 板

将 MC 板安装到右内衬上，使用 H2.0 内六角扳手锁入 6 颗固定螺丝。随后重新连接 MC 板线缆。

|  |  |
| --- | --- |
| 016.png | 017.png |

> **MC 板连接器说明如下：**（红色 “X” 标识的两个连接器不可用，请忽略。）

![018.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-tool-control-bridge-board/zh/018.png)

| **序号** | **连接对象** | **序号** | **连接对象** | **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 后自适应风道组件转接板 | 6 | AP-MC USB通信线 | 11 | 闪切挂架控制板 | 16 | 空 |
| 2 | AP-MC 板信号线 | 7 | AP板电源 | 12 | 空 | X | A 电机 |
| 3 | 空 | 8 | 辅助部件冷却风扇（右） | 13 | AC板信号线 | Y | B 电机 |
| 4 | 6pin接口板/缓冲器 | 9 | 空 | 14 | 空 | Z | Z 电机 |
| 5 | 打印头控制转接板 | 10 | MC 板电源 | 15 | 热床信号线 |  |  |

### 步骤 2. 安装线缆

将线缆穿过打印机金属框架，并把接头插入 MC 板的 5 号接口。

|  |  |
| --- | --- |
| 019.png | 020.png |

> 注意：若在穿梭过程中遇见线缆接头存在阻力或干涉，可适当旋转线缆以调整位置或使用扳手从金属框架上的观察孔中借力。
>
> ![021.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-tool-control-bridge-board/zh/021.png)

### 步骤 3. 安装打印头控制转接板

对准打印机框架上的 2 处定位销，将打印头控制转接板底座安装到位；随后将转接板斜向上对准框架接口插入，并按压到位。

|  |  |
| --- | --- |
| 022.png | 023.webp |

使用 H1.5 内六角扳手锁入转接板 2 颗螺丝固定，随后将转接板盖按压到位，直至听见卡扣发出咔哒声。

|  |  |
| --- | --- |
| 024.png | 025.png |

### 步骤 4. 安装废料滑梯

安装废料滑梯，使用 H2.0 内六角扳手，锁入滑梯的 1 颗螺丝固定。

|  |  |
| --- | --- |
| 010.png | 009.png |

### 步骤 5. 安装背板

您可以参考WIKI：[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的安装。

![026.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-tool-control-bridge-board/zh/026.png)

## 功能验证

启动打印机，执行一次取用打印头的操作，能正常完成即可。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
