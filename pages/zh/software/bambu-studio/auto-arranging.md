---
path: zh/software/bambu-studio/auto-arranging
title: "自动摆盘功能"
description: ""
tags: []
created: 2023-08-09T02:56:47.679Z
updated: 2026-05-15T06:22:59.192Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/auto-arranging
---

自动摆盘功能是 Bambu Studio 中用于自动整理打印板上多个对象的功能。该功能可优化对象间距、减少手动操作，加快打印准备速度。本指南介绍了如何使用自动摆盘功能高效地摆放模型。

## 如何使用

自动摆盘功能有两种**开启方法**：

1. 点击最上方工具栏中的 **自动摆盘** 按钮，即可重新摆盘。

![arrange_all_objects_in_the_toolbar.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_arrange_all_objects_in_the_toolbar.png)

若一盘内的对象过多，则会自动添加新盘来摆放。

![new_plates_added.gif](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_new_plates_added.webp)

也可以使用快捷键 `A` 对全局进行摆盘，使用 `Shift+A` 对当前盘进行摆盘。

2. 点击任意盘旁边的**摆盘图标**，也会对盘上的所有对象进行整理和摆放。

不过，这种方法不会自动增加新的盘，如果摆盘后该盘无法装下所有的对象，会自动把一些对象移到盘外区域。

![arrange_the_plates.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_arrange_the_plates.png)

点击盘旁的锁定图标**锁定**该盘，盘上对象将不会被自动摆盘处理。

![lock_the_plate.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_lock_the_plate.png)

## 操作界面

该功能涉及 1 个参数和 3 个选项：

![arrange_all_objects.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_arrange_all_objects.png)

1. **间距**：相邻对象之间的最小间距。
2. **自动旋转以优化自动摆放效果**：允许旋转多个角度来获得更好的摆盘效果。勾选后最多会尝试 4 个角度（0°、45°、90°、135°）。

![auto_rotate_per_angle.gif](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_auto_rotate_per_angle.webp)

3. **允许同一盘中包含多种材料**：允许不同种类耗材的对象放在同一盘上。启用此选项后，原本因耗材不同而被分到不同盘上的对象会被整理到同一个盘中，多余的盘会被移除。

![arranging_all_the_3d_models_to_a_single_plate.gif](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_arranging_all_the_3d_models_to_a_single_plate.webp)

请注意，若不同的 AMS 槽位放置的是同一类型耗材，也会被视为不同的耗材。

4. **对齐到 Y 轴**：此选项会在自动摆盘时将模型沿打印板 Y 轴方向统一对齐，而不是以随机角度摆放，使整体布局更加整洁有序。

![arrange_to_y-axis.gif](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_arrange_to_y-axis.webp)

## 工作原理

自动摆盘的底层算法是 libnest2d，一个著名的 2D 装箱算法包。这个过程可以缩短为：

1. 获取所有可打印对象的排列多边形，由 a. 二维凸投影多边形，b. 高度、打印温度、热床温度等属性组成。凸投影是对象在打印板上的投影多边形的凸壳（换句话说，即对象在任意方向上的最大尺寸）。不可打印对象被视为不可装箱，将被放在所有打印板的外面。
2. 通过间距展开凸多边形（即将最小间距加到对象的整体尺寸上）。
3. 使用排序函数对对象进行排序。对于逐层打印（默认切片设置），面积是主要考虑因素，即较大的对象优先摆放；对于逐件打印，高度是主要考虑因素，即较矮的对象优先摆放。
4. 为每个多边形找到新的位置。libnest2d 包提供多个候选位置，我们从中选择代价（占用面积）最小的位置。
5. 将对象移动到新的位置。

### 当启用了擦料塔时

![prime_tower.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_prime_tower.png)

自动摆盘不会移动擦料塔，为了确保最佳擦拭效果和避免漏料，只能手动移动它。此外还有两个额外的逻辑：

1. 当打印板上有擦料塔时，对象会被紧密地排列在擦料塔周围，但不会超过擦料塔的上边界。这样做是为了减少漏料，并确保在切换耗材丝后始终打印擦料塔。
2. 当对多色对象进行全局排列（整理所有对象）时，我们会估计是否需要擦料塔。因为在摆盘之前无法得知对象的位置，所以只要有一个盘需要擦料塔，就假设所有盘都需要。以下情况需要使用擦料塔：  
   a. 有一个多色对象；  
   b. 启用了支撑，且支撑接触面采用与支撑主体不同的耗材；  
   c. 启用了 允许同一盘中包含多种材料，并且有使用相同热床温度但不同耗材的对象（例如不同颜色的 PLA）。

![allow_multiple_materials_on_the_same_plate.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_allow_multiple_materials_on_the_same_plate.png)

3. 在做单盘整理（仅对当前盘上对象摆盘）时，我们仅使用该盘上的实际擦料塔。所以其他盘上的擦料塔不会影响到该盘。

### 逐层打印的自动摆盘

![print_sequence.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_print_sequence.png)

当打印顺序设置为逐层打印时，排列多边形严格按照 **间距** 参数展开。因此，物体之间的排列更加紧密。

### 逐件打印的自动摆盘

![auto_arranging_by_object.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_auto_arranging_by_object.png)

当打印顺序设置为逐件打印时，排列多边形严格按照 max(间距, extruder\_radius) 展开。这是为了确保工具头不会与任何已经打印的对象发生碰撞。

![need_to_auto_arrange.png](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_need_to_auto_arrange.png)

![auto_arranged_3d_models.gif](https://wiki.bambulab.com/software/bambu-studio/auto-arranging/cn_auto_arranged_3d_models.webp)

（可参考：[逐件打印 | Bambu Lab Wiki](sequent-print.md)）

因此，逐件打印的物体排列距离要比逐层打印的物体排列距离远得多。

您可能会注意到工具头不是对称的。如果严格按照"从下到上，再从左到右"的打印顺序，可以把物品排列得更紧密。然而，由于我们允许自由移动物体、自由调整打印顺序，必须使用最大避让半径进行碰撞检测。为了保持一致性，自动摆盘算法也必须使用相同的避让半径。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
