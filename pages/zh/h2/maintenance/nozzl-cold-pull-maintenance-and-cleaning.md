---
path: zh/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning
title: "H2D 喷嘴冷拔维护清理"
description: ""
tags: []
created: 2025-03-26T08:53:18.989Z
updated: 2025-03-26T12:13:42.629Z
source: https://wiki.bambulab.com/zh/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning
---

## 前言

在 3D 打印过程中，确保喷嘴干净、通畅至关重要，这直接关乎打印效果与质量。得益于 H2D 智能挤出电机，我们开发了一项实用功能，助力用户高效清理喷嘴。我们强烈建议您在日常使用中，运用该功能对喷嘴进行维护从而有效延长喷嘴的使用寿命。

以下是几种场景您必须进行冷拔维护：

1. 挤出电机频繁过载报错：当挤出电机在常规打印流量下频繁出现过载报错，这意味着喷嘴阻力过大，急需清理。
2. 打印耗材切换至 TPU 前：鉴于 TPU 材料对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，我们建议您在打印 TPU 前，对喷嘴进行冷拔清理，以保障打印顺畅。

> 注意：若喷嘴完全堵塞，无法进行常规冲刷操作，请先参考[热端堵塞清理](../troubleshooting/unclogging.md)，完成疏通后，再进行冷拔操作。  
> 喷嘴完全阻塞的测试标准：在挤出机装配喷嘴并稳定加热至 250℃后，使用 PLA 或 PETG 耗材进行进料测试。若观察到喷嘴底部无熔融物料挤出，或耗材挤出显著低于正常水平，即可判定为喷嘴完全阻塞。

## 冷拔参数的选择

经过系列测试我们确定了PLA和PETG在冷拔中表现优异。其他部分耗材在冷拔实验中表现欠佳，它们在冷拔过程中容易撕裂，进而残留在喷嘴内部。对于第三方厂家生产的清洁耗材，使用前请务必仔细阅读说明书，并在合适的条件下使用。以下为冷拔过程中的参数选择指南：

### 挤出机选择

左右挤出机均支持自动冷拔功能。若您要对 HF 喷嘴进行冷拔操作，建议选择右挤出机以显著提高冷拔成功率。

### 喷嘴选择

此处需输入您要进行冷拔的喷嘴参数。由于不同喷嘴的几何参数存在差异，我们针对各类喷嘴预设了相应参数。

### 冷拔耗材选择

冷拔耗材需同时承担三项核心功能：基于冲刷温度执行冲刷来去除喷嘴内部残留耗材、基于耗材打印温度回填喷嘴腔体、降温至冷拔温度通过冷拔操作带出内部杂质。对于不同型号喷嘴适配冷拔耗材存在差异：

- SF 喷嘴：推荐使用 PLA 或 PETG 作为冷拔耗材。
- HF 喷嘴：建议优先选用 PETG 进行冷拔，因为它具有更好的延展性。

### 冲刷温度选择

您可根据喷嘴使用过的最高温耗材来选择合适的冲刷温度：

- 250℃：适用于 PLA、PETG、TPU 、PVA等低温耗材。
- 290℃：适用于 ABS、ASA、PA、PC、PET等高温耗材。
- 320℃：适用于 PPS、PPA 等超高温耗材。

若您不确定该选择何种温度，可依据所拥有耗材的最高使用温度类别进行冲刷。

### 冷拔温度选择

冷拔通过精确控制喷嘴温度（建议设置于材料玻璃化转变温度以上20-30℃区间），利用材料黏弹性实现喷嘴内壁污染物的物理剥离。H2D已内置我们预先调试好的参数表，您可根据冷拔效果和成功率灵活调整，单次调整的步长建议为5℃。具体调整方向如下：

- 若在冷拔过程中发现阻力较大且耗材易拉断，建议提高冷拔温度。
- 若在冷拔时耗材在较小阻力下就被拉断，建议降低冷拔温度。

## 冷拔流程

### 功能入口：

![1.gif](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/1.gif)

### 参数选择操作：

以右挤出机使用0.4 标准流量(SF)喷嘴使用PLA进行冷拔操作为例：

![2.gif](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/2.gif)

### 拆卸 PTFE 管：

本指南以清洁右热端为例，因此您仅需右侧的 PTFE 管。

![20250325115623_rec__(1).gif](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/20250325115623_rec__(1).gif)

### 机器自动冲刷冷拔：

在工具头和热床运动到指定位置后，请您截取至少 30cm 长的耗材，加载至对应热端。

![](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/image-3.png)

![20250325115737_rec__(1).gif](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/20250325115737_rec__(1).gif)

在该过程中机器会自动执行冲刷及耗材回填的动作，在降至冷拔温度后，挤出机会自动缓慢冷拔至耗材丝缩颈处抵达挤出机，然后需要您进行后续的耗材拔出操作。

> 注意：
>
> - 机器进入自动流程后喷嘴将会升温，请勿用手触摸喷嘴避免烫伤
> - 在机器自动冲刷冷拔的过程中，可能由于冲刷温度过高产生烟雾。请关闭机器前盖以及上盖，等待冲刷完成后再打开。

### 用户自助冷拔：

> 冷拔时喷嘴温度仍然维持在您设置的冷拔温度，操作中避免直接接触喷嘴发生烫伤。

在机器提示您进行手动冷拔后，握住挤出机上方的耗材进行冷拔，在冷拔的过程中请缓慢向上冷拔出耗材，过快的冷拔速度以及倾斜角度拔出会导致耗材断裂。

![4.gif](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/4.gif)

### 评估冷拔效果：

在已拉出的耗材末端（如下图为 HF 喷嘴）上，需重点关注以下质量指标：

![](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/image-1.png)

1. **色泽一致性**：已拉出耗材丝不得夹杂异色杂质或碳化沉积物。
2. **表面洁净度**：已拉出耗材丝表面需呈现均质化熔融状态，无颗粒状烧结物附着。

我们强烈建议您建议多次重复冷拔直至挤出的耗材丝达到表面洁净无异常物质残留（如下图所示为 HF 喷嘴）。

![](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/image.png)

### 装回 PTFE 管：

本指南以清洁右热端为例，由于仅移除了右侧的 PTFE 管，因此仅需重新连接右侧的 PTFE 管。

![3.gif](https://wiki.bambulab.com/h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning/3.gif)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
