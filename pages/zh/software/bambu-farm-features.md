---
path: zh/software/bambu-farm-features
title: "拓竹农场管家功能"
description: "本文介绍了拓竹农场管家的主要功能"
tags: ["software"]
created: 2024-11-11T07:38:33.388Z
updated: 2025-04-14T02:40:59.380Z
source: https://wiki.bambulab.com/zh/software/bambu-farm-features
---

## 打印机页总览

本页面可以让您全局监控打印机状态和管理您的打印机。  
![image_-_2024-12-30t114019.273.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114019.273.png)

顶部状态导航可帮助您快速识别哪些打印机需要人员操作，如打印完成后等待取件，打印中缺料暂停等。

- "可开始打印"：如果打印机为空闲态且有待执行任务，将显示在该页面下。
- "需要关注"：打印机可能处于暂停，离线，异常停止等状态，需要您查看处理。
- "已完成的打印"：打印完成或终止的打印机将显示在该页面下，提示您哪些打印机需要清理热床。您需要在打印机侧或本软件中点击“确认清盘”（或“批量清盘”），将打印机切换到“空闲态”，以便发起下一轮打印。

![image_-_2024-12-30t114054.623.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114054.623.png)

- "无任务"：打印机处于空闲态，且无待执行任务。

##### 打印机详情页

可在“详情”页中可查看设备型号，序列号，喷嘴和热床温度等信息。

![image_(64).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(64).png)

## 批量控制

当您需要逐个打印机执行暂停，退料等操作时，可使用批量控制功能，节省您的操作时间。可以在打印机页面，选择打印机后执行。  
![image_-_2024-12-30t114217.383.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114217.383.png)

也可以在任务页面下点击“批量操作”，选择该任务下的打印机执行操作。  
![image_-_2024-12-30t114221.582.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114221.582.png)

目前支持 “暂停打印，取消打印，继续打印，补光灯开关，修改打印速度，设置喷嘴和热床温度，外挂料盘退料，机器校准” 等命令。  
![image_-_2024-12-30t114317.288.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114317.288.png)

## 更新打印机固件

点击 “更新打印机固件”，可进入打印机升级管理页面。农场管家客户端需要具备外网访问能力，以便查询和下载打印机固件。

![image_(68).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(68).png)

该页面下显示空闲态打印机，可选择打印机并指定版本升级。  
![image_(69).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(69).png)

## 切片文件存储

- 上传后切片文件将存储在农场管家服务器所在电脑中，支持二级目录管理文件。
- 支持文件夹/文件重命名，移动位置等操作。
- 自动识别切片文件的适配机型，喷嘴直径和热床类型，打印时长等信息。

![image_(71).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(71).png)

## 任务队列

- **创建任务**

如果您需要先创建任务计划，稍后再启动打印，可以选择“发送任务到队列”选项。该模式下，您可以指定一个模型文件需要打印的次数，以及选择哪些打印机来完成这些打印任务。之后，您可以在任务列表中查看和操作这些任务。  
![image_-_2024-12-30t114520.542.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114520.542.png)

- **发起多机打印**

当一个任务有可用打印机时，该任务的“开始”按钮变为绿色，提示您可发起打印。  
![image_-_2024-12-30t114547.614.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114547.614.png)  
![image_-_2024-12-30t114550.136.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114550.136.png)

- **发起单机打印**

在“打印机”页面下。当打印机空闲且有待执行任务时， 可点击“开始”，选择需求启动的任务。  
![image_-_2024-12-30t114844.782.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2024-12-30t114844.782.png)

- **其他任务操作**

1. "编辑任务"：支持修改目标打印次数，增加和移除该任务下的打印机。
2. "取消任务"：取消任务不会影响已开始执行的打印。当前任务会被标记为结束状态，剩余次数不会再被执行。

![image_(72).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(72).png)

队列任务列表也会周期性的同步到打印机中，如果您的电脑离打印区比较远，可在打印机屏幕上查任务，并选择执行。  
![1730515277451.png](https://wiki.bambulab.com/software/bambu-farm-features/1730515277451.png)

对于 P1P/P1S 打印机，左侧导航栏向下浏览，依然可以进入 microSD 卡页面。  
![image_(73).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(73).png)

## 多账号管理

农场管家支持多用户访问, 账号信息仅存储在本地服务器中。您需要在首次激活服务器时设置本地管理员的账号名称和密码。仅管理员账号具备创建和删除普通用户，重置普通用户密码的权限。  
![image_(74).png](https://wiki.bambulab.com/software/bambu-farm-features/image_(74).png)

普通用户登录时，可以在发现页面选择服务器，然后使用本地账号用户名和密码登录农场服务器。

![image_-_2024-12-30t120218.238.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2025-01-10t170440.013.png)  
![image_-_2024-12-30t120219.551.png](https://wiki.bambulab.com/software/bambu-farm-features/image_-_2025-01-10t170441.764.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
