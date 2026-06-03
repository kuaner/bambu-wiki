---
path: zh/p1/maintenance/z-motor
title: "Z 轴电机"
description: "拆装 P1 系列打印机 Z 轴电机的操作步骤"
tags: ["p1", "z 轴电机"]
created: 2022-12-29T10:40:33.074Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/p1/maintenance/z-motor
---

## Z 轴电机

![](https://wiki.bambulab.com/p1/maintenance/z-motor/z_motor.jpg)

## 工具

- H2.0/1.5 内六角扳手
- 镊子

## 准备工作

断开电源连接。

## 拆除

### **第 1 步 -**  移除后面板

参考 [后面板](rear-panel.md) 的相关内容，移除后面板。

![](https://wiki.bambulab.com/p1/maintenance/z-motor/rear_panel_removed.jpg)

### **第 2 步 -** 松脱电机排线

从 MC 板上断开 Z 电机连接线，移除柱形磁环，然后沿着走线将整条电缆松出。

![](https://wiki.bambulab.com/p1/maintenance/z-motor/release_the_motor_cable.jpg)

### **第 3 步 -** 下降热床并锁定 Z 轴滑块

倾斜打印机，拉动 Z 轴皮带将热床下降到底部，锁入 3 颗辅助螺丝固定 3 个 Z 轴滑块。

![](https://wiki.bambulab.com/p1/maintenance/z-motor/lower_the_head_bed_and_lock_the_sliders.jpg)

### **第 4 步 -** 松 Z 张紧器

侧放打印机，拧松 Z 张紧器螺丝，解除张紧弹簧的张紧状态。

|  |  |
| --- | --- |
|  |  |

### **第 5 步 -** 移除 Z 电机

移除 4 颗螺丝，取下 Z 轴电机。

![](https://wiki.bambulab.com/p1/maintenance/z-motor/remove_4_screws.jpg)

## 安装

### **第 1 步 -** 安装 Z 轴电机

将 Z 轴电机安装到打印机底座上，注意电机排线的朝向，皮带要绕过主动轮。

|  |  |
| --- | --- |
|  |  |

### **第 2 步 -** 锁电机螺丝

按对角线打螺丝固定的方法，锁入 4 颗螺丝固定Z轴电机，然后挂上张紧弹簧。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 -** 解除 Z 滑块锁定

正放打印机，然后移除锁定 Z 轴滑块的 3 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/z-motor/unlock_the_sliders.jpg)

### **第 4 步 -** 锁张紧器螺丝

再次侧放打印机，拉动 Z 轴皮带使热床上下运动，确认动作无异常，然后锁紧张紧器螺丝。

|  |  |
| --- | --- |
|  |  |

### **第 5 步 -** 连接电机电缆

正放打印机，将电机电缆沿走线路径整理好，装上柱形磁环，并连接到 MC 板的连接器上。

|  |  |
| --- | --- |
|  |  |

### **第 6 步 -** 安装后面板

参考 [后面板](rear-panel.md) 的相关内容，安装好后面板。

![](https://wiki.bambulab.com/p1/maintenance/excess-chute/rear_panel_installed.jpg)

## 如何验证完成

接上打印机电源，开启打印机，在屏幕上操作，运行设备校准流程，如自检通过，说明操作成功。

![32.校准.jpg](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/32.%E6%A0%A1%E5%87%86.jpg)
