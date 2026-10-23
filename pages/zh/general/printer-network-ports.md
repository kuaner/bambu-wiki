---
path: zh/general/printer-network-ports
title: "打印机网络端口"
description: ""
tags: ["端口", "网络端口"]
created: 2023-01-09T08:56:56.138Z
updated: 2026-10-15T07:44:00.435Z
source: https://wiki.bambulab.com/zh/general/printer-network-ports
---

本页列出打印机各项功能所需的网络端口与 IP 地址。当某项功能异常时（例如发送打印任务失败、无法绑定设备、远程视频无法加载），可能是路由器或电脑防火墙阻止了相关端口或 IP，您可参照本页进行排查。

## 端口列表

| 应用 | 端口 | 类型 | 模式 |
| --- | --- | --- | --- |
| http API | 80/443/8080 | TCP | 云模式（Cloud mode） |
| MQTT | 8883 | TCP | 云模式（Cloud mode） |
| Remote video 远程视频 | 8000/21047/1000/443/8443 | TCP | 云模式（Cloud mode） |
| Remote video 远程视频 | 10001~10512/5888~5889/4000~4100 /8443/8130/3478~3989 | UDP | 云模式（Cloud mode） |
| Device binding 设备绑定 | 3000 | TCP | 云模式（Cloud mode） |
| Device discovering 设备发现 | 1990/2021 | SSDP. multicast/broadcast | 云模式/局域网模式（Cloud/LAN mode） |
| LAN mode MQTT | 8883 | TCP | 局域网模式（LAN mode） |
| LAN mode FTP | 990/50000~50100 | TCP | 局域网模式（LAN mode） |
| LAN mode video | 6000 | TCP | 局域网模式（LAN mode） |
| NTP | 123 | TCP/UDP | 云模式/局域网模式（Cloud/LAN mode） |

> **ℹ️ 如何看懂本表**
>
> - **应用**：打印机的对应功能。例如「远程视频」用于查看摄像头画面、「设备发现」用于让 Bambu Studio 在同一网络下找到打印机。
> - **端口**：该功能通信所使用的网络端口号，`~` 表示一个连续的端口范围。
> - **类型**：通信协议类型（TCP / UDP / SSDP 等）。
> - **模式**：该端口的适用模式（**云模式**／**局域网模式**／两者通用）。

## 域名/IP 列表

> **✅ 说明**：
>
> - 当打印机处于「局域网模式」时，所有域名/IP 地址均不适用
> - 域名/IP 地址未来可能会发生变更
> - 不需要某项功能时，可在路由器防火墙中阻止相应域名/IP（例如禁用所有远程视频端口后，您将无法远程访问摄像头）
>
> 关于远程视频：考虑到网络带宽要求较高、且不同地区的网络环境较为复杂，我们在全球部署了多台服务器以保证视频传输的稳定性，因此列表中包含较多域名/IP 地址。

为了使打印机能够与云服务器通信，使用了以下域名/IP 地址。

#### 中国大陆用户

👇️ **提示**：滑动表格查看更多内容。

