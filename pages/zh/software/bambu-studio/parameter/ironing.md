---
path: zh/software/bambu-studio/parameter/ironing
title: "熨烫功能"
description: ""
tags: []
created: 2023-11-06T03:58:33.914Z
updated: 2024-11-01T08:41:14.731Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/ironing
---

## 什么是熨烫

众所周知，受限于FDM 3D打印的成型原理，我们在仔细观察打印的模型顶面可以看到它是由密集的线条组成的，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/ironing/顶面条纹.png)

而熨烫功能，顾名思义，就像熨平衣服上的褶皱一样，可以消除模型顶面的线条，让顶面看起来更平滑。它的工作原理是，在打印完模型的顶面后，在同一Z高度上喷嘴继续使用小流量在模型表面打印，让少量的挤出材料渗透进线条之间并填平缝隙。在熨烫过程中，由于Z高度没有抬升（喷嘴仍保持在打印顶层时的高度），喷嘴抹过顶层的热量会使顶层的线条变软，挤出的少量材料也能够轻松填充和抹平顶层。熨烫过程如下图所示：

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫动图.gif)

熨烫前后的效果对比如下图所示。不论是观感上还是触感上，熨烫过的表面都会更加光滑。

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫对比.png)

**左：熨烫前；右：熨烫后**

由于我们的3D 打印机都是喷嘴朝下进行打印的，所以熨烫功能也只能对模型的顶面进行操作，无法熨烫模型的侧面。

## 注意事项

熨烫可以使得顶面层更加光滑，但也有以下注意点需要提前考虑：

1. 熨烫层需要额外的打印时间来完成，而且熨烫的速度通常较慢，如果您打印零件的顶面面积较大，可能会增加不少打印时间。

2. 由于熨烫过程仅用少量的挤出流量和较慢的打印速度，所以有一定概率发生热蠕变，从而导致热端堵塞，尤其是对PLA、PETG和TPU等软化温度较低的材料。

3. 熨烫是依靠喷嘴抹过顶层实现的，所以熨烫过程模型受到喷嘴的作用力相比正常打印时更大，如果模型在构建板上粘接不够牢固，很可能从构建板上脱落导致打印失败。

4. 选择合适的熨烫设置才能获得一个平滑的表面，否则可能效果会更差，例如过度挤出表面堆料，表面平滑度不一致等。

5. 熨烫仅限于在顶面是平面的时候能有较好的效果。在带有弧度弯曲的顶面上，熨烫将无法抹平图层之间线条，所以未必能得到比不熨烫更好的效果，反而徒增打印时间。

## 参数设置

### 熨烫类型

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫类型1.png)

您可以在“熨烫类型”里选中开启该功能，Bambu Studio的默认是不开启熨烫的，选中其他几项即可开启熨烫功能。具体解释如下：

**所有顶面：**即模型的所有顶面都会被熨烫。

**最顶面：**仅熨烫模型的最后一层，即最高的那一层“顶面”。

**熨烫所有顶面和最顶面的区别如下：**

![](https://wiki.bambulab.com/software/bambu-studio/ironing/顶面和最顶面的区别.png)

**左：熨烫所有顶面；右：熨烫最顶面**

**所有实心层：**所有的实心层（包括顶面、底面和内部实心填充）都会被熨烫，该选项很少会用到，因为未必会带来良好的打印效果，且会花费大量的打印时间。

### 熨烫模式

熨烫模式中有两种熨烫图案可选：直线和同心。

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫模式1.png)

**直线熨烫图案：**

![](https://wiki.bambulab.com/software/bambu-studio/ironing/直线熨烫模式.png)

**同心熨烫图案：**

![](https://wiki.bambulab.com/software/bambu-studio/ironing/同心熨烫模式.png)

### 熨烫速度

熨烫速度即为熨烫过程喷嘴的移动速度，通常较慢的速度能获得较好的熨烫效果。

### 熨烫流量

在熨烫过程中挤出的材料量。该数值表示相对于打印正常层高的流量的百分比。过高的值会导致挤出过度，太小的值也会导致熨烫表面不够平整。

熨烫流量太少：

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫流量太少.png)

熨烫流量太多：

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫流量太多.png)

### 熨烫间距

熨烫走线的间距， 该值越大喷嘴熨烫路径的间隔就越大。通常建议小于喷嘴直径，这样可以反复熨烫同一个区域多次。

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫间距0.15.png)

**熨烫间距0.15mm**

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫间距0.5.png)

**熨烫间距0.5mm**

### 熨烫内缩

Bambu Studio 1.10版本引入了熨烫内缩功能。在熨烫的时候，有时候边缘区域会出现材料堆积的现象。通过调整“熨烫内缩”可以适当调整熨烫区域，避免材料堆积。该参数值单位为mm，表示熨烫区域距离轮廓边界的距离，0表示禁用。

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫内缩.gif)
![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫内缩对比示意图.png)

**启用熨烫内缩后的效果对比**

## 熨烫方向

如果要调整该参数，请先启用 "偏好设置 "中的 "开发者模式 "。  
熨烫走线的方向，**该值表示熨烫走线与顶面图案走线的相对角度**，通常45°的角度能获得更好的熨烫效果，如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫方向45°.png)

**熨烫方向45°**

![](https://wiki.bambulab.com/software/bambu-studio/ironing/熨烫方向90°.png)

**熨烫方向90°**
