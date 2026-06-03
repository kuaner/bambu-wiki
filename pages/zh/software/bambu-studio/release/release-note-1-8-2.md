---
path: zh/software/bambu-studio/release/release-note-1-8-2
title: "Bambu Studio 1.8.2 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-12-11T09:16:33.523Z
updated: 2024-05-28T11:06:06.977Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-8-2
---

# 新增功能

1. 支撑创建自定义耗材预设

在过去，Bambu Studio 仅提供了有限的第三方耗材预设，用户需要以“Generic XXX”为基准，新建自己需要的第三方耗材。同时，自定义的第三方材料在AMS 映射上使用会产生问题。现在，您可以直接在 Bambu Studio 中创建自己的自定义耗材。在这个版本中，Bambu Studio 提供了一种可以直接在 Bambu Studio 中创建自定义耗材的便捷的方式。

您可以在材料的引导页面找到自定义耗材的编辑入口，进行创建/删除自定义耗材或为现有耗材创建预设。详细的步骤说明可在我们的网站上找到。[Wiki](../../../../en/bambu-studio/create-filament.md).

![create_filament.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/create_filament.png)

此外，和系统耗材一样，自定义耗材丝可以在 X1 和 X1C 打印机AMS上选择并开始打印。这项功能将在固件更新到1.6.6版本及以上后可用。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/new-filament-printer.jpeg)

2. 支持创建自定义打印机预设

以前，当 Bambu Studio 不支持某些第三方打印机，或者用户希望通过更改打印机喷嘴来提高打印质量时，手动调整打印机配置文件是一件繁琐的事情。为了解决这个问题，我们实现了创建自定义打印机预设的功能，便于创建需要的打印机预设。自定义打印机预设被创建后将被归类于“用户预设”类别中。这项功能可以通过下方图片展示的入口进行使用。关于如何使用这一新功能的全面指导，请参阅我们的 [Wiki](../../../../en/software/bambu-studio/3rd-party-printer-profile.md).

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/create-printer-1.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/create-printer-2.png)

3. 支持导入导出打印机预设，材料预设和工艺预设。

您可以在线下使用此功能与他人分享您的预设文件，或是使用他人的预设文件。

左边的图片显示了导出功能入口。右边显示了导出功能的界面。详细的指导请查看 [Wiki](../../../../en/bambu-studio/export-filament.md) for details.

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/export-printer-1.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/export-filament-1.png)

现在，导入预设文件功能支持四种不同的文件类型，分别是 .json、.bbscfg、.bbsflmt 和 .zip。下方的动图简单展示了如何导入预设文件。

![import-setting.gif](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/import-setting.gif)

4. 支持 Bambu Lab A1

![support-a1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/support-a1.png)

5. 自动计算冲刷功能

在多色打印场景中，用户常忽略计算耗材冲刷量，或在更换耗材颜色时忘记重新计算冲刷，从而导致打印缺陷。为了解决这个问题，Bambu Studio 实现了自动计算冲刷量的功能。当您添加新的耗材或编辑耗材颜色时，冲洗量将会自动重新计算。下图展示了自动冲刷功能。

![auto-flush-calc.gif](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/auto-flush-calc.gif)

6. 修改P1P安装升级升级套件后的兼容性弹窗逻辑

考虑到不少用户购买并安装了 Bambu 的 P1P 到 P1S 的升级套件，为了提升此部分用户的打印体验，在这个版本中，如果安装了 P1P 到 P1S 的升级套件，在发送打印任务时，如果机器预设设置为 P1S，将不再弹出兼容性提醒弹框，如果机器预设设置为 P1P，则弹出兼容性提醒。这项功能将在 P1P 固件更新到 01.05.00.00 版本后可用（即将发布）。

7. 切换打印机时，自动重新摆盘到盘的中心

您可能总是因为在切换打印机配置文件时必须手动将零件排列到打印板上而感到烦恼，但是，Bambu Studio 解决了这个问题。当机型的预设文件更改后，对象会自动重新排列到对应的打印板上。

这个 GIF 展示了在以前的版本中切换机型的预设文件后造成的混乱情况。  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/auto-arrange-after-switch-printer.gif)

这个 GIF 展示了新版本的自动排列功能。  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/auto-arrange-after-switch-printer-2.gif)

8. 自动添加连接件功能

Bambu Studio 中的切割工具已经升级，提供了新功能，包括 Snap 连接器和燕尾榫切割，以及对现有平面切割能力的改进。这一增强包括部分从 PrusaSlicer 适配的代码，我们感谢 PrusaSlicer 和 [YuSanka](https://github.com/YuSanka), [enricoturri1966](https://github.com/enricoturri1966) 的贡献。  
Snap 连接器功能：  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/snap-connector-2.gif)

