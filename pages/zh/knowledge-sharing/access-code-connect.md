---
path: zh/knowledge-sharing/access-code-connect
title: "如何使用访问码连接打印机"
description: "本文介绍了如何使用访问码连接打印机"
tags: []
created: 2026-01-12T04:09:24.490Z
updated: 2026-01-15T10:07:51.314Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/access-code-connect
---

使用 Bambu Studio 连接局域网模式下的打印机，包含两种连接方式：

- 常规方式：当电脑与打印机连接同一 WiFi 时，在 Studio 中输入**访问码**即可连接打印机；
- 特殊方式：适用于特殊网络环境（如打印机与电脑分属不同 VLAN、网段不同）或防火墙拦截通信的场景，需同时输入**打印机 IP 和访问码**实现绑定。

> 本文以 H2 系列的屏幕操作为例，其他机型的操作步骤一致。

## 打印机开启局域网模式

- 进入设置页面，点击 **设置 > 仅局域网**；

|  |  |
| --- | --- |
|  |  |

- 开启“仅局域网”模式，并根据需求选择是否开启局域网模式实况。

|  |  |
| --- | --- |
|  |  |

## 使用访问码连接打印机

### 常规网络环境（打印机和电脑连接同一 WiFi，处于同一局域网）

- 将电脑和打印机连接同一个 WiFi；
- 在 Bambu Studio 中点击设备，打开“设备”页面下弹出的打印机列表，找到已切换为“仅局域网”模式的打印机，仅局域网模式下的打印机名称前面会有一个锁定图标，如下图所示；

> 注意：该过程可能需要 20-60 秒，极少数情况下耗时可能更长，请您耐心等待。若打印机长时间仍未显示，需检查打印机与 Bambu Studio 是否处于同一本地网络，且两者间通信未被拦截（该问题可能出现在部分访客网络环境中）。

![device.png](https://wiki.bambulab.com/knowledge-sharing/lan-mode/device.png)

- 输入打印机访问码并单击“确认”。

![访问码.png](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E8%AE%BF%E9%97%AE%E7%A0%81.png)

### 特殊网络环境（打印机与电脑分属不同 VLAN、网段不同）

- 在“仅局域网”页面中查看打印机 IP 和访问码；

![局域网模式.png](https://wiki.bambulab.com/knowledge-sharing/access-code/%E5%B1%80%E5%9F%9F%E7%BD%91%E6%A8%A1%E5%BC%8F.png)

- 在 Bambu Studio 中点击设备，点击“无打印机 > 通过访问码绑定”；

![access_code-.png](https://wiki.bambulab.com/knowledge-sharing/access-code/access_code-.png)

- 输入打印机 IP 和访问码并单击“连接”。

![连接.png](https://wiki.bambulab.com/knowledge-sharing/access-code/%E8%BF%9E%E6%8E%A5.png)

> **注意：** 出于隐私保护需求，Bambu Studio 不会存储用户的打印机 IP 信息。因此，采用 IP + 访问码进行绑定时，**每次重启 Studio 后都需要重新输入这两项信息完成绑定**；若仅通过访问码连接打印机，则可避免该问题。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
