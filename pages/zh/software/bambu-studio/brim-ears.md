---
path: zh/software/bambu-studio/brim-ears
title: "耳状Brim"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-10-14T06:16:32.707Z
updated: 2026-04-16T01:39:59.410Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/brim-ears
---

在3D打印过程中，由于材料局部收缩或与打印床的粘附力不足，模型常常会出现翘边现象，尤其是在使用ABS或ASA等易收缩的材料时。为了解决这一问题，你可以在Bambu Studio中添加Brim或提高热床温度，以增强模型首层的粘附性[（详细信息可参见Bambu Lab Wiki上的“模型翘边、脱落或倒塌”）](../../filament-acc/filament/print-quality/warping-falling-off-collapsing.md)。然而，有时候Brim拆除较为麻烦，有些区域并不需要添加，我们需要针对需要在有尖角处添加Brim,这时使用耳状Brim工具能够更方便解决这些问题。

|  |  |
| --- | --- |
| **模型翘边** | **耳状Brim 拉住边角防止翘边** |
|  |  |

## Brim类型设置为“绘制”

首先，要确保Brim类型设置为**绘制**模式，否则切片将不会生成耳状Brim。当你选择特定对象设置耳状Brim时，操作界面会有相关提醒，您可以直接点击“将Brim类型设为绘制模式”更改该对象的Brim类型。

![painted.png](https://wiki.bambulab.com/software/bambu-studio/brim-ears/painted.png)
![](https://wiki.bambulab.com/software/bambu-studio/brim-ears/brim类型设为绘制.gif)

## 用户操作界面

![ui.png](https://wiki.bambulab.com/software/bambu-studio/brim-ears/ui.png)

## Brim直径

用于设置放置耳状Brim的直径，单位是毫米。

![brim_redius.png](https://wiki.bambulab.com/software/bambu-studio/brim-ears/brim_redius.png)

## 最大角度

使用“自动生成点”时，检测模型的首层轮廓，当转角处角度小于此值时生成耳状Brim。

![max_angle.gif](https://wiki.bambulab.com/software/bambu-studio/brim-ears/max_angle.gif)

## 检测半径

使用“自动生成点”时，使用[道格拉斯-普克算法](https://zh.wikipedia.org/wiki/%E9%81%93%E6%A0%BC%E6%8B%89%E6%96%AF-%E6%99%AE%E5%85%8B%E7%AE%97%E6%B3%95)拟合简化模型首层轮廓。设置值越大，生成的耳状Brim越少。

![radius.gif](https://wiki.bambulab.com/software/bambu-studio/brim-ears/radius.gif)

## 手动绘制

可以直接在模型上自由添加耳状Brim，左键点击模型添加，右键点击删除。也可以鼠标左键+shift同时选中多个耳状Brim，然后点击“删除已选择的点”，一次性删除多个耳状Brim。点击“删除所有点”可以删除所有已添加的耳状Brim。

![](https://wiki.bambulab.com/software/bambu-studio/brim-ears/手动添加删除brimear.gif)

**注意：无论是自动生成的还是手动绘制的耳状Brim，在退出编辑窗口后，它都将暂时不可见，只有在切片后你才能看到添加耳状Brim后的效果。**

![](https://wiki.bambulab.com/software/bambu-studio/brim-ears/切片后brim可见.gif)
