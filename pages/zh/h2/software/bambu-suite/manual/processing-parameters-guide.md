---
path: zh/h2/software/bambu-suite/manual/processing-parameters-guide
title: "Bambu Suite 加工参数介绍"
description: ""
tags: []
created: 2025-03-26T03:58:44.397Z
updated: 2025-03-26T04:22:30.616Z
source: https://wiki.bambulab.com/zh/h2/software/bambu-suite/manual/processing-parameters-guide
---

## 背景

加工参数是 Bambu Suite 软件在生成加工路径时的重要配置选项。通过使用合适的加工参数，能够显著提升加工质量，并实现预期的加工效果。不同材料在不同工艺（如激光线条雕刻、激光线条切割等）下，均需要独立配置相应的工艺参数。Bambu Suite 软件已为支持的材料预先优化了相关加工参数，确保用户能够快速上手并获得理想效果。

本文将详细介绍 Bambu Suite 软件中涉及的工艺参数及其设置对加工效果的影响，帮助用户根据需求选择合适的加工参数，从而优化加工质量或调整加工效果。为便于用户理解和使用，我们将加工参数按照常用程度分为三个等级：**简单**、**高级**和**开发者模式**。用户可通过菜单 -> 偏好设置 -> 用户设置 调整所需的参数等级。此外，本文还将按照**激光加工**、**刀切加工**和**绘画加工**三大类别，分别介绍相关加工参数的具体应用与设置方法。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/image-4.png)

## 激光加工参数

### （最大）功率 [(Max) Power]

激光输出的最大功率，以百分比形式输入。例如，10W 激光在 50% 功率设置下会输出 5W 功率。

### 速度 [Speed]

激光线条雕刻时工具头的移动速度，单位为 mm/s。激光功率和速度共同决定加工效果，不同组合的效果如下图所示。

|  |  |
| --- | --- |
|  |  |

### 加速度 [Acceleration]

工具头的加速度设置。降低加速度可减少机器震动和噪音，但会延长加工时间。

### 加工次数 [Pass]

设置路径重复加工的次数。对于较厚材料，可通过多次加工实现切割效果。

### 启用空气辅助、吹气速率 [Ais Assistant, Air Speed]

是否启用空气辅助及吹气速率（100% 为最大速率）。空气辅助可清除切割过程中的灰尘，提升切割表面清晰度和雕刻精度。

## **穿孔模式、加工长度、跳过长度 [Performation Mode, Perforation Cut, Perforation Skip]**

在需要加工虚线效果的场景时，可以使用穿孔模式。加工长度[perforation cut]是指虚线中线段的长度，跳过长度是指虚线中的间隙长度。

![group_167.png](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_167.png)

### Z 偏移 [Z Offset]

设置加工对象在 Z 方向上的偏移量，默认值为零，通常无需调整。

### 引入线长度 、引出线长度 [Lead In, Lead Out]

引入线和引出线是路径起点和终点沿切线方向的延长线。设置适当长度可改善因速度方向突变导致的加工问题。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_166.png%3E)

## 扫描参数介绍 [scanning settings]

### 双向扫描 [Dual Scanning]

控制激光在扫描时的出光方向。

- **关闭时**：激光仅在正向扫描时出光，返回起点时不工作。
- **开启时**：激光在正向和反向扫描时均出光，可显著减少加工时间。

![左：关闭双向扫描；右：开启双向扫描](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_171.png%3E)

### 十字扫描 [ Cross Scanning]

通过沿 X 和 Y 方向各扫描一次，使雕刻效果更加均匀。适用于需要高均匀度的雕刻任务，效果如下图所示。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/image.png)

### 过扫描距离 [Overscanning Distance]

在每行扫描的开始和结束时，增加一段不出光的延长线，改善因激光速度方向突变导致的雕刻不均匀问题。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/image-1.png)

### 扫描间距 [Scanning Interval]

设置相邻扫描线之间的间隔，通常与激光光斑大小相近。

- **注意事项**：

  - 间隔过小：扫描线重叠，雕刻区域变暗。
  - 间隔过大：扫描线分离，雕刻区域过亮。
  - **理想设置**：扫描线刚好相接但不重叠。

### 扫描角度 [Scanning Angle]

设置扫描线与 X 正方向的夹角（顺时针方向）。可以根据材料特性和雕刻效果需求调整角度，以获得最佳效果。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/image-2.png)

