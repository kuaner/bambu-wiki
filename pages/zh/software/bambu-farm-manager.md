---
path: zh/software/bambu-farm-manager
title: "拓竹农场管家软件快速入门"
description: "本文介绍了拓竹农场管家软件。"
tags: []
created: 2024-10-24T10:07:33.966Z
updated: 2026-08-03T04:27:56.901Z
source: https://wiki.bambulab.com/zh/software/bambu-farm-manager
---

## 软件介绍

“拓竹农场管家”是一款为多打印机管理而设计的应用套件。它支持打印状态实时展示，批量控制，打印机固件升级，打印队列管理和多用户管理等功能，可帮助您优化工作流程，提高生产效率。

- 本套件包含“农场管家服务器”（简称为“服务器”）和“农场管家客户端”（简称为“客户端”）两个应用软件。

![ch.jpg](https://wiki.bambulab.com/software/bambu-farm-manager/ch.jpg)

- 服务器作为中央管理平台，负责连接并控制局域网内的打印机。客户端提供一个用户友好的监控与管理页面。支持团队成员同时访问服务器，实现高效的工作协同。
- 服务协议：[拓竹农场管家服务协议](https://bambulab.cn/zh-cn/policies/bambu-farm-manager-service-agreement)。

## 系统与网络要求

- Windows10 或更高版本操作系统。
- 使用 X86 指令集 64 位处理器的电脑或平板。
- 打印机使用 2.4G WIFI 接入局域网。
- 服务器需要与打印机部署在同一个局域网中，或二者可基于 IP 地址通信（如同路由器下的不同子网）。
- 客户端需要与服务器部署在同一局域网中，或二者可基于 IP 地址通信。
- 客户端需要具备公网访问能力，服务器激活，打印机校验和固件下载等通信需求。

## 适配机型及版本要求

- H2C：01.02.00.00 及以上
- H2D：V01.02.00.00 及以上
- H2D Pro: V01.01.00.00 及以上
- H2S: V01.02.00.00 及以上
- X2D: V01.01.00.00 及以上
- X1C: V01.09.00.00 及以上
- X1E：V01.01.03.12 及以上
- P2S: V01.02.00.00 及以上
- P1P/P1S: V01.07.00.00 及以上
- A1/A1mini: V01.04.00.00 及以上
- A2L：V01.00.03.00 及以上

## 下载最新版本

[拓竹农场管家服务器 02.04.00.03](https://public-cdn.bblmw.cn/upgrade/farm-manager/Bambu_Farm_Manager_Server_win-v02.04.00.03-20260731111311.exe)

[拓竹农场管家客户端 02.04.03](https://public-cdn.bblmw.cn/upgrade/farm-manager/bambu-farm-manager-client-v2.4.3-12ed15b8-win32-x64.exe)

## 安装

“拓竹农场服务器”和“拓竹农场客户端”安装后，电脑桌面上会创建对应图标。服务器运行与激活状态可在任务托盘中。

|  |  |
| --- | --- |
| 桌面快捷方式 | windows 托盘中显示服务器运行状态 |

## 激活

1. 首次使用时，需要激活服务器来获取使用授权。在“服务器发现界面”，点击**激活**。

![image_(24).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(24).png)

2. 选择登录区域 “中国大陆”，使用 bambulab 账号（手机号）完成登录。

![image_(25).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(25).png)

3. 在“激活和设置页面”，可修改服务器的初始配置，如服务器名称，是否开启错峰启动（**A1 mini由于热床加热功耗小，并不会受到热床同步加热配置的限制**）。这里必须配置本地管理员账号和密码，请妥善保管该信息，后续需要使用本地账号访问农场服务器。

![image_(26).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(26).png)

## 添加打印机

添加打印机前需要检查：打印机固件版本已升级到目标版本；打印机已与 Bambu Handy 解绑, 打印机账号显示为“登出状态”；打印机局域网模式为关闭状态。  
![image_(27).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(27).png)

“查找附近的打印机”：服务器可自动查找同一路由器（或同一IP网段内）下的打印机。

![image_(28).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(28).png)

“配置IP查找范围”：若打印机与服务器部署在不同的子网，可配置IP范围，进行主动查找。

![image_(29).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(29).png)  
![image_(30).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(30).png)

## 修改打印机名称

打印机添加后，可在主页面查看到该打印机。  
![image_(30).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(31).png)

点击右侧 “详情” 按钮，可修改打印机名称及查看设备信息。  
![image_(30).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(32).png)

## 设置打印机分组

您可以通过标签功能对打印机进行分组管理。只需点击“编辑标签”，即可输入标签名称并将其分配给相应的打印机。  
![image_-_2024-12-30t155022.036.png](https://wiki.bambulab.com/software/bambu-farm-manager/image_-_2024-12-30t155022.036.png)  
![image_(34).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(34).png)

## 上传 gcode.3mf 文件

在 Bambu Studio 中，您可以利用“导出单盘切片文件”功能将切片文件保存至您的电脑目录。随后，通过客户端软件，可以将这些切片添加到农场管家文件存储目录中（请注意，目前仅支持上传单盘切片文件）

![image_-_2024-12-30t140712.940.png](https://wiki.bambulab.com/software/bambu-farm-manager/image_-_2024-12-30t140712.940.png)  
![image_(34).png](https://wiki.bambulab.com/software/bambu-farm-manager/image_(36).png)

## 发起打印

- 创建任务并选择“直接打印”，可快速启动一台或多台打印机开始执行任务。
- “直接打印”模式下，仅空闲态打印机可被选择。
- 仅机型和喷嘴直径与切片文件兼容的打印机被显示在列表中。  
  ![image_-_2024-12-30t155427.598.png](https://wiki.bambulab.com/software/bambu-farm-manager/image_-_2024-12-30t155427.598.png)

## 状态查看

可以在打印机页面实时的查看打印执行状态、进度和速度等关键信息。  
![f6a2f7652d5b41b3f7654d34cbff263.png](https://wiki.bambulab.com/software/bambu-farm-manager/f6a2f7652d5b41b3f7654d34cbff263.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
