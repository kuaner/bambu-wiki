---
path: zh/x1/maintenance/replace-gear-unit-in-filaments-hub
title: "更换AMS五通挤出轮"
description: ""
tags: []
created: 2022-08-01T02:38:00.261Z
updated: 2024-05-28T10:28:54.899Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-gear-unit-in-filaments-hub
---

## 什么是AMS五通挤出轮

AMS五通挤出轮是一组安装在 AMS 五通组件内的一组主动驱动齿轮单元，它在马达的带动下，参与打印丝的输送和回退。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/388px-gear_unit.png)

## 何时使用

当打印丝卡住，且打印丝停在AMS五通组件或在五通内的打印丝有明显磨损或发现打印丝有缺口时。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/312px-notch.png)

## 所需工具和材料

- 新的AMS五通挤出轮
- H2.0 & H1.5 内六角扳手

## 开始运行前的安全警告和机器状态

关闭打印机电源并断开AMS与打印机的连接。

## 操作指南

### 步骤 1 - (拆卸) 拆除PTFE管

打开AMS上盖，按压AMS 五通组件上的按钮（解锁快速接头），然后从AMS背面拉出PTFE管。

|  |  |
| --- | --- |
|  |  |

### 第 2 步 - 移除螺丝

移除固定AMS主框架上2颗螺丝。

|  |  |
| --- | --- |
|  |  |

### 第 3 步 - 移除AMS主框架组件

向上翻转中间框架组件，断开bambu总线电缆和电源电缆，移除AMS主框架组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/377px-2_cable_ams_power_board.png)

### 第 4 步 - 断开 4 条PTFE 管

依次按下快速接头上的按钮，解锁连接并断开 4 条PTFE 管。

|  |  |
| --- | --- |
|  |  |

### 第 5 步 - 移除 4 颗螺丝

移除 4 颗螺丝，然后将AMS五通组件翻转过来。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/318px-4_screws_v2.png)

### 第 6 步 - 移除五通组件驱动齿轮

移除 4 颗螺丝，然后取下保护盖和AMS五通挤出轮。

|  |  |
| --- | --- |
|  |  |

### 第 7 步 - （组装）安装AMS五通挤出轮

 将新的AMS五通挤出轮和保护盖安装到AMS五通组件上，并用 4 颗螺丝固定保护盖。

|  |  |
| --- | --- |
|  |  |

### 第 8 步 - 安装AMS五通组件

将AMS五通组件安装到中框，并锁入 4 颗螺丝进行固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/318px-4_screws_v2.png)

### 第 9 步 - 连接 4 根 PTFE 管

理好电缆走线，并依次连接 4 根 PTFE 管到五通组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/376px-tubes.png)

### 第 10 步 - 安装AMS主框架组件

将AMS主框架组件装入AMS外壳，并将Bambu总线电缆和电源电缆连接到AMS电源板。

|  |  |
| --- | --- |
|  |  |

### 第 11 步 - 固定AMS主框架组件

如下图所示，将AMS主框架安装到位，用2颗螺丝固定AMS主框架组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/524px-remove_2_screw.png)

### 第 12 步 - 连接PTFE管

检查确认PTFE管硅胶支架与五通组件的料孔对齐，并从AMS后部推入PTFE管。装完后，拉动PTFE管，确认PTFE管已固定。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

将 AMS 连接到打印机并打开电源。将打印材料加载到 AMS 的所有料槽中，然后单击屏幕上的“进料”开始加载打印丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-gear-unit-in-filaments-hub/494px-load1.png)

如果打印丝加载过程表现正常，则更换完成并成功。

否则，请检查电缆和PTFE管的连接后重试。如果未发现异常但仍出现故障，请联系 Bambu Lab 服务团队以获得进一步帮助。