### 光斑矫正 [Dot Correction]

补偿激光光斑大小对雕刻精度的影响。在精度要求较高的雕刻任务中启用光斑矫正，可提高雕刻精度。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_41.png%3E)

### 最小功率 [ Min Power]

仅在激光图像雕刻加工时设置，因为激光加工功率超过一定功率值后，在材料上才有雕刻效果。在激光图像雕刻时，软件会将图像中接近白色的像素值映射到最小功率值参数。

### 图像模式 [Image Mode]

支持多种图像加工模式。针对不同的图片对象，不同的加工模式有各自的效果和特点。

- **灰度模式：**将图像转换为灰度图，然后将像素值映射到介于最大最小功率值中的某个功率。
- **阈值模式：**将图像进行二值化后，映射到最大最小功率进行加工。
- **Stucki、Jarvis、Bayer、Halftone、Atkinson、Floyd、Sierra：**用于在有限的灰度下模拟连续的灰度，效果更加清晰，可以保留更多的细节。

### 负片 [Negtive Image]

开启后对图像进行一次反向处理，可在需要反转图像明暗区域时使用。

### 灰度功率映射 [Grayscale Power Mapping]

利用标定图中不同功率和速度的雕刻效果，自动拟合功率映射曲线，优化灰度图像的雕刻质量。可在需要高精度灰度雕刻时启用。

## 图像Gamma [Image Gamma]

调整像素灰度值到输出功率的映射曲线。仅灰度模式下生效，用于微调图像亮度和对比度。

### 启用Clahe, Clahe Limit, 分块大小 [Clahe Enable, Clahe Limit, Clahe Size]

通过直方图均衡化增强图像对比度。

- **适用场景**：仅灰度模式下生效，适合需要高对比度的图像雕刻。

### 启用焦点下沉、焦点下沉距离 [Lower Focus Enable, Lower Focus]

激光切割时，一般焦点为材料上表面，通过将激光的焦点下移一小段距离，可以提高激光的切割能力，如需切割较厚的材料时，可以尝试启用该功能达到更好的切割效果。

### 光斑补偿 [Spot Correction]

启用光斑补偿后，在激光线条切割加工时，会将加工路径偏移半个光斑大小，以补偿光斑大小引入的切割精度误差，来提高加工尺寸精度。如下图所示：

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_176_(1).png%3E)

### 切割偏移 [Cut Offset]

设置切割路径偏移量，通常为光斑大小的一半，效果与光斑补偿类似。

### 过切 [Overcut]

为了确保激光线条切割加工可以完整的切割材料，所以在加工封闭路径一圈之后，会继续沿着路径切割一段距离，这个距离长度称做过切。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/image-3.png)

### 内部形状优先 [Inner Shape First]

优先加工内部形状，默认开启。在激光线条切割时，优先加工内部形状，可以避免已经切割的材料掉落导致内部形状再加工时出现雕刻偏差甚至雕刻失败问题。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_173.png%3E)

### 路径开始暂停时间、路径结束暂停时间、路径开始暂停时输出功率、路径结束暂停时输出功率 [Start Pause Time, End Pause Time, Start Pause Power, End Pause Power]

在激光线条切割加工时，在路径开始点，可能会出现由于激光没有切穿材料就发生了移动的情况，容易出现没有完全切割的问题，故支持在路径开始和结束位置额外停留并输出一定的功率，确保完全切割。

## 刀切加工参数

### 压力 [Pressure]

设置刀切时的下压力，单位为 gF（1gF 表示 1g 物体在标准重力下的受力）。

### 加工次数 [Pass]

刀切加工路径的次数，在刀切比较厚的材料或者比较硬的材料时，单次加工可能无法切穿，需要多次加工才能切穿。

### 内部形状优先 [Inner Shape First]

优先加工内部形状，默认开启。在刀切加工时，如果先加工了外部形状，可能导致已经被刀切下来的材料附着力下降，导致内部形状在加工时出现材料位移，导致加工瑕疵甚至失败。开启内部形状优先可以尽量避免这种情况的发生。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_173-1.png)

### 切穿刀压 [Cut Though Pressure]

设置能够完全切穿材料的压力。一般用于两层或者多层材料，将完全能够切穿材料的压力设置为切穿刀压，一般在使用贴纸材料制作贴纸时使用。

