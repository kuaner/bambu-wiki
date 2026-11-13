---
path: zh/software/bambu-studio/release/release-note-2-9-1
title: "Bambu Studio 2.9.1 版本说明"
description: ""
tags: []
created: 2026-11-03T03:26:05.070Z
updated: 2026-11-10T13:07:48.193Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-9-1
---

本次 Bambu Studio 版本更新适配拓竹 H 系列新品拓竹H3C 多头打印机，同时带来多项重要功能与体验优化，并修复了若干稳定性与安全问题。

## 新功能

### 支持混合口径喷嘴切片打印

这是本次 Bambu Studio 版本发布中最重要的更新。

多口径混合打印不是一个新话题，过去，用户可以按墙、填充、支撑等切片走线类型分配耗材和喷嘴，例如，在 “工艺-强度-高级” 页面设置稀疏填充、实心填充、墙的耗材。本次更新的不同点在于，Bambu Studio 将多口径混合打印推进到模型区域：在同一模型中，用户可以为局部细节和模型主体指定不同口径的喷嘴，并**让不同口径喷嘴采用各自合适的层高打印**。

这意味着，即使位于模型**相同的高度范围内，小口径喷嘴不必为了迁就主体而加厚层高，大口径喷嘴也不必为了局部细节始终使用薄层**。小喷嘴可以用较窄线宽、较薄层高还原文字和刻度；大喷嘴则以较宽线宽、较厚层高打印主体。细节留给需要细节的区域，效率留给适合快速打印的区域。

得益于这项能力，以使用拓竹H3C 打印的 Maker Watch (by DadaLand) 为例，精细表盘、表壳主体与柔性 TPU 表带可以在一次打印任务中完成，减少分件打印与后续组装的需求。[查看 Wiki](https://e.bambulab.com/t?c=Sqg2600TPZCRDDpU) 了解功能原理、适用场景及使用限制。

![img_v3_02172_d23ab148-13f9-4876-93d6-3d3fee6a6f1g.jpg](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/img_v3_02172_d23ab148-13f9-4876-93d6-3d3fee6a6f1g.jpg)

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_34.png)

这项能力基于对切片架构的多处重构才得以实现，因此所有多头机型均会受益。混合口径涉及切片、材料、预设及AMS和喷嘴切换适配等多项工作，本次发布先适配拓竹H3C。其他机型的适配信息请以[官方公告](https://mp.weixin.qq.com/s/C1DNh4_YXBhanpIjvJhMXQ)为准。感谢用户的耐心等待，同时欢迎用户和社区反馈实际模型中的切片与打印表现，或基于BambuStudio开源代码更新和迭代。

### 混色功能更新与优化

- 操作更集中：拆色功能已并入混色页面改名为颜色匹配，添加混色耗材时可在同一页面完成手动混色与颜色匹配功能，该功能可以选择项目耗材中的目标色，自动计算出颜色匹配的混色结果，并支持用户在此基础上进行调整。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_35.png)

- 操作更便捷：对拓竹H3C 的 0.4 mm 喷嘴、0.2 mm 与 0.24 mm 层高预设，混色子层功能默认开启，无需手动设置。
- 耗材配置更灵活：混色耗材不再计入项目最多 32 种耗材的限额，并新增对拓竹混色耗材套件 **Bambu PLA Palette** 系列的支持。点击 “使用官方混色套装” 即可自动添加套件内的耗材。
- 重复配置更省事：手动添加混色耗材时会沿用上一次的混色参数，便于复制和微调。
- 纹理模型导入更顺畅：导入页面改为两阶段步骤式，流程更清晰；提升颜色量化性能；支持直接绑定拓竹混色耗材套件；优化界面与视觉布局。

![20261102193847_rec_.gif](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/20261102193847_rec_.gif)

> 另外前序2.8.3 Public Beta和2.8.4 Public Beta的功能也包含在此次版本更新中。

### 优化顶面单调线填充图案的打印路径，减少空驶

