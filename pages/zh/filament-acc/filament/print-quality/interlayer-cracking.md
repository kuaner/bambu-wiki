---
path: zh/filament-acc/filament/print-quality/interlayer-cracking
title: "模型层间开裂"
description: ""
tags: ["打印质量", "层间开裂"]
created: 2023-12-10T06:00:38.438Z
updated: 2026-04-14T08:52:33.254Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/interlayer-cracking
---

## 模型层间开裂

当模型层间附着力不足且材料收缩较明显时，打印件表面可能会沿 Z 方向出现开裂现象。此问题常见于 ABS、ASA、PC、PET-CF、PA-CF 等材料的打印过程中，具体表现如下图所示：

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%B1%82%E9%97%B4%E5%BC%80%E8%A3%82.png)

## 改善方法

### 疏通喷嘴

喷嘴的轻微堵塞可能导致打印过程中某一层无法挤出耗材，其表现形式也如开裂一样。

1. 疏通喷嘴  
   可参考喷嘴疏通教程，对喷嘴进行冷拔维护。  
   [H2D 喷嘴疏通教程](../../../h2/troubleshooting/unclogging.md)  
   [H2C 喷嘴疏通教程](../../../h2c/troubleshooting/unclogging.md)  
   [H2S 喷嘴疏通教程](../../../h2s/troubleshooting/nozzle-clog.md)  
   [A 系列喷嘴疏通教程](../../../a1-mini/troubleshooting/nozzle-clog.md)  
   [X1/P1 喷嘴疏通教程](../../../x1/troubleshooting/nozzle-clog.md)
2. 适当提高喷嘴温度或降低打印速度

   该方法可使挤出的耗材在与下层模型结合时具备更充足的时间，从而提升层间结合强度。以 ABS 为例，可将内墙速度降低至150 mm/s，外墙速度降低至100 mm/s。

   ![速度zh.png](https://wiki.bambulab.com/filament-acc/filament/print-quality/interlayer-cracking/%E9%80%9F%E5%BA%A6zh.png)
3. 减小部件冷却风扇转速

   预览该模型切片后的风扇转速，如下图内外墙部分的风扇转速为 60%，则降低“最大风扇转速”。

   ![风扇速度.png](https://wiki.bambulab.com/filament-acc/filament/print-quality/interlayer-cracking/%E9%A3%8E%E6%89%87%E9%80%9F%E5%BA%A6.png)
4. 适当调高热床温度 5-10 度，如果设备拥有仓温主动加热，请调高仓温 5 度。

   该方法能够稍微改善耗材收缩现象，从而避免开裂。  
   ![热床温度.png](https://wiki.bambulab.com/filament-acc/filament/print-quality/interlayer-cracking/%E7%83%AD%E5%BA%8A%E6%B8%A9%E5%BA%A6.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
