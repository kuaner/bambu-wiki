---
path: zh/x1/troubleshooting/homing-z-axis-failed_part-unit-interference
title: "Z轴回中失败—组件干涉"
description: ""
tags: []
created: 2022-08-05T00:45:25.963Z
updated: 2024-06-19T09:25:34.250Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/homing-z-axis-failed_part-unit-interference
---

## 问题现象

1.  用户每次都会收到**“Z轴回中失败”** 错误。

![](https://wiki.bambulab.com/x1/troubleshooting/homing-z-failed-1/err_code.jpg)

2. 热床与废料滑梯之间有明显的干涉。

![](https://wiki.bambulab.com/x1/troubleshooting/homing-z-failed-2/interference.png)

## 造成的原因

正常情况下热床和废料滑梯之间应该至少有2 mm的间隙。但由于因为运输或螺丝松动等某些原因，热床会从原来的位置偏移。因此，在校准过程中，当热床向上移动时，热床接触到废料滑梯会被卡住从而导致校准或回中的失败。

## 解决方案：

重置热床位置

### 步骤 1 - 升起热床

关闭打印机电源。将工具头向废料滑滑梯A侧或B侧移动，这样热床就不会意外接触到喷嘴。

![](https://wiki.bambulab.com/x1/troubleshooting/homing-z-failed-2/position_a_or_b.jpg)

### 步骤 2 - 拧松螺栓

![](https://wiki.bambulab.com/x1/troubleshooting/hmscode/mc-assets/screw-cover.jpg)

有些批次的机器一颗螺丝是用贴纸盖住的，请放心戳破贴纸。

松开固定3个热床支架的6个螺丝，轻轻地将加热床向前拉并远离废料滑槽。它只需要移动几毫米，所以不要太大力。然后您可以倾斜打印机并伸手到打印机下方以移动Z轴皮带，或戴上一次性手套，然后慢慢顺时针旋转其中一个Z轴丝杆皮带以升高热床，直到热床立柱与前面的Z丝杆螺丝固定块接触(见下图)。

|  |  |
| --- | --- |
|  |  |

### 步骤 3 - 将热床向前门方向拉

在将加热床轻轻向前拉的同时，确认左右两边的定位插销接触到热床支撑架定位椭圆的后边缘(见图)。

|  |  |
| --- | --- |
|  |  |

### 步骤 4 - 重新拧紧螺栓

在将热床向前门轻轻拉出的同时，确保热床和废料滑梯之间有间隙并且不再接触，重新拧紧6个螺丝。拧紧螺丝后确认间隙仍然存在，并且插销正确对齐。如果没有，请通过松开6个螺丝并返回到步骤3再试一遍。

![](https://wiki.bambulab.com/x1/troubleshooting/homing-z-failed-2/gap.jpg)

### 步骤 5 - 校准

打开打印机电源并启动校准程序。

![](https://wiki.bambulab.com/x1/troubleshooting/homing-z-failed-2/calibration.jpg)

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
