---
path: zh/knowledge-sharing/tpu-printing-guide
title: "TPU 打印指南"
description: "本文介绍了打印 TPU 的建议"
tags: ["tpu"]
created: 2023-08-02T08:20:33.025Z
updated: 2026-07-23T03:25:37.341Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/tpu-printing-guide
---

## 耗材介绍

TPU（热塑性聚氨酯）是一种柔性耗材，有弹性、能被拉伸但又能回弹。用于打印需要软性、弹性的部件（例如手机壳、休闲鞋、玩具部件等）。更多使用场景可进入商品详情页中了解：[TPU](https://bambulab.tmall.com/category-1695408974.htm?spm=a1z10.5-b-s.w4010-25176969462.18.3c4f7eabUhW1Lp&search=y&parentCatId=1692717251&parentCatName=3D%B4%F2%D3%A1%BA%C4%B2%C4&catName=%C8%E1%D0%D4%B2%C4%C1%CF#bd)

TPU 的硬度通常采用邵氏硬度（Shore Hardness） 表示，常见标尺包括 Shore A（软质）与 Shore D（偏硬）。数字越高，一般表示材料越硬、更不容易弯曲或变形。一般的硬度排序为：77D > 70D > 68D > 55D > 95A > 90A > 85A > 83A > 80A > 75A > 70A 等。

95A、90A、85A 的 TPU 硬度适中，可用拓竹打印机打印（硬度越高的打印失败风险越低）。低于 85A 硬度的 TPU （如 83A、80A）耗材过于柔软，在打印过程中容易出现挤出异常，因此，*拓竹打印机暂不支持打印低于 85A 硬度的 TPU 耗材*。

![1.jpg](https://wiki.bambulab.com/filament-acc/tpu/1.jpg)

> 📌 **耗材使用注意事项**：
>
> 1. 请在**阴凉、避光、干燥**环境中存放耗材，避免阳光直射或高温环境。
> 2. 请将耗材及折断的碎屑放在**婴幼儿及宠物无法触及的地方**，避免吞咽和窒息的风险。
> 3. TPU 属于**吸水性较强**的材料，未使用完的耗材应立即放入含有有效干燥剂的**密封容器**内，并且在打印前按照指南中推荐的温度和时间进行**充分烘干**。
> 4. 建议在**通风良好**的区域使用打印机，或安装有效的空气过滤、外排风系统。
> 5. 本耗材**不属于**食品接触级耗材，请避免将打印成品用于存放或接触食品。

## 打印前的准备

### 配件选择

#### 打印机适配性

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TPU 85A | TPU 90A | TPU 95A HF | TPU for AMS |
| H2，X1，P 系列 | ✅ | ✅ | ✅ | ✅ |
| A1 系列 | ❌不适配 | ✅ | ✅ | ✅ |
| A2L | ✅ | ✅ | ✅ | ✅ |

#### 喷嘴

- **打印 TPU 耗材时需特别注意喷嘴的选择。**
- TPU 耗材不适配 0.2mm 喷嘴，其中 85A TPU 耗材不适配 0.4mm 喷嘴。
- **建议使用全新的喷嘴来打印，或者在打印前对旧的喷嘴进行冷拔（具体操作步骤请参考 [冷拔喷嘴指南](../p1/manual/p1s-cold-pull.md)）** 。
- 建议不要使用曾打印过碳纤增强、玻纤增强等纤维类耗材的喷嘴，这类耗材残留的纤维会大幅增加挤出阻力，极易引发堵塞问题。
- 📌 请参考下方表格选用合适的喷嘴进行打印：

|  |  |
| --- | --- |
| **TPU 85A** | **支持：** 0.6/ 0.8 mm / TPU 高流量喷嘴    **不推荐：** 0.6/ 0.8 mm 的高流量喷嘴    **不支持：** 0.2/ 0.4 mm / 高流量 0.4 mm |
| **TPU 90A** | **支持：** 0.4/ 0.6/ 0.8 mm / TPU 高流量喷嘴    **不推荐：** 高流量喷嘴    **不支持：** 0.2 mm |
| **TPU 95A HF** | **支持：** 0.4/ 0.6/ 0.8 mm / 高流量喷嘴 / TPU 高流量喷嘴    **不支持：** 0.2 mm |
| **TPU for AMS** | **支持：** 0.4/ 0.6/ 0.8 mm / 高流量喷嘴    **不支持：** 0.2 mm |

> 🔗 有关 TPU 高流量喷嘴的完整介绍与使用教程，请[点击此处](../h2d/manual/tpu-high-flow-hotend.md)了解详情。  
> ![induction](https://wiki.bambulab.com/filament-acc/acc/nozzles/tpu_high-flow-nozzle.png)

#### 打印板

**除了增稳低温打印板以外，** 其他类型打印板均适配 TPU 耗材的打印。

#### AMS 系列兼容性

AMS 系列中，仅有 AMS HT 可以用来配合 TPU 耗材的打印，且打印时，AMS HT 仅作为一个密封容器，不能使用其常规出料口与自动供料功能，而需要通过其背面的 **TPU 出料口**送出耗材。

![进料口.png](https://wiki.bambulab.com/filament-acc/tpu/%E8%BF%9B%E6%96%99%E5%8F%A3.png)

其他 AMS 系列（AMS / AMS lite / AMS 2 Pro）无法配合 TPU 打印。

此外，TPU for AMS 耗材可以使用所有 AMS 系列的常规供料功能进行进料与打印。

#### TPU 送料助力模块

TPU 送料助力模块是一款专为 H/X/P 系列设备打印柔性耗材设计的增强组件。

该模块能够降低 TPU 耗材在各种摆放场景下的进料阻力，有效解决柔性耗材进料卡顿、断料问题，大幅提升 TPU 打印的稳定性和成功率。此外，该模块简化了 TPU 打印的进料流程，减少打印前的准备工作，支持封箱打印，可直接从 TPU 专用进料口进料，操作更便捷。

有关 TPU 送料助力模块的完整介绍，请[点击此处](../general/manual/tpu-feed-assist-module.md)了解详情。

![](https://wiki.bambulab.com/general/tpu-feed-assist-module/036.jpg)

### 耗材烘干

TPU 耗材具有较强的吸湿性，在自然环境中容易吸收水分。在不烘干的情况下打印会造成打印质量问题，甚至可能导致打印失败。因此，**打印 TPU 耗材前，必需对 TPU 耗材进行烘干。**

耗材烘干有两种方法：

1. 使用 **AMS 2 Pro 和 AMS HT** 的烘干功能进行烘干；
2. 使用封箱的 X 系列、P 系列和 H2 系列打印机的**热床**进行烘干。

> 📌 使用 AMS 2 Pro 进行烘干时，需要根据打印机机型与 AMS 数量来连接电源适配器，部分机型连接 1 台 AMS 2 Pro 时无须电源适配器；使用 AMS HT 烘干时，必需为其连接电源线。**具体的电源要求与烘干步骤请参阅：[耗材烘干操作指南 | Bambu Lab Wiki](../filament-acc/filament/dry-filament.md)**。

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-9.png)

### 容器选择

TPU 耗材因其具有一定的弹性和黏性，需要采用特殊的进料方式，减少进料阻力，避免“进料不畅”或者“打滑”。因此，选择合适的容器对于打印 TPU 耗材尤为重要。

因 TPU 耗材具有较强的吸湿性，所以配合其打印的容器必需具有**很好的密封性**。

基于此，我们建议使用 **AMS HT** 或 **米桶**来配合 TPU 耗材的打印。

两种容器的介绍与耗材装载方法如下：

#### **1. AMS HT**

- 使用 AMS HT 配合打印 TPU 耗材时，**AMS HT 仅作为一个密封容器，无须使用其送料功能**。
- 打印时，需要通过 **TPU 出料口**送出耗材，而**不是默认的出料口**。

![进料口.png](https://wiki.bambulab.com/filament-acc/tpu/%E8%BF%9B%E6%96%99%E5%8F%A3.png)

**使用 AMS HT 装载耗材的步骤如下：**

- **步骤 1**：

先裁剪 50mm 长的 PTFE 管，并将 PTFE 管微微弯折，使其保持弯曲，便于后续进料。然后打开 AMS HT 尾部的硅胶塞，将 PTFE 管凸起一侧朝上，将 PTFE 管插入硅胶塞的小孔，确保插入 AMS HT 的长度为 5mm。

|  |  |
| --- | --- |
| 50mm 长的 PTFE 管 | 插入 AMS HT |

- **步骤 2**：

确认耗材的方向，将耗材放入 AMS HT 中，从下至上穿过铁氟龙管。

|  |  |
| --- | --- |
| 确认耗材的方向 | 将耗材从下至上穿过铁氟龙管 |

- **步骤 3**：

扣紧 AMS HT 上盖，即安装完成。

|  |  |
| --- | --- |
| TPU 出料口 | 耗材进料方向 |

#### **2. 米桶**

- 米桶为进料提供了一个阻力较小、密封性强的空间。
- **使用米桶进料时，需要在其中放置一个米桶支架来固定料盘，确保耗材旋转顺畅。** 可点击下方链接下载并打印料桶支架。  
  *[5.8L 料桶支架模型](https://makerworld.com.cn/zh/models/437644?from=search#profileId-353897)*
- 此外，**为了减小进料阻力，请从米桶的侧边开口**。

|  |  |
| --- | --- |
| 料桶侧边开孔.jpeg  米桶的侧边开口 | 耗材正常旋转.gif  确保耗材旋转顺畅 |

---

> 💡 **注意：**
>
> - 打印 TPU 时，建议将容器垫高，确保进料顺畅，避免耗材送出过多时被热床或喷嘴剐蹭。
> - 您可以使用小凳子或小箱子等物品来垫高；若时间充裕，也可以选择打印 MakerWorld 上的 [TPU 线材卷轴架](https://makerworld.com.cn/zh/models/983129-tpuxian-cai-juan-zhou-jia?from=search#profileId-1004263) 模型来垫高。  
>   ![](https://wiki.bambulab.com/filament-acc/tpu/image141.png)

## 进料操作

不同的机型有不同的进料操作步骤，请选择您的机型查看详细的教程。

类似格式展示

[![H2 系列](https://wiki.bambulab.com/h2s/h2d1_compressed.png)
  
H2 系列](https://wiki.bambulab.com/zh/h2/h2d-tpu-printing-guide)

[![X1 系列](https://wiki.bambulab.com/h2s/x1_series.png)
  
X 系列](https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-x-series)

[![P1 系列](https://wiki.bambulab.com/h2s/test3_compressed.png)
  
P 系列](https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-p-series)

[![A1](https://wiki.bambulab.com/stock-images/new/a1.png)
  
A1 系列](https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-a-series)

[![A2L](https://public-cdn.bblmw.com/wiki/new/homepage/a2l-2.png)
  
A2L](https://wiki.bambulab.com/zh/a2l/manual/tpu-printing-guide)

[![X2D](https://wiki.bambulab.com/x1/x2d-1_compressed.jpg)
  
X2D](https://wiki.bambulab.com/zh/x2d/manual/tpu-printing-guide)

> 📌**注意：**
>
> - 打印 TPU 耗材前，请关闭动态流量校准。详情请参阅：[动态流量校准 | Bambu Lab Wiki](../software/bambu-studio/calibration_pa.md)
> - ![关闭动态流量校准.png](https://wiki.bambulab.com/filament-acc/tpu/%E5%85%B3%E9%97%AD%E5%8A%A8%E6%80%81%E6%B5%81%E9%87%8F%E6%A0%A1%E5%87%86.png)

## 耗材存储

由于 TPU 材料具有较强的**吸湿性**，受潮后会导致打印质量下降（如气泡、拉丝、层间粘结不良等）。

因此，建议在打印完成后，将耗材存放于**湿度低于 20% RH 的干燥环境中**。

可以放入 AMS 中密封存储，并且需要在 AMS 中放入足够量的硅胶干燥剂。

若未使用 AMS，可采用**密封收纳盒**进行保存，并在盒内放置足量干燥剂，以延长耗材的可用寿命。

![image18.jpeg](https://wiki.bambulab.com/filament-acc/tpu/image18.jpeg)

## 常见打印问题

### 模型拉丝

如您遇到了 TPU 拉丝的情况，建议参考以下几个方案进行解决：

![image19.png](https://wiki.bambulab.com/filament-acc/tpu/image19.png)

1. **逐件打印：** 如果摆放了多个模型，或是打印较为复杂的模型，在打印时应尽量避免存在过多的空驶，可选用逐件打印的方式，或放置少量模型并选择逐件打印。打印空驶比较多的模型也可将模型简化后再发起打印。

|  |  |
| --- | --- |
| 不建议一盘放多个模型且逐层打印，这样会导致模型与模型之间有很多空驶，造成严重拉丝。 | 建议选用逐件打印的方式，减少空驶次数。 |

2. **降低喷嘴温度：** TPU 的流动性较强，在喷嘴温度较高时容易产生溢出，因此可适当降低喷嘴温度（原有基础上降低5℃），并在降低喷嘴温度后将速度参数一并降低（最大流量体积速度下调 0,4 mm³/s）。

![image22.png](https://wiki.bambulab.com/filament-acc/tpu/image22.png)

3. **调节回抽：** 在打完一层后会有一个回抽的动作避免耗材溢出，若出现较为严重的漏料情况，可以将回抽值提高（在原有基础上提高 0.2mm）。

![image23.png](https://wiki.bambulab.com/filament-acc/tpu/image23.png)

4. 在耗材受潮时，也极易出现拉丝漏料的情况，建议在打印前参考 [耗材烘干操作指南](../filament-acc/filament/dry-filament.md) 对耗材进行烘干。

### 模型缺料

当您遇到模型缺料的情况可以参考以下几个建议进行处理：

![image24.jpeg](https://wiki.bambulab.com/filament-acc/tpu/image24.jpeg)

1. **降低打印速度：** 较低的速度可以使耗材熔融的更加充分，从而减少缺料的概率。

![image25.png](https://wiki.bambulab.com/filament-acc/tpu/image25.png)

2. 当进料阻力过大时也会出现打印缺料的情况，请参考机型对应的进料指南正确摆放进料容器，使用正确的进料方式。
3. 确认耗材是否受潮，缺料可能是耗材受潮的表现，如果受潮，请烘干耗材。
4. 确认热端是否打印过其他硬质耗材（特别是高温料），可能会有耗材残渣在热端中残留，请进行冷拔而后再发起打印。

### 拆卸支撑困难

如果出现支撑剥离困难的情况，可以在 TPU 与 PLA 粘合边角处，拉起一道缝隙，然后往其中喷洒酒精，待酒精彻底浸润到两种耗材之间后，便可逐渐用力把模型和支撑分离。

**注意：** 强行拆除支撑可能会导致模型损坏，请注意拆除力度与技巧。

![tpu_喷酒精拆除支撑.gif](https://wiki.bambulab.com/filament-acc/tpu/tpu_%E5%96%B7%E9%85%92%E7%B2%BE%E6%8B%86%E9%99%A4%E6%94%AF%E6%92%91.gif)

> 💡 **小贴士:「支撑耗材的选择」**
>
> - **TPU 耗材建议搭配 PLA 耗材作为支撑**：打印时，若直接使用 TPU 本身作为支撑往往难以拆除，容易造成表面拉丝或变形。推荐使用 PLA 作为支撑材料，既能保证打印稳定性，又便于后期移除。
> - **推荐支撑颜色**：请选择与 TPU 本体**颜色相近的 PLA**，或使用**玉石白 PLA**，这样可有效避免因色差过大造成的染色或颜色残留问题。

### 取模困难

一般而言，TPU 对打印板的粘结力较强，部分底面较大的模型较难拆下。这时，请勿使用蛮力，以免损伤模型或打印板，而是应该**将模型的一个边角拉起一道缝隙后，往其中喷洒酒精，然后便可逐渐用力把模型和打印板分离。**

---

*如果以上信息未涉及您遇到的问题，请[点击此处](../filament-acc/filament/print-quality.md)获取更多解决方案。*

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
