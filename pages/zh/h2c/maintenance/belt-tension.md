---
path: zh/h2c/maintenance/belt-tension
title: "H2C 皮带张紧"
description: "关于 H2C 打印机 XYZ 轴以及热端架皮带张紧的操作步骤。"
tags: []
created: 2025-11-18T13:19:11.106Z
updated: 2026-03-18T06:26:15.093Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/belt-tension
---

## 皮带张紧

正确的皮带张紧对于 core XY 运动系统至关重要。皮带松动会导致 3D 打印中出现很多问题，例如会把圆圈打印得像椭圆。

皮带和龙门架构成了质量-弹簧系统，皮带为弹簧（k），龙门架为质量（m）。系统的[固有频率](https://en.wikipedia.org/wiki/Natural_frequency)为 f=√(k/m)。皮带松动会降低 k 和 f，进而影响振动补偿。

H2C 通过这个方程 f=√(k/m) 监控皮带张力。在校准过程中，电机会产生不同频率的振动，并寻找共振，当输入频率等于固有频率时就会发生共振。我们称这种操作为频率扫描，它会随着音调的增加产生相当多的噪声。

当 H2C 发现固有频率发生变化时，它将收紧皮带。这是一个半自动过程，只需简单的操作即可完成。您只需拧下皮带张紧器上的四颗螺丝，前后移动工具头若干次，并在最后将工具头两端滑车都紧贴后壁，然后再次拧紧螺丝即可。皮带收紧器中的弹簧系统会将皮带收紧到正确的状态，整个过程操作起来是比较简单的。

## 皮带张紧步骤

> 重要提醒：操作之前请先关闭打印机电源。

### XY 皮带张紧

1. 拧松皮带张紧器左侧和右侧共 **4** 个螺丝。**拧松 1-2 圈即可，请勿卸下螺丝**；

|  |  |
| --- | --- |
|  |  |

2. 轻轻地**来回移动工具头几次**，皮带张紧器中的弹簧结构会将皮带张紧至正确的张紧度；然后将工具头停靠在中间靠后位置。

![mvi_1389.webp](https://wiki.bambulab.com/h2c/maintenance/belt-tension/mvi_1389.webp)

3. 完成后再次拧紧背后 4 颗螺丝，固定张紧器器位置完成张紧。

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

### 热端挂架皮带张紧

使用 H2.0 螺丝刀拧下两颗固定螺丝，移除保护壳。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/1.png)

找到电机三颗固定螺丝，用H2.0螺丝刀将其拧松（注意：仅松动即可，切勿完全拆卸螺丝，避免电机脱落）。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/2.png)

螺丝松动后，轻轻晃动电机，确保电机可灵活活动，为后续张紧调节预留空间。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/5.webp)

接下来调节底部张紧螺丝，在锁紧螺丝的过程中，需持续轻轻按压皮带，通过触感判断张紧力度，确保张力均匀适中。

|  |  |
| --- | --- |
|  |  |

张紧调节完成后，再次轻轻按压皮带，若能明显感受到皮带紧绷、无松动回弹，即为正常状态。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/6.webp)

如下图示，若按压皮带时仍感觉松垮、无紧绷感，说明张紧度不足，需重新调整张紧螺丝。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/7.webp)

张紧完成后锁紧电机三颗固定螺丝，固定电机位置。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/5.webp)

将保护壳复位，对准安装孔位后，拧紧两颗固定螺丝，完成整个张紧操作。

![1.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/1.png)

## 校准

在完成皮带张紧操作后，需要重新校准共振频率识别，以记录设备新的共振特性。

H2C 也可通过机器屏幕或 Bambu Studio 进行校准操作。

|  |  |
| --- | --- |
|  |  |

![pixpin_2025-03-09_19-59-01.png](https://wiki.bambulab.com/screen-operation/calibration/pixpin_2025-03-09_19-59-01.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
