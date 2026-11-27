---
path: zh/software/bambu-scan/troubleshooting/insufficient-video-memory
title: "显存不足的可能原因及解法"
description: ""
tags: []
created: 2026-11-26T14:02:06.024Z
updated: 2026-11-26T14:02:06.024Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/troubleshooting/insufficient-video-memory
---

### 最低配置要求

- 最低配置:Intel i7 Gen7或AMD Ryzen7系;64位Windows10/11;内存≥16GB;显卡Nvidia 2060及以上,显存≥6GB
- 推荐配置:Intel i7 Gen13或AMDRyzen9系;64位Windows10/11;内存≥32GB;显卡Nvidia 3060及以上,显存>8GB

若您不熟悉自身电脑配置，可下载 Bambu Scan 后，运行软件自带的性能检测。

|  |  |
| --- | --- |
| 001.jpg | 002.jpg |

若电脑能够通过“性能检测”，但开始扫描时软件提示“显存不足”，请进行后续排查。

|  |
| --- |
| 003.png |

### 检查显示屏的输入线缆

以常规主机的布局为例，竖向的 HDMI/DP 接口均直连核显，而横向的 HDMI/DP 接口均直连独显，请确保显示屏连接在独显上。

![005.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/troubleshooting/insufficient-video-memory/zh/005.png)

### 检查 Windows 设置

进入系统-屏幕-显示卡中，找到 Bambu Scan。若应用列表中没有 Bambu Scan，可点击“添加桌面应用”。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/troubleshooting/insufficient-video-memory/zh/006.jpg)

在软件安装位置找到 Bambu Scan.exe 文件。

> 若忘记安装位置，可右键图标，点击“打开文件所在的位置”。

|  |  |
| --- | --- |
| 007.jpg | 008.jpg |

然后将“GPU首选项”改为“高性能”，重启软件即可。

![009.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/troubleshooting/insufficient-video-memory/zh/009.jpg)

### GPU加速选项

GPU 计算加速可提升点云融合等处理任务的速度，但也会占用更多显存。对于显存容量较低的设备（如 4GB 显存），可以关闭该选项，以降低扫描过程中的显存占用，从而支持更大规模的点云数据，但部分处理任务可能需要更长时间。

> 该选项默认为**自动**，软件会根据当前 GPU 配置选择合适的加速模式。当设备显存容量低于最低配置要求时，将自动关闭额外加速；满足要求时则开启。用户也可以根据实际需求手动调整。

|  |
| --- |
| 010.png |

### PC 推荐显卡型号

除推荐配置外，以下显卡型号已通过 Bambu Scan 实际扫描测试，均可提供良好的扫描体验。我们将持续测试更多显卡并更新此列表。

| **已验证显卡型号** | **显存** |
| --- | --- |
| RTX 5080 / RTX 5080 Laptop | 16 GB |
| RTX 5060 / RTX 5060 Laptop | 8 GB |
| RTX 4060 / RTX 4060 Laptop | 8 GB |
| RTX 3060 | 6 GB |
| RTX A4000 Laptop | 8 GB |
| RTX A2000 | 8 GB |

此外，我们也测试了部分低于最低显卡配置要求的设备（如搭载GTX 1650 Ti 4GB、RTX 3050 4 GB显卡的电脑），在测试中仍获得了较为流畅的扫描体验。但实际表现可能因硬件配置、扫描场景及点云数据规模而有所差异，无法保证所有低于最低配置要求的设备均能获得相同体验。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
