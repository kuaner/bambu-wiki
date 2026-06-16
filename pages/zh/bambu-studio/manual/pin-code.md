---
path: zh/bambu-studio/manual/pin-code
title: "如何在 Bambu Studio 中使用 Pin 码绑定打印机"
description: "介绍在 Bambu Studio 中使用 Pin 码绑定打印机的详细步骤"
tags: ["bambu studio"]
created: 2024-04-22T02:38:55.014Z
updated: 2026-06-02T02:29:29.896Z
source: https://wiki.bambulab.com/zh/bambu-studio/manual/pin-code
---

## 功能介绍

只要不同网络之间的必要接口和协议能够互相通信，即可在 Bambu Studio 中通过使用 Pin 码绑定打印机，不再限制打印机和电脑必须连接同一局域网。

## 注意事项

### 固件支持

- H、P、A系列打印机支持PIN码绑定。
- X1 系列打印机暂时不支持此功能，请等待固件更新。

> 注意：如果您的打印机屏幕没有出现 Pin 码，可能是网络故障导致，请联系[拓竹客户支持](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)

### 不同网络之间的必要设置

| 应用 | 接口 | 协议类型 | 模式 |
| --- | --- | --- | --- |
| http API | 80/443/8080 | TCP | Cloud mode |
| mqtt | 8883 | TCP | Cloud mode |
| Remote video | 8000/21047/10001 | TCP | Cloud mode |
| Remote video | 10001-10512 | UDP | loud mode |
| Device binding | 3000 | TCP | Cloud mode |
| Device discovering | 1990/2021 | SSDP. multicast/broadcast | Cloud/LAN mode |
| LAN mode MQTT | 8883 | TCP | LAN mode |
| LAN mode FTP | 990/50000~50100 | TCP | LAN mode |
| LAN mode video | 6000 | TCP | LAN mode |
| NTP | 123 | TCP/UDP | Cloud/LAN mode |

## 操作步骤

### P1 系列

步骤 1. 打开打印机。

步骤 2. 选择“**设置 > 账号**”。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/acccount-cn.png)

步骤 3. 选择区域信息后等待 Pin 码刷新。请记住此 Pin 码用于后续步骤。

> 每个 Pin 码的有效时间为 230 秒，超过时间后会自动重新刷新。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/region-cn.png)

步骤 4. 打开 Bambu Studio 软件，**登录您的帐户**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/studio-login-cn.png)

步骤 5. 单击“设备”标签，在设备列表界面中，单击“**通过 Pin 码绑定**”。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-with-pin--code.png)

步骤 6. 输入 Pin 码，单击**确定**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-with-pin-code--2.png)

步骤 7. 在屏幕上选择"绑定"。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/printer-bind-cn.png)

如果 Pin 码输入正确且在有效期内，Bambu Studio 将成功完成与打印机的绑定。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/studio-success-cn.png)

### A 系列

步骤 1. 打开打印机。

步骤 2. 选择“**设置 > 账号**”。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/a1-series-pincode-1.png)

步骤 3. 选择区域信息后等待 Pin 码刷新。请记住此 Pin 码用于后续步骤。

> 每个 Pin 码的有效时间为 230 秒，超过时间后会自动重新刷新。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/a1-series-pincode-4.png)

步骤 4. 打开 Bambu Studio 软件，**登录您的帐户**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/studio-login-cn.png)

步骤 5. 单击“设备”标签，在绑定界面中，单击“**通过 Pin 码绑定**”。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-with-pin--code.png)

步骤 6. 输入 Pin 码，单击**确定**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-with-pin-code--2.png)

步骤 7. 在屏幕上点击"绑定"。

![bind-on-a1.png](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-on-a1.png)

如果 Pin 码输入正确且在有效期内，Bambu Studio 将成功完成与打印机的绑定。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/studio-success-cn.png)

### H2 系列及 P2S 打印机

步骤 1. 打开打印机。

步骤 2. 点击“登陆”。

![login.png](https://wiki.bambulab.com/bambu-studio/manual/pin-code/login_zh.png)

步骤 3. 选择区域信息后等待 Pin 码刷新。请记住此 Pin 码用于后续步骤。

> 每个 Pin 码的有效时间为 230 秒，超过时间后会自动重新刷新。

![pincn.png](https://wiki.bambulab.com/bambu-studio/manual/pin-code/pin_zh.png)

步骤 4. 打开 Bambu Studio 软件，**登录您的帐户**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/studio-login-cn.png)

步骤 5. 单击“设备”标签，在绑定界面中，单击“**通过 Pin 码绑定**”。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-with-pin--code.png)

步骤 6. 输入 Pin 码，单击**确定**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/bind-with-pin-code--2.png)

步骤 7. 在屏幕上点击"允许"，完成绑定。

![allowcn.png](https://wiki.bambulab.com/bambu-studio/manual/pin-code/allowcn.png)

## **结束语**

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
