---
path: zh/bambu-studio/color-mixing
title: "混色打印"
description: "本文介绍混色打印（也称叠色打印）的具体步骤与注意事项，帮助您学习如何使用 Bambu Studio 的颜色混合功能，在单次打印中通过双色或三色混合，实现自定义色调与渐变效果。"
tags: []
created: 2026-07-02T09:02:15.300Z
updated: 2026-11-04T07:11:35.385Z
source: https://wiki.bambulab.com/zh/bambu-studio/color-mixing
---

## 混色打印

传统的多色 3D 打印中，能够使用的颜色往往受限于打印机可连接的 AMS 数量，以及 AMS 中可装载的耗材卷数量，而 Bambu Studio 的 **颜色混合功能** 突破了这一限制。该功能可在单次打印中组合不同的单色耗材，通过自定义比例，混合生成多种混色、渐变色效果。其原理是将模型的基础单层拆分为 2-3 个更薄的子层，每层使用不同颜色的耗材打印，最终打印成品在视觉上会产生颜色混合的效果，呈现出全新的色调。

如下图所示的所有小船，仅使用了四种颜色的耗材（CMYK：青、品红、黄、白）进行混色，单盘打印而成。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/benchies-intro.jpeg)

> ⚠️ **Bambu Studio 版本要求：** 若要使用混色打印功能，请将 Bambu Studio 更新至 v2.5.3 版本及以上；若要使用渐变颜色曲线图功能，需更新至 v2.7.1 版本及以上。

## 耗材推荐

推荐使用 **拓竹 PLA Palette 耗材套装**，这是一款专门用于 FDM 叠色功能的混色耗材套装，共包含 5 种颜色的耗材，分别是**青色（Cyan）、品红（Magenta）、黄色（Yellow）、半透明黑（Key）、白色（White）**，即 **CMYKW** 组合。PLA Palette 耗材经过官方测试，混色映射的颜色更准确，配合 Bambu Studio 的混色功能及其内置的色彩数据库，能够轻松实现为多色模型一键自动调色，无须手动调整混色参数。

此外，也可使用拓竹 **PLA Basic** 颜色相似或一致的耗材组成 CMYKW 组合进行混色打印；不过，自行组合的色彩无法保证混色效果。

> **注意：** 仅支持 **相同类型的耗材** 相互混色（例如全部为 PLA 耗材）。不支持 PLA 与 PETG 或其他类型耗材之间互相混色。

## Bambu Studio 界面与功能指南

混色打印主要通过 Bambu Studio 的混色功能实现。混色功能有两种实现方式：

**一、手动添加混色耗材** （适用于 **3MF** 格式的模型文件）

**二、使用纹理转涂色功能自动匹配混色耗材** （适用于 **GLB、OBJ** 等格式的带纹理信息的模型文件）

本章节分别为您介绍如何通过这两种方式完成混色打印。

### 一、添加与匹配混色耗材

**①** 点击 **项目耗材列表** 底部的 **添加混色耗材** 按钮 1 。

**②** 弹出混色功能窗口 2 ，其中包含两个子窗口 3 和 4 。

**③ 手动混色**：手动选择并搭配现有耗材，创建新的混色耗材。

**④ 颜色匹配**：先选择目标颜色，系统根据现有耗材自动搭配出最接近的颜色。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/color-mixing-window.png)

#### 手动混色

1 **手动选择**：通过下拉菜单选择想要混合的颜色。

2 **混色推荐**：色块为现有耗材可搭配出的所有混色结果，点击选择想要的颜色，软件会自动调整混色材料以呈现该目标色。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/manual-mixing.png)

**混色模式有两种：常规模式和渐变模式。**

##### 常规模式

双色或三色混色，使用色盘进行调色，或直接从推荐颜色中选择。

- **双色混合**：拖动色盘条滑块，调节至所需颜色。
- **三色混合**：拖动色盘三角形的滑块，调节至所需颜色。

|  |  |
| --- | --- |
| 双色混合 | 三色混合 |
|  |  |

> **注意：** 只有相同类型的耗材才能相互混色（例如全部为 PLA）。不支持 PLA 与 PETG 或其他耗材类型之间互相混色。

---

##### 渐变模式

渐变模式基于双色混合，可实现丰富的过渡色打印效果。该模式适合装饰花瓶等设计，如下右图所示。

**适用场景**： **双色混合** （暂不适用于三色混合）

