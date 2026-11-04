---
path: zh/knowledge-sharing/tpu-printing-guide
title: "TPU 打印指南"
description: "本文介绍了打印 TPU 的建议"
tags: ["tpu"]
created: 2023-08-02T08:20:33.025Z
updated: 2026-11-03T13:19:36.243Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/tpu-printing-guide
---

## 🧵 耗材介绍

TPU（热塑性聚氨酯）是一种柔性 3D 打印材料，兼具 **弹性**、 **柔韧性**、 **耐磨性** 和 **抗冲击性**， **可弯曲、可拉伸、易回弹**。常用于打印需要柔韧性、弹性或减震性能的功能性零件，例如休闲鞋、自行车坐垫、手表带、遥控车轮胎等。

TPU 有多种硬度可选，不同硬度可适配不同的应用场景。其硬度通常采用邵氏硬度（Shore Hardness）表示，例如 85A、90A、95A。其中， **数字** 表示软硬程度，数值越小，材料越柔软，数值越大，材料越硬； **字母** 表示测试标尺，TPU 通常使用测试柔性材料的 Shore A 标尺。

常见 TPU 硬度从硬到软大致为：77D > 70D > 68D > 55D > 95A > 90A > 85A > 83A > 80A > 75A > 70A。

拓竹 TPU 目前有两种线径，分别是 **1.75 mm** 与 **2.85 mm**。其中，TPU 75A 为 2.85 mm 线径，TPU 98A HF、TPU 85A、TPU 90A、TPU for AMS 为 1.75 mm 线径。

需要注意的是，由于 TPU 柔软易弯曲，所以相比 PLA、PETG 等常见硬质耗材打印难度较高，进料方式也较为特殊，对耗材干燥度、进料稳定性以及硬件适配性要求较高。

本文将详细介绍打印 TPU 的方法与注意事项，建议打印前仔细阅读本指南。

![1.jpg](https://wiki.bambulab.com/filament-acc/tpu/1.jpg)

> **耗材使用注意事项**：
>
> 1. 请在 **阴凉、避光、干燥** 环境中存放耗材，避免阳光直射或高温环境。
> 2. 请将耗材及折断的碎屑放在 **婴幼儿及宠物无法触及的地方**，避免吞咽和窒息的风险。
> 3. TPU 属于 **吸水性较强** 的材料，未使用完的耗材应立即放入含有有效干燥剂的 **密封容器** 内，并且在打印前按照指南中推荐的温度和时间进行 **充分烘干**。
> 4. 建议在 **通风良好** 的区域使用打印机，或安装有效的空气过滤、外排风系统。
> 5. 本耗材 **不属于** 食品接触级耗材，请避免将打印成品用于存放或接触食品。

## 📦 耗材存储

TPU 耗材具有较强的 **吸湿性**，暴露在空气中极易受潮。打印受潮的耗材会导致模型出现气泡、拉丝、层间粘结不良等质量问题。

因此，在耗材拆封后或使用完毕后，建议：

- 将耗材存放在湿度低于 **20% RH** 的干燥密封环境中；
- 可存放在 **AMS / 密封收纳盒 / 密封袋** 等密封容器中；
- 同时在容器中放入足量的有效 **干燥剂**。

> 如何判断干燥剂是否有效，请阅读：[AMS 干燥剂 | Bambu Lab Wiki](desiccant-status.md)

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/sealed-bag-dry-cabinet.jpg)

密封袋（左）；防潮箱（右）

## 🔧 打印准备

本章介绍在打印 TPU 前需要做哪些准备工作。

### 硬件选择

打印 TPU 时，需使用与其兼容的硬件和配件，否则可能导致设备故障或打印失败。

本章节列出了不同硬度 TPU 与拓竹 3D 打印机、喷嘴、打印板、及 AMS 等硬件的适配性信息，请在打印前确认并准备好适配的硬件。

#### 打印机

下表为不同硬度 TPU 与拓竹各机型打印机的兼容性信息，请参考并使用适配的机型打印。

**注：** ✅ 表示适配；❌ 表示不适配。

|  | **TPU 75A (2.85 mm)** | **TPU 85A** | **TPU 90A** | **TPU 95A HF** | **TPU for AMS** |
| --- | --- | --- | --- | --- | --- |
| **H2、X、P 系列** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **A1 系列** | ❌ | ❌ | ✅ | ✅ | ✅ |
| **A2L** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **H3C** | ✅ | ✅ | ✅ | ✅ | ✅ |

#### 喷嘴

下表为不同硬度 TPU 与各类喷嘴的兼容性信息，请参考并使用适配的喷嘴来打印。

**注：** ✅ 表示可用；⚠️ 表示不推荐，即可以使用，但打印失败率较高；❌ 表示不可用。

