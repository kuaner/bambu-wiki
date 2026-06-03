---
path: zh/x1/maintenance/replace-power-module
title: "更换电源模块"
description: "本指南介绍更换 X1 系列打印机电源模块的详细步骤"
tags: ["x1", "电源模块"]
created: 2022-08-04T12:57:23.211Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-power-module
---

## 什么是电源模块

X1 系列 3D 打印机的电源模块是一个输入电压为 AC 100-240V，输出电压为 DC 24V 的电源转换器，它为除加热床以外的整个打印机供电。

![](https://wiki.bambulab.com/x1/maintenance/replace-power-module/350px-power_module.png)

## 何时更换

当您确定电源模块的输出电压不正常，或者电源模块板上的元器件有明显的烧坏现象时，可能需要更电源模块。

## 需要的工具和材料

- 一个新的电源模块
- H1.5 和 H2.0 内六角扳手
- 十字螺丝刀

## 开始操作前的安全警告和机器状态

关闭电源，从电源插座上拔下电源线。

## 拆卸指南

### 步骤 1 - 断开电源线

从电源插座上拔下电源线。

![](https://wiki.bambulab.com/x1/maintenance/replace-power-module/377px-disconnect_the_power.png)

### 步骤 2 - 拆除螺丝

注意：这个过程涉及到很多螺丝，请将它们区分开来，并把它们放在不同的区域，以免弄混。

如图所示，取下后盖上的 10 颗螺丝和 4 颗螺丝。这是两种类型的螺丝，所以要把它们分开。

|  |  |
| --- | --- |
|  |  |

### 步骤 3 - 拆除后盖

拆下后盖，先将后盖从左侧（面向后盖）皮带张紧口的位置松开，再松开右侧（面向后盖）皮带张紧口的位置，以免卡住。

|  |  |
| --- | --- |
|  |  |

### 步骤 4 - 移除废料滑梯

拧下 2 颗螺丝，并拆下废料滑梯。

|  |  |
| --- | --- |
|  |  |

> *注意：在新版本机器中，滑梯左侧追加了 1 颗螺丝，可以用 H2.0 扳手拧下。*
>
> ![](https://wiki.bambulab.com/p1/maintenance/excess-chute/new_screw.png)

### 步骤 5 - 移除保护盖

拆下 6 颗螺丝，将电源模块保护盖移到一边，并断开热床的电源线。

|  |  |
| --- | --- |
|  |  |

### 步骤 6 - 断开电缆

打开接口盖，拧松 3 颗螺丝，断开 3 根电缆，然后断开 MC 板的电源连接线。

![](https://wiki.bambulab.com/x1/maintenance/replace-power-module/382px-3_screw_and_cable.png)

### 步骤 7 - 拆除电源模块

拧下2颗螺丝，拆下电源模块。

|  |  |
| --- | --- |
|  |  |

### 步骤 8 - 断开 MC 板电源电缆

拧松图示的 2 颗螺丝，拆下 MC 板电源线。

|  |  |
| --- | --- |
|  |  |

### 步骤 9 - 连接 MC 板电源线

将 MC 板电源线连接到电源板模块，锁紧 2 个螺丝(另外 1 颗地线螺丝不要锁紧)。

![](https://wiki.bambulab.com/x1/maintenance/replace-power-module/452px-connect_cable_power_board_1.png)

## 安装指南

### 步骤 1 - 安装电源板

将电源模块安装到内衬上，锁紧 2 个螺钉(其中 1 颗螺丝要穿上地线)。

|  |  |
| --- | --- |
|  |  |

### 步骤 2 - 连接电缆

连接 3 根电缆，合上接口盖，并将 MC 板电源线接到 MC 板的电源接口上，连接热床的电源线。

|  |  |
| --- | --- |
|  |  |

### 步骤 3 - 安装保护盖

安装电源模块保护盖，并锁紧 6 颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-power-module/318px-6_screws.png)

### 步骤 4 - 安装废料滑梯

安装废料滑梯，注意两边的卡扣，锁紧 2 颗螺丝。

|  |  |
| --- | --- |
|  |  |

> *注意：如果在拆解时发现滑梯侧面有螺丝，可以锁回去。*
>
> ![](https://wiki.bambulab.com/p1/maintenance/excess-chute/new_screw.png)

### 步骤 5 - 安装后盖

安装后盖时，应首先穿过 PTFE 管支架和装好右侧的皮带张紧口位置。

|  |  |
| --- | --- |
|  |  |

### 步骤 6 - 锁紧螺丝

将后盖重新固定。注意使用的不同类型的螺丝(如下图所示的 10 颗螺丝和 4 颗螺丝)。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

连接电源线并打开电源。在 LCD 屏幕上点击运行设备自检。如果自检完成后没有错误提示，则替换完成并成功。

![](https://wiki.bambulab.com/screen-operation/selftest.png)

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步的帮助。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
