---
path: zh/h2/maintenance/belt-tension
title: "H2D 皮带张紧"
description: "关于 H2D 打印机 XY 轴皮带张紧的操作"
tags: []
created: 2025-04-14T08:28:34.523Z
updated: 2026-03-24T02:39:12.768Z
source: https://wiki.bambulab.com/zh/h2/maintenance/belt-tension
---

## 皮带张紧

正确的皮带张紧对于 core XY 运动系统至关重要。皮带松动会导致 3D 打印中出现很多问题，例如会把圆圈打印得像椭圆。

皮带和 X 轴组件构成了质量-弹簧系统，皮带为弹簧（k），整个 X 轴组件为质量（m）。系统的[固有频率](https://en.wikipedia.org/wiki/Natural_frequency)为 f=√(k/m)。皮带松动会降低 k 和 f，进而影响振动补偿。

H2D 通过这个方程 f=√(k/m) 监控皮带张力。在校准过程中，电机会产生不同频率的振动，并寻找共振，当输入频率等于固有频率时就会发生共振。我们称这种操作为频率扫描，它会随着音调的增加产生相当多的噪声。

当 H2D 发现固有频率发生变化时，它将收紧皮带。这是一个半自动过程，只需简单的操作即可完成。您只需拧下皮带张紧器上的四颗螺丝，前后移动工具头若干次，并在最后将工具头两端滑车都紧贴后壁，然后再次拧紧螺丝即可。皮带收紧器中的弹簧系统会将皮带收紧到正确的状态，整个过程操作起来是比较简单的。

## 皮带张紧步骤

> 重要提醒：操作之前请先关闭打印机电源。

### XY 皮带张紧

1. 拧松皮带张紧器左侧和右侧共 **4** 个螺丝。**拧松 1-2 圈即可，请勿卸下螺丝**；

|  |  |
| --- | --- |
|  |  |

2. 轻轻地**来回移动工具头几次**，最后将其移至打印机**后端**；

![来回推动.webp](https://wiki.bambulab.com/h2/maintenance/belt-tension/%E6%9D%A5%E5%9B%9E%E6%8E%A8%E5%8A%A8.webp)

\*画面仅做示意如何推动工具头前后移动，您无需拆下热端。

移动后，确保工具头和线轨位置如下图所示，再进行下一步。

![位置.png](https://wiki.bambulab.com/h2/maintenance/belt-tension/%E4%BD%8D%E7%BD%AE.png)

3. 再次拧紧 4 颗螺丝。皮带张紧器中的弹簧结构会将皮带张紧至正确的张紧度。

|  |  |
| --- | --- |
|  |  |

> 注意：请勿将螺钉拧得过紧，以免滑丝。

### Z皮带张紧

移除上盖玻璃，将打印机倾斜放置，使用 H2.0 螺丝刀拧松张紧器螺丝。（不用移除该螺丝）

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-19.png)

用手来回拉动 Z 轴皮带 3-5 次，确认动作顺畅，然后使用 H2.0 内六角扳手将 Z 轴张紧器滑块固定螺丝拧紧（M3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-21.png)

拧紧之后将打印机重新正放在平稳的桌面/地面，并盖上上盖玻璃。

> 由于打印机比较重，建议两个人一起操作，避免由此带来的损伤。

## 校准

在完成皮带张紧操作后，需要重新校准共振频率识别，以记录设备新的共振特性。

H2D 可通过机器屏幕或 Bambu Studio 进行校准操作。

|  |  |
| --- | --- |
|  |  |

![pixpin_2025-03-09_19-59-01.png](https://wiki.bambulab.com/screen-operation/calibration/pixpin_2025-03-09_19-59-01.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
