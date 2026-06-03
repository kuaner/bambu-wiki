---
path: zh/x1/troubleshooting/upgrade-fail
title: "X1 系列升级失败"
description: "本指南介绍X1 系列打印机固件升级失败的表现、原因和解决方法。"
tags: ["x1"]
created: 2024-11-18T08:04:43.294Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/upgrade-fail
---

## 固件升级原理

对于联网的打印机，当云端检测到打印机的固件版本不是最新时，将向设备推送更新通知。一旦用户选择了升级，打印机便会从云端下载固件。随后，打印机的主电路板会对各关键部件电路板的型号进行检查，并专门推送并接收各关键部件电路板的数据，以确保升级顺利进行。

![x1.jpg](https://wiki.bambulab.com/a1/troubleshooting/upgrade-failed/x1.jpg)

## 故障现象

升级进度无法到达 100%，例如：0%，34%，97%。

|  |  |
| --- | --- |
|  |  |

## 故障原因

常见的固件升级失败的原因有：

- 网络连接异常或 MicroSD 卡存储空间不足，导致固件下载失败
- TH 模块的 USB-C 信号线未插好
- AMS 信号线未插好
- AP 板、MC 板、TH 板硬件故障

## 故障排除

> 用户可视情调整各排故措施的顺序。

1. 检查并排除网络异常  
   **请参考**：[HMS\_0500-0200-0002-0008 时间同步失败](hmscode/0500_0200_0002_0008.md)

- 恢复出厂设置后重启打印机
- 切换至其他无线网络或使用 2.4G 手机热点
- NTP 服务连接测试

2. 检查 MicroSD 卡存储空间，若空间不足，MicroSD 卡格式化后重试。
3. 拔插 TH 板与 AP 间的 USB-C 线、AMS 与机器的连接线后重试。

- 拔插 USB-C 线，参考：[USB-C 线安装](../maintenance/replace-typec-cable.md)
- 拔插 AMS-缓冲器-打印机的连接线，参考：[连接 AMS 到 P1 系列](../../p1/manual/connect-ams.md)

4. 尝试断开 AMS 先升级打印机，再连接 AMS 升级。

- 若打印机升级成功而 AMS 失败，可能是 AMS 与打印机间连接异常或 AMS 主板坏了。

5. 若以上措施均无法解决问题，请[提交工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并上传打印机日志。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
