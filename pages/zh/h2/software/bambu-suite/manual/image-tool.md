---
path: zh/h2/software/bambu-suite/manual/image-tool
title: "Bambu Suite图片工具使用指南"
description: "本指南介绍了Bambu Suite软件中图片工具的各种基本功能并进行了操作演示。"
tags: ["h2d", "software"]
created: 2025-05-27T02:09:37.750Z
updated: 2025-07-25T08:55:04.999Z
source: https://wiki.bambulab.com/zh/h2/software/bambu-suite/manual/image-tool
---

## 1. 工具概览

Bambu Suite图片工具集成了全面的图像处理功能，其中包括多种图像滤镜应用、精细化图像调整、专业编辑工具、图形矢量化功能、一键重置选项和图片替换等，无需借助第三方软件，即可满足大多数用户的日常图片处理需求。

## 2. 图片滤镜功能

### 2.1 滤镜类型

Bambu Suite提供了四种风格化滤镜，用户可以通过点击对应的按钮对图片设置不同的滤镜。

- **原图** - 保持图片原始状态
- **二值化** - 黑白分明的艺术效果
- **草图** - 转换手绘风格
- **浮雕** - 3D浮雕效果

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool///20250520160043_rec_.gif)

### 2.2 参数调节

其中一些滤镜有特有的滤镜参数，可以通过更改滤镜参数来实现想要的效果。

##### 二值化阈值

- 阈值范围：0-255（默认值127）；
- 参数说明：低于阈值的像素点会被设置为黑色，高于阈值的像素点会被设置为白色；
- 极端值效果：阈值=0，图片全白；阈值=255，图片全黑；

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520160703_rec_.gif)

##### 浮雕阈值

- 阈值范围：1~20（默认值5）；
- 参数说明：浮雕阈值越大，浮雕效果越强。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520160939_rec_.gif)

## 3. 图片调整

可以对图片的锐度、亮度、对比度进行调整，还可以设置图片反色显示，**所有调整操作将在滤镜应用后生效。**

### 3.1 锐度

- 功能：控制图像中边缘和细节的清晰程度；
- 可调节范围：-100~100（默认值0）；
- 参数说明：锐度越大，图像越清晰，轮廓和细节越明显，看起来"更锋利"；锐度越小，图像越模糊，细节变得不清楚，边缘显得"柔和"。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520162352_rec_.gif)

### 3.2 亮度

- 功能：调整图像整体的明亮程度；
- 可调节范围：-100~100（默认值0）；
- 参数说明：亮度越大，图像越明亮，画面看起来更"发光"或"清晰"；亮度越小，图像越暗，可能显得阴沉或不易辨认。亮度设置为-100时，图片会是全黑；亮度设置为100时，图片会是全白。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520162531_rec_.gif)

### 3.3 对比度

- 功能：调节图像中明暗区域之间的差异程度；
- 可调节范围：-100~100（默认值0）；
- 参数说明：对比度越大，明暗反差越强烈，图像更立体、有冲击力；对比度越小，明暗差异较小，图像趋于灰平、显得"雾蒙蒙"。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520162657_rec_.gif)

### 3.4 反色

设置完滤镜以及对锐度、亮度、对比度进行调整后，还可以设置图片反色显示。

- **效果：** 反转RGB三个颜色通道

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520163122_rec_.gif)
  

- **特性：** 保留原始透明度不变，图片中透明的区域还会保持透明。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520163321_rec_.gif)

## 4. 图片编辑

点击图片属性面板下方的"编辑"按钮，可以进入图片编辑器。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520163914_rec_.gif)

### 4.1 画布控制

#### 4.1.1 移动画布

- 操作方法：按住鼠标滚轮拖动

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520163947_rec_.gif)

#### 4.1.2 缩放画布

- 方式一：鼠标在画布上时滚动滚轮，会以鼠标位置为中心缩放画布，达到查看图片局部细节的目的；

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520164150_rec_.gif)

- 方式二：画布下方的比例调节按钮增减或者手动输入比例；

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520164317_rec_.gif)

#### 4.1.3 重置画布

如果图片被移动或者缩放到不容易查看的位置，可以双击鼠标滚轮重置图片到一个合适的视角。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520164535_rec_.gif)

