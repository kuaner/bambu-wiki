---
path: zh/p1/manual/connect-AMS-multi-color-printing
title: "P1系列打印机本地多色打印指南"
description: "本指南介绍如何在 P1 系列打印机上本地打印多色文件。"
tags: ["p1", "本地多色打印"]
created: 2025-04-28T01:28:45.179Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/p1/manual/connect-AMS-multi-color-printing
---

## AMS 槽位 ID 分配

当 P1 系列的打印机连接 AMS 时，打印机会根据连接 AMS 的顺序对槽位进行ID分配。

AMS 和 AMS 2 Pro 的槽位会被分配为 A1-A4, B1-B4, C1-C4, D1-D4；

![](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//image-4.png)

AMS HT 的槽位会被分配为 A B C D；

![](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//image-3.png)

这些槽位 ID 会对应切片时的1-16号(A1-D4)，17-20号(A-D)颜色。

![](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//image-5.png)

> **需注意，如果提前将多个 AMS 连接在一起，然后 [再连接到AMS Hub 或 AMS 缓冲器上](../../ams/manual/multi-model-AMS-compatibility-guide.md)，或者在打印机关机状态下将所有 AMS 连接到 AMS Hub 或 AMS 缓冲器，则打印机将随机为这些 AMS 分配槽位 ID。**

## 本地打印多色文件匹配规则

当打印 microSD 卡中的切片文件时，打印机会根据是否连接AMS、是否通过Bambu Studio或Bambu Handy发起的云端打印，结合切片时模型使用的颜色编号或历史打印配置使用对应槽位的耗材进行打印。

**具体场景如下：**

1. 若打印机没有连接AMS，则会默认使用外挂料盘进行打印。
2. 使用 Bambu Studio 或 Bambu Handy 通过拓竹云服务发送打印任务，打印机会将切片文件和打印配置保存在 microSD 卡的 cache 文件夹中。通过打印机屏幕再次打印该文件时，打印机会读取保存的打印配置，选择之前打印使用的槽位进行打印。
3. 使用 Bambu Studio 在局域网模式发送打印任务，并通过屏幕选择该切片文件进行二次打印，打印机会读取切片文件中模型使用的颜色 ID，匹配对应的槽位 ID 进行打印。
4. 发送切片文件至打印机或导出至 microSD 卡时，打印机会读取切片文件中模型使用的颜色 ID，匹配对应的槽位 ID 进行打印。

**对于场景 3 和场景 4，匹配规则如下：**

- 模型上的颜色为 1 时，则使用AMS A1 槽进行打印。
- 模型上的颜色为 18 时，则使用AMS-HT B 槽进行打印。
- 模型上的颜色为 1 8 17 18时，则使用 AMS A1 B4 槽和 AMS-HT A B 槽进行打印。

## 使用建议

1. 使用打印机屏幕上的“控制——AMS——重置ID”功能，重置打印机的槽位 ID 分配记录；

![](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//image-2.png)

2. 保持打印机处于开机状态，按顺序依次重新连接 AMS；

注：图为 X1 系列机器，P1 系列同理  
![图为 X1 系列机器，P1 系列同理](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//image.png)

3. 按照 AMS 槽位 ID 顺序依次摆放耗材；

![](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//img_v3_02lo_51100d08-7b68-4528-8e45-6f13f87ac9cg.jpg)

4. 使用“从 AMS 同步材料列表”功能，将AMS的耗材信息同步至项目材料列表中。

![](https://wiki.bambulab.com/p1/manual/connect-ams-multi-color-printing//image-1.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
