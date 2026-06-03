---
path: zh/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning
title: "H2C 喷嘴冷拔维护清理"
description: ""
tags: []
created: 2025-11-18T13:21:12.638Z
updated: 2026-01-19T04:20:07.011Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning
---

## 前言

在 3D 打印过程中，确保喷嘴干净、通畅至关重要，这直接关乎打印效果与质量。得益于 H2C 智能挤出电机，我们开发了一项实用功能，助力用户高效清理喷嘴。我们强烈建议您在日常使用中，运用该功能对喷嘴进行维护从而有效延长喷嘴的使用寿命。

以下是几种场景您必须进行冷拔维护：

1. 挤出电机频繁过载报错：当挤出电机在常规打印流量下频繁出现过载报错，这意味着喷嘴阻力过大，急需清理。
2. 打印耗材切换至 TPU 前：鉴于 TPU 材料对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，我们建议您在打印 TPU 前，对喷嘴进行冷拔清理，以保障打印顺畅。

> 注意：若喷嘴完全堵塞，无法进行常规冲刷操作，请先参考[热端堵塞清理](../../h2/troubleshooting/unclogging.md)，完成疏通后，再进行冷拔操作。  
> 喷嘴完全阻塞的测试标准：在挤出机装配喷嘴并稳定加热至 250℃后，使用 PLA 或 PETG 耗材进行进料测试。若观察到喷嘴底部无熔融物料挤出，或耗材挤出显著低于正常水平，即可判定为喷嘴完全阻塞。

## 冷拔参数的选择

经过系列测试我们确定了PLA和PETG在冷拔中表现优异。其他部分耗材在冷拔实验中表现欠佳，它们在冷拔过程中容易撕裂，进而残留在喷嘴内部。对于第三方厂家生产的清洁耗材，使用前请务必仔细阅读说明书，并在合适的条件下使用。以下为冷拔过程中的参数选择指南：

### 挤出机选择

左右挤出机均支持自动冷拔功能。若您要对 HF 喷嘴进行冷拔操作，建议选择右挤出机以显著提高冷拔成功率。

### 喷嘴选择

此处需输入您要进行冷拔的喷嘴参数。由于不同喷嘴的几何参数存在差异，我们针对各类喷嘴预设了相应参数。

### 冷拔耗材选择

冷拔耗材需同时承担三项核心功能：基于冲刷温度执行冲刷来去除喷嘴内部残留耗材、基于耗材打印温度回填喷嘴腔体、降温至冷拔温度通过冷拔操作带出内部杂质。对于不同型号喷嘴适配冷拔耗材存在差异：

- SF 喷嘴（标准）：推荐使用 PLA 或 PETG 作为冷拔耗材。
- HF 喷嘴（高流量）：建议优先选用 PETG 进行冷拔，因为它具有更好的延展性。

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

### 步骤 1. 开始前的准备

在打印机触控屏主界面，按以下路径操作：

1. 导航至 “设置” 菜单（标识 1）；
2. 选择 “工具箱” 按钮（标识 2）；

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/1.png)

3. 在菜单中找到并点击 “喷嘴冷拔维护” 选项（标识 3），即可进入冷拔程序准备界面。

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/2.png)

### 步骤 2. 冷拔参数设置与准备

点击界面中的 “下一步” 按钮。

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/3.png)

进入冷拔参数配置页面，菜单将显示以下可配置选项（参考下图）：

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/4.png)

1. **选择清洁喷嘴：** 根据需求勾选 “左侧” 或 “右侧” 喷嘴（与待清理堵塞的喷嘴一致）；
2. **选择清洁耗材：** 优先推荐 PLA 或 PETG 耗材；建议选用颜色比之前使用的耗材更浅，或对比度更高的型号，便于后续观察是否带出残留杂质、碎屑；
3. **指定喷嘴规格：** 准确选择当前安装的喷嘴尺寸（如 0.4 mm、0.6 mm 等）及类型；
4. **选择残留耗材类型：** 勾选堵塞时正在使用，或最近一次使用的耗材类型（机器会自动匹配该耗材的适配加热温度，确保残留耗材充分软化）。

所有参数配置完成后，点击 “**开始**” 按钮，启动冷拔清洁程序。

### 步骤 3. 拔出 PTFE 管

1. 按照屏幕提示，按住两个黑色气动接头的外圈，同时将上方 PTFE 管拔出。

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/5.webp)

2. 点击 “**已完成，完成**”，继续下一步。

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/8.png)

### 步骤 4. 插入耗材并启动自动程序

1. 按照屏幕提示，将步骤 2 中选定的清洁耗材（PLA 或 PETG）从进料口插入并推至就位。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/20.webp)

2. 确认安装到位后，点击界面上的“已完成，继续”。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/19_improve.png)

3. 接下来设备将自动完成以下步骤（无需手动操作）：

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/21_improve.png)

- 将喷嘴加热至预设温度；
- 清除喷嘴内残留的旧耗材；
- 将喷嘴冷却至适合冷拔的温度。

### 步骤 5. 取出耗材并复位 PTFE 管

1. 出现提示后，请 **缓慢、匀速**手动拉出耗材（耗材前端可能带出堵塞杂质）。

|  |  |
| --- | --- |
|  |  |

> **注意：** 冷拔过程中请垂直且缓慢向上拉出耗材；过快或倾斜用力易导致断丝。

2. 耗材完全取出后，点击“**已完成，继续**”。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/23_improve.png)

3. 随后界面将显示清洁后的参考示例，供您比对：

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/24_improve.png)

- 若取出的耗材表面仍有残留物、焦块或异色杂质，请重复冷拔流程，直至耗材前端干净平整；
- 若耗材前端光滑且无附着物，则表示清理完成。

4. 最后，将 PTFE 管复位并按压至位（确保牢固），点击“**OK**”（标识 1），即可完成本次冷拔维护流程。

|  |  |
| --- | --- |
|  |  |

## 评估冷拔效果

在已拉出的耗材末端（如下图为 HF 喷嘴）上，需重点关注以下质量指标：

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/6.png)

1. 色泽一致性：已拉出耗材丝不得夹杂异色杂质或碳化沉积物。
2. 表面洁净度：已拉出耗材丝表面需呈现均质化熔融状态，无颗粒状烧结物附着。

我们强烈建议您建议多次重复冷拔直至挤出的耗材丝达到表面洁净无异常物质残留（如下图所示为 HF 喷嘴）。

![](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/7.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
