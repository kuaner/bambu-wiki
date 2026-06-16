---
path: zh/cyberbrick/troubleshooting/unable-connect-control-board
title: "CyberBrick 无法通过手机或电脑连接多功能主控板"
description: "本页面提供 CyberBrick 无法通过手机或电脑连接多功能主控板的故障排查指南，涵盖检查蓝牙名称、避免多设备同时连接及确保稳定供电的步骤。"
tags: []
created: 2025-06-26T13:26:16.117Z
updated: 2026-06-05T09:59:00.552Z
source: https://wiki.bambulab.com/zh/cyberbrick/troubleshooting/unable-connect-control-board
---

## 现象

当使用手机或电脑连接多功能主控板板时，出现连接失败的报错。

![failed_to_connect-cn.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/unable-connect-control-board/failed_to_connect-cn.png)

## 故障排查

您可以参考下述方案来进行故障排查。

### 步骤 1：检查多功能主控板的蓝牙名称

延时摄影固件无法通过手机/电脑来进行绑定，如果需要使用延时摄影套件功能，请参考[延时摄影套件 使用指南](../../makerworld/cyberbrick/example-projects/time-lapse.md)。

延时摄影固件的蓝牙名称为：

- 1.0.3.2及以上版本的延时摄影固件的蓝牙名称为：**CyberBrick-xxxx**
- 1.0.3.2 版本以下的延时摄影固件的蓝牙名称为：**BBL\_SHUTTER**

遥控固件的蓝牙名称为：

- 1.0.3.2 及以上版本的遥控固件的蓝牙名称为：**CyberBrick-xxxx**
- 1.0.3.2 版本以下的遥控固件的蓝牙名称为：**RC\_MODULE**

### 步骤 2：检查电脑和手机是否在同时连接多功能主控板

**目前不支持电脑/手机同时连接多功能主控板。**

如果您曾经使用电脑连接过多功能主控板，请在电脑上关闭蓝牙或在蓝牙列表中删除该设备，再重新使用手机来连接。

注：如果您是电脑无法连接多功能主控板，请检查电脑是否有蓝牙。多功能主控板与电脑也是通过蓝牙连接，不是通过数据线（com 口）来连接。

### 步骤 3：检查多功能主控板的供电

**电源供电不稳定也可能导致与手机/电脑连接失败。**

您可以依次使用下述三种供电方式：

1. 使用全新的碱性电池；
2. 将锂电池充满电；
3. 单独拆下多功能主控板，用 Type-C 线供电；

![主控.png](https://wiki.bambulab.com/cyberbrick/troubleshooting/unable-connect-control-board/%E4%B8%BB%E6%8E%A7.png)

然后重启手机蓝牙尝试连接：

1. 如果设备可以连接，问题可能是电源不稳定所致。建议更换全新的碱性电池，或为锂电池充满电后再尝试连接。
2. 如果无法连接，请尝试使用其他手机重新配对设备。
3. 若仍无法连接，可使用 CyberBrick USB 升级工具将核心板恢复至出厂固件后再尝试。

请参考[CyberBrick USB 升级工具指南](wired-firmware-guide.md) 了解如何使用 USB 升级工具。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