优化了顶面单调线填充图案的打印路径，减少打印过程中的空驶移动，从而提升打印效率。

对于顶面细节越多、路径越复杂的模型，该优化效果越明显。

|  |  |
| --- | --- |
| image.png | image.png |

### 切片参数 Tips 支持图文说明

当用户将鼠标悬停在工艺参数名称上时，Bambu Studio 会显示对应的参数 Tips。现在，参数 Tips 支持图文并茂的展示方式，可以更直观地解释参数含义、作用及其对打印结果的影响，帮助新用户更轻松地理解和调整切片参数。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_8.png)

注意：本次更新主要覆盖简单模式下的工艺参数。更多高级参数的 Tips 将在后续版本中持续补充和完善。

### 支持单独设置首层墙与填充的线宽

本版本新增了“首层填充线宽”参数。原有的“首层线宽”参数现在作用于除了首层填充走线之外的其他走线，包括首层墙。用户可以分别控制首层墙线宽与首层填充线宽。

用户可根据实际打印效果，适当调大首层填充线宽。例如，使用 0.4 mm 喷嘴时，可将首层填充线宽设置为 0.55 mm，以改善首层附着效果，降低首层打印不佳的概率。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_20.png)

注意：不建议将首层墙线宽设置得过大，否则可能增加部分模型首层细节丢失的风险。

### 耗材管理器录入界面支持新增耗材供应商 / 品牌

本版本优化了耗材管理器的耗材录入流程，支持在录入界面直接添加自定义耗材供应商或品牌。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_17.png)

当对应的耗材参数预设不存在时，用户可以直接在耗材管理器中创建自定义耗材，无需再跳转到准备页面进行创建，操作流程更加便捷高效。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_19.png)

### 熨烫类型新增阿基米德螺旋线图案，表面效果更均匀

本版本为熨烫功能新增了阿基米德螺旋线图案。不同之处在于，用于熨烫的阿基米德螺旋线的打印顺序会以区域中心为起点逐步向外扩展，走线可被模型内部孔洞自然截断。相比普通同心图案，该打印方式可以减少最内圈走线产生的纹路，使熨烫效果更加均匀。

![img_v3_0215b_6d317f78-dac1-49f6-9251-0439410a494g.jpg](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/img_v3_0215b_6d317f78-dac1-49f6-9251-0439410a494g.jpg)

注意：熨烫效果会受到流量、线距、顶面打印速度、温度、材料物理特性等多种因素影响。用户需要根据实际打印效果进行调校，默认参数并不保证适用于所有场景。 (详见 [Wiki](../parameter/ironing.md))

### 新增次顶面填充图案参数

本版本将次顶面从内部实心填充中单独拆分出来，默认次顶面使用单调填充，以替代原先使用的直线图案。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_22.png)

该调整有助于减少内部实心填充挤压纹在模型顶面透出的情况，提升顶面外观质量。

![snipaste_2026-09-08_15-44-50_1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/snipaste_2026-09-08_15-44-50_1.png)

> 更多请查看[2.8.3 Public Beta](https://github.com/bambulab/BambuStudio/releases#release-v02.08.03.66)和[2.8.4 Public Beta](https://github.com/bambulab/BambuStudio/releases#release-v02.08.04.57)的release note

## 优化与改进

### 准备页面新增折叠状态图标

提升折叠功能的可见性：准备页面左侧面板新增折叠状态图标，让折叠功能更容易被发现。调整参数时，点击设备栏和耗材栏的标题可将它们收起，为参数编辑留出更大空间。

|  |  |
| --- | --- |
| image.png | image.png |

### 设备页Liveview 画面支持以鼠标位置为中心进行缩放

此前，设备页 Liveview 画面只能以画面中心缩放，无法放大查看其他区域。现支持以鼠标位置为中心缩放，方便查看。

![20261102111318_rec_-convert.gif](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/20261102111318_rec_-convert.gif)

### 同步打印机信息时显示参数差异

打开 3MF 文件或同步打印机信息时，会显示当前 3MF 与已连接打印机之间的参数差异，便于确认后再决定是否同步。若没有完全匹配的喷嘴，可从下拉菜单中手动选择。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_15.png)

