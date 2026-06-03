---
path: zh/x1/maintenance/Replacing-the-heat-bed-cable
title: "更换热床信号线"
description: "介绍如何更换热床到MC板的信号线（旧版）"
tags: []
created: 2022-10-28T09:05:32.255Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/maintenance/Replacing-the-heat-bed-cable
---

## 什么是热床信号线

热床信号线是一根连接热床和 MC 板的 6pin 电缆。

[点击此处](../../p1/maintenance/heat-bed-signal-cable-p1p.md)查看 P1 系列的更换指南。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-heat-bed-cable/6_pin_cable.jpg)

## 何时更换

1. 热床温度异常， 且已排查过，确认连接器无异常；

2. 热床移动或打印过程中，出现热床温度丢失；

3. 线材本身有明确的损伤或连接器损坏；

4. 经过售后人员的确认，需要更换热床信号线。

## 所需的工具和材料

- 热床信号线（6pin）
- H1.5/H2.0 内六角扳手
- 镊子
- 电吹风
- Z 轴滑块固定螺丝 3 颗(如果开箱后有保留的话)
- 一些必要的胶布和胶水

![](https://wiki.bambulab.com/x1/maintenance/replace-the-chamber-led/silicone_glue.jpg)

硅胶胶水，仅供参考

## 开始操作前的安全警告和机器状态

在进行拆装作业时，请确保打印机没有连接电源。

## 操作指南

### 步骤 1 - 从打印机上拆下热床组件

参考 [更换热床](Replacing-the-heat-bed.md) 中步骤 1~12 的内容，对打印机进行拆解，将热床组件从打印机上取下。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-heat-bed-cable/heat_bed.jpg)

### 步骤 2 - 移除调平螺母

用 H2.0 内六角扳手移除地线固定螺丝和垫圈，然后用手拧下 3 颗热床调平螺母（带橡胶圈）。

|  |  |
| --- | --- |
|  |  |

### 步骤 3 - 移除热床支架

翻转打开热床支架，因为 NTC 线还保持连接状态，注意不要损坏 NTC 线。

|  |  |
| --- | --- |
|  |  |

### 步骤 4 - 移除旧的信号线

用电吹风加热信号线上的白色硅胶，使硅胶软化， 然后用镊子剔除部分硅胶后，断开信号线连接，移除热床信号线。

|  |  |
| --- | --- |
|  |  |

### 步骤 5 - 安装新的信号线

将新的热床信号线穿过热床支架上的过线孔，连接到板件的连接器上，点上硅胶加固连接器和固定信号线，等待约 30 分钟（待胶水固化）。

|  |  |
| --- | --- |
|  |  |

### 步骤 6 - 安装热床支架

将热床支架装回到热床上，对齐螺柱和通孔。

|  |  |
| --- | --- |
|  |  |

### 步骤 7 - 安装调平螺母

安装上 3 个调平螺母（带橡胶圈），螺柱刚好与螺母平齐即可，用螺丝固定地线。

|  |  |
| --- | --- |
|  |  |

### 步骤 8 - 安装热床并装好打印机

参考 [更换热床](Replacing-the-heat-bed.md) 中步骤 13~25 的内容，安装好热床，并组装好打印机。由于产品结构优化，热床信号线的走线方式有变化 ，参考下图。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

1. 连接电源线并打开电源;

2. 参考[热床手动调平](../manual/manual-bed-leveling.md)的内容完成热床的手动调平；

3. 进入 LCD 屏幕上的设置菜单，选择校准选项卡，然后按“开始校准”。

![calibration.png](https://wiki.bambulab.com/screen-operation/calibration.png)

如果一切正常，并且在校准过程中没有出现错误或警告，则更换成功。否则，请检查连接并重试。如果问题仍然存在，请联系服务团队寻求进一步帮助。
