---
path: zh/software/bambu-studio/assembly-view/assemble-guide
title: "整体视图装配指南功能"
description: "本文将介绍如何在整体视图下制作装配指南。"
tags: []
created: 2026-05-22T02:28:27.892Z
updated: 2026-06-30T03:19:45.813Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/assembly-view/assemble-guide
---

## 功能介绍

随着 3D 打印作品的形式越来越丰富，许多模型不再是单个零件即可完成，而是需要通过多个打印件的组装，才能呈现出完整、有趣且美观的成品效果。对于零件较多的作品，如果创作者在分享时没有提供清晰的装配说明，普通用户，尤其是新手用户，往往会不知道从哪里开始，影响打印后的组装体验。

目前，装配说明的制作通常需要借助 SolidWorks 等专业软件，或通过手动截图、排版等方式完成。这类方式不仅制作效率较低，对创作者的工具使用能力也有一定要求，同时成品说明书的格式和展示效果也不够统一规范。

基于以上背景，并结合用户反馈，我们开发了装配指南功能。它既可以帮助习惯使用 STEP / STP 文件的专业创作者，更高效地制作装配说明；也支持对 MakerWorld 上已有的大量 3MF 模型进行二次装配说明制作。同时，该功能降低了使用门槛，让更多新手用户也能够轻松体验装配指南的创建过程。该功能支持直接在 Bambu Studio 内设计并生成模型组装指南，在导入装配体后，可逆向还原整个零件拼装过程。

一份清晰、直观的装配指南，不仅能提升复杂 3D 打印作品的传播和复刻效率，也能让用户在组装过程中获得额外的乐趣。尤其对于小朋友来说，这种“打印 + 组装”的体验有点类似积木玩具，能够让 3D 打印作品变得更加有趣、更具互动性。

示例模型来源：[Original OpenRC F1](https://makerworld.com/en/models/1080601-original-openrc-f1#profileId-2818893) by Daniel Norée

### 步骤列表

1.点击后可预览装配体完整组装后的情况，光标悬停将显示所有对象或零件名称。

![list1.jpg](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/list1.jpg)

2.可增减步骤，点击右侧菜单栏可选择所需对象或零件。

![list1.jpg](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/list2.jpg)

### 画布编辑

1.可在画布上增加连接类型标签，或添加框图、文本栏、箭头等备注。

![备注.jpg](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E5%A4%87%E6%B3%A8.jpg)

2.可隐藏或显示标签，显示标签时能够点击自动布局，软件将自动排列标签。

![标签.jpg](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E6%A0%87%E7%AD%BE.jpg)

3.可额外添加“起始帧”，自动爆炸当前对象，统一当前步骤视角。

![帧.jpg](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E5%B8%A7.jpg)

### 预览设置

![预览.jpg](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E9%A2%84%E8%A7%882.jpg)

1.调整剖面视图：可观察封闭模型内部情况。  
2.切换选择模式：决定单击鼠标时选择零件或对象。  
3.切换显示模式：透视或隐藏其他对象或零件。

## 流程介绍

导入 step 文件后，软件会自动生成装配步骤，每一个步骤会自动推荐了合适的相机视角，并自动布局一次标签。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD.webp)

点击左侧列表，修改需要的对象或零件。每个对象或零件都可以选中并单独高亮，单击确认后完成零件选取。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(1).webp)

支持“相机视角推荐”功能，点击后自动切换为合适的视角。此外，可以双击画布空白取消所有零件选择，双击标签来定位需要选择的对象或零件，标签名字也可以进行修改，按下回车键保存。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(2).webp)

支持两种显示模式，用于透视或隐藏不需要的零件。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(3).webp)

支持给每个步骤添加起始帧，可增加自动爆炸功能，自动打散需要组装的零件，并对选中的物体添加不同的卡扣标签、矩形或者文字标签，保存后通过单击播放按钮可以得到一个插值动画。

> 若播放过程中标签过于杂乱，可隐藏起始帧的标签。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(4).webp)  
![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(5).webp)

可以旋转相机，找到自己喜欢的视角，如果想以此视角作为整个插值动画的视角，可以单击 “应用当前视角到所有帧 ”的按钮，再重复上述过程完成插值动画。

> 对于视角转动后的标签，可以点击自动布局重新排列。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(6).webp)

标签设置里面支持 仅显示对象的功能，这样就可以看到多个零件合并成一个对象的完整过程。

![](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(7).webp)

所有步骤调整完成后，可点击播放按钮，预览“MP4”格式。

![下载_(8).webp](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD_(8).webp)

步骤确认无误后，可以单击导出按钮，目前支持导出 Pdf、Markdown、MP4 等三种格式。

![下载.png](https://wiki.bambulab.com/software/bambu-studio/assemble-guide/%E4%B8%8B%E8%BD%BD.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
