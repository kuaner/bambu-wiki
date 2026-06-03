---
path: zh/software/bambu-studio/view-slicing-information
title: "查看切片信息"
description: ""
tags: []
created: 2024-06-06T02:52:41.087Z
updated: 2024-06-19T09:36:55.923Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/view-slicing-information
---

在 Bambu Stuido 切片后，可以查看不同层的详细信息，例如走线类型、耗材丝、打印速度，打印路径等。同时，可以为层添加自定义操作，包括自定义G-code、暂停打印和更换耗材丝。

## 基础介绍

### 走线类型

不同部分的走线类型以不同的颜色显示，并显示每种走线类型需要的打印时间、打印时间占比、消耗耗材的长度和重量。更多介绍请参考[线宽设置](parameter/line-width.md)。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/line-type.png)

### 耗材丝

显示耗材颜色、用于模型打印消耗长度和重量、用于[冲刷](reduce-wasting-during-filament-change.md)的消耗长度和重量、用于[擦料塔](parameter/prime-tower.md)的耗材消耗长度和重量。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/filament.png)

### 速度

不同打印速度以不同的颜色显示。数值越大，打印速度越快。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/speed.png)

### 层高

在打印过程中是模型是层层堆叠成型的，通常也把层高视作模型的垂直分辨率，即层高越低，模型的精细度也就越高。不同层高以不同的颜色显示。颜色越亮，层越高。可以通过[可变层高](adaptive-layer-height.md)功能，自定义不同层的高度。更多介绍请参考[层高设置](layer-height.md)。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/layer-height.png)

### 线宽

线宽指的是打印过程中，喷嘴挤出单根耗材丝的宽度。通常情况下，挤出材料的宽度和喷嘴直径几乎一致。不同的线宽会影响打印质量、速度、强度和细节，例如，增大线宽可以增加层间的接触面积，改善层间附着力，但是可能会降低模型的细节。更多介绍请参考[线宽设置](parameter/line-width.md)。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/line-width.png)

### 流量

显示不同位置的耗材流量速度（体积速度）。打印机对于各种耗材丝都有最大体积速度的限制，也就是对单位时间内最大挤出流量的限制。**最大体积速度=挤出线的横截面积 \* 最大打印速度。**

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/flow.png)

### 层时间

显示不同层的打印时间。一般情况下，层的面积越大，所需打印时间越长。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/layer-time.png)

### 风扇速度

显示不同层的部件冷却风扇速度。风扇速度越快，耗材冷却得越快。更多关于冷却相关的介绍，请参考[冷却设置](auto-cooling.md)。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/fan-speed.png)

### 温度

显示不同层的喷嘴温度。使用同一种材料打印时，喷嘴温度在整个过程表现一致。使用多材料（配套 AMS）打印，使用不同耗材时，喷嘴温度可能会不一样。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/temperature.png)

### 使用方法

拖动界面右侧和底部的进度条，可以查看不同层的信息和打印路径。使用键盘的方向键，可以一次移动一层。

右侧进度条显示模型的层数、层高和打印时间，底部进度条显示打印头在所选层的移动路径。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/use-1.gif)

选择某一层时，单击右下角的图标，可以只查看此层，此时再拖动进度条，可以只查看单一层。再次单击该图标，恢复显示所有层。右键“+”并选择“跳转到层”，可以自定义选择查看哪一层。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/use-2.gif)

如果此时修改任何参数，需要重新对模型切片。如果想要回到打印准备界面，单击左上角的**准备**标签即可。

右键“+”后可以看到以下功能：

- 添加暂停打印：添加暂停后，打印机在**打印该层前会停止打印**，需要手动恢复打印。例如，在第1层添加暂停，打印机在打印第1层之前，会停止打印。（小技巧：在第1层添加暂停，打印机在打印第1层之前会停止打印，您可以铲掉打印板上打印的流量标定线，然后手动恢复打印，此时流量标定线就不会占用打印板的面积。可以通过此操作，打印首层较大的模型。）

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/use-3.webp)

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/use-4.png)

- 添加自定义G-code：可以在所选层添加自定义G code，实现各种个性化功能。例如M104 S250，指的是在打印这一层前，把喷嘴温度升到 250 摄氏度。通过在不同层，插入 Gcode 指定不同层的打印温度，可以实现温度塔功能。  
  ![动画.apng](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/%E5%8A%A8%E7%94%BB.apng)
- 更换耗材丝：添加耗材更换位置，可指定在任意层切换耗材。请注意，此功能必须配合 [AMS](../../ams.md) 使用。

![](https://wiki.bambulab.com/software/bambu-studio/view-slicing-information/use-5.gif)

## 使用场景

合理利用此功能，可以更好地调整打印参数，提高模型的打印质量。

- **检查打印路径**：通过逐层查看打印路径，可以详细检查 Bambu Studio 生成的G-code，确保打印路径符合预期。这样可以发现并修正潜在的问题。
- **满足自定义需求**：在打印过程中暂停，允许你在模型中嵌入物件，如磁铁等材料。打印完成后，这些嵌件可以牢固地嵌入模型内。
- **优化支撑结构**：查看不同层的支撑结构，可以帮助你优化支撑的生成方式和位置。确认支撑结构是否覆盖了需要支撑的区域，同时避免不必要的支撑；确保支撑接触点合理，减少支撑对模型表面质量的影响。更多关于支撑的介绍，请参考此wiki文章：[支撑耗材与支撑功能的介绍](support.md)。
- **调整填充模式**：逐层查看填充模式（如网格、三角形、蜂窝等）可以帮助评估和优化填充设置。检查填充密度是否合适，既保证模型强度，又避免浪费耗材；确保填充方向合理，有助于增强模型的结构强度。
- **评估层高设置**：评估当前层高设置对模型细节和表面质量的影响。确保层高设置的一致性，避免层间高度不一致导致的打印质量问题，例如表面层纹；检查较小的层高是否能够更好地处理模型的细节部分。
- **加快打印时间**：识别打印时间较长的区域，进行必要的优化，缩短打印时间。
- **发现潜在问题**：通过逐层查看，可以提前发现并解决一些潜在的打印问题。悬空部分：识别悬空部分，确保有足够的支撑或调整打印参数以减少悬空；过渡区域：检查过渡区域的打印路径，确保平滑过渡，避免层间结合不良。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
