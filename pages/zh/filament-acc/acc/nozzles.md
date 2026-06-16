---
path: zh/filament-acc/acc/nozzles
title: "拓竹热端喷嘴介绍"
description: "本篇指南详细介绍了拓竹各类喷嘴组件的特点、功能、尺寸、材质，以及喷嘴硅胶套的基本信息。"
tags: []
created: 2025-12-30T10:35:04.180Z
updated: 2026-06-12T02:02:18.932Z
source: https://wiki.bambulab.com/zh/filament-acc/acc/nozzles
---

## 喷嘴

喷嘴组件，也称“热端”，位于 3D 打印机的工具头，是每台 3D 打印机的核心部件之一。它负责将耗材加热到指定温度，使其迅速熔化为流体。熔化后的耗材以薄层的形式沉积来生成模型，从而实现打印。喷嘴直径一般有 **0.2 mm、0.4 mm、0.6 mm** 和 **0.8 mm** 四种选择。喷嘴的材质有**硬化钢**和**不锈钢**。

![collective.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/collective.png)

喷嘴组件由两个部分构成：

- **冷端：**由铝合金散热鳍片组成，可以有效阻隔热端热量向上传导，避免耗材提前软化，从而减少挤出机堵塞风险。此外，位于设备左侧的散热风扇持续为散热片提供强劲冷却，保障系统长时间稳定运行。
- **热端：**由熔腔和喷头两部分组成，负责将耗材快速融化再经由喷头挤出。

热端与冷端之间，通过坚固耐用的钛合金喉管实现可靠隔离，确保两者温度互不影响。

在拓竹所有打印机中，冷端和热端的组合通常都被统称为"热端"或"喷嘴"，作为一个整体使用。

![2._喷嘴组件由两个部分构成.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/2._%E5%96%B7%E5%98%B4%E7%BB%84%E4%BB%B6%E7%94%B1%E4%B8%A4%E4%B8%AA%E9%83%A8%E5%88%86%E6%9E%84%E6%88%90.jpg)

> 📌 如果您想了解更多**喷嘴与耗材的兼容性**信息，请参阅[耗材指南](../../general/filament-guide-material-table.md)。

### 📏 喷嘴尺寸

喷嘴尺寸即喷嘴尖端的直径，决定了耗材挤出的宽度，也是决定**打印精度**、**层高范围**和**打印速度**的关键参数。口径越大，每秒挤出的熔融塑料体积（流速）越高，打印速度越快，打印件的整体强度越强。

下图直观地展示了 0.2mm 喷嘴与 0.4mm 喷嘴在打印同等大小字体时的效果，0.2mm 喷嘴打印出来的文字更加清晰、更加精细。

![3._0.2mm_喷嘴与_0.4mm_喷嘴.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/3._0.2mm_%E5%96%B7%E5%98%B4%E4%B8%8E_0.4mm_%E5%96%B7%E5%98%B4.png)

💡 提示：滑动表格查看更多内容。

