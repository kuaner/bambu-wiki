---
path: zh/software/bambu-studio/filament-mapping-principle
title: "Bambu Studio 发起打印时耗材映射原则"
description: "本文将详细介绍 Bambu Studio 在发起打印任务时，系统如何将切片预设与 AMS 实际耗材进行关联，帮助您理解自动映射机制，避免因错误分组导致的打印质量问题。"
tags: []
created: 2026-01-16T06:08:22.326Z
updated: 2026-01-26T08:19:42.753Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/filament-mapping-principle
---

## 核心原则：工艺安全优先于视觉匹配

在 Bambu Studio 发起打印任务时，系统会自动将“切片预设耗材”与“AMS 实际装载耗材”进行匹配。这套算法遵循：**优先确保打印成功率与质量，其次才考虑颜色一致性。**

Bambu Studio 会按以下优先级进行逻辑判断：

1. **第一优先级：耗材预设参数匹配** —— 保质量
2. **第二优先级：颜色匹配** —— 保外观

### **原则一：耗材类型匹配**

为了确保打印质量。耗材“大类”（如都是 PETG）需要一致，必须细分型号（如 CF 与 HF）推荐选择一致。这是因为不同型号在最大体积流速、熔融温度及冷却需求上存在物理差异，混用极易导致堵头或打印失败。因此，Bambu studio 会优先锁定参数完全一致的料槽。

### **原则二：耗材类型一致的前提下，优先匹配颜色**

只有在确定型号匹配后，系统才会对比颜色代码（Hex Code）。优先选择颜色完全一致的料槽；若无完全匹配，则尝试寻找色系最接近的（如深红配粉红）。

> 如果使用的是外挂料盘，在发送打印页面不会自动匹配，需要您手动确认耗材类型。

## 场景案例

AMS 槽内同时有黄色的 PETG HF 和红色 PETG CF 两种材料。

![bbl1.png](https://wiki.bambulab.com/bambu-studio/zh1.png)

当使用黄色 PETG CF 发起模型打印时，Studio 会优先匹配耗材参数预设选择使用红色 PETG CF。

![zh.png](https://wiki.bambulab.com/bambu-studio/zh.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
