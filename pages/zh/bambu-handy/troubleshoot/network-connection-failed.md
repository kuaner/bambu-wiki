---
path: zh/bambu-handy/troubleshoot/network-connection-failed
title: "Bambu Handy 无法连接网络（iOS 系统）"
description: "本文将介绍当使用 iOS 系统时，Bambu Handy 连接网络失败的排查指引"
tags: ["bambu handy"]
created: 2024-11-01T01:12:15.768Z
updated: 2024-11-09T00:22:16.280Z
source: https://wiki.bambulab.com/zh/bambu-handy/troubleshoot/network-connection-failed
---

## 问题现象

Bambu Handy提示无法连接服务器或者无法加载任何内容。

|  |  |
| --- | --- |
|  |  |

## 原因

1.Bambu 云服务异常。  
2.手机网络异常或者 APP 网络权限设置错误。  
3.**iOS 系统方面存在一些遗留问题**，可能会导致部分 APP 更新后无法连接网络。

## 排查指引

### 检查 Bambu 系统状态

如果Bambu云服务存在异常，除了 Bambu Handy 可能会出现无法连接服务器的问题，Bambu Studio 也会出现同样的情况。可以在[该页面](https://status.bambulab.com/)可以查看 Bambu 云服务器的状态。

### 检查手机和 Bambu Handy 的网络设置

1. 确保手机已经连接到互联网，并且 Bambu Handy 的网络权限也正确开放。  
   点击 **设置** > **Bambu Handy** > **无线数据** > 选择**无线局域网与蜂窝数据**。

|  |  |
| --- | --- |
|  |  |

2. 检查手机是否开启了VPN或者其他第三方安全软件。请关闭这些软件再尝试重新连接。
3. 检查Bambu Handy是否已经更新到了最新版本。更新到最新版本后再重试重新连接。

### 检查手机的时间设置

确保手机上的日期和时间已根据你所在的时区进行了正确设置。如果日期和时间不正确，请更新这一信息，或打开用于自动设置日期和时间的选项。  
点击 **设置** > **通用** > **日期与时间**。  
![日期和时间.jpg](https://wiki.bambulab.com/bambu-handy/troubleshooting/network-connection-failed/%E6%97%A5%E6%9C%9F%E5%92%8C%E6%97%B6%E9%97%B4.jpg)

### 还原手机的网络设置

完成上述检查后，Bambu Handy仍然无法正常连接，请更新手机系统到最新版本，并还原手机的网络设置。  
点击 **设置** > **通用** > **传输或还原 iPhone** > **还原** > **还原网络设置**。

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](hhttps://support.bambulab.cn/cn/im)
