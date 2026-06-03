---
path: zh/filament-acc/filament/support-for-abs
title: "Support for ABS 打印指南"
description: ""
tags: []
created: 2024-07-05T06:50:55.623Z
updated: 2026-05-12T06:39:02.487Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/support-for-abs
---

## **预设配置文件**

下载、打开以下 .3mf 文件后，下文提到的打印参数已自动调整，导入目标打印模型的 **.stl 文件**后即可应用这些参数，无需再次调整。  
  
如果需要使用其他型号的打印机打印，可直接选择对应的型号，根据提示选择使用修改值，即可迁移相应的工艺参数和耗材丝参数。  
  
[Bambu Support for ABS（普通支撑）.3mf](https://wiki.bambulab.com/filament-acc/filament/support-for-abs-printing-guide/bambu_support_for_abs（普通支撑）.3mf)  
  
[Bambu Support for ABS（树状支撑）.3mf](https://wiki.bambulab.com/filament-acc/filament/support-for-abs-printing-guide/bambu_support_for_abs（树状支撑）.3mf)

![](https://wiki.bambulab.com/filament-acc/filament/support-for-abs-printing-guide/import-and-apply-cn.apng)

## 打印前的准备和防护

Support for ABS 的主要成分是高抗冲聚苯乙烯 (HIPS)，它对水分不敏感，不容易从空气中吸收水分，通常情况下无须在打印前进行烘烤。

在打印 Support for ABS 的过程中，会有类似打印 ABS 材料时出现的**刺激性气味（但较轻微），**因此建议**使用封闭式的打印机**进行打印，并注意在打印过程**保持环境通风和避免长时间近距离接触**

## 支撑参数设置

### 不支持可变层高

使用 Support for ABS 进行打印时，选择可变层高可能会导致打印失败，因此不建议使用可变层高进行打印。

### 关于模型主体的层间强度

当使用自动供料系统 (AMS) 打印支撑材料时，由于以下原因，与支撑处于同一高度的模型主体层间强度会有所降低：

- ABS 材料对层时间比较敏感，换料冲刷过程会增加层打印时间，导致一定程度的过度冷却，从而使层间强度降低。
- Support for ABS 是非极性的材料，在冲刷过程中较难被 ABS 材料冲刷干净，导致 ABS 材料中混入了支撑材料。由于支撑材料的层间强度较低，这种情况也会导致与支撑处于同一高度的模型主体层间强度降低。

通过以下参数设置，能在一定程度上减少模型层间强度的损失。

#### 冲刷量

如下图所示，把从 Support for ABS 切换至 ABS 材料时的冲刷量增大至 800，从而降低两种材料在喷嘴的混合程度，减弱支撑材料对模型层间强度的影响。

![](https://wiki.bambulab.com/20240709-102534.jpg)

#### 擦拭塔

- 增大擦拭塔的清理量。
- 关闭**冲刷到对象的填充/支撑**。
- 打开**界面材料不用于主体。**

|  |  |
| --- | --- |
| 提高清理量；关闭**冲刷到对象的填充/支撑选项** | 勾选**界面材料不用于主体选项** |

了解擦拭塔的更多信息，请参见[擦拭塔介绍](../../software/bambu-studio/parameter/prime-tower.md)。

#### 模型方向

由于打印机的打印方式是从低到高层层堆叠，因此模型内部的强度会比层与层的边缘粘合处更强。通过合理布置模型方向，避免模型在层间受力。

如下图所示，在模型受力面、受力点不变的情况下，通过调整模型的摆放角度，避免模型在层间方向上受力，因此左往右模型的强度依次降低。

![](https://wiki.bambulab.com/filament-acc/filament/support-for-abs/force-and-direction.png)

### 支撑的剥离性

通过以下参数设置，可以提高支撑的易剥离性。

#### 样式

使用普通支撑时，推荐设置样式为**缺省/网格**，如下图所示。

![](https://wiki.bambulab.com/样式.png)

#### 支撑面速度

提高支撑面速度，可以增加支撑的易剥离性。但如果支撑面速度过快，会增加模型翘曲的风险。

![](https://wiki.bambulab.com/filament-acc/filament/support-for-abs/支撑面速度中文.png)

#### 接触面层数

增加接触面层数，能够使支撑更容易剥离。

![](https://wiki.bambulab.com/接触面层数.png)

#### 树状支撑

如下图所示，在使用树状支撑时，建议调整参数使接触面完整并连结成片。

![](https://wiki.bambulab.com/支撑成片.png)

更详细的树状支撑功能，请参见[支撑耗材与支撑功能的介绍](../../software/bambu-studio/support.md)。

### 使用 H2D 打印 ABS 和 Support for ABS 时

1 需要把 ABS 的材料清理量提高至 90mm³；

![](https://wiki.bambulab.com/filament-acc/filament/support-for-abs/材料清理量.jpg)

2. 修改 ABS 的部件冷却风扇设置，提高最小风扇速度阈值为 50%。

![](https://wiki.bambulab.com/filament-acc/filament/support-for-abs/部件冷却风扇阈值.jpg)

## 可溶性

Support for ABS 除了可以作为易剥离支撑耗材来使用，还能够作为可溶性支撑溶解在 **d-柠檬烯**中。

**d-柠檬烯**是一种有机化合物，主要存在于柑橘类植物的果皮中，是许多精油的主要成分之一。它具有清新的柑橘类香气，能作为香料成分广泛应用于食品、化妆品和香水行业。它能够**溶解 HIPS**，因此可以去除 Support for ABS 打印的支撑。

**虽然柠檬烯通常被认为是安全的，但长时间暴露或吸入高浓度蒸气可能引起刺激，因此使用时应避免接触皮肤和眼睛，并戴好手套和口罩再进行支撑溶解和模型清洗的有关操作。使用完成后，应将柠檬烯放置在孩童接触不到的地方，并妥善处置溶解完支撑材料的废液。**

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
