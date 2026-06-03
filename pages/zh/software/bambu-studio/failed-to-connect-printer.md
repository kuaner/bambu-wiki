---
path: zh/software/bambu-studio/failed-to-connect-printer
title: "Bambu Studio 连接打印机失败"
description: "简要说明如何解决设备连接问题。"
tags: []
created: 2023-03-14T13:31:01.089Z
updated: 2026-01-12T03:08:28.843Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/failed-to-connect-printer
---

## 找不到我的设备

### 在“我的设备”中无法找到设备

#### 显示界面

如果您的设备没有连接成功，在 Bambu Studio 软件界面中 “设备” → “我的设备” 那一栏中将会如下图所示：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/1_%E6%88%91%E7%9A%84%E8%AE%BE%E5%A4%87.jpg)

又或者是，当您在 Bambu Studio 中发起打印任务时可能会出现找不到打印机的情况：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/8_%E6%89%BE%E4%B8%8D%E5%88%B0%E6%89%93%E5%8D%B0%E6%9C%BA.jpg)

#### 解决办法

1. 请确认您是否已经**成功登录**进 Bambu Studio 中；

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/2_%E5%B7%B2%E7%99%BB%E5%BD%95.jpg)

2. 并且选中了正确的**登录区域。**例如，您可以根据下图中提示的位置找到更改登录区域的位置，或者快捷键 **Ctrl + P** 调出**偏好设置**面板。

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/3_%E8%AE%BE%E7%BD%AE%E5%9C%B0%E5%8C%BA.jpg)

3. 您也可以选择用官方的 Bambu Handy 这个 APP 扫描设备中的二维码，并登录您的账号（如下图中以 A1 设备的界面为例）。

另外，请确保您在设备中的账号名字与 Bambu Studio 中的账号名字保持一致。

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/5_%E6%89%8B%E6%9C%BA%E7%BB%91%E5%AE%9A%E6%89%93%E5%8D%B0%E6%9C%BA.jpg)

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/4_%E6%89%AB%E6%8F%8F%E9%93%BE%E6%8E%A5%E8%AE%BE%E5%A4%87.jpg)

一旦登录成功，您的设备将会出现在“我的设备”这一栏：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/13_%E9%93%BE%E6%8E%A5%E6%88%90%E5%8A%9F.jpg)

### 在“其他设备”中无法找到设备

#### 显示界面

如果您的设备没有连接成功，在 Bambu Studio 软件界面中 “设备” → “其他设备” 那一栏中将会如下图所示：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/6_%E5%85%B6%E4%BB%96%E8%AE%BE%E5%A4%87.jpg)

当您处于未登录的状态，但与 Bambu Studio 处于同一局域网下的时候，（A1）打印机的界面中如下图显示：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/14_%E5%B1%80%E5%9F%9F%E7%BD%91_-1.jpg)

#### 解决办法

您可以检查一下您计算机中 “系统和安全” → “ Windows Defender 防火墙设置” 中的设置，请确保 Bambu Studio 被允许使用网络。

如果调整过后仍然失败，可以尝试关掉防火墙。

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/7_%E9%98%B2%E7%81%AB%E5%A2%99.jpg)

当设置完成后您可以再次打开 Bambu Studio, 这时，您应该可以看到设备出现在“其他设备”中。

这时您可以点选设备并登录。

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/6-1%E5%85%B6%E4%BB%96%E8%AE%BE%E5%A4%87_%E5%B7%B2%E6%8E%A5%E4%B8%8A.jpg)

> **注意**：如果在网络正常的情况下仍然无法连接，请考虑再次检查您的 **Bambu Handy**，有可能是您在 APP 上解除了与打印机的绑定。

## 无法连接打印机

> **注意：** 需要使用同一个账号登录打印机，Bambu Handy 和 Bambu Studio 才能互相发起打印。

如果出现如下图所示的报错：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/9_%E7%BD%91%E7%BB%9C%E6%8A%A5%E9%94%99.jpg)

这表示 Bambu Studio 在一定时间内（超时 30 秒）无法接收打印机状态信息，请通过点击打印机名称前的圆形图标检查打印机的连接状态，系统将会自动尝试再次连接设备，如下图所示：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/10_%E5%B0%9D%E8%AF%95%E8%BF%9E%E6%8E%A5.jpg)

您可以在“设置” → “Wi-Fi” 界面中再次确认打印机的网络是否连接正常（如下图 H2D 设备中的截图所示）。并且确认主屏幕上没有 MQTT 错误（即在使用 MQTT 协议进行通信时出现的问题或异常）。

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/11_%E7%BD%91%E7%BB%9C%E6%AD%A3%E5%B8%B8_h2d.jpg)

## 无法连接服务器

如果您出现如下图的情况：

![](https://wiki.bambulab.com/bambu-studio/failed-to-connect-printer/12_-_1%E6%97%A0%E6%B3%95%E8%BF%9E%E6%8E%A5%E5%88%B0%E6%9C%8D%E5%8A%A1%E5%99%A8.jpg)

这意味着 Bambu Studio 无法连接到云服务器，请检查计算机的网络连接和防火墙设置。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
