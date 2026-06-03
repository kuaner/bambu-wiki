---
path: zh/p1/maintenance/heat-bed
title: "热床拆装指引"
description: "拆装 P1 打印机热床的操作步骤"
tags: ["热床", "p1"]
created: 2022-12-11T15:41:56.410Z
updated: 2026-05-11T02:27:15.165Z
source: https://wiki.bambulab.com/zh/p1/maintenance/heat-bed
---

## 热床

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/heat_bed.jpg)

## 工具

- H2.0/H1.5 内六角扳手
- 镊子

## 准备工作

断开电源连接。

## 拆除

### **第 1 步 -**  拆除背板、废料滑梯、护线盖

参考 [更换 P1S 金属背板](p1s-rear-panel.md)、[更换 P1P 金属背板](rear-panel.md) 、 [废料滑梯](excess-chute.md) 和 [护线盖](power-board-protective-cover.md) 相关内容，移除背板、废料滑梯和护线盖。

> P1S 产品还需参考[P1系列塑胶右侧板](p1s-right-panel.md) 额外移除右侧板。

![](https://wiki.bambulab.com/p1/maintenance/p1s-rear-panel/rear_panel_-_p1p.png)

### **第 2 步 -** 断开热床电源线

移除保护胶套，用镊子解除锁扣，拔出两根电源线。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 -** 断开热床传感器线缆

先断开 MC-AC 连接线，然后清除热床传感器线缆上的硅胶，再断开热床传感器线缆的连接。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/disconnect_2_cables.jpg)

### **第 4 步 -** 拆除地线螺丝

用手按住螺母，然后用 H2.0 内六角扳手拧下接地螺丝，松开地线。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/heat_bed_ground_cable.jpg)

### **第 5 步 -** 松脱电缆

将热床线缆从线扣和过线孔中松出。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/release_the_cables.jpg)

### **第 6 步 -** 移除扎网

撕开扎网两端的胶布，移除扎网。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/remove_the_net.jpg)

### **第 7 步 -** 上升热床

侧放打印机，通过拉动 Z 轴皮带将热床上升至全程 2/3 以上的位置。

|  |  |
| --- | --- |
|  |  |

### **第 8 步 -** 移除走线压片

拧下 2 颗螺丝，移除走线压片。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/remove_the_hold_plate.jpg)

### **第 9 步 -** 解锁热床

重新正放打印机，移除6颗固定热床的螺丝。

请注意，有些螺丝上可能有黑色贴纸。您可以安全地撕掉贴纸，然后继续拆卸。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/6_screws.jpg)

### **第 10 步 -** 移除热床

侧放热床，回退热床线缆，移除热床。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/pull_out_the_cables.jpg)

## 安装

### **第 1 步 -** 安装热床

将热床安装到滑块上，将热床尽量靠前放置，锁入 6 颗螺丝进行固定。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/install_the_heat_bed.jpg)

### **第 2 步 -** 穿热床线，安装走线压片

将打印机侧放，热床线缆穿过后滑块过线孔，将电缆整理好压入后滑块线槽，然后装上走线压片，拧紧螺丝固定。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/install_the_plate.jpg)

### **第 3 步 -** 安装扎网

将扎网安装到电缆上，两端用胶带固定。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/remove_the_net.jpg)

### **第 4 步 -** 理线

穿地线，并将电源线和通信线装到线扣上。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/release_the_cables.jpg)

### **第 5 步 -** 锁地线

用螺丝和螺母将地线锁定到立柱上。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/heat_bed_ground_cable.jpg)

### **第 6 步 -** 接电源线

确认电源线插头的状态，将两个插头连接到 AC 板接口上。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/connect_heat_bed_power_cable.jpg)

### **第 7 步 -** 连接热床传感器线缆

将热床传感器线缆连接到 MC 板对应接口上，在连接器处点上硅胶进行加固，连接 MC-AC 连接线。

|  |  |
| --- | --- |
|  |  |

### **第 8 步 -** 安装护线盖、废料滑梯和背板

参考 [护线盖](power-board-protective-cover.md) 、[废料滑梯](excess-chute.md) 、[更换 P1P 金属背板](rear-panel.md) 、[更换 P1S 塑胶右侧板](p1s-right-panel.md) 和 [更换 P1S 金属背板](p1s-rear-panel.md)相关内容，安装护线盖、废料滑梯和背板。

![](https://wiki.bambulab.com/p1/maintenance/excess-chute/rear_panel_installed.jpg)

## 如何验证完成

启动打印机，运行设备校准流程，如果校准过程顺利通过，说明操作成功。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/calibration2.jpg)
