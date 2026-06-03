---
path: zh/software/bambu-studio/release/release-note-1-9-1
title: "Bambu Studio 1.9.1 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-05-13T01:38:00.422Z
updated: 2024-06-04T06:45:15.631Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-9-1
---

## 新功能

### **1. 支持多设备管理**

我们在最新版本中引入了一项新功能：设备列表云打印。通过这项功能，你可以同时向设备列表中的所有设备发送云打印命令。该功能让跨多设备管理和控制打印任务更加方便高效。

关键功能：

1.可选择使用外挂料盘或 AMS 自动供料系统发起打印。如果选择使用 AMS，请注意目前软件仅支持简单的映射功能。

2.可自定义的发送设置：不同用户在发送打印命令时可能有不同的要求。因此，新版 Studio 提供了自定义最大发送间隔和数量的功能，你可以根据特定需求和工作负载来配置这些设置。

在发送窗口编辑打印参数

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/multi-dev_1.png)

在多设备选项卡上查看任务详细信息

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/multi-dev_2.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/multi-dev_3.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/multi-dev_4.png)

欲了解关于此功能的详细信息，请点击跳转【多设备管理】Wiki页面：

<https://wiki.bambulab.com/zh/software/bambu-studio/multi-device-management>

### **2. 支持导入带颜色信息的 OBJ 文件**

新增从 .obj 文件的 Vertex 颜色中导入颜色，以及从 mtl 文件导入颜色的功能。用户可以使用 Blender 或 Meshlab 等软件为模型的顶点或面着色。PNG 颜色相关功能目前正在开发中。请持续关注。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/支持导入带颜色信息的_obj_文件.webp)

注意：

请确保导入的 OBJ 文件没有非流形边，以保障正确切片。

颜色解析后，可能无法完全对应渲染软件内效果。用户可以继续在 Bambu Studio 中手动调整打印的颜色。

### **3. 支持在首层以上自定义打印顺序**

欲了解详情，请访问[相关Wiki](../parameter/filament-sequence-for-different-layers.md)

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/printsequence.png)

### **4. 优化了斜拼接缝（Scarf Seam）**

斜拼接缝是帮助棱角较少的模型隐藏接缝的实用技术，这时接缝处不再像一个“点”，而会变成短斜坡状。

斜拼接缝最早由 [Noisyfox](https://github.com/Noisyfox) 在 OcarSlicer 和其他社区贡献者参与和讨论，真挚感谢他们的巨大贡献。我们在 Bambu Studio 中引入并优化了斜拼接缝。

利用社区贡献，Bambu Studio 尽力在不改变参数的情况下，改善接缝质量。这种方法旨在不调整线宽或降低打印速度的情况下，实现增强版的接缝效果：

![](https://wiki.bambulab.com/20240514-092123.jpg)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/scarfseam_2.png)

此外，Bambu Studio 为斜拼接缝增加了悬垂检测条件判定。启用后，如果悬垂角度超过某个阈值，则无法使用斜拼接缝。这解决了斜拼接缝在过大悬垂角度的情况下效果变差或失效的问题。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/scarfseam_3.png)

请注意：该条件检测为实验功能，默认情况下处于关闭状态，请斟酌后再行使用。功能开关入口如下图所示。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/scarfseam_4.png)

### **5. 通过耗材回抽降低冲刷量**

在开发者模式下的实验功能，目前仅适用于 X1 和 P1 系列，默认情况下禁用该功能。此功能可在换料过程中延长耗材的回抽和切割距离，以降低冲刷。

虽然它可以显著减少冲刷，但有一定增加喷嘴堵塞或其他打印并发症的风险，请谨慎使用。感谢[**LeonFisherSkipper**](https://github.com/LeonFisherSkipper)

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/long_retraction.gif)

### **6. 优化 PA 校准（动态流量校准）图案**

改进 PA 校准（动态流量校准）图案。现在，所有打印的校准线都连接着同一个底板，以便于拆卸模型。感谢[OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/pa_calibration.png)

### 7.**支持手动校准值管理**

根据用户反馈，Bambu Studio 加入了校准值管理功能，允许用户直接在打印机上输入并保存特定校准值。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/manual_calibration.png)

### **8. 新增直线绘制和视图增强**

引入了在涂色中绘制垂直或水平直线的工具，以及由 OrcaSlicer 提供的默认前视图和水平旋转功能。感谢[OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/straight_line_painting.gif)

### **9. 整合并优化测量工具**

“测量”功能最初由 PrusaSlicer 团队创建，受到众多用户的喜爱，现已适用于 Bambu Studio，感谢 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) 和 [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer)。

Bambu Studio 在此基础上引入了能够跨多个模型对象进行测量的修改，提升了功能。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/measure_tool_2.gif)

