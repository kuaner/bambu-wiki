---
path: zh/knowledge-sharing/access-code-connect
title: "如何使用访问码连接打印机"
description: "本文介绍了如何使用访问码连接打印机"
tags: []
created: 2026-01-12T04:09:24.490Z
updated: 2026-08-28T06:36:17.651Z
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

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
