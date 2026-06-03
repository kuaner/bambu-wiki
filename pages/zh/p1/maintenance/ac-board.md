---
path: zh/p1/maintenance/ac-board
title: "更换 P1 系列打印机 AC 板"
description: "拆装 P1 系列打印机 AC 板的操作步骤"
tags: ["ac 电源板", "p1"]
created: 2022-12-15T15:01:21.248Z
updated: 2026-04-29T08:59:09.787Z
source: https://wiki.bambulab.com/zh/p1/maintenance/ac-board
---

## AC 电源板

该 AC 电源板是专门为 X1 打印机的 V3 版本热床和 P1 系列打印机的热床提供交流电源的电路板。

![](https://wiki.bambulab.com/p1/maintenance/ac-board/ac_board.jpg)

## 工具

- H2.0/H1.5 内六角扳手
- 十字螺丝刀

## 准备工作

断开电源连接。

## 拆除

### **第 1 步 -**  拆除背板、废料滑梯、电源板保护盖

参考拆装电源板保护盖的相关内容，移除背板、废料滑梯和电源板保护盖。

![](https://wiki.bambulab.com/p1/maintenance/ac-board/ac.png)

### **第 2 步 -** 断开热床电源线

移除保护胶套，用镊子协助解除锁扣，拔出 2 根热床电源线。

![](https://wiki.bambulab.com/p1/maintenance/ac-board/disconnect_power_sockets.jpg)

### **第 3 步 -** 断开 AC 板电源线

揭开保护盖，用十字螺丝刀拧松 3 颗螺丝，拔出电源线，再断开 AC-MC 连接线。

![](https://wiki.bambulab.com/p1/maintenance/ac-board/disconnect_power_cables.jpg)

### **第 4 步 -** 移除 AC 电源板

用 H1.5 内六角扳手，移除 3 颗螺丝，取下 AC 电源板。

![](https://wiki.bambulab.com/p1/maintenance/ac-board/3_screws_for_ac_board.jpg)

## 安装

### **第 1 步 -** 安装 AC 电源板

将 AC 电源板安装到内衬上，锁入 3 颗螺丝进行固定。

![](https://wiki.bambulab.com/p1/maintenance/ac-board/3_screws_for_ac_board.jpg)

### **第 2 步 -** 连接 AC 板电源线

将 3 根电缆连接到输入端子上，锁紧螺丝，合上保护盖，然后再接上 AC-MC 连接线。

![](https://wiki.bambulab.com/x1/maintenance/replace-ac-board/mc-ac.png)

### **第 3 步 -** 连接热床电源线

检查热床电源线插头，如有问题需要先进行处理。然后插到 AC 板对应接口上，装好保护胶套。

|  |  |
| --- | --- |
|  |  |

### **第 4 步 -** 组装好打印机

整理好电缆后，参考拆装电源板保护盖的相关内容，依次装上电源保护盖、废料滑梯和背板，将打印机组装好。

![](https://wiki.bambulab.com/p1/maintenance/power-board/rear_panel_installed.jpg)

## 如何验证完成

接上打印机电源，开启打印机，在屏幕上操作，运行设备校准流程，如校准通过，说明操作成功。

![32.校准.jpg](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/32.%E6%A0%A1%E5%87%86.jpg)
