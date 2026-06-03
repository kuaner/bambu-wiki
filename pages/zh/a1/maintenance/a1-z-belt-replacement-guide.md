---
path: zh/a1/maintenance/a1-z-belt-replacement-guide
title: "A1 Z 皮带更换指南"
description: "更换 A1 打印机 Z 皮带的操作步骤"
tags: []
created: 2024-08-16T03:38:00.220Z
updated: 2026-05-12T06:39:02.492Z
source: https://wiki.bambulab.com/zh/a1/maintenance/a1-z-belt-replacement-guide
---

## Z 皮带

Z 皮带是安装在 Z 轴底部的闭口皮带，它连接 Z 电机和 Z 轴丝杆，带动工具头完成在 Z 方向上移动。

## 适用打印机型号

Bambu Lab A1

## 可解决的问题

当出现下列情况时需要更换：

- 皮带断裂
- 皮带老化/磨损，影响打印机的功能。

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- Z 皮带（购买链接：[京东](https://item.jd.com/10092503715192.html) [天猫](https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-25177047232.249.206e51d7iiDieu&id=755525852131&rn=605370164bf16c6b338ba7832eabdc79&abbucket=6&skuId=5208956976312)）
- H2.0 内六角扳手
- H1.5 内六角扳手

## 拆解步骤

### 移除 Y 轴上盖

步骤 1：关闭打印机。

步骤 2：正放打印机，将 X 轴移动到顶部。

![](https://wiki.bambulab.com/a1/maintenance/printer/raise_x_axis.jpg)

步骤 3：将热床移动到屏幕的一端，然后移除 Y 轴上盖。

|  |  |
| --- | --- |
|  |  |

### 移除 Z 轴底板

步骤 1：用 H2.0 内六角扳手移除 4 颗绿色标识的螺丝。

![remove_screws_2.jpg](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/remove_screws_2.jpg)

步骤 2：用 H2.0 内六角扳手，将 Z 皮带张紧螺丝**拧松一圈（请勿完全松开）**。

> Z 皮带的张紧螺丝位于底座靠右侧立柱的位置，将热床前移后可以看到。

|  |  |
| --- | --- |
|  |  |

步骤 3：将热床移动至屏幕相反方向的一端，然后打印机的背面放置桌面上。

> 建议提前用纸板垫在桌面上，用于保护打印机。放置时，请将热床也放在桌面上，避免翻转打印机时热床突然掉下。

步骤 4：用 H2.0 内六角扳手移除 15 颗螺丝后，即可取下底板。

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/pic2.png)

> 底板内部突出的螺丝头较为尖锐，部分金属框架上可能存在毛刺。在拆装过程请小心操作，注意规避，或佩戴防割手套进行操作。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### 移除 Z 皮带

先按住张紧器，使 Z 皮带松弛，然后即可将皮带拉出移除。

|  |  |
| --- | --- |
|  |  |

## 安装步骤

### 安装 Z 皮带

步骤 1：检查 X 轴是否与顶部平行。如果不平行，可用手将 X 轴推至顶部，确保处于水平状态。

|  |  |
| --- | --- |
| X 轴与顶部不平行 |  |

步骤 2：按照图示的方式，先将皮带安装至右下方的同步轮和张紧器。

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/pic12.png)

步骤 3：按住 Z 张紧器，然后将 Z 皮带套入左侧的同步轮。

|  |  |
| --- | --- |
|  |  |

步骤 4：拉动皮带，检查是否移动顺畅。

如果不顺畅，请检查皮带是否安装正确，以及丝杆是否被卡住。

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/pic14.png)

### 安装 Z 轴底板

步骤 1：放置底板， 然后用 H2.0 内六角扳手拧紧图示 15 颗螺丝。

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/pic2.png)

步骤 2：将打印机正放至桌面，用 H2.0 内六角扳手拧紧图示 4 颗螺丝。

![remove_screws_2.jpg](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/remove_screws_2.jpg)

步骤 3：装回 Y 轴上盖。

![install_y_cover.jpg](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/install_y_cover.jpg)

### 张紧 Z 皮带

步骤 1：打开打印机电源，进入打印机运动控制界面，执行一次回零。

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/screen4.png)

步骤 2：等待回零完成后，先后点击右侧的向上/方向键 **1 次**，使 X 轴沿 Z 轴方向上下分别移动 **1 次。**

> 向下移动 X 轴前，请确保喷嘴不会撞击到热床！

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/screen6.png)

步骤 3：用 H2.0 内六角扳手拧紧 2 颗张紧螺丝。

|  |  |
| --- | --- |
|  |  |

## 操作后校准

在**校准**页面，仅选择**振动补偿**，点击**开始**。

请执行此步骤以确保打印机正常工作。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
