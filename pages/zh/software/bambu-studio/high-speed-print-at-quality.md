---
path: zh/software/bambu-studio/high-speed-print-at-quality
title: "高速与高质量打印"
description: ""
tags: []
created: 2025-05-29T03:36:11.245Z
updated: 2025-05-29T04:09:12.178Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/high-speed-print-at-quality
---

高打印速度意味着更多的振动、更大的接触力以及更短的冷却时间。在保证质量的前提下实现高速打印极具挑战性。挑战不仅在于打印机本身，还包括切片软件的能力。Bambu Studio 通过以下改进实现了这一目标。

![](https://wiki.bambulab.com/software/bambu-studio/high-speed-at-quality/high_speed_print.png)

这些改进如下所示：

1. **“圆弧运动”** 让打印头的运动更平滑，减少机器振动。
2. **智能冷却**，基于每种耗材的精细调节冷却参数。
3. **悬垂自动减速**，防止高速打印时变形。

---

## 圆弧运动 – 平滑路径，减少振动

3D 模型大多以三角网格成型，这意味着最终切片与打印路径由大量密集的直线段组成。当打印速度较慢时，这些密集的路径不会对打印质量产生明显影响。但当打印速度很高时，路径转折点会产生大量的瞬时冲击信号，从而引发噪音和振动。

为了解决这一问题，Bambu Studio 会在可接受的公差范围内生成圆弧路径。圆弧拟合方法基于 [ArcWelderLib](https://github.com/FormerLurker/ArcWelderLib)，在此对该项目的开源贡献表示衷心感谢。

![](https://wiki.bambulab.com/software/bambu-studio/high-speed-at-quality/arc-creation-example.png)

> 图片来源：  
> <https://plugins.octoprint.org/assets/img/plugins/arc_welder/arc_creation_example.png>

这样可以减少路径的转折点数量，使路径更加平滑，从而在快速打印中减少振动。

我们打印了同一个模型两次并录制了视频，以比较噪音、振动和打印质量。  
<https://public-cdn.bblmw.com/wiki/bambu-studio/arc-move.mp4>

![](https://wiki.bambulab.com/software/bambu-studio/high-speed-at-quality/test-model.png)

打印质量对比如下图所示：左侧启用了圆弧运动，右侧未启用。

![](https://wiki.bambulab.com/software/bambu-studio/high-speed-at-quality/arc-vs-non-arc.jpg)

圆弧拟合的弦公差与 Bambu Studio 中的分辨率设置一致。

![](https://wiki.bambulab.com/software/bambu-studio/high-speed-at-quality/resolution.png)

因此，如果模型网格精度较低，或者切片软件中分辨率设置得太小，圆弧拟合可能会失败。我们建议您直接将 STEP 文件导入 Bambu Studio 并使用默认分辨率切片，这样可以保留模型更多的细节并生成更多的圆弧路径。

---

## 基于精细调节冷却参数的智能冷却

冷却对于 FDM 打印机来说至关重要。Bambu Studio 提供了一套完整的冷却设置，能够控制风扇转速和打印速度，并且所有设置都经过精细的参数调节。这样，用户在使用拓竹官方耗材进行快速打印时，无需调整任何冷却设置，就能获得非常好的打印质量。

![](https://wiki.bambulab.com/software/bambu-studio/auto-cooling/enable-auto-slow-down.png)

![](https://wiki.bambulab.com/software/bambu-studio/auto-cooling/disable-auto-slow-down.png)

冷却设置的详细说明可查看此页面：  
👉 [自动耗材冷却设置](auto-cooling.md)。

---

## 自动悬垂降速

外墙的打印速度对模型表面质量影响很大，尤其是悬垂位置。一般来说，打印速度较慢时，悬垂部分不会出现问题。但在高速打印场景下，墙体速度过快会让悬垂质量非常差，即使层面积大、冷却时间充足。Bambu Studio 能够计算每个墙体段的悬垂角度，并在悬垂部分使用更慢的速度。这可以显著改善悬垂表面质量，同时保持大部分非悬垂区域的高速打印。

切片与打印的对比如下所示：

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/slicing-result.png)

![](https://wiki.bambulab.com/software/bambu-studio/slow-down-for-overhangs/result2.png)

更多详细信息可查看此页面：  
👉 [悬垂降速](slow-down-for-overhang.md)。