| **耗材** | **标准喷嘴→** |  |  |  | **高流量→** |  |  |  | **2.85mm线径用热端→** |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **0.2 mm** | **0.4 mm** | **0.6 mm** | **0.8 mm** | **0.4 mm** | **0.6 mm** | **0.8 mm** | [**TPU 高流量喷嘴**](../h2d/manual/tpu-high-flow-hotend.md) | **0.4 mm** | **0.6 mm** | **0.8 mm** |
| **TPU 75A (2.85mm)** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **TPU 85A** | ❌ | ❌ | ✅ | ✅ | ❌ | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ❌ |
| **TPU 90A** | ❌ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ❌ |
| **TPU 95A HF** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **TPU for AMS** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |

> **注意：**
>
> - 打印 TPU 建议使用 **全新** 的喷嘴，或在打印前对使用过的喷嘴进行 **冷拔；** 冷拔的具体操作请参考 [冷拔喷嘴指南](../p1/manual/p1s-cold-pull.md)；
> - **不建议** 使用打印过碳纤、玻纤等纤维增强耗材的喷嘴，以免因残留纤维增加挤出阻力，导致喷嘴堵塞。

#### 打印板

请勿使用 **增稳低温打印板** 打印 TPU。除增稳低温打印板外，其他类型打印板均可用于 TPU 打印。

> 了解更多打印板相关信息，请参阅：[拓竹打印板介绍 | Bambu Lab Wiki](../filament-acc/acc/plates.md)

#### AMS 系列

本节介绍不同硬度 TPU 与 AMS 系列（及其不同进料方式）的兼容性，具体请参考下表：

**注：** ✅ 表示可用；⚠️ 表示不推荐，即可以使用，但打印失败率较高；❌ 表示不可用。

|  | **AMS HT 自动供料** | **AMS HT TPU 出料口** | **AMS 3H 耗材直通口** | **AMS 3H 自动进料口** | **AMS 3H 外挂料盘** | **AMS 2 Pro** | **AMS lite** | **AMS** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **TPU 75A (2.85mm)** | ❌ | ❌ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| **TPU 85A** | ❌ | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| **TPU 90A** | ❌ | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| **TPU 95A HF** | ❌ | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| **TPU for AMS** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**说明：**

- **TPU for AMS：** 可使用所有 AMS 系列的常规自动供料功能打印。
- **AMS 3H：** 打印硬度为 95A 及以下的 TPU 时，需使用耗材直通口，不能使用自动进料口。
- **AMS HT：** 仅作为密封容器，使用其背面的 **TPU 出料口** 送出耗材，不能使用常规出料口与自动供料功能。

![进料口.png](https://wiki.bambulab.com/filament-acc/tpu/%E8%BF%9B%E6%96%99%E5%8F%A3.png)

#### TPU 送料助力模块

TPU 送料助力模块是用于提升 TPU 打印稳定性的可选增强组件，适用于 **H2、X 和 P 系列** 打印机。加装后可降低 TPU 进料阻力，减少进料卡顿和断料，提升打印稳定性与成功率；同时简化进料流程，减少打印前准备，并支持封箱打印。更多信息请参阅：[**TPU 送料助力模块组装 & 使用指南**](../general/manual/tpu-feed-assist-module.md)。

![](https://wiki.bambulab.com/general/tpu-feed-assist-module/036.jpg)

---

### 耗材烘干

**为确保打印质量和成功率，请务必在打印前对 TPU 耗材进行烘干。**

由于 TPU 具有较强的吸湿性，在自然环境中容易吸收水分。若使用受潮的 TPU 直接打印，可能导致拉丝、表面粗糙、气泡、层间结合不良等打印质量问题，甚至造成打印失败。

**可通过以下三种方式烘干：**

1. 使用 **AMS HT / AMS 2 Pro / AMS 3H** 的烘干功能；
2. 使用封箱的 X 系列、P 系列和 H 系列打印机的 **热床** 进行烘干；
3. 使用 **鼓风式烤箱** 烘干。

了解烘干的具体教程与参数，请参考这篇 Wiki：[**耗材烘干操作指南 | Bambu Lab Wiki**](../filament-acc/filament/dry-filament.md)。

> **注意**：AMS 2 Pro 最高烘干温度为 65°C，低于 TPU 推荐烘干温度，存在无法完全烘干的风险。若需要充分烘干 TPU，建议使用热床、AMS HT、AMS 3H 或鼓风式烤箱烘干。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-9.png)

需注意的是，在烘干过程中，TPU 受热会产生轻微的膨胀，料盘宽度可能 **从 65.4 mm 增大到约 69.4 mm**，这是正常现象。使用 **热床** 烘干时，可在料盘上放置耐高温重物，以抑制料盘变形。

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/spool-expansion.png)

左：膨胀前；右：膨胀后

---

### 容器选择

