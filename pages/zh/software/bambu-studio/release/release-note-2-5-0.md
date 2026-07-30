---
path: zh/software/bambu-studio/release/release-note-2-5-0
title: "Bambu Studio 2.5.0 版本说明"
description: ""
tags: []
created: 2026-01-27T09:41:11.808Z
updated: 2026-07-21T08:39:29.540Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-5-0
---

## 新功能

### 支持AMS远程烘干

现支持从Studio“设备”页面发起**H2D**连接的AMS 2 PRO与AMS HT的烘干操作。

- 点击对应AMS的“湿度”按钮，打开对应控制弹框。
- 弹窗中**启动**或**停止**烘干来控制烘干，同时支持**边烘边打**。

> ⚠️固件最低支持版本：**01.02.30.00**（H2D）。其他机型支持正在适配中，敬请期待。

|  |  |
| --- | --- |
|  |  |

### 支持支撑面熨烫功能

新增支撑接触面的熨烫能力。用户在不使用支撑料的场景下，可尝试通过该功能获得更理想的支撑表面质量。感谢[@Noisyfox](https://github.com/Noisyfox)的贡献。

|  |  |
| --- | --- |
|  |  |

### 顶/底面支持非100%填充pattern

支持顶部、底部表面使用非100%填充图案，带来更多外观与效果玩法。感谢[@Buildasaurus](https://github.com/Buildasaurus)的贡献。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/006.png)

#### 支持标准3MF的颜色解析

支持导入带颜色信息的标准3MF文件。导入后流程类似多色OBJ：选择需要映射的颜色信息后即可完成上色。

> ℹ️带颜色信息的标准3MF：目前Fusion360/Meshmixer/OpenSCAD等软件已支持，详情请参考各软件说明或https://3mf.io/相关标准。

> ⚠️注意：当前**仅支持面片着色与顶点着色**两种方式3MF的颜色信息导入；贴图着色的3MF导入时仅支持导入面片。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/048.jpg)

### 网格细分

右键零件选择“细分网格”，即可使用[Loop细分](https://libigl.github.io/libigl-python-bindings/tut-chapter6/#subdivision-surfaces)算法对该零件进行细分，并支持多次迭代计算。该功能适用于原始网格分辨率较低的模型。

> ⚠注意：
>
> 1. 该算法仅支持不含非流形边的网格；
> 2. 细分后颜色属性会丢失，建议先进行细分，再进行上色。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/002.gif)

### 打印件缩放到平台大小

新增“缩放到打印体积”功能。选中零件后右键选择该选项，可在保持各轴比例不变的前提下，将零件缩放至当前打印平台允许的最大尺寸。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/003.gif)

### 支持进/退料过程的停止功能

Studio现支持在进料/退料过程中执行“停止”操作。

> ⚠️当前支持机型：A1/A1 mini/P1P/P1S，其他机型将会在后续版本中支持。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/042.png)

### 二维晶格填充

新增二维晶格填充类型，适用于机翼等减重结构场景，并提供两个角度参数用于调整填充方向。感谢[@LoftedAero](https://github.com/LoftedAero)的贡献。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/043.png)

### 一致表面与短比行程加速度（实验）

针对常见的VFA问题，引入两种方式降低振纹效应，以下功能均只在开发者模式中可见：

1. **一致表面功能**：启用后，速度计算会优先降低填充等区域速度，仅在必要时才降低外墙打印速度，有助于提升外观一致性，尤其适用于亮光或丝绸材料。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/044.png)

|  |  |
| --- | --- |
|  |  |

2. **短比行程加速度**：调整该参数来使外墙短距离移动将采用更柔和、更低的加速度，有助于减少短行程加减速带来的振纹影响。目前短比形成加速度为全局参数，默认值设置为250mm/s²。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/009.png)

感谢[@lorenzofanchi](https://github.com/lorenzofanchi)和PrusaSlicer的贡献。

> ⚠️注意：相关选项当前仅在开发者模式下开放。

## 改进

1. **H2D左挤出头支持TPU打印**。

> ⚠️注意：
>
> - 固件最低支持版本： 01.02.30.00（H2D）
> - 左挤出头目前仅支持**硬度等级≥90A的TPU耗材**

2. 新增**钨钢喷嘴**，支持H2D/H2S/H2C/P2S。

> ⚠️固件最低支持版本：01.01.01.00（P2S）、 01.02.30.00（H2D）、01.01.30.00（H2S）、01.01.00.00（H2C）

3. 新增**TPU高流量喷嘴**（即将推出）支持。增加工艺参数“顶部表面流量比例”的左右挤出头参数拆分。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/010.png)