### 转刀半径 [Turning Radius]

设置刀头在转弯时的半径，通常与刀尖偏移大小一致。一般情况下无需调整，保持默认值即可。

### 转刀刀压 [Turning Pressure]

转刀刀压是在转刀时使用的刀压，一般比正常刀切路径中的刀压小。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_179.png)

### 下刀刀压 [Lead in Pressure]

下刀刀压是指刀头到达切割路径起点时施加的压力。下刀过程采用渐进加压方式：

1. **起始阶段**：刀头在空驶移动时处于无压力状态。
2. **引入阶段**：沿切割引入线（进入材料前的预备路径）逐步增加压力。抵达路径起点时，压力达到设定的下刀刀压值，同时在切引入线的同时把刀的方向调整至路径起点加工所需的方向。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_180.png)

### 垫板转刀、垫板转刀刀压、垫板转刀长度 [Plate Turning, Plate Turning Pressure, Plate Leadin]

**垫板转刀**指的是通过在垫板上调整刀头方向再进行加工，避免直接在材料上转刀留下痕迹影响加工效果，提高加工质量，但开启后刀切加工时间会更长。

- **垫板转刀刀压**：刀头在垫板上转刀时所需的压力。
- **垫板转刀长度**：刀头在垫板上转刀时走过的长度。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_174.png%3E)

### 过切 [Overcut]

为了确保刀切加工可以完整的切割材料，所以在加工封闭路径一圈之后，会继续沿着路径切割一段距离，这个距离长度称做过切。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_175.png%3E)

### 启用渐进下刀、渐进下刀长度 [Gradual Lead In Enable, Gradual Lead In]

**在路径起点前增加一段距离，逐步增大刀压并沿路径移动，**调整刀头方向。减少因刀头方向调整引入的切割瑕疵，提高加工质量。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_181.png%3E)

### 下刀长度、抬刀长度、切入距离 [Lead In, Lead Out, Cut Inout]

**下刀长度**

- **作用**：刀头在正式切割前需要“倒车一小段”来调整方向，它会在起点的反方向开始下刀并将刀的方向调整到与加工方向一致。
- **过程**：

  - 从路径起点的反方向开始下刀，逐渐调整刀具方向，使其与切割路径一致。
  - 如果当前切割路径方向与上一路径方向相同，只需使用较短的 **切入距离**；如果方向差异较大，则需要更长的 **下刀长度** 来平稳调整方向

**抬刀长度（Lead Out）**

- **作用**：刀头在切割结束后“多走一段”以避免突然停止导致的材料撕裂或毛刺。
- **过程**：切割路径结束后，刀头会沿原方向继续移动一定距离（即抬刀长度），再完全抬起离开材料。

**切入距离（Cut Inout）**

- **作用**：用于方向相近的路径衔接，减少重复调整刀头方向的次数。
- **适用场景**：当相邻切割路径方向一致或接近时，只需使用切入距离即可平稳过渡，无需大幅调整。

![](https://wiki.bambulab.com/h2/manual/processing-parameters-guide/group_177_(1).png%3E)

### X方向加工时Z补偿值、Y方向加工时Z补偿值 [Z compensation X, Z compencation Y]

调整 X 和 Y 方向的 Z 补偿值，使两方向在相同刀压下达到一致的切割效果。当 X 和 Y 方向切割效果不一致时，可通过调整补偿值优化切割质量。

### 小区域过滤尺寸 [Small Area Size]

设置一个尺寸阈值，长宽均小于该尺寸的对象将被忽略，不进行刀切加工。由于刀切加工的精度限制，过小的对象切割效果不佳，过滤后可提高加工效率。

## 绘画加工参数

### 绘画方向 [Draw Direction]

设置绘画路径的方向，当前支持以下两种模式：

- **不限制**：不固定绘画方向，系统将自动选择最近的路径进行绘画。
- **手写方向**：按照从上到下、从左到右的顺序依次绘画路径。

### 绘画结束类型 [Drawing Endtype]

支持以下两种结束方式：

- **普通结束类型**：封闭图形首尾相接后结束绘画并抬升画笔。
- **锐角结束类型**：封闭图形尾部提前抬升画笔，形成尖角，减少水彩笔类型画笔在起始点的晕染现象。
