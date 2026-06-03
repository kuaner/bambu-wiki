---
path: zh/software/bambu-studio/fill-patterns
title: "填充图案介绍"
description: "本文介绍了稀疏填充图案、顶面填充和底面填充图案"
tags: []
created: 2025-01-15T07:07:44.055Z
updated: 2026-05-25T02:42:48.938Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/fill-patterns
---

## 功能设置

可以在**工艺——强度——稀疏填充密度**中选择稀疏填充图案，也可在“**顶面图案/底面图案**”中选择适合模型顶面或底面的图案。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-8.png)

## 稀疏填充图案类型及特点

> **注意：仅有以下图案类型支持 100% 密度填充：** 同心、直线、直线排列、希尔伯特曲线、阿基米德螺旋、八角螺旋。

### 同心

在稀疏图案中创建由墙壁收缩得到的一系列平行环线（同心圆结构），无直线交叉，形成了立体的环形框架，使用透明材料可呈现美观的视觉效果。该填充图案在水平方向的承载能力低于垂直方向，不适合水平方向受力的模型。

![fig1.png](https://wiki.bambulab.com/software/bambu-studio/infill%20pattern/fig1.png)

### 直线

其特点为每层仅包含单一斜向线条，相邻层之间呈 90 度交替排列（如第 1、3、5 层线条方向相同，第 2、4、6 层方向垂直），形成非连续网格结构。

单层单一方向线条大幅缩短打印路径，显著提升打印速度，同时降低耗材的消耗量。同时，由于该图案填充交替排列，因此相邻层间仅通过交叉点连接，降低了层间的结合强度，适用于对模型强度要求不高的场景。

|  |  |
| --- | --- |
| fig2.png | fig3.png |

### 网格

由两组互相垂直的平行线组成十字交叉网格，是最简单且打印速度最快的填充类型。但这种填充在交叉点会导致耗材轻微堆积，**高速打印时可能出现喷嘴与模型的剐蹭异响**。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-5.png)

### 线

线填充是以直线为唯一基础填充单元（无任何曲线形态）的内部填充模式。

与直线填充不同的是，线填充的线条并非平行排列，可通过网状交织等方式排布，形成更复杂的立体支撑结构，因此比较适合对基础结构强度有要求的模型。

|  |  |
| --- | --- |
| fig5.png | fig6.png |

### 立方体

立方体填充可创建角朝下的立方体结构，形成多个气泡空间，有助于物体在水中浮起并提供隔热效果。

同时这种填充方式能提供较为均匀的强度分布，在 X、Y、Z 三个方向上均表现出稳定的机械性能，适用于需要平衡强度与打印效率的场景。

