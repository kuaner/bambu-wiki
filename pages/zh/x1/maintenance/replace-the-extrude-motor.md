---
path: zh/x1/maintenance/replace-the-extrude-motor
title: "更换挤出电机及 Logo LED 灯连接线"
description: "本指南详细介绍了如何卸下和安装挤出电机、 Logo LED 灯连接线"
tags: []
created: 2022-10-25T02:38:14.647Z
updated: 2026-08-20T06:56:01.840Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-the-extrude-motor
---

## 挤出电机

挤出电机是安装在工具头上，用于驱动挤出机进行动作的电机，它是一款 36 系列圆形步进电机。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/extrude_motor.jpg)

> 注意：本篇适用于 X1 系列打印机，如果您需要更换 P1 系列打印机的挤出电机，请参考 Wiki ：[更换 P1 系列挤出电机](../../p1/maintenance/replace-extruder-motor.md)

## 何时更换

- 挤出电机烧坏，无法运转
- 售后人员通过日志分析，确认是挤出电机故障

## 所需工具

1. 新的挤出电机
2. H2.0/H1.5 内六角扳手
3. 硅胶胶水

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/silicone_glue.jpg)

硅胶胶水仅供参考

## 安全警告

关闭电源，移除电源线。

## 操作指南

### 步骤 1 - 移除工具头 TH 板组件

参考 [更换工具头主板组件](replace-the-th-board-assembly.md) 的视频内容，移除 TH 板组件。

|  |  |
| --- | --- |
|  |  |

### 步骤 2 **- 移除 Logo LED 灯连接线**

移除工具头 Logo LED 灯连接线。

|  |  |
| --- | --- |
|  |  |

### 步骤 3 - 移除激光雷达组件

用 H1.5 内六角扳手，移除 2 颗螺丝，取下激光雷达组件。

|  |  |
| --- | --- |
|  |  |

### 步骤 4 - 拆除固定螺丝

用 H2.0 内六角扳手，依次移除 8 颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/remove_8_screws.jpg)

### 步骤 5 - 移除工具头滑车前盖（含挤出机）

将工具头的滑车前盖组件（含挤出机）移除。

|  |  |
| --- | --- |
|  |  |

> 注意：在上部铜套位置，工具头滑车后盖装有 4 根弹簧，要防止脱落丢失

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/springs_inside.jpg)

### 步骤 6 - 移除挤出机

用 H2.0 内六角扳手，移除 3 颗螺丝，取下挤出机和热端。

|  |  |
| --- | --- |
|  |  |

### 步骤 7 - 移除挤出电机

用 H2.0 内六角扳手，移除 2 颗螺丝，取下挤出电机。

|  |  |
| --- | --- |
|  |  |

### 步骤 8 **- 安装挤出电机**

将新的挤出电机安装到滑车前盖上，注意电缆在上方，然后锁入 2 颗螺丝固定电机。

|  |  |
| --- | --- |
|  |  |

### 步骤 9 - 安装挤出机

将挤出机和热端一起安装到滑车前盖上，锁入 3 颗螺丝进行固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/install_the_extruder.jpg)

### 步骤 10 **- 安装滑车前盖组件**

安装前，先确认弹簧在位，上下铜套在滑车后盖对应的槽内，然后将装有挤出电机的滑车前盖装上，注意不要压到电机电缆。

|  |  |
| --- | --- |
|  |  |

### 步骤 11- 锁螺丝（4+4）

锁螺丝固定滑车前盖，请按下图所示，按 1~8 的顺序依次锁紧螺丝。

|  |  |
| --- | --- |
|  |  |

### 步骤 12 - 安装激光雷达组件

将激光雷达组件安装到工具头下方，锁入 2 颗螺丝固定。

|  |  |
| --- | --- |
|  |  |

### 步骤 13 - 安装 Logo LED 灯连接线

安装 Logo LED 灯连接线。

|  |  |
| --- | --- |
|  |  |

### 步骤 14 - 安装 TH 板，完成工具头的组装

参考 [更换工具头主板组件](replace-the-th-board-assembly.md) 的视频内容，安装好 TH 板组件和工具头。

## 验证完成/成功

- 连接电源，启动打印机；
- 在控制页面，点击挤出机挤出按钮，确认电机能正常驱动挤出机；

![点击挤出按钮.png](https://wiki.bambulab.com/%E7%82%B9%E5%87%BB%E6%8C%A4%E5%87%BA%E6%8C%89%E9%92%AE.png)

- 点击“设置→工具箱→设备自检”，运行设备自检流程，确认没有出现工具头关联部件的报错信息。

![selftest.png](https://wiki.bambulab.com/screen-operation/selftest.png)

如果有异常，请按照操作步骤排查组装是否有问题，排除后，再次运行设备自检。如果问题仍然存在，请联系技术服务团队寻求进一步的帮助。
