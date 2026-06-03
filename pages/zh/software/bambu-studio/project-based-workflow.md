---
path: zh/software/bambu-studio/project-based-workflow
title: "基于项目和附件的工作流程"
description: "本文介绍了Bambu Studio中项目和附件板块的用法。"
tags: []
created: 2023-08-30T07:48:41.734Z
updated: 2024-05-28T10:55:20.914Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/project-based-workflow
---

# 常用于复杂的模型

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/pictures_aio_2.png)

许多令人惊叹的 3D 打印模型都是由数十或数百个物体组成。  
虽然非常有吸引力，但当用户真正开始创建它们时会遇到很多挑战，最常见的挑战有：

- 打印的对象需要从几个到几十个项目文件中进行手动摆放。在项目文件中重新摆放对象时，既繁琐又容易出错。
- 调整切片配置需要对3D打印有一定的了解。即使是经验丰富的用户，也可能花费大量时间，并在实际打印中遇到问题。
- 由于缺乏整体效果预览视图，很难自由定制模型的颜色。
- 将散落在不同项目文件中，并且打印失败的对象，要重新挑选出来打印也不容易。
- 缺少一些重要的指导性文件。

# 项目的工作流程

Bambu Studio 提供以下关键功能来解决这些痛点，并使模型原创作者和终端用户的 3D 打印工作流程比以往更加顺畅。

## 多盘管理

Bambu Studio在工作流程方面取得了很大的进步，其中包括支持多盘机制。它可以将众多的对象有序的排列在盘上，每个盘代表一个打印任务。与将这些对象放置在多个项目文件中相比，单个项目文件具有模型的全局视角，您在使用过程中，可以轻松规划每个盘上放置的对象（可以通过在不同盘之间，直接任意移动对象）

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/multi_plates.png)

同时，多盘机制也是零件和组装的基础。了解更多详情，请参考[盘功能介绍 | Bambu Lab Wiki](plates_management.md)。

## 附件板块

附件板块中包含了项目所需的所有辅助资源，这个板块主要用于模型的原创作者上传相关文件，并且可以让模型的用户在使用过程中添加文件进行补充。

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/project_resource_cn.png)

- **基本信息**  
  基本信息包含“作者”名称和“模型名字”。它们标记了模型的所有权，并且也会显示在设备屏幕上。模型的用户，也能在“项目”中看到这些模型信息。
- **图片**  
  包含该项目的封面、不同的配色方案、模型打印成品图等。还支持选择图片作为该项目的封面，封面将在 PC 和打印机设备的文件浏览中显示为缩略图。
- **物料清单**  
  包含构成模型的所有零件，特别是需采购的零件（不可打印零件，比如螺丝、电机和弹簧），用户在组装模型之前需要准备好所有的所需零件。它支持 PDF 和 Excel 格式，直接双击物料清单(BOM)文件，可以打开它。
- **组装指南**  
  组装指南指导指导用户如何将大量零件组装成一个完整的模型，需要PDF格式，双击文件即可打开。
- **其他**  
  模型的原创作者可能会告诉用户一些关于此模型的注意事项或者作品的故事背景等，可以在这里添加文本文件。

附件板块页面内容演示，如图：

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/fu_jian1_cn.gif)

## 在对象零件和装配视图之间切换

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/zhuangpeishitu.gif)

- **零件视图**  
  将模型拆分为零件可以更轻松地打印，即使没有AMS，也可以帮您打印不同颜色的零件。
- **装配视图**  
  装配视图对于查看模型着色、设置零件的切片参数以及组装打印的零件特别有用。  
  *注意：装配视图要求原始导入模型是装配好的模型，如 STEP 文件。*

## 3MF文件格式

3MF 文件实际上是一个压缩文件，比 STL文件 小得多。它包含项目中所需的一切，例如

- 所有对象的3D几何数据
- 所有的切片参数和修改器
- 将对象摆放在一个或多个盘中
- 分割前的对象几何关系，可用于恢复装配视图
- 颜色信息
- 支撑绘制信息
- 项目资源（物料清单、组装指南、图片等）
- 作者信息

# 模型原创作者和终端用户的工作流程

## 模型原创作者工作流程

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/creator_workflow_cn.png)

建议导入STEP文件格式。与STL相比，它为项目提供了更重要的信息。

## 终端用户工作流程

![](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/regular_user_workflow_cn.png)

所有设置和项目文件都已经打包到了一个 3mf 文件中准备就绪，可直接使用。

无需多个项目文件（每个文件用于一个打印任务），无需繁琐的模型着色，无需复杂的参数调整，也无需担心模型分析过程中物流清单和装配指南等重要资源的丢失。

此外，即使模型被分解成零散的零件，用户仍可在装配视图中查看模型的完整装配图和爆炸图。这为用户自定义模型颜色提供了极大的便利，并有助于模型组装过程。

注意：这需要作者导入 STEP 模型。

## 项目示例

下载链接: [OpenRC\_F1\_v2.3mf](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/openrc_f1_v2.3mf)

![example_project.png](https://wiki.bambulab.com/software/bambu-studio/project-based-workflow/example_project.png)

这个项目”OpenRC\_F1\_v2”, 是 [Daniel Noree](https://twitter.com/DanielNoree)的“[OpenRC F1](https://www.thingiverse.com/thing:1193309)”衍生版，用于[CC-BY-SA](http://creativecommons.org/licenses/by-sa/4.0/).” OpenRC\_F1\_v1” 采用 [CC-BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) x许可，由by Bambu Lab发布。

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
