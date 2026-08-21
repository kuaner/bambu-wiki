---
path: zh/software/bambu-studio/filament-track-switch-dynamic-mapping
title: "耗材变轨器动态映射切片功能介绍"
description: "本文介绍了耗材变轨器加装后 Bambu Studio 的动态映射功能"
tags: []
created: 2026-03-25T03:17:20.231Z
updated: 2026-08-19T12:16:38.771Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/filament-track-switch-dynamic-mapping
---

## 概述

耗材变轨器安装在双喷嘴打印机上后，可打破传统双头打印机中耗材与喷嘴的固定绑定关系。启用动态映射功能后，Bambu Studio 能在打印的不同阶段，为每种耗材灵活选择使用的喷嘴，从而减少不必要的冲刷浪费，并缩短整体打印时间。

## 如何启用动态映射？

**必须同时满足以下几个条件，动态映射才会生效：**

1. 打印机是双喷嘴机型，且已安装并连接好耗材变轨器（具体步骤请参考：[耗材变轨器使用指南](../../general/manual/filament-track-switch.md)）；
2. 在**准备**页面，点击“**编辑材料分组**”图标，选择**省料**模式，勾选底部“**启用智能耗材分配**”选项，并点击**确认**。

![smart_filament_assign_setup_zh.png](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/smart_filament_assign_setup_zh.png)

设置后，点击切片并开启打印，Bambu Studio 会提供一个最优耗材摆放建议，推荐将哪些耗材放入耗材变轨器的同侧（即同个 AMS 内）。按照此建议摆放耗材，可最大程度缩短实际打印时间。

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/022.png)

## 为什么动态映射更省料？

传统双喷嘴打印对耗材的分组采用**静态分组模式**，即切片前就将每种耗材固定分配给左或右喷嘴，且打印过程中分组保持不变。由于模型在不同高度使用的颜色组合常常变化，这种固定分配会导致浪费。以三色方块和带局部装饰色的支撑打印为例：

**示例一：三色方块模型**

在该方块模型中，按高度可以分为三个颜色区间：

①[绿, 红]

②[绿, 黄]

③[红, 黄]

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/003.png)

- **静态分组：**3 种颜色必须提前固定分配给 2 个喷嘴。无论怎么分配，总会有一个区间的两种颜色被分到同一个喷嘴。例如，若绿和黄都在左喷嘴时，打印 ②[绿, 黄]区间时，只能用左喷嘴单独切换，导致同一喷嘴内频繁换料冲刷，而右喷嘴则闲置。

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/017.png)  
![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/006.png)

- **动态映射：**动态映射可按区间灵活分配喷嘴。打印③[红, 黄]区间时，红色和黄色可分别由左右喷嘴打印；切换到②[绿, 黄]区间时，又可重新分配，使用不同喷嘴打印绿色和黄色。这样，每个区间都能充分利用双喷嘴，减少不必要的单喷嘴换料。**若喷嘴映射列表中出现“L R”，则表示本次打印过程中会动态切换使用左右喷嘴来打印该耗材。**

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/007.png)  
![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/008.png)

**示例二：带局部装饰色的支撑打印**

模型主体始终使用灰色耗材（模型材料）和橘色耗材（支撑材料），但中间约有 20 层需额外使用装饰色黄色。

- **静态分组：**黄色耗材必须在整个打印过程中一直占据着右喷嘴的位置，从而导致打印 [橘, 黄] 区间时，需要额外冲刷，而闲置左喷嘴。

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/019.png)

- **动态映射：**黄色耗材仅在需要的那 20 层临时“借用”左喷嘴，从而显著减少整体换料冲刷。

## 最优摆放建议与打印时长

### 耗材变轨器换料的两种模式

切片完成后提供的 **“最优耗材摆放建议”**，是基于耗材变轨器内部两种换料路径的耗时差异来计算的。

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/021.png)

耗材变轨器有两个进料口（In-A, In-B）和两个出料口（Out-A, Out-B）。换料时：

- **同进料口换料**：如果前后使用的两种耗材都连接在**同一个进料口**（例如都在 In-A），则换料时，系统需要先将当前耗材**完全退回 AMS**，再将新耗材从同一入口送入。这个过程涉及 AMS 完整的退料与进料，**耗时较长**。

  **示例**：若当前使用路径为 **AA**（In-A 进，Out-A 出），需要切换为 **AB**（In-A 进，Out-B 出）。尽管出料口不同，但进料口相同，因此必须将耗材完全退回 AMS，才能在同一进料口送入下一种耗材。

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/001.png)

- **异进料口换料**：如果前后使用的两种耗材连接在**不同的进料口**（例如从 In-A 切换到 In-B），换料时，当前耗材只需**退回到变轨器内部**，下一种耗材便可立即从另一进料口送入，省去了耗材在 AMS 与变轨器之间的往返，**速度显著更快**。

  **示例**：若当前使用路径为 **AB**（In-A 进，Out-B 出），需要切换为 **BA**（In-B 进，Out-A 出）。由于进料口不同，变轨器可以快速完成内部路径切换，实现高效换料。

![](https://wiki.bambulab.com/software/bambu-studio/filament-track-switch-dynamic-mapping/012.png)

**切片预估说明**：Bambu Studio 在切片时预估的换料时间，是以较快的 **“异进料口换料”** 耗时作为基准进行计算的。

- 如果您的耗材摆放符合最优建议，使**多数换料发生在不同进料口（异进料口换料）**，那么实际打印时间将**接近**切片预估时间。
- 如果耗材摆放偏离最优建议，导致**大量换料发生在同一进料口（同进料口换料**），那么实际打印时间将**显著长于**切片预估时间。

### 最优摆放的目标

Bambu Studio 会分析整个打印任务中的所有换料事件，统计出哪两种耗材之间的切换最频繁。

**最优摆放的目标，就是将切换最频繁的耗材连接到耗材变轨器的两个进料口**。这样，大多数频繁的换料操作都能走快速的“异进料口换料”通道。

**示例：**一个 4 色模型，耗材 A 与 B 之间切换 80 次，C 与 D 之间切换 60 次，而 A 与 C 或 B 与 D 之间的切换仅 10 次。最优建议将是：将 A 和 B 放入**不同进料口**（如 A 连 In-A，B 连 In-B），C 和 D 也放入**不同进料口**。这样，140 次高频换料都能走快速通道，只有 10 次低频换料走慢速通道。

> 按最优摆放建议放置耗材，实际打印时间往往比切片预估的时间**更短**。偏离建议时，同侧换料增多，实际时间会向切片预估甚至更长方向靠拢。

## 推荐的打印场景

**动态映射收益显著，推荐使用：**

- 不同高度段颜色组合变化明显的多色模型（如分段配色摆件、渐变模型）
- 颜色复杂的多色打印，且某些颜色仅出现在局部区域
- 预计有大量换料次数的长时间打印任务

**动态映射收益有限，普通双头模式即可：**

- 每层用到的颜色组合从头到尾完全一致的模型
- 只有 2-3 种颜色的简单双色模型
- 以功能性支撑为主、颜色单一的打印

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
