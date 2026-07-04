---
path: zh/bambu-studio/color-mixing
title: "混色打印"
description: "学习如何使用 Bambu Studio 的颜色混合功能，在单次打印中通过双色混合或三色混合，实现自定义的色调和渐变效果。"
tags: []
created: 2026-07-02T09:02:15.300Z
updated: 2026-07-03T04:32:57.368Z
source: https://wiki.bambulab.com/zh/bambu-studio/color-mixing
---

## 混色打印

传统的多色 3D 打印中，能够使用的颜色往往受限于打印机可连接的 AMS 数量，以及 AMS 中可装载的耗材卷数量，因此，多色打印往往需要许多不同颜色的耗材卷来实现。

而 Bambu Studio 的**颜色混合功能**突破了这一限制：该功能可在单次打印中组合多种颜色耗材，自定义颜色混合的比例，生成自定义的色调或平滑的色彩过渡。通过将单层拆分为 2-3 个更薄的层，每层使用不同颜色的耗材打印，最终打印成品在视觉上会产生颜色混合的效果，呈现出全新的色调。

如下图所示的所有小船，仅仅使用了四种颜色的耗材（CMYK 耗材）进行混色，单盘打印而成。

![benchies-intro.jpeg](https://wiki.bambulab.com/software/bambu-studio/color-mixing/benchies-intro.jpeg)

> ⚠️ **Bambu Studio 版本要求：** 若要使用混色打印功能，请将 Bambu Studio 更新至 v2.5.3 版本及以上；若要使用渐变颜色曲线图功能，需更新至 v2.7.1 版本及以上。

## 界面与功能指南

**功能入口**：点击**项目耗材列表**底部的 **添加混色耗材** 按钮 1 进入。在弹出的窗口中，即可在 **选择混色材料** 列表 2 中管理要混合的耗材。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/color-mixing-steps_zh.png)

- **手动混色**：通过下拉菜单 1 选择想要混合的颜色。
- **自动混色**：在 **混色推荐** 2 中选择想要的颜色，软件会自动调整混色材料以呈现该目标色。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/add-mixed-filament_zh.png)

**混色模式有两种：**

- **常规模式：** 双色混色或者三色混色，使用色盘条或色盘三角形进行调色，或直接从下方推荐颜色中选择。
- **渐变模式：** 基于双色的渐变色彩效果，可实现丰富的过渡色打印效果。该模式适合装饰花瓶等设计，例如，可使打印件从底部的沙滩棕无缝渐变到顶部的深海蓝。

### 常规模式

- **双色混合**：拖动色盘条滑块，调节至所需颜色。
- **三色混合**：拖动色盘三角形的滑块，调节至所需颜色。

|  |  |
| --- | --- |
|  |  |
| 双色混合 | 三色混合 |

> **注意：** 只有相同类型的耗材才能相互混色（例如全部为 PLA）。不支持 PLA 与 PETG 或其他耗材类型之间互相混色。

### 渐变模式

**适用场景**：**双色混合** （*暂不适用于三色混合*）

**开启位置**：如下图

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/gradient-effect_zh.png)

**功能原理**：通过在打印件垂直方向上，改变两种颜色各层的相对厚度，实现视觉上的渐变效果。具体效果可通过在渐变颜色曲线图上自定义控制点来调整。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/edit-material-ratio_zh.png)

### **渐变颜色曲线图**

渐变颜色曲线图可精确控制两种颜色沿打印件高度过渡变化的快慢。

在曲线路径上任意位置左键单击可添加自定义控制点，右键单击则可删除控制点。

![twisted-vase-print.png](https://wiki.bambulab.com/software/bambu-studio/color-mixing/twisted-vase-print_zh.png)

拖动这些控制点，可将明显的颜色突变集中在特定区域、让某种混合色调在中间较长的区段延续，或让颜色过渡平滑收尾，以贴合模型的外形设计。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/edit-per-part-gradient-effect_zh.png)

### **单个零件渐变效果**

当打印由多个小部件作为单一对象组合在一起的模型时，**启用单个零件渐变效果** 功能可使多个部件的渐变效果一致：

- **开启时：** 每个独立部件都呈现完整的渐变效果。例如，在同一个打印板上打印高度各异的国际象棋棋子时，每一枚棋子都会呈现完整、独立的渐变。
- **关闭时（默认）：** 切片软件默认将所有部件视为一个整体，这种情况下，最高的部件通常能够展现渐变的完整效果，而较矮的部件则只能呈现部分渐变效果。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/enable-per-part-gradient-effect_zh.png)

## 功能原理

