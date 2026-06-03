---
path: zh/filament-acc/filament/print-quality/seam
title: "接缝"
description: ""
tags: ["打印质量", "接缝"]
created: 2023-12-10T06:02:40.137Z
updated: 2024-05-28T11:05:42.869Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/seam
---

# 接缝

**在 FDM 3D 打印中，每层打印的起始点和终点的走线交界处都会形成一个接缝，这是正常的现象。要了解更多关于接缝的知识，可以点击这个 wiki 链接：**[**Seam | Bambu Lab Wiki。**](../../../../en/software/bambu-studio/Seam.md)

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%88%87%E7%89%87%E6%8E%A5%E7%BC%9D.jpeg)
![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%9C%86%E6%9F%B1%E6%8E%A5%E7%BC%9D.png)

**可以采用以下方法来适当改善接缝的质量：**

1. 把墙的层数设置为 3；

2. 尽量避免在同一盘上打印多个模型，以减少工具头的空驶；

3. 适当提升喷嘴温度、降低外墙打印速度；

4. 对于某些特殊模型，可启用旋转花瓶模式。启用“旋转花瓶”模式后，模型的墙将会以一条走线螺旋上升的方式打印，接缝将只出现于模型底部的那几层，而完全不会出现在外墙上。注意：该模式打出来的模型只有单层外壁，无填充和顶壳，且只适用于一些简单模型（复杂模型无法用单条走线完成时会导致切片后会有悬空部分）。详情可以参考wiki：[旋转花瓶 | Bambu Lab Wiki](../../../software/bambu-studio/spiral-vase.md)。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%97%8B%E8%BD%AC%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F%E5%BC%80%E5%90%AF.png)
