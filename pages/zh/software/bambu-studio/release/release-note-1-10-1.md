---
path: zh/software/bambu-studio/release/release-note-1-10-1
title: "Bambu Studio 1.10.1 Public Release 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-11-15T08:10:38.880Z
updated: 2024-11-15T13:14:40.313Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-10-1
---

该版本为基于1.10.0的Hotfix版本

## Bugs Fixed

1. **STEP文件导入崩溃修复**:修复了部分用户在导入STEP文件时发生崩溃的问题，并优化了STEP导入参数设置框的UI，以避免部分Mac机型出现排版错误。特别感谢[@benjaminkott](https://github.com/benjaminkott)率先发现并协助解决该问题。([#5816](https://github.com/bambulab/BambuStudio/issues/5186),[#5819](https://github.com/bambulab/BambuStudio/issues/5189) ,[#5192](https://github.com/bambulab/BambuStudio/issues/5192) ,[#5198](https://github.com/bambulab/BambuStudio/issues/5198),[#5199](https://github.com/bambulab/BambuStudio/issues/5199) ,[#5197](https://github.com/bambulab/BambuStudio/issues/5197) ,[#5203](https://github.com/bambulab/BambuStudio/issues/5203) ,[#5208](https://github.com/bambulab/BambuStudio/issues/5208) ,[#5210](https://github.com/bambulab/BambuStudio/issues/5210) ,[#5218](https://github.com/bambulab/BambuStudio/issues/5218) ,[#5222](https://github.com/bambulab/BambuStudio/issues/5222) ,[#5225](https://github.com/bambulab/BambuStudio/issues/5225) ,[#5243](https://github.com/bambulab/BambuStudio/issues/5243) ,[#5248](https://github.com/bambulab/BambuStudio/issues/5248))
2. **Mac上切片后性能问题修复**:修复了部分Intel CPU的Mac在切片后界面响应速度变慢的问题。特别感谢[@HO44-PROJECT](https://github.com/HO44-PROJECT)、[@northdakota](https://github.com/northdakota)和其他一系列用户积极协助并帮助验证了该问题。我们还在偏好设置中新增了“开启opengl多实例渲染性能”选项，若您仍遇到性能下降，可尝试关闭此选项。([#5194](https://github.com/bambulab/BambuStudio/issues/5194) ,[#5237](https://github.com/bambulab/BambuStudio/issues/5237) ,[#5200](https://github.com/bambulab/BambuStudio/issues/5200) ,[#5247](https://github.com/bambulab/BambuStudio/issues/5247) ,[#5244](https://github.com/bambulab/BambuStudio/issues/5244) ,[#5223](https://github.com/bambulab/BambuStudio/issues/5223) )

|  |
| --- |
|  |

3. **打印机温度显示错误修复**：修复了打印机温度显示不正确或延迟的问题。([#5216](https://github.com/bambulab/BambuStudio/issues/5216),[#5196](https://github.com/bambulab/BambuStudio/issues/5196))
4. **停止打印弹窗提示优化**：优化了停止打印时弹窗的文案，使之语义表达更清晰。

|  |
| --- |
|  |

5. **关闭Scarf Seam默认启用**：在测试了PLA大类各个材料的Scarf seam效果和合理普适的参数后，我们在V1.10.0 Public Release版本中将Scarf seam的开关以及部分参数设置为材料属性，并对大部分PLA材料的Scarf seam默认启用。版本发布后，我们发现由于某些模型的轮廓角度检测判定存在差异，scarf seam的应用难以在z方向保持均一性，造成表面seam质量差异。如下图所示，根据角度阈值判定后选择应用了scarf seam的区域表面更为平整，而没有应用Scarf seam的区域表面质量较差。两个区域的交界处的凹凸不平在Seam附近形成了不一致的表面效果。我们将在后续版本进一步优化Scarf Seam的使用场景逻辑，以保持同一条直线上的外表面打印质量一致。

|  |  |
| --- | --- |
|  |  |

鉴于此缺陷，Scarf seam功能被暂时关闭。如果您想要使用Scarf seam，请从材料编辑页面打开该功能。如果使用时Scarf seam出现不整齐的情况，可以调小整应用角度阈值或者关闭智能斜拼接缝应用来改善这个问题。

|  |  |
| --- | --- |
|  |  |

6. 修复了部分STL着色后分割到Objects颜色异常的问题。([#5201](https://github.com/bambulab/BambuStudio/issues/5201))
7. 修复了部分情况下暂停打印失效的问题。([#5253](https://github.com/bambulab/BambuStudio/issues/5253) ,[#5275](https://github.com/bambulab/BambuStudio/issues/5275))
