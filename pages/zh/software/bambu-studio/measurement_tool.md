---
path: zh/software/bambu-studio/measurement_tool
title: "测量工具"
description: "介绍测量工具和使用方法"
tags: ["bambu studio"]
created: 2024-06-19T02:18:06.785Z
updated: 2024-09-23T03:04:29.864Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/measurement_tool
---

![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_1.png)

Bambu studio 1.9 版本引入了测量工具（感谢 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) 和 [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer)），可以用于测量对象之间的角度和距离。

该功能可以在同一个对象中测量不同位置之间的距离，也可以测量多个对象之间的数据。如果需要测量多个对象，需要提前通过 Ctrl+鼠标左键选中多个对象，然后再点击测量工具，就可以测量多个对象之间不同位置的角度或距离。

![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_2.webp)

## 使用方法

使用测量工具可以测量不同位置之间的角度和距离，而测量的主体分为点、线、面和圆四个部分。

### 1. 点

- 鼠标悬浮至模型的边角处即可选择点。
- 通过 shift+鼠标左键，在任意一个位置选取一个点。

选择两个不同位置的点后，测量点和点之间的直线距离和 XYZ 距离。

**点和点**

![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_3.webp)

### 2. 线

在模型的任意一条边点击鼠标左键，可以选择线，测量线和其他位置之间的直线距离、XYZ 距离和角度。

- **线和线**之间，可以测量角度和距离，如下所示：

  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_4.webp)
- **线和点**之间，可以测量平行距离和直线距离。

  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement__5.webp)

### 3. 面

在模型的任何一个面，点击鼠标左键，即可选中面。

- **面和面**之间，如果两个面平行，则可以测量面和面在Z方向上的距离；如果两个面不平行，可以测量面和面之间的角度。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_6.webp)
- **面和点**之间，可以测量Z方向上的距离。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_7.webp)
- **面和线**之间，可以测量距离和角度。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement__8.webp)

### 4. 圆

- 用鼠标选中某个**圆形面片的周长**，即可选中一个圆。选中圆后，可以测出该圆的半径（直径）。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_9.webp)
- **圆和圆**之间，可以测量两个圆心之间的直线距离。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_10.webp)
- **圆和点**之间，可以测量圆心和点之间的距离。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_11.webp)
- **圆和线**之间，可以测量圆心和线之间的距离。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_12.webp)
- **圆和面**之间，如果是圆形面，则测量圆心到圆形面之间的 Z 距离；如果非圆形面，则测量圆与该面的边缘最近的点之间的距离。  
  ![measurement_1.png](https://wiki.bambulab.com/software/bambu-studio/measurement_tool/measurement_13.webp)

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
