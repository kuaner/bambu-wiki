---
path: zh/p2s/maintenance/replace-toolhead-carriage
title: "更换 P2S 工具头滑车"
description: "更换 P2S 打印机工具头滑车的操作流程"
tags: []
created: 2025-12-11T08:15:30.707Z
updated: 2026-01-19T04:20:07.077Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-toolhead-carriage
---

## 工具头滑车

工具头滑车组件主要由滑车前盖和滑车后盖组成，安装在 X 轴组件的石墨铝套上，可以在 XY 皮带的牵引下实现在 X 方向上的移动。

![fac170-1.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac170-1.jpg)

> **注意：** 更换工具头滑车组件时，无需拆卸打印机的外壳。

## 适用场景

- 工具头滑车组件损坏

## 所需工具与材料

- 新的工具头滑车组件
- H1.5 内六角扳手
- H2.0 内六角扳手

## 拆卸工具头滑车组件

### 步骤 1. 移除工具头上的组件

1. 请参考 [更换 P2S 热端加热组件/热端风扇](replace-hotend-heating-assembly-and-cooling-fan.md) 移除工具头外壳、热端、热端加热组件、和热端风扇；
2. 请参考 [更换 P2S 挤出机配件](replace-extruder-components.md)、[更换 P2S 切刀刀柄](replace-filament-cutter-lever.md) 移除挤出机组件和切刀刀柄；
3. 请参考 [更换 P2S 工具头电路板](replace-th-boards-and-fpc-cable.md) 拆除拆卸 TH 板与挤出接口板；
4. 请参考 [更换 P2S 工具头线缆](replace-toolhead-cable.md)、[更换 P2S 拖链](replace-cable-chain.md) 拆除工具头线缆与拖链；
5. 请参考 [更换 P2S 涡流线圈](replace-eddy-sensor.md) 拆卸涡流线圈；
6. 请参考 [更换 P2S 挤出电机](replace-3508-extruder-servo-motor.md) 移除挤出机电机。

### 步骤 2. 取下皮带固定座

使用 H2.0 内六角扳手拧松（拧松 1-2 圈即可，请勿卸下螺丝）四颗张紧螺丝，放松 XY 皮带。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image.png)

使用 H2.0 内六角扳手移除三颗皮带固定座螺丝，将皮带固定座取下。

> **提示：** 下方示例图中 P2S 的后侧板与侧板已拆下，但本教程不需要拆卸这两个面板。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/01_001.png)

在另一侧重复相同步骤，拆下另一侧皮带固定座。

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/02_002.png)

### 步骤 3. 拆卸工具头滑车组件

使用 H2.0 内六角扳手拆下八颗固定滑车组件的螺丝。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/03_003.png)

用手握住工具头滑车前壳和后壳，先轻微向上倾斜前盖，再将滑车取下，防止工具头滑车前壳顶部的四个弹簧掉落。

![](https://wiki.bambulab.com/p2s/maintenance/remove_p2s_x_carriage_and_keep_screws_in_place.png)

## 安装工具头滑车组件

### 步骤 1. 安装工具头滑车组件

安装前，请检查工具头滑车前盖顶部的弹簧是否在位；

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/04_004.png)

检查轴承是否在位；如果不在位，请将旧工具头滑车上面的轴承安装到位；

![image-2.png](https://wiki.bambulab.com/p2s/maintenance/toolhead-front-carriage/image-2.png)

对齐 X 轴导杆上的上下两个铝套；

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/06_006.png)

先将工具头滑车前壳的底部贴住铝套，再慢慢转动工具头滑车前壳直至前壳顶部贴住铝套；

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/07_007.png)

接下来，安装工具头滑车的后盖，使用 H2.0 六角扳手以对角线顺序拧紧 8 颗螺丝。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/03_003.png)

### 步骤 2. 安装皮带固定座

先将右侧的皮带固定座（靠近右侧板）安装至工具头上，使用 H2.0 内六角扳手拧紧三颗固定螺丝；

![20_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/20_020.png)

将工具头推到右后方，然后稳固地安装左侧皮带固定座；

![21_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/21_021.png)

使用 H2.0 内六角扳手拧紧三颗固定螺丝；

![22_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/22_022.png)

手动推动工具头滑车，沿 XY 方向尽可能大范围地前后来回推动 3–5 次，然后使用 H2.0 内六角扳手拧紧打印机背后的四颗张紧螺丝。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image.png)

### 步骤 3. 安装工具头上的组件

1. 请参考 [更换 P2S 挤出电机](replace-3508-extruder-servo-motor.md) 安装挤出机电机；
2. 请参考 [更换 P2S 涡流线圈](replace-eddy-sensor.md) 安装涡流线圈：
3. 请参考 [更换 P2S 工具头电路板](replace-th-boards-and-fpc-cable.md) 安装工具头电路板
4. 请参考 [更换 P2S 工具头线缆](replace-toolhead-cable.md)、[更换 P2S 拖链](replace-cable-chain.md) 安装工具头线缆与拖链
5. 请参考 [更换 P2S 挤出机配件](replace-extruder-components.md)、[更换 P2S 切刀刀柄](replace-filament-cutter-lever.md) 安装挤出机组件和切刀刀柄
6. 请参考 [更换 P2S 热端加热组件/热端风扇](replace-hotend-heating-assembly-and-cooling-fan.md) 安装热端加热组件、热端风扇、工具头外壳和热端

### 步骤 4. 调整涡流线圈

请参考 [P2S 涡流线圈调整](adjust-the-eddy-sensor.md) 调整涡流线圈位置。

## 成功验证

接通电源并启动打印机，运行整机校准流程，确认校准能够顺利完成。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