> ⚠️注意：
>
> - 固件最低支持版本： 01.02.30.00（H2D）
> - 修改过“顶部表面流量比例”的旧版本双挤出机3mf导入时，修改值仅被迁移至左挤出头，右挤出头参数需要重新设置。

4. **发送打印界面映射交互优化**：为避免多挤出机在部分场景下出现映射歧义，发送打印时将展示多挤出机的全部AMS信息，映射逻辑更清晰。更多映射规则请参考[Bambu Wiki](../filament-mapping-principle.md)。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/011.png)

5. \*\*发送打印时硬度判断逻辑优化：\*\*当耗材硬度超过喷嘴硬度时，不再直接阻塞打印，并增加明确提示。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/012.png)

6. 自动摆盘效果优化。

|  |  |
| --- | --- |
| 改进前 | 改进后 |

7. 新增快捷键**Ctrl+L**用于切换悬垂显示。
8. 内嵌MakerWorld、MakerLab页面中增加“**后退**”、”**刷新**”以及“**在浏览器中打开**”按键。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/022.png)

9. 存储介质的延时摄影、模型页面增加“全选”按钮，用以支持便捷批量删除。

![](https://wiki.bambulab.com//software/bambu-studio/release-note-2-5-0/021.png)

10. 无U盘场景下支持启用延时摄影模块功能。
11. 耗材预设默认显示顺序优化。
12. X1/P1/A1工程材料板预览图更新。
13. 剩余打印时间文案优化。

### Bug修复

1. 修复X1E不支持高流量喷嘴的问题。([#8992](https://github.com/bambulab/BambuStudio/issues/8992))
2. 修复使用ASA-Aero/PLA-Aero/TPU线材时，H2D错误显示E3D高流量喷嘴警告的问题。([#9010](https://github.com/bambulab/BambuStudio/issues/9010))
3. 修复H2C右侧喷嘴校准在部分语言下不可用的问题（[#9121](https://github.com/bambulab/BambuStudio/issues/9121)）
4. 修复P2S设备PETG冷却模式的UI提示错误（[#9131](https://github.com/bambulab/BambuStudio/issues/9131)）。
5. 修复鼠标遮挡部分UI提示的问题（[#8872](https://github.com/bambulab/BambuStudio/issues/8872)）
6. 允许在切割功能中使用更细的连接器尺寸。（[#8669](https://github.com/bambulab/BambuStudio/issues/8669)）
7. 修复了MacOS部分构建错误，感谢[@johanohly](https://github.com/johanohly)的贡献。
8. 修复Ubuntu25无法构建的问题，感谢[@dblueman](https://github.com/dblueman)的贡献。
9. 修复精准外墙功能在非“内/外”填充顺序下的异常，感谢[@michaelr0](https://github.com/michaelr0)的贡献。
10. 修复MacOS在LAN模式下新增机器失败的问题，感谢[@raulp](https://github.com/raulp)的贡献。
11. 修复MacOS部分场景下滚动回弹的问题，感谢[@eldade](https://github.com/eldade)的贡献。
12. 修复了Github仓库中的部分拼写错误，感谢[@reedy](https://github.com/reedy)。
13. 修复了部分场景下切片错误的问题。（[#9043](https://github.com/bambulab/BambuStudio/issues/9043)）
14. 修复了部分拼写错误。（[#9201](https://github.com/bambulab/BambuStudio/issues/9201)）
15. 修复了Helio优化的加载错误，感谢[@vipulrajan](https://github.com/vipulrajan)的贡献。
16. 更新部分翻译内容，感谢[@jli](https://github.com/jli)的贡献。
17. 修复了Linux上打开文件夹的错误，感谢[@fcrozat](https://github.com/fcrozat)的贡献。
18. 感谢[@jomixlaf](https://github.com/jomixlaf)的多项贡献，包含:

- 对象列表中单盘选项新增右键“全部展开/折叠”按钮；
- 优化下拉菜单多选逻辑；
- 新增多选“Reload from disk”；
- 将“0”按键设为10号耗材设置快捷键。

19. 修复MacOS构建包copyright年份错误，感谢[@JohnSmithCYM](https://github.com/JohnSmithCYM)的贡献。([#8849](https://github.com/bambulab/BambuStudio/issues/8849))
20. 修复Linux平台视频无法播放的问题。感谢[@hadess](https://github.com/hadess) 的贡献。
21. 修复更多拼写错误，感谢[@luzpaz](https://github.com/luzpaz)的贡献。
22. 修复了Linux平台构建错误，感谢[@3vi1](https://github.com/3vi1)的贡献。
23. 更新KSR内置模型并修复其标注错误，感谢[@luis88luis](https://github.com/luis88luis)和[@JohnSmithCYM](https://github.com/JohnSmithCYM)的贡献。
