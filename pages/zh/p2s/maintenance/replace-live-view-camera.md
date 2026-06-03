---
path: zh/p2s/maintenance/replace-live-view-camera
title: "更换 P2S 实况摄像头"
description: "本文介绍了如何更换 P2S 实况摄像头"
tags: []
created: 2025-10-14T13:14:08.817Z
updated: 2026-05-28T09:15:05.980Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-live-view-camera
---

> **隐私提示**：请确保摄像头已正确安装，使摄像头视野正确朝向打印机腔体，以避免对打印区域或喷嘴的检测出现问题。

## 实况摄像头

实况摄像头安装在打印机内部，可以通过实况摄像头在 Bambu Studio 和 Bambu Handy 中实时查看打印的过程，并提供炒面检测、异物检测、打印板检测以及热端类型识别等多种智能检测功能。  
![cam010.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/cam010.jpg)

## 何时更换

- 实况摄像头损坏；
- 实况摄像头连接线损坏

## 需要的工具和材料

- 新的实况摄像头
- 镊子
- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 更换实况摄像头

### 步骤 1：移除 AP 板盖，断开线缆

移除 AP 板盖，[更换 P2S AP 板盖/LED 补光灯 - 左 | Bambu Lab Wiki](replace-ap-board-cover-and-led-light-left.md) 。打开线扣（编号 10），将摄像头连接线从 AP 板上断开连接；

![ap_connectors_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap_connectors_007.png)

### 步骤 2：移除左侧板

为避免在操作过程中扯断实况摄像头连接线，请先移除左侧板：

[更换 P2S 左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

### 步骤 3：移除实况摄像头

使用镊子插入实况摄像头与立柱之间，将实况摄像头往外推出；

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/01_001.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/02_002.png)

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/03_003.png)

将摄像头连接线从框架上撕下。

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/11_011.png)

## 安装实况摄像头

### 步骤 1：安装实况摄像头

将实况摄像头对准横梁的孔位放入，然后往前门一侧推动。在安装完成后请检查实况摄像头是否完全与横梁齐平。

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/10_010.png)

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/09_009.png)  
参考下图将线缆贴在横梁上，并将摄像头连接线穿过横梁上的小孔，插入 AP 板的线扣中并扣紧（编号 10）  
![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-live-view-camera/11_011.png)  
![ap_connectors_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap_connectors_007.png)

### 步骤 2：安装左侧板和 AP 板盖

将左侧板和 AP 板盖依次装回：

- [更换 P2S 左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)
- [更换 P2S AP 板盖/LED 补光灯 - 左 | Bambu Lab Wiki](replace-ap-board-cover-and-led-light-left.md)

## 如何验证成功

连接电源线并打开电源，在 Bambu Studio/Bambu Handy 中点击播放视频，检查是否可以正常播放。

如果无法正常查看视频，则请检查线缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