打印 TPU 时需使用 **进料阻力小** 且 **密封性良好** 的容器，以减少进料不畅或打滑等问题。

**推荐使用以下三种容器配合打印 TPU，点击对应标签可查看使用方法：**

#### AMS 3H

需搭配 **H3C** 打印机使用，其他机型请使用 AMS HT 或米桶。

具体操作方法请参考这篇 Wiki：[**H3C TPU 打印指南**](../h3c/manual/tpu-printing-guide.md)

#### **AMS HT**

打印 TPU 时， **AMS HT 仅作为密封容器，无须使用其自动送料功能**。打印时，需要通过 **TPU 出料口** 送出耗材，而 **不是默认的出料口**。

![进料口.png](https://wiki.bambulab.com/filament-acc/tpu/%E8%BF%9B%E6%96%99%E5%8F%A3.png)

**打印前，请按以下步骤将 TPU 装入 AMS HT 中：**

**步骤 1.** 裁剪一段 50 mm 长的料管；

![](https://wiki.bambulab.com/filament-acc/tpu/image6.png)

**步骤 2.** 将料管微微弯折，使其保持弯曲，便于后续进料；

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/bend-ptfe-tube.webp)

**步骤 3.** 打开 AMS HT 尾部的硅胶塞，将料管凸起一侧朝上，插入硅胶塞的小孔，插入 AMS HT 的长度为 5 mm；

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/insert-ptfe-outlet.webp)

**步骤 4.** 确认料盘旋转方向如下图所示，将耗材放入 AMS HT 中；

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/load-spool-ams-ht.webp)

**步骤 5.** 从下至上将耗材头部穿过铁氟龙管，扣紧 AMS HT 上盖，即完成；

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/feed-tpu-ams-ht.webp)

**步骤 6.** 将 AMS HT 垫高，确保进料顺畅，避免耗材送出过多时被热床或喷嘴剐蹭。推荐方式如下：

