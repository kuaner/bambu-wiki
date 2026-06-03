---
path: zh/software/bambu-studio/parameter/fuzzy-skin
title: "绒毛表面"
description: ""
tags: []
created: 2023-11-20T10:46:48.063Z
updated: 2024-05-28T11:02:48.868Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/fuzzy-skin
---

# 功能介绍

绒毛表面功能，顾名思义就是在模型的侧面生成一种类似动物绒毛的粗糙纹理。这个功能不仅能打印出特殊的模型外观，还可以有效地隐藏层纹、振纹和接缝，并增加模型表面的摩擦力。它的原理是在切片时给墙走线增加随机的抖动，从而使原始的直线的墙走线变成密集粗糙的折线来实现这种不规则的纹理效果。由于它只作用于墙走线，所以顶面和底面无法产生绒毛表面效果，因为底面和顶面的走线是属于实心填充，无法在打印一层填充时Z轴上下抖动

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/打印绒毛表面效果.png)

# 开启功能

绒毛表面功能可以在 **工艺——其他——绒毛表面** 开启。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/绒毛表面开启.png)

### **轮廓**

仅在模型的外轮廓位置生成绒毛表面效果。**对轮廓和孔的定义可以参考wiki：**[**XY孔洞/轮廓补偿 | Bambu Lab Wiki**](../xy-hole-contour-compensation.md)

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/仅轮廓.png)

### **轮廓和孔**

在模型的外轮廓和孔洞都产生绒毛表面的效果。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/轮廓和孔.png)

### **所有墙**

在打印模型的所有内墙和外墙都都抖动喷嘴产生绒毛表面效果。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/所有墙.png)

### **绒毛表面点间距**

绒毛表面效果是在打印走线时喷嘴随机抖动产生的。该值确定了喷嘴在每个走线中抖动的点之间的平均距离。降低绒毛表面点间距将增加墙走线上随机偏移点的数量，效果如下图：

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/绒毛表面点间距0.2.png)

**绒毛表面点间距 0.2mm**

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/绒毛表面点间距1.png)

**绒毛表面点间距 1mm**

### **绒毛表面厚度**

该参数控制用于产生绒毛表面的每次喷嘴摆动的大小和深度。这个值是以毫米为单位的距离，增加它会使模型的表面更不平整，绒毛感更明显。不过如果该值设置太大，可能会在模型表面出现悬空墙，如下图所示：

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/绒毛表面厚度0.3.png)

**绒毛表面厚度 0.3mm**

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/绒毛表面厚度1.png)

**绒毛表面厚度 1mm**

# 用修改器添加局部绒毛表面效果

您还可以使用修改器功能，来给模型的局部添加绒毛表面效果。

- **右键单击**模型，然后选择**添加修改器** - 选择合适的修改器模型。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/添加修改器.png)

- 把修改器模型拖动到模型上与之重叠，可以适当调节其位置和大小。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/调整负零件大小和位置.png)

- 在**对象列表**里，给修改器单独设置绒毛表面，它将会给修改器和模型重叠部分增加绒毛表面效果。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/对象列表启用绒毛表面.png)

- 切完片后，就会看到模型局部生成绒毛表面的效果。

![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/切片完绒毛表面效果.png)
![](https://wiki.bambulab.com/software/bambu-studio/fuzzy-skin/实际打印效果.png)

**局部绒毛表面打印效果**
