---
path: zh/software/bambu-scan/troubleshooting/wireless-connection-failure
title: "无线连接失败的可能原因及解法"
description: ""
tags: []
created: 2026-11-26T14:02:04.721Z
updated: 2026-11-26T14:02:04.721Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/troubleshooting/wireless-connection-failure
---

## 检查网卡状态

将网卡插上电脑后，在 Windows 搜索栏中搜索“设备管理器”。

|  |
| --- |
| 001.png |

打开“设备管理器”，在其他设备中检查是否有“Wireless\_Device”。

|  |
| --- |
| 003.png |

如果有，那么右键进入属性页面，查看相关报错信息。

|  |
| --- |
| 005.png |

若提示驱动未被安装，可重新下载 Bambu Scan 软件，并在安装软件时勾选“安装 Bambu 官方网卡驱动”。

|  |
| --- |
| 007.png |

下载完成后可在“网络适配器”中查看到正确的网卡信息。

|  |  |
| --- | --- |
| 009.png | 010.jpg |

## 网卡驱动无法安装

若参考上述步骤，重新安装网卡驱动后，设备依然提示“驱动程序未被安装”。请检查该 Windows 账户是否具备管理员权限，需要管理员权限才能正确安装驱动。

## 更新固件

若网卡能够正常使用，那么无线连接失败的原因可能是扫描仪固件版本过低，请使用有线连接升级固件，再尝试无线连接。

## Windows 定位服务

Windows 目前依赖于定位服务来发现 Wifi 设备，请打开定位服务选项后重试。<https://support.microsoft.com/zh-cn/windows/privacy/windows-location-service-and-privacy>

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
