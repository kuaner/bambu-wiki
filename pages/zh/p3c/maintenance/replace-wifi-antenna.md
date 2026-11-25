---
path: zh/p3c/maintenance/replace-wifi-antenna
title: "P3C WiFi 天线更换指南"
description: "本文介绍了如何更换 P3C WiFi 天线"
tags: []
created: 2026-11-24T14:06:12.022Z
updated: 2026-11-24T14:06:12.022Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-wifi-antenna
---

## WiFi 天线

简述：WIFI 天线是用于增强无线网络信号电子配件，安装在打印机上盖组件左内侧并连接至 AP 板。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-wifi-antenna/zh/001.png)

## 何时更换

1. WIFI 天线线缆或连接器损坏；
2. WIFI 信号不稳定或较弱，且 Bambu Lab 服务团队通过 log 分析确认是 WIFI 天线的问题。

## 所需工具和材料

- 镊子
- H2.0 内六角扳手
- Wi-Fi 天线

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 本指南是在已移除 AMS 3P 的情况下进行的，操作前请参考 WiKi：[AMS 3P 拆装指南](replace-ams3p.md) 取下 AMS 3P。

## 移除 WiFi 天线

### 步骤 1. 移除左侧板

请您参考WIKI：[P3C 左侧板/右侧板更换指南](replace-side-panel-left.md)，完成左侧板的移除。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-wifi-antenna/zh/002.png)

### 步骤 2. 移除 WiFi 天线

使用镊子清理干净 Wifi 天线插头上的白胶，然后断开 Wifi 天线。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-wifi-antenna/zh/003.png)

将线缆从上盖线扣中取出，并撕掉 WiFi 天线贴纸，移除 WiFi 天线。

|  |  |
| --- | --- |
| 004.png | 005.png |

## 安装 WiFi 天线

### 步骤 1. 安装 WiFi 天线

将 WiFi 天线粘贴到原处，随后将线缆卡入上盖组件右图示的线扣中；

|  |  |
| --- | --- |
| 006.png | 007.png |

按压 WiFi 天线插头，将插头装入 AP 板插座中。（电子硅胶主要用于运输过程中确保插头的稳定连接，重新安装无需再涂抹硅胶）

![008.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-wifi-antenna/zh/008.png)

### 步骤 2. 安装左侧板

请您参考WIKI：[P3C 左侧板/右侧板更换指南](replace-side-panel-left.md)，将左侧板装回。

![009.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-wifi-antenna/zh/009.png)

## 功能验证

连接电源线并打开电源，通过 APP 连接打印机，确认打印机能正常检测到 WIFI 信号并能完成连接。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
