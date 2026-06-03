---
path: zh/p2s/manual/cooling-fan-system
title: "P2S 空调系统"
description: "本篇指南介绍了 P2S 自适应空气循环系统的主要构成部件与工作模式。"
tags: []
created: 2025-10-16T09:28:18.932Z
updated: 2026-03-27T06:15:26.743Z
source: https://wiki.bambulab.com/zh/p2s/manual/cooling-fan-system
---

## 自适应空气循环系统

P2S 的自适应空气循环系统主要由**自适应风道切换组件**和**空气滤芯**组成，可根据不同打印场景在**外部吸风冷却模式**和**内循环过滤保温模式**间自动切换，从而调节腔体温度。自适应空气循环系统的主要功能如下：

- **冷却：** 与循环热风的传统冷却系统不同，P2S 的自适应空气循环系统可直接从机箱外吸入冷空气，显著提高冷却效率。打印低温耗材时您可以放心关上打印机舱门，无需担心悬垂质量问题或堵头。
- **保温：** 该系统确保有效地在打印机内部存住热量，从而在打印易翘曲的工程耗材时更加轻松。
- **主动过滤：** 该系统通过高性能多效过滤器主动过滤内部空气，保证工作空间内的干净和安全。

本篇指南为您详细介绍 P2S 自适应空气循环系统的主要构成部件与工作模式。

### 主要部件

#### 自适应风道切换组件

P2S 采用行业首创的**自适应风道切换组件**，您可简单将其理解为具备外部吸风功能的辅助部件冷却风扇。该组件安装在打印机腔室右侧（如下图所示）。

该组件可根据腔温模式切换风道：

- 在打印 PLA 等低温耗材时，该组件可直接将外部环境的冷空气吸进打印机腔体内部，降低腔内温度，防止因腔温过高导致的热端堵头。同时，风扇吹出的冷气会在打印件上形成“气流层”，有助于尽快固化打印层，提升打印效果。
- 在打印高温耗材时，该组件则不再吸入冷空气，而与空气滤芯形成内循环。  
  ![26-aux-part-cooling-fan.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/p2s-intro/26-aux-part-cooling-fan.png)

> 为了实现更加平衡的冷却效果，您也可额外在机箱左侧加装一个**辅助部件冷却风扇**，具体方法详见 [加装辅助部件冷却风扇（左）](../maintenance/install-auxiliary-part-cooling-fan-left.md)。

#### 空气滤芯

空气滤芯位于机箱右后侧（如下图所示）。

在内循环过滤保温模式下，腔体空气经由滤芯后方的进风口被吸入，并通过滤芯进行过滤与净化，有效降低颗粒物和气味排放。相比 P1 系列，P2S 空气滤芯面积更大，过滤效果更佳。  
![27-air-filter.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/p2s-intro/27-air-filter.png)

#### **部件冷却风扇**

快速打印需要对打印部件进行良好的冷却，P2S 配备了一个定制的 5815 离心风扇，位于工具头上（如下图所示）。风扇会吹出冷却空气到热端喷嘴附近，确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。  
![19-part-cooling-fan.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/p2s-intro/19-part-cooling-fan.jpg)

其 UI 界面如下：

![cooling-en.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/part-cooling-fan--cn.png)

#### **自适应风道切换组件**

位于机腔内右侧面板，能为高速打印提供更好的冷却条件。其 UI 界面如下：

![cooling-en.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/heat--cn.png)

### 工作模式

P2S 打印机的空调系统共有两种工作模式，分别是**冷却模式**与**腔温保持模式**。

#### **冷却模式**

在打印 PLA 等低温耗材时，打印机处于外部吸风冷却模式。该模式的工作原理如下：

- 自适应风道切换组件直接将外部环境的冷空气吸进打印机腔体内部，降低腔体内温度，帮助热端及打印件散热，提升打印质量、避免热端堵头。
- 腔体内原有的热空气会通过打印机背板散热孔和吐料组件缝隙排出。

|  |  |
| --- | --- |
|  |  |

P2S 不配备外排风扇。即使在自适应风道切换组件高速运转时，整机依然能保持较低噪音，相比 P1S 的外排风扇方案更加安静。

冷却模式的 UI 界面如下：

![air-condition-cn-1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/air-condition-cn-1.png)

#### **腔温保持模式**

P2S 无主动腔温控制系统，但可通过内循环实现腔体内的空气加热与过滤。该模式的工作原理如下：

1. 通过热床与热端加热后的高温辐射加热腔体内空气。
2. 自适应风道切换组件不再从外部吸取冷空气，而与空气滤芯共同形成内循环，在保证腔体内部热空气均匀性的同时对空气进行过滤和净化。

![30-heating-mode.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/p2s-intro/30-heating-mode.png)

该模式的 UI 界面如下：

![air-condition-cn-1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/air-condition-cn-2.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
