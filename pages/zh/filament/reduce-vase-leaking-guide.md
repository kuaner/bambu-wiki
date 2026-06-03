---
path: zh/filament/reduce-vase-leaking-guide
title: "降低打印件漏液风险的指南"
description: ""
tags: ["花瓶"]
created: 2024-01-10T03:11:50.894Z
updated: 2026-05-12T06:39:02.487Z
source: https://wiki.bambulab.com/zh/filament/reduce-vase-leaking-guide
---

# 目的

**本文指导在打印花瓶等盛装液体的模型时，如何尽可能地降低它们的漏液风险。**

# 注意事项和打印参数技巧：

- **打印前先把耗材烘干：**以避免水汽使得挤出线条中产生孔洞而降低模型质量。
- **提高流量比例：**材料在经过 “熔融—凝固” 后会出现体积差异，提高挤出流量比例能使挤出的线条更饱满，可减少或避免缝隙的产生。
- **适当调大线宽、调小层高：**较大的线宽可以最大限度地减小打印线条之间的间隙，而较小的层高可以让打印线条粘接得更紧密。
- 修改底部图案为 “同心”：“同心” 图案可以更好地填满线材在填充小区域时产生的缝隙。
- **调大墙层数和（或）调高填充密度：**较大的墙层数和（或）较高的填充密度能使打印件的壁厚较大、空隙较少，从而使液体更难渗透、泄露。

文末提供了包含推荐参数的 3mf 文件。

\*请注意：这些打印参数技巧只能降低漏液风险，不能保证所有的模型都不会漏液，且打印件实际的抵抗液体能力、漏液风险还和所用材料的性质和打印件的尺寸、结构等有关。因此，不推荐用常规打印件来盛放有腐蚀性或有毒性的酸、碱、盐溶液和有机溶剂等可能导致潜在危险的液体。

# 切片参数设置（图片示例为 0.4 mm 喷嘴与 PLA Basic  耗材的参数）

**1. 适当提高流量比例。**

         建议提高量为 0.02 - 0.05，例如把 PLA Basic 的从 0.98 提高到 1.00 - 1.03 之间。注意，请勿使用过高的流量比例，否则可能会导致模型出现表面粗糙、拉丝、漏料等问题。

![](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/01-提高流量比例.png)

**2. 适当调大线宽、调小层高。**

参考设置如下图：

![](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/02-调大线宽和调小层高.png)

**3. 修改底部图案为同心。**

![](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/03-修改底部图案.png)

**4. 调大墙层数和（或）调高填充密度**

        可根据模型自身特点和使用需求来适当调大墙层数和（或）调高填充密度。建议的设置为：墙层数在  2 - 4 之间，填充密度在 0 % - 40 % 之间。墙层数越大、填充密度越高，则打印件抵抗漏液的能力越强，但同时，打印时间越长、耗材用量越大，请根据实际需求来设置。

![](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/04-墙层数和填充密度.png)

# 打印模型展示

模型盛水放置 48 小时后的效果如下图所示：

|  |  |
| --- | --- |
|  |  |

盛水的花瓶下方的纸巾仍然是干的，说明该花瓶抵抗水渗漏的能力足够强。

注：为便于判断，模型内盛放了用黑色墨水染色过的水。

# 预设配置文件

我们在这里也提供一些预设配置文件，您可以根据所使用的料线来下载对应的预设配置文件：

[bambu\_pla\_basic\_-\_vase\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/bambu_pla_basic_-_vase_-_0.4_mm_nozzle.3mf)

[bambu\_pla\_silk\_-\_vase\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/bambu_pla_silk_-_vase_-_0.4_mm_nozzle.3mf)

[generic\_pla\_-\_vase\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/generic_pla_-_vase_-_0.4_mm_nozzle.3mf)

[bambu\_petg\_basic\_-\_vase\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/bambu_petg_basic_-_vase_-_0.4_mm_nozzle.3mf)

## 如何导入预设配置文件？

您可以将下载的配置文件（上述3mf 文件） **“导入”** 到Bambu Studio中，当导入之后即可得到该预设配置参数。

![](https://wiki.bambulab.com/filament-acc/filament/reduce-vase-leaking-guide/07-导入预设.png)

注：这套参数不一定适配所有模型，请您根据实际情况适当调整部分参数；用其他型号的打印机打印时，可 **“迁移”**下述 X1C 的相应的工艺参数和耗材丝参数。

原模型链接：<https://makerworld.com/zh/models/41840#profileId-50731>