|  |  |
| --- | --- |
|  |  |
| 开启渐变效果 | 双色渐变花瓶 |

> **注意**：勾选**渐变效果**后，将自动开启**混色子层**功能。若渐变效果开启失败，请检查**混色子层**功能是否开启。  
> ![mixed_color_sublayer_zh.png](https://wiki.bambulab.com/software/bambu-studio/color-mixing/mixed_color_sublayer_zh.png)

**功能原理**：通过在打印件垂直方向上，改变两种颜色各层的相对厚度，实现视觉上的渐变效果。具体效果可通过在渐变颜色曲线图上自定义控制点来调整。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/edit-material-ratio_zh.png)

**渐变颜色曲线图：** 渐变颜色曲线图可精确控制两种颜色沿打印件高度过渡变化的快慢。在曲线路径上任意位置左键单击可添加自定义控制点，右键单击则可删除控制点。拖动这些控制点，可将明显的颜色突变集中在特定区域、让某种混合色调在中间较长的区段延续，或让颜色过渡平滑收尾，以贴合模型的外形设计。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/gradient-curve.png)

**单个零件渐变效果：** 当打印由多个小部件作为单一对象组合在一起的模型时，**启用单个零件渐变效果** 功能可使多个部件的渐变效果一致：

- **开启时：** 每个独立部件都呈现完整的渐变效果。
- **关闭时（默认）：** 软件默认将所有部件视为一个整体，所有部件在同一个高度上的渐变一致，最高的部件通常能够展现完整的渐变效果，较矮的部件只能呈现部分渐变效果。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/per-part-gradient.png)

#### 颜色匹配

##### 功能介绍

颜色匹配窗口的各个功能模块介绍如下：

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/color-matching-window.png)

1 **目标耗材**：在项目耗材列表的颜色中，选择想要通过混色来形成的颜色。

2 **混色结果**：目标耗材确定后，这里会同步呈现推荐的混色结果，即系统自动按比例组合已有耗材生成的最接近目标颜色的混色结果。可根据实际色彩需求，在下方条状/三角色块中手动调整比例。

3 **使用官方混色套装：** 若您的打印机中装有 Palette 的 CMYKW 五色耗材，点此即可一键将 CMYKW 耗材导入耗材列表，并且系统会优先使用这些 Palette 耗材进行混色。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/replace-target-color.png)

4 勾选后，混色结果将替换模型上原有的颜色，即前述的目标耗材。

5 设置完毕并点击确定，即可在项目耗材列表中看到新增的混色耗材。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/new-mixed-filament.png)

##### 应用示例

本章节以 MakerWorld 创作者 Dommivat 的 [神龙](https://makerworld.com.cn/zh/models/2031819-shen-long?appSharePlatform=copy#profileId-2695144) 模型为例，演示如何使用 Bambu Studio 颜色匹配功能，搭配 Palette CMYKW 五色耗材混色打印出近似原模型的效果。

###### 步骤 1. 导入模型

|  |  |
| --- | --- |
|  |  |

###### 步骤 2. 添加并应用混色耗材

1. 首先，记下原模型颜色及序号，它们是目标颜色，在后续步骤中须分别为它们创建混色耗材。本示例中为色号 ①-⑥。

> **注意**： **耗材栏** 中的 **CMYKW** 五种基础颜色的 **PLA Palette 耗材** 不属于目标颜色，无须为其添加混色耗材。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/target-colors.png)

2. 创建色号 ①-② 的混色耗材：

   - 首次创建时，选择使用官方混色套装，一键将 CMYKW 耗材导入耗材列表，以便应用于颜色匹配。
   - 每个混色耗材的创建都需勾选“用混色结果替换模型上的目标颜色”，以便将混色结果应用至模型。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/mix-colors-1-2.webp)

3. 创建色号 ③-④ 的混色耗材：

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/mix-colors-3-4.webp)

**注意：** 若模型存在颜色与 PLA Palette 的 CMYKW 五种色彩同色的情况，无须为其创建混色耗材。可根据下图步骤将其合并至同色 PLA Palette，即可应用至模型。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/merge-same-color.png)

4. 创建色号 ⑤-⑥ 的混色耗材：

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/mix-colors-5-6.webp)

5. 原模型六种颜色对应的 PLA Palette 混色耗材均已创建并匹配完成，且已应用在模型上。前后效果对比如下：

