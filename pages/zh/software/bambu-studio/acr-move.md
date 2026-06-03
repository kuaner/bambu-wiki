---
path: zh/software/bambu-studio/acr-move
title: "圆弧运动"
description: ""
tags: ["bambu studio"]
created: 2023-07-26T13:23:08.666Z
updated: 2025-05-29T03:44:04.384Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/acr-move
---

## 圆弧拟合

3D 模型大多为三角形面组成的，这意味着所有 3D 模型中的圆弧，在STL文件中已经被转化为使用大量的短直线线段模拟而成的曲线。您可以在“简化模型”功能中勾选“显示线框”，就可以看到组成模型的三角形面以及组成圆弧的小线段（详见[简化模型 | Bambu Lab Wiki](simplify-model.md)），如下图所示。

![](https://wiki.bambulab.com/software/bambu-studio/arc-move/线段组成圆弧.png)

这样在最终的切片和实际打印中，也会按照这个规划路径进行运动和打印。当打印机速度较慢时，这些密集的线段对打印质量没有明显的不良影响。但当打印速度较高时，在线段的拐点处会产生大量的瞬态脉冲信号，从而带来噪声和振动。

为了改善这个问题，Bambu studio 通过在一定可接受的公差范围内拟合来生成圆弧运动路径，使得导出的 Gcode 支持 G2/G3 圆弧运动。这样可以减少线段拐点的数量，使路径更加平滑，减少快速打印时的振动。

圆弧拟合方法基于[ArcWelderLib](https://github.com/FormerLurker/ArcWelderLib)，衷心感谢您提供如此优秀的开源代码。

我们将一个模型打印两次，并录制视频，比较噪音、振动和质量。

视频前半段是禁用了此功能情况下拍摄的，后半段是启用了它的。

<https://public-cdn.bblmw.com/wiki/bambu-studio/arc-move.mp4>

## 工作原理

圆弧拟合的过程如下图所示，先找工具头移动路径上的三个连续点采用**取外接圆**的方式拟合成一个圆弧（P1-P2-P3），并确保创建的圆弧与原始路径最大的偏差小于圆弧拟合最大容许值（也就是分辨率值）。然后继续在之后的路径上继续寻找点，确认偏差值是否在最大拟合容许值范围内，直到找到超出范围的点后将其剔除（P6），完成之前这些点的圆弧拟合（P1-P5）。然后以此类推，重复之前的过程直到整个 Gcode 结束。

![](https://wiki.bambulab.com/software/bambu-studio/high-speed-at-quality/arc-creation-example.png)

图片来源:  https://plugins.octoprint.org/assets/img/plugins/arc\_welder/arc\_creation\_example.png

## 操作指导

您可以在这里启用/关闭圆弧拟合功能，为了实现高速打印下更好的打印效果，**该功能是默认开启的。**

![](https://wiki.bambulab.com/software/bambu-studio/arc-move/开启圆弧拟合.png)

分辨率（精度）即为圆弧拟合路径与原始路径的最大偏差（弓高误差），您可以通过降低分辨率（增加这个值）来使原本精度较低的模型在切片后增加更多的圆弧。不过我们通常不建议把这个值设置太大。如果想要把精度较低的模型去强行成拟合圆弧而设置一个较大的分辨率，模型会出现明显的层间错位，甚至导致模型完全变形。

![](https://wiki.bambulab.com/software/bambu-studio/arc-move/分辨率设置.png)

以下是调节不同分辨率后模型圆弧表面的对比：

![](https://wiki.bambulab.com/software/bambu-studio/arc-move/默认分辨率拟合.png)

**默认分辨率**

![](https://wiki.bambulab.com/software/bambu-studio/arc-move/0.03分辨率拟合.png)

**分辨率0.03mm**

如果强行降低分辨率，把它设为一个较大值，不同层拟合的弧线会形状不一导致模型表面错位破损：

![](https://wiki.bambulab.com/software/bambu-studio/arc-move/1mm分辨率拟合.png)

**分辨率1mm**

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