### 新增 TPU 75A 预设，优化支撑打印参数与行为

- 新增 TPU 75A 耗材预设。
- 优化 PVA 回抽动作：由原先的先回抽 2 mm后停顿、再回抽 10 mm，改为一次连续回抽 12 mm，回抽过程不再中断，改善打印质量。
- 优化 Support for PLA/PETG 材料的打印温度和冷却风扇参数，改善该支撑材料与 PLA 之间的粘接，降低因粘接不足导致打印失败的风险。

### 修改器支持隔层生效，新增贴型填充模式

- 隔层起效果：修改器可按 “生效 N 层、跳过 M 层” 循环生效，例如隔一层加一圈墙，在鞋面等表面形成规律纹理；勾选 “忽略填充设置” 可只覆盖墙圈数、不改动原区域填充。
- 贴形填充：稀疏填充沿每层轮廓走线，在鞋面等曲面上呈放射状，顶底壳、实心填充与桥接保持原图案；工艺、物体、零件与修改器均可开启。

|  |  |
| --- | --- |
| image.png | image.png |

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_3.png)

### 支持调整树状支撑尖端直径

在开发者模式中开放树状支撑的尖端直径参数，可灵活控制支撑尖端的粗细；例如打印微缩模型时调小该值，可获得更精细的支撑。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_28.png)

### AMS 续料功能改进

此前，AMS 续料只能在同一耗材、同一颜色的料盘之间进行。本次更新重新设计了设备页的 AMS 续料功能，并放宽了部分限制：现在可以手动指定续料耗材，同一耗材大类（如 PLA）下的不同子类型（如 PLA Basic 与 PLA Silk）、不同颜色之间均可续料。

![image.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/image_29.png)

注意：该功能目前仅拓竹H3C 打印机支持，其他机型请等待后续固件更新。

### 其他优化项

