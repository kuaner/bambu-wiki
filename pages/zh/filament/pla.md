---
path: zh/filament/pla
title: "PLA 使用指南"
description: ""
tags: ["耗材"]
created: 2025-09-30T07:37:50.780Z
updated: 2026-07-27T04:22:23.454Z
source: https://wiki.bambulab.com/zh/filament/pla
---

> 📌 **耗材使用注意事项**：
>
> 1. 请在**阴凉、避光、干燥**环境中存放耗材，避免阳光直射或高温环境。
> 2. 请将耗材及折断的碎屑放在**婴幼儿及宠物无法触及**的地方，避免吞咽和窒息的风险。
> 3. 对于已拆封耗材，建议使用前按照指南中推荐的温度和时间进行**烘干**。**PLA Wood** 耗材由于添加了极具吸湿性的木纤维成分，在打印前需要充分烘干，使用后应立即放入含有**有效干燥剂的密封容器**内。
> 4. 建议在**通风良好**的区域使用打印机，或安装有效的空气过滤、外排风系统。
> 5. 除 PLA Pure 以外的 PLA 耗材，均**不属于**食品接触级耗材，请避免将打印成品用于存放或接触食品。
> 6. **PLA-CF** 耗材表面及端口处可能带有肉眼不可见的**硬质微刺**，在处理该类耗材线、拆除支撑或者打磨打印件时，建议佩戴**防刺防割手套并佩戴护目镜**。

Bambu Lab 的 PLA 耗材自带 RFID 芯片，设备自动识别耗材参数，默认参数即可获得较好的打印效果。**对于大部分的耗材（如 PLA）**，您只需参考以下三个步骤即可完成打印。

1. 打印前请用热水和洗洁精清洁打印板，以确保最佳附着力。
2. 在 Bambu Studio 中发起打印。
3. 待打印完成后，请等打印板充分冷却，再取下打印件。

