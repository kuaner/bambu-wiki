---
path: zh/bambu-studio/multi_color_with_external
title: "外挂料多色打印介绍"
description: "本文将介绍外挂料多色打印的相关知识。"
tags: []
created: 2026-05-18T06:20:52.129Z
updated: 2026-08-28T06:42:21.077Z
source: https://wiki.bambulab.com/zh/bambu-studio/multi_color_with_external
---

## 外挂料多色打印

当您没有 AMS 时，可以仅使用外挂料盘实现多色打印。该功能会在需要换色时暂停打印任务，此时更换其他颜色的耗材后恢复打印即可。

### 版本要求

|  |  |  |
| --- | --- | --- |
| 机型 | 最低支持固件版本 | 配套 Bambu Studio 要求 |
| P1P / P1S | 01.10.00.00 | ≥ 2.5.2.65 |
| A1 | 01.08.00.00 | ≥ 2.5.2.65 |
| A1 mini | 01.08.00.00 | ≥ 2.5.2.65 |
| P2S | 01.02.00.00 | ≥ 2.5.2.65 |
| H2S | 01.02.00.00 | ≥ 2.5.2.65 |

### 操作步骤

示例模型：[test\_model.3mf](https://wiki.bambulab.com/software/bambu-studio/multi_color_with_external/test_model.3mf)

多色模型直接切片。

![1.jpg](https://wiki.bambulab.com/software/bambu-studio/multi_color_with_external/1.jpg)

在发起打印的准备阶段，勾选“外挂料多色打印”。

![2.jpg](https://wiki.bambulab.com/software/bambu-studio/multi_color_with_external/2.jpg)

第一个颜色打印完后，将弹出如下提示。

![error.jpg](https://wiki.bambulab.com/software/bambu-studio/multi_color_with_external/error.jpg)

根据提示更换新的外挂料盘上的耗材后，点击“继续”。

**优点：** 无需检查换色层；同一层可换色；切片体验更好。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
