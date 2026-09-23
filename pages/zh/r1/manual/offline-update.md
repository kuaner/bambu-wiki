---
path: zh/r1/manual/offline-update
title: "R1 离线升级功能介绍"
description: "本文介绍了如何进行 R1 离线升级"
tags: []
created: 2026-09-22T12:49:01.318Z
updated: 2026-09-22T12:49:02.555Z
source: https://wiki.bambulab.com/zh/r1/manual/offline-update
---

## 离线升级

R1 支持离线升级，不依赖设备联网，可通过 USB 将离线升级包从电脑传输至 R1，在本地完成整机固件升级。

## 什么时候使用？

- 设备所在网络环境较差，云端 OTA 升级频繁失败或卡住。
- 设备部署于公司内网，无法正常访问外网，导致联网 OTA 失败。
- 需要刷入指定版本（用于问题排查、对比测试等场景）。
- 需要为多台设备批量刷写同一版本，逐台等待云端 OTA 效率过低。

## 操作步骤

1. 从[官方渠道](https://bambulab.cn/zh-cn/support/firmware-download/all)下载对应版本的离线升级包；
2. 连接机器；

**方法一**：使用 USB 数据线将 R1 连接至电脑；

> 推荐使用 **USB-IF 认证线缆。**

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-update/zh/001.png)

连接后，打开 Bambu Suite，屏幕会自动弹出连接到的设备，点击“立即切换”；

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-update/zh/002.png)

**方法二：** 在机器屏幕点击 **“设置 > 仅局域网”**，开启局域网模式；

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-processing-guide/zh/003.png)

打开 Bambu Suite，使用 PIN 码或 IP 和访问码连接机器。

|  |  |  |
| --- | --- | --- |
| 004.png | 005.png | 006.png |

3. 连接后，点击右上角“查看设备”；

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-update/zh/003.png)

4. 进入“固件更新”页面，点击“选择历史文件”功能；

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-update/zh/004.png)

选中已下载的离线升级包，进行升级；

![005.jpg](https://public-cdn.bblmw.com/wiki/new/r1/manual/offline-update/zh/005.jpg)

5. 等待设备自动完成传包、校验、刷写、重启。

> 注意：过程中请勿拔出 USB 线或切断电源。

|  |  |
| --- | --- |
| 007.jpg | 008.png |

## 注意事项

1. **请勿使用仅支持充电的线缆，推荐使用 USB-IF 认证的 USB 数据线**。若 Suite 无法识别 R1，请更换数据线或更换电脑后重试；
2. **请勿通过 USB Hub 同时连接多台 R1**，可能引发通信错误，影响升级流程；
3. 加工任务中无法启动升级，升级过程中也无法启动加工任务；
4. 请勿修改离线包的文件名，否则会被设备拒绝升级；
5. 必须使用 R1 专用离线升级包，请勿使用其他机型的升级包。

## 常见问题

1. **能用 U 盘 / SD 卡给 R1 离线升级吗？**

不能。R1 的 USB 接口不支持 Host 模式，只能通过电脑 + Bambu Suite 完成离线升级。

2. **升级中途断电怎么办？**

本次升级失败，重新按照流程操作重试。

3. **接线后识别不到 R1 怎么办？**

更换 USB 线（推荐使用 **USB-IF 认证线缆**），或更换不同电脑重试。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
