---
path: zh/x1/maintenance/replace-micro-lidar>
title: "更换 Bambu 激光雷达"
description: "更换激光雷达的要求、操作步骤和检验方法"
tags: []
created: 2022-07-31T03:36:11.062Z
updated: 2026-04-23T04:05:29.862Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-micro-lidar>
---

## 什么是Bambu 激光雷达？

Bambu 激光雷达是一种能够以微米为单位的测量深度的传感器，它将微米级的精度带入到 3D 打印。它能够检测喷嘴距离打印面的高度，校准从喷嘴挤出的流量，并扫描首层打印的状况。

在购买 X1C/X1 的 TH 板或激光雷达之前，请务必确保先确定其版本，以免购买错误版本导致报错不兼容。[Bambu Lab 激光雷达介绍和单红光和双红光版本判断逻辑说明](../manual/micro-lidar-model.md)

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/424px-bml.png)

## 何时更换

如果您的打印机在屏幕上显示与“激光雷达”相关的警告（例如，激光未点亮），您重新测试并检查相关的了连接线路，但没有得到改善，你可能需要更换激光雷达。

## 需要的工具和材料

- 全新 Bambu 激光雷达
- H1.5 内六角扳手
- 电吹风
- 硅胶

![](https://wiki.bambulab.com/x1/maintenance/replace-the-chamber-led/silicone_glue.jpg)

仅供参考

## 开始操作前的安全警告和机器状态

请仔细按照本指南步骤进行更换。在开始任何拆卸和组装之前，请确保机器已断电。

## 操作指南

本文以 V8 版本 TH 板举例，激光雷达的更换步骤完全相同，您可以放心操作。

### 第 1 步 - 下降热床

打开打印机电源，在显示屏的移动菜单中点击下降热床标签，将热床降低到接近机器底部。完成后，关闭打印机电源并取下顶部玻璃盖板。

### 第 2 步 - 移除工具头的后盖

使用内六角扳手移除固定工具头后盖的 4 颗螺丝，然后取下工具头后盖。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/1020px-lidar_ds4.png)

### 第 3 步 - 断开 FPC

移除位于挤出板左下角用于加固 FPC 连接器的 2 颗螺丝。完成后，将 FPC 从连接器上松开。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/632px-cam_c.png)

### 第 4 步 - 拧松螺丝

稍微拧松固定挤出板的 3 颗螺丝，以便更轻松地将激光雷达的电缆从卡扣中取出。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/674px-cables.png)

### 第 5 步 - 断开电缆连接器

连接器有用到一些硅胶进行加固，以确保它们在运动过程中保持这种连接的状态。所以为了拔下电缆，请使用吹风机稍微加热硅胶，将硅胶软化后再将电缆从连接器中轻松。断开连接后，您可以去除在连接器上的残胶。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/287px-connectors.png)

### 第 6 步 - 移除Bambu激光雷达

移除位于工具头下方的 2 颗螺丝。完成后，激光雷达应该会脱落，将其取下即可。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/353px-screw2.png)

### \*\*第 7 步 - 组装新的Bambu激光雷达

我们现在需要将拆解过程反过来以完成新激光雷达的安装。首先将激光雷达安装到工具头的底部，然后锁入 2 颗螺丝将其固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/353px-screw2.png)

### 第 8 步 - 连接 3 根电缆

如下图所示将三根电缆连接到挤出板对应的连接器上，(建议在连接器上点上硅胶进行加固，然后静置 30 分钟，等待硅胶初步硬化)。完成后，将拧松的 3 颗螺丝重新固定。

|![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/287px-connectors_(1).png)

> V9 版本的线缆安装位置与 V8 一致，位于绿色标记位置；图中 2 号标记插座为测试插座，无需安装。  
> ![thth.jpg](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/thth.jpg)

### 第 9 步 - 理线

如下图所示，沿挤出板的侧面理好电缆，将线材扣入到卡扣内侧，注意避开螺丝孔。然后，连接 FPC 排线到挤出板下方的接口上，用 2 颗螺丝将连接器固定片安装到位。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/555px-arrange1.png)

### 第 10 步 - 安装工具头后盖

重新安装工具头的后盖并用 4 颗螺丝（每侧 2 颗）将其固定。完成后，将顶部玻璃盖放回机器上。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/1047px-lidar_as4.png)

## 如何验证完成/成功

- 打开打印机电源后，屏幕上应该会弹出一条消息，提示检测到新的激光雷达。
- 在确认机器内部干净无异物后，进入屏幕上的校准菜单，然后点出“开始校准”。

![calibration.png](https://wiki.bambulab.com/screen-operation/calibration.png)

- 校准完成后，再执行一次设备自检，如下所示。

![selftest.png](https://wiki.bambulab.com/screen-operation/selftest.png)

如果以上操作一切顺利，并且在校准和自检过程中没有出现错误或警告，则更换成功。否则，请检查连接后重试。如果问题仍然存在，请联系服务团队寻求进一步帮助。
