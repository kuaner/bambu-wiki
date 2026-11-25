---
path: zh/p3c/maintenance/replace-6-pin-port-board
title: "P3C 缓冲器/ 6pin 接口板更换指南"
description: "本文介绍了如何更换 P3C 缓冲器/ 6pin 接口板"
tags: []
created: 2026-11-24T14:06:33.232Z
updated: 2026-11-24T14:06:33.232Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-6-pin-port-board
---

## 6pin 接口板

简述：连接 AMS 3P 并为 AMS 3P 提供低压供电的接口电路板。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-6-pin-port-board/zh/001.png)

## 缓冲器

> 缓冲器非标配，如有连接外置 AMS 的需求，可选购适用 P3C 的缓冲器。
>
> ![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-6-pin-port-board/zh/002.png)

## 何时更换

- 连接器损坏或板件上有明显的元器件脱落或烧毁。
- 经技术支持判断，是 6-pin 接口板导致的 AMS 通信故障。

## 所需工具和材料

- H2.0 内六角扳手
- 6-pin 接口板（缓冲器）

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 6-pin 接口板

### 步骤 1. 移除螺丝

使用 H2.0 内六角扳手，移除图示 2 颗固定螺丝。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-6-pin-port-board/zh/003.png)

### 步骤 2. 移除 6-pin 接口板

按压接口板连接器锁扣解锁，断开连接线缆，取下 6-pin 接口板。

|  |  |
| --- | --- |
| 004.png | 005.png |

> 如果更换内容包括 6-pin 接口板/缓冲器的连接线，请参考 [P3C 背板更换指南](replace-back-panel.md) 在拆除打印机背板后进行更换。将线缆从图示 MC 板上编号为 4 的连接器上断开，并从卡扣上松出即可。
>
> ![006.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-6-pin-port-board/zh/006.png)

## 安装 6-pin 接口板

### 步骤 1. 安装 6-pin 接口板

将线缆接头插回接口板连接器座，随后将接口板下方的卡扣斜向下插回背板卡槽安装到位。

|  |  |
| --- | --- |
| 007.png | 008.png |

### 步骤 2. 紧固螺丝

使用 H2.0 内六角扳手锁入 2 颗固定螺丝。

![009.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-6-pin-port-board/zh/009.png)

---

## 移除缓冲器

### 步骤 1. 移除螺丝

外置 AMS 操作退料后，按压 6-pin 线锁扣解锁并断开连接；随后使用 H2.0 内六角扳手移除缓冲器 2 颗螺丝；

|  |  |
| --- | --- |
| 010.png | 011.png |

### 步骤 2. 移除缓冲器

按压缓冲器排线锁扣解锁，断开连接线缆，移除缓冲器。

|  |  |
| --- | --- |
| 012.png | 013.png |

> 如果更换内容包括 6-pin 接口板/缓冲器的连接线，请参考 [P3C 背板更换指南](replace-back-panel.md) 在拆除打印机背板后进行更换。将线缆从图示 MC 板上编号为 4 的连接器上断开，并从卡扣上松出即可。
>
> ![014.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-6-pin-port-board/zh/014.png)

## 安装缓冲器

### 步骤 1. 安装缓冲器

将线缆接头插回缓冲器电路板接口，随后将缓冲器下方的卡扣斜向下插回背板卡槽安装到位；

|  |  |
| --- | --- |
| 015.png | 016.png |

### 步骤 2. 锁入螺丝

使用 H2.0 内六角扳手锁入缓冲器 2 颗固定螺丝。并将线缆与上下两端料管重新连接好。

|  |  |
| --- | --- |
| 017.png | 018.png |

## 功能验证

通过 6-pin 连接线连接到 AMS 3P，接上打印机电源并启动打印机，确认 AMS 3P 供电响应正常。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
