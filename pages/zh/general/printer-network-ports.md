---
path: zh/general/printer-network-ports
title: "打印机网络端口"
description: ""
tags: ["端口", "网络端口"]
created: 2023-01-09T08:56:56.138Z
updated: 2025-11-26T08:24:20.021Z
source: https://wiki.bambulab.com/zh/general/printer-network-ports
---

本文档列出了打印机所需的所有应用程序和端口。 请检查路由器或您的 PC 的设置，确保这些端口未被阻止。

|  |  |  |  |
| --- | --- | --- | --- |
| **应用** | **接口** | **类型** | **模式** |
| http API | 80/443/8080 | TCP | Cloud mode |
| mqtt | 8883 | TCP | Cloud mode |
| Remote video | 8000/21047/1000/443/8443 | TCP | Cloud mode |
| Remote video | 10001~10512/5888~5889/4000~4100  /8443/8130/3478~3989 | UDP | Cloud mode |
| Device binding | 3000 | TCP | Cloud mode |
| Device discovering | 1990/2021 | SSDP. multicast/broadcast | Cloud/LAN mode |
| LAN mode MQTT | 8883 | TCP | LAN mode. |
| LAN mode FTP | 990/50000~50100 | TCP | LAN mode |
| LAN mode video | 6000 | TCP | LAN mode |
| NTP | 123 | TCP/UDP | Cloud/LAN mode |

# 域名/IP

为了使打印机能够与云服务器通信，使用了以下域名/IP地址。

请注意:

当打印机处于局域网模式时，所有域名/IP地址都是无用的;

域名/IP地址在未来可能会被改变;

当你不需要相关功能时，你可以在路由器的防火墙中阻止以下域名/IP的全部或部分。例如：你可以禁用所有的远程视频端口，然后你就不能从远程访问打印机的摄像头;

关于远程视频:

考虑到网络带宽非常高，并且不同地区的网络可能很复杂，由于我们在全球使用了许多服务器来稳定视频传输，因此列表上有很多域名/IP地址。

|  |  |  |
| --- | --- | --- |
| **应用** | **域名/IP** | **相关功能** |
| NTP | 0.pool.ntp.org iburst  1.pool.ntp.org iburst  2.pool.ntp.org iburst  3.pool.ntp.org iburst  time.windows.com  time.google.com  time.pool.aliyun.com  time.nist.gov  ntp.pagasa.dost.gov.ph |  |
| http API | 全球用户:  - \*.bambulab.com: 鉴于云服务的变化，我们无法在此列出所有域名。比如： api.bambulab.com, e.bambulab.com  - \*.amazonaws.com: 这是 AWS S3 服务，域名参考： https://docs.aws.amazon.com/general/latest/gr/s3.html  中国大陆用户:  - \*.bambulab.cn:  鉴于云服务的变化，我们无法在此列出所有域名。比如： api.bambulab.cn e.bambulab.cn  - \*.aliyuncs.com: 这是aliyun oss服务，域名参考： https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints | 主要云功能包括用户登录、远程打印、远程视频、固件OTA等。 |
| mqtt | 全球用户:  - us.mqtt.bambulab.com  中国大陆用户:  - cn.mqtt.bambulab.com | 远程打印机控制/打印 |
| 远程视频 | 全球用户:  鉴于视频服务器可能会发生变化，我们无法在此列出所有域名。  - all-master-tutk.iotcplatform.com  - all-c-master-71spctnsfa8p5xvgkssa.iotcplatform.com  - all-c-master-tutk.iotcplatform.com  - m1.iotcplatform.com  - m2.iotcplatform.com  - m3.iotcplatform.com  - m4.iotcplatform.com  - m5.iotcplatform.com  - m6.iotcplatform.com -  - m7.iotcplatform.com  - m8.iotcplatform.com  - m9.iotcplatform.com  - m10.iotcplatform.com  - m11.iotcplatform.com  - m-12.iotcplatform.com  - m-13.iotcplatform.com    中国大陆用户:  鉴于视频服务器可能会发生变化，我们无法在此列出所有域名。  - all-master-tutk.kalay.net.cn  - m1.kalay.net.cn  - m2.kalay.net.cn  - m3.kalay.net.cn  - m4.kalay.net.cn  - m5.kalay.net.cn  - m6.kalay.net.cn  - m7.kalay.net.cn  - m8.kalay.net.cn  - m9.kalay.net.cn  - m10.kalay.net.cn  - m11.kalay.net.cn  - m-12.kalay.net.cn  - m-13.kalay.net.cn | 远程视频监控/视频文件下载 |
