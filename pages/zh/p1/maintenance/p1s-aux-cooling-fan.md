---
path: zh/p1/maintenance/p1s-aux-cooling-fan
title: "更换P1S辅助部件冷却风扇"
description: "如何更换P1S的辅助部件冷却风扇"
tags: ["辅助部件冷却风扇"]
created: 2023-06-30T03:28:09.925Z
updated: 2026-04-28T02:09:57.299Z
source: https://wiki.bambulab.com/zh/p1/maintenance/p1s-aux-cooling-fan
---

## P1S辅助部件冷却风扇

辅助部件冷却风扇是一个强大的12W冷却风扇，安装在腔室的左侧，为高速打印提供了更好的冷却条件。

![](https://wiki.bambulab.com/x1/maintenance/replace-aux-fan/new_fan.jpg)

## 何时更换/安装

叶片损坏或风扇电机故障，风扇异响

## 工具和材料

新的金属后面板

H2.0 内六角扳手

螺丝清单

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 型号 | 位置 | 规格 |  | 型号 | 位置 | 规格 |
| 螺丝A | BT3\*5 | 后面板 |  | 螺丝B | M3\*4.5 | 后面板 |  |
| 螺丝C | ST3\*4.5 | 后面板 |  | 螺丝D | BT3\*12 | 风扇 |  |

# 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

# 移除辅助部件冷却风扇

## **第 1 步 -下降热床**

倾斜打印机，拉动Z轴皮带，下降热床，将辅助部件冷却风扇完全显露出来。

## **第2步 - 移除金属后面板**

参考 [金属后面板](p1s-rear-panel.md) 的相关指引，移除金属后面板。

![](https://wiki.bambulab.com/p1/maintenance/p1s-rear-panel/without_rear_panel.jpg)

## 步骤3 - 断开辅助部件冷却风扇电缆

|  |  |
| --- | --- |
| 找到MC板上辅助部件冷却风扇的连接器(FAN-2) | 然后断开电缆连接 |

## 步骤4 - 移除辅助部件冷却风扇

|  |  |
| --- | --- |
| 用H2.0 内六角扳手拧下固定风扇的2颗螺丝D | 通过手用力将还有双面胶固定的风扇与侧板分离 |

将风扇电缆拉出，取下辅助部件冷却风扇。

![](https://wiki.bambulab.com/p1/maintenance/p1s-aux-part-cooling-fan/disattached.jpg)

# 安装新的辅助部件冷却风扇

## 步骤1 - 安装风扇

|  |  |
| --- | --- |
| 撕掉风扇上的双面胶保护纸 | 根据螺柱位将风扇安装到位 |

锁入2颗螺丝D固定

![](https://wiki.bambulab.com/p1/maintenance/p1s-aux-part-cooling-fan/2_screws.jpg)

## 步骤2 - 连接风扇电缆

|  |  |
| --- | --- |
| 将风扇电缆穿过侧面板和内搁板之间的间隙 | 将电缆连接到MC板上标识为FAN\_2的连接器上 |

## **第3步 - 安装金属后面板**

参考  [金属后面板](p1s-rear-panel.md) 的相关指引，安装金属后面板。

![](https://wiki.bambulab.com/p1/maintenance/p1s-aux-part-cooling-fan/rear_panel_installed.jpg)

# 功能确认

连接电源线并开启电源，在屏幕上点击辅助部件冷却风扇图标，开启辅助冷却风扇 。

![](https://wiki.bambulab.com/p1/maintenance/p1s-aux-part-cooling-fan/on.jpg)

如果辅助部件冷却风扇按预期工作，那么更换完成。否则，请返回检查步骤和连接后重试。如果问题仍然存在，请联系Bambu Lab服务团队寻求进一步帮助。

# 设备校准

更换辅助部件冷却风扇不需要进行额外的校准操作。

# 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
