---
path: zh/filament-acc/filament/print-quality/under-extrusion
title: "模型缺料"
description: "了解如何识别并解决 3D 打印中的模型缺料问题。本指南介绍了整体缺料和局部缺料两种现象，并详细说明常见原因与解决方法。"
tags: ["打印质量", "模型缺料"]
created: 2023-12-10T05:51:53.569Z
updated: 2026-06-23T06:29:29.955Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/under-extrusion
---

## 模型缺料

模型缺料通常由**挤出不足**导致，可分为**整体缺料**和**局部缺料**两种现象。

- **整体缺料**：模型表面线条稀疏，表现如下。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E9%A1%B6%E9%9D%A2%E7%BC%BA%E6%96%99.png)

- **局部缺料**：模型表面局部范围内线条稀疏，表现如下。

|  |  |
| --- | --- |
|  |  |

  

## 常见原因与解决方法

缺料主要由以下三类原因引起，可对照排查并处理。

### 1. 挤出阻力过大

挤出路径上任一环节受阻，都会导致出料不足。常见情况如下：

| 具体原因 | 处理方法 |
| --- | --- |
| 料盘转动受阻或料线缠结 | 排除故障后重新打印。 |
| 料管进入异物、局部弯折或磨损 | 清除异物，并修复或更换料管。 |
| 挤出机齿轮卡住或损坏 | 清洁或更换齿轮。 |
| 喷嘴内部通道阻塞、出料困难（长时间打印或打印含纤维耗材后易发生） | 疏通喷嘴或更换新喷嘴。 |

  

### 2. 挤出量偏小

出料量跟不上打印需求时，同样会出现缺料。常见情况如下：

- **熔融速度不足**：耗材的熔融、挤出速度跟不上打印速度 ——可适当提高喷嘴温度或降低打印速度。
  - 若要开启“狂暴模式”（更高速打印），建议将喷嘴温度提高 `10 ℃` 左右，以加快耗材熔融。
  - 若要使用第三方耗材（可能不支持高速打印），请选择打印速度相对较低的 `Generic` 参数进行切片打印。
- **喷嘴阻塞**：喷嘴内部通道阻塞、出料困难 ——疏通喷嘴或更换新喷嘴。
- **流量比例不足**：若模型整个表面都明显缺料，可能是流量比例不足导致的，可在切片软件中适当调高流量比例。如果您使用的是 Bambu 官方耗材，建议保持默认流量比例，请勿随意修改。

![flow_rate.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/flow_rate.png)

### 3. 压力提前值设置错误

若缺料只出现在模型转角处（如下图），很可能是压力提前值设置错误，需重新进行流量标定（校准）。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%8E%8B%E5%8A%9B%E6%8F%90%E5%89%8D%E5%80%BC%E5%A4%AA%E5%A4%A7%E4%BA%86(pla0.1).png)

流量标定的作用是，确保工具头在加速、减速运动时，挤出量保持均匀，避免在变速节点出现多料或少料。压力提前值错误，有可能导致打印头变速瞬间挤出过多或过少。

P1P 和 X1 系列打印机的流量标定方法如下图所示。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/p1p%E6%B5%81%E9%87%8F%E6%A0%87%E5%AE%9A.png)

**X1 动态流量标定：**

![19_打印前选择动态流量校准.png](https://wiki.bambulab.com/software/bambu-studio/calibration/19_%E6%89%93%E5%8D%B0%E5%89%8D%E9%80%89%E6%8B%A9%E5%8A%A8%E6%80%81%E6%B5%81%E9%87%8F%E6%A0%A1%E5%87%86.png)

  

动态流量校准的本质，是在工具头加速、减速的过程中，找到合适的挤出补偿值，从而保证挤出线条均匀。

![20_x1打印前校准.png](https://wiki.bambulab.com/software/bambu-studio/calibration/20_x1%E6%89%93%E5%8D%B0%E5%89%8D%E6%A0%A1%E5%87%86.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
