---
path: zh/P2S/troubleshooting/nozzle-clumping-detection
title: "0300-4015：P2S"
description: ""
tags: []
created: 2025-12-23T08:24:18.870Z
updated: 2026-04-30T10:23:52.196Z
source: https://wiki.bambulab.com/zh/P2S/troubleshooting/nozzle-clumping-detection
---

## 故障描述

打印机会利用热床边缘的特定位置进行裹头检测，该位置需要在裹头检测校准中完成标定。

校准过程中，机器会将喷嘴尖端伸入热床后侧小钢片边的圆孔内。尖端在伸入圆孔的过程中，打印机会利用挤出力传感器判断喷嘴是否触碰热床，如果检测到传感器信号变化过大，系统会发出警告，并停止校准过程。

![指示.png](https://wiki.bambulab.com/p2s/troubleshooting/hmscode/030018000001000/%E6%8C%87%E7%A4%BA.png)

### 导致该故障的原因可能是：

- 喷嘴未正确安装，导致喷嘴尖端位置有过大误差，校准时并未伸入圆孔内
- 喷嘴尖端有残余耗材粘附，校准前置过程未清理干净
- 喷嘴清理小钢片存在问题，例如：凹陷，倾斜，安装松动等等
- 喷嘴清理小钢片右侧的圆孔内存在残余废料，或圆孔内螺栓松动

## 所需工具

- H2.0 六角扳手

## 故障排除：检查零件状态

### 步骤1. 检查喷嘴是否正确安装

1. 检查热端与底座是否完全的贴合，热端上的突起会嵌入至加热底座上的凹槽。
2. 检查热端卡扣是否如图正确扣紧（先合上左侧金属板，再压紧右侧压环）。

![correct_clip_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/correct_clip_011.png)

3. 用手摇晃热端是否松动，若不松动则正确安装。

### 步骤2. 检查喷嘴尖端是否干净

若如图喷嘴上有遗留耗材，请加热喷嘴并清理热端。为防止热端高温烫伤，建议使用镊子移除残留耗材。

![20251231-161601.jpg](https://wiki.bambulab.com/p2s/20251231-161601.jpg)

### 步骤3. 检查小钢片两侧的圆孔内无异物

![p2shole.png](https://wiki.bambulab.com/h2/troubleshooting/calibrate-failed/p2shole.png)

### 步骤4. 检查小钢片状态

观察小钢片是否有倾斜，凹陷，用手指轻按小钢片，是否存在过软易变形问题。

最后使用H2.0 六角扳手拧紧小钢片两侧圆孔内的螺栓。

### 步骤5. 重新校准

完成以上排查步骤后，请在打印机屏幕上点击**重新校准**。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
