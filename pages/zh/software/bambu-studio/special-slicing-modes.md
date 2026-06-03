---
path: zh/software/bambu-studio/special-slicing-modes
title: "Bambu Studio 特殊切片模式"
description: "本文介绍了 Bambu Studio 特殊模式中的切片模式"
tags: []
created: 2025-06-05T03:09:49.424Z
updated: 2025-08-05T05:53:53.078Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/special-slicing-modes
---

## 特殊模式——切片模式

Bambu Studio 中的特殊切片模式决定了切片器在生成 G 代码之前如何解析和处理 3D 模型的几何形状。它会影响表面、孔洞和壳体的处理方式，尤其是在具有特殊结构、开放边缘或重叠几何形状的模型中。

可在**其他 > 特殊模式 > 切片模式**中进行设置。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/screenshot-20250606-143804.png)

选项包括**常规、奇偶和闭孔**，请根据模型特性选择适合的切片模式进行切片。

## 常规

切片模式的默认选项，适用于具有干净流形几何的标准 3D 模型。该模式基于标准网格规则处理模型，要求模型必须完全密封（流形闭合），不能有破损或缺口且符合设计规范。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/常规模式.png)

- **适用的模型：**常规模型；
- **不适用的模型：**具有特殊结构的模型，比如遥控飞机翅膀内部的支架（这些支架很薄或者有交叉重叠的情况），用常规模式切片可能会出错，此时需切换至**“奇偶”**模式。

## 奇偶

奇偶切片模式是专为航模、无人机等特殊结构设计的智能方案，它能精准处理那些为了减重而设计的交叉薄壁结构。这种切片模式下打印的模型只有单层外壳，没有内部填充，既轻巧又不失强度，特别适合追求极致轻量化的高性能应用场景。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/奇偶-.png)

当模型存在结构重叠或破损时，普通切片模式往往会将其误判为损坏文件；特别是遇到细薄结构时，要么挤料过多导致变形，要么挤料不足造成强度不够。而奇偶切片模式能精准识别哪些该填实，哪些该留空，自动生成恰到好处的打印路径，完美还原复杂设计。

最能展示奇偶切片功能的模型代表就是 [3DLabPrint](https://3dlabprint.com/) 这类网站提供的模型文件。它们专为薄壁打印优化设计，采用了一种特殊的建模技巧，让多层外壳相互交叠、边缘共享。而对于这种精妙的空心结构，常规模式无法判断哪里该填充（相当于"外面"），哪里该留空（相当于"里面"）。请参考下图，对比了解常规模式与奇偶模式的区别：

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/常规对比.png)

常规模式

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/奇偶.png)

奇偶模式

## 闭孔

闭孔模式可密封 3D 模型中的开放区域。它不仅可以封闭圆形孔洞，还可以填充任何类型的间隙或开放轮廓。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/screenshot-20250606-142624.png)

应用“闭孔”后，顶部所有孔洞都会被封闭。

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/闭孔切片.png)

有些模型**侧面**存在洞孔，导致**单层内的走线未闭合，则就不会被识别为孔**。如下图：

![](https://wiki.bambulab.com/software/bambu-studio/slicing-mode/侧面洞孔.png)
> 使用此功能时需注意：自动修复可能导致模型某些结构被封闭，进而影响其设计功能特性。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！
>
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
