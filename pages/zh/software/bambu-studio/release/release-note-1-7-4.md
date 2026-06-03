---
path: zh/software/bambu-studio/release/release-note-1-7-4
title: "Bambu Studio 1.7.4 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-08-16T02:13:45.965Z
updated: 2024-05-28T10:53:15.154Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7-4
---

---

这是一个基于[1.7.3.50](release-note-1-7-3.md)的功能增强的版本，包括一些用户呼声较高的新功能和增强功能，并修复了一些老版本的Bug。

## 功能

1. 支持多色情况下的零件跳过功能

这个功能目前不是最优状态。当多色打印有部分零件打印失败时，此功能支持跳过失败的零件，保证其他零件顺利打印。但是冲刷和换料部分不能被跳过，即使相关的耗材已经不会被用于模型打印了。因为跳过换料冲刷会造成材料打印顺序改变，可能会影响后续材料的冲刷量，导致模型产生混色。后续的版本会持续对此功能进行优化，在跳过零件的同时跳过不必要的换料和冲刷，节省打印时间和冲刷消耗。

2. 支持用户定义首层材料的打印顺序

这是一个github上许多用户要求的痛点功能. [可以在这里找到相关内容](https://github.com/bambulab/BambuStudio/issues/1816). 十分感谢大家的建议! 下面的GIF展示了此功能如何使用。进行演示的[模型](https://www.printables.com/model/529455-lock-pick-card-kit/files)从 [Clem 3DVO](https://www.printables.com/@Clem3DVO_573880)的模型库中下载。感谢他的贡献。

![图片](https://wiki.bambulab.com/software/bambu-studio/1-7-4-version/define_filament_order.gif)

3. 支持用户在左侧的零件栏中定义模型内部相交部分的裁剪顺序和归属  
   这个功能原本由PrusaSlicer实现，我们在BambuSlicer中将其重新开放. 感谢 PrusaSlicer做出的贡献!  
   <https://github.com/bambulab/BambuStudio/issues/1896>  
   下图演示了如何使用此功能。  
   ![图片](https://wiki.bambulab.com/software/bambu-studio/1-7-4-version/define_clip_order.gif)

另外，使用此功能可以生成brim ear，在必要的点改善模型和打印板的粘结性。用户可以将小块的区域和主体模型组合成组合体，将其材料修改为支撑材料，从而获得使用支撑料打印brim的效果。  
下面的GIF展示了如何进行操作。进行演示的[模型](https://www.printables.com/model/63192-hydroponic-self-watering-seeds-starter-robert-plan)从 [Estudio Aditivo](https://www.printables.com/@EstudioAditivo)的模型库中下载。感谢他的贡献。

![图片](https://wiki.bambulab.com/software/bambu-studio/1-7-4-version/brim_ear.gif)

这是一个实验性的功能，存在一些已知缺陷，使用时建议将象脚参数设置为0mm。此功能后续版本也会进行优化。欢迎各位继续提出建议，我们会持续跟进！

4. 增加 Ellis' pattern 作为第三方新的压力提前标定图案  
   原始代码由 @thewildmage 加入OrcaSlicer中，并由社区友好用户在提给拓竹的相关[github issue](https://github.com/bambulab/BambuStudio/issues/2222)中建议引入。感谢@thewildmage的贡献和社区用户的积极建议!

![图片](https://wiki.bambulab.com/software/bambu-studio/1-7-4-version/new_pa_pattern.gif)

## 优化

1. 盘名长度增加到250个字符  
   <https://github.com/bambulab/BambuStudio/issues/2119>
2. 从 OrcaSlicer 的库中获取 Anycubic Kobra 2 的预设. 感谢 @Lee Colarelli 的贡献
3. 将第三方打印机的熨烫功能的默认值改为不熨烫. 感谢 @SoftFever 的贡献
4. 添加 Anker 的预设. 感谢 @just-trey 的贡献

## 修复

1. 修复 MacOS 系统上生成混乱的支撑面的问题  
   <https://github.com/bambulab/BambuStudio/issues/2115>
2. 修复部分语言下的登录窗口失败的问题  
   <https://github.com/bambulab/BambuStudio/issues/2240>,  
   <https://github.com/bambulab/BambuStudio/issues/2238>,  
   <https://github.com/bambulab/BambuStudio/issues/2237>,  
   <https://github.com/bambulab/BambuStudio/issues/2189>,  
   <https://github.com/bambulab/BambuStudio/issues/1995>,  
   <https://github.com/bambulab/BambuStudio/issues/1828>
3. 修复 Mesh Boolean 切片后结果不正确的问题  
   <https://github.com/bambulab/BambuStudio/issues/2263>
4. 修复没有 SD card 时候的崩溃问题  
   <https://github.com/bambulab/BambuStudio/issues/2206>
5. 从 OrcaSlicer 合并的修复支撑宽度为 0 的问题。感谢 @scottmudge 的贡献!
6. 修复回抽时关闭擦拭时的空驶路径混乱的问题  
   <https://github.com/bambulab/BambuStudio/issues/2256>
7. 修复小语种下自动流量标定返回 0,00 的问题  
   <https://github.com/bambulab/BambuStudio/issues/2141>
8. 修复 0.8 喷嘴下的流量标定图案间距过窄的问题  
   <https://github.com/bambulab/BambuStudio/issues/2296>
