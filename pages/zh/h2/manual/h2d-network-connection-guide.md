---
path: zh/h2/manual/h2d-network-connection-guide
title: "H2 系列/ X 系列/ P2S 打印机网络连接指南"
description: ""
tags: []
created: 2025-06-18T07:56:09.512Z
updated: 2026-04-15T03:13:12.372Z
source: https://wiki.bambulab.com/zh/h2/manual/h2d-network-connection-guide
---

## 何时使用

当您首次使用 H2 系列打印机或 P2S、X 系列打印机时，可参考本文为设备连接无线网络。

## 适用型号

- H2 系列打印机
- P2S 打印机
- X 系列打印机

## 支持模式

**Wi-Fi：** 在打印机上选择无线网络，并在屏幕上输入密码连接。

[**仅局域网模式**](../../knowledge-sharing/enable-lan-mode.md)：打印机仅在本地网络中运行，云端功能、Bambu Handy 和打印历史将不可用。

## 操作步骤

### 步骤 1：进入设置页面，点击“网络”。

![](https://wiki.bambulab.com/h2/manual/h2d-network-connection-guide/1.jpg)

### 步骤 2：开启无线局域网功能。

打印机会自动检测周围的无线信号，并将它们显示在屏幕上。

![](https://wiki.bambulab.com/h2/manual/h2d-network-connection-guide/2-.jpg)

### 步骤 3：选择对应的无线网络，输入密码并点击“OK”连接。

![](https://wiki.bambulab.com/h2/manual/h2d-network-connection-guide/3-.jpg)

过一段时间后，打印机屏幕将提示您连接成功，点击 **OK** 即可。

![](https://wiki.bambulab.com/h2/manual/h2d-network-connection-guide/4.jpg)

## 故障排除

### 故障 1：打印机无法连接上无线信号

原因及解决方法：

- 路由器距离打印机较远，或者路由器与打印机之间存在较多的障碍物，导致无线信号较弱。请尝试将路由器放置在距打印机较近的位置上，并重新启动路由器。如果不方便移动路由器或者打印机，请开启手机热点，尝试将打印机连接到手机热点，以测试是否是由于路由器距离较远引起。
- 环境中可能存在比较严重的信号干扰，请尝试调整路由器的2.4G无线信道再重新连接。
- 打印机本身无线信号强度可能存在异常，检查WiFi天线的连接是否稳固，可以尝试重新连接几次WiFi天线。可参考以下文档。

[更换 H2 系列 Wifi 天线](../maintenance/replace-wifi-antenna.md)  
[更换 P2S Wifi 天线](../../p2s/maintenance/replace-wifi-antenna.md)  
[更换 X1 Wifi 天线](../../x1/maintenance/replace-wifi-antenna.md)

- 如果打印机仍然无法连接上无线信号，请[点击此处提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)并上传打印机日志。

### 故障 2：打印机可以成功连接无线信号，但是无法绑定到Bambu Studio或Bambu Handy

原因及解决方法：

- 由于路由器的网络设置，打印机可能与电脑或手机隔离，导致无法通信。这种情况常发生在启用了“客户端隔离”的访客网络上。

在开始菜单搜索 **“cmd”**，打开命令提示符。输入 `ping <打印机 IP>`，查看是否能够连通。

如果出现请求超时、丢包或延迟过高，请调整路由器/AP 设置，使同一网络下的设备可以互相通信。例如，将打印机和电脑/手机移动到主网络，或在该网络上关闭“客户端隔离”。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/ping-the-printer.png)

- 打印机无法连接到Bambu云服务器。请[点击此处](../../general/printer-network-ports.md)检查打印机所需要的网络端口是否在路由器上完全开放了，或者尝试将打印机和电脑连接到同一手机热点进行绑定。
- 电脑防火墙阻拦了连接。请关闭电脑上的杀毒软件、防火墙以及VPN等代理软件，然后重新绑定。

### 故障 3：打印机无法刷新二维码

原因及解决方法：

打印机无法正确同步时间，导致屏幕二维码无法刷新。请[阅读此文章](../../x1/troubleshooting/hmscode/0500_0200_0002_0008.md)进行检查。

## 结束语

> *我们希望这份指南为您提供了有效的信息，并真实地帮助了您。*
>
> *如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。*
>
> *我们随时准备为您提供帮助并回答您的任何问题。*
>
> [*点击这里提交服务工单*](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
