---
path: zh/p1/troubleshooting/heat-bed-not-heat-up-1
title: "P1 系列打印机热床不升温问题排查"
description: "P1 系列打印机热床加热失败，排查指导"
tags: []
created: 2023-02-24T08:32:05.537Z
updated: 2026-03-18T08:19:01.528Z
source: https://wiki.bambulab.com/zh/p1/troubleshooting/heat-bed-not-heat-up-1
---

## **问题现象**

打印机在准备打印和打印过程中，出现热床无法加热或者床温为零，手动设置床温也无响应。

## 原因及解决方案

导致热床温度异常主要的几个原因及解决方案如下：

1. 检测热床电阻值 → 电阻值异常 → 热床元器件烧坏或开路 → 更换热床；
2. 检查热床供电线连接状态，MC 板-AC 电源板连接状态 → 接触不良→ 重新连接；
3. 检查热床电源线导通→ 开路 → 更换热床电源线缆（或更换热床）；
4. 检查 AC 电源板 → 器件损坏（确认热床及电源线正常） → 更换 AC 电源板。

## 安全和操作提示

1. 热床是直接使用市电加热的，有高压危险，需要确保在断开电源连接的情况下进行故障排查;

2. 如果发现是热床（AC 电源板）烧坏，应同时检查 AC 电源板（热床）是否也烧坏。

## 所需的工具

- H2.0 内六角扳手
- 万用表
- 镊子

## 情形一：热床温度显示 0℃

![](https://wiki.bambulab.com/p1/troubleshooting/heat-bed-not-heat-up/0_c_p1p.png)

### 排查方案

1. 检查热床 NTC 的连接状态；
2. 检查热床到 MC 板连接线的连接状态；

> 注意：这两根线的接头用白色硅胶固定，需要断开时，可以用吹风机加热硅胶使其硬度降低，再断开连接线。

### 操作步骤（拆解检查）

#### 步骤 1：抬升热床

倾斜打印机，拉动 Z 轴皮带使热床抬升至丝杆全高度 ⅔ 位置，腾出处理空间。

![](https://wiki.bambulab.com/p1/troubleshooting/heat-bed-not-heat-up/move_up_the_heatbed.jpg)

#### **步骤 2**  - 拆下热床预紧螺母

拧下 3 个预紧螺母，将加热床从金属支架上解锁。请注意，每个螺母顶部还有一个橡胶环。

|  |  |
| --- | --- |
|  |  |

#### **步骤 3**  -  打开热床

小心打开热床，因为里面有电缆连接，取下已松脱出来的预紧弹簧。

![](https://wiki.bambulab.com/x1/troubleshooting/heatbed-not-heat-up/open.jpg)

#### **步骤 4**  -  检查连接状态

检查热床到 MC 板的连接线和 NTC 线，其中 2PIN 为 NTC 连接线。检查连接器有无松动，连接线有无松出。

- 检查确认或重新连接后，可再次连接电源，开机确认热床温度是否不再显示 0℃。
- 如果故障仍未排除，需要联系售后进行确认。

![](https://wiki.bambulab.com/x1/troubleshooting/heatbed-not-heat-up/ntc_and_mc-heatbed.jpg)

#### 步骤 5 - 移除背板

- 移除 4 颗粗牙螺丝；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/remove_4_screws.jpg)

- 移除 7 颗细牙螺丝，取下背板。

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/lock_7_screws.jpg)

> P1S 请参考：[更换 P1 系列金属背板](../maintenance/p1s-rear-panel.md)

#### 步骤 6 - 检查连接器

检查 MC 板端的连接线状态，确认连接没有浮起和退 PIN。检查确认后，可重新连接电源，开机确认热床温度是否不再显示为 0； 如果故障未排除，则需要再检查热床端的连接状态。

![](https://wiki.bambulab.com/p1/maintenance/heat-bed/connect_the_signal_cable.jpg)

### 安装指引

#### 安装预紧弹簧

握住热床的上部，将预紧弹簧一个接一个地安装到加热床螺钉上。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/install_the_springs.jpg)

#### 安装热床

合上热床并将它与支架固定在一起。从加热床顶部轻轻按压，并确认所有三个螺钉的个根部都可以穿过传感器支架上的孔。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/screw.jpg)

#### 锁定预紧螺母

将橡胶圈放在 3 个预紧螺母上，然后将它们均匀拧入，一次拧一点，不要拧紧，直到螺柱与螺母底部齐平（见下图）。

|  |  |
| --- | --- |
|  |  |

#### 安装背板

1. 将后面板安装到打印机背面；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/install_rear_panel.jpg)