此外，Bambu Studio 新支持了设置不同网格之间的距离，支持类似于 CAD 的装配功能，便于基于距离的精确装配。

### 10. **支持在每个打印盘上开启旋转花瓶模式**

<https://github.com/bambulab/BambuStudio/issues/2079>  
在“盘参数设置”选项卡下添加了“旋转花瓶”模式选项，现在必须在旋转花瓶模式下打印的模型、飞机零件等，只要与普通零件位于不同盘中，即可一起切片。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/spiral_vase_per_plate.png)

### 11**.** 增加“支撑/对象首层间隙”选项

过去，首层支撑与物体之间的距离由 Brim 间隙决定，在某些情况下，这种设置可能会让拆支撑变得更难。现在，这个间隙可以独立调整，默认值为 0.2 mm，在纹理 PEI 打印板上通常表现优异。但对于其他类型的打印板，可能需要重新调整。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/support_first_layer_gap.png)

### 12. **新的交叉层叠填充图案**

我们开发了一种新的填充图案，称为“交叉层叠”。顾名思义，它主要用线填充零件，同时通过一些过渡层定期更改线的方向。与线性和同心填充相比，它显著提高了强度，同时在大多数层中实现了高速和无声打印。

与螺旋体填充相比，它在测试立方体中的打印速度快28%。与网格填充相比，在相同的密度设置下，它的网格尺寸较小。根据我们的测试，我们建议打印时使用比正常情况下稍低的密度设置，例如12%。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/crosshatch.png)

## 优化

### 1. 优化尖尾支撑

尖尾结构是指像动物尾巴或人类头发一样悬空在外的一种特殊类型的悬垂结构。以前，我们使用非常紧密和密集的树形支撑结构来支撑尖尾，这种支撑结构很难移除。现在我们改进了支撑结构，大大提高了支撑效果并简化了尖尾拆除的难度。我们仅在尖尾周围添加了稀疏的接触节点，并将树形分支分开得足够远，以便于拆除。此外，尖尾悬垂结构将不再有支撑界面层。更多详情请查看Wiki [支撑耗材与支撑功能的介绍](../support.md)。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/sharptail_1.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/sharptail_2.png)

### 2. 平滑过渡悬垂调速

  此更新增强了悬垂调速，使速度之间更加平滑过渡，从而改善了速度过渡缺陷的外观。这项改进可在经典模式下使用。下图展示了平滑过渡悬垂调速的效果（关闭了冷却功能以展示悬垂速度过渡）。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothoverhang_1.png)

  A. 悬垂调速过渡肉眼可见得到了显著提升，衔接处更加完美。测试模型来自<https://makerworld.com/zh/models/12888#profileId-13005>

如左侧图片所示，速度变化明显区域存在过渡 (红色箭头)，而路径变化剧烈的区域则没有过渡 (黄色箭头)。右侧图片展示的打印结果则证明了表面质量的提升。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothoverhang_2.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothoverhang_3.jpg)

  B. 此外，圆弧拟合结果得以保留。无论速度过渡部分还是非速度过渡部分，都能保持弧线拟合。左下角的图像显示了速度过渡部分的圆弧拟合，右下角的图像显示了非速度过渡部分的圆弧拟合。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothoverhang_4.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothoverhang_5.png)

### 3. 改善飞线问题

得益于改进的悬垂计算方法，因悬垂计算引起的飞线问题得到了改善。左下角的图像展示了改进之前的情况，而右下角的图像展示了改进之后的情况。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/flywall_1.png)
![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/flywall_2.png)

### 4. 全面改进的错误提示系统

  我们升级了错误代码提示信息，并添加了相应的插图，让用户更容易理解错误代码。 这样一来，用户就能更方便地定位和识别遇到的问题。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/popup_1.png)

### 5.在每个模型调节工具上新增简单易懂的提示，给用户贴心的讲解

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/在每个模型调节工具上新增简单易懂的提示.webp)

### 6. 新增多盘统计功能，可查看多盘总时间和总耗材消耗 by [niklasb22](https://github.com/niklasb22).

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/niklasb22.png)

### 7.新增层信息在右侧的进度尺 by [@Noisyfox](https://github.com/Noisyfox)

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/noisyfox.png)

### 8. 新增远程文件批量管理

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/新增远程文件批量管理.png)

### 9. 优化了参数页面切换的性能，减少了切换时的延迟

### 10. 优化了实时预览和文件浏览

### 11. 单窗口模式，开启后仅允许单个Bambu Studio窗口同时运行

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/单窗口模式.png)

### 12.优化了AMS湿度计的图标

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/humidity_new_ui.png)

### 13.为HMS信息增加红点提示

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/hmsnotification.png)

