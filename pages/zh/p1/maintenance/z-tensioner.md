---
path: zh/p1/maintenance/z-tensioner
title: "Z轴张紧器"
description: "本文章介绍了P1系列Z轴张紧器的更换步骤"
tags: ["p1", "p1p", "p1s", "z张紧器", "z轴"]
created: 2023-11-29T01:28:53.059Z
updated: 2025-06-09T08:02:06.151Z
source: https://wiki.bambulab.com/zh/p1/maintenance/z-tensioner
---

# Z轴张紧器

## 什么是Z轴张紧器

Z轴张紧器是安装在打印机底部，用于张紧Z轴皮带的零件。

![](https://wiki.bambulab.com/x1/maintenance/replace-z-tensioner/z-tensioner.jpg)

## 何时更换

- 张紧器惰轮异响，打油未能解决
- 张紧器惰轮轴承损坏

## 所需工具和材料

- H1.5, H2.0 内六角扳手
- 新的Z轴张紧器

# 安全提示

> ***重要提醒 ！***
>
> *在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。*
>
> *在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。*
>
> *如果您对本指南有任何疑问，请*[*点击这里提交工单*](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)*，我们将及时回复并为您提供所需的帮助。*

# 操作步骤 - 拆卸

## 步骤**1 - 清洁打印机底座**

清理打印机底座上的异物，特别是光杆处的残留物。

|  |  |
| --- | --- |
|  |  |

## 步骤2 **- 将热床下降到底部**

在显示屏上操作，将热床下降到底部，用3颗螺丝将3个滑块进行锁定。然后关闭打印机，断开电源连接。

> ***注意：****此处需用螺丝牢固固定热床或滑块但不要拧的过紧导致滑丝。****若Z轴单个滑块在后续步骤中由于皮带未张紧导致失去同步，则热床将无法调平。***

![](https://wiki.bambulab.com/p1/maintenance/z-motor/lower_the_head_bed_and_lock_the_sliders.jpg)

## 步骤3 - **移除玻璃上盖（P1S），侧放打印机**

侧放打印机。若您的打印机为P1S，请移除上盖后再将机器侧放，避免损坏。

**如需倒放打印机，在将打印机倒置前请务必拆除显示屏避免造成损坏！**拆除显示屏的方式可参考[屏幕组件](screen.md)

![](https://wiki.bambulab.com/p1/maintenance/z-motor/right_side_down.jpg)

## 步骤4 - 移除螺丝

释放弹簧，用H1.5内六角扳手移除3颗银色螺丝，用H2.0内六角扳手移除黑色的螺丝。

|  |  |
| --- | --- |
|  |  |

## 步骤5 - 移除张紧轮盖子和扭簧

取下张紧轮盖子，移除Z轴张紧弹簧。

![](https://wiki.bambulab.com/p1/maintenance/z-belt/remove_spring_and_tensioner.jpg)

## 步骤6 - 移除Z轴张紧器

将张紧器移动至导轨尽头以移除张紧器组件。注意组件里有一个螺母，小心切勿丢失。

|  |  |
| --- | --- |
|  |  |

# 操作步骤 - 组装

## 步骤1 - 安装Z轴张紧器

先确认前面提到的螺母有在组件上，将张紧器组件安装到相应位置，注意根据卡扣位完成安装。

|  |  |
| --- | --- |
|  |  |

## 步骤2 - 安装扭簧

将扭簧安装到相应的立柱上，注意扭簧的长边在左边，如下图所示。

![](https://wiki.bambulab.com/p1/maintenance/z-belt/remove_spring_and_tensioner.jpg)

## 步骤3 - 安装盖子，锁螺丝，卡弹簧

放上张紧器盖子，用H1.5内六角扳手锁入3颗银色螺丝固定张紧轮盖子，用H2.0内六角扳手拧入黑色螺丝，但不要拧紧。然后将弹簧的两侧分别卡入对应槽中，如下图所示。

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 步骤4 **-** 解除Z滑块锁定

正放打印机，然后移除锁定Z轴滑块的3颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/z-motor/unlock_the_sliders.jpg)

## 步骤5 - Z轴张紧皮带，拧紧螺丝

重新侧放打印机，往复拉动Z轴皮带，确认动作顺畅，然后锁紧黑色螺丝。

![](https://wiki.bambulab.com/p1/troubleshooting/tensioning_(1)_(1).webp)

|  |  |
| --- | --- |
|  |  |

# 功能确认

连接电源线并启动电源。运行设备校准流程，如果没有报错，更换完成。

如果出现异常，请排查组装是否有问题，特别是皮带是否正确张紧。排除后，再次运行设备自检。如果问题仍然存在，请联系Bambu Lab服务团队寻求进一步的帮助。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/calibration-cn.jpg)

# 结语

> *我们希望这份指南能为您提供有效信息和有效帮助。*
>
> *如果您对本文中描述的操作有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们将随时准备为您提供帮助并回答您的任何问题。*
>
> [*点击这里提交服务工单*](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
