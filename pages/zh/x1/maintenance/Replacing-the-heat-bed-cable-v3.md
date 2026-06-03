---
path: zh/x1/maintenance/Replacing-the-heat-bed-cable-v3
title: "更换热床信号线（新版）"
description: "X系列新版热床线更换指引，热床线是一样的，只是热床直线不一样了，拆装方式有变更。"
tags: []
created: 2023-03-22T14:36:42.212Z
updated: 2026-03-30T03:50:00.672Z
source: https://wiki.bambulab.com/zh/x1/maintenance/Replacing-the-heat-bed-cable-v3
---

## 什么是热床信号线

热床信号线是一根连接热床和 MC 板的 6pin 电缆。

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
- Z 轴滑块固定螺丝3颗(如果开箱后有保留的话)
- 一些必要的胶布和胶水

![](https://wiki.bambulab.com/x1/maintenance/replace-the-chamber-led/silicone_glue.jpg)

硅胶胶水，仅供参考

## 开始操作前的安全警告和机器状态

在进行拆装作业时，请确保打印机没有连接电源。

## 操作指南

### 步骤 1 - 调整热床位置

在开机状态下，通过显示屏幕控制热床运动，将热床置于约全程 ⅔ 的高度。然后关闭打印机，断开电源线，移除玻璃上盖。也可以在关机状态下，侧放打印机，然后拉动Z轴皮带，将热床上升至约全程 ⅔ 的高度。

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/raise_up_the_heat_bed.jpg)

### 步骤 2 - 拆除后面板螺丝

注意：这个过程涉及到很多螺丝，请将它们区分开来，并把它们放在不同的区域，以免弄混。

如图所示，移除后面板上的 10 颗螺丝和 4 颗螺丝。这是两种不同类型的螺丝，要把它们分开，避免混淆。

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/rear_panel_screws.jpg)

### 步骤3 - 拆除后面板

拆除后面板时，需先将后面板从右侧（面向后盖）皮带张紧口的位置松开，再松开左侧（面向后盖）皮带张紧口的位置，以免卡住。

|  |  |
| --- | --- |
|  |  |

### 步骤 4 - 移除废料滑梯

如下图所示，用 H2.0 内六角扳手拆除 1 颗银色螺丝，用 H1.5 内六角扳手拆除两颗黑色螺丝，取下废料滑梯。

|  |  |
| --- | --- |
|  |  |

### 步骤 5 **-** 移除走线槽

用 H2.0 内六角扳手移除2颗螺丝，取下走线槽。

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/holder_screws.jpg)

### 步骤 6 **-** 断开热床信号线

建议先去除部份涂布在接口处的硅胶（用镊子或电吹风加热，不要用热风枪），然后再断开热床信号线的连接。如果MC-AC的连接线有被硅胶粘在一起，可以一起断开连接。

|  |  |
| --- | --- |
|  |  |

### 步骤 7 **- 松**扎网，抽出信号线

撕开扎网两端的胶布，将信号线从扎网中松脱出来。

|  |  |
| --- | --- |
|  |  |

### 步骤 8 **-** 移除走线压片

用 H1.5 内六角扳手拧下 2 颗螺丝，移除走线压片。

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/plate_screws.jpg)

### 步骤 9 **- 取下热床**

用 H2.0 内六角扳手，移除 6 颗固定热床的螺丝。翻转热床，将连接热床的电缆往热床端方向拉出一段，然后热床正面朝下放置在打印机底部表面上。

|  |  |
| --- | --- |
|  |  |

### 步骤 10 **-** 拆除调平螺母

拆除 3 颗调平螺母和垫圈，移除地线固定螺丝。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed-signal-cable/3_nuts.jpg)

### 步骤 11 **-** 打开热床支架

从左向右翻转打开热床支架，注意有一条 2PIN 电线连接，不要损坏。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed-signal-cable/open_the_heat_bed.jpg)

### 步骤 12 **-** 移除热床信号线

清理热床信号线连接器处的硅胶，断开连接，然后再将热床信号线移除。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed-signal-cable/disconnect_cable_1.jpg)

### 步骤 13 **-** 连接热床信号线

将热床信号线穿过热床支架上的过线孔，连接到板件的接口上，点上硅胶对连接器进行加固。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed-signal-cable/connect_the_signal_cable_2.jpg)

### 步骤 14 **-** 安装热床支架

合上热床支架，调整好位置。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed-signal-cable/place_back_the_bracket.jpg)

### 步骤 15 **-** 安装调平螺母

按压热床支架，依次拧上 3 颗调平螺母，通过肉眼观察，尽量将 3 颗螺母的拧入量接近一致，锁好地线。

|  |  |
| --- | --- |
|  |  |

### 步骤 16 **-** 安装热床

将热床安装到滑块上，将热床尽量靠前门方向放置，锁入 6 颗螺丝进行固定。

|  |  |
| --- | --- |
|  |  |

### 步骤 17 **-** 穿热床线，安装走线压片

侧放打印机，将热床信号线穿过后滑块过线孔，整理好滑块线槽内的电缆，装上走线压片并锁入 2 颗螺丝进行固定。

|  |  |
| --- | --- |
|  |  |

### 步骤 18 **-** 固定扎网

正放打印机，将热床信号线穿过扎网，然后在扎网两端缠上胶布固定扎网。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed-signal-cable/pass_through_the_net.jpg)

### 步骤 19 **-** 连接热床信号线

将热床信号线连接到 MC 板对应接口上，连接 MC-AC 连接线，在连接器处点上硅胶进行加固。

|  |  |
| --- | --- |
|  |  |

### 步骤 20 - 安装走线槽

安装走线槽，锁入 2 颗螺丝进行固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/holder_screws.jpg)

### 步骤 21- 安装废料滑梯

安装废料滑梯，注意滑梯两侧需要安装到位，右侧确认没有压到电缆，在滑梯方锁入 2 颗黑色螺丝，在左侧锁入 1 颗银色螺丝。

|  |  |
| --- | --- |
|  |  |

### 步骤 22 - 安装后面板

安装后面板时，应首先穿过 PTFE 管支架和装好右侧的皮带张紧口位置。

|  |  |
| --- | --- |
|  |  |

### 步骤 23 -锁紧螺丝

用螺丝将后盖重新固定。注意使用的不同类型的螺丝(如下图所示的 10 颗螺丝和 4 颗螺丝)。

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/rear_panel_screws.jpg)

## 如何验证完成/成功

连接电源线并打开电源。

确保腔室和热床上没有任何打印物品或挤出材料。然后进入 LCD 屏幕上的设置菜单，选择校准选项卡，然后按“开始校准”。

![calibration.png](https://wiki.bambulab.com/screen-operation/calibration.png)

如果一切正常，并且在校准过程中没有出现错误或警告，则更换成功。否则，请检查连接并重试。如果问题仍然存在，请联系服务团队寻求进一步帮助。
