---
path: zh/cyberbrick/troubleshooting/fix-the-drifting
title: "如何纠正舵机转向，解决小车跑偏？"
description: "本文将详细讲解舵机转向的纠正方法，帮助解决小车跑偏问题。"
tags: []
created: 2025-09-19T11:52:28.379Z
updated: 2026-05-12T09:03:30.469Z
source: https://wiki.bambulab.com/zh/cyberbrick/troubleshooting/fix-the-drifting
---

如果发现小车在直行时跑偏，可以通过以下**舵机偏置** 来校正：

## 修复步骤

1. 在PC软件中，打开当前**项目配置界面**。
2. 在配置界面中，找到 **角度舵机** 配置项**「偏置」**

![1_角度舵机设置.gif](https://wiki.bambulab.com/cyberbrick/1_%E8%A7%92%E5%BA%A6%E8%88%B5%E6%9C%BA%E8%AE%BE%E7%BD%AE.gif)

- 根据小车运行情况进行调节：

  - 若小车向 **左偏**，请调大偏置值；
  - 若小车向 **右偏**，请调小偏置值。

![2_更改偏值设置.gif](https://wiki.bambulab.com/cyberbrick/2_%E6%9B%B4%E6%94%B9%E5%81%8F%E5%80%BC%E8%AE%BE%E7%BD%AE.gif)

- 保存配置并发送到核心板，测试效果，直至小车能保持直行。

### 原理解析

在旧版本中，舵机角度的中点（mid）固定为 `(max + min) / 2`，无法灵活调整。如果舵机机械中点与实际小车直行方向不一致，会导致跑偏。

在新版本（RC\_MPY\_1.0.0.4）中，引入了 **bias 参数**。

- bias 用于在计算 **真实最小值（real\_min）和最大值（real\_max）** 时进行修正：

  - `real_min = min + bias`
  - `real_max = max + bias`
- 这样，即使舵机的物理中点与小车直行方向存在偏差，也能通过调整 bias 来对齐，使小车在逻辑中点处保持直行。

因此，**调节 bias 就是人为移动舵机的中点位置**，从而纠正小车跑偏问题。

![](https://wiki.bambulab.com/cyberbrick/troubleshooting/forget-the-pin-code/diagram.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
