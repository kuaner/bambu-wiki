---
path: zh/software/bambu-studio/release/release-note-2-4-0
title: "Bambu Studio 2.4.0 版本说明"
description: ""
tags: []
created: 2025-11-18T11:41:20.120Z
updated: 2025-11-18T14:50:58.746Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-4-0
---

V2.4.0版本新增对[Bambu Lab H2C](https://bambulab.com/zh/h2c)支持，同时包含了若干新功能与Bug修复。

|  |
| --- |
|  |

### 支持Bambu Lab H2C

Bambu Lab H2C其右侧挤出机支持6喷嘴。其切片与使用流程整体与Bambu Lab H2D保持一致，在此基础上针对H2C的新特性进行了以下适配与优化，更多内容参考[Bambu Wiki](../../../h2c/manual/bambu-studio-h2c-operation.md)：

- **切片信息设置与打印机信息同步：**支持**混合模式**（高流量与标准流量）切片。

> ⚠注意：暂不支持不同口径混合切片。

|  |  |
| --- | --- |
|  |  |

- **冲刷模式调整**：支持在标准模式和省料模式之间切换。更多详情请参考[Bambu Wiki](../h2c-purge-mode.md)。

|  |
| --- |
|  |

- **发送打印支持映射到特定喷嘴**：除AMS可指定映射槽位外，右挤出头支持映射到特定喷嘴。

|  |
| --- |
|  |

- **设备页面新增喷嘴详情**：支持自动读取全部喷嘴信息。  
  ![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/036.png)

### 新功能

#### 支持不同特征使用不同耗材打印（开发者模式）

在**开发者模式**的“**对象列表-其他-高级”**中，现支持对单个对象（Object）将墙、实心填充、稀疏填充分别指定为不同耗材进行打印。该功能可充分挖掘H2D、H2C等多挤出机打印机的使用潜力，提供更丰富的打印可能。该功能参考了PrusaSlicer和OrcaSlicer的实现逻辑，并在此基础上修复了一系列问题。感谢[@SoftFever](https://github.com/SoftFever)和[@ianalexis](https://github.com/ianalexis)的贡献。

> ⚠注意：
>
> - 仅在**开发者模式**下可见。
> - 仅支持**对象（Object）级别**设置，不支持全局设置。

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/037.png)

#### 稀疏填充线倍增填充器

现支持针对稀疏填充线数进行倍增处理，可在进行工艺预设的“**强度-稀疏填充**”中进行设置。该选项可增强零件强度。感谢[@RF47](https://github.com/RF47)的贡献。

> ⚠注意：该功能目前暂不支持以下部分填充类型：同心、线、希尔伯特曲线、阿基米德螺旋线、八角螺旋、交叉层叠、Zig Zag、Cross Zag、Locked Zag。

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/038.png)

#### 对齐功能

现在支持对在X、Y、Z三个方向，对多选对象（Object）/零件（Part）进行**对齐**和**平均分布**。复选多个对象或零件后，通过Gizmo的**移动**功能或**右键菜单-对齐/分布**使用使用对应功能。

> 💡Tip：Ctrl+左键可多选对象（Object），Alt+左键可多选零件（Part）

![001.gif](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/001.gif)

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/039.png)

#### 移动盘

