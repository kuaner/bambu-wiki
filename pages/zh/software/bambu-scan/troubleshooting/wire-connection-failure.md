---
path: zh/software/bambu-scan/troubleshooting/wire-connection-failure
title: "有线连接失败的可能原因及解法"
description: ""
tags: []
created: 2026-11-26T14:01:56.417Z
updated: 2026-11-26T14:01:56.417Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/troubleshooting/wire-connection-failure
---

## 1.检查硬件连接

使用原装线缆连接扫描仪和电脑后，在 Windows 搜索栏中搜索“设备管理器”。

|  |
| --- |
| 001.png |

打开后，在“通用串行总线设备”下检查是否有 Bambu Lab S1。

|  |
| --- |
| 003.png |

若此处无法显示 Bambu Lab S1，说明扫描仪和电脑的连接存在异常。

#### 可能的原因：

1. 设备电量耗尽，已关机。
2. 使用了拓展坞或转接线。
3. 线缆故障。
4. 电脑或扫描仪的 Type-C 口损坏。

## 2.检查杀毒软件设置

如果上一步 Windows 能够发现 Bambu Lab S1，那么软件无法通过有线连接绑定扫描仪，就可能是杀毒软件导致的异常。

建议关闭后台的杀毒软件后，重新连接线缆并尝试绑定，若依然无法绑定成功，请联系客户支持团队。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
