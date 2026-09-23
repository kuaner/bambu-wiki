---
path: zh/r1/manual/magnetic-encoder-calibration
title: "R1 电机定位校准"
description: "本文介绍了 R1 电机定位校准"
tags: []
created: 2026-09-22T13:29:17.656Z
updated: 2026-09-22T13:29:18.890Z
source: https://wiki.bambulab.com/zh/r1/manual/magnetic-encoder-calibration
---

## 电机定位校准

R1 的 XY 电机配备了磁编码器，主要用于在**电机下电或解锁后**，帮助机器识别工具头的实际位置，从而支持工具头选区、测高等功能，并减少机器重新回零的次数。

需要注意的是，磁编码器**不参与电机运动控制**。XY 电机运行时仍然采用开环控制，但磁编码器不会实时参与电机闭环修正。

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/magnetic-encoder-calibration/zh/001.png)

## 校准目的

由于磁铁偏心、安装误差、传感器误差等因素的影响，磁编码器读取到的原始角度不一定与电机的真实机械角度严格线性对应。

电机定位校准的作用是建立一组**原始磁编码器角度 > 校正后机械角度**的查表数据，并将其保存到主板内存中。后续设备在需要通过磁编码器获取工具头位置时，会使用这组数据对磁编码器角度进行修正，从而提高电机下电或解锁状态下工具头位置识别的准确性。

需要说明的是，电机定位校准提升的是**磁编码器位置识别的准确性**，其主要是为手动拖动工具头的场景服务，因为此时工具头处于下电或解锁状态，设备只能依靠磁编码器并结合校正数据来识别其位置，因此校准的准确性直接决定了手拖工具头相关功能的可靠性。关于手拖工具头功能的具体介绍，请参考 wiki：[手拖工具头介绍](toolhead-drag-measurement.md)。

## 什么时候需要校准？

- 更换 XY 电机后；
- 出现磁编码器相关报错时。

## 校准过程

- 点击屏幕：“设置 > 校准 > 电机定位校准”；

|  |  |
| --- | --- |
| 002.png | 003.png |

- 开始校准后，工具头会先进行一次回零；

![004.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/magnetic-encoder-calibration/zh/004.webp)

随后，机器会从固定位置开始，驱动对应电机缓慢转动，并记录电机与磁编码器之间的对应关系；

![005.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/magnetic-encoder-calibration/zh/005.webp)

校准完成后，工具头会再次回零，并回到默认位置。

![006.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/magnetic-encoder-calibration/zh/006.webp)

> 整个校准过程无需手动干预，通常可在 1 分钟内完成。

## 注意事项

校准过程中请注意：

- 请勿关闭电源；
- 请勿移动工具头或触碰运动部件；
- 请保持机器处于稳定状态；
- 请等待校准完成后，再进行下一步操作。

## 失败处理

如果校准失败，请按以下顺序进行检查：

1. 确认工具头运动区域内没有异物阻挡；
2. 确认电机、皮带、导轨等运动部件无卡滞；
3. 确认工具头没有被人为移动，也没有受到外力干扰；
4. 如果 HMS 报错提示磁编码器超时或返回值异常，请关闭电源后检查磁编码器接线，参考此 wiki：[更换主板](https://wiki.bambulab.com/zh/r1/maintenance/replace-mainboard)。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/magnetic-encoder-calibration/zh/007.png)

5. 完成检查后，请重新执行电机定位校准。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/magnetic-encoder-calibration/zh/007.png)

5. 完成检查后，请重新执行电机定位校准。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