#### 4.1.4 撤销与重做

- 按钮控制：左上角撤销/重做按钮可以撤销或者恢复对图片的修改；
- 快捷键：Ctrl+Z（撤销），Ctrl+Y（重做）。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520164725_rec_.gif)

### 4.2 智能擦除

- 工作原理：自动识别并清除与鼠标点击位置颜色相近的像素点；
- 容差：决定擦除范围大小，容差越大，被擦除的像素点越多；
- 删除所有相同颜色：默认仅清除连续的像素点，如果勾选了该选项，满足条件的不相连的像素也会被擦除。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520165401_rec_.gif)
![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520165634_rec_.gif)

### 4.3 手动擦除

- 工具形态：鼠标会自动变成圆形笔刷；
- 尺寸调节：自定义圆形区域的大小；
- 使用方法：按住左键涂抹目标区域，图片中圆形区域经过的区域将会被擦除。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520170017_rec_.gif)

### 4.4 还原

- 作用：擦除的反向操作，恢复被擦除区域；
- 尺寸条件：与手动擦除中的尺寸设置相同。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520170350_rec_.gif)

### 4.5 裁剪

裁剪可以让用户在原有图形上裁剪出一个矩形区域。

**操作流程：**

1. 选择裁剪区域（支持选择裁剪比例设置裁剪矩形的长宽比）

   ![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520170627_rec_.gif)
2. 调整选框，无固定比例时用户可以通过控制点移动或者缩放选择框。

   ![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520170909_rec_.gif)
3. **如果设置了裁剪比例，选择框边缘没有控制点。**

   ![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520171107_rec_.gif)
4. 确认操作：

   - 按钮：√确认 / ×取消裁剪；
   - 快捷键：Enter确认 / Esc取消裁剪。

## 5. 图形矢量化

该功能可以将位图转换成矢量图形，以便后续进行分块切割等操作。

点击图片属性面板下方的**图形矢量化**按钮，可进入图形矢量化界面。

### 5.1 画布操作

可以参考图片编辑的画布操作。

### 5.2 模式

图形矢量化工具提供了单色/多色两种模式，可以通过画布上方的单选按钮进行切换。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//image12.png)

#### 5.2.1 单色模式

- 最佳适用场景：单色Logo、黑白图标等
- 输出效果：生成单一颜色的矢量轮廓

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//单色模式.gif)

#### 5.2.2 多色分层模式

该模式适用场景为将包含多个色块的复杂图形，中的色块抠出来，以便设置不同加工参数。

**使用技巧：**

1. 执行前需将加工模式设为"打印后刀切"以保留原始颜色
2. 输出后将自动分层显示不同色块
3. 多色分层模式会尽可能捕获区域，通常需要删除不需要的色块。故建议用于符合以下特征的图片：

   - 边界清晰无渐变
   - 背景干净无杂色
   - 图形结构简单

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//多色分层.gif)

### 5.3 参数说明

#### 5.3.1 去除小颗粒

过滤掉小于一定尺寸的色块。

#### 5.3.2 亮度阈值

- 功能：单色模式下，亮度阈值可以决定捕获的范围；
- 技巧：通过实时预览调整，以捕获干净完整的色块。

#### 5.3.3 颜色容差

在多色分层模式下，调整颜色容差，可以调整颜色合并的范围。提升颜色容差可以区分色彩差距更小的色块，但也会导致产生更多的细小区域。

#### 5.3.4 平滑度

双重作用：

- 位图通常会在色块的边缘产生颜色不稳定的区域，更大的平滑度可以更好地过滤这部分边缘锯齿；
- 可能弱化尖锐转角；

建议：请在清晰度与自然度间调整最佳值。

## 6. 重置

- 功能位置：图片属性面板底部；
- 功能效果：可以重置所有滤镜为默认滤镜，恢复所有调整参数为默认值。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520172224_rec_.gif)

## 7. 图片替换

- 功能位置：属性面板"图片替换"按钮；
- 功能特性：会弹出文件选择对话框让用户选择将会替换为的图片，图片替换前后图片滤镜、图片调整部分保持不变。

![](https://wiki.bambulab.com/h2/software/bambu-suite/manual/image-tool//20250520173058_rec_.gif)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
