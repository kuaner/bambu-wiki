---
path: zh/x1e/maintenance/how-to-use-internet-cable
title: "如何使用网线接口连接打印机"
description: "本文将介绍如何使用网线连接电脑和打印机。"
tags: ["h2d pro", "x1e"]
created: 2026-07-16T02:01:58.056Z
updated: 2026-07-16T02:48:16.105Z
source: https://wiki.bambulab.com/zh/x1e/maintenance/how-to-use-internet-cable
---

## 何时使用：

对于不想使用 Bambu Lab 云服务的用户，我们提供局域网模式以便用户使用，而 X1E/H2D Pro 设备可以使用网线实现局域网通信，实现本地打印与监控。

## 所需材料

- 一台可以连接网线的计算机
- X1E/H2D Pro

## X1E

### 1. 网线连接打印机与计算机

计算机若需联网，那么还需要一个额外的有/无线网卡。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/1.png)

### 2. 设置计算机为局域网网关

点击设置->网络和Internet->高级网络设置。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/2.png)

网络适配器->打印机所连接的网口所在的网卡->更多适配器选项。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/3.png)

属性->IPv4属性

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/5.png)

手动设置 IP 地址，将计算机的 IP 地址设置为网关地址。  
这里的 IP 地址理论上可以设置任何 IPv4 地址，但我们强烈建议使用私有地址(见下表)。设置时注意避免使用计算机上连接的其他网络已使用的网段，且计算机上不要配置该网络网段与其他网段的路由。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/4.png)

需要注意，如果打印机启动了无线网络连接，在设置 IP 地址时需要避开无线网络的网段避免造成冲突。

### 3. 设置打印机 IP 地址

根据此前设置的IP和子网掩码设置打印机地址，该例中使用的192.168.2网段，故打印机设置为192.168.2.2。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/6.jpg)

### 4. 启动局域网模式

打印机设置->通用 菜单中启动仅局域网选项。  
启动该选项后打印机将生成访问码，在下一步连接打印机时需要用到。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/7.jpg)

### 5. 连接打印机

在 Bambu Studio 的设备页面下点击 + 号添加打印机。  
在其他设备中找到所需连接的打印机，输入访问码。连接成功后即可在局域网模式下操作和监控打印机。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/8.png)

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/9.png)

## H2D Pro

### 所需工具

- 一台可以连接互联网且拥有至少两张网卡的电脑，如带有有线网口且可连接无线网的笔记本电脑

### 操作指南

1. 将笔记本电脑连接到互联网
2. 进入笔记本网络适配器设置  
   设置->网络和Internet->高级网络设置->更多适配器设置。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/10.png)  
3. 在适配器属性中启动Internet连接共享

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/11.png)

此时 Windows 应启动了一个本地的 DHCP 服务器，并将网络从计算机上的另一个网卡进行分享。该设置可以通过检查另一个网络适配器的 IP 地址确定，此时另一网络适配器的默认IP地址为192.168.137.1。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/12.png)  
4. 打印机端设置自定义 IP

在满足了 DHCP 服务器和网络连接后，即可手动设置 IP 地址。在自定义菜单中将 IP 地址、默认网关等设置为需要的地址即可。

![](https://wiki.bambulab.com/x1e/how-to-use-internet-cable/13.png)

5. 关闭 Internet 连接共享  
   若打印机需要离线运行，在打印机 IP 设置完成后即可从 Windows 设置中关闭 Internet 连接共享。注意在关闭连接共享后，连接到打印机的网卡IP将从 192.168.137.1 变更为自动。如需继续使用该网卡连接打印机，则连接步骤与 X1E 相同。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
