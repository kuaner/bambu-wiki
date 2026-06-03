---
path: zh/p1/maintenance/xy-motor
title: "XY 电机拆装指南"
description: "拆装 P1 系列打印机 XY 电机的操作步骤"
tags: ["p1", "xy 电机"]
created: 2022-12-19T11:12:52.538Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/p1/maintenance/xy-motor
---

## XY 电机

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/motor_a_and_b_cn.jpg)

电机A和电机B是一样的

## 工具

- H2.0/1.5 内六角扳手（加长和加磁的H2.0内六角扳手）
- 镊子

## 准备工作

断开电源连接。

## 拆除

### **第 1 步 -**  拆除废料滑梯

参考 [废料滑梯](excess-chute.md) 的相关内容，拆除后面板和废料滑梯。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/excess_chute_removed.jpg)

### **第 2 步 -** 松出 XY 张紧器

根据要更换的电机，参考[XY张紧器惰轮](xy-idler-pulley.md) 的相关内容，松出对应位置的 XY 张紧器。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 -  移**除 A 电机

可根据以下步骤拆下 A 电机：

#### 3-1 断开电机连接

断开电机 A 连接，并移除其上的柱形磁环，将电机电缆从线扣和胶带中松脱出来。

|  |  |
| --- | --- |
|  |  |

#### 3-2 移除皮带

用扳手或镊子将皮带从 A 电机主动轮中松出。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/remove_the_belt_from_the_pulley.jpg)

#### 3-3 移除 A 电机固定螺丝

电机由 4 颗螺丝固定，两颗明显可见，两颗需要用较长的内六角螺丝刀从上往下穿到螺丝位置，移除 4 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/4_screws_for_motor_a.jpg)

#### 3-4 移除 A 电机

回退电机电缆后，移除 A 电机。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/remove_motor_a.jpg)

### **第 4 步 - 移**除 B 电机

可根据以下步骤拆下 B 电机：

#### 4-1 断开电机连接

从 AMS 接口板上断开到 MC 板的电缆连接，然后从 MC 板上断开 MC-AP、MC-TH 的电缆连接，断开 B 电机的连接，并移除柱形磁环，将电机电缆从线扣上释放出来。

|  |  |
| --- | --- |
|  |  |

#### 4-2 下降热床

倾斜打印机，拉动 Z 轴皮带，在不影响拆装内衬螺丝的情况下，尽可能降低热床。

|  |  |
| --- | --- |
|  |  |

#### 4-3 松出电源插口

用镊子撬松电并取出电源插口。

|  |  |
| --- | --- |
|  |  |

#### 4-4 松内衬

拧下固定内衬的 9 颗螺丝，将内衬上方松开一些空间，便于电机的拆装。

|  |  |
| --- | --- |
|  |  |

#### 4-5 移除皮带

用扳手或镊子将皮带从 B 电机主动轮中松出。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/remove_the_belt_from_the_pulley_b.jpg)

#### 4-6 移除 B 电机固定螺丝

电机 B 同样由 4 颗螺丝固定，两颗明显可见，两颗需要用较长的内六角螺丝刀从上往下穿到螺丝位置，移除 4 颗螺丝。

***注意：扳手要充分加磁，且固定电机的螺丝比较紧，需要小心处理，防止螺帽损坏。***

|  |  |
| --- | --- |
|  |  |

对于 P1S，有 2 颗螺丝被拖链盖板挡住，需要先移除拖链盖板：

1. 参考[此页面](p1s-rear-panel.md)，移除打印机的金属背板。

2. 移除拖链盖板的固定螺丝。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/remove-screw.png)

3. 移除拖链盖板。

> *红色圆圈为螺丝孔的位置，用于插入扳手，方便移除电机固定螺丝。您可以选择移除此处的黑色泡棉，或用扳手戳穿泡棉，使孔漏出。*

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/remove--cover.png)

#### 4-7 移除 B 电机

先下沉电机，再倾斜着将电机移除，同时将电机线从过线孔中拉出。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/remove_motor_b.jpg)

## 安装

### **第 1 步 -** 安装 A 电机

参考以下步骤安装 A 电机

#### 1-1 安装 A 电机

将电机电缆穿过过线孔，将 A 电机安装到电机支架上，皮带装到主动轮上。

|  |  |
| --- | --- |
|  |  |

#### 1-2 锁 A 电机螺丝

锁入固定电机的 4 颗螺丝，后面的两颗螺丝需要在上横梁的位置将螺丝放置到内六角螺丝刀上，再通过螺丝刀将螺丝送到位。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/lock_motor_a.jpg)

#### 1-3 连接电机电缆

如图所示整理好电机电缆，安装上柱形磁环，然后连接到 MC 板 A 电机的接口上。

|  |  |
| --- | --- |
|  |  |

### **第 2 步 -** 安装 B 电机

参考以下步骤安装 B 电机：

#### 2-1 安装 B 电机

先将 B 电机电缆穿过过线孔，然后将 B 电机安装到位，并将同步皮带安装到电机主动轮上。

|  |  |
| --- | --- |
|  |  |

#### 2-2 锁 B 电机螺丝

锁入固定电机的 4 颗螺丝，后面的螺丝有 1 颗需要在上横梁的位置将螺丝放置到内六角螺丝刀上，再通过螺丝刀将螺丝送到位，另一颗螺丝需要直接将螺丝放到螺丝孔上，再用螺丝刀拧紧。

|  |  |
| --- | --- |
|  |  |

#### 2-3 固定内衬

将内衬贴合后横梁，锁入 9 颗螺丝固定。

|  |  |
| --- | --- |
|  |  |

#### 2-4 连接电缆

安装好柱形磁环，并将电机线连接到 MC 板 B 电机的连接口上，连接 MC-AP、MC-TH 电缆，连接 AMS 接口板，整理好电缆。

|  |  |
| --- | --- |
|  |  |

#### 2-5 安装电源插口

将电源插口装回原位。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/mount_the_power_socket.jpg)

### **第 3 步 -** 安装 XY 张紧器

参考 [XY张紧器惰轮](xy-idler-pulley.md) 的相关内容，安装好已松出的张紧器，并重新张紧皮带。

![](https://wiki.bambulab.com/p1/maintenance/xy-motor/lock_the_tensioners.jpg)

### **第 4 步 -** 组装好打印机

参考 [废料滑梯](excess-chute.md) 的内容，安装好废料滑梯和后面板。

![](https://wiki.bambulab.com/p1/maintenance/excess-chute/rear_panel_installed.jpg)

## 如何验证完成

接上打印机电源，开启打印机，在屏幕上操作，运行设备校准流程，如自检通过，说明操作成功。

![32.校准.jpg](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/32.%E6%A0%A1%E5%87%86.jpg)
