---
path: zh/software/bambu-studio/assemble
title: "装配工具"
description: "介绍装配工具和使用方法"
tags: ["bambu studio"]
created: 2024-06-19T07:06:06.310Z
updated: 2026-08-28T08:28:55.275Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/assemble
---

过去，如果想要装配两个模型，需要精确地调整两个模型的坐标，才能将他们恰好装配贴合在一起。在 Bambu Studio 1.9 版本中，我们开发了装配功能，可以快速实现模型装配。该功能分为**点和点装配**和**面和面装配**。

![assemble_1.png](https://wiki.bambulab.com/software/bambu-studio/assemble/assemble_1.png)

## 点和点装配

选择**点和点装配**后，可以在两个物体上选择两个点，然后指定它们之间的距离。

在使用点对点装配功能之前，建议先把两个物体组合成同一个对象。因为组合成对象后，两个物体均属于零件，可以随意调整 Z 方向上的高度。零件和对象的区别请查看[拆分为对象/零件](split-to-objects-parts.md)。

如果未组合，每个独立的对象必须有一个面贴合着热床，且 Z 方向上的高度不可调整。

![assemble_1.png](https://wiki.bambulab.com/software/bambu-studio/assemble/assemble__2.webp)

## 面和面装配

选择**面和面装配**，也可以在两个物体上选择两个面并组合在在一起。

![assemble_1.png](https://wiki.bambulab.com/software/bambu-studio/assemble/assemble_3.png)

同理，先把两个物体组合成一个对象。然后选择两个面。

- **平行**：如果是两个非平行的面，可以点击**平行**，使两个面平行。然后。可以设置两个平面的距离。
- **中心重合**：将选中的两个面贴合，从而将两个物体组合在一起。
- **通过面 2 翻转**：沿着面 2 翻转物体 2。

![assemble_1.png](https://wiki.bambulab.com/software/bambu-studio/assemble/assemble__4.webp)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
