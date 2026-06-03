---
path: zh/h2/maintenance/replace-calibration-stickers
title: "H2 系列校准贴纸更换指南"
description: "本文将介绍如何更换 H2 打印机校准贴纸包。"
tags: []
created: 2026-05-12T03:15:09.472Z
updated: 2026-05-14T09:03:16.222Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-calibration-stickers
---

## 校准贴纸包

H2系列打印机的工具头摄像头使用校准贴纸来校准打印、切割、雕刻和绘图任务的运动系统。这些贴纸贴在热床或激光平台的关键位置。

![calibration_sticker_pack.png](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/calibration_sticker_pack.png)

## 何时使用本指南

1. 一个或多个校准贴纸损坏或缺失，导致校准失败。

## 所需工具和材料

1. 激光垫板热校准贴纸
2. 擦嘴钢片
3. 热床校准贴纸
4. 激光/刀切垫板回中校准贴纸
5. BT2-5螺丝 \* 2
6. 刮刀或其他撬动工具

![calibration_sticker_pack_annotated.png](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/calibration_sticker_pack_annotated.png)

## 安全警告

> **重要！**
>
> 在进行维护工作前，务必**关闭并断开**打印机的电源。否则，存在**触电、短路以及损坏**打印机或周围环境的**风险**。
>
> 当维护任务需要打印机通电时，请使用**绝缘手套**以确保安全，并特别注意**不要夹住、损坏或对**任何裸露的电线、连接器或电路板**施加压力**。此外，喷嘴可能非常烫，切勿用裸露的皮肤接触。
>
> 如果您对上述内容或本指南中的步骤有任何疑问或顾虑，请[在我们的支持页面提交新工单](https://bambulab.com/en/my/support/tickets?from=5)以获取帮助。

## 激光垫板热校准贴纸

### 移除旧贴纸

使用刮刀或其他撬动工具，小心地撬起激光垫板上热校准贴纸的一个角，然后用手将其完全撕下。

![laser_platform_big_sticker_removal.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/laser_platform_big_sticker_removal.gif)

### 安装新贴纸

小心地将新贴纸对准凹槽，用力按压使其贴合，然后撕掉保护膜。

![laser_platform_big_sticker_install.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/laser_platform_big_sticker_install.gif)

## 擦嘴钢片

### 移除旧钢片

首先，拧下钢片两端的两个安装螺丝。

![nozzle_wiper_screws_annotated.png](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/nozzle_wiper_screws_annotated.png)

然后，取下钢片。

![heatbed_wiper_sheet_removal.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/heatbed_wiper_sheet_removal.gif)

### 安装新钢片

放置新钢片。

![heatbed_wiper_sheet_install.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/heatbed_wiper_sheet_install.gif)

用两个安装螺丝将其固定到位。

![nozzle_wiper_screws_annotated.png](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/nozzle_wiper_screws_annotated.png)

## 热床校准贴纸

### 移除旧贴纸

使用刮刀或其他撬动工具，小心地撬起热床右后角的校准贴纸。您可以使用贴纸右侧的凹口作为撬动工具的着力点。稍微撬起后，用手将其完全撕下。

![heatbed_calibration_removal.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/heatbed_calibration_removal.gif)

### 安装新贴纸

注意贴纸的方向，其右侧有之前提到的大方格图案和凹口。小心地将新贴纸对准凹槽，然后用力按压使其牢固贴合。

![heatbed_calibration_install.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/heatbed_calibration_install.gif)

## 激光/刀切垫板回中校准贴纸

### 移除旧贴纸

使用热床刮刀或其他撬动工具，小心地撬起激光垫板上校准贴纸的一角，然后用手将其完全撕下。

![laser_calibration_sticker_removal.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/laser_calibration_sticker_removal.gif)

### 安装新贴纸

注意新贴纸上的向上标记，使其朝向打印机的后方。

![upward_marking.png](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/upward_marking.png)

小心地将其对准激光垫板上的凹槽，然后用力按压使其牢固贴合。

![laser_calibration_sticker_install.gif](https://wiki.bambulab.com/h2/maintenance/replace-calibration-stickers/laser_calibration_sticker_install.gif)

## 功能验证

将热床安装回打印机（如有必要，也请测试激光垫板），开始打印或其他任务，查看启动校准是否成功完成。如果任务在校准时失败（出现相关错误），请仔细检查校准贴纸的对齐和位置，并确保贴纸和工具头摄像头均未被遮挡。

## 结束语

> 我们希望本指南提供了清晰实用的支持。  
> 如果问题仍未解决，请提交 [支持工单](https://bambulab.com/zh/my/support/tickets/create)，并附上您最近的打印机日志以及额外的图片或其他详细信息。我们的技术团队将审核您的请求并提供详细协助。  
> 您也可以访问 [Bambu AI](https://support.bambulab.com/liveChat/?from=6&lang=zh)，它可以即时回答常见问题并为您提供操作指导。
