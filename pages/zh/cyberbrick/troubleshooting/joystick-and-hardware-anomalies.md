---
path: zh/cyberbrick/troubleshooting/joystick-and-hardware-anomalies
title: "Cyberbrick 摇杆和硬件异常的排查方法"
description: "本章将为您介绍当 Cyberbrick 摇杆和硬件出现异常的时候应该如何进行故障排查。"
tags: []
created: 2025-07-07T02:20:48.458Z
updated: 2026-05-12T08:54:02.200Z
source: https://wiki.bambulab.com/zh/cyberbrick/troubleshooting/joystick-and-hardware-anomalies
---

在使用 cyberbrick 产品时，您可能会遇到摇杆没反应等情况。当您遇到这些问题时，您可以根据实际遇到的故障，选择对应的方法来解决您所遇到的问题：

## 问题 1：遥控器摇杆没反应/小车自动往某个方向偏移

当您推动摇杆时，小车没有反应，或小车自动往某一方向移动，您可以参考下述步骤进行排查，可根据实际情况来调整排查顺序。

### 步骤 1：检查摇杆的接头是否插到位

请检查板子上的接头是否全部插到位，同时也请再次对照组装模型的图纸来检查线缆是否连接正确。

### 步骤 2：重新烧录程序

您可以打开 Cyberbrick 手机 APP，在 APP 中选择对应的模型（需与组装的模型一致），将程序重新烧录至遥控器和小车上，然后检查是否可以正常使用。

### 步骤 3：校准摇杆中值

1. 在 CyberBrick 软件上点击‘’遥控器‘’左侧的箭头，弹出下拉菜单；

![pic-1.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/joystick-and-hardware-anomalies/pic-1.png)

- 选择对应的摇杆，并点击中值设置，连接遥控器；

![pic-2.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/joystick-and-hardware-anomalies/pic-2.png)

- 根据实际的异常情况，选择对应的摇杆来进行中值校准。以校准左摇杆为例：

  1. 点击左摇杆；
  2. 点击中值设置；
  3. 点击自动中值校准；
  4. 最后根据提示点击开始即可。
  > 注：请勿自行修改中值和死区大小。

![pic-3.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/joystick-and-hardware-anomalies/pic-3.png)

![pic-4.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/joystick-and-hardware-anomalies/pic-4.png)

### 步骤 4：交叉验证

如果上述没有解决您的问题，您可以依次互换摇杆和连接线，用于确定故障范围。

如：摇杆 A 异常，未通过上述步骤解决，您可以将摇杆 B 更换至摇杆 A 的位置，然后摇动摇杆，检查功能是否正常：

- 如果功能正常，则为摇杆 A 异常，可更换一个摇杆；
- 如果功能异常，则请继续更换摇杆连接，检查功能是否正常;

  - 如果功能正常，则为连接线异常，可更换连接线；
  - 如果功能异常，可能为底板或多功能主板异常，请更换底板或多功能主板进行验证。

## 问题 2：舵机旋转效果不对

在 RC 套件中我们有两种类型的舵机：

- 9g 180° 角度舵机 - PG001
- 9g 360° 速度舵机 - PG002

![](https://wiki.bambulab.com/cyberbrick/troubleshooting/joystick-and-hardware-anomalies/123.jpg)

角度舵机一般用于转向机构、变形机构等。如在车辆模型中用于控制转向架，可以实现小车向左或向右转弯。如果您在小车上使用了 9g 360° 速度舵机，那么由于舵机会一直选项，当处于限位处时发出“哒哒哒”的声音。

**区分舵机类型方法：**

1. 通过舵机上的标签进行区分（如上图所示）；
2. 将舵机安装接收板上，然后将卡车的程序导入，使用右摇杆往左（或往右）摆动，观察舵机的转动：

   1. 舵机能 360° 转动，则为 360° 速度舵机；
   2. 舵机转动至一定角度停止，则为 180° 角度舵机

因此，当您遇到舵机的效果与预期不符时，请根据说明书检查是否使用了正确的舵机。

## 问题 3：某个硬件没有反应（交叉验证）

如果您的某个硬件没有反应（如电机无法正常转动），您可以参考“问题 1”中“步骤 4：交叉验证”的方法进行排查。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
