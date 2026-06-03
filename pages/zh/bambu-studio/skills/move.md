---
path: zh/bambu-studio/skills/move
title: "Bambu Studio 移动功能"
description: "本文介绍 Bambu Studio 工具栏的移动功能。"
tags: []
created: 2025-03-18T04:10:24.140Z
updated: 2025-07-25T08:55:04.956Z
source: https://wiki.bambulab.com/zh/bambu-studio/skills/move
---

## 功能介绍

如果需要调整对象在盘中位置，可以使用 Bambu Studio 顶部工具栏的“**移动**”功能。

![toolbar-move.png](https://wiki.bambulab.com/bambu-studio/skills/toolbar-move.png)

移动工具可以精确控制打印板上对象的位置，可用于多种目的，包括：

- 调整对象位置：当您需要微调或准确调整打印盘中对象的位置时，可以使用移动功能来移动对象到所需位置。
- 避免碰撞：在打印多个对象或较大尺寸对象时，可能需要调整它们的位置，以避免碰撞或重叠。
- 布局优化：通过移动功能，可以对对象进行重新布局，以实现更有效的利用打印空间，提高打印效率和质量。
- 对准边缘：有时需要将对象对准打印盘的特定边缘或参考点，移动功能可以帮助您快速准确地实现这一目标。

## 使用指南

### 拖动对象移动

选中对象，点击“移动”，鼠标拖动对象，或拖动 XYZ 箭头，移动到目标位置。

![拖动.webp](https://wiki.bambulab.com/bambu-studio/skills/%E6%8B%96%E5%8A%A8.webp)

### 输入坐标移动

- **世界坐标**：以打印盘的 XYZ 轴坐标作为参考点，调整对象在打印盘中的位置。

![世界坐标-对齐.webp](https://wiki.bambulab.com/bambu-studio/skills/%E4%B8%96%E7%95%8C%E5%9D%90%E6%A0%87-%E5%AF%B9%E9%BD%90.webp)

- **物体坐标**：以对象自身坐标系为参考点，沿 XYZ 轴方向调整对象的位置。

![物体坐标.webp](https://wiki.bambulab.com/bambu-studio/skills/%E7%89%A9%E4%BD%93%E5%9D%90%E6%A0%87.webp)

> 注意：每个对象必须有一面作为底面接触打印板，所以无法随意调整 Z 轴方向的移动。而零件可以在 Z 轴方向上自由移动。如下图选择整个“对象”时，Z轴方向不能移动，但选择“对象”的其中一个“零件”则可以移动。  
> ![](https://wiki.bambulab.com/software/bambu-studio/split-to-objects-parts/lingjianxuankong.gif)  
> 点击[这里](../../software/bambu-studio/split-to-objects-parts.md)查看更多对象与零件的区别。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