| 喷嘴尺寸 | 表现效果 | 主要特点 | 最佳适用场景 | 推荐设置 | 不足 |
| --- | --- | --- | --- | --- | --- |
| **0.2 mm** | 4._0.2mm.png | 最小口径，适合极致细节和高分辨率打印，细节表现力强，最佳的表面光洁度，可使用更低层高以提升打印质量。 | 精细模型或需要尖锐特征的部件，如艺术模型、微缩模型。实现珠宝级细节，满足最小层纹要求。 | 层高通常为 0.05-0.12mm，即喷嘴直径的 25-60%，以获得最佳效果。 | · 强度较低：打印件通常强度较低，因为更细的挤出线条会降低模型层间附着力。  · 打印速度较慢：喷嘴直径越小，单次挤出耗材量少，需要更多层来完成打印，整体效率低下。 · 易发生喷嘴堵塞：更小的喷嘴孔径更容易堵塞，尤其是在耗材有杂质或直径不稳定时。 |
| **0.4 mm** | 5._0.4mm.png | 最常用、最通用的喷嘴尺寸，较好地平衡了打印质量和打印速度，兼容市面上大多数耗材。 | 日常打印、大多数模型、功能原型。适合大多数的通用打印需求。 | 最佳层高为 0.1-0.3mm (喷嘴直径的 25%-70%)，常规推荐设置为 0.2mm。 | · 可用于纤维增强耗材，但仍有堵塞风险，建议优先选择更大口径喷嘴减少堵塞概率。 |
| **0.6 mm** | 6._0.6mm.png | 高速打印，更强的零件强度，更高的流速。对碳纤或玻璃纤维等纤维增强耗材较为友好，不易堵塞，添加的纤维或颗粒易通过。 | 大型模型、功能性部件、不追求太多细节但需更快速度或更高强度的部件。 | 最佳层高为 0.15-0.45mm (喷嘴直径的 25%-70%)，常规推荐设置为 0.3-0.4mm。 | · 打印细节有所损失，层线可见度高，边缘清晰度下降。 · 耗材消耗量更大，会增加大型模型的打印成本。 · 较厚的挤出线条可能导致悬垂或桥接效果较差。 |
| **0.8 mm** | 7._0.8mm.png | 超高速打印，最大流速，更节省打印时间，最粗层高，结构更坚固。 | 巨大模型、快速草稿、结构件、对表面质量要求不高的应用。需要快速打印或者对强度要求高，但对精度要求不高的打印件。 | 最佳层高为 0.2-0.6mm (喷嘴直径的 25%-70%)，常规推荐设置为 0.4-0.5mm。 | · 精度低：打印件精细度较低，表面层纹更明显，模型表面粗糙度较高。 · 支撑移除困难：支撑结构更加坚固，移除难度会增加，且易在模型表面留下明显的连接痕迹。 · 耗材消耗量大，会增加大型模型的打印成本。 |

### 🔧 材质差异

喷嘴有两种常见材质：

| 热端材料 | 图片示例 | 外观区别 | 关键特性 | 推荐用途 | 适用耗材示例 |
| --- | --- | --- | --- | --- | --- |
| **硬化钢** | 8._硬化钢.png | 黑色散热鳍片 | 相较于不锈钢，硬化钢更坚硬、更耐磨，抗磨损能力更强。 | 适用于任何含有硬颗粒的磨损性耗材。 | PA-CF, PLA-CF, PETG-CF, Glow-in-the-Dark (夜光), Wood (木材填充) 等。 |
| **不锈钢** | 9._不锈钢.png | 灰色散热鳍片 | 耐高温、耐腐蚀，成本效益高。 | 适用于大多数不含纤维或者颗粒的非磨损性通用耗材。 | PLA, ABS, ASA, PETG, TPU, PVA 等。 |

### ✒️ 喷嘴种类

#### TPU 热端

