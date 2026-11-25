---
path: zh/p3c/maintenance/replace-ptfe-tube-guide-assembly
title: "P3C 料管导向组件更换指南"
description: "本文介绍了如何更换 P3C 料管导向组件"
tags: []
created: 2026-11-24T14:06:31.120Z
updated: 2026-11-24T14:06:31.120Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-ptfe-tube-guide-assembly
---

## 料管导向组件

简述：料管导向组件采用塑料中空结构，位于 AMS 舱体与主料管支架之间，用于 AMS 舱体与料管之间的对接与导向。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ptfe-tube-guide-assembly/zh/001.png)

## 何时更换

- 料管导向组件结构受损
- 料管导向组件内部严重堵塞，常规清理无法恢复

## 所需工具和材料

- H2.0 内六角扳手
- 料管导向组件

## 安全提示

> 重要提醒 ！
>
> 在对 AMS 及其内部电子设备进行任何维护工作之前，请关闭 AMS 及打印机电源，并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 拆装过程中请避免暴力操作，防止造成零部件或连接结构的二次损伤。
>
> 断开插头前，建议拍照记录各插头的连接位置，便于后续按正确顺序恢复连接。

## 拆装提示

> 本指南是在已移除 AMS 3P 舱体的情况操作的，请参考WIKI: [AMS 3P 舱体拆装指南](replace-chamber.md) ，完成将 AMS 舱体从AMS 支架上移除和安装的操作。

## 移除料管导向组件

### 步骤 1. 断开打印头插头与料管

使用 H2.0 内六角扳手拆下料管导向组件左右两侧顶部的 2 颗螺丝；

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ptfe-tube-guide-assembly/zh/002.png)

断开打印头控制板两侧的线缆后，向上提起料管导向组件，逐一断开打印头与控制板之间的 6-pin 线缆；

|  |  |
| --- | --- |
| 003.png | 004.png |

按压气动接头，逐一拔除 PTFE 管，将料管导向组件与打印头控制板整个从打印机上移除。

|  |  |
| --- | --- |
| 005.png | 006.png |

### 步骤 2. 移除打印头控制板

使用H2.0 内六角扳手，将打印头控制板与料管导向组件分离。

|  |  |
| --- | --- |
| 007.png | 008.png |

## 安装料管导向组件

### 步骤 1. 安装料管导向组件

将料管导向组件对齐料管支架上方的定位销嵌入到底。

![009.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ptfe-tube-guide-assembly/zh/009.png)

### 步骤 2. 连接料管

面向机器背面，料管导向组件上的 7 根铁氟龙料管从右到左依次编号为 1 至 7 号，请根据左右料管支架上的料管编号，依次将料管插回料管导向组件。

![010.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ptfe-tube-guide-assembly/zh/010.png)

### 步骤 3. 安装打印头控制板

将打印头按序连接到打印头控制板，装回到料管导向组件上，并锁入 4 颗螺丝固定，随后将两侧线缆插入连接到控制板。

|  |  |
| --- | --- |
| 011.png | 012.png |

### 步骤 4. 整理打印头线缆

为确保打印头线缆长度适宜并防止工具头运动时发生干涉，请调整线缆并检查中间卡扣是否对准空心橙色丝印中心。

![013.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-ptfe-tube-guide-assembly/zh/013.png)

## 功能验证

开启设备电源，通过屏幕操作 AMS 送料，送料过程系统无错误提示。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