燕尾榫切割功能功能：  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/dovetail-cut.gif)

# 优化

1. 改进自动抬升算法以提高计算速度

使用来自 [davidkelly021](https://makerworld.com/zh/u/4200030776) 在 MakerWorld 中上传的模型 “aquatic dragon” 进行测试。这一改进将 Gcode 导出时间缩短了大约12秒。左边的图片展示了原始的时间消耗，右边展示了改进的结果。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/improve-auto-lift-detection-speed-1.gif)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/improve-auto-lift-detection-speed-2.gif)

2. 支持喷嘴与材质的兼容性检查

当打印任务被发送时，Bambu Studio 会检测喷嘴是否适合打印所用的耗材丝，检查项目如下：  
a. 检查预设喷嘴的直径是否与打印机喷嘴的直径相同。  
b. 检查打印机喷嘴的硬度是否适合用于打印的耗材丝。  
这个功能减少了喷嘴堵塞的风险，并通过防止过度磨损来确保喷嘴的使用寿命。  
注意：喷嘴的直径和硬度可以在打印机的屏幕上设置。  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/check-nozzles-filament.gif)

3. 支持机器内文件查看 P1P/P1S/A1 mini  
   <https://github.com/bambulab/BambuStudio/issues/2088>  
   <https://github.com/bambulab/BambuStudio/issues/2328> .

Bambu Studio 现在支持 P1/P1S/A1 mini 的文件浏览功能。请注意，这一功能依赖于打印机固件升级到新版本（P1P/P1S v1.5 及以上 和 A1 mini v1.2 及以上）。  
启用此功能后，您可以通 Studio 浏览和下载打印机上的延时视频文件，浏览打印机上的模型切片文件，并启动打印；当前，这些型号的打印机上的下载模型功能目前仍不支持。

4. 提升深色模型的预览可见度  
   <https://github.com/bambulab/BambuStudio/issues/2761>
5. 开发者模式中添加 "top area threshold" 参数, 在部分场景可以提升打印质量，感谢 [igiannakas](https://github.com/igiannakas) 的贡献

在开发者模式下，有一个新的参数叫做“顶层区域阈值”。这决定了顶层区域减小的程度，以决定是否应用“顶部只有一层墙”的设置。调整这个阈值会影响收缩参数。增加它可以增强模型的外观。例如，左边的球体显示了一些顶层只有单层循环，导致顶部表面不平。相比之下，右边的球体，由于顶层更少，呈现出更精致的形状。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/top-area-threshold-1.png)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/top-area-threshold-2.png)

6. 添加有机树类型支撑。 此功能来自PrusaSlicer。 感谢 PrusaSlicer。  
   <https://github.com/bambulab/BambuStudio/issues/797>  
   <https://github.com/bambulab/BambuStudio/issues/1785>  
   <https://github.com/bambulab/BambuStudio/issues/2420>
7. 改进不同的打印块之间的链接强度。

使用绘制工具后会产生不同的区块，您可能会担忧不同区块之间的连接强度。现在开放了可以启用绘制块与相邻部分的互锁的选项，通过交叉打印的方式改善了块之间的连接。这个功能源自 PrusaSlicer，感谢 PrusaSlicer 做出的贡献。  
请参考下图了解参数的位置。注意：此参数的值表示奇数层的嵌入深度，值为 0 时将停用此功能。  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/improve-multi-materials-connections.gif)

8. 支持通过名称在对象列表中搜索模型，快捷键是 Ctrl + F。  
   ![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/search-model-by-name.gif)
9. 自动打印板跟踪功能。

Studio 会记住上一次为不同打印机型号选择的打印板，减少用户忘记切换打印板造成的打印麻烦（不沾热床，过大的象脚等）。此功能默认启用，您可以在偏好设置中关闭它。如下方 gif 所示，例如，X1 机器的默认床型是冷床，但当您手动更改床型并从另一台机器切换回来时，X1 机器将选择你上次偏好的床型。  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/auto-bed-type-2.gif)

10. 添加“最佳对象位置”参数，允许用户定义放置模型的最佳位置。

该参数可以在打印机预设中修改，自动摆盘功能将会把模型放置在设定的位置。我们已经为 A1 mini 和 X1 系列设定了不同的最佳位置。  
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/add-best-object-location.png)

11. 添加一个名为"avoid interface filament for base"的选项，以阻止支撑面的耗材用于打印支撑底座。

这个参数可以在开发者模式下看到，此选择在选用了支撑主体材料时不生效。这避免了由于使用粘附力低的耗材来打印支撑体而导致的支撑塌陷倾倒问题。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/avoid-interfaces-filament-for-base.jpg)
![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/avoid-interfaces-filament-for-base-2.jpg)

12. 高度范围涂色工具中实现鼠标跟随设置，以及指定初始位置的功能。  
    ![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/mouse-following-layers-2.gif)
