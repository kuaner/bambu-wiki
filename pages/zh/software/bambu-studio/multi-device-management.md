---
path: zh/software/bambu-studio/multi-device-management
title: "多设备管理"
description: ""
tags: []
created: 2024-04-23T08:19:25.057Z
updated: 2026-08-28T06:20:39.660Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/multi-device-management
---

## 使用 Bambu Studio 进行多设备管理

本文介绍了如何使用Bambu Studio 进行管理多设备。它解释了如何激活多设备管理功能，向多个设备分派任务，以及监控不同设备和任务的状态的过程。

> 该功能在配合打印设备使用时，可能会出现部分兼容性差异。如遇异常，建议您优先使用[拓竹农场管家](../bambu-farm-features.md)。

### 开启多设备管理

您可以在偏好设置部分激活多设备管理功能。

注意：启用多设备管理后，您必须重启 Bambu Studio 以使更改生效。此外，此功能无法管理开启了局域网模式的打印机。

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/enable_multi-device_management.png)

当多设备管理功能被激活时，菜单栏中会出现一个多设备选项卡。

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/multi_device.png)

### 发送一个任务到多个设备

切片完成后， 点击“发送到多设备” 发送到多个设备。

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/sending_a_job_to_multiple_devices.png)

1. 目前，当向多个设备发送任务时，仅支持相同的AMS映射，或者您可以使用外挂料盘来使用单色耗材进行打印。
2. 有两个可以配置的选项。

- 其中一个确定同时可以发送到多少台设备，通常取决于能够同时加热热床的设备数量。热床加热的时打印机功率将达到峰值，当多台机器同时加热热床时，存在外部供电电源被超负荷的风险，请仔细评估电源供电能力。
- 另一个选项是多个打印任务的批次之间的间隔。这取决于前一个批次加热热床的时间。一般建议设置为至少五分钟的间隔。一旦前一批次打印机的热床达到工作温度，对外部电源的功率负载变少时，您就可以在其他机器上启动新任务。

注意：最多能控制6台设备。

### 监测设备状态

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/monitoring_device_status.png)

在"设备”页面，你可以查看某一个设备的状态。

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/monitoring_device_status_single.png)

### 检查任务发送状态

“正在发送的任务”展示了已经发送的任务和正在队伍中的任务。

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/task_sending.png)

### 查看已经发送的任务

你可以在“已经发送的任务”查看任务历史。

![](https://wiki.bambulab.com/bambu-studio/manual/multi-devices/tasks_have_been_sent.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
