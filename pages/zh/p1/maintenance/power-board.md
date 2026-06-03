---
path: zh/p1/maintenance/power-board
title: "电源模块拆装指南"
description: "拆装 P1 系列打印机电源模块的操作步骤"
tags: ["电源模块"]
created: 2022-12-14T16:03:00.776Z
updated: 2025-12-09T02:07:19.383Z
source: https://wiki.bambulab.com/zh/p1/maintenance/power-board
---

## 电源模块

![](https://wiki.bambulab.com/p1/maintenance/power-board/power_board.jpg)

## 工具

- H2.0/H1.5 内六角扳手
- 十字螺丝刀

## 接线方式校准修改

![](https://wiki.bambulab.com/general/tripping-electric-issue/cn-ac-connect-wiring.png)

右边的接线方式漏电流更低，即蓝色线缆连接到第一个座子，棕色线缆连接到第二个座子

本文后续的图片采用了漏电流较高的接线方式，这并不是最优的方式。强烈建议您采用右边那种漏电流较低的接线方式，而不要参考左边的那种方式进行接线。

## 准备工作

断开电源连接。

## 拆除

### **第 1 步 -**  拆除背板、废料滑梯、电源模块保护盖

参考 [护线盖](power-board-protective-cover.md) 的相关内容，移除背板、废料滑梯和电源模块保护盖。

![](https://wiki.bambulab.com/p1/maintenance/power-board/power_cover_removed.jpg)

### **第 2 步 -** 松脱电源线

用十字螺丝刀拧松 3 颗压线螺丝，松出 3 根输入电缆。

![](https://wiki.bambulab.com/p1/maintenance/power-board/disconnect_power_cables.jpg)

### **第 3 步 -** 断开 MC 板电线源

从 MC 板上断开 XT30 电源线连接。

![](https://wiki.bambulab.com/p1/maintenance/power-board/disconect_power_cable_to_mc_board.jpg)

### **第 4 步 -** 移除电源模块

拆下 2 颗螺丝，移除电源模块。

![](https://wiki.bambulab.com/p1/maintenance/power-board/2_screws_for_power_module.jpg)

### **第 5 步 -** 移除 XT30 电源线

拧松 2 颗螺丝，将 XT30 电源线从电源模块上取下。

![](https://wiki.bambulab.com/p1/maintenance/power-board/loose_2_screws.jpg)

## 安装

### **第 1 步 -** 安装 XT30 电源线

将 XT30 电源线按下图所示连接到对应端子上，锁紧 2 颗螺丝（地线螺丝暂时不用锁紧）。

![](https://wiki.bambulab.com/p1/maintenance/power-board/loose_2_screws.jpg)

### **第 2 步 -** 安装电源模块

将电源模块安装到内衬上，锁入 2 颗螺丝进行固定，其中下方的螺丝需要同时锁定地线。

![](https://wiki.bambulab.com/p1/maintenance/power-board/2_screws_for_power_module.jpg)

### **第 3 步 -** 连接 XT30 电源线

将 XT30 电源线沿着线槽布线，然后连接到 MC 板上，确认插到底。

![](https://wiki.bambulab.com/p1/maintenance/power-board/connect_the_power_cable_to_mc.jpg)

### **第 4 步 -** 连接电源线

将 2 根电源线和 1 根据地线插到对应端子上，依次锁紧螺丝，注意不要漏装 XT30 电源线的地线。

![](https://wiki.bambulab.com/p1/maintenance/power-board/connect_power_cables.jpg)

### **第 5 步 -** 组装好打印机

整理好电缆后，参考 [护线盖](power-board-protective-cover.md) 的相关内容，依次装上电源模块保护盖、废料滑梯和背板，将打印机组装好。

![](https://wiki.bambulab.com/p1/maintenance/power-board/rear_panel_installed.jpg)

## 如何验证完成

接上打印机电源，开启打印机，在屏幕上操作，运行设备校准流程，如校准通过，说明操作成功。

![32.校准.jpg](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/32.%E6%A0%A1%E5%87%86.jpg)
