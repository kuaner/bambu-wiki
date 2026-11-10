---
path: zh/r1/troubleshooting/x-axis-skew-adjustment
title: "R1 X 轴歪斜调整指南"
description: ""
tags: []
created: 2026-11-09T03:42:05.030Z
updated: 2026-11-09T03:43:15.264Z
source: https://wiki.bambulab.com/zh/r1/troubleshooting/x-axis-skew-adjustment
---

## 何时调整

若设备因运输颠簸或撞击等意外情况导致 X 轴发生歪斜，可参考本教程进行校准。

## 故障现象

X 轴歪斜可能导致以下一个或多个故障。

1. **系统报错： **歪斜过大时，在进行**电机定位校准**或**视觉精度校准**过程中，易触发“XY 电机丢步”报错，甚至导致自动光路校准失败。

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/001.png)

- **结构偏差：** X 轴移动到最后侧，目视可观察到 X 轴与框架不平行，存在轻微歪斜。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/002.png)

- **加工位置偏差：** 实际加工位置与软件预览位置误差过大，且切割/雕刻线条出现倾斜。

![003.jpg](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/003.jpg)

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 所需工具和材料

- H2.0 内六角螺丝刀

### 步骤 1.解锁 Y 轴皮带张紧器

使用 H2.0 内六角螺丝刀卸下左右两侧各 2 颗固定螺丝，取下两侧的 Y 轴张紧器盖板。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/004.png)

使用 H2.0 内六角螺丝刀拧松张紧器的 3 颗固定螺丝（**无需完全拧下**），释放张紧器。重复此操作完成另一侧。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/005.png)

依次解锁两侧的张紧弹簧。

![006.webp](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/006.webp)

### 步骤 2.粗调 X 轴

用手握住 X 轴外侧两端，向后方框架均匀施力撞击几次，直至 X 轴两侧均紧贴后侧框架，完成初步调正。

> 调整时听到“咔咔”声属于正常现象，这是皮带齿与光轴同步轮齿在轻微跳齿时因震动发出的声音。此操作频次极低，不会对皮带整体寿命造成实质性影响。

![007.webp](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/007.webp)

当 X 轴基本调正后，参照图示将左右两侧的 Y 轴张紧器弹簧挂回（此时**暂不锁紧张紧器固定螺丝**）。

![008.webp](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/008.webp)

### 步骤 3.微调 X 轴

> 再次检查 X 轴是否平行，如果已经平行则跳过此步骤。

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/009.png)

重新将 X 轴推近后侧框架，检查其是否已经完全平行。若仍有轻微歪斜，可选择以下方法之一进行微调：  
**方法一（直接扭转法）：** 双手直接握住 X 轴两端，朝歪斜的相反方向适度用力扭转 X 轴。听到跳齿声后松手，检查 X 轴是否平行；若未完全平行，可重复此操作，直至 X 轴与后侧框架完全平行。

![010.webp](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/010.webp)

**方法 2（垫片辅助法）：** 在缝隙偏小的一侧塞入一个厚度合适的薄片（建议 2~3 mm），然后继续向后推撞 X 轴进行复位。听到跳齿声后停止，检查并重复此操作，直至 X 轴与后侧框架完全平行。

![011.webp](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/011.webp)

确认 X 轴与后侧框架完全平行后，方可进入下一步。

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/012.png)

### 步骤 4.锁定 Y 轴皮带张紧器

使用 H2.0 内六角螺丝刀依次锁紧左右张紧器固定螺丝，共计 6 颗。

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/013.png)

装回张紧器盖板，使用 H2.0 内六角螺丝刀拧入 2 颗螺丝进行固定。另一侧采用相同方法安装。

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/troubleshooting/x-axis-skew-adjustment/zh/014.png)

## 功能验证

开机，在设备屏幕上选择设置 > 校准，分别运行**电机定位校准、光路自动校准以及视觉精度校准**，如果校准顺利完成，则上述安装正确。

|  |  |
| --- | --- |
| 015.png | 016.png |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