|  |  |
| --- | --- |
| 原模型 | 混色模型 |
|  |  |

###### 步骤 3. 调整预设参数

颜色匹配完成后，可根据模型特点，调整各类预设参数。

**例如：**

- 调整模型位置、大小、方位等；
- 具有悬空区域的模型需要开启 **支撑**；为获得更好的悬垂叠色效果，建议搭配使用 **PETG** 作为支撑界面，并将顶部 Z 距离设置为 **0**。更多详细教程可参阅：[PLA Basic 与 PETG HF、PETG Basic 互相支撑打印指南](../filament-acc/filament/h2d-pla-and-petg-mutual-support.md)。

**重要：** 建议阅读  [**注意事项→层高设置**](#%E5%B1%82%E9%AB%98%E8%AE%BE%E7%BD%AE) ，合理设置层高，避免影响打印效果。

###### 步骤 4. 切片并发起打印

参数调整完毕后，点击「 **切片单盘** 」以预览切片效果。确认无误后即可开始打印。实际打印效果如下右图所示。

|  |  |
| --- | --- |
| 模型效果 | 实际打印 |
|  |  |

### 二、使用纹理转涂色功能进行混色打印

「 **纹理转涂色** 」功能用于将带纹理贴图的模型转换为多色模型。在耗材匹配环节，可将模型涂色拆解为基础色组合（如 CMYKW）以实现混色打印。

> **目前支持纹理转换的格式**：OBJ、glTF、GLB、FBX（需包含纹理贴图）

本章仅介绍纹理转涂色的 **混色** 相关功能。如需了解纹理转涂色的完整功能和使用方法，请阅读这篇 Wiki 教程： [**纹理转涂色**](../software/bambu-studio/texture-to-color.md) 。

|  |  |
| --- | --- |
|  |  |
| 带贴图的纹理模型 | 通过纹理转涂色进行混色后的多色模型 |

Bambu Studio 在导入带有纹理贴图的模型后，会自动弹出 **纹理转涂色** 功能设置窗口。

窗口设置流程共分为两步：「 **简化颜色** 」与「 **耗材匹配** 」。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/texture-color-window.png)

#### 步骤 1. 简化颜色

设置颜色数目、边缘平滑度、间隙面积。参数介绍详见： [**纹理转涂色**](../software/bambu-studio/texture-to-color.md) 。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/simplify-colors.png)

#### 步骤 2. 耗材匹配

1. 点击「**使用官方耗材套装**」，将 PLA Palette 的 CMYKW 五色耗材添加至项目耗材列表，软件便会使用这五种颜色一键自动混合出模型需要的颜色，并匹配至模型对应的位置。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/filament-matching.webp)

2. 点击确定，跳转至 Bambu Studio 准备页面，导入完成。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/prepare-page.png)

#### 步骤 3. 调整预设参数

可根据模型特点，调整各类预设参数。

**例如：**

- 调整模型位置、大小、方位等；
- 具有悬空区域的模型需要开启 **支撑**；为获得更好的悬垂叠色效果，建议搭配使用 **PETG** 作为支撑界面，并将顶部 Z 距离设置为 **0**。更多详细教程可参阅：[PLA Basic 与 PETG HF、PETG Basic 互相支撑打印指南](../filament-acc/filament/h2d-pla-and-petg-mutual-support.md)。

**重要：** 建议阅读  [**注意事项→层高设置**](https://bambulab.feishu.cn/docx/C9X2dAQuso3xE9xhMtmc5pKKnAd#share-SRysda5W6oH4tWxS0Hec4TuLnIh) ，合理设置层高，避免影响打印效果。

#### 步骤 4. 切片并发起打印

参数调整完毕后，点击「 **切片单盘** 」以预览切片效果。确认无误后即可开始打印。实际打印效果如下右图所示。

|  |  |
| --- | --- |
| 模型效果 | 实际打印 |
|  |  |

## 注意事项

### 层高设置

有关混色打印的层高设置主要涉及 「**混色子层**」 与「**可变层高**」。混色打印前，建议阅读本章节，结合模型实际情况设置层高相关的参数。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/layer-height.png)

#### 混色子层

混色子层是用于为混色耗材分层的功能，其开关位置在左侧栏 **「工艺」→「质量」→「层高」** 中。

- **打开混色子层**