|  |  |
| --- | --- |
| induction | **购买链接：**[H2D TPU 高流量套件](https://item.jd.com/10213815463816.html?pcdk=EQz3y1RRCoTlqEsYSe2kcYktrYddxwFV2gnDAJFhGy0%3D.M8AW.sbc1) |
| **适配机型：** 仅适用于H2D 和 H2D Pro 的右热端 |
| **尺寸：** 0.4mm/ 0.6mm |

TPU 热端专为提升**柔性耗材**打印性能而设计，能显著提高打印时的**体积流量**及**运行稳定性**。它在结构上与标准 H2 系列热端不同，**必须配合 TPU 专用热端盖使用**。后续使用中可根据打印需求，在 TPU 热端与标准热端之间灵活切换。

- **功能受限：** 安装 TPU 热端后不支持安装切刀，切刀功能将无法使用；同时右喷头不支持自动换料及自动进/退料，仅支持外挂料盘打印。
- **仅限柔性耗材：** TPU 热端喉管带有特殊镀层，禁止打印硬质耗材（如 PLA、PETG、TPU for AMS），否则会造成镀层磨损失效。
- **位置限定：** TPU 热端仅建议安装于右喷头；若强行装入左喷头，将导致喷头升降功能异常。

> 🔗 **有关 TPU 热端安装与使用教程，请参阅：**[TPU 高流量套件使用指南 - H2D系列 | Bambu Lab Wiki](../../h2d/manual/tpu-high-flow-hotend.md)

#### Vortek 智能感应热端

|  |  |
| --- | --- |
| induction | **购买链接：**[H2C 感应热端组件](https://item.jd.com/10200112744649.html) |
| **适配机型：** H2C (右热端) |
| **最高打印温度：** 350 ℃ |
| **尺寸：** 0.2mm/ 0.4mm/ 0.6mm/ 0.8mm |
| **材质:** 硬化钢 / 不锈钢 |

Vortek 智能感应热端转为 H2C 右热端设计。H2C 打印机的 Vortek 热端切换系统实现了右热端的自动更换，最多可安装 **6 个**右热端交替使用。

该热端可在约 8 秒内（以 PLA 为例）将喷嘴加热至工作温度，显著缩短换色过渡时间，并进一步减少冲刷废料。系统内置过热、过压、短路与断路保护机制，确保在多材料连续打印过程中依然保持稳定可靠的性能。

- **极速加热：**从室温到打印温度（如 220°C）仅需约 8 秒，大幅减少换色等待时间，提升多色打印效率。
- **非接触性集成：**无需物理线缆和连接器，消除了因反复插拔导致的线缆磨损、接触不良等故障点，可靠性更高。
- **高效节能：**热量直接在被加热金属内部产生，热效率远高于传统的加热片，升温更快。
- **安全可靠：**热端在位检测确保了只有正常的热端才能被激活工作。

> 🔗 **有关更多 Vortek 感应热端工作流程的介绍，请阅读：**[Vortek 感应热端系统工作流程介绍](../../h2c/manual/induction-hotend-system-workflow.md)

智能感应热端提供了**标准流量**与**高流量**两种类型选择。相比于标准流量热端，高流量热端在打印过程中耗材的流量更高，因为不同的喷嘴结构增加了耗材与热端之间的接触面积。这种设计提高了打印速度，有助于减少整体打印时间。

![13._智能普通vs高流量.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/13._%E6%99%BA%E8%83%BD%E6%99%AE%E9%80%9Avs%E9%AB%98%E6%B5%81%E9%87%8F.png)

H2C 打印机与 H2D 相似，有两个喷嘴组件。不同的是，H2C 右侧喷嘴组件为智能感应喷嘴，左侧为标准喷嘴（左侧标配0.4mm 硬化钢标准流量喷嘴）。而 H2D 的两个喷嘴组件都是标准喷嘴。

![12._h2c_智能感应热端喷嘴.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/12._h2c_%E6%99%BA%E8%83%BD%E6%84%9F%E5%BA%94%E7%83%AD%E7%AB%AF%E5%96%B7%E5%98%B4.png)

> - **更换教程：**[更换 H2C 感应热端组件](../../h2c/maintenance/replace-induction-hotend.md)
> - **冷拔维护指南：**[H2C 喷嘴冷拔维护清理](../../h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning.md)
> - **堵塞清理指南：**[H2C 喷嘴/热端堵塞清理指南](../../h2c/troubleshooting/unclogging.md)

#### 碳化钨喷嘴

|  |  |
| --- | --- |
| tungsten_carbide | **碳化钨喷嘴 - 标准流量 & 高流量** |
| **适配机型：** H2D (左右热端), H2S, H2C (左热端), P2S |
| **最高打印温度：** 350 ℃ |
| **尺寸：** 0.4mm/ 0.6mm/ 0.8mm |

碳化钨喷嘴非常耐用，即使长时间使用也能保持其精确的形状。与硬化钢喷嘴相比，即使使用数公斤耗材，其磨损也明显更低。

![14.碳化钨new.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/14.%E7%A2%B3%E5%8C%96%E9%92%A8new.png)

碳化钨喷嘴提供了**标准流量**与**高流量**两种类型选择。相比于标准流量热端，高流量碳化钨热端兼具高耐用性和卓越的流量性能，是快拆热端产品中速度最快、耐磨性最佳的喷嘴。

#### H2 系列/P2S/X2D 喷嘴

|  |  |
| --- | --- |
| h2_p2s热端喷嘴 | **购买链接：** [H2 系列/P2S/X2D 喷嘴 - 标准流量](https://item.jd.com/10145051294182.html) & [高流量](https://item.jd.com/10145051305491.html) |
| **适配机型：** H2D (左右热端), H2S, H2C (左热端), P2S, X2D |
| **最高打印温度：** 350 ℃ |
| **尺寸：** 0.2mm/ 0.4mm/ 0.6mm/ 0.8mm |
| **材质：** 硬化钢 / 不锈钢 |

该喷嘴耐用性和耐磨性出色，专为稳定、长期打印高性能纤维增强材料设计。

H2D 与 P2S/X2D 标配的都是此类喷嘴的 0.4mm 硬化钢版本。

高流量硬化钢喷嘴是标准硬化钢喷嘴的升级版，拥有更强大的喷嘴加热能力。其焰融区的优化将最大体积速度提高 62.5%，使挤出的耗材能够更快、更高效地熔化，同时又不损失细节，可将模型打印时间最多缩短至 30%。

![normal_vs_high_flow.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/normal_vs_high_flow.jpg)

> - **更换教程：**[H2D](../../h2/maintenance/replace-hotend.md)； [P2S](https://wiki.bambulab.com/zh/p2s/maintenance/replace-hotend-and-silicone-sock#%E7%83%AD%E7%AB%AF%E5%92%8C%E7%83%AD%E7%AB%AF%E7%A1%85%E8%83%B6%E5%A5%97) ；[X2D](../../x2d/maintenance/replace-hotend-and-silicone-sock.md)
> - **冷拔维护指南：**[H2D](../../h2/maintenance/nozzl-cold-pull-maintenance-and-cleaning.md)；[H2S](../../h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning.md)；
> - **堵塞清理指南：**[H2D](../../h2/troubleshooting/unclogging.md)；[H2S](../../h2s/troubleshooting/nozzle-clog.md)；[P2S](../../p2s/maintenance/cold-pull-maintenance-hotend.md)；[X2D](../../x2d/maintenance/cold-pull-maintenance-hotend.md)

**H2D 双喷嘴系统：**

H2D 打印机有两个独立的喷嘴组件，每次使用其中一个喷嘴进行打印。在 H2D 推出之前，拓竹所有打印机都采用单喷嘴结构挤出耗材。双喷嘴的设计显著减少了耗材浪费，同时提升了打印速度。

例如，在使用一种普通耗材和一种支撑耗材进行打印时，将普通耗材装载到 H2D 的一个喷嘴，支撑耗材装载到另一个喷嘴。这样，每层在普通耗材和支撑耗材之间切换时，H2D 只需切换喷嘴，无需进行清料操作，从而几乎没有耗材浪费，且切换耗材的时间大大缩短，这在仅使用两种耗材的打印中效果尤为明显。

![10._h2d_双热端喷嘴.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/10._h2d_%E5%8F%8C%E7%83%AD%E7%AB%AF%E5%96%B7%E5%98%B4.png)

> - **切片分组介绍：**[双喷嘴打印机耗材切片分组](../../software/bambu-studio/manual/dual-nozzles-slicing-filament-grouping.md)
> - **可打印范围：**[H2D双喷嘴可打印范围介绍](../../h2/manual/printable-range-for-dual-nozzles.md)

#### A 系列喷嘴

|  |  |
| --- | --- |
| A1 Series Nozzle | **购买链接：**[A 系列热端喷嘴](https://item.jd.com/10087803259803.html) |
| **适配机型：** A2L / A1 / A1 mini |
| **最高打印温度：** 300 ℃ |
| **尺寸：** 0.2mm/0.4mm/0.6mm/0.8mm |
| **材质：** 不锈钢 / 硬化钢 |

A 系列热端喷嘴采用特殊的一体式设计，喷嘴集成到热块中，并通过细金属管连接到散热器，以获得最佳性能。有了这种设计，热端的加热速度比普通热端快得多，而且一体式设计与便捷的卡扣设计使得喷嘴更换过程变得轻松快捷，有效减少了更换喷嘴时可能出现的问题。

A 系列打印机标配的是 0.4mm 不锈钢喷嘴组件，也可选购升级为硬化钢喷嘴。

> - **更换教程：**[更换 A1 热端](../../a1/maintenance/replace-hotend.md)；[更换 A2L 热端及热端硅胶套](../../a2l/maintenance/replace-silicone-sock-for-hotend.md)
> - **堵塞清理教程：** [A2L 喷嘴堵塞清理指南](../../a2l/maintenance/cold-pull-maintenance-hotend.md)；[A1 系列喷嘴/热端堵塞清理指南](../../a1-mini/troubleshooting/nozzle-clog.md)；[热端脏污清洁维护](../../a1-mini/maintenance/clean-hotend-assembly.md)

#### X1 / P1 系列喷嘴

|  |  |
| --- | --- |
| X1/P1 nozzle | **购买链接：**[Bambu Hotend - X1C](https://asia.store.bambulab.com/products/bambu-hotend-x1c) & [Bambu Hotend - P1 Series](https://asia.store.bambulab.com/products/bambu-hotend-p1-series) |
| **适配机型：** X1C, P1P, P1S |
| **最高打印温度：** 300 ℃ |
| **尺寸：** 0.2mm/ 0.4mm/ 0.6mm/ 0.8mm |
| **材质：** 不锈钢 / 硬化钢 |

X1C/P1 系列的热端采用特殊的一体式设计。喷嘴集成到热块中，并通过细金属管连接到散热器，以获得卓越性能表现。有了这种设计，热端的加热速度比普通热端快得多，而且一体式设计非常便于更换。

P1S 标配 0.4 mm 不锈钢喷嘴，也可选购升级为硬化钢喷嘴。X1C 标配 0.4 mm 硬化钢喷嘴。

> - **更换教程：**[P1 系列](../../p1/maintenance/complete-hot-end-assembly.md)；[X1 系列](../../x1/maintenance/replace-hotend.md)
> - **堵塞清理教程：**[X1 / P1 系列](../../x1/troubleshooting/nozzle-clog.md)
> - **冷拔维护：**[X1 系列](../../x1/maintenance/what-is-cold-pull-and-how-to-perform-it.md)；[P1 系列](../../p1/manual/p1s-cold-pull.md)

**X1/P1 系列喷嘴配件分类：**

![x1p1_系列喷嘴配件分类](https://wiki.bambulab.com/filament-acc/acc/nozzles/16.x1p1_系列喷嘴配件分类.png)

（左侧为单个喷嘴组件，右侧为整套热端组件）

- **单个喷嘴组件**：仅更换金属喷嘴本体，无加热片、热端风扇、热敏电阻或硅胶套等，适合复用原有热端电子元件的情况，成本更低。

  - **购买链接：**[X1/P1 系列喷嘴组件](https://item.jd.com/10058365307258.html)
- **整套热端组件**：包含喷嘴、加热片、热敏电阻、硅胶套和热端风扇，可快速一体化更换，无需额外装配，比较便捷但成本稍高。

  - X1 系列喷嘴的完整热端套装（注：它只与 X1 和 X1C 兼容，与 X1E 不兼容）。  
    **购买链接：**  
    [硬化钢喷嘴的完整热端套装](https://item.jd.com/10067317462187.html)  
    [不锈钢喷嘴的完整热端套装](https://item.jd.com/10061830517199.html)

    ![17.喷嘴的完整热端套装【x1_系列】.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/17.%E5%96%B7%E5%98%B4%E7%9A%84%E5%AE%8C%E6%95%B4%E7%83%AD%E7%AB%AF%E5%A5%97%E8%A3%85%E3%80%90x1_%E7%B3%BB%E5%88%97%E3%80%91.jpg)
  - P1 系列喷嘴的完整热端套装  
    **购买链接：**  
    [硬化钢喷嘴的完整热端套装](https://item.jd.com/10067317462187.html)  
    [不锈钢喷嘴的完整热端套装](https://item.jd.com/10067317152309.html)  
    ![18._-_喷嘴的完整热端套装【p1_系列】.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/18._-_%E5%96%B7%E5%98%B4%E7%9A%84%E5%AE%8C%E6%95%B4%E7%83%AD%E7%AB%AF%E5%A5%97%E8%A3%85%E3%80%90p1_%E7%B3%BB%E5%88%97%E3%80%91.jpg)

### ⭐ 喷嘴-机型适配表

💡**提示**：表格可**上下滑动**查看更多信息。

| 产品名称 | 图片 | 适配机型 |
| --- | --- | --- |
| [TPU 热端](https://item.jd.com/10213815463816.html?pcdk=EQz3y1RRCoTlqEsYSe2kcYktrYddxwFV2gnDAJFhGy0%3D.M8AW.sbc1) | H2 系列/P2S 热端喷嘴 | H2D 与 H2D Pro 的右热端 |
| [H2 系列/P2S/X2D 热端喷嘴](https://item.jd.com/10145051294182.html) | H2 系列/P2S 热端喷嘴 | H2D, H2S, H2C, P2S, X2D |
| [H2C 智能感应热端](https://item.jd.com/10200112744649.html) | H2C 智能感应热端 | H2C |
| [X1C/P1 系列热端喷嘴](https://item.jd.com/10058365307258.html) | X1C/P1 系列热端喷嘴 | X1C, P1P, P1S |
| [A 系列热端喷嘴](https://item.jd.com/10087803259803.html) | A1 系列热端喷嘴 | A1 mini, A1, A2L |
| [高流量硬化钢热端喷嘴 - H2/P2S/X2D](https://item.jd.com/10145051305491.html) | 高流量硬化钢热端喷嘴 - H2/P2S | H2D, H2S, H2C, P2S, X2D |
| [不锈钢喷嘴全金属热端套装【X1 系列专用】](https://item.jd.com/10061830517199.html#switch-sku) | 不锈钢喷嘴全金属热端套装【X1 系列专用】 | X1C |
| [硬化钢喷嘴全金属热端套装【X1 系列专用】](https://item.jd.com/10058364850753.html) | 硬化钢喷嘴全金属热端套装【X1 系列专用】 | X1C |
| [不锈钢喷嘴全金属热端套装【P1 系列专用】](https://item.jd.com/10067317152309.html) | 不锈钢喷嘴全金属热端套装【P1 系列专用】 | P1P, P1S |
| [硬化钢喷嘴全金属热端套装【P1 系列专用】](https://item.jd.com/10067317462186.html) | 硬化钢喷嘴全金属热端套装【P1 系列专用】 | P1P, P1S |
| [碳化钨喷嘴](https://item.jd.com/10211584828822.html?pcdk=AT4tISGVv9iLh0b9s01RicIKpHjgY9lrO7apMeqXIbnL_UV3Ku-r6IlCfZ1ir6kl.rQ4a.tlbT#switch-sku) | 碳化钨喷嘴 | H2D, H2S, H2C, P2S, X2D |
| [碳化钨高流量喷嘴](https://item.jd.com/10211585701067.html?pcdk=4UpE6WAT_H918SdYfUBrskM7-efpqDdUABH5mkuQ6cmPW9VI_I8MxpjjVGjRcgdb.rQ4a.tlbT#switch-sku) | 碳化钨高流量喷嘴 | H2D, H2S, H2C, P2S, X2D |

> ℹ️ **喷嘴适配性说明：**
>
> - A2L 打印机虽然支持使用拓竹全系列机型的快拆热端，但**无法保证一定带来性能提升**。为了确保最佳打印效果，A2L 打印机请使用 A 系列喷嘴进行打印。

## **喷嘴（热端）硅胶套**

喷嘴硅胶套是包裹在喷嘴外部的黑色保护套，由优质硅胶制成，具有超强耐温性（额定温度高达300°C），提供最佳的隔热性能，使喷嘴能够在打印过程中保持温度稳定，减少热量流失，同时还能提供持久保护，防止耗材粘在喷嘴表面。如果没有硅胶套，部件冷却风扇会使喷嘴温度降低，导致温度波动，影响打印质量。  
![all_socks.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/all_socks.jpg)

### **H2 系列硅胶套**

由优质硅胶制成，具有更高的耐温性(额定温度高达300°C)。可为热端提供最佳的隔热性能，使其在打印过程中保持稳定的温度，同时还能提供持久保护，防止耗材粘在热端上。

**适配机型：**H2D / H2D Pro / H2C / H2S

**购买链接：** [H2 系列硅胶套](https://item.jd.com/10145040750867.html)

![21.h2_系列硅胶套.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/21.h2_%E7%B3%BB%E5%88%97%E7%A1%85%E8%83%B6%E5%A5%97.jpg)

### **X1/P1 系列硅胶套**

由优质硅胶制成，具有更高的耐温性(额定温度高达300°C)。可为热端提供最佳的隔热性能，使其在打印过程中保持稳定的温度，同时还能提供持久保护，防止耗材粘在热端上。

**适配机型：**X1C / P1P / P1S

**购买链接：** [X1/P1 系列硅胶套](https://item.jd.com/10058365880483.html)

![22.x1p1_系列硅胶套.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/22.x1p1_%E7%B3%BB%E5%88%97%E7%A1%85%E8%83%B6%E5%A5%97.jpg)

### **P2S/X2D 硅胶套**

与以往机型的硅胶套不同，P2S 硅胶套具有三个橙色 marker 点，是 P2S 特有的设计，用于 AI 识别功能，以检测喷嘴是否安装了硅胶套，如未安装带 marker 的硅胶套，系统会自动出现报错，提示安装硅胶套；若使用旧版本硅胶套，同样也会导致报错。

X2D 和 P2S 共用同一类硅胶套，但无 AI 识别功能。

**适配机型：** P2S/X2D

**购买链接：** [P2S/X2D 硅胶套](https://item.jd.com/10194459622494.html)

![23.p2s_硅胶套.png](https://wiki.bambulab.com/filament-acc/acc/nozzles/23.p2s_%E7%A1%85%E8%83%B6%E5%A5%97.png)

### A2L 硅胶套

由优质硅胶制成，具有更高的耐温性。硅胶套为热端提供优质的隔热性能，使其在打印过程中保持稳定的温度，同时起到保护作用，防止耗材粘在热端上。

**适配机型：** A2L

**更换指南：** [更换 A2L 热端硅胶套](../../a2l/maintenance/replace-silicone-sock-for-hotend.md)

**购买链接：** [A2L 热端硅胶套](https://item.jd.com/10224277526854.html?pcdk=yL13HC2JBY7zg5aik8XiiJasWf9_41z6VR533M461CY=.M8AW.sbc1)

![fah071.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/fah071.png)

### **A1/A1 mini 硅胶套**

由优质硅胶制成，具有更高的耐温性(额定温度高达300°C)。可为热端提供最佳的隔热性能，使其在打印过程中保持稳定的温度，同时还能提供持久保护，防止耗材粘在热端上。

**适配机型：**A1 / A1 mini

**购买链接：** [A1/A1 mini 硅胶套](https://item.jd.com/10085236731073.html)

![24.a1a1_mini_硅胶套.jpg](https://wiki.bambulab.com/filament-acc/acc/nozzles/24.a1a1_mini_%E7%A1%85%E8%83%B6%E5%A5%97.jpg)

## 相关链接

[耗材指南 —— 耗材与机型、喷嘴、AMS、打印板、胶水的兼容性、适配性及参数设置](../../general/filament-guide-material-table.md)

[使用 0.2mm 喷嘴打印 - FAQ](../../knowledge-sharing/02-mm-nozzle-FAQ.md)

[如何有效防止喷嘴堵塞](../../knowledge-sharing/how_to_avoid_nozzle_clogs.md)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