### 14.为MakerWorld模型下载增加安全检测 我们实行了额外的安全检查措施，例如文件类型验证和下载服务器检测。这些措施旨在防止用户被虚假的 MakerWorld 网站欺骗，从而意外下载病毒或木马程序。

### 15. 启动 SD 卡中的模型文件进行打印时，会执行打印机与切片文件的兼容性检查。这有助于避免潜在问题，并确保打印操作顺利进行。<https://github.com/bambulab/BambuStudio/issues/2991>

### 16. 用户可在打印暂停时方便地进行外置料盘耗材的换料

### 17. 增加葡萄牙语界面

### 18. 给冲刷量系数增加了0-3的限制范围

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/18._给冲刷量系数增加了0-3的限制范围.png)

### 19. 切片预览中可分别查看每种走线类型的耗材消耗情况

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/filamentconsumption.png)

### 20. 针对模型对象复制操作，优化了内存使用效率和运行速度。

### 21. 对包含大量模型的 3MF 文件，优化了加载速度。

### 22. Bambu Studio 进行了更新，以确保敏感信息（例如 print\_host 和 apikey）不再包含在 Gcode文件中。

### 23. 优化了换料顺序生成速度，并扩展了支持范围，可调整超过 8 种颜色的换料操作。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/materialchangelogic.png)

### 24. 在主页的最近打开项目目录中，增加批量管理功能

### 25. 支持在预设中添加注解

### 26. 为工艺选项增加了介绍信息

### 27. 增加了对OLTP格式文件的支持

### 28.增加对10以上的耗材槽位的快捷键，可使用1+其他数字的形式操作

### 29. 对00.00.07.89以上版本的AMS，重新装料自动重新读取耗材信息，优化信息刷新。

### 30. 可在配置中输入"skip\_3dmouse\_detect": true 来屏蔽让系统运行速度变慢的USB设备。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/skip3dmouse.jpg)

### 31. 切片前添加处理脚本的绝对路径，如下图所示。 切片完成后，可以自动处理该脚本。 注意：由于脚本在切片过程中已调用过，因此导出 G 代码时将不再调用该脚本。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/切片前添加处理脚本的绝对路径.jpg)

### 32. 更新了参数继承的提示文案<https://github.com/bambulab/BambuStudio/issues/3236>

|  |  |
| --- | --- |
|  |  |

### 33. 优化了对日文的支持

### 34. 可直接在 Bambu Studio 端设置自定义耗材，无需再在打印机端操作。<https://wiki.bambulab.com/zh/bambu-studio/create-filament>

### 35. 精准 Z 高度

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/precisez1.png)

如启用，切片后的模型将获得确的 Z 向高度。

例如，切片一个 12.3mm × 12.3mm × 12.3 mm 的正方形，层高为 0.2mm。最终切片结果将是 0.2mm 的倍数（如第一张照片所示，切片后的高度将为12.4mm）。启用此项后，切片将调整最后 5 层的层高度，使切片结果的高度与对象的实际高度一致。（如第二张图片所示，切片后的高度为12.3mm，与物体的实际高度一致）

**注意：**当对象层数小于 6 层时，此项无效。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/precisez2.png)

精准Z高度未启用

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/precisez3.png)

精准Z高度启用

### 36. 多材料图形分区改进

我们提取了 Arachne 中关于公共位置 Voronoi 图检测的部分，并将其应用于多色区域分割。并重新实现了多素材分割的主要部分，解决了素材分割溢出层的所有问题。这个补丁是从 Prusa 采集的，感谢[PrusaSlicer](https://github.com/prusa3d/PrusaSlicer)。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/colorsegment1.png)

Version 1.8 或更早

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/colorsegment2.png)

Version 1.9 bera2

### 37. 更加重要的是，我们在装配图中新增了翻译、旋转和测量工具，并在测量工具中添加了面与面装配功能，方便您快速地将两个物体进行装配。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/assembly.png)

### 38. 基于由  [@gringer (David Eccles)](https://github.com/gringer)最初为 Slic3r 开发的创新型 3DHoneyComb 蜂巢填充 ，我们对其进行了改进并引入到了 Bambu Studio 中。 同时，我们还实现了填充角度选项，使您可以针对这种蜂巢填充类型微调填充角度。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/3dhoneycomb.png)

### 39. 从 PrusaSlicer 导入全新的 "保证垂直厚度" 算法。感谢 [Vojtech Bubnik](https://github.com/bubnikv) <[bubnikv@gmail.com](mailto:bubnikv@gmail.com)>

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/从_prusaslicer_导入全新的_old.png)

old

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/从_prusaslicer_导入全新的_new.png)

new

### 40. 更新新的官方耗材列表与对应参数

### 41. 加入土耳其语支持，感谢 [Fatih AYDIN](https://github.com/fatih5228) 的翻译

### 42.改进乌克兰语言支持 @<https://github.com/iZonex>

