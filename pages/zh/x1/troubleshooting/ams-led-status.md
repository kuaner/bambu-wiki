---
path: zh/x1/troubleshooting/ams-led-status
title: "AMS指示灯状态解析"
description: "本文介绍了不同指示灯对应的AMS工作状态"
tags: []
created: 2022-12-18T13:49:05.771Z
updated: 2026-02-11T08:39:00.843Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/ams-led-status
---

## 前言

在日常使用AMS时，可以通过第一阶段进料器的LED灯状态来判断AMS是否正常工作。

## 指示灯状态

|  |  |  |
| --- | --- | --- |
| **LED 状态** | **AMS 状态** | 备注 |
| 4个白灯依次闪烁 | 正常状态，四个槽都没有料 |  |
| 白灯常亮 | 正常状态，有料插入该槽且处于空闲状态 |  |
| 白灯呼吸 | 正常状态，有料插入该槽且处于忙碌状态（送料，读取RFID等） |  |
| 红灯单闪 | 错误状态，此时第一阶段进料器检测到有料，五通检测没料。可能是上下料组件工作异常，或料管中存在堵塞。 | 可参考 [拆解和清洁AMS五通组件](clean-the-filaments-hub.md) 检查是否存在堵塞 |
| 红灯双闪 | 错误状态，第一阶段进料器和五通都检测到有料可能是进料或退料失败，可能是进料/退料失败，需根据实际情况分析 |  |
| 红灯呼吸 | 错误状态，打印开始后对应槽没放料，**插入料线后恢复正常** |  |
| 红灯常亮 | 错误状态，第一阶段进料器检测没料，但是五通检测到有料，可能是料线断在五通内部 | 可参考 [拆解和清洁AMS五通组件](clean-the-filaments-hub.md) 清理堵塞物 |
| 4个槽都闪红灯 | 错误状态，AMS 通信异常 | 可参考 [AMS无法被打印机识别](AMS_is_not_detected_by_the_printer.md) 进行处理 |
| LED灯不亮 | 1.当某个槽插入料线后，其余没有料线的空槽的LED灯都不亮，这是正常的  2.当4个槽都是空的时候，如果某个槽的[LED始终不亮](ams-power-failure.md)，说明是进料器上电异常，需要检查线缆是否脱落 | 可根据[更换AMS上下料组件](../maintenance/replace-first-stage-feeder.md)重新安装线缆或进行对调测试 |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
