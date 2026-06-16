---
path: zh/p2s/troubleshooting/clogging
title: "P2S 堵塞排查"
description: "本文介绍如何进行 P2S 堵塞排查"
tags: []
created: 2025-10-14T13:14:59.368Z
updated: 2026-06-12T03:08:30.576Z
source: https://wiki.bambulab.com/zh/p2s/troubleshooting/clogging
---

## 适用场景

打印机报错挤出电机过载、空打或者打印机未报错，但是可以观察喷嘴无法出料。

## 问题可能发生的位置

**1. 挤出机组件  
2. 喷嘴**

## 所需工具

- H1.5 和 H2.0 内六角扳手

## 排障步骤

### 步骤 1. 移除喷嘴

打开工具头前盖，按压连接器锁扣后拔出连接插头，取下工具头前盖。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder-cleaning-guide/image-6.png)

确认喷嘴温度处于室温，按压切刀切断耗材。

[](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder-cleaning-guide/20250909-095953.mp4)

用手握住硅胶套高温标识的两侧，用力斜向下拉，取下硅胶套。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/remove_silicone_003.png)

解锁喷嘴卡扣。

|  |  |
| --- | --- |
|  |  |

握住喷嘴散热片上下两端（避免高温烫伤），取下喷嘴。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/remove_hotend_008.png)

### 步骤 2. 手动挤出

取下喷嘴后，将耗材送入挤出机并尝试手动挤出，点击屏幕上的挤出键。如果打印机提示“请将喷嘴加热至170℃以上”，可选择“本次不再提醒”。

![](https://public-cdn.bblmw.com/wiki/new/p2s/troubleshooting/clogging/down.png)

若耗材顺利挤出，说明很可能是喷嘴堵塞了，建议您参考 [P2S 喷嘴堵塞清理指南](../maintenance/cold-pull-maintenance-hotend.md) 清理疏通喷嘴。

![](https://wiki.bambulab.com/p2s/manual/jichu2.webp)

若耗材无法正常挤出或回抽，说明挤出机故障或者卡料，建议您参考 [P2S 挤出机堵塞清理指南](../maintenance/extruder-cleaning-guide.md) 清理挤出机。

## 功能验证

启动打印机，依次完成一次上料与退料操作。

- 若能正常连续出料且无异响/空打，说明挤出通道已恢复正常。
- 若仍无法正常出料或伴随异响/空打，**可能是挤出机和喷嘴组件同时存在堵塞**，请参考 [P2S 喷嘴堵塞清理指南](../maintenance/cold-pull-maintenance-hotend.md) 进行喷嘴清理后再验证。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