在选中的盘上**右键**选择**移动盘**，即可将该盘整体移动到目标位置。感谢[@Azio-Pantheon](https://github.com/Azio-Pantheon)的贡献。

![001.gif](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/002.gif)

#### 支持项目页内容编辑

我们更新了项目页的样式，同时新增对3MF项目页内容的编辑支持([#4546](https://github.com/bambulab/BambuStudio/issues/4546), [#2111](https://github.com/bambulab/BambuStudio/issues/2111))：

- 在项目页点击右上角**编辑**按钮进入编辑模式。
- 完成修改后点击**保存**以应用更改。

> ⚠注意：当您的3MF上传至MakerWorld时，原3MF中项目页内容会被MakerWorld填写内容覆盖。

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/040.png)

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/006.png)

#### 外墙和填充嵌合功能

鞋类模型存在裸露填充和墙体粘接的场景（如下图所示），此时墙体和填充之间的连接非常脆弱。我们增加了外墙和填充嵌合功能来改善该问题，位于工艺选项卡的“**强度-墙**”设置下。

|  |  |
| --- | --- |
|  |  |

当功能开启后，会在墙内侧（非外观面）增加嵌合区域，并引入Z方向的叠加效果（如下图所示）。该功能保证了水平和Z方向的强度，有利于类似场景的打印件表现。

|  |  |
| --- | --- |
|  |  |

### 改进

1. **X/P系列支持E3D喷嘴高流量切片。**

![xpe3d.png](https://wiki.bambulab.com/studio_releasenote/2_4_0_public/xpe3d.png)

2. **GCodeViewer更新**：升级后的GCodeViewer可解决部分设备显示时的渲染卡顿问题。新版本的GCodeViewer在Windows/Linux的OpenGL版本不低于3.2时自动启用（您可在**偏好设置-3D设置**中关闭）。其他平台上暂仍使用旧版本。
3. 挤出机参数设置交互优化。

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/013.png)

4. 优化了AMS白色耗材的余量显示：当耗材余量低于10%时，统一按照10%余量进行显示。
5. 切片后GCodeViewer默认记忆其状态（展开或折叠）。
6. 更新了部分Helio优化功能界面，感谢[@HelioPri](https://github.com/HelioPri)的支持。
7. 布尔功能新增列表全选按钮。

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/014.png)

### Bug修复

1. 修复了设备页耗材列表排序的的错误的问题，感谢[@ansonl](https://github.com/ansonl)的贡献。
2. 修复了部分tooltip拼写错误，感谢[@kunningKing11](https://github.com/kunningKing11)的贡献。
3. 修复了部分场景下同步AMS耗材后的crash问题。([#8576](https://github.com/bambulab/BambuStudio/issues/8576))
4. 修复了部分Intel集成显卡渲染导致的crash问题。([#8427](https://github.com/bambulab/BambuStudio/issues/8427))
5. 修复了部分场景下No FuzzySkin选项不生效的错误。([#7841](https://github.com/bambulab/BambuStudio/issues/7841))
6. 修复了OBS直播在Mac/Linux失效的问题。([#8129](https://github.com/bambulab/BambuStudio/issues/8129))
7. 修复了文字工具中粘贴emoji时的crash问题。([#8728](https://github.com/bambulab/BambuStudio/issues/8728))
8. 修复了部分场景下文字工具渲染错误。([#8705](https://github.com/bambulab/BambuStudio/issues/8705))
9. Locked Zag填充新增“使用填充纹理以取代封闭的顶面和底面”的选项（默认关闭），此选项关闭时，顶面和底面与保持默认样式，当该选项打开，顶面与地面会设置为对应的填充纹理，保证纹理的美观性。

![041.png](https://wiki.bambulab.com/software/bambu-studio/release-note-2-4-0/015.png)

10. 修复了因overlap区域未清除导致的填充偏移的错误。
11. 修复了部分场景下AMS显示不全的问题。([#8441](https://github.com/bambulab/BambuStudio/issues/8441) , [#8411](https://github.com/bambulab/BambuStudio/issues/8411) , [#8468](https://github.com/bambulab/BambuStudio/issues/8468) , [#8522](https://github.com/bambulab/BambuStudio/issues/8522) , [#8762](https://github.com/bambulab/BambuStudio/issues/8762))
12. 修复了多AMS连接时的显示排序问题。([#8590](https://github.com/bambulab/BambuStudio/issues/8590) , [#8553](https://github.com/bambulab/BambuStudio/issues/8553))
13. 修复了部分用户OBS推流失败的问题。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
