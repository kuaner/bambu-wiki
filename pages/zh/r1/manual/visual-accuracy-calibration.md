---
path: zh/r1/manual/visual-accuracy-calibration
title: "R1 视觉精度校准"
description: "本文介绍了 R1 视觉精度校准"
tags: []
created: 2026-09-22T12:48:45.788Z
updated: 2026-09-22T12:48:47.035Z
source: https://wiki.bambulab.com/zh/r1/manual/visual-accuracy-calibration
---

## 视觉精度校准介绍

视觉精度校准是为了校准工具头摄像头、测距激光、选点激光以及工作激光之间的位置和参数。

## 何时需要校准？

- 更换聚焦镜后；
- 激光焦点 XY 标定结果偏差较大或标定失败时。

## 操作步骤

### 步骤 1. 点击屏幕

点击屏幕，进入 **“设置 > 校准 > 视觉精度校准”**。

|  |  |
| --- | --- |
| 001.png | 002.png |

### 步骤 2. 安装刀条和标定板

参考下图，在**左前方 marker**处安装两条刀条，然后将标定板放在刀条上，需严格保证安装位置正确。

> 确保刀条按压到位，若有刀条翘起导致标定块倾斜，则容易导致校准失败。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/visual-accuracy-calibtration/zh/003.png)

### 步骤 3. 开启校准

在屏幕点击“开始”后，关闭上盖，按下“启停按钮”，即可开始校准。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/visual-accuracy-calibtration/zh/004.png)

> **注意：**
>
> 1. 确保标定板上**没有任何脏污**，否则会影响校准结果；
> 2. 确保工具头上未安装光路校准传感器。
>
> ![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/visual-accuracy-calibtration/zh/005.png)

## 校准动作

### 工具头摄像头与测距激光标定

工具头会在两个不同的 marker 上拍摄测距激光和标定板，通过标定板反算出激光线上各点的真实三维坐标，再推算出整束激光的空间位置和角度。

|  |  |
| --- | --- |
| 006.png | 007.png |

### 工具头摄像头标定

将工具头摄像头移动到机箱右侧标定板上方，拍摄棋盘格，以此来标定工具头摄像头的参数，确保其工作正常。

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/visual-accuracy-calibtration/zh/008.png)

### 工作激光与工具头摄像头的手眼标定

激光会在热敏纸上打出标记点，供工具头摄像头识别，以此来标定二者之间的相对位置。

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/visual-accuracy-calibtration/zh/009.png)

### 选点激光与工具头摄像头标定

选点激光和摄像头中心依次对准棋盘格板的一个角点，通过两次对位的移动距离可以计算选点激光和工具头摄像头间的相对位置。

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/visual-accuracy-calibtration/zh/010.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
