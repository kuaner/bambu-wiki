---
path: zh/software/bambu-studio/release/release-note-2-8-2-60
title: "Bambu Studio 2.8.2.60 版本说明"
description: ""
tags: []
created: 2026-08-14T06:12:19.462Z
updated: 2026-08-14T12:57:08.577Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-8-2-60
---

> **已知问题：**
>
> 1. **macOS 27 Beta网络插件已可正常下载和使用云端连接，但用户无法连接局域网机器，这是因为当前配置在 macOS 27 下会触发权限问题。该问题正在处理中，将在后续版本中修复。**
> 2. **macOS 27发送打印弹窗中切换耗材丝映射后，概率性出现白色悬浮窗口，再次选择相同的槽位耗材可消除。**
> 3. **macOS 27 Beta 最大化BambuStudio窗口后无法退出全屏幕。可通过快捷键：Command (⌘) + Control (^) + F 退出。**

本次 Bambu Studio 更新带来了多项重要功能与体验优化，包括打印进度条暂停点展示、模型装配指南生成、颜色预测与拆色能力升级、设备页耗材管理增强、E3D 热端支持，以及多项切片与设备交互体验改进。

## 新功能

## 打印进度条支持展示暂停点信息

用户可以在打印进度条上直观看到当前打印任务中的暂停点信息，包括：本次打印任务包含的暂停点总数，已经触发的暂停点数量，即将触发的暂停点位置等。

将鼠标悬停在进度条上的暂停点标记时，还可以查看预计多久后会触发暂停，方便用户提前做好操作准备，例如嵌入零件、换色、放置磁铁等。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image.png)

注意：

1. 该功能依赖打印机固件支持，最低支持版本为 **01.02.50.00（H2S）**。各机型也将逐步通过固件更新支持该功能。
2. 打印进度条上最多展示即将触发的 **5 个暂停点**。随着打印进度推进，后续暂停点信息会逐步显示在进度条上。

> 另外前序beta版本的重点新功能也包含在此次public版本中。
>
> ### 支持直接在 Bambu Studio 内设计并生成模型装配指南
>
> Bambu Studio 现在支持在软件内创建模型装配指南。对于复杂装配模型，导入 STEP 文件后，软件可辅助拆分装配步骤，并通过可视化方式展示装配关系，帮助用户更轻松地理解模型结构与安装顺序。
>
> 主要功能包括：
>
> - 支持通过对象树编辑每个装配步骤中包含的对象或零件
> - 支持设置零件之间的相对位置
> - 支持记录每个装配步骤的起始帧与结束帧，并生成对应动画
> - 支持爆炸动画以及多种标签类型，包括卡扣、矩形、文字等
> - 支持一键生成装配演示动画，并可统一视角、自动布局
> - 支持一键导出 **PDF / Markdown / MP4** 格式的模型装配指南
>
> 具体内容可查看wiki: <https://e.bambulab.com/t?c=T0HuraoU2gH6ufRk>
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/zhg.gif)
>
> ### 颜色预测更新并支持拆色
>
> 本版本引入拆色功能。当用户导入带有颜色信息的模型或项目时，可以将任一颜色拆分为多种不同颜色叠加后的效果，并保存为新的颜色方案。同时，我们优化并更新了颜色预测算法。使用 **Bambu PLA Basic 的 CMYW、RYBW 耗材组合**时，可以获得更加精准的叠色预测效果。
>
> 具体包括：
>
> - 支持从耗材列表拆色，或拆分为特定颜色组合（目前仅支持Bambu PLA Basic的CMYW和RYBW组合）。
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-1.png)
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-2.png)
>
> - 支持纹理模型、OBJ文件导入时自动拆色：导入带颜色的模型后，软件会自动匹配耗材库并生成拆色方案，无需用户手动配色
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-3.png)
>
> ### 设备页耗材管理功能升级
>
> 设备页的耗材管理能力进一步增强，方便用户更高效地管理多卷耗材与设备槽位。
>
> 更新内容包括：
>
> - 支持将耗材管理器中的耗材直接绑定到可编辑槽位
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-4.png)
>
> - 支持查看耗材在位信息以及当前所在的打印机和AMS
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-5.png)
>
> - 当放入尚未录入的官方耗材时，可在设备页快速录入，或将其与已有耗材进行关联
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-6.png)
>
> ### 集成 E3D 热端支持
>
> 本版本新增对 **E3D High Flow 喷嘴类型** 的支持。支持机型包括：H2D，H2S，H2C（仅左喷头），X2D，P2S
>
> 注意：仅支持 0.4 / 0.6 mm 喷嘴直径
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-7.png)
>
> ### H2D 新增余料提醒
>
> Bambu Studio 现在可在发送打印流程中检查耗材余量是否充足，帮助用户降低因耗材不足导致打印中断的风险。
>
> ⚠️ 固件最低支持版本：01.03.50.00 (H2D)
>
> ![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-8.png)