由于 PLA 等耗材本身略带半透明性，Bambu Studio 会将目标颜色拆分为一系列极薄且交替排列的层。当以精细的层高打印时，我们的眼睛会自然地将这些微层融合在一起，从而感知到一种全新的中间色调。

颜色预测方法基于 [@ratdoux](https://github.com/ratdoux) 在 OrcaSlicer-FullSpectrum 中提出的方案，由 Bambu Studio 团队在 v2.6.1 中进行了更新和集成。其他所有部分——用户界面与打印路径（toolpath）编排——均由 Bambu Studio 团队独立开发。

> **注意**：本功能为实验功能，目前暂不支持将包含混色耗材的 3MF 文件上传至 MakerWorld。

## 注意事项

### 耗材要求

仅支持==相同类型的耗材==相互混色（例如全部为 PLA 耗材）。不支持 PLA 与 PETG 或其他类型耗材之间互相混色。

### 层高设置

混色打印时，由于每一层会被拆分为最多三个薄层，因此在使用 0.4mm 喷嘴时，固定层高建议使用 0.12mm、叠层层高建议使用 0.2mm 来获得较为均匀的混色效果。应避免使用极端叠层比例，避免过小层高触发熔体破裂导致打印质量下降。

下图展示了混合比例中蓝色 1 占比 62% 的极厚层、白色 2 占比 31% 的中等层，以及红色 3 仅占 7% 的极薄层。

![](https://wiki.bambulab.com/software/bambu-studio/color-mixing/layer-composition-diagram_zh.png)

### 打印机选择

由于有效层高较小且颜色切换频繁，与非混色打印相比，**单喷嘴打印机会产生大量废料，打印时间也会明显延长**。因此，**大量使用混色进行打印的模型**，建议使用**多喷嘴打印机**。

![mixed_filament_switch_fidgets.png](https://wiki.bambulab.com/software/bambu-studio/color-mixing/mixed_filament_switch_fidgets.png)

**示例**：下图展示了多喷嘴打印机与单喷嘴打印机打印同一模型（使用四种源耗材、约进行 246 次换料）时的切片结果：单喷嘴打印机消耗 **185.63g** 耗材，而多喷嘴打印机共消耗 **112g** 耗材——可节省约 72g 耗材和 151 次换料。

|  |  |
| --- | --- |
|  |  |
| 双喷嘴的 H2D 打印机 | 单喷嘴的 H2S 打印机 |

### 模型选择

由于混色效果由交替颜色的层构成，因此，具有以下特点的模型能呈现出最佳效果和最均匀的混色：

- 侧壁均近乎垂直的模型
- 斜面、悬垂及曲面顶面较少的模型

## 实用技巧

1. **深浅色占比**：耗材颜色的混合与调和颜料十分相似，一般情况下，深色往往会主导最终成色。因此，通常应调低深色耗材的混色占比，以便浅色仍能凸显视觉效果。
2. **CMYK 耗材**：只要巧妙地搭配耗材颜色，即可凭几卷耗材调配出几乎整个色谱的颜色。**拓竹 CMYK 耗材套装**即可实现这样的效果。

   - CMYK 耗材包括**青色、品红色、黄色和白色**的耗材。这四种颜色与普通纸质打印机中的墨盒颜色类似。
   - 如下方右图的所有小船均为使用拓竹 CMYK 耗材套装在单盘中打印。
   - 注意，若要呈现最鲜艳的颜色效果，仍建议使用本色耗材；但若追求灵活性和简化的配置，CMYK 耗材套装是理想的选择。
   - 购买链接：[**拓竹 CMYK 耗材套装**](https://detail.tmall.com/item.htm?abbucket=8&id=715351727644&rn=4757913396790a202d86e233290c7b70&spm=a1z10.5-b-s.w4011-25176969463.62.665d6f97fyI8Jr&skuId=5170951278326)

|  |  |
| --- | --- |
|  |  |
| CMYK 叠色实拍图 | CMYK 打印实例 |

3. **优先使用双色混合：** 双色混合相比于三色混合而言，能产生更纯净、更可控、更可预测的效果。因此，推荐优先使用双色混合。
4. **先打印测试色块：** 正式打印前，建议先使用设定好的混色设置打印一个小测试色块观察结果精调。
5. **减少冲刷废料：** 启用"冲刷到对象的填充"和"冲刷到对象的支撑"，将冲刷耗材用于打印填充部分和支撑部分。

## 相关阅读

- [减少多色打印时的材料浪费](../software/bambu-studio/reduce-wasting-during-filament-change.md)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
