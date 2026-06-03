---
path: zh/software/bambu-studio/multi-device-management
title: "多设备管理"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-04-23T08:19:25.057Z
updated: 2025-01-13T07:50:21.844Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/multi-device-management
---

# 使用 Bambu Studio 进行多设备管理

本文介绍了如何使用Bambu Studio 进行管理多设备。它解释了如何激活多设备管理功能，向多个设备分派任务，以及监控不同设备和任务的状态的过程。

## 开启多设备管理

您可以在偏好设置部分激活多设备管理功能。

注意：启用多设备管理后，您必须重启 Bambu Studio 以使更改生效。此外，此功能无法管理开启了局域网模式的打印机。  
![](https://wiki.bambulab.com/bambu-studio/manual/preferences.png)

当多设备管理功能被激活时，菜单栏中会出现一个Multi-Device选项卡。  
![](https://wiki.bambulab.com/bambu-studio/manual/tab.png)

## 发送一个任务到多个设备

### 发送一个任务到多个设备

切片完成后， 点击“Send to Multi-device” 发送到多个设备。

![](https://wiki.bambulab.com/bambu-studio/manual/sending.png)

1. 目前，当向多个设备发送任务时，仅支持相同的AMS映射，或者您可以使用外挂料盘来使用单色耗材进行打印。
2. 有两个可以配置的选项。

- 其中一个确定同时可以发送到多少台设备，通常取决于能够同时加热热床的设备数量。热床加热的时打印机功率将达到峰值，当多台机器同时加热热床时，存在外部供电电源被超负荷的风险，请仔细评估电源供电能力。
- 另一个选项是多个打印任务的批次之间的间隔。这取决于前一个批次加热热床的时间。一般建议设置为至少五分钟的间隔。一旦前一批次打印机的热床达到工作温度，对外部电源的功率负载变少时，您就可以在其他机器上启动新任务。

注意：最多能控制6台设备。

## 监测设备状态

![](https://wiki.bambulab.com/bambu-studio/manual/devices.png)

在"Device”页面，你可以点击View 查看某一个设备的状态。  
![](https://wiki.bambulab.com/bambu-studio/manual/view_single.png)

## 检查任务发送状态

“Task Sending”展示了已经发送的任务和正在队伍中的任务。  
![](https://wiki.bambulab.com/bambu-studio/manual/task_sending.png)

## 查看已经发送的任务

你可以在“Task Sent”查看任务历史。  
![](https://wiki.bambulab.com/bambu-studio/manual/tasks_sent.png)
