---
path: zh/bambu-studio/troubleshoot/login-binding-issue
title: "Bambu Studio 登录和绑定打印机故障排除"
description: ""
tags: ["bambu studio", "故障排查", "登录", "绑定"]
created: 2024-02-29T04:00:47.861Z
updated: 2026-02-05T03:51:46.132Z
source: https://wiki.bambulab.com/zh/bambu-studio/troubleshoot/login-binding-issue
---

# 在非“仅局域网”模式下绑定打印机失败

### 绑定失败时窗口信息

![](https://wiki.bambulab.com/bambu-studio/troubleshoot/error_zh.jpg)

- 错误代码  
  - 这是一个四位错误代码，对应不同的错误，需要参考错误代码表进行解释。
- 错误描述  
  - 关于此错误，描述将包括有关错误的具体详细信息，例如绑定超时或网络错误。
- 额外信息  
  - 它将包括一些特定的错误代码，例如“IOT\_ERROR\_NO\_VALID\_DEVICE”，这表明设备尚未注册。

### 网络原因导致的绑定失败

如果 "错误描述 "或 "额外信息 "显示连接失败、无法连接或与连接有关的类似错误，则极有可能是网络问题造成的。

- 首先，检查您的网络是否正常工作，是否可以正常连接互联网。
- 如果使用的网络没有问题，请检查打印机的网络是否正常。您可以使用 cmd 工具 ping 打印机 IP 地址。  
  （打印机的 IP 地址可以从打印机屏幕上获取。）

（P1P/P1S）

![](https://wiki.bambulab.com/bind-issue/case5-3.png)

（X1/X1C）

![](https://wiki.bambulab.com/bind-issue/screenshot-20230901-141846.png)

- 如果延迟很高或无法 ping 到打印机的 IP 地址，请检查您的网络。

![](https://wiki.bambulab.com/bind-issue/20230901-142352.jpg)

### 错误代码

|  |  |  |  |
| --- | --- | --- | --- |
| **代码** | **解释** | **问题的可能原因** | **具体的检查方法** |
| -1010 | failed to create socket | 打印机的连接问题 | 检查打印机使用的网络和 Studio 使用的网络是否存在问题。 |
| -1020 | failed to socket connect | 打印机的连接问题 | 检查打印机使用的网络和 Studio 使用的网络是否存在问题。 |
| -1030 | failed to publish login request | 云服务器的网络连接问题 | - 请在错误代码上方，点击 "检查当前系统服务状态 "，跳转到我们的服务器工具页面 - 如果你的网络和我们的云服务都运行正常，请检查你的防火墙设置。 - 将打印机靠近移动热点。 |
| -1040 | timeout to get ticket from printer | 云服务器的网络连接问题 |
| -1050 | timeout to get ticket from cloud server | 云服务器的网络连接问题 |
| -1060 | failed to post ticket to cloud server | 云服务器的网络连接问题 |
| -1070 | failed to parse login report reason / no error code | 打印机的连接问题 | 检查打印机使用的网络和 Studio 使用的网络是否存在问题。 |
| -1080 | failed to parse login report reason / has error code | 打印机的连接问题 | 检查打印机使用的网络和 Studio 使用的网络是否存在问题。 |
| -1090 | timeout to receive login report | 打印机的连接问题 | 检查打印机使用的网络和 Studio 使用的网络是否存在问题。 |

# 在“仅局域网” 模式下绑定打印机失败

- “仅局域网模式”和非“仅局域网模式”的区别在于它不访问我们的云服务。
- 如果“仅局域网模式”模式登录打印机失败，请检查您的打印机和工作室是否在同一个局域网中。

# 使用APP绑定

- 尝试使用我们的应用程序绑定打印机，请查看Wiki [Bambu Handy 快速入门指南](../../studio-handy/handy/bambu-handy-quick-start.md)
- [点击此处下载Bambu Handy APP](https://bambulab.cn/zh-cn/download/app)

# 联系我们

- 如果您进行上述检查后仍无法绑定我们的打印机，请[联系我们的售后团队](https://bambulab.cn/zh-cn/my/support/tickets?from=5)。
- 请把您的Bambu Studio日志文件一起提供给我们分析，请参考Wiki[导出Bambu studio的日志](../../x1/troubleshooting/bambu-studio-log.md)。