2. 锁入 7 颗细牙螺丝；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/lock_7_screws.jpg)

3. 锁入 4 颗粗牙螺丝。

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/remove_4_screws.jpg)

> P1S 请参考：[更换 P1 系列金属背板](../maintenance/p1s-rear-panel.md)

## 情形二：热床温度不为 0℃

这种情况一般是热床的供电异常，导致热床无法加热。

![](https://wiki.bambulab.com/x1/troubleshooting/heatbed-not-heat-up/not_0.jpg)

### 排查方案

1. 检查热床电源线的连接状态；

2. 检查 AC 板输出（高压危险，需要有电工基础）

### 操作步骤（拆解检查）

#### 步骤 1：抬升热床

倾斜打印机，拉动Z轴皮带使热床抬升至丝杆全高度⅔的位置，腾出处理空间。

![](https://wiki.bambulab.com/p1/troubleshooting/heat-bed-not-heat-up/move_up_the_heatbed.jpg)

#### 步骤 2：测试热床电阻值

拆下热床底下电源线的两颗螺丝，取下盖子，用万用表测试两个端子的电阻值；

- 如果阻值在 40~60 ohms，则热床正常；
- 如果阻值不在 40~60 ohms，需要更换热床，请参考[更换热床](../maintenance/heat-bed.md)。

|  |  |
| --- | --- |
|  |  |

#### 步骤 3：移除背板

- 移除 4 颗粗牙螺丝；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/remove_4_screws.jpg)

- 移除 7 颗细牙螺丝；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/lock_7_screws.jpg)

- 取下后面板。

![](https://wiki.bambulab.com/p1/maintenance/protective-cover/excess_chute_removed.jpg)

> P1S 请参考：[更换 P1 系列金属背板](../maintenance/p1s-rear-panel.md)

#### 步骤 4：移除走线槽

用 H2.0 内六角扳手移除2颗螺丝，取下走线槽。

![](https://wiki.bambulab.com/p1/maintenance/protective-cover/remove_the_holder.jpg)

#### 步骤 5：移除护线盖

用 H1.5 内六角扳手移除6颗螺丝，取下护线盖。

![](https://wiki.bambulab.com/p1/maintenance/protective-cover/6_screws.jpg)

#### 步骤 6：检查连接器

拆除打印机背板和护线盖，检查热床电源线和 MC 板-AC 板连接线的连接状态，确认连接正常，无松脱或歪斜。

|  |  |
| --- | --- |
|  |  |

#### 步骤 7：检测热床电源线

移开两个保护胶套，用万用表测试阻值；

- 如果阻值在 40~60 ohms，则热床正常；
- 如果阻值不在 40~60 ohms，需要更换热床，请参考[更换热床](../maintenance/heat-bed.md)。

![](https://wiki.bambulab.com/p1/troubleshooting/heat-bed-not-heat-up/measure_the_resistance.jpg)

> 注意：测试完或维修完成后，请务必将两个保护胶套装回原位，避免短路。  
> ![](https://wiki.bambulab.com/p1/troubleshooting/heat-bed-not-heat-up/power_scokets.jpg)

#### 步骤 8：检查 AC 电源板

如果上述步骤确认无异常，那么基本上确认是 AC 电源板故障，需要更换 AC 电源板，请参考[更换 AC 电源板](../maintenance/ac-board.md)。

当然，如果能直接观察到 AC 电源板上有元器件损坏，也可以判断是 AC 电源板损坏。

![](https://wiki.bambulab.com/p1/troubleshooting/heat-bed-not-heat-up/ac_board.jpg)

### 安装指引

#### 安装护线盖

将护线盖安装到打印机上，注意避让电缆，锁入 6 颗螺丝固定。

|  |  |
| --- | --- |
|  |  |

#### 安装走线槽

安装走线槽，锁入 2 颗螺丝固定。

![](https://wiki.bambulab.com/p1/maintenance/protective-cover/remove_the_holder.jpg)

#### 安装背板

1. 将后面板安装到打印机背面；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/install_rear_panel.jpg)

2. 锁入 7 颗细牙螺丝；

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/lock_7_screws.jpg)

3. 锁入 4 颗粗牙螺丝。

![](https://wiki.bambulab.com/p1/maintenance/rear-panel/remove_4_screws.jpg)

> P1S 请参考：[更换 P1 系列金属背板](../maintenance/p1s-rear-panel.md)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