- 布尔运算、合并、简化模型时保留逐面涂色信息，避免涂色丢失（[#11444](https://github.com/bambulab/BambuStudio/pull/11444)）。感谢[Cstm3DBldr](https://github.com/Cstm3DBldr)
- 擦料塔增加斜向擦嘴动作，降低喷嘴粘料剐蹭导致的打印失败风险
- 新增接口，解决本地保存的用户预设的setting\_id问题（[#12582](https://github.com/bambulab/BambuStudio/pull/12582)）。感谢[chenshj73](https://github.com/chenshj73)
- 按住 Alt 选择零件时锁定零件位置，避免产生微小的移动导致多零件之间相对位置变化。
- 去除盘级别的高低温材料混打的阻塞提示，在材料同步页面常驻注意提示和wiki链接。

![029a6f62-1719-456a-90ba-926d69418e93.jpg](https://wiki.bambulab.com/software/bambu-studio/release-note/v2-9-1-00/029a6f62-1719-456a-90ba-926d69418e93.jpg)

- 优化发送打印时的耗材映射和槽位显示。
- 设备页显示喷嘴状态的具体问题，耗材页面展示喷嘴信息。
- 优化设备页挤出机的挤出状态显示实时性
- 更新外接 AMS 的自动映射规则。
- 适配外接 AMS 的烘干页面。打印机空闲时支持发起 AMS 烘干，并提示连接外接电源。
- 烘干入口调整为从烘干页面进入，与打印机屏幕和 Bambu Handy 保持一致。
- AMS 显示非烘干槽位的温湿度。
- 调整项目耗材列表的布局：同步和设置按钮移到冲刷模式所在的一行。
- X2D使用选料器的场景新增部分耗材兼容性提示。
- 更新新款冷打板（低温板）图片样式。
- 提升标准 3MF 文件的解析兼容性。
- 支持 Bambu Lab E1 空气净化器。

## Bug 修复

- 修复编译问题（[#12596](https://github.com/bambulab/BambuStudio/pull/12596)）。感谢[hadess](https://github.com/hadess)
- 解决Linux鼠标悬停导致tooltip无法关闭的问题（[#12262](https://github.com/bambulab/BambuStudio/pull/12262)）。感谢[Alexey Cluster](https://github.com/ClusterM)
- 修复部分项目打开时，操作对象列表导致软件反复崩溃的问题。
- 修复多项安全问题，提升软件安全性。
- 修复复制或克隆对象时软件崩溃的问题。([#12232](https://github.com/bambulab/BambuStudio/issues/12232), [#12336](https://github.com/bambulab/BambuStudio/issues/12336), [#12375](https://github.com/bambulab/BambuStudio/issues/12375), [#12393](https://github.com/bambulab/BambuStudio/issues/12393))
- 修复导入SVG图片贴附到模型表面时，勾选“使用表面”后软件必现崩溃的问题。
- 修复 macOS 上软件卡死的问题。([#12260](https://github.com/bambulab/BambuStudio/issues/12260))
- 修复 Linux 上鼠标悬停在参数提示上时软件永久卡死的问题。([#12233](https://github.com/bambulab/BambuStudio/issues/12233), [#12253](https://github.com/bambulab/BambuStudio/issues/12253))
- 修复 PETG 支撑接触面打印温度错误（低于喷嘴设定温度）的问题。([#12509](https://github.com/bambulab/BambuStudio/issues/12509), [#12514](https://github.com/bambulab/BambuStudio/issues/12514))
- 修复修改耗材收缩补偿后 brim 丢失的问题。([#12186](https://github.com/bambulab/BambuStudio/issues/12186))
- 修复沉孔桥接部分不生效的问题。([#12237](https://github.com/bambulab/BambuStudio/issues/12237))
- 修复模型存在极细小碎面时，涂色在部分层上颜色错误的问题。([#12720](https://github.com/bambulab/BambuStudio/issues/12720))
- 修复特定模型上修改器不生效的问题。
- 修复使用混色套装时叠色效果不符合预期、无法调出最接近目标色的颜色的问题。
- 修复 X2D 使用不同直径喷嘴时，校准页面按 1 号挤出机的喷嘴直径选用耗材/工艺预设的问题。([#12227](https://github.com/bambulab/BambuStudio/issues/12227))
- 修复发送打印后账号被意外登出的问题。([#12451](https://github.com/bambulab/BambuStudio/issues/12451), [#12462](https://github.com/bambulab/BambuStudio/issues/12462), [#12492](https://github.com/bambulab/BambuStudio/issues/12492))
- 修复切换连接模式后，与打印机的绑定关系没有断开的问题。
- 修复设备页 AMS 图标显示不全的问题。
- 修复切换打印机或编辑外挂料后，外挂料要等十几秒才显示正确的问题。
- 修复设备页显示“等待热床达到目标温度”时，窗口布局超出屏幕边缘的问题。([#12649](https://github.com/bambulab/BambuStudio/issues/12649))
- 修复设备页1号料盘图标被遮挡的问题。([#12638](https://github.com/bambulab/BambuStudio/issues/12638))
- 修复 macOS 上执行操作后屏幕中央出现白色方块遮挡窗口的问题。([#12661](https://github.com/bambulab/BambuStudio/issues/12661))
- 修复创建项目时无法上传图片导致项目无法保存的问题。([#12665](https://github.com/bambulab/BambuStudio/issues/12665))
- 修复从 MakerWorld 打开模型时提示“非受信任站点”的问题。
- 修复断网启动后恢复网络，模型商城和 MakerLab 页面不自动刷新的问题。
- 修复时钟无法切换为 12 小时制的问题。([#12223](https://github.com/bambulab/BambuStudio/issues/12223))
- 修复西班牙语中部分参数翻译错误的问题。([#12667](https://github.com/bambulab/BambuStudio/issues/12667))
