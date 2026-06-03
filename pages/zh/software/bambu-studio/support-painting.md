---
path: zh/software/bambu-studio/support-painting
title: "支撑绘制"
description: "本文介绍了如何使用支撑绘制功能强制生成/屏蔽支撑"
tags: []
created: 2023-07-12T12:45:48.110Z
updated: 2026-04-16T07:46:41.074Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/support-painting
---

## 支撑绘制工具

支撑绘制功能允许用户给3D模型绘制支撑相关的区域，绘制的区域分为\*\*“强制支撑”**和**“屏蔽支撑”\*\*两种，这意味着该区域会强制生成支撑或者屏蔽支撑。

当你在支撑页面选择“**普通（手动）**”或“**树状（手动）**”支撑类型时，切片生成的支撑区域将完全取决于你手绘的支撑区域。如您没有给任何区域手动绘制支撑，**手动支撑**将不会为模型生成支撑。

## 操作界面

支撑绘制工具在顶部工具栏中。选中一个模型对象将它激活，点击**支撑绘制图标**进入编辑模式，同时会出现设置面板。

![](https://wiki.bambulab.com/software/bambu-studio/support-painting/screenshot-20250213-113821.png)

在编辑模式下，只允许绘制选中的对象，其他所有对象将被隐藏。模型会被渲染成灰色，以确保在绘制后有足够的对比。手动绘制的支撑区域将会显示为**绿色**。

此外，如果选择**自动支撑**类型，例如普通(自动)，则在支撑阈值角度范围内的区域将会被用另一种颜色高亮出来。如果您选择了自动支撑类型，又手动绘制了支撑区域，那么在生成自动支撑的时候既会给符合条件的区域生成自动支撑，又会在手动绘制的区域生成手动支撑。

![](https://wiki.bambulab.com/software/bambu-studio/support-painting/%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E5%8C%BA%E5%9F%9F%E5%92%8C%E6%89%8B%E5%8A%A8%E7%BB%98%E5%88%B6%E5%8C%BA%E5%9F%9F.png)

**自动支撑和手绘支撑区域**

![](https://wiki.bambulab.com/software/bambu-studio/support-painting/%E8%87%AA%E5%8A%A8+%E6%89%8B%E7%BB%98%E6%94%AF%E6%92%91.png)

**垂直面上添加手动支撑**

Bambu Studio 1.10.0 版本支持在垂直的平面进行涂抹，生成支撑。对于在瘦高零件垂直面涂抹生成支撑，能够有效降低打印中模型倒塌的可能性。

![](https://wiki.bambulab.com/software/bambu-studio/support-painting/screenshot-20250213-114524.png)

### 支撑屏蔽功能

#### 方法一

和手动绘制方式一样，选中模型后右键涂抹不需要支撑的区域，即可禁止此处生成支撑。

![支撑屏蔽.jpg](https://wiki.bambulab.com/software/bambu-studio/support-painting/%E6%94%AF%E6%92%91%E5%B1%8F%E8%94%BD.jpg)

#### 方法二

添加模型为支撑屏蔽，那么该模型覆盖到的范围将不会生成支撑。

1. 右键单击模型，选择“添加支撑屏蔽”，并选择一个模型。不同模型功能相同，此处以立方体为例。

![](https://wiki.bambulab.com/bambu-studio/manual/support_blocker_1.png)

2. 利用移动工具，使立方体覆盖不需要生成支撑的位置。

![](https://wiki.bambulab.com/bambu-studio/manual/support_blocker_2.png)

3. 切片后，被屏蔽的位置不会生成支撑。

![](https://wiki.bambulab.com/bambu-studio/manual/support_blocker_3.png)

由于模型更易于调整、复制和移动，此方法适用于需要屏蔽平坦的底面、大块的突出部分等，实现快速屏蔽大量区域。

### 工具类型

- **圆**

该工具是一个圆形钢笔工具，用于在模型表面上绘制任何曲线。

- **球**

球类似于圆，但它将为球体接触的所有面着色，而不仅仅是可见的面。

- **填充**

填充工具会对从鼠标所指的面整块区域进行涂色绘制。当颜色传播达到阈值拐角时，传播也会停止。

- **缝隙填充**

使用上述工具绘制时经常会产生间隙区域。缝隙填充工具可以检测出细小的间隙，并用邻近面组中的强制支撑/屏蔽支撑类型自动进行填充。

### 快捷键

- **强制生成支撑**  
  鼠标左键
- **强制屏蔽支撑**  
  鼠标右键
- **擦除绘制**  
  Shift+鼠标左键
- **调节画笔尺寸**  
  Ctrl+鼠标滚轮
- **剖面视图**  
  Alt+鼠标滚轮
