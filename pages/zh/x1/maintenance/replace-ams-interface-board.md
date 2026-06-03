---
path: zh/x1/maintenance/replace-ams-interface-board
title: "更换AMS接口板"
description: ""
tags: []
created: 2022-08-05T02:30:30.364Z
updated: 2026-02-05T03:19:29.040Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-ams-interface-board
---

## 什么是 AMS 接口板

AMS 接口板是安装在打印机后横梁上的一块电路板，它为 AMS 提供 24 V 的直流电源，并处理 AMS 和打印机之间的通信连接。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-interface-board/397px-ams_interface_board.png)

## 何时更换

AMS 接口板的电源输出不正常，AMS 出现电源或通信故障的，有很大可能需要更换 AMS 接口板。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-interface-board/290px-24v.png)

## 所需的工具和材料

- 一块新的 AMS 接口板
- H2.0 内六角扳手.

## 开始操作前的安全警告和机器状态

在开始本指南中的过程之前，请确保机器已关闭。需要断开与 AMS 的电缆连接，并移除供料缓冲器。

## 操作指南

### 步骤1 - (拆卸)断开电源线

关闭电源，从电源插座上拔下电源线。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-interface-board/377px-disconnect_the_power.png)

### 步骤2 - 断开 PTFE 管

按下快速接头，断开 PTFE 管。拔下4针连接电缆，断开 AMS 与打印机的连接。

|  |  |
| --- | --- |
|  |  |

### 步骤3 - 移除 AMS 供料缓冲器

拆下固定供料缓冲器的 2 颗螺丝（M3×23），移除供料缓冲器。

|  |  |
| --- | --- |
|  |  |

### 步骤4 - 拆除螺丝

注意：这个过程涉及到很多螺丝，请将它们区分开来，并把它们放在不同的区域，以免弄混。

如图所示，取下后盖上的 10 颗螺丝（M3×4.5）和 4 颗螺丝（BT3×5）。这是两种类型的螺丝，所以要把它们分开。

|  |  |
| --- | --- |
|  |  |

### 步骤5 -拆除后盖

拆下后盖，先将后盖从左侧（面向后盖）皮带张紧口的位置松开，再松开右侧（面向后盖）皮带张紧口的位置，以免卡住。

|  |  |
| --- | --- |
|  |  |

### 步骤6 -移除废料滑梯

拧下 2 颗螺丝（BT2×8），并拆下废料滑梯。

|  |  |
| --- | --- |
|  |  |

### 步骤7 -断开电缆连接

从位于打印机背面右上方的 AMS 接口板上拔下连接电缆。

|  |  |
| --- | --- |
|  |  |

### 步骤8 -移除AMS接口板

拧下固定AMS接口电路板的 2 颗螺丝（ST3×4.5），移除AMS接口板。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-interface-board/350px-connector_ams-mc.png)

### 步骤9 -(装配)安装接口电路板

我们将目前为止所采取的步骤倒过来，就可以完成AMS 接口板的安装 了。首先，安装新的AMS接口板，并用2颗螺丝（ST3×4.5）将其固定到位。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### 步骤10 -连接电缆

重新将连接电缆接到AMS接口板上。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-interface-board/396px-connector_ams-mc.png)

### 步骤11 -安装废料滑梯

将废料滑梯装回原位，安装时注意滑槽两侧突出的止扣，锁紧2颗螺丝（BT3×8）。

|  |  |
| --- | --- |
|  |  |

### 步骤12 -安装后盖

安装后盖时，应首先穿过PTFE管支架和装好右侧的皮带张紧口位置。

|  |  |
| --- | --- |
|  |  |

### 步骤13 -锁紧螺丝

用螺丝将后盖重新固定。注意使用的不同类型的螺丝(如下图所示的10颗螺丝（M3×4.5）和4颗螺丝（BT3×5）)。

|  |  |
| --- | --- |
|  |  |

### 步骤14 -安装 AMS 供料缓冲器

将 AMS 供料缓冲器装回原位，拧入 2 颗螺丝（M3×23）固定。

|  |  |
| --- | --- |
|  |  |

### 步骤15 -连接 PTFE 管和电缆

只需将带连接器的 PTFE 管推向机器后部的 PTFE 管，即可快速连接 PTFE 管，连接 4 针 Bambu 总线电缆。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

连接电源线并启动电源。在显示屏上，按下屏幕上的AMS标签，如下所示，屏幕将显示AMS控制面板。按下“上料”按钮开始上料，如果该过程没有任何错误地完成，AMS接口板更换完成并成功。

|  |  |
| --- | --- |
|  |  |

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系Bambu Lab服务团队寻求进一步帮助。
