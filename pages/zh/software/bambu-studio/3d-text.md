---
path: zh/software/bambu-studio/3d-text
title: "文本形状"
description: "文本形状工具用于在平面或曲面上创建可定制的 3D 文本"
tags: []
created: 2023-08-08T09:51:08.195Z
updated: 2026-04-21T07:46:06.878Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/3d-text
---

## 简介

**“文本形状”**是一种用于为对象创建 3D 文本部件的工具，可在任意类型的表面上添加 3D 文本，包括平面和曲面。

与其他模型零件一样，3D 文本也可以修改颜色：你既可以通过更换其“耗材丝”来实现，也可以使用涂色工具对其进行上色。

![bambustudio_text_display.png](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_display.png)

## 用户操作界面

选中需要增加文本的模型后，点击工具栏中**“文本形状”**工具即可打开用户操作界面。

![firststep.png](https://wiki.bambulab.com/software/bambu-studio/3d-text/firststep.png)

  

### 输入文本

在此处可以输入所需生成的 3D 文本的内容。

![bambustudio_text_text.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_text.jpg)

### 字体

点击下拉菜单可选择用于生成文本的字体，Bambu Studio 提供丰富的内置字体库供用户选择。此外，我们新增了备用字体功能：若当前字体不支持特定字符时，系统将自动使用备用字体进行显示。

![bambustudio_text_font.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_font.jpg)

### 大小

可以在输入框中直接输入数值，或点击**‘-’**、**‘+’**按钮来调整字体大小，以毫米为单位。

![bambustudio_text_size.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_size.jpg)

### B 粗体

点击将字体加粗。

![bambustudio_text_bold.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_bold.jpg)

### T 斜体

点击将字体倾斜。

![bambustudio_text_italic.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_italic.jpg)

### 高级

#### 粗细

拖动区间滑块，可自定义字体的粗细程度。

![bambustudio_text_boldness.webp](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_boldness.webp)

### 偏斜

拖动区间滑块，可自定义字体的偏斜程度。

![bambustudio_text_skew.webp](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_skew.webp)

### 厚度

可以在输入框中直接输入数值，改变字体厚度，以毫米为单位。

![bambustudio_text_thickness.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_thickness.jpg)

### 内嵌深度

可以在输入框中直接输入数值，改变字体嵌入物体的深度，以毫米为单位。

![bambustudio_text_embedded_depth.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_embedded_depth.jpg)

### 文字间距

拖动区间滑块，可自定义字体的文字的间距，以毫米为单位。  
![bambustudio_text_text_gap.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_text_gap.jpg)

### 角度

拖动区间滑块，可自定义字体的文字的角度。  
![bambustudio_text_angle.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_angle.jpg)

### 模式

点击下拉菜单可选择**文本生成模式**，包含以下四个选项：

- **未环绕**：在选定位置生成平面文本，不随模型表面弯曲。
- **环绕表面**：文本将贴合着模型对象的表面。
- **环绕+水平**：文本紧贴模型表面，同时保持水平方向排列。
- **按字符环绕投影**：文本紧贴模型表面，仅显示投射在模型表面上的文本部分（即与模型表面相交的部分）。

![bambustudio_text_mode.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_mode.jpg)

![bambustudio_text_surround_character.webp](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_surround_character.webp)

### 操作

在此处可选择生成的 3D 文本的三种类型。

**零件**：生成的 3D 文本会是一个实体，切片时将被视为常规模型实体。

![bambustudio_text_part.webp](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_part.webp)

**负零件**：生成的 3D 文本会变成负零件，用于在模型表面进行布尔运算，形成凹陷的雕刻效果。

![bambustudio_text_cut.webp](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/bambustudio_text_cut.webp)

**修改器**：生成的文本仅作为参数修改区域。它不改变模型几何形状，而是修改其与模型重叠部分的打印参数（如颜色）。利用此特性，可制作与模型表面完全平齐的 2D 文本图案。

![modify1.webp](https://wiki.bambulab.com/bambu-studio/toolbar/text-shape/modify1.webp)
