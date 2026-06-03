---
path: zh/h2/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes
title: "多工艺制作工作流"
description: ""
tags: []
created: 2025-03-26T02:18:13.789Z
updated: 2026-03-17T09:57:51.158Z
source: https://wiki.bambulab.com/zh/h2/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes
---

## **软件架构与核心流程**

Bambu Suite 采用 **设计→分盘和准备制作→制作状态监控** 的三界面架构，拥有一套标准化的工作流：

1. **设计界面**：完成图案创作与工艺设置，呈现的是2D项目的整体多图层“拼装”效果
2. **准备界面**：智能分盘与材料适配
3. **监控界面**：实时跟踪加工进度

Bambu Suite支持**激光雕刻、激光切割、基础刀切、画笔、打印后刀切**等加工工艺，允许单项目内使用多个制作工艺加工多种材料，同时可以在单次任务中进行**多工艺组合制作**（更多信息 [不同工艺同盘制作的可组合性](../../../../software/bambu-suite/manual/composability-of-different-process-types-processed-on-same-plate.md)）。用户不需要按照工艺或工具模组拆分多个制作任务。制作中若需要更换工具模组，会自动触发机器暂停，提示用户更换工具模组。用户更换后即可恢复任务，直接进行下一道工艺的加工。

### **典型应用示例：立体贺卡制作**

立体贺卡包含多个不同的加工工艺，包括不同的画笔，激光雕刻，基础刀切等。

1. **设计阶段**：

   - 给贺卡上各图案设置加工工艺，如激光雕刻工艺，两种颜色画笔（红色和黑色）和基础刀切。
   - 移动这些图案到指定的位置，使贺卡完整。然后（重要！）使用“绑定”工具将这些图案绑定在一起。这样他们才会在同一张纸上相对固定的位置加工。

![image_-_2025-03-26t102332.673.png](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image_-_2025-03-26t102332.673.png)

2. **准备阶段**：

- 选择牛皮纸来制作卡片，我们只需要一种材料，只需要使用一种垫板，所有的加工都可以在一盘内完成。
- 因为我们需要多个不同的工艺，所以机器会在每一种工艺完成时暂停，并等待我们更换加工工具。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-10.png)

3. **加工阶段**：

- 跟随 Bambu Suite 或者机器屏幕上的指引完成加工。根据提示更换加工工具。（激光模组→刀切模组和画笔→切换为刀头）。
- 用户按指引更换工具后恢复任务，一步一步完成所有工艺加工。机器将保证不同加工工艺下图案的定位精度。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-8.png)

**多工艺组合制作工作流的显著特点：**

1. **可视化拼装效果。**设计画布实时呈现多图案、多工艺图层的完整“拼装”效果；
2. **智能分盘加工。**自动按材料类型分组为多个加工盘次，且单盘内支持混合工艺连续加工（如雕刻+切割+绘画），避免了拆分多个加工任务的步骤，简化复杂项目流程；
3. **确保加工定位准确。**多工艺组合制作保证不同工艺图案的相对位置的准确性，无需用户拆分为多次加工并进行手动对齐；
4. **完善的引导流程。**Step by step的制作引导，引导用户在加工过程中进行工具模组切换，减少出错概率；

## 软件各界面工作流详解

### 设计界面

#### 主要功能

Bambu Suite的设计界面采用整体画布布局，直观展示项目的多层叠加效果。用户可以在完成基础刀切（如贺卡轮廓）后，继续在贺卡上叠加雕刻或绘制其他图案。设计界面主要功能包括：

1. 图案编辑：支持调整图层关系和加工工艺设置
2. 工艺选择：提供激光雕刻（线条/填充）、激光切割、画笔、基础刀切等多种工艺。可点击下拉列表中的加工工艺介绍wiki，查看每一种工艺的详细介绍、适用场景和制作效果（ [2D工艺类型介绍](../../../../software/bambu-suite/manual/2d-processing-type-intro.md)）。
3. 实时预览：渲染效果尽可能真实反映最终加工效果，所见即所得，便于用户直观地看到所有图案的整体“多层拼装”效果。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/img_v3_02jk_67f71c87-ecc2-4223-8927-e9a9d97db91g.jpg)