### 43. 增加支撑用耗材切片统计

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/supportfilamentuse.png)

### 44. 重新编写旋转花瓶功能，在旋转花瓶下增加平滑旋转的选项[andrewboktor](https://github.com/andrewboktor)

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothvase1.png)

一些花瓶模型在打印过程中会出现瑕疵，如图所示。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothvase2.jpg)

平滑旋转可以改善这些瑕疵

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/smoothvase3.jpg)

**注意:** 该改进只适用于圆滑外观的花瓶，有棱角的形状不适用。

### 45. 在更换耗材下拉菜单中显示耗材名称 by @<https://github.com/javawizard>

### 46. 我们正在积极优化软件，解决因页面错误增加导致的性能下降问题。这只是其中的一部分改进，我们未来也将持续关注此问题。<https://github.com/bambulab/BambuStudio/issues/3702>

### 47. 增加PIN码绑定模式，可绑定不在一个局域网内的打印机

  P series 引入 version 01.06

  A1 mini 引入 version 01.03

  A1 引入 version 01.03

  X series 目前还未支持(计划8月份新版固件支持)

更多信息可查看 WIKI <https://wiki.bambulab.com/zh/bambu-studio/manual/pin-code>

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/bindpin.png)

### 48. P 系列和 A 系列打印机现在可以像 X 系列打印机一样，将校准结果保存到打印机本身。校准结果可以在 Studio 的“结果管理”中进行编辑，并且可以在设备页面的 AMS 插槽中设置校准后的 k 值。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/manageresult.png)

### 49. 引入更多字体，这个改进是受PrusaSlicer启发，感谢Filip Sykala<[filip.sykala@prusa3d.cz](mailto:filip.sykala@prusa3d.cz)>!

### 50. 新加入了用于装配对象关系的装配工具。目前，已经实现了面对面装配和点对点装配功能。

![](https://wiki.bambulab.com/studio_releasenote/studio_1-9/新加入了用于装配对象关系的装配工具.png)

### 51. 多语言优化，俄语 by @<https://github.com/AndylgTom> , 土耳其语 by <https://github.com/fatih5228>, 韩语 by @<https://github.com/bluesoul33>

### 52. 为A1系列打印机增加局部调平功能

在发送打印任务前勾选“热床调平”，打印机将根据切片模型的外轮廓进行局部调平，而不是整个构建板区域进行热床调平，减少打印前的准备时间。

### 53. 为了改善的材料的冷却，增加了ASA材料的层时间参数，打印的时间将会增加。

|  |  |
| --- | --- |
|  |  |

## **修复问题**

- 修复了 Linux 编译问题 (由 @lucianoloder 贡献, [链接](https://github.com/bambulab/BambuStudio/issues/3874))
- 修复了无法编辑文本的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3750))
- 修复了切片器创建无效颜色模式的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3749))
- 修复了 flathub 构建问题 (由 @hadess 贡献)
- 修改了 macOS 快捷键组合键的键位描述 ([链接](https://github.com/bambulab/BambuStudio/issues/3026))
- 修复了下载包含图像的打印物评分时窗口标题拼写错误 ("Upload Pictrues" 改为 "Upload Pictures") ([链接](https://github.com/bambulab/BambuStudio/issues/3617))
- 修复了 AMS 插槽中的相同颜色无法匹配彩色耗材的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/2190)) ([链接](https://github.com/bambulab/BambuStudio/issues/3570))
- 修复了保存/导出 gcode 文件时强制使用 .gcode.3mf 文件扩展名的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3375))
- 修复了 AMS 中自定义耗材恢复为问号的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3087))
- 修复了缩放指示器箭头方向错误的问题
- 修复了编辑文本时文本工具中文本不可见的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3258))
- 修复了彩色涂色禁用 Shift 键多选对象的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3480))
- 修复了黑色纹理显示问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3484))
- 修复了切片错误 ([链接](https://github.com/bambulab/BambuStudio/issues/3601)) ([链接](https://github.com/bambulab/BambuStudio/issues/3554))
- 禁用“距离太近”警告 ([链接](https://github.com/bambulab/BambuStudio/issues/3647))
- 修复了多色切片出现颜色溢出的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/3681))
- 修复了“添加部件”未正确对齐父对象的问题 ([链接](https://github.com/bambulab/BambuStudio/issues/980))
- 修复了多色打印中出现意外层的问题

## 已知问题

1. 更新Bambu Studio后，在一些 MacOS 电脑上打开时可能导致软件崩溃 ([#4050](https://github.com/bambulab/BambuStudio/issues/4050))  
   发生的原因是以下目录中的一些旧的配置文件导致了冲突 `$HOME/Library/Application\ Support/BambuStudio/ota`  
   请删除这个目录，并尝试重新启动Bambu Studio。
