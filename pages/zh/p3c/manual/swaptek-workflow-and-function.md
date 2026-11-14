---
path: zh/p3c/manual/swaptek-workflow-and-function
title: "P3C Swaptek 闪切系统工作流程介绍"
description: "本文介绍 Swaptek 闪切系统的工作流程。"
tags: []
created: 2026-11-13T08:52:52.730Z
updated: 2026-11-13T08:52:52.730Z
source: https://wiki.bambulab.com/zh/p3c/manual/swaptek-workflow-and-function
---

## 闪切系统概述

**闪切（Swaptek）系统**是 P3C 打印机实现多材料/多色打印的核心技术模块。该系统主要由闪切挂架和打印头组成，通过霍尔传感器和磁铁的配合，实现精准定位、自动抓取、可靠换头。

![p3c_swaptek___________-image-3.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/swaptek-workflow-and-function/zh/p3c_swaptek___________-image-3.png)

## 回零流程

挂架先向上运动，初步获取上极限位置，再向下移动一定距离后，继续向上运动，获取上限位的精确位置，然后向下运动获取下极限位置的精确坐标。

> 通过上下限位的精确位置可获取挂架的最大运动行程，根据距离即可判断挂架运动路径上是否有障碍物或者皮带是否松脱。

最后，挂架向上运动待命，完成回零。

![p3c_swaptek___________-pixpin_2026-09-24_11-36-34.webp](https://public-cdn.bblmw.com/wiki/new/p3c/manual/swaptek-workflow-and-function/zh/p3c_swaptek___________-pixpin_2026-09-24_11-36-34.webp)

## 校准流程

> 可在打印机屏幕上点击：设置 > 校准 > 挂架对位校准，开启校准。
>
> |  |  |
> | --- | --- |
> | p3c_swaptek___________-image-2.png | p3c_swaptek___________-image-1.png |

打印机固件已在内部定义好每个泊位的 XY 坐标，当工具头回中后，工具头的泊位标定传感器会在预设的泊位坐标附近搜索打印头上的磁铁；找到磁铁后，霍尔传感器将记录该磁铁的精确 XY 坐标，并继续检测磁铁所在的 Z 坐标。

|  |  |
| --- | --- |
| 检测 XY 坐标 | 检测 Z 坐标 |

每次完成热端泊位坐标的标定后，工具头会按照以下顺序进行测试：

1. **磁铁位置校核：**工具头上的标定霍尔传感器会再次确认磁铁的精确位置；
2. **抓取位置校核：**验证工具头的夹持点是否正好位于磁铁中心，确保抓取动作对齐；
3. **热端取放测试：**自动把热端从挂架取下再放回，检验取放动作的可靠准确性。

![p3c_swaptek___________-pixpin_2026-09-24_12-12-41.webp](https://public-cdn.bblmw.com/wiki/new/p3c/manual/swaptek-workflow-and-function/zh/p3c_swaptek___________-pixpin_2026-09-24_12-12-41.webp)

在初步标定完成后，系统立即进行热端取放测试，随后再执行二次标定，并将两次标定得到的 XY 和 Z 坐标进行对比：若两次标定结果在设定误差范围内，则本次标定被视为可靠；若差值超出阈值，系统会识别出因人工放置不正（例如磁铁偏斜、工具头倾斜）导致的第一次标定异常，并判定为不可靠。

## 换头流程

- 当挂架未接收到换打印头命令时，挂架会保持在待命（上升）位置，便于用户观察打印件状态；

![p3c_swaptek___________-image.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/swaptek-workflow-and-function/zh/p3c_swaptek___________-image.png)

- 当挂架接收到换打印头命令时，挂架会预先降低高度至工作位置，等待工具头将打印头送回待载位置。当工具头移动至预设位置并将打印头解锁后，挂架会吸附打印头至固定位置，并上升回到待命状态。

![p3c_swaptek___________-pixpin_2026-09-24_15-59-17.webp](https://public-cdn.bblmw.com/wiki/new/p3c/manual/swaptek-workflow-and-function/zh/p3c_swaptek___________-pixpin_2026-09-24_15-59-17.webp)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