| 应用 | 域名/IP | 相关功能 |
| --- | --- | --- |
| NTP | [0.pool.ntp.org](http://0.pool.ntp.org) iburst [1.pool.ntp.org](http://1.pool.ntp.org) iburst [2.pool.ntp.org](http://2.pool.ntp.org) iburst [3.pool.ntp.org](http://3.pool.ntp.org) iburst [time.windows.com](http://time.windows.com) [time.google.com](https://time.google.com) [time.pool.aliyun.com](http://time.pool.aliyun.com) [time.nist.gov](http://time.nist.gov) [ntp.pagasa.dost.gov.ph](http://ntp.pagasa.dost.gov.ph) |  |
| http API | - \*.bambulab.cn: 鉴于云服务的变化，我们无法在此列出所有域名。 比如： [api.bambulab.cn](http://api.bambulab.cn), [e.bambulab.cn](http://e.bambulab.cn) - \*.aliyuncs.com: 这是 aliyun oss 服务，域名参考： <https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints> | 主要云功能包括用户登录、远程打印、远程视频、固件OTA等。 |
| MQTT | - [cn.mqtt.bambulab.com](http://cn.mqtt.bambulab.com) | 远程打印机控制/打印 |
| 远程视频 | 鉴于视频服务器可能会发生变化，我们无法在此列出所有域名。 - [all-master-tutk.kalay.net.cn](http://all-master-tutk.kalay.net.cn) - [m1.kalay.net.cn](http://m1.kalay.net.cn) - [m2.kalay.net.cn](http://m2.kalay.net.cn) - [m3.kalay.net.cn](http://m3.kalay.net.cn) - [m4.kalay.net.cn](http://m4.kalay.net.cn) - [m5.kalay.net.cn](http://m5.kalay.net.cn) - [m6.kalay.net.cn](http://m6.kalay.net.cn) - [m7.kalay.net.cn](http://m7.kalay.net.cn) - [m8.kalay.net.cn](http://m8.kalay.net.cn) - [m9.kalay.net.cn](http://m9.kalay.net.cn) - [m10.kalay.net.cn](http://m10.kalay.net.cn) - [m11.kalay.net.cn](http://m11.kalay.net.cn) - [m-12.kalay.net.cn](http://m-12.kalay.net.cn) - [m-13.kalay.net.cn](http://m-13.kalay.net.cn) | 远程视频监控/视频文件下载 |

  

#### 全球用户

👇️ **提示**：滑动表格查看更多内容。

| 应用 | 域名/IP | 相关功能 |
| --- | --- | --- |
| NTP | [0.pool.ntp.org](http://0.pool.ntp.org) iburst [1.pool.ntp.org](http://1.pool.ntp.org) iburst [2.pool.ntp.org](http://2.pool.ntp.org) iburst [3.pool.ntp.org](http://3.pool.ntp.org) iburst [time.windows.com](http://time.windows.com) [time.google.com](https://time.google.com) [time.pool.aliyun.com](http://time.pool.aliyun.com) [time.nist.gov](http://time.nist.gov) [ntp.pagasa.dost.gov.ph](http://ntp.pagasa.dost.gov.ph) |  |
| http API | - \*.bambulab.com: 鉴于云服务的变化，我们无法在此列出所有域名。 比如： [api.bambulab.com](http://api.bambulab.com), [e.bambulab.com](http://e.bambulab.com) - \*.amazonaws.com: 这是 AWS S3 服务，域名参考： <https://docs.aws.amazon.com/general/latest/gr/s3.html> | 主要云功能包括用户登录、远程打印、远程视频、固件OTA等。 |
| MQTT | - [us.mqtt.bambulab.com](http://us.mqtt.bambulab.com) | 远程打印机控制/打印 |
| 远程视频 | 鉴于视频服务器可能会发生变化，我们无法在此列出所有域名。 - [all-master-tutk.iotcplatform.com](http://all-master-tutk.iotcplatform.com) - [all-c-master-71spctnsfa8p5xvgkssa.iotcplatform.com](http://all-c-master-71spctnsfa8p5xvgkssa.iotcplatform.com)  - [all-c-master-tutk.iotcplatform.com](http://all-c-master-tutk.iotcplatform.com) - [m1.iotcplatform.com](http://m1.iotcplatform.com) - [m2.iotcplatform.com](http://m2.iotcplatform.com)  - [m3.iotcplatform.com](http://m3.iotcplatform.com)  - [m4.iotcplatform.com](http://m4.iotcplatform.com)  - [m5.iotcplatform.com](http://m5.iotcplatform.com)  - [m6.iotcplatform.com](http://m6.iotcplatform.com)  - [m7.iotcplatform.com](http://m7.iotcplatform.com)  - [m8.iotcplatform.com](http://m8.iotcplatform.com)  - [m9.iotcplatform.com](http://m9.iotcplatform.com)  - [m10.iotcplatform.com](http://m10.iotcplatform.com) - [m11.iotcplatform.com](http://m11.iotcplatform.com) - [m-12.iotcplatform.com](http://m-12.iotcplatform.com) - [m-13.iotcplatform.com](http://m-13.iotcplatform.com) | 远程视频监控/视频文件下载 |

  

## 如何检查是否被阻止

您可以按以下步骤排查，判断是否为网络端口或 域名/IP 被阻止导致的问题：

### 1. 切换到手机热点进行测试

将打印机和电脑连接到同一个手机 2.4GHz 热点后重试。  
如果换网后功能恢复正常，基本可以确定是原网络环境（路由器设置、防火墙或网络稳定性）导致的问题，可继续按下方步骤排查。

### 2. 确认网络模式

确认打印机处于**云模式**还是**局域网模式**：

- **云模式**：需要用到云端通信，请参照本页的**端口列表**和**域名/IP 列表**进行检查。
- **局域网模式**：打印机不与云端通信，只需关注端口列表中标注「局域网模式」的项，**域名/IP 列表无需关注**。

关于局域网模式的更多信息，您可以参阅：[如何在Bambu Lab打印机上使用局域网模式](../knowledge-sharing/enable-lan-mode.md)

### 3. 检查电脑防火墙 / VPN 设置

确认电脑的防火墙、安全软件，或 **VPN / 代理软件**没有阻止上述端口，也没有阻止 Bambu 相关软件的联网。如不确定，可**临时关闭防火墙与 VPN / 代理软件**后重试。

### 4. 检查路由器设置

登录路由器管理页面，确认没有防火墙、端口过滤或访问控制规则，阻止了本页**端口列表**与**域名/IP 列表**中列出的端口或地址。

> **✅ 说明**：不同品牌路由器的设置界面差异较大，具体位置请参考您所用路由器的官方说明，相关选项通常名为「防火墙」「端口过滤」「访问控制」或「安全设置」。

如果完成以上排查后问题仍未解决，请联系 Bambu Lab 客户支持团队，我们将协助您进一步排查。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