#### 设计工具

设计页面提供了丰富的图案创建和编辑工具，便于用户直接编辑和修改项目的整体效果，设计工具分为三大类：

- 创作类工具：图片导入、形状绘制（矩形/圆/圆弧）、自由画笔、文字工具、二维码生成工具等；
- 编辑工具：设置图案坐标定位、图案角度调整、设置圆角、图案尺寸缩放、镜像翻转
- 贴纸工具：用于为图案附加贴纸边框属性，以及设定贴纸切穿层数，方便用户制作卡通贴纸。

#### 界面布局

设计界面布局如下：

- 右上角：设备连接和查看的入口，方便用户绑定和连接物理机器；
- 右中下方：整个项目的所有图案对象的列表，以及常用的对象组合和布尔工具，**您还可以进一步地点击材料组标签，为不同的图案设置不同的加工材料。**
- 底部：颜色选择、画布缩放和套索选择工具，方便用户调整画布的大小，选中画布中期望的图案对象。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image.png)

### 准备界面

准备界面通过设计界面"准备制作"按钮进入，主要功能包括：

1. **预览和智能分盘：**

   - 自动根据加工工艺以及绑定和分组情况，结合制作盘的大小，自动进行分盘和摆盘。
   - 可以点击右侧的盘列表（材料组）查看每一盘内的图案，并为每一个材料组分配加工材料。
   - 支持手动调整图案的分盘，右击图案即可选择“移动到盘”或“移动到组”。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-7.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-6.png)

2. **材料摆盘：**

- 点击“拍照”按钮，获取加工平面视图，并查看图案是否摆放在待加工材料的合适位置；
- 可以手动选中图案移动至合适位置。或者直接点击“自动摆盘”按钮，软件会自动识别材料的轮廓和位置，将图案调整到材料的范围内。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-9.png)

3. **加工准备：**

- 激光加工需要让激光光标正好对焦在材料表面，才能确保加工质量。软件提供了测厚功能，点击厚度测量按钮会触发机器自动测量材料的厚度，来确保激光对焦。对于材料反光无法测量的场景，您可以直接手动测量材料的厚度并填入参数框内。
- 点击右下角的预览按钮，可查看加工路径和加工时长。拖拽下方的进度条或者直接点击左下角的播放按钮，查看加工路径的模拟过程。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-3.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-5.png)

- 随后即可点击“制作”按钮，软件会弹窗提示用户使用对应的加工工具头以及垫板类型，在确定物理机器相关工具头和垫板安装好之后，即可点击发送，开始加工。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-4.png)

### 制作过程监控界面

1. **任务启动和确认：**;务发送成功之后，软件会自动跳转到制作过程的监控界面。首先它会提示用户去机器屏幕前进行操作，确保相关材料，工具头，垫板准备好。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-1.png)

2. **实时监控：**确认一切准备就绪后，根据屏幕提示点击按钮让机器开始加工，等待加工完成。期间可以通过软件远程查看摄像头画面，当加工任务发生异常或者不想继续进行时，您可以使用界面右下角的按钮暂停或者中止制作任务。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/image-2.png)

3. **加工后处理：**对于复杂的多盘项目，加工完成所有盘后，用户需要将多盘图案进行组装。拼装指南，项目描述等信息可以保存到项目文件中，便于以后分享和查看。

![8a3df116-4569-410e-a046-826a140eb42e.gif](https://wiki.bambulab.com/software/bambu-suite/manual/smart-work-flow-for-multiple-combined-processes/8a3df116-4569-410e-a046-826a140eb42e.gif)
