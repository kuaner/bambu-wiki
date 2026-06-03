---
path: zh/p2s/maintenance/belt-tension
title: "P2S 皮带张紧"
description: "本文将详细为您介绍 P2S 打印机 XY 皮带。"
tags: []
created: 2025-10-14T14:40:26.461Z
updated: 2026-01-06T03:47:31.601Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/belt-tension
---

## 皮带张紧：

正确的皮带张紧对于 coreXY 运动系统至关重要。松动的皮带或皮带松动会导致 3D 打印中出现很多问题，例如会把圆圈打印得像椭圆。

皮带和龙门架构成了质量-弹簧系统，皮带为弹簧（k），龙门架为质量（m）。系统的[固有频率](https://en.wikipedia.org/wiki/Natural_frequency)为 f=√(k/m)。皮带松动会降低 k 和 f，进而影响振动补偿。

P2S 通过这个方程 f=√(k/m) 监控皮带张力。在校准过程中，电机会产生不同频率的振动，并寻找共振，当输入频率等于固有频率时就会发生共振。我们称这种操作为频率扫描，它会随着音调的增加产生相当多的噪声。

当 P2S 的固有频率发生变化时，需要收紧皮带。这只需简单的操作即可完成。

## 视频教程

## XY 轴皮带张紧

- 在进行皮带张紧之前请**关闭打印机电源并移除顶盖玻璃**。

![113.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/113.png)

- 使用 H2.0 内六角扳手拧松（**拧松 1-2 圈即可，请勿卸下螺丝**）四颗张紧螺丝，放松 XY 皮带。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image.png)

- 手动推动工具头，沿 XY 方向尽可能大范围地往返移动 3-5 次。

![111.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/111.webp)

- 再次拧紧打印机背后 4 颗螺丝；

> 注意：安装张紧器螺丝时请勿将螺丝拧太紧，避免滑丝。

|  |  |
| --- | --- |
|  |  |

## Z 轴皮带张紧

> ℹ️ **注意：** 极少数情况下，Z轴皮带在运转时可能会发出吱吱声。在皮带与Z轴皮带张紧器惰轮的接触处滴一小滴润滑油可以帮助降低噪音。过多的润滑油可能会导致Z轴运转不正常。

- 将打印机向后放倒，漏出底部皮带和张紧器。

![111.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/115.png)

- 使用H2.0螺丝刀拧松张紧器螺丝。（不用完全移除螺丝）

![111.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/116.png)

- 拉动打印机 Z 轴皮带，上下移动 3-5 次。

![111.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/112.webp)

- 随后锁紧张紧器螺丝，即可完成 Z 轴皮带的张紧操作。

![111.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/116.png)

## 校准

- 安装好顶盖玻璃，并接通打印机电源。

![111.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/114.png)

- 在屏幕上点击“校准-打印校准”，只需单独勾选“振动补偿”并完成该校准项即可。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image-4.png)

- Bambu Studio上也可以通过点击下面位置开启：

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image-1.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