![23-1.png](https://wiki.bambulab.com/filament-acc/beginner/23-1.png)

## 1. 耗材介绍

拓竹的 PLA 由植物等可再生资源生产制成，具有无毒、可降解、易打印等特性。适用于大多数日常项目。在确保使用安全与产品质量的同时减少了对环境的影响。更多的详细信息可以进入 [PLA](https://detail.tmall.com/item.htm?abbucket=9&id=693972799714&pisk=g1lEkwbjjBdUBBs6OcFP0O1JHwVLT7-brbZ7r40uRkqHephzUqiMJU3uVbPrXc2oOWgIbuoSoviQO8Oo_zaf-zf3KG2glzwoVugCJAnjo6GBp71z97FkcnOXGe3Lw7YGStTdvG40kQ1uxkVLsWv8QQdXG23NRyYjSIG7i0X85TfoqJ2MszEGtyqoqR2gylf3r6VujFz8j7f3EuqgsraR-TXnqOAgryS3r6XHsG47o7qoq7YZSlUzZumuZFuigdunr1zbKFAZuu6VCwwum2qNZs7Y8Jfr8T1Paf43Lj0gbFTs_yyUmRCGjJcnf4cI9RpFK73s30komh6Qxxzqb-Me06oqvz0zrDRAulcEzfyKCMX3uWrUnXmGkEg4EAlaOXxRHVgax-PsCdKQFWoEHoeHBhnr7kioTRjefuMj5X2Zmh1Z28koO5cHjISP3gUG2Wc-LgXzKPUacF8abr3ieEmkwt6ReRVY7oTQRTXlcnC5LjzGeTegrPrX54f..&rn=4e7dc14c46e4815a2b4c882c59822636&spm=a1z10.5-b-s.w4011-25176969463.45.31dc6b8eLy91Fo) 官方商品详情页中查看。

![image-100.png](https://wiki.bambulab.com/filament-acc/pla/image-100.png)

### 1.1 硬件兼容性

> 提示：在电脑端可靠近耗材的 ⚠️ 标记查看**不兼容的原因**。

PLA 全系机型均适配，更多兼容性可参考下表：

1. **默认选择**：官方标配 0.4 mm 喷嘴 + 通用打印板 + AMS 系列配件，除下方标记的四种耗材除外，其余均可直接打印。
2. **注意 ⚠️ 标记**：如特殊材料 **PLA Silk/Silk+**⚠️、**PLA-CF**⚠️、**PLA Glow**⚠️和 **PLA Aero**⚠️ ，请遵循喷嘴或其他配件限制。

| 材料 | 喷嘴兼容性（说明） | 打印板兼容性（说明） | 配件兼容性（说明） |
| --- | --- | --- | --- |
| PLA Basic / Matte / Translucent / Tough+ / Lite / Metal | 全部常规喷嘴兼容（无特别限制） | 全部打印板兼容 | AMS 系列全兼容 |
| PLA Silk / Silk+ | 常规喷嘴均可（推荐 0.4 mm 喷嘴） | 不推荐使用低温增稳板 | AMS 系列全兼容 |
| PLA-CF | 兼容硬化钢喷嘴；不建议使用 0.4 mm 高流量喷嘴 | 全部打印板兼容 | 仅拓竹版 PLA-CF 可适配 AMS 全系列 |
| PLA Galaxy / Wood / Marble / Sparkle | 常规喷嘴均可（不含 0.2 mm） | 全部打印板兼容 | AMS 系列全兼容 |
| PLA Glow | 只兼容硬化钢与高流量喷嘴（不兼容 0.2 mm 喷嘴） | 全部打印板兼容 | AMS lite 不兼容 |
| PLA Aero | 只兼容 0.4 mm 喷嘴 | 全部打印板兼容 | AMS 系列全兼容 |
| PLA Pure | 兼容除铜制喷嘴以外的全部常规喷嘴 | 全部打印板兼容 | AMS 系列全兼容 |

> 注意：PLA Wood、PLA Glow、PLA Translucent⚠️、PLA Galaxy⚠️、PLA Marble⚠️、PLA Sparkle⚠️ 均不兼容 0.2 mm 不锈钢喷嘴。

## 2. 打印前的准备

PLA Basic 耗材是最容易打印的耗材之一，开封即可打印，一般无需其他调整。**但需要特别注意的是，所有耗材在剪断四根固定带后必须拿好线头，以免耗材散开。** 除了 PLA Basic，还有一些 PLA 品类因成分特殊需要特别注意，而为了进一步确保打印质量，您可以参考下述建议进行**打印前的准备工作**。

### 2.1 耗材烘干

PLA 材料本身吸湿性较低，在 50%–60% 的环境湿度下可正常存放，通常无需像 PETG 或尼龙等材料那样频繁干燥。但表格中的**以下五类特殊 PLA** 材因材质构成不同，建议在打印前进行烘干处理，以避免因残留水分在打印时产生气泡、孔洞或透明度下降，影响模型表面质量。 [耗材烘干操作指南](../filament-acc/filament/dry-filament.md)

| 材料类型 | 鼓风式烤箱 | 热床 | AMS HT/AMS 2 pro |
| --- | --- | --- | --- |
| **PLA Silk / Silk+ / Wood / Aero / Pure** | 55℃，8 h | 70℃，12 h | 55℃，8 h |
| **PLA CF / Translucent** | 50℃，8 h | 70℃，12 h | 55℃，8 h |

> **注意：**
>
> - 使用热床进行耗材烘干时，请每隔 6 小时将耗材翻面一次，并在耗材上方覆盖耗材包装盒或 PC 盒。
> - 若使用 [AMS HT](https://wiki.bambulab.com/zh/ams-ht/Intr-to-ams-ht-workflow-and-features#%E8%80%97%E6%9D%90%E7%83%98%E5%B9%B2%E5%8A%9F%E8%83%BD) / [AMS 2 Pro](https://wiki.bambulab.com/zh/ams-2-pro/manual/setup-and-printting#%E7%83%98%E5%B9%B2%E5%8A%9F%E8%83%BD) 进行烘干，耗材在高温下可能会发生软化，进而被送料齿轮挤压而变形，导致送料失败。请务必遵循设备对应链接中的温度设定与操作流程。

## 3. 打印注意事项

### 3.1 常规提醒

如先前打印过 ABS、PC 等高温材料，建议先执行喷嘴冷拔操作，避免残留物料导致 PLA 打印堵塞或失败。详细操作请参阅喷嘴的[冷拔喷嘴操作](../p1/manual/p1s-cold-pull.md)。

### 3.2 需特别关注的耗材类型

若您使用的是 [**PLA Aero**](https://wiki.bambulab.com/zh/filament/pla#pla-aero)、[**PLA Wood**](https://wiki.bambulab.com/zh/filament/pla#pla-wood) 、[**PLA-Glow**](https://wiki.bambulab.com/zh/filament/pla#pla-glow) 和 [**PLA-CF**](https://wiki.bambulab.com/zh/filament/pla#pla-cf)，可以直接跳转至本文中对应的位置。

> **提示：若您使用其他 PLA 可直接忽略下文，直接开始打印。**

- PLA Aero（需调整软件设置 + 简化模型）
- PLA Wood（需提前烘干 + 注意通风）
- PLA-CF（定期冷拔喷嘴 + 预防断料）
- PLA-Glow（AMS Lite 不适配+减少进料阻力）

#### PLA Wood

> **不建议**使用 0.2 mm 不锈钢喷嘴，因为该种耗材由高品质 PLA 与细木粉混合制成，会堵塞这种型号的喷嘴。

- 由于 PLA Wood 中添加了天然木粉让木质 PLA 具有轻微、自然的木质香气。该气味在打印过程中较为明显，属于非刺激性气味且无毒性。若对于该气味较为敏感，建议打印时做好室内通风等工作。
- **天然木粉容易吸水受潮，因此打印前需要进行烘干，避免打印时产生拉丝的情况。**

![wood_烘干与否.jpg](https://wiki.bambulab.com/filament-acc/pla/wood_%E7%83%98%E5%B9%B2%E4%B8%8E%E5%90%A6.jpg)

#### PLA-CF

> **❗ 重要提示**：PLA-CF为碳纤增强耗材，在其使用、后处理、或接触其打印件的粗糙/断裂表面过程中，可能产生细小的纤维碎屑，存在皮肤机械性刺伤、皮肤过敏或异物刺激等风险。因此，**请避免裸手直接触摸或摩擦**粗糙边缘或断面。建议在装卸耗材、剪切打磨及其他后处理操作时**佩戴防护手套**，并根据实际需要佩戴其他防护用具。

**使用提示**

- **必须**使用**硬化钢喷嘴。不宜**使用 0.2 mm 不锈钢喷嘴，因为该种耗材含有碳纤颗粒，会堵塞这种型号的喷嘴。不建议使用 0.4 mm 高流量喷嘴，因为打印模型时会导致模型的[悬垂结构打印质量差](../filament-acc/filament/print-quality/overhang.md)。适配拓竹全系列 AMS ，官方有专门适配的设计。

- 若长期使用该耗材，推荐您进行定期使用 PLA Basic 或者PLA Matte 进行**冷拔喷嘴**的操作，这是一种常见的机器清理维护手段，通过拔出耗材清理喷嘴内部的灰尘、堵塞或残留物，可以更好地保证打印质量。更多的相关操作可以参考下面的视频：

#### PLA Aero

> **不建议**使用 0.2 mm 不锈钢喷嘴，因为该种发泡后的材料在打印时会膨胀，容易堵塞喷嘴，会堵塞这种型号的喷嘴。此外，不建议使用 0.6 / 0.8 mm 的硬化钢喷嘴，因耗材的强流动性会导致漏料。由于 PLA Aero 耗材较软，如遇到进料失败可使用外挂料盘的方式打印。

**操作提示**

- 在 Bambu Studio 中，取消勾选「动态流量校准」
- 优先选择结构简单的模型（如下面右图），复杂模型需将薄壁加厚至 ≥1 mm。PLA Aero 流动性较强、体积膨胀明显，若回抽位置过多易造成漏料，因此不推荐打印空驶较多的复杂模型（如下面左图）。

> 名词解释：**空驶**指的是 3D 打印机喷嘴在不挤出材料时的移动路线，也叫“空走”“空程”或英文里的 travel move。

![发泡测试.png](https://wiki.bambulab.com/filament-acc/pla/%E5%8F%91%E6%B3%A1%E6%B5%8B%E8%AF%952.png)

**补充说明**

- 由于 PLA Aero 的硬度较低，**动态流量校准可能无法得到准确结果**，甚至会在打印校准线时出现拉丝、漏料等问题。该发泡耗材较为特殊，修改参数可以获得更好的打印效果。您可以参考下文 5.3 了解到更多相关内容。
- 此材料对**挤出压力**非常敏感。若模型结构过于复杂，频繁的挤出量变化容易导致拉丝、飞边、过度挤出或填充不均，从而产生内部气泡。

#### PLA-Glow

> **必须使用硬化钢喷嘴。不建议**使用 0.2 mm 和 0.4 mm 不锈钢喷嘴，因为该种耗材配方中添加了夜光粉，会磨损这种型号的喷嘴。另外，不建议配合 AMS lite 使用，该种耗材会导致进退料阻力太大，导致打印失败。

**使用提示**

- 在打印 PLA Glow 时可能会因其耗材表面较为粗糙的缘故出现打印中断的情况。建议如果没有特殊需求，优先外挂料盘打印。

## 4. 常见打印问题与解决方案

### 4.1 热蠕变导致挤出机堵塞

1. **PLA 材料的耐热性限制**  
   PLA 材料的耐热性较低，热变形温度只有57℃。当环境温度过高，同时使用需要较高热床温度的打印平台（如纹理板）时，打印机内部温度可能逐渐升高至大于57℃，从而使 PLA 在挤出机内提前软化，进而引发堵塞问题。

![](https://wiki.bambulab.com/filament-acc/pla/%E7%83%AD%E8%A0%95%E5%8F%98%E6%BC%94%E7%A4%BA.jpg)

> 名词解释：热变形温度（Heat Deflection Temperature, 简称 HDT）是衡量塑料在特定载荷作用下，抵抗变形的能力的温度，代表材料在高温和受力双重影响下开始失去刚性并发生规定变形的临界点。

2. **推荐的打印环境条件**  
   建议在通风良好、环境温度适宜（推荐 10–30 °C）的条件下打印 PLA，以避免机仓内热量积聚，确保打印过程顺利。
3. **高温季节的应对措施**  
   这类问题多见于炎热的夏季。若环境温度偏高，建议打开打印机仓门，并适当降低热床温度。以 PLA 为例，热床温度可在原来**默认 55 度**的基础上适当**降低 5-10 度**。

|  |  |
| --- | --- |
| 热变形温度 | 设置热床温度位置 |

### 4.2 PLA Aero 打印质量差

PLA Aero 在打印时容易出现漏料的情况（如下方左图），通常表现为喷嘴渗料、打印间隙时滴料，或在耗材回抽后仍漏料。当参数调整正确且耗材完全烘干后，打印结果应为下面的右图。

![plaaero.png](https://wiki.bambulab.com/filament-acc/pla/plaaero.png)

可以参考以下解决方案进行操作：

1. **打印前深度烘干耗材**

PLA Aero 在潮湿状态下较容易出现漏料的情况，建议将耗材进行一次深度烘干以避免在打印期间出现漏料的情况。若出现首层不粘的情况可以考虑先[清洗打印板](../filament-acc/acc/pei-plate-clean-guide.md)。

2. **打印前调整参数**

可以点击以下链接下载 PLA Aero 打印航模的配置文件，然后用拓竹切片软件 “打开”，并 “导入目标打印模型” 以获得调整好的适配大部分打印场景的拓竹发泡 PLA 参数。请注意，该参数并不一定适合所有的打印模型和材料，请根据实际情况和需求适当调整。

- [pla\_aero\_配置文件(非花瓶模式).3mf](https://wiki.bambulab.com/filament-acc/pla/pla_aero_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6(%E9%9D%9E%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F)-%E6%96%B0_(1).3mf)
- [pla\_aero\_配置文件(花瓶模式).3mf](https://wiki.bambulab.com/filament-acc/pla/pla_aero_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6(%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F)-%E6%96%B0_(3).3mf)

3. **打印后检查喷嘴**

打印完成后，检查喷嘴是否有明显磨损。

- 对 **A 系列** 和 **H2 系列** 用户，也可以参考喷嘴截面来判断磨损情况。（如下图左边的喷嘴已严重磨损）
- 及时更换磨损严重的喷嘴，可以保证后续打印质量。

![](https://wiki.bambulab.com/filament-acc/pla/image-4.png)

### 4.3 PLA Silk 外墙色彩差异

PLA Silk 的常见问题主要有模型表面光泽度不均和打印件强度不足。另外建议在使用该种耗材之前**需要烘干，避免产生拉丝等现象**。以下这两个问题的解决方案。

#### 案例一：局部速度差异过大

在模型打印切片前查看一下切片结果速度卡中的速度变化是否过大（如下面左图），若局部速度差异过大的话可以将整体速度调至均一，以确保耗材在打印后呈现出的颜色一致，不同的打印速度会导致[模型不同区域的光泽具有差异](../filament-acc/filament/print-quality/different-gloss.md)。具体的参数设置详见本章的5.1。

|  |  |
| --- | --- |
| 切片结果观察打印速度变化 | 模型光泽度差异 |

#### 案例二：丝绸耗材打印件强度不足

##### 材料特性

PLA Silk 因成分原因，**层间粘合性能较弱**。与普通 PLA 相比，Z 轴方向强度显著降低，约为 PLA Basic 的65%；而 XY 方向强度则与普通 PLA 基本相当。

| **耗材类型** | **冲击强度（Z）** |
| --- | --- |
| PLA Silk | 8.5kJ/m² |
| PLA Basic | 13.8kJ/m² |

##### 解决方案

**情况一：对强度要求较高的打印件**

- **问题表现：** 打印件在受力时，容易因 Z 轴方向强度不足而断裂。
- **调整建议：**

  - 优先将模型的受力方向调整到 XY 平面，以利用较好的 XY 层间强度。（请注意：只有外墙有丝绸光泽，顶面没有丝绸光泽）
  - 若方向无法调整，可通过**增加墙层数和填充密度**来增强整体强度。
  - 具体参数设置可参考[强度高级设置](../software/bambu-studio/parameter/strength-advance-settings.md)进行定制化设置。

![](https://wiki.bambulab.com/filament-acc/pla/image-6.png)

**情况二：细长零件容易在打印过程中断裂**

- **问题表现：** 模型打印过程中，细长结构的模型常因材料脆性和晃动应力而断裂。
- **调整建议：**

  - 适当降低打印速度，减少挤出和晃动带来的应力。
  - 为零件增加**额外支撑**，必要时可在 Bambu Studio 中**手动绘制支撑**。

  ![](https://wiki.bambulab.com/filament-acc/pla/image-7.png)

  - 操作方法可参考[支撑绘制指南](../software/bambu-studio/support-painting.md)。

|  |  |
| --- | --- |
| 切片结果观察手动绘制支撑生成结果 | 细长零件打印结果 |

### 4.4 模型表面出现环形凸起纹路

在盒子类模型的大底面与薄壁交界处，或小船模型的腰部区域，外壁表面可能出现异常的环形凸起纹路，这类现象我们通常统称为变截面类层纹。

![image-29.png](https://wiki.bambulab.com/filament-acc/pla/image-29.png)

可以参考以下几个方法进行解决（需要在建模软件中操作）：

1. 模型增加内侧圆角：切片后桥接不再与内墙接触。

![](https://wiki.bambulab.com/filament-acc/pla/image-15.png)

2. 模型增加内侧斜角，切片后桥接几乎不与内墙接触。

![](https://wiki.bambulab.com/filament-acc/pla/output.gif)

> 提示：更多关于 PLA 的专业知识内容可以继续阅读本文第五节**进阶学习**。如果您遇到的打印问题非以上这几点，可以进入[打印质量与解决办法指南](../filament-acc/filament/print-quality.md)中根据图片展示的现象对应处理。

## 5. 进阶学习

### 5.1 打印出仿丝绸质感

为打出较好的仿丝绸质感，参数的调整将分为外墙与顶面两个部分。

#### 外墙

PLA Silk / Silk+ 的独特外观来自其特殊成分，而打印速度的不同会直接影响表面光泽度：

- **低速打印**：材料有充足时间平整铺展，表面更规则，光泽感更强。推荐将打印速度控制在 **40 – 60 mm/s**。
- **高速打印**：材料被快速挤出，表面微观凹凸增多，光线散射增强，整体光泽感减弱。

- [速度测试件下载.3mf](https://wiki.bambulab.com/filament-acc/pla/%E9%80%9F%E5%BA%A6%E6%B5%8B%E8%AF%95.3mf)

> 温馨提示：在正式打印前，可以先制作一个带速度渐变的[测试件](https://makerworld.com.cn/zh/models/1535030-silkguang-ze-ce-shi#profileId-1672145)，通过对比效果来选择最适合的速度区间，从而获得理想的光泽表现。如下图测试件中为三种速度，分别是 10mm/s，60mm/s 和 120mm/s。
>
> ![](https://wiki.bambulab.com/filament-acc/pla/silk%E6%B5%8B%E9%80%9F%E5%9D%971.jpg)

- **不减慢外墙速度**：在打印 Silk 这种材料是，在耗材丝设置中可以选取“不减慢外墙速度”这个选项，帮助模型减少光泽度变化。

![silk.png](https://wiki.bambulab.com/filament-acc/pla/silk.png)

#### 顶面

当使用阿基米德螺旋的顶面填充（中间最右边）时相较其他填充，其光泽度会更优，但需要注意的是，阿基米德螺旋图案并不适用于所有模型，可根据使用场景选择是否修改填充图案。

![](https://wiki.bambulab.com/filament-acc/pla/2.jpg)

### 5.2 提升透明耗材的透明度

**推荐操作**

- 烘干耗材：打印前请务必充分烘干材料。这一步能有效避免因水汽而产生的挤出气泡和孔洞，是实现均匀透光的基础。
- 选用 0.8mm 喷嘴：我们推荐使用较大尺寸的喷嘴。它可以减少模型表面的打印线条数量，从而显著淡化层纹，提升整体透光表现。

**优化打印设置**

- 降低打印速度：在低速打印时，挤出相较稳定，建议将打印速度控制在 20mm/s。

![](https://wiki.bambulab.com/filament-acc/pla/image-17.png)

- 调整填充与壳层：将顶部与底部壳层数设置为 0，并选择**直线**填充图案。此举可确保光路方向一致，最大程度减少内部折射与重叠。

![](https://wiki.bambulab.com/filament-acc/pla/image-18.png)

- 提高打印温度并提高流量比例：适当提升打印温度，可使材料熔融更充分、挤出更均匀，增强层间结合力。适度提高流量比例，有助于彻底填满打印线条间的微小缝隙，减少光线散射。（请注意：此操作需在耗材完全干燥的前提下进行）

![](https://wiki.bambulab.com/filament-acc/pla/image-19.png)

- 关闭冷却风扇：打印时请关闭所有风扇，让挤出材料自然缓慢冷却。这样可以有效减少因冷却不均带来的内部应力与雾化现象。

![](https://wiki.bambulab.com/filament-acc/pla/image-20.png)

不同的墙层数有一定的区别，可以参考下图的打印效果进行调节。

![](https://wiki.bambulab.com/filament-acc/pla/image-21.png)

> 重要提醒！！
>
> 模型的最终透明度也与其几何结构密切相关。即便采用最佳参数，复杂的内部结构也可能影响透光效果。
>
> 此外，材料本身的光学特性至关重要。PETG 作为非结晶材料，其天然透光性通常优于半结晶的 PLA。

下载预设 3MF 文件并替换成需要打印模型（用其他打印机机型打印时，可迁移下述 X1C 的相应的工艺参数和耗材丝参数）：

1. X1C，0.4 mm 喷嘴：[PLA\_-\_transparent\_parameters\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/pla_-_transparent_parameters_-_0.4_mm_nozzle_.3mf)

> 提示：
>
> 如果以上的进阶调整无法满足您的需求，欢迎进入到 **拓竹学院** —— [Bambu Studio](https://bambulab.cn/zh-cn/support/academy) 篇中进行学习，这是一个拓竹官方的 3D 打印学习平台，致力于为用户提供从基础到进阶的全方位 3D 打印知识培训，助力用户在 3D 打印领域不断提升技能，实现创新与发展。

### 5.3 PLA Aero 打印航模指南

PLA Aero 属于发泡材料，由于其独特的性能，是打印 RC Plane（航模）零件的绝佳选择。这种材料以其较低的密度而闻名，这使得打印模型更轻，是实现航模性能的关键因素。另外，相比于常规的打印材料，用发泡 PLA 打印出来的航模可以避免头部过重或者尾部过重，不必花大量时间去调配飞机的重心，使得航模飞行更加可靠安全。

但是，在使用发泡 PLA 打印时，也有不少注意事项（文末提供了包含适配拓竹发泡 PLA 的打印参数的 .3mf 文件）。该种材料在打印过程中会膨胀，这需要仔细校准打印机并精确控制打印温度。此外，由于其轻质特性，它可能不如其他材料耐用，因此必须考虑零件的预期用途及其承受的应力。最后，进行打磨或喷漆等后处理时需谨慎，以避免损坏打印部件。

| 打印温度 | 最小流量比 | 最大体积膨胀率 | 最大发泡率 | 最小打印密度 |
| --- | --- | --- | --- | --- |
| 190 °C | 0.95 | 100% | 0% | 1.17 g/cm³ |
| 200 °C | 0.89 | 110% | 10% | 1.06 g/cm³ |
| 210 °C | 0.85 | 115% | 15% | 1.02 g/cm³ |
| 220 °C | 0.76 | 129% | 29% | 0.91 g/cm³ |
| 230 °C | 0.62 | 158% | 58% | 0.74 g/cm³ |
| 240 °C | 0.45 | 217% | 117% | 0.54 g/cm³ |
| 250 °C | 0.38 | 258% | 158% | 0.45 g/cm³ |
| 260 °C | 0.35 | 280% | 180% | 0.42 g/cm³ |
| 270 °C | 0.37 | 265% | 165% | 0.44 g/cm³ |

由于旋转花瓶模式可以去除接缝，是打印发泡耗材的不二之选。下文会分为使用旋转花瓶模式与传统模式进行参数调整。

#### 旋转花瓶模式

1. 关闭切片间隙闭合半径；墙生成器选择“经典”

![](https://wiki.bambulab.com/filament-acc/pla/image-22.png)

2. 墙层数设置为 1；顶壳/底壳层数设置为 0； 稀疏填充密度设置为 0%。

![](https://wiki.bambulab.com/filament-acc/pla/image-23.png)

3. 将所有打印速度设置为相同；关闭“悬垂降速”;适当地降低打印加速度。

![](https://wiki.bambulab.com/filament-acc/pla/image-24.png)

![](https://wiki.bambulab.com/filament-acc/pla/image-25.png)

4. 选择“奇偶”切片模式；启用“旋转花瓶”；打印顺序选择“逐件”（如需一盘打印多个模型）。

![](https://wiki.bambulab.com/filament-acc/pla/image-26.png)

#### 传统模式

有些模型用一条走线螺旋上升的方式切片可能会导致细节丢失，所以不建议用“旋转花瓶”模式，需要调整参数。不过大部分的参数都与旋转花瓶模式的切片配置相同，您只需要修改以下部分。

1. 减小或者关闭回抽；关闭 Z 抬升

![](https://wiki.bambulab.com/filament-acc/pla/image-27.png)

2. 接缝按实际切片结果调整，一般选择“最近”

![](https://wiki.bambulab.com/filament-acc/pla/image-28.png)

在打印前进行最后检查，确保整个模型没有太多的**空驶路线**（下图中的深蓝色线）。您还可以使用水平切片条查看每层中的打印顺序，确保走线已闭合。

![qypvbvjtjo79alxtfmycrupnndm.png](https://wiki.bambulab.com/filament-acc/pla/qypvbvjtjo79alxtfmycrupnndm.png)

**可以点击以下链接下载 PLA Aero 打印航模的配置文件，然后用拓竹切片软件 “打开”，并 “导入目标打印模型” 以获得调整好的适配大部分打印场景的拓竹发泡 PLA 参数**。**请注意，该参数并不一定适合所有的打印模型和材料，请根据实际情况和需求适当调整。**

- [PLA Aero 配置文件（花瓶模式）](https://wiki.bambulab.com/knowledge-sharing/rc-with-lwpla/pla_aero_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6(%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F)-%E6%96%B0.3mf)：请根据实际模型结构、用途和切片预览情况来确定是否手动添加顶部壳体层数
- [PLA Aero 配置文件（非花瓶模式）](https://wiki.bambulab.com/knowledge-sharing/rc-with-lwpla/pla_aero_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6(%E9%9D%9E%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F)-%E6%96%B0.3mf)

### 5.4 纯净 PLA 进阶安全打印指南

纯净 PLA 专为 FDM 3D 打印排放安全和接触安全设计，使用纯净 PLA 默认参数打印，即可获得优秀打印质量和接触安全特性。若对成品打印件的接触安全等级要求更高，请参考 [纯净 PLA 安全打印建议](https://wiki.bambulab.com/zh/filament/pla-pure#%E8%BF%9B%E9%98%B6%E5%AE%89%E5%85%A8%E6%89%93%E5%8D%B0%E5%BB%BA%E8%AE%AE) 对模型进行更深度地调整与处理。

![](https://wiki.bambulab.com/filament-acc/filament/pla-pure/2.5.2_cross_dry-coat_method_1.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
