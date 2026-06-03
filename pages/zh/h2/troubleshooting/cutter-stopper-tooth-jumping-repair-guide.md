---
path: zh/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide
title: "H2系列切刀顶块更换和跳齿修复指引"
description: ""
tags: []
created: 2025-04-03T02:27:07.919Z
updated: 2026-02-24T09:46:36.537Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide
---

![img_2782.jpg](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/img_2782.jpg)

## 何时使用

当打印机执行换料切断的时候出现顶偏的情况，可能是切刀顶块组件内的齿轮跳齿导致的，此时需要打开刀切顶块组件进行调整。

![异常.jpg](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%BC%82%E5%B8%B8.jpg)

> 如果**首次使用H2系列**切料时就出现切刀触发杆跳齿问题，可能是因为开箱时意外碰撞导致，可参考下方提供的快速修复指南进行处理。

### 快速修复指南

|  |  |
| --- | --- |
|  |  |
| 正常状态：顶杆水平时，齿条和顶块末端平齐 | 异常状态：顶杆水平时，齿条和顶块末端突出一段 |

**在向后按压齿条的同时，往机箱后方拨动切刀顶杆。**

![img_3312.webp](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/img_3312.webp)

> 此方式既适用于H2D，也适用于H2S。如果通过此方式不能将切刀顶块修复，建议您参考以下步骤移除切刀顶块进行修复。

## 所需工具

H2.0 内六角螺丝刀

[H2D 切刀顶块修复辅助工具](https://makerworld.com.cn/zh/models/1251170-h2d-qie-dao-ding-kuai-xiu-fu-fu-zhu-gong-ju#profileId-1336646)（可选，此链接的模型仅适用于H2D，不可用于H2S）

H2S 切刀顶块修复模型即将上传至Makerworld网站上，敬请期待

10 分钟

> 如果在此之前需要打印辅助工具，需要注意区分左右。

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 视频指南

> 视频中演示的圆形齿轮螺丝安装位置仅适用于 H2D，H2S 请依照后续图文教程的指引进行安装。

## 操作指南

### 移除切刀顶块

使用 H2.0 内六角螺丝刀移除4颗固定螺丝，红色螺丝为 BT2.6\*8 ，绿色螺丝为 M2.5\*5。

![移除.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E7%A7%BB%E9%99%A4.png)

下图绿色内为上下两齿条正确位置，红色内为异常状态，需要重新调整齿轮位置。

![对比.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%AF%B9%E6%AF%942.jpg)

### 调整齿轮位置

使用H2.0螺丝刀移除右侧齿轮固定螺丝，并取出齿轮。

|  |  |
| --- | --- |
|  |  |

接下来，向**下按压齿条**，同时**向下旋转切刀顶块**组件

|  |  |
| --- | --- |
|  |  |

下图所示为正确齿轮对齐时的状态。

![对齐.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%AF%B9%E9%BD%90.png)

#### H2D 圆形齿轮安装

> 请注意，在调节圆形齿轮时，H2D 与 H2S 的安装孔位置不同。

1. 找到左侧的圆形齿轮安装孔

![安装螺丝.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%AE%89%E8%A3%85%E8%9E%BA%E4%B8%9D.png)  
2. 滑动下侧齿条，使其顶在最左侧极限位置：

![向左.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%90%91%E5%B7%A6.png)

3. 对齐左侧安装孔和圆形齿轮的圆心，将齿轮放入齿条之间：

![对准.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%AF%B9%E5%87%86.png)

4. 拧紧固定螺丝：

![1](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%8F%96%E5%87%BA%E8%9E%BA%E4%B8%9D.png)

#### H2S 圆形齿轮螺丝安装

1. 找到右侧的圆形齿轮安装孔

![h2s-gear-adjustion.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/h2s-gear-adjustion.png)

2. 滑动下侧齿条，使齿条右边缘和外壳齐平：

![image.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/image.png)  
3. 对齐右侧安装孔和圆形齿轮的圆心，将齿轮放入齿条之间：

![image2.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/image2.png)

4. 拧紧固定螺丝：

![image3.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/image3.png)

> 如果有打印好的安装治具，可将其装入切刀顶块，用来辅助安装齿轮和螺丝。请注意，正确嵌入辅助模型后，需利用左右限位凸点固定，两侧都不应有任何移动。

[H2D 切刀顶块修复辅助工具（H2D专用）](https://makerworld.com/zh/models/1325689-h2d-filament-cutter-stopper-installation-aid#profileId-1362848)

[H2S 切刀顶块修复辅助工具（H2S专用）](https://makerworld.com.cn/zh/models/1623864-h2s-qie-dao-ding-kuai-xiu-fu-fu-zhu-gong-ju#profileId-1777844)

![h2s-stopper.jpg](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/h2s-stopper.jpg)

![h2s-stopper-aid.webp](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/h2s-stopper-aid.webp)

> ![治具.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E6%B2%BB%E5%85%B7.png)

安装完成后拨动底部齿条，检查摆杆是否回正和移动是否顺畅。  
如果齿条移动**卡涩**，可以使用H2.0内六角扳手适当拧松对应齿条的**两颗螺丝**，顶部和底部齿条各两颗固定螺丝。  
![左右.png](https://wiki.bambulab.com/h2/troubleshooting/cutter-stopper-tooth-jumping-repair-guide/%E5%B7%A6%E5%8F%B3.png)

> 安装切刀顶块前，需将 X 轴整体移动到最前（靠近前门）再进行安装。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