![fig7.png](https://wiki.bambulab.com/software/bambu-studio/infill%20pattern/fig7.png)

### 三角形

三角形图案的填充路径由连续的直线构成等边三角形网格，形成均匀分布的立体网状结构。

作为 3D 打印中的一种填充方式，其抗剪切能力十分出色，且各个水平方向的强度大致相当。不过，该图案的顶部线条需桥接较长距离，因此通常需要设置较多顶部表皮层，才能获得平整均匀的顶部表面。另外，打印时材料流动会在交叉点处显著受阻，这可能导致高填充率情况下整体强度相对较低。

![fig8.png](https://wiki.bambulab.com/software/bambu-studio/infill%20pattern/fig8.png)

### 内六边形

与三角形图案类似，该填充模式由三组平行线交叉形成六边形，因此每层图案中既包含小三角形也包含大六边形。这种结构使其在承受任何水平方向的拉力时，抗剪强度在各类填充图案中表现最优。此外，由于其与模型壁边的连接线较短，能够有效减少因冷却不良导致的弯曲问题。

![fig9.png](https://wiki.bambulab.com/software/bambu-studio/infill%20pattern/fig9.png)

### 螺旋体

螺旋体又称螺旋二四面体，是一种三周期极小曲面（TPMS）晶格图案。螺旋体填充在所有维度上都能提供良好支撑，且同一层内无交叉部分，打印速度相对较快；

由于打印路径更复杂，切片时间会更长并生成较大的 G 代码文件，同时在高密度且高速打印过程中可能产生较大振动。

|  |  |  |
| --- | --- | --- |
| fig10.png | fig11.png | fig12.png |

### 蜂窝

蜂窝填充是一种模仿蜂巢结构的创新填充模式，以六边形单元为核心构建高强度且轻量化的内部结构（无交叉设计），但耗材消耗比其他填充方式高出 25%。

该填充可显著提升打印件的刚性与抗冲击性能，不过由于路径复杂，也会增加切片和打印时间。

![fig13.png](https://wiki.bambulab.com/software/bambu-studio/infill%20pattern/fig13.png)

### 自适应立方体

与立方体填充相似，自适应立方体的填充密度更低，可根据区域到模型壁面的距离自动调整密度分布，在省料省时的同时，能为顶层提供稳定支撑，有效避免打印时出现顶层塌陷问题。

![download_image.png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image.png)

### 直线排列

直线排列填充由平行线构成，通过拉大直线间的间距降低填充密度，路径简单，省时省料。但如果顶面图案与填充图案的方向相同，顶部表面可能会因为支撑点不足出现塌陷的现象。

![fig14.png](https://wiki.bambulab.com/software/bambu-studio/infill%20pattern/fig14.png)

### 3D 蜂窝

和蜂窝类似，但蜂窝填充始终以六边形单元为核心，3D 蜂窝填充则是独立的立体框架结构，填充密度比蜂窝更低，因此打印时间也比蜂窝填充更短。

![download_image_(2).png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image_(2).png)

3D 蜂窝会在 Z 轴上快速改变打印方向，呈现立体填充形态，以此提升层间连接性。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/3d_%E8%9C%82%E7%AA%9D.webp)

### 希尔伯特曲线

希尔伯特曲线是一种路径复杂的曲线，包含多个直角拐点，因此切片时间和打印时间均会增加，但其特殊的曲线纹路会让模型内部受力更均匀，适合追求精细表面质量的轻量化模型。

![download_image_(3).png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image_(3).png)

### 阿基米德螺旋

阿基米德螺旋填充是一种基于阿基米德螺旋数学原理设计的填充方式，同一层内的路径中无交叉部分，且路径呈单向连续延伸状态，无需频繁切换打印方向，能有效避免耗材堆积问题。

![download_image_(4).png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image_(4).png)

### 八角螺旋

和希尔伯特曲线相似，但以独特的八边形折线螺旋路径形成大隔间结构，兼顾美观与功能扩展性。结构强度较弱，层间缺乏充足的连接结构，导致模型整聚力差，水平方向容易变形。

![download_image_(5).png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image_(5).png)

### 支撑立方体

与三角形填充类似，能随层高增加逐步增加内部三角形的数量，在 X、Y、Z 三向上均具有稳定性，能应对多方向的受力需求。

![download_image_(6).png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image_(6).png)

### 闪电填充

是一种锯齿状的极简填充图案，该图案不会在距离顶面较远的打印层生成，仅在临近顶面的层从模型墙面延伸出来，以支撑顶面，其设定的填充密度仅在顶面的下一层中生效。

闪电填充可节省大量打印时间和耗材，适合无需受力的观赏类模型。

|  |  |
| --- | --- |
| fig5.png | fig6.png |

### 交叉层叠

交叉层叠通过层间路径交叉排布实现，但部分层高区间可连续保持同一方向，以此减少打印方向的改变，缩短打印时间，适配非承重件与快速原型打印。

![download_image_(8).png](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/download_image_(8).png)

### Zig zag

Zig Zag 填充每一层由连续直线以交替方向排列成之字形，可通过调节每层 **“填充旋转步长”** 改变填充图案。这种方式能让喷嘴打印时连续挤出，减少回抽和停顿，从而加快打印速度，但结构强度较低，通常用于对承载要求不高的打印件。

![zigzag.png](https://wiki.bambulab.com/software/zigzag.png)

当旋转角度为 0 时，其效果与直线填充类似。

![0.png](https://wiki.bambulab.com/software/0.png)

### Cross zag

传统“直线”填充通常在每层生成垂直交叉的图案，而“Cross Zag”在此基础上新增了垂直交叉点走向的调节功能。

可通过调节 **“填充移动步长”** 改变交叉点的走向。

![cross.png](https://wiki.bambulab.com/software/cross.png)

同样，当“填充移动步长”设置为 0 时，其效果与直线填充类似。

![pixpin_2025-04-06_14-03-11.png](https://wiki.bambulab.com/software/pixpin_2025-04-06_14-03-11.png)

### Locked Zag

Locked Zag 是专门为“将填充作为外表面”场景设计的纹理，是一种**兼顾外观与结构强度**的填充图案。Locked Zag 的详细信息可参考：[Bambu Studio Locked Zag 填充图案使用说明](manual/locked-zag.md)

![img2.jpg](https://wiki.bambulab.com/software/bambu-studio/locked-zag/img2.jpg)

### 二维晶格

二维晶格填充是一种结构性填充图案，能够以较低的耗材用量，实现较高的机械强度。相比网格或三角形等简单填充图案，二维晶格采用了更复杂的相交线几何排布，可以更高效地分散应力。

![lattice_studio.png](https://wiki.bambulab.com/software/bambu-studio/2d-lattice/lattice_studio_zh.jpg)  
![2dlattice_animation.gif](https://wiki.bambulab.com/software/bambu-studio/2d-lattice/2dlattice_animation.gif)

二维晶格填充可通过调整参数**晶格角度 1** 和**晶格角度 2** 来调整打印件内部支撑结构的倾斜方向。

> ✅ 角度对模型强度的影响如下：
>
> - **小角度 [0° - 45°]：** 填充结构会更加竖直，**垂直方向的强度更高，适合需要承受顶部向下压力的模型。**
> - **大角度 [45° - 75°]：** 填充结构会更加扁平，**水平方向的强度更高，适合需要承受侧向拉力或推力的模型。**
> - 简而言之：小角度更"抗压"，大角度更"抗侧向力"。

|  |  |
| --- | --- |
|  |  |

## 顶面填充和底面填充

目前有 5 种基础选项——同心、直线、单调、单调线和直线排列，以及新增的 3 种——希尔伯特曲线、阿基米德螺旋和八角螺旋。

|  |  |
| --- | --- |
|  |  |

### 同心

同心填充以类似年轮的环线结构呈现，图案路径简单，因此耗时短，打印效率高。

同心的图案会自动贴合模型的邻近轮廓进行适配，如下图所示，靠近内部圆形轮廓的填充路径为圆形，靠近外部方形轮廓的填充路径为方形，在两者的交界区域，填充路径以三角形进行过渡衔接，确保填充层无间隙。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-10.png)

### 直线/单调/单调线/直线排列

- **直线：**与相邻层呈垂直方向，因此直线作为顶面图案时，无法看出效果（具体请参考后文）；
- **单调：**单调填充采用均匀线条，因此表面比直线填充更光滑，适合大尺寸平整顶面，并对表面顺滑度有要求的模型。
- **单调线：**相较于直线、单调和直线排列填充，单调线填充与外轮廓无边缘过渡走线。虽然表面可能出现一些接缝，但连接区域不会有多余材料。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-11.png)

- **直线排列：**直线排列的打印方向和直线一致，但不同于直线的是，直线排列与相邻层呈平行而非垂直关系。使用透明材料时，若顶面/底面填充设置为直线排列填充，建议将稀疏填充图案也设置为直线排列填充，以获得更优的视觉效果，但打印出来的实心填充会带有各向异性的力学特性，即沿着纤维方向的抗拉强度高，但是垂直纤维方向则较为脆弱。

|  |  |
| --- | --- |
| 直线 | 单调 |
| 单调线 | 直线排列 |

在打印方向上，单调与单调线填充均为单向打印，每条填充线的起点均排布于相邻线条的同侧（左侧或右侧），形成类似鳞片的单向层叠结构。即便打印过程中出现轻微走线变形，整体纹理仍能保持均匀一致。另一方面，双向打印的优势在于路径衔接更紧凑，可有效缩短空驶距离。在与相邻图层的方向关系上，直线排列填充与内部实心填充的路径呈平行状态，而直线、单调和单调线这三种填充模式，相邻层的打印方向均为垂直交叉关系。

|  |  |
| --- | --- |
| 单调顶面与相邻层的垂直关系 fig2.png | 直线排列顶面与相邻层的平行关系 fig3.png |

简而言之，仅单调线填充无边缘过渡走线；单调与单调线均为层内单向打印，直线与直线排列支持双向打印。层间方向上，仅直线排列顶层与相邻层保持平行，其余三种的相邻层均呈垂直关系。

|  | **是否有边缘过渡走线** | **打印方向** | **层间方向关系** |
| --- | --- | --- | --- |
| **直线** | 是 | 双向皆可 | 垂直 |
| **单调** | 是 | 仅单向 | 垂直 |
| **单调线** | 否 | 仅单向 | 垂直 |
| **直线排列** | 是 | 双向皆可 | 平行 |

### 希尔伯特曲线

希尔伯特曲线常用于顶面填充，交叉连续的路径可让层间衔接紧密，减少顶面塌陷、孔洞等缺陷。用于底面填充时，打印过程会受到打印板的影响，比如，在纹理板上打印希尔伯特曲线时，光滑的板面会弱化曲线纹理。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-12.png)

### 阿基米德螺旋

阿基米德螺旋适配对外观和模型表面均匀性要求较高的模型，相比于希尔伯特曲线，其路径更简单，打印速度更快。作为底面填充时，其打印质量也会受到打印板的影响，且曲线路径难控制，易出现漏料问题。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-13.png)

### 八角螺旋

作为顶面填充，八角螺旋同样能突出视觉效果，观赏性较强；但作为底面填充时，整体强度有限，易受力变形，且对打印精度和参数设置要求高，易出现线条不均的现象。

![](https://wiki.bambulab.com/software/bambu-studio/fill-patterns/image-14.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
