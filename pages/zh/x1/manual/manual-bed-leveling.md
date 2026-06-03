---
path: zh/x1/manual/manual-bed-leveling
title: "X1/P1 系列热床手动调平"
description: "介绍如何对 X1/P1 系列打印机的热床进行手动调平。"
tags: ["手动调平", "热床"]
created: 2022-11-02T09:28:11.494Z
updated: 2026-05-28T02:58:44.349Z
source: https://wiki.bambulab.com/zh/x1/manual/manual-bed-leveling
---

## 热床手动调平

Bambu Lab X1/P1系列打印机的热床是已调整好的。 由于各种运输条件，热床的平整度可能不准确。 为了帮助解决这个问题，我们准备了一个热床调平的操作指引，以确保打印平台表面是平整的。

### 什么时候需要手动调平

只有当您发现热床调平不准确或客户服务团队提出要求时，才需要进行手动调平。

### 调平前的准备

在操作过程中，您可以选择放置或不放置板子，这两种方式都是可行的。

在开始热床手动调平之前，准备工作很重要：

- 确保喷嘴清洁且喷嘴上没有任何材料。 如果需要，加热喷嘴并擦拭喷嘴以确保其清洁。
- 检查热床调平螺母并确保它们正确拧紧。 调平螺母与热床螺丝齐平即可，不可过松或过紧，如下图所示。

![](https://wiki.bambulab.com/x1/manual/bed-leveling/screw_tension.jpg)

### 开始调平

首先，下载以下G CODE文件，并将其传输到 SD 卡中。

[/x1/manual/bed-leveling/hotbed\_tramming.gcode](https://wiki.bambulab.com/x1/manual/bed-leveling/hotbed_tramming_20221102.gcode)

其次，将SD 卡插入打印机卡槽，待识别后，选中上述G CODE 文件，点击开始打印。

![](https://wiki.bambulab.com/x1/manual/bed-leveling/hotbed_tramming_print.jpg)

加载 G code 文件后，打印机将进行回中操作，然后移至热床左前方并等待 30 秒。 这时，请小心转动热床对应位置的调平螺母，请确保喷嘴刚好未接触到打印表面，不要让打印面板撞上喷嘴。

> 拧紧螺母会使热床远离喷嘴，拧松螺母会使热床靠近喷嘴。

![](https://wiki.bambulab.com/x1/manual/bed-leveling/nozzle_touching_the_print_surface.jpeg)

30 秒后，喷嘴将移动到后方的调平螺母上方。 重复调整操作，使得打印面板刚好不接触喷嘴。 再之后，调整右前方的调平螺母。

当第一次调平完成后，该过程将再重复两次，但停留时间将变为15秒，以便您微调并仔细检查喷嘴和床之间的距离。

### 重复该过程（如果需要的话）

如果你想重复热床手动调平的操作，请在运行G code文件前，先手动调整调平螺母，使螺丝与螺母表面齐平。

## **设备校准**

X1：在屏幕点击 **控制 > 工具 > 校准**，开始进行校准。

![](https://wiki.bambulab.com/x1/manual/bed-leveling/20250115-172310.jpg)

P1: 点击 **设置 > 校准**，开始进行校准。

|  |  |
| --- | --- |
|  |  |

如果一切正常，并且校准过程中没有出现错误或警告，则调平成功。如果仍有问题，请联系服务团队寻求进一步帮助。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