## 改进

### 模型仅在较高位置换色时，可打印更矮的擦料塔以节省耗材

开启开发者模式后，可在 **其他 > 擦料塔** 中启用“无稀疏层”功能。

启用后，生成擦料塔时会跳过中间没有换料需求的层，仅在需要换料的高度附近生成擦料塔，从而减少擦料塔材料消耗。对于仅在模型较高位置发生换色的打印任务，该功能可以在一定程度上节省耗材。

注意：

1. 该功能仍属于实验性质，并且对擦料塔与模型之间的相对位置有一定要求，只有满足条件时才可正常使用。
2. 由于 Z 轴移动速度较慢，打印完较矮擦料塔后再移动到模型位置可能需要较长时间，存在漏料、拉丝等打印瑕疵风险。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-9.png)

### 耗材管理器显示耗材的备注信息

耗材管理器现可在耗材列表中显示 Note（备注）信息，便于区分多卷同类耗材。([#11354](https://github.com/bambulab/BambuStudio/issues/11354))

用户也可以在搜索窗口中通过备注信息搜索对应耗材。[PR #11505](https://github.com/bambulab/BambuStudio/pull/11505)。感谢 [@BenJule](https://github.com/BenJule)

![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-10.png)

### 优化树状支撑悬空问题

针对有机树状支撑，软件现在会对内部的悬空默认启用闪电填充补强，从而降低支撑悬空导致打印失败的风险。

### 右键菜单新增零件级别克隆功能

用户可以通过右键菜单直接对单个零件进行克隆，提升多零件模型复制和编辑效率。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-11.png)

### 优化 A2L 连接不同类型 AMS 时的打印时长预估

针对 A2L 机型，当连接不同类型 AMS 时，Bambu Studio 优化了与 AMS 换料相关的打印时长预估，使预计打印时间更加接近实际情况。

用户也可以根据自己的进料管长度和 AMS 类型，对进退料时间进行校准。

> ⚠️ 固件最低支持版本： 01.01.01.00 (A2L)

![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-12.png)

### A2L 机型展示首层保温区域，并对打印时长的影响进行说明

当打印较大平面且高度较低的首层模型时，为确保最佳打印质量，打印机会根据热床温度和模型的摆放位置自动调整预热与保温时间，以减少热形变并提升首层稳定性。目前此功能支持 **A2L** 打印机（需固件支持）。

Bambu Studio 现在支持可视化显示对应的首层保温区域。用户可以根据提示调整模型摆放位置，将打印件摆放于中心区域可减少保温时间。在首选项中可关闭相关区域提示。

> ⚠️ 固件最低支持版本：01.01.01.00 (A2L)

![](https://wiki.bambulab.com/bambu-studio/release-note-2-8-2/new/2.8%E5%8F%91%E5%B8%83%E8%AE%B0%E5%BD%95-image-13.png)

#### 其他改进：

1. 设备页实时摄像头画面支持鼠标滚轮缩放 [PR #11325](https://github.com/bambulab/BambuStudio/pull/11325)。感谢 [@BenJule](https://github.com/BenJule)。  
   注意：当前暂不支持画面平移，后续版本将继续优化。
2. 优化 PET-CF 的材料参数，改善在悬垂打印场景下的打印效果。
3. 更新 PVA 支撑 PLA 时的建议工艺参数，将支撑的底部Z距离设置为0提升支撑稳定性。
4. 当云服务异常或网络状况不稳定时，软件会自动尝试切换至 LAN 模式继续发送打印，提高设备互联稳定性。
5. 优化发送打印页面的耗材映射逻辑，减少切片耗材和打印机实际耗材类型映射不一致的情况。
6. 装配指南工具支持撤销与重做，提升装配指南编辑过程中的容错性与编辑效率。
7. 使用切割工具切割模型并生成燕尾榫结构时，模型原有涂色信息将被保留。
8. 当多个 AMS 槽位装有相同类型与颜色的耗材时，发起打印页面优先匹配余量少的耗材 [PR #11347](https://github.com/bambulab/BambuStudio/pull/11347)。感谢[@ojimpo](https://github.com/ojimpo) 。
9. 优化多头机器省料模式下的切片逻辑。当换料次数仅有一次时，切片引擎会尽量按照实际耗材左右分组，避免为了减少一次换料而导致用户需要在打印机端进行繁琐的耗材摆放。
10. 增强了 Helio 仿真功能的稳定性和工作流安全性，减少因网络不稳定导致的失败问题 [PR #11793](https://github.com/bambulab/BambuStudio/pull/11793) 。感谢[@HelioPri](https://github.com/HelioPri)。
11. 系统信息对话框“复制到剪贴板”支持更完整的信息，便于用户在反馈问题时提供更完整的软件与系统信息，提升问题诊断效率 [PR #11491](https://github.com/bambulab/BambuStudio/pull/11491)。感谢 [@BenJule](https://github.com/BenJule)。

## Bug修复

1. 修复了关闭应用时可能发生崩溃的问题。 ([#11482](https://github.com/bambulab/BambuStudio/issues/11482) )
2. 修复了盘上对象较多时切片耗时过长的问题。 ([#11255](https://github.com/bambulab/BambuStudio/issues/11255))
3. 修复了项目配置名称显示不正确或不显示的问题。 ([#10769](https://github.com/bambulab/BambuStudio/issues/10769))
4. 修复了自定义热床纹理加载后显示为黑色的问题。 ([#11314](https://github.com/bambulab/BambuStudio/issues/11314))
5. 修复了自动流量校准在特定情况下发生崩溃的问题。 ([#11416](https://github.com/bambulab/BambuStudio/issues/11416))
6. 修复了导入标准多色 3MF（各体积为单色）时切片颜色渗入相邻对象的问题。 ([#11348](https://github.com/bambulab/BambuStudio/issues/11348))
7. 修复了树状支撑根部悬空生成、未落到模型或热床的问题。 ([#11681](https://github.com/bambulab/BambuStudio/issues/11681))
8. 修复了树状支撑存在下方无法承托而悬空生成的区域的问题。 ([#11681](https://github.com/bambulab/BambuStudio/issues/11681))
9. 修复了在 Mac 上打开耗材管理器时偶发白屏的问题。 ([#11005](https://github.com/bambulab/BambuStudio/issues/11005))
10. 修复了压力提前（PA）设置始终显示为 Default 的问题。 ([#8196](https://github.com/bambulab/BambuStudio/issues/8196))
11. 修复了点击保存时偶发闪退导致文件未保存的问题。 ([#11715](https://github.com/bambulab/BambuStudio/issues/11715))
12. 修复了使用 Google/Gmail 账号登录下载模型时反复要求登录的问题。 ([#11095](https://github.com/bambulab/BambuStudio/issues/11095))
13. 修复了 MakerWorld 页面中图标与“在浏览器中打开”等外链无法跳转的问题。([#11579](https://github.com/bambulab/BambuStudio/issues/11579))
14. 修复了旧版或自建耗材预设在高流量等喷嘴下无法切片的问题。 ([#11589](https://github.com/bambulab/BambuStudio/issues/11589))
15. 修复了界面提示文案中的语法与格式错误。 ([PR #11257](https://github.com/bambulab/BambuStudio/pull/11257))
16. 修复了主挤出机对应的 AMS 耗材设置中无法显示已保存 PA 校准配置的问题。 ([PR #10850](https://github.com/bambulab/BambuStudio/pull/10850))
17. 修复了荷兰语界面中「空驶速度」翻译拼写错误的问题。 ([PR #11480](https://github.com/bambulab/BambuStudio/pull/11480))
18. 修复了英文界面中若干措辞与标点错误。 ([PR #10814](https://github.com/bambulab/BambuStudio/pull/10814))
19. 修复了 Linux ARM64 环境下因缺少 Node.js 依赖支持导致无法正常构建的问题。 ([PR #10712](https://github.com/bambulab/BambuStudio/pull/10712))
20. 修复了 SpaceMouse Wireless BT 设备名称缺失导致无法正确识别的问题。 ([PR #11755](https://github.com/bambulab/BambuStudio/pull/11755))
21. 修复了 Linux 单实例模式下通过第二实例打开文件无法传递到已运行实例的问题。 ([PR #11826](https://github.com/bambulab/BambuStudio/pull/11826))