13. 为P1P机型的0.2 0.6 0.8喷嘴增加了更多预设
14. 在 speed 列表中添加了 "small perimeter" 参数。这个功能来自 PrusaSlicer 和 OrcaSlicer。感谢他们。

<https://github.com/bambulab/BambuStudio/issues/735>  
<https://github.com/bambulab/BambuStudio/issues/2221>

15. 允许通过自动摆盘将不同打印温度的多种耗材放置在同一个打印板上。

以前我们在自动摆盘时只能放置数量有限的不同类型耗材在同一个打印板上。逻辑是，如果两种耗材的打印温度相差太大，它们就不能放在同一个打印板上。例如，如果我们有一个 PLA 对象和一个 PETG 对象，它们就不会被自动排列在同一个打印板上，因为它们的打印温度相差超过 20 度。

这个限制现在已经放宽。耗材被分类为“低温”（如 PLA、TPU 等）、“高温”（如 ABS、PC 等）和“兼容温度”（如 PETG 等）。我们不允许将低温和高温耗材放在同一打印板上，这是唯一的限制。因此，PLA 和 PETG 现在可以放在一起了。

16. 更改撤销按钮的位置，以避免意外点击。

![change-revert-button-position.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_8_2/change-revert-button-position.png)

17. 添加 Bambu TPU 95A HF 耗材。
18. 在预览中添加擦料塔的重量估计。  
    <https://github.com/bambulab/BambuStudio/issues/1167>  
    <https://github.com/bambulab/BambuStudio/issues/2576>
19. 支持在对象列表内修改盘名称。
20. 支持设置熨烫角度。

熨烫角度是指填充方向与熨烫方向的相对角度。这个功能允许用户改变熨烫与填充方向之间的角度，以获得更平滑的熨烫效果。

21. 将每日提醒放在在切片的进度条上展示。
22. 在暗黑模式下的状态面板界面中增强暗色模型的可视性。
23. 修改克隆热键为 Ctrl + M。
24. 使用标准的 mine-type 来处理 3mf 文件，感谢 [Bastien Nocera](https://github.com/hadess) 的贡献。
25. 添加对 Creality 3D 打印机型号 K1 和 K1 Max 的支持。感谢 [izonex](https://github.com/iZonex) 的贡献。
26. 在导入 Gcode 文件时显示估计的打印成本。

# 修复

1. 修复了在逐渐打印时跳过换料的错误。  
   <https://github.com/bambulab/BambuStudio/issues/2776>
2. 修复了从磁盘加载 3mf 文件失败的问题。  
   <https://github.com/bambulab/BambuStudio/issues/2324>  
   <https://github.com/bambulab/BambuStudio/issues/2696>  
   <https://github.com/bambulab/BambuStudio/issues/2258>  
   <https://github.com/bambulab/BambuStudio/issues/2246>  
   <https://github.com/bambulab/BambuStudio/issues/2209>
3. 修复了应用启动时从云同步用户预设时偶尔发生的崩溃问题。  
   <https://github.com/bambulab/BambuStudio/issues/2850>
4. 修复了在 Mac 上打开开发者模式时发生的崩溃问题。
5. 修复了在明亮模式下透明材料显示不清晰的问题，以及在暗黑模式下透明材料选择不清晰的问题。
6. 修复了应用启动时从云同步用户预设时偶尔发生的崩溃问题。  
   <https://github.com/bambulab/BambuStudio/issues/2850>
7. 修复了在成功发送打印任务后，重定向到设备页面时，进度条显示为 100% 而不是 0% 的问题。
8. 修复了混合支撑可能出现的浮空支撑的问题。
9. 修复了树状支撑可能穿过对象的问题。
10. 修复了在使用 Arachne 墙壁生成器时，树状支撑的第一层可能过度挤出的问题。
11. 修复了可能出现的浮动树状支撑问题。
12. 修复了在某些语言中高度范围的“+”按钮不可见的问题。  
    <https://github.com/bambulab/BambuStudio/issues/2203>
13. 修复了使用自定义更换耗材 Gcode 进行切片可能导致崩溃的问题。
14. 修复了在切换暗黑模式或改变屏幕 DPI 时发生的崩溃问题。
15. 修复了在预览中，如果勾选了travel选项，则速度值预览颜色显示不正确的问题。  
    <https://github.com/bambulab/BambuStudio/issues/2513>
16. 修复了在 Linux 上在高度范围调节器上按下 Enter 键时发生的崩溃问题。  
    <https://github.com/bambulab/BambuStudio/issues/2481>
17. 修复了在使用“逐件打印”打开 A1 mini 预设文件时，信息显示错误的问题。  
    <https://github.com/bambulab/BambuStudio/issues/2803>
