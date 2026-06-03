---
path: zh/x1/maintenance/replace-the-heatbed-force-sensor
title: "更换热床压力传感器和跟随小板"
description: "本指南提供更换 X1 系列打印机热床压力传感器和跟随小板的详细步骤。"
tags: ["x1"]
created: 2022-08-20T13:43:33.598Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-the-heatbed-force-sensor
---

## 热床压力传感器

压力传感器是一种能够感知力信号并将力信号按照一定规则转换成可输出的电信号的装置。 为了检测热床的表面压力，我们在热床底部安装了 3 个陶瓷压力传感器。

|  |  |
| --- | --- |
|  |  |

> 注意区分跟随小板和跟随转接板：
>
> - 热床跟随小板：安装在热床内，连接传感器 1 和传感器 3 的小电路板，共有 2 块。
>
> ![](https://wiki.bambulab.com/x1/pcb.jpg)
>
> - 跟随转接板：安装在热床后，有 5 个连接口。
>
> ![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/%E8%B7%9F%E9%9A%8F%E8%BD%AC%E6%8E%A5%E6%9D%BF.png)

## 何时维护

当同时满足以下 3 个条件时，或者可以看到传感器有明显的物理损坏，则需要更换压力传感器或（跟随小板）。

1. 当您收到错误消息“热床压力传感器 1/2/3 的灵敏度太低。 传感器的电子连接可能已损坏。”

2. 按照 HMS 指南进行了检查，但没有解决问题。

3. 服务团队确认需要更换。

## 所需工具和材料

- 新的压力传感器 (热床跟随小板)
- H2.0/H1.5 六角扳手

## 开始操作前的安全警告和机器状态

请仔细按照本指南步骤进行更换。 在开始任何拆卸和组装之前，请确保机器已关闭。

## 操作指南

本次更换我们以 1 号压力传感器、1 号跟随小板为例进行指导，其他两个压力传感器、跟随小板的更换类似。

### **步骤 1** ：为更换腾出空间

打开打印机电源，在屏幕上的控制界面，将热床的 Z 位置调整到中间。 完成后，关闭打印机电源并取下顶部玻璃盖板，然后将工具头移至废料滑梯位置。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/space.jpg)

### **步骤 2** ：取下保护盖

保护罩由 4 个卡扣固定。 您可以通过先解锁一侧然后再解锁另一侧来将其移除。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/remove_protective_cover.jpg)

### **步骤 3** ：拆下热床预紧螺母

拧下 3 个预紧螺母，将加热床从金属支架上解锁。 请注意，每个螺母顶部还有一个橡胶环。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/remove_the_nuts.jpg)

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/rubber_on_the_nuts.jpg)

### **步骤 4** ：暂时打开并支撑热床

小心打开加热床，因为里面有电缆，然后拆下松动的预紧弹簧。 为了继续进行下面的操作，需要暂时将热床支撑起来。 您可以使用一个方块来支撑加热床的上部（见下图）。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/open_upper_cover.jpg)

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/hold_the_upper_cover.jpg)

### **步骤 5 ：移除跟随小板**

现在您可以断开跟随小板上的 2 根连接电缆，移除 2 颗螺丝，取下跟随小板。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-heat-bed/2_connectors.jpg)

![](https://wiki.bambulab.com/x1/maintenance/replace-the-heat-bed/2_screws_2.jpg)

### **步骤 6** ：拆下压力传感器

拧下底部的 2 颗螺丝，取下带有支架的压力传感器。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/unscrew.jpg)

### **步骤 7 ：安装力传感器**

准备要安装的新压力传感器。 请注意，有 2 个限制柱有助于简化安装（见下图）。 拧紧 2 个螺钉以固定压力传感器。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/install_location.jpg)

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/unscrew.jpg)

### **步骤 8 ：安装跟随小板**

将跟随小板安装到支架上，锁上 2 颗螺丝，连接 2 根电缆。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-heat-bed/2_screws_2.jpg)

![](https://wiki.bambulab.com/x1/maintenance/replace-the-heat-bed/2_connectors.jpg)

### **步骤 9** ：安装预紧弹簧

握住加热床的上部，取下刚刚使用的支撑块。将预紧弹簧一个接一个地安装到加热床螺钉上。一般情况下，只需要安装前两个弹簧，因为后面的不会脱落。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/install_the_springs.jpg)

### **步骤 10** ：安装热床

现在您可以合上热床并将它与支架固定在一起。 从加热床顶部轻轻按压，并确认所有三个螺钉的个根部都可以穿过传感器支架上的孔。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/screw.jpg)

### **步骤 11** ：锁定预紧螺母

将橡胶圈放在 3 个预紧螺母上，然后将它们均匀拧入，一次拧一点。不要锁定它们。继续均匀地拧入螺母，直到螺柱与螺母底部齐平（见下图）。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/rubber_on_the_nuts.jpg)

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/check_the_nut_position.jpg)

### **步骤 12** ：安装保护罩

现在您需要安装保护罩。 与拆卸时相同，先安装一侧，然后安装另一侧。

![](https://wiki.bambulab.com/x1/maintenance/heatbed-force-sensor/install_the_protective_cover.jpg)

## 如何验证完成/成功

连接电源线并打开电源。

确保腔室没有床上的任何打印物品或挤出材料。然后进入 LCD 屏幕上的设置菜单，选择校准选项卡，然后按“开始校准”。

![calibration.png](https://wiki.bambulab.com/screen-operation/calibration.png)

如果一切按计划进行，并且在校准过程中没有出现错误或警告，则更换成功。否则，请检查连接并重试。如果问题仍然存在，请联系服务团队寻求进一步帮助。
