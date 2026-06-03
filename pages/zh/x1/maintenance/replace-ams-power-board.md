---
path: zh/x1/maintenance/replace-ams-power-board
title: "更换AMS电源板"
description: ""
tags: []
created: 2022-08-05T03:13:50.597Z
updated: 2026-03-02T09:36:34.101Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-ams-power-board
---

## AMS电源板

AMS电源板一块安装在AMS后部的电路板，它负责接收从打印机输出过来的直流电源，并将电源传输到AMS主板，同时也担负一定的通信转接功能。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-power-board/ams_power_board.jpg)

购买链接：  
[京东](https://item.jd.com/10088508873275.html)

## 何时更换

1. AMS接口板的电源输出正常，bambu总线电缆4pin/6pin的连接也正常，但AMS却不能正常启动。

2. AMS电源板有明显烧坏的现象。

3. AMS电源板上的连接器或元器件损坏。

## 所需的工具和材料

- 一块新的AMS电源板
- H2.0 和 H1.5 内六角扳手

## 开始操作前的安全警告和机器状态

在开始操作之前，请确认AMS已经从打印上断开连接。

## 操作指南

### 步骤1 - (拆卸)拆除PTFE管

打开AMS上盖，按压AMS 五通组件上的按钮（解锁快速接头），然后从AMS背面拉出PTFE管。

|  |  |
| --- | --- |
|  |  |

### 步骤2 - 松开AMS中框

如下图所示，移除固定AMS中框上2颗螺丝，然后向上转动翻起中框。您可能需要按压五通组件上的按钮来将中框后部完全翻转起来，但注意不要将中框完全取出，因为仍然有电缆连接在上面。

|  |  |
| --- | --- |
|  |  |

### 步骤3 - 移除AMS中框

将Bambu总线电缆和电源电缆从AMS电源板上断开，现在，您可以取出AMS中框了。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-power-board/377px-2_cables_ams_power_board.png)

### 步骤4 - 移除AMS电源板

移除固定AMS电源板的4个螺丝，然后取下电源板。

|  |  |
| --- | --- |
|  |  |

### 步骤5 - (装配)安装AMS电源板

准备一个新的AMS电源板，用4颗螺丝将其固定在AMS外壳的内侧，如下所示。

|  |  |
| --- | --- |
|  |  |

### 步骤6 -安装AMS中框

将AMS中框装入AMS外壳，并将Bambu总线电缆和电源电缆连接到AMS电源板。

|  |  |
| --- | --- |
|  |  |

### 步骤7 - 固定AMS中框

如下图所示，将AMS中框安装到位，用2颗螺丝固定AMS中框。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-power-board/524px-remove_2_screw.png)

### 步骤8 - 连接PTFE管

检查确认PTFE管硅胶支架与五通组件的料孔对齐，并从AMS后部推入PTFE管。装完后，拉动PTFE管，确认PTFE管已固定。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

连接电源线，将AMS连接到打印机，打开电源，通过机器显示屏的操作，开始使用AMS上料，如果能完成上料动作并且整个上料过程没有出现错误提示，则更换成功。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-power-board/494px-load1.png)

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系Bambu Lab服务团队寻求进一步帮助。