启用混色子层后，使用混色耗材的层会按比例拆分为更薄的子层，以实现更均匀的混色效果。

例如，在 **1:9** 的混色比例下，如果工艺层高为 0.2 mm，软件可能会将该层拆分为：

- 黑色：0.18 mm
- 蓝色：0.02 mm

**推荐层高：** 在使用 0.4 mm 喷嘴时，建议使用 0.20 / 0.24 mm 层高预设，由子层承担混色。

> **注意**：混色子层可能产生较小层高，最小可达 **0.02 mm**。极小层高可能导致熔体破裂，从而影响模型表面质量，但通常不会导致打印失败。降低打印速度可以缓解该问题，但无法完全消除。如果希望获得更好的表面质量，建议避免使用过于极端的颜色比例，以减少极小层高的产生；相应地，颜色准确度可能会有所下降。

|  |  |
| --- | --- |
|  |  |

- **关闭混色子层**

关闭混色子层后，软件会按照工艺参数中的层高进行切片，并为每一层分配一种颜色。此时混色本质上是通过不同颜色层之间的排列比例来实现混色效果。

**推荐层高**：0.08 / 0.10 / 0.12 mm

**适用场景**：

- 打印 **层高较小的微缩模型** 时，建议 **关闭混色子层**，使用固定层高，比例推荐如下：
  - 双色混色推荐比 `1:1` / `1:2`
  - 三色混色推荐比 `1:1:1`
- 颜色比例较均衡的场景较适合关闭混色子层，例如 **1:1、1:2、1:3** 等。这类比例通常可以获得较均匀的视觉混色效果。颜色比例过于极端时，例如 **1:9**，颜色层分布不够均匀，混色效果会明显下降。如下图所示，左侧为 **1:1**，右侧为 **1:9**。

|  |  |
| --- | --- |
|  |  |

#### 可变层高

⚠️ 混色打印时，不建议同时使用 **可变层高** 和 **混色子层**，以避免打印效果不佳。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/variable-layer-height-zh.png)

例如，在下图示例中，启用可变层高可能导致颜色过渡不均匀，且可能生成较小的层高，例如 **0.08 mm**。在此基础上启用混色子层时，软件会继续将该层拆分为更小的子层，可能导致层高过小，从而影响打印质量。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/variable-layer-uneven.png)

> 有关可变层高的介绍，请阅读：[可变层高 | Bambu Lab Wiki](../software/bambu-studio/adaptive-layer-height.md)

### 打印机选择

建议使用 **多喷嘴打印机** 进行混色打印。

**原因**：混色打印由于有效层高较小且颜色切换频繁，与非混色打印相比，单喷嘴打印机会产生大量废料，打印时间也会明显延长。因此，大量使用混色进行打印的模型，建议使用多喷嘴打印机。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/mixed_filament_switch_fidgets.png)

**示例**：使用四种源耗材、约进行 246 次换料时，单喷嘴打印机消耗 185.63 g 耗材，而多喷嘴打印机共消耗 112 g 耗材——可节省约 72 g 耗材和 151 次换料。

|  |  |
| --- | --- |
|  |  |
| 双喷嘴的 H2D 打印机 | 单喷嘴的 H2S 打印机 |

### 模型选择

具有以下特点的模型能呈现出最佳效果和最均匀的混色：

- 侧壁均近乎垂直的模型
- 斜面、悬垂及曲面顶面较少的模型

## 实用技巧

1. **深浅色占比**：深色往往会主导最终成色，通常应调低深色耗材的混色占比。
2. **优先使用双色混合**：双色混合能产生更纯净、更可控、更可预测的效果。
3. **先打印测试色块**：正式打印前，建议先打印小测试色块观察结果并精调。
4. **减少冲刷废料**：启用“冲刷到对象的填充”和“冲刷到对象的支撑”。

## 功能原理

由于 PLA 等耗材本身略带半透明性，Bambu Studio 会将目标颜色拆分为一系列极薄且交替排列的层。当以精细的层高打印时，我们的眼睛会自然地将这些微层融合在一起，从而感知到一种全新的中间色调。

颜色预测方法基于 [@ratdoux](https://github.com/ratdoux) 在 OrcaSlicer-FullSpectrum 中提出的方案，由 Bambu Studio 团队在 v2.6.1 中进行了更新和集成。其他所有部分——用户界面与打印路径（toolpath）编排——均由 Bambu Studio 团队独立开发。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
