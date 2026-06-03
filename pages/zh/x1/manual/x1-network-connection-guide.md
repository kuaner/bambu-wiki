---
path: zh/x1/manual/x1-network-connection-guide
title: "X1/X1C 网络连接指南"
description: "介绍 X1/X1C 如何接入网络，以及可能遇到的问题和解决方法"
tags: ["x1", "x1c", "x1e", "网络"]
created: 2024-08-08T10:16:06.840Z
updated: 2024-08-09T08:31:53.390Z
source: https://wiki.bambulab.com/zh/x1/manual/x1-network-connection-guide
---

## 简介

介绍 X1/X1C 如何接入网络，以及可能遇到的网络问题和解决方法。

## 何时使用

当你不知道如何将X1/X1C连接到网络，或者连接网络的过程中遇到问题时，请查看此文章。

## 适用型号

X1 和 X1C。

## 操作步骤

### 步骤 1：进入设置页面，点击“网络”。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/step-1.jpg)

### 步骤 2：开启无线局域网功能。

打印机会自动检测周围的无线信号，并将它们显示在屏幕上。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/step-2.jpg)

### 步骤 3：选择对应的无线网络，输入密码并点击“连接”。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/step-3.jpg)

连接成功。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/step-4.jpg)

## 故障排除

### 故障 1：打印机无法连接上无线信号

原因及解决方法：

1.路由器距离打印机较远，或者路由器与打印机之间存在较多的障碍物，导致无线信号较弱。请尝试将路由器放置在距打印机较近的位置上，并重新启动路由器。如果不方便移动路由器或者打印机，请开启手机热点，尝试将打印机连接到手机热点。

2.环境中可能存在比较严重的信号干扰，请尝试调整路由器的2.4G无线信道再重新连接。

3.打印机本身无线信号强度可能存在异常，请[点击查看此页面](../maintenance/replace-wifi-antenna.md)的步骤，检查一下WiFi天线的连接是否稳固，可以尝试重新连接几次WiFi天线。如果打印机仍然无法连接上无线信号，请[点击此处提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)并上传打印机日志。

### 故障 2：打印机可以成功连接无线信号，但是无法绑定到Bambu Studio或Bambu Handy

原因及解决方法：

- 路由器网络存在限制，打印机和电脑/手机之间存在隔离。请在电脑上使用CMD工具Ping打印机的IP地址，如果显示的延迟非常高或者无法Ping通打印机IP，请检查路由器网络。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/ping-the-printer.png)

- 打印机无法连接到Bambu云服务器。请[点击此处](../../general/printer-network-ports.md)检查打印机所需要的网络端口是否在路由器上完全开放了，或者尝试将打印机和电脑连接到同一手机热点进行绑定。
- 电脑防火墙阻拦了连接。请关闭电脑上的杀毒软件、防火墙以及VPN等代理软件，然后重新绑定。

### 故障 3：打印机无法刷新二维码

原因及解决方法：

打印机无法正确同步时间，导致屏幕二维码无法刷新。请[阅读此文章](../troubleshooting/hmscode/0500_0200_0002_0008.md)进行检查。

## 结束语

> *我们希望这份指南为您提供了有效的信息，并真实地帮助了您。*
>
> *如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。*
>
> *我们随时准备为您提供帮助并回答您的任何问题。*
>
> [*点击这里提交服务工单*](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
