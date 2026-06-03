---
path: zh/p1/manual/p1-sd-card-network-configuration-guide
title: "P1/A1系列打印机通过micro SD卡配置网络"
description: "本文介绍了如何通过SD卡来配置P1和A1系列打印机的网络"
tags: ["p1", "sd卡", "a1"]
created: 2023-10-24T04:10:30.780Z
updated: 2025-10-27T04:14:35.740Z
source: https://wiki.bambulab.com/zh/p1/manual/p1-sd-card-network-configuration-guide
---

## 适用机型

P1 和 A1 系列打印机。

## P1 系列支持网络连接及模式

1. PIN 码：打印机屏幕显示 6 位 PIN 码，有效期 230 秒，之后会刷新。

2. 通过 SD 卡配置 Wi-Fi：适用于隐藏网络或包含不支持字符的密码。

3. 仅 LAN 模式：打印机仅在本地网络运行；云功能、Bambu Handy 和打印历史将被禁用。

## A1 系列支持网络连接及模式

1. PIN 码：打印机屏幕显示 6 位 PIN 码，有效期 230 秒，之后会刷新。

2. Wi-Fi 连接：在打印机上选择网络，并在屏幕上输入密码。

3. 通过 SD 卡配置 Wi-Fi：适用于隐藏网络或包含不支持字符的密码。

4. 仅 LAN 模式：打印机仅在本地网络运行；云功能、Bambu Handy 和打印历史将被禁用。

## 适用场景

1. 不想使用 Bambu Handy app 给 P1 系列打印机配网；

2. WiFi 密码中有特殊字符，无法在 A1 系列打印机的屏幕上输入；

3. 想将打印机连接到一个隐藏的 WiFi 网络。

## 操作步骤

### 步骤1：准备文件

有两种方法准备这个文件：

#### 方法1：直接新建，并按照格式要求配置您实际使用的网络信息。

新建文档，并修改文件名为“user\_wifi.cfg” 文件名和文件后缀都要按照这个要求。

将以下内容添加到 user\_wifi.cfg文件中。

ssid: 改为你的 WiFi 名

password: 改为你的 WiFi 密码

“:” 后面输入您实际使用的 WiFi 名和 WiFi 密码。

#### 方法2（推荐的方法）：直接下载该文件，并修改示例中的网络信息为您实际使用的网络环境。

点击[此处](https://wiki.bambulab.com/p1/manual/p1-network-configuration-sdcard/user_wifi.cfg)下载文件"user\_wifi.cfg"

将“:” 后面输入你使用的 WiFi 名和 WiFi 密码。

ssid:改为你的 WiFi 名

password:改为你的 WiFi 密码

例如：

![](https://wiki.bambulab.com/p1/manual/p1-network-configuration-sdcard/wifi配置文件.png)

### 步骤2：复制文件，并重启打印机。

将上一步准备的文件复制到 micro SD 卡的根目录下，并在 micro SD 卡插入打印机后，重启打印机。

**注意：**

**1. 为了让配置生效，务必要重启打印机，因为 micro SD 卡配网只在开机时检测配置文件。**

**2. 当前打印机如果已经连接上了其他网络，请先断开当前的网络连接，才可以用这个方法连上特定的网络。**

![](https://wiki.bambulab.com/p1/manual/p1-network-configuration-sdcard/保存到sd卡根目录-2.jpg)

### 步骤3：验证联网是否成功

进入打印机的网络设置界面，检查是否联网成功。如以下 P1 和 A1 屏幕图所示，表示打印机已经连上了名为 “FruitTest08” 的网络。

|  |  |
| --- | --- |
| P1 | A1 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
