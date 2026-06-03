---
path: zh/filament/support
title: "支撑耗材指南"
description: ""
tags: ["耗材"]
created: 2025-10-10T01:49:27.982Z
updated: 2026-05-20T07:17:57.629Z
source: https://wiki.bambulab.com/zh/filament/support
---

## 1. 耗材基本信息

支撑耗材可以确保支撑面和被支撑面零距离接触，因此可以保证模型的被支撑面获得光滑的打印效果，保护模型的复杂细节。

详细信息可以进入官方商详中查看: [支撑耗材](https://bambulab.tmall.com/category-1692717259.htm?spm=a1z10.5-b-s.w4010-25176969462.19.248f7eabP7zheW&search=y&parentCatId=1692717251&parentCatName=3D%B4%F2%D3%A1%BA%C4%B2%C4&catName=%D6%A7%B3%C5%B2%C4%C1%CF#bd)

![1280x1280_ch.jpg](https://wiki.bambulab.com/filament-acc/support/1280x1280_ch.jpg)

### 1.1 耗材介绍

以下为拓竹支撑耗材的简介：

| **耗材种类** | **可支撑耗材** | **特点** |
| --- | --- | --- |
| Support for ABS | ABS | 不溶于水，可溶于柠檬烯，适用于不便手动拆除支撑的场景。 |
| Support for PLA | PLA（PLA Aero 不适用） | 不易受潮，对烘干、防潮的要求较低。 |
| Support for PLA/PETG | PLA ＆ PETG | 有一定受潮风险，建议放置在干燥的环境下存储。 |
| Support for PA/PET | 所有 PA 与 PET 系列均可（例 PA6-CF，PET-CF） | 易受潮，对烘干、防潮的要求很高需密封保存。 |
| PVA | PLA 与 PLA-CF/GF | 极易受潮，对烘干、防潮的要求很高需密封保存；可溶于水，适用于不便手动拆除支撑的场景。 |

> **重要提醒：**  
> 1.**打印时请确保支撑耗材与主体耗材匹配。若两种耗材不匹配，可能会导致挤出机或喷嘴堵塞等故障。**  
> 2.**不支持使用 PVA 来支撑 PETG 耗材。** 打印 PVA 前建议查阅 [PVA 打印指南](../filament-acc/filament/pva-printing-guide.md)。

### 1.2 硬件兼容性

#### 耗材兼容性一览

| 支撑耗材 | 说明 |
| --- | --- |
| **Support for PLA/PETG** | **打印机兼容性：** 所有打印机兼容 **喷嘴兼容性：** 所有喷嘴均适配 **打印板兼容性：** 均适配 **配件兼容性：** AMS 系列全兼容 |
| **Support for PA/PET** | **打印机兼容性：** 不兼容 A1 系列、P1P **喷嘴兼容性：** 不适配 0.2 mm 口径喷嘴 **打印板兼容性：** 均适配 **配件兼容性：** AMS Lite 不兼容 |
| **Support for ABS** | **打印机兼容性：** 同上（不兼容 A1 系列、P1P） **喷嘴兼容性：** 不建议使用 0.2 mm 口径喷嘴 **打印板兼容性：** 均适配 **配件兼容性：** AMS Lite 不兼容 |
| **PVA（水溶支撑）** | **打印机兼容性：** 全部打印机兼容，但不推荐 A 系列。H2 系列无法同时使用左右喷嘴混打 **喷嘴兼容性：** 不建议使用 0.2mm 口径喷嘴 **打印板兼容性：** 均适配 **配件兼容性：** AMS Lite 不建议使用 |

> 注意：**不建议使用 A 系列搭配 AMS lite 打印 PVA 耗材。**  
> PVA 耗材在烘干后较硬，可以使用 AMS lite 正常送料进行打印。但是在潮湿状态下会变软，导致打印失败。AMS lite 为开放式结构，耗材直接接触空气，因此在打印过程中有可能会进一步吸水变软，导致**打印失败**。

## 2. 打印准备

### 2.1 耗材烘干

部分支撑耗材由于其材质原因，存放一段时间后，它会缓慢吸收空气中的水分，且存放时间越长、环境湿度越高，吸水量越大。这几类耗材建议打印前都进行一次烘干：PVA ＆ Support for PA/PET ＆ Support for PLA。且将其放入密封环境中存储。

> 提示：烘干流程可以参考[耗材打印前的干燥指南](../filament-acc/filament/dry-filament.md)。

具体各种耗材的烘干温度及烘干时间建议如下：

| 耗材类型 | 耗材 | **鼓风式烤箱** | **热床** | **AMS HT/AMS 2pro** | 打印前烘干 | 打印中防潮 |
| --- | --- | --- | --- | --- | --- | --- |
| 机械剥离型 | Support for PA/PET | 75 °C, 8 h | 65 - 75 °C, 12h | AMS 2Pro: 65°, 12h AMS HT: 80℃, 12h | **需要烘干** | **需要防潮** |
|  | Support for PLA/PETG | 75 °C, 8 h | 65-75℃, 12H | 60℃, 12H | **需要烘干** | **需要防潮** |
|  | Support for PLA | 55℃, 8h | 65-75℃, 12H | 60℃, 12H | 无特殊要求 | - |
|  | Support for ABS | 80 °C, 4 h | 85 - 95 °C, 6 h | AMS 2Pro: 65°, 4h AMS HT: 80℃, 4h | - | - |
| 水溶型 | PVA | 80℃, 8 - 12h | 90 - 100 °C, 12h | AMS 2Pro: 65°, 18h AMS HT: 85℃, 18h | **需要烘干** | **需要防潮** |

Support for ABS、PVA、Support for PA/PET 对于烘干条件要求严苛，AMS 2 Pro 由于温度限制无法将耗材彻底烘干，如需要更好的烘干效果建议通过鼓风式烤箱或配合 AMS HT 使用进行深度烘干。

> **注意：**
>
> 使用热床进行耗材烘干时，请每隔 6 小时将耗材翻面一次，并在耗材上方覆盖耗材包装盒或 PC 盒。

### 2.2 PVA 打印注意事项

- **PVA 可溶于水，对湿气极为敏感，因此对烘干和保存有更严格的要求。**
- 为避免打印质量问题，需在打印前对受潮耗材进行充分烘干；**在打印过程中，应始终将耗材存放在密封容器或 AMS 中，并配合干燥剂使用**，确保环境湿度保持在 **20% RH 以下**，以防耗材在烘干后迅速再次吸潮。
- 另外，耗材烘干后会变硬，这是正常现象。
- **不支持使用 PVA 来支撑 PETG 耗材。**

> 名词解释：
>
> 这里的 **RH** 是 **Relative Humidity** 的缩写，中文叫**相对湿度**。
>
> - **湿度 (Humidity)** 指空气中所含水汽的多少。
> - **相对湿度 (RH)** 则是一个百分比，表示当前空气中实际含有的水汽量与在该温度下空气所能容纳的最大水汽量的比值。
> - RH 越低，空气越干燥；RH 越高，空气越潮湿。

![支撑耗材_篇_ch.jpg](https://wiki.bambulab.com/filament-acc/support/%E6%94%AF%E6%92%91%E8%80%97%E6%9D%90_%E7%AF%87_ch.jpg)

#### 2.2.1 H2D 机型

1. **H2D 搭配 AMS HT 使用**

当搭配 AMS HT 使用时就可以进行边打边烘，但 AMS HT 无法使用自动进退料功能，但可作为干燥箱使用，防止材料受潮。以下是操作步骤：

**步骤1：开启烘干**

**开启烘干模式，并关闭烘干时旋转料盘**功能，将温度设置为 85 ℃ 左右。

![](https://wiki.bambulab.com/filament-acc/support/image.png)

**步骤2：进料**

**建议将 AMS HT 放置在机器上方，使用 TPU 专用出料口出料，其出料口到打印机的进料口（如 H2D 应使用 TPU 进料口）间最好有料管连接，以避免材料过早的变形。**

![image-29.png](https://wiki.bambulab.com/filament-acc/support/image-29.png)

**步骤3：确保耗材能够正常挤出**

在进料时，请先先尝试手动送入耗材，在手动挤出耗材的过程中检查喷嘴是否能顺利挤出耗材。

确认耗材已完全干燥，且挤出温度已正确设置在 **240℃–250℃** 后，若仍出现挤出不畅，或挤出时料线不能直线下垂等情况，请尝试冷拔喷嘴，或更换新的喷嘴。

|  |  |  |
| --- | --- | --- |
| 正常挤出示意图 | 异常挤出1 | 异常挤出2 |

2. **H2D 搭配其他密封盒使用**

H2D 可以通过切换喷嘴实现耗材切换，因此可以使用其他密封盒保持耗材的干燥，模型网站有相关优秀案例，可以参考 [MakerWorld 中的米桶模型](https://makerworld.com/zh/search/models?keyword=%E7%B1%B3%E6%A1%B6)。

![image-30.png](https://wiki.bambulab.com/filament-acc/support/image-30.png)

#### 2.2.2 其他机型

X 系列、P 系列、H2S 打印 PVA 耗材时，均需要搭配 AMS 进行换料。因此无法边烘干边打印，需要做好打印前耗材的干燥与打印时耗材的防潮保存。PVA 耗材用在 AMS Lite 上时则不建议打印过长时间（约 1h 以内），长时间打印容易让 PVA 再次受潮从而影响打印质量。

**打印时的耗材防潮工作也需要做到位**，建议更换新的干燥剂并盖好 AMS 上盖，确保其中湿度小于 20% RH，以避免已经烘干过的耗材过快地再次受潮。

![image-31.png](https://wiki.bambulab.com/filament-acc/support/image-31.png)

## 3. 参数设置

### 3.1 Support for ABS

> 提示：Support for ABS 的主要成分是高抗冲聚苯乙烯 (HIPS)，它对水分不敏感，不容易从空气中吸收水分，通常情况下无须在打印前进行烘烤。  
> 在打印 Support for ABS 的过程中，会有类似打印 ABS 材料时出现的**刺激性气味（但较轻微）**，因此建议**使用封闭式的打印机**进行打印，并需要在打印过程中**保持环境通风，尽量避免长时间近距离接触**。

> 注意：使用 Support for ABS 进行打印时，选择可变层高可能会导致打印失败，因此不建议使用可变层高对这种耗材进行打印。

ABS 材料对层时间比较敏感，换料冲刷过程会增加层打印时间，导致一定程度的过度冷却，从而使层间强度降低。同时 Support for ABS 是非极性的材料，在冲刷过程中较难被 ABS 材料冲刷干净，导致 ABS 材料中混入了支撑材料。由于支撑材料的层间强度较低，这种情况也会导致与支撑处于同一高度的模型主体层间强度降低。

因此建议按照以下两个参数设置，能在一定程度上减少模型层间强度的损失。

1. 如下图所示，把从 Support for ABS 切换至 ABS 材料时的**冲刷量增大至 800**，从而降低两种材料在喷嘴的混合程度，减弱支撑材料对模型层间强度的影响。

![](https://wiki.bambulab.com/filament-acc/support/image-6.png)

2. 调整清理参数

![image-32.png](https://wiki.bambulab.com/filament-acc/support/image-32.png)

![](https://wiki.bambulab.com/filament-acc/support/image-9.png)

同时建议您使用普通支撑时，推荐设置样式为**缺省/网格。**

![](https://wiki.bambulab.com/filament-acc/support/image-10.png)

如您是 H2D 机型需要把 ABS 的材料清理量提高至 90 mm³。ABS 的部件冷却风扇设置，提高最小风扇速度阈值为 50%。

![image-33.png](https://wiki.bambulab.com/filament-acc/support/image-33.png)

> 提示：Support for ABS 除了可以作为易剥离支撑耗材来使用，还能够作为可溶性支撑溶解在 **d-柠檬烯**中。
>
> **d-柠檬烯**是一种有机化合物，主要存在于柑橘类植物的果皮中，是许多精油的主要成分之一。
>
> **虽然柠檬烯通常被认为是安全的，但长时间暴露或吸入高浓度蒸气可能引起刺激，因此使用时应避免接触皮肤和眼睛，并戴好手套和口罩再进行支撑溶解和模型清洗的有关操作。使用完成后，应将柠檬烯放置在孩童接触不到的地方，并妥善处置溶解完支撑材料的废液。**

### 3.2 机械剥离型耗材

除了 PVA 支撑耗材外，其他的支撑耗材都可以在 Bambu Studio 中选择支撑/筏层界面耗材，切片软件会自动弹窗提示自动设置以下工艺参数:

![](https://wiki.bambulab.com/filament-acc/support/20250901153048_rec_.gif)

自动参数适用于大部分场景，打印效果可以参考下图：

![image-34.png](https://wiki.bambulab.com/filament-acc/support/image-34.png)

### 3.3 PVA 支撑耗材（水溶型）

PVA 支撑耗材需要主体与界面一致，且支撑种类需要切换成普通支撑，提高其稳定性。

|  | 支撑类型 | 支撑界面 | 支撑主体＆支撑界面 | 打印效果 |
| --- | --- | --- | --- | --- |
| **PVA** | 建议普通支撑 | 不建议只在支撑界面使用 | 建议支撑主体＆支撑界面都使用 |  |

使用 PVA 耗材作为支撑主体时，**应尽量避免切片时使用树状支撑（局部过于瘦高、单薄），** 以免打印过程中树状支撑倒塌。为了获得较好的效果，推荐按照以下切片设置，使用普通支撑进行打印。更详细的 PVA 参数设置可以参考 [PVA 打印指南](../filament-acc/filament/pva-printing-guide.md)。

![image-35.png](https://wiki.bambulab.com/filament-acc/support/image-35.png)

## 4. 打印完成模型后处理及耗材保存

### 4.1 支撑拆除

#### 4.1.1 机械剥离型

除 PVA 耗材外，其他支撑耗材都适合手动剥离。

> 注意：在使用 **Support for PA / PET** 建议在打印后 **2 小时内**移除支撑结构，以防止其吸湿后粘连。如果发生粘连，请将模型干燥以便于移除。

![image-17.png](https://wiki.bambulab.com/filament-acc/support/image-17.png)

#### 4.1.2 水溶性（PVA）耗材支撑溶解

打印结束后，将模型放入水中浸泡，可以轻松溶解、去除 PVA 支撑。溶解过程可能要几个到十几个小时。**使用温水和搅拌可加速 PVA 的溶解，但如果模型主体为耐热性较低的 PLA 时，水温不宜超出 50 ℃，以免模型变形。**

| **浸泡前** | **浸泡几小时后（部分溶解）** | **浸泡完全后（随后晾干即可）** |
| --- | --- | --- |
|  |  |  |

因 FDM 3D 打印的大部分模型内部有较多孔隙，泡水溶解支撑时，部分模型内部可能会进水。若要降低模型内部进水的风险，可参考[降低打印件漏液风险指南](reduce-vase-leaking-guide.md)中的内容进行参数设置修改。

#### 4.1.3 Support for ABS 的支撑拆除

**1. 机械剥离**

对于不复杂的支撑结构，可直接通过手动剥离 Support for ABS 支撑。

**2. 柠檬烯溶解**

对于较为复杂的支撑结构，可以使用 **d-柠檬烯** 溶解 Support for ABS 支撑。

d-柠檬烯是一种有机化合物，主要存在于柑橘类植物的果皮中，是许多精油的主要成分之一。

虽然柠檬烯通常被认为是安全的，但长时间暴露或吸入高浓度蒸气可能引起刺激。

因此，使用柠檬烯时，需要注意以下使用规范及安全要求：

- 请佩戴**氟橡胶手套**或**多层复合膜手套**；禁止使用乳胶手套——柠檬烯会快速渗透并溶胀乳胶。
- 请佩戴口罩。
- 在**通风良好**的环境中操作。
- 柠檬烯闪点仅约 48°C，**严禁在明火、热床高温裸露面**附近操作。
- 使用完成后，应将其放置在孩童接触不到的地方，并妥善处置溶解完支撑材料的废液。

![support_for_abs_removing_cn.jpg](https://wiki.bambulab.com/filament-acc/support/support_for_abs_removing_cn.jpg)

### 4.2 耗材存储

除了 Support for ABS 与 Support for PLA 外。其他耗材建议在打印后进行密封存储。

尤其是 PVA 耗材极易吸水受潮，所以烘干后**无需等它冷却**就要立刻放入干燥环境内（干燥箱或 AMS ）。在 20% RH 的干燥环境中，PVA 耗材保持干燥时长约为 1 ~ 3 天；**在通常的 55% RH 左右的室内环境中，刚烤干的 PVA 耗材会在约 1 ~ 3 小时内受潮到会使打印质量下降的程度**，潮湿天气时会更快。

- **AMS**

请定期更换干燥剂，确保 AMS 内湿度小于 20% RH。打印前进行烘干。

![](https://wiki.bambulab.com/filament-acc/support/image-21.png)

- **其他密封容器**

模型网站有相关优秀案例，可以参考：[搜索:米桶 - MakerWorld](https://makerworld.com/zh/search/models?keyword=%E7%B1%B3%E6%A1%B6)

![](https://wiki.bambulab.com/filament-acc/support/image-22.png)

## 5. 常见打印问题与解决方案

在打印中遇到使用专用支撑耗材打印问题时可以参考以下几个方案：

### 5.1 堵头

如果您遇到 **PVA 堵头** 的情况，建议先对耗材进行**深度烘干**，并在密封环境中**配合干燥剂保存**。  
由于 PVA 是水溶性材料，吸湿性极强，即使在常规环境下也会迅速吸收空气中的水分；当环境湿度超过 50% 时，更容易出现明显受潮甚至结块的情况。  
当潮湿的 PVA 进入高温喷嘴（通常为 190–210℃）时，内部水分会瞬间汽化，产生大量蒸汽气泡，可能会导致挤出机堵塞。

### 5.2 使用专用支撑后出现支撑面质量差

1. 如果模型主体支撑面出现脱线情况，建议将冲刷量适当增大，可将参数提高至原来的约两倍（如由 30 调整为 60 mm³）。

![](https://wiki.bambulab.com/filament-acc/support/image-23.png)

2. 如果是出现了支撑面不光滑，不规整的情况可以先确定一下参数是否有设置正确（只有 PVA 需要主体与界面都调为支撑耗材）。

![](https://wiki.bambulab.com/filament-acc/support/20250901151952_rec_.gif)

### 5.3 支撑难剥离

如果出现剥离困难的情况可以参考以下方案调整。

调整桥接速度：可以适当增大桥接速度，例如增大到100 - 150mm/s 之间。

![](https://wiki.bambulab.com/filament-acc/support/image-24.png)

对于易吸水的 PA-CF、PA6-CF 等 PA 类主体材料和易吸水的 PVA、Support for PA/PET 等支撑材料而言。若确实已因放置太久而变得难拆，请把整个模型烘干、放置冷却后再及时拆除。

### 5.4 模型与支撑面不粘

由于支撑材料的特殊性，可能会出现模型与支撑面不粘的情况，建议参考以下方式调整：

1. 修改支撑面速度：数值越大，速度越快，支撑易拆除，支撑不牢固易倒塌；降低则效果相反。

![](https://wiki.bambulab.com/filament-acc/support/image-25.png)

2. 调整 Z 距离：增大间隙，支撑接触面减少，沾附力减弱，支撑易拆除，悬垂表面质量差；降低则效果相反。

![](https://wiki.bambulab.com/filament-acc/support/image-26.png)

> 注意：如遇到的打印问题非以上两点，可以进入该链接中根据图片展示的现象对应处理：[打印质量与解决办法](../filament-acc/filament/print-quality.md)

## 6. 进阶学习

### 6.1 通过预览查看支撑生成效果

如下左图为模型切片后的示意图，如下右图是只显示模型支撑部分的图示。

![image-36.png](https://wiki.bambulab.com/filament-acc/support/image-37.png)

### 6.2 支撑参数设置

对于支撑的设置可以参考下面这篇 wiki 进行调节：[支撑耗材与支撑功能的介绍](../software/bambu-studio/support.md)。

> 提示：
>
> 如果以上的进阶调整无法满足您的需求，可以进入到“拓竹学院”——“[Bambu Studio](https://bambulab.cn/zh-cn/support/academy)”中进行学习，这是一个 3D 打印学习平台，致力于为用户提供从基础到进阶的全方位 3D 打印知识培训，助力用户在 3D 打印领域不断提升技能，实现创新与发展。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
