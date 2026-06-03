---
path: zh/p1/troubleshooting/printer-binding-issue
title: "P1系列打印机网络故障问题排查指南"
description: "本指南介绍 P1 系列打印机网络绑定问题的故障排除步骤。"
tags: ["p1", "网络故障"]
created: 2023-08-15T14:26:36.449Z
updated: 2026-02-04T09:30:22.356Z
source: https://wiki.bambulab.com/zh/p1/troubleshooting/printer-binding-issue
---

# 对于 P1 系列打印机，需要满足以下要求：

## **1**: Bambu Handy 的权限

iOS 和 Android 手机都需要蓝牙权限。对于某些 Android 手机，还需要“位置权限”。

## **2**: 激活的蓝牙设备

在打印机绑定操作期间，禁用或断开与手机当前连接的其他蓝牙设备。

## **3**: 打印机 Wi-Fi 天线连接

确保天线连接器和电缆没有外观损坏，并且连接器牢固地固定在板上。

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/wifi-antenna.png)

## **4**: 忘记已配对的 BBLPrinter 并重新配对打印机：

需要在手机的蓝牙设置中忘记（或删除）之前配对的"BBLPrinter"。此外，禁用并重新启用蓝牙一次，然后再次配对打印机的蓝牙。

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/rq4.png)

## **5**: 如果您之前已成功绑定打印机，那请将打印机的恢复出厂设置后，再进行故障排查。

# 案列 1: 01S/01PXXXXXX not found

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case1-1v1.png)

Handy应用程序正在尝试通过蓝牙查找具有特定产品序列号（SN）的Bambulab打印机，但无法找到打印机。

请首先确保您已检查了上述的要求1、2和4。

步骤1：使用Handy应用程序扫描所有打印机，允许其进行大约5-10秒的扫描。如果在此扫描期间找到了打印机，请选择它以执行绑定操作。

|  |  |
| --- | --- |
|  |  |

步骤2：按照上述“打印机天线要求”中的步骤执行，重新启动打印机（关闭电源后等待20秒），然后重试“步骤1”。

步骤3：重新启动您的手机或尝试使用另一部手机重复“步骤1”。

如果问题仍然存在，请联系售后服务，并提供以下信息以获取进一步帮助：手机型号、操作视频和打印机日志。

# 案例 2: Failed to request the printer's "WI-FI" list

当您遇到以下的提示信息时，均可采用下述方法来解决。

|  |  |
| --- | --- |
|  |  |

在大多数情况下，问题是由手机和打印机之间的蓝牙配对失败引起的。请按照“忘记已配对的BBL打印机设备的要求4”进行操作。

您应该尝试重新扫描QR码以开始绑定操作。同时，请按照以下描述，在手机和打印机屏幕上确认配对。

打印机屏幕显示内容：

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case2-2.png)

iOS 手机屏幕显示内容:

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case2-3.png)

安卓手机屏幕显示内容

|  |  |
| --- | --- |
|  |  |

# 案例 3: Invalid password

在大多数情况下，问题是由于在Wi-Fi连接过程中输入了错误的密码或遇到无线干扰引起的。

步骤1：重新尝试直接设置Wi-Fi，并确保SSID和密码正确无误。

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case3-1.png)

步骤2：将打印机靠近路由器，并再次尝试。

步骤3：尝试使用不同的路由器或让打印机连接到移动热点，以验证网络问题是由路由器设置还是故障的打印机网络模块引起的。

步骤4：如果问题仍然存在，请仔细检查上述提到的“要求3：打印机Wi-Fi天线”。此外，请提供打印机的日志以获取进一步帮助。

# 案例 4: DHCP Failed

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case4-1.png)

原因1：无线信号弱或无线干扰可能导致DHCP数据包丢失。建议的解决方案是将打印机靠近路由器，并尝试重新连接。

原因2：由于连接的设备数量较多，路由器已用尽可用的IP地址，可能存在网络中的IP地址冲突。这可能发生在某些设备具有静态IP配置或在路由器重新启动后继续使用旧IP地址而没有获取新IP地址的情况下。为了解决这个问题，您可以尝试使用移动热点作为替代方案，看看是否可以成功连接。

# 案例 5: Maybe not on the same LAN

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case5-1.png)

原因1：手机未连接到Wi-Fi网络或未连接到相同的路由器。请检查打印机和手机是否连接到相同的路由器（验证SSID）。此外，确保打印机的IP地址和手机的IP地址在同一网络段内（在大多数情况下，只有最后一位数字不同，例如，192.168.2.X）。

|  |  |
| --- | --- |
|  |  |

原因2：可能在路由器上启用了隔离设置，需要将其禁用。

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case5-4.png)

原因3：可能存在特定IP或TCP/UDP端口的网络防火墙限制。请检查路由器设置，确保打印机的MAC/IP地址的通信未被阻止。

# 案例 6: IP 地址是 0.0.0.0

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case6-1.png)

原因1：可能是您的路由器的DHCP地址池已满，您需要重新启动路由器来解决该问题。

原因2：可能是您的路由器的信道设置不正确。如果重新启动路由器无法解决问题，可能是由于不正确的信道设置。我们请求您上传打印机的日志，以便我们可以检查您的路由器上的信道设置是否受打印机支持（我们的打印机支持1-11信道）。

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case6-2.png)

# 案例 7:  IOT\_ERROR\_NO\_VALID\_DEVICE

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case8.png)

此错误消息通常表示您的打印机序列号（SN）尚未被注册。如果您更换了AP板而未与售后服务联系以重新注册打印机的序列号，就会发生这种情况。如果打印机在出厂时未注册，也可能发生这种情况。如果您收到上述提示，请联系客户服务，他们将帮助您注册序列号。

# 案例 8: IOT\_ERROR\_REGION\_LIMITED

![](https://wiki.bambulab.com/p1/troubleshooting/binding-issue/case7.png)

这个提示是指打印机使用区域的限制，例如，如果你购买的打印机是仅限中国大陆地区使用，那么，您需要切换成中国大陆地区的账号（中国大陆手机号），并重新登录。

# 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
