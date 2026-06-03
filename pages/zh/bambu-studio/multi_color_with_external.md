---
path: zh/bambu-studio/multi_color_with_external
title: "外挂料多色打印介绍"
description: "本文将介绍外挂料多色打印的相关知识。"
tags: []
created: 2026-05-18T06:20:52.129Z
updated: 2026-05-25T07:51:28.900Z
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

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