- 使用小凳子或小箱子等物品垫高；
- 打印并使用增高架模型垫高：[点击下载推荐模型-MakerWorld](https://makerworld.com.cn/zh/models/983129-tpuxian-cai-juan-zhou-jia?from=search#profileId-1004263)

|  |  |
| --- | --- |
|  |  |

**步骤 7.** 一切准备就绪，请参考 **进料操作** 章节完成进料。

#### **米桶**

**步骤 1. 打印并安装料盘支架**

打印一个料盘支架，安装在米桶中，用于固定料盘，确保料盘顺畅旋转。

推荐模型：[*点击下载 5.8 L 料桶支架模型*](https://makerworld.com.cn/zh/models/437644?from=search#profileId-353897)

**步骤 2. 在米桶侧边开孔**

在米桶的侧边开一个小口，从中拉出耗材。

请注意耗材旋转方向，具体参考下图。

|  |  |
| --- | --- |
|  |  |

**步骤 3. 将米桶垫高**

为减小进料阻力，请将米桶垫高，避免耗材送出过多时被热床或喷嘴剐蹭。

**推荐方式：**

- 使用小凳子或小箱子等物品垫高；
- 打印并使用增高架模型来垫高：[点击下载推荐模型-MakerWorld](https://makerworld.com.cn/zh/models/983129-tpuxian-cai-juan-zhou-jia?from=search#profileId-1004263)

|  |  |
| --- | --- |
|  |  |

**步骤 4.** 一切准备就绪，请参考 **进料操作** 章节完成进料。

## ℹ️ 进料操作

不同机型的进料步骤有所不同，请选择对应机型查看详细教程。

类似格式展示

[![H3C](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/h3c_home.png)
  
H3C](https://wiki.bambulab.com/zh/h3c/manual/tpu-printing-guide)

[![H2 系列](https://wiki.bambulab.com/h2s/h2d1_compressed.png)
  
H2 系列](https://wiki.bambulab.com/zh/h2/h2d-tpu-printing-guide)

[![X1 系列](https://wiki.bambulab.com/h2s/x1_series.png)
  
X1 系列](https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-x-series)

[![P1 系列](https://wiki.bambulab.com/h2s/test3_compressed.png)
  
P 系列](https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-p-series)

[![A1](https://wiki.bambulab.com/stock-images/new/a1.png)
  
A1 系列](https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-a-series)

[![A2L](https://public-cdn.bblmw.com/wiki/new/homepage/a2l-2.png)
  
A2L](https://wiki.bambulab.com/zh/a2l/manual/tpu-printing-guide)

[![X2D](https://wiki.bambulab.com/x1/x2d-1_compressed.jpg)
  
X2D](https://wiki.bambulab.com/zh/x2d/manual/tpu-printing-guide)

## 📋 常见打印问题

### 模型表面有孔洞

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/surface-holes.png)

**现象描述**：模型外表面出现不连续的小孔、凹坑或缺料区域。

**解决方法**：

1. **烘干耗材**：耗材受潮后打印时容易产生气泡、爆裂声或表面小孔。建议参考 [耗材烘干操作指南](../filament-acc/filament/dry-filament.md) 对耗材重新烘干后再打印。
2. **降低回抽长度：** 回抽距离过大可能导致出料延迟或短暂欠挤出，从而在模型表面形成空洞。可在当前配置基础上逐步降低回抽距离，每次降低 0.2 mm 后重新测试，直到空洞改善。

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/retraction-length.png)

### 模型表面出现拉丝漏料

![](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/stringing.png)

**现象描述**：模型表面或不同结构之间出现细丝、毛发状拉丝，或喷嘴在移动过程中有材料渗出，导致表面残留多余耗材。

**解决方法：**

1. **逐件打印：** 如果摆放了多个模型，或是打印较为复杂的模型，在打印时应尽量避免存在过多的空驶，可选用逐件打印的方式，或放置少量模型并选择逐件打印。打印空驶比较多的模型也可将模型简化后再发起打印。

|  |  |
| --- | --- |
| 不建议一盘放多个模型且逐层打印，这样会导致模型与模型之间有很多空驶，造成严重拉丝。 | 建议选用逐件打印的方式，减少空驶次数。 |

2. **烘干耗材**：在耗材受潮时，极易出现拉丝漏料的情况，建议在打印前参考 [耗材烘干操作指南](../filament-acc/filament/dry-filament.md) 对耗材进行烘干。
3. **调节回抽：** 在打完一层后会有一个回抽的动作避免耗材溢出，若出现较为严重的漏料情况，可以将回抽值提高（在原有基础上提高 0.2 mm）。

![](https://wiki.bambulab.com/filament-acc/tpu/image23.png)

### 模型缺料

![](https://wiki.bambulab.com/filament-acc/tpu/image24.jpeg)

**现象描述**：模型局部出现出料不足、线条变细、层间不连续。

**解决方法：**

1. 当进料阻力过大时会出现打印缺料的情况，请参考机型对应的进料指南正确摆放进料容器，使用正确的进料方式。
2. 耗材受潮易导致模型缺料。请参考 [耗材烘干操作指南](../filament-acc/filament/dry-filament.md) 对耗材重新烘干后再打印。
3. 确认热端是否打印过其他硬质耗材（特别是高温耗材），可能会有耗材残渣在热端中残留，请对喷嘴进行冷拔而后再发起打印；冷拔的具体操作请参考 [冷拔喷嘴指南](../p1/manual/p1s-cold-pull.md)。

### 支撑表面出现乱丝、塌陷

![support-collapse-tpu.png](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/support-collapse-tpu.png)

**现象描述**：使用 TPU 本身作为支撑时（TPU for AMS 除外），支撑表面易出现乱丝、塌陷、变形等问题，支撑稳定性和成型效果较差，可能导致模型表面质量下降或产生结构缺陷。

**解决方法：**

- 推荐使用 PLA 作为支撑耗材。
- 单热端打印机可将支撑主体图案设置为「**直线网格**」，支撑形状设置为「**普通**」。

|  |  |
| --- | --- |
|  |  |

### 拆卸支撑困难

如果出现支撑剥离困难的情况，可以在 TPU 与 PLA 粘合边角处，拉起一道缝隙，然后往其中喷洒酒精，待酒精彻底浸润到两种耗材之间后，便可逐渐用力把模型和支撑分离。

**注意：** 强行拆除支撑可能会导致模型损坏，请注意拆除力度与技巧。

![tpu_喷酒精拆除支撑.gif](https://wiki.bambulab.com/filament-acc/tpu/tpu_%E5%96%B7%E9%85%92%E7%B2%BE%E6%8B%86%E9%99%A4%E6%94%AF%E6%92%91.gif)

> 💡 **小贴士：「支撑耗材的选择」**
>
> - **TPU 耗材建议搭配 PLA 耗材作为支撑**：打印时，若直接使用 TPU 本身作为支撑往往难以拆除，容易造成表面拉丝或变形。推荐使用 PLA 作为支撑材料，既能保证打印稳定性，又便于后期移除。
> - **推荐支撑颜色**：请选择与 TPU 本体 **颜色相近的 PLA**，或使用 **玉石白 PLA**，这样可有效避免因色差过大造成的染色或颜色残留问题。

### 取模困难

TPU 对打印板的粘结力较强，部分底面较大的模型可能会较难取下。这时，请勿使用蛮力，以免损伤模型或打印板。可以 **将模型的一个边角拉起一道缝隙后，往其中喷洒酒精，然后逐渐用力把模型和打印板分离。**

---

*如果以上信息未涉及您遇到的问题，请*[*点击此处*](../filament-acc/filament/print-quality.md)*获取更多解决方案。*

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
