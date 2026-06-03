---
path: zh/p1/manual/kind-reminder-for-P1P-enclosure
title: "P1P封箱温馨提示"
description: "P1P封箱的一些注意事项和提醒。"
tags: ["封箱"]
created: 2023-03-20T11:22:10.964Z
updated: 2024-09-09T08:50:16.120Z
source: https://wiki.bambulab.com/zh/p1/manual/kind-reminder-for-P1P-enclosure
---

如果您想要进行DIY封箱，请务必保证按照如下要求进行准备、改制和测试。否则可能会造成打印机故障。

特别提醒：

1. 在没有加装腔室控温风扇的情况下，封箱后不建议打高温材料;

2. 建议参考官方的升级包安装指引完成封箱。

### 1. 需要加装MC风扇（固件默认MC风扇关闭，需要使用Gcode开启）

P1P是基于不封闭机箱的环境下设计的，取消了主控板上的风扇（最早期的300台+P1P也已被禁用）。如果对P1P进行了封箱，理论上需要重新加装主控板风扇，加装的主控板风扇只能通过Gcode进行开启。

> - M710 A1 S255:打开主控板冷却风扇自动控制，主控板冷却风扇将在步进电机打开时自动打开，步进电机关闭时自动关闭;
> - M710 S0:关闭主控板冷却风扇.

![](https://wiki.bambulab.com/p1/manual/firmware-history/c11u3p09cn.png)
![](https://wiki.bambulab.com/p1/manual/p1p-enclosure/mc_fan.jpg)

**Bambu Lab拓竹3D打印机主控板风扇**

风扇安装位置如下图，上下边沿建议打上结构胶固定。

![](https://wiki.bambulab.com/p1/manual/p1p-enclosure/mc_fan_location.png)

主控板风扇安装位置

### 2. 关于拖链的安装

如果您需要给您的P1P安装拖链，请参考视频并阅读以下提醒：

1. 标配的工具头数据线在加装拖链后可能会容易损坏，请同时购买合金铜版本的工具头线缆进行更换。

![](https://wiki.bambulab.com/p1/manual/p1p-enclosure/tool_head_cable.jpg)

**Bambu Lab 3D打印机P1P工具头数据线**

2. 为避免料管长度不足而导致工具头丢步，建议将原来长度是530mm的料管更换成550mm的料管。

![](https://wiki.bambulab.com/p1/manual/p1p-enclosure/cable_chain.jpg)

**Bambu Lab拓竹X1 3D打印机工具头拖链组件**

### 3. 建议使用cool plate打印

完成封箱后，如果没有加装机箱控温风扇，建议采用低温打印板进行打印，避免在腔温较高的情况下，部分打印材料因提前软化而频繁出现挤出机卡料或喷嘴堵头的问题。

![](https://wiki.bambulab.com/p1/manual/p1p-enclosure/cool_plate.jpg)

**Bambu Lab拓竹3D打印机低温打印面板**

### 4. 建议加装机箱控温风扇

如果需要经常打印高温材料，如ABS，要用到高床温的情况下，建议打印以下风道模型进行加装控温风扇。

[风道模型](https://wiki.bambulab.com/p1/manual/p1p-to-p1s/fan_&_air_filter_bracket(1).3mf)

![](https://wiki.bambulab.com/p1/manual/p1p-enclosure/regulator_fan.jpg)

**Bambu Lab拓竹3D打印机机箱控温风扇**

其他提醒：因前面盖的尺寸差异，X1系列使用的玻璃前门不能直接用于P1P, 如果需要完全匹配，需要更换成P1S的前面盖，或者自行增加挡边。

为更好的保证打印品的质量和打印的顺利完成，在您确认要进行封箱时，强烈建议您参考官方升级包的封箱操作后再进行个性化的封箱。
