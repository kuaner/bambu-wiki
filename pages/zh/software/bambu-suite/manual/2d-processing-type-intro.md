---
path: zh/software/bambu-suite/manual/2d-processing-type-intro
title: "2D 工艺类型介绍"
description: ""
tags: []
created: 2025-03-25T13:07:36.191Z
updated: 2026-02-09T07:33:45.053Z
source: https://wiki.bambulab.com/zh/software/bambu-suite/manual/2d-processing-type-intro
---

不同的加工工艺适用于不同的材料和图案，每一种工艺的加工效果也会不同，您可以根据作品所需的实际加工效果选择合适的制作工艺。本文将简单介绍每种加工工艺的工作原理和实际效果。

## **激光线条雕刻**

激光线条雕刻是使用较小的激光功率和较快的加工速度，在材料表面烧蚀出线条，**适用于由线条构成的矢量图形。**因此当图案的加工工艺被设置为激光线条雕刻时，在软件画布上也会只渲染线条，不渲染图案内部的填充部分。加工路径示意图如下：

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/%E7%BA%BF%E6%9D%A1%E9%9B%95%E5%88%BB%E5%8A%A0%E5%B7%A5%E8%B7%AF%E5%BE%84.gif)

## **激光填充雕刻**

激光填充雕刻是使用较小的激光功率和较快的加工速度，采用逐行扫描的方式，在材料表面烧蚀出图案，**适用于由线条构成的封闭的图形。**因此当图案被设置为激光填充雕刻时，软件会着重渲染图形的填充部分。加工路径示意图如下：

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/%E5%A1%AB%E5%85%85%E9%9B%95%E5%88%BB%E5%8A%A0%E5%B7%A5%E8%B7%AF%E5%BE%84.gif)

## **激光线条切割**

激光线条切割需要沿着图案的线条将把材料切穿，因此和激光线条雕刻非常相似，都是**适用于线条组成的矢量图**，但不同的是，激光线条切割需要更大的加工功率，更慢的切割速度，才能将材料切穿为特定形状。与激光线条雕刻相比，激光线条切割地图案在软件画布上渲染地更粗一些。

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/%E7%BA%BF%E6%9D%A1%E5%88%87%E5%89%B2%E5%8A%A0%E5%B7%A5%E8%B7%AF%E5%BE%84.gif)

激光线条雕刻，激光填充雕刻，激光线条切割三者在画布上的渲染效果和加工效果对比如下图所示。

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-6.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-5.png)

## **激光图像雕刻**

激光图像雕刻**适用于由像素点构成的位图对象**，比如需要在木板表面雕刻一张照片等场景，会采用逐行扫描的方式，在不同的像素位置变功率烧蚀。**位图并不是线条构成的矢量图形，因此位图不能被设置为激光线条雕刻、激光填充雕刻和激光线条切割。当你在画布中导入位图后，工艺类型中仅有“激光图像雕刻”和“打印后刀切”可选。**  
![2.gif](https://wiki.bambulab.com/software/bambu-suite/2d-processing-type-intro/1.jpg)

> 提示：如果需要对图片使用其他工艺类型（如激光线条雕刻、线条绘画等），可先用图形矢量化工具将图片转换为矢量线条，再设置为所需工艺。

|  |  |
| --- | --- |
|  |  |

## **基础刀切**

基础刀切就是使用切刀，在薄材料，比如纸张、卡纸、乙烯基等，切割下特定形状，简而言之就是个”自动裁纸机“，或者剪刀，**适用于加工矢量的线条图形。**显然，材料是什么颜色，最后裁剪下来就是什么颜色，因此对于基础刀切工艺的图案，软件会默认采用填充的方式进行渲染。不同的颜色代表用户需要使用不同颜色的材料进行裁剪。

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-2.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/img_v3_02hl_25b93e43-3d61-4027-b1c4-5aea139c742g.jpg)

## 线条绘画

该工艺专为在薄型材料（如普通A4纸、卡纸等）上进行图案绘制或文字书写而设计，适用于加工矢量线条图形。

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/20250213-173212.jpg)

若需进行文字书写：

1. 在左侧工具栏选择【文字】工具，默认生成可编辑的宽体文字
2. 如需单线字体：

   - 选中文字后，在编辑窗口选择"内置"→"单线体"。
   - 从筛选出的单线字体中选择所需样式即可创建。

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-1.png)

## 填充绘画

适用于矢量图形加工，支持图案绘制或文字书写，并会使用画笔将图案内部填充为实心色块。

![填充绘画示意图](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/img_v3_02kd_235791f6-d42c-4bdd-943a-5102e77355eg.jpg)

## **打印后刀切**

该功能需要先**使用2D打印机先在材料上（如A4纸）打印图案**，打印完成之后贴到刀切垫板上，使用切刀沿着图案的边框或者切割路径切割下来，**常用来制作小贴纸**。对于位图，切割路径会沿着图像的边缘，您可以在图片编辑工具里使用工具去除位图里不需要的部分（例如背景），再进行制作。具体请参考：[H2D打印后刀切功能指南](../../../h2/manual/post-printing-cutting.md)。

在进入准备页面发送作业后，软件中会弹出对话框，需要点击“发送”将图片发送给电脑已连接的纸质打印机（此步骤需要提前将电脑连接至打印机）。

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-9.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-10.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/2d-processing-type-intro/image-8.png)

打印完成后，去纸质打印机中取出打印的A4纸，然后按照下图中的示例，将纸贴在刀切垫板上，然后在显示屏上点击开始任务即可。**注意：打印出图案的纸必须贴在沿着第二条虚线框的左上角位置贴好。**

| **打印后的A4纸贴在垫板上** | **将图案用切刀切割下来** |
| --- | --- |
|  |  |

更便捷的使用方式是结合Bambu Suite的贴纸工具进行制作，可以参考[贴纸工具](sticker-tool.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
