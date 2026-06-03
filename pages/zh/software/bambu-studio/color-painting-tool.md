---
path: zh/software/bambu-studio/color-painting-tool
title: "涂色工具使用指南"
description: ""
tags: []
created: 2023-07-23T15:17:10.549Z
updated: 2026-03-24T03:41:44.513Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/color-painting-tool
---

涂色功能是一种可以让用户在3D场景中绘制模型的功能。绘制的模型将被切片成由多种耗材丝打印的Gcode路径，最终打印成一个彩色模型。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/color_painting_example.png)

这个模型由来自[thingiverse](https://www.thingiverse.com/thing:3962846/files)的Patrick提供。

## 操作界面介绍

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E6%93%8D%E4%BD%9C%E7%95%8C%E9%9D%A2.png)

### 耗材丝

它以颜色框的形式列出当前项目中所有可用的耗材丝。您可以通过简单地单击颜色框或使用键盘快捷键1~9来选择绘画的颜色（耗材丝）。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E6%B6%82%E8%89%B2%E9%A1%B5%E9%9D%A2%E9%80%89%E6%8B%A9%E8%80%97%E6%9D%90%E4%B8%9D.png)

### 工具类型

Bambu studio共提供6种绘画工具。

#### **圆**

圆形工具是一种圆形钢笔工具，用于在模型表面绘制任何曲线。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E5%9C%86%E5%BD%A2%E5%B7%A5%E5%85%B7.gif)

- 选择**垂直**或**水平**方向，可让涂色工具保持垂直或水平状态。
- 选择**视图：保持水平**，可让模型回到水平状态。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E5%9C%86.webp)

设置剖面视图，可对被挡住的平面进行涂色。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E5%89%96%E9%9D%A2zh.webp)

#### **球**

球型绘画工具类似于圆，但它将为球体内的所有面着色，而不仅仅是可见的面。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E7%90%83%E5%B7%A5%E5%85%B7.gif)

#### **三角形**

三角形工具可为鼠标指针所指的三角形面着色。单击可为单个三角形面着色，拖动可连续选择一连串三角形面来上色。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E4%B8%89%E8%A7%92%E5%BD%A2%E5%B7%A5%E5%85%B7.gif)

#### **高度范围**

高度范围工具将给定高度范围内的所有面着色，即使它们可能位于不相交的区域。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E9%AB%98%E5%BA%A6%E8%8C%83%E5%9B%B4%E5%B7%A5%E5%85%B7.gif)

高度范围工具支持鼠标跟随设置。您可以在选择涂色的高度范围后，点击鼠标位置进行涂色，也可以通过修改输入框中的数值来调整工具距离底边的高度。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E9%AB%98%E5%BA%A6%E8%8C%83%E5%9B%B42.webp)

启用**起点输入框置于鼠标附近**的功能前，需将视图调平，即可快速捕捉输入框，调整底边高度。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E9%BC%A0%E6%A0%87en-.webp)

#### **填充**

填充工具会对从鼠标指针所指的面开始传播的相连面进行着色。当到达具有不同颜色的面时，传播会停止。如果开启了 "边缘检测"功能，则在到达比阈值更锐利的角时也会停止传播。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E5%A1%AB%E5%85%85%E5%B7%A5%E5%85%B7.gif)

#### **缝隙填充工具**

使用上述工具进行绘画通常会产生间隙区域。它们可能看起来很丑，并且增加耗材丝更换的次数。空白填充工具将检测小的空白，并采用相邻面的颜色来自动填充它们。

![](https://wiki.bambulab.com/software/bambu-studio/color-paiting-guide/%E7%BC%9D%E9%9A%99%E5%A1%AB%E5%85%85%E5%B7%A5%E5%85%B7.gif)

### 快捷键

- **选择耗材丝**  
  数字快捷键 1~9
- **擦除绘制**  
  选择一个绘制工具（缝隙填充除外），Shift +鼠标左键拖动即可擦除
- **改变圆/球半径**  
  Ctrl+鼠标滚轮
- **剖面试图**  
  Alt+鼠标滚轮
