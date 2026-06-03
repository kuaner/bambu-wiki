---
path: zh/x1/maintenance/replace-ams-main-board
title: "更换AMS主板"
description: "本文介绍了如何更换 AMS 主板"
tags: []
created: 2022-08-05T03:22:06.510Z
updated: 2026-03-09T03:39:15.948Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-ams-main-board
---

## 什么是AMS主板

AMS主板是AMS的核心电路板，它提供了一系列连接器，通过这些连接器和连接电缆将种功能组件连接起来。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/ams_main_board.png)

## 何时更换

当出现AMS主板板件电压异常、元器件异常发热或烧坏、模块间的通信异常、连接器损坏、不可恢复的固件升级失败等故障发生时，可能需要更换AMS主板。

## 所需的工具和材料

H2.0 和 H1.5  内六角扳手

## 开始操作前的安全警告和机器状态

在开始操作之前，请确认AMS已经从打印上断开连接。

## 操作指南

### 步骤1 - (拆卸)拆除PTFE管

打开AMS上盖，按压AMS 五通组件上的按钮（解锁快速接头），然后从AMS背面拉出PTFE管。

|  |  |
| --- | --- |
|  |  |

### 步骤2 - 移除螺丝

移除固定AMS主框架上2颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/611px-remove_2_screw.png)

### 步骤3 - 移除AMS主框架组件

向上翻转中间框架组件，断开bambu总线电缆和电源电缆，移除AMS主框架组件。

|  |  |
| --- | --- |
|  |  |

### 步骤4 - 断开11根电缆

从主板上的连接器上拔下所有电缆。建议在电缆上做一些标记或者拍下连接状态的照片，避免后面重新接线时出错。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/disconnect_11_cables.png)

### 步骤5 - 移除AMS主板

移除2颗螺丝，将主板从4个卡扣中解锁，然后取下AMS主板。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/install_the_ams_main_board.png)

### 步骤6 - (装配)安装主板

将主板安装到AMS主框架上，先确认主板安装在被4个卡扣扣住的状态，然后锁紧2颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/install_ams_main_board.png)

### 步骤7 - 连接11根电缆

根据断开前的标记或照片，连接好11根电缆。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/connect_11_cables.png)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 序号 | 连接对象 | 序号 | 连接对象 | 序号 | 连接对象 |
| 1 | 上下料器 1 | 5 | 五通组件（霍尔线） | 9 | 上下料器 3 |
| 2 | RFID板 1 | 6 | AMS电源板（电源线） | 10 | RFID板 2 |
| 3 | 上下料器 2 | 7 | AMS电源板（bambu总线） | 11 | 上下料器 4 |
| 4 | 里程轮 | 8 | 五通组件（电机线） |  |  |

### 步骤8 - 安装AMS主框架组件

将AMS主框架组件装入AMS外壳，并将Bambu总线电缆和电源电缆连接到AMS电源板。

|  |  |
| --- | --- |
|  |  |

### 步骤9 - 固定AMS主框架组件

如下图所示，将AMS主框架安装到位，用2颗螺丝固定AMS主框架组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-first-stage-feeder/524px-remove_2_screw.png)

### 步骤10 - 连接PTFE管

检查确认PTFE管硅胶支架与五通组件的料孔对齐，并从AMS后部推入PTFE管。装完后，拉动PTFE管，确认PTFE管已固定。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

1.将AMS连接到打印机并开启电源，确认AMS菜单已打开。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/ams_connected.png)

2.检查序列号和固件，固件和序列号应在输入后显示，如果提示发现新固件，请更新固件。

|  |  |
| --- | --- |
|  |  |

3.将耗材装入4个料槽，并通过上料和退料依次确认每个槽都能工作正常。如果你装载的是Bambu Lab官方耗材，耗材还将会被自动识别。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/filaments_info.png)

如果您的AMS表现不是如此，请检查连接线后重试。如果仍然出现故障，请联系Bambu Lab服务团队寻求进一步帮助。
