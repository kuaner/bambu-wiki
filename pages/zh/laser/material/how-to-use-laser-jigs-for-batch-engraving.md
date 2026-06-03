---
path: zh/laser/material/how-to-use-laser-jigs-for-batch-engraving
title: "如何使用激光夹具进行批量激光雕刻"
description: "本篇教程将介绍如何使用激光夹具进行批量激光雕刻。"
tags: []
created: 2026-01-06T09:28:28.389Z
updated: 2026-03-27T04:12:32.879Z
source: https://wiki.bambulab.com/zh/laser/material/how-to-use-laser-jigs-for-batch-engraving
---

**激光夹具**是一种定制夹具，用于固定多个需要激光雕刻的小物件，例如金属名片或圆形标签，实现批量且精确地在物品上雕刻徽标、文字或图案，提高批量加工效率；同时，有效防止物品在雕刻过程中移动导致雕刻错位。

本教程将为您介绍两种使用激光夹具进行激光雕刻的案例，分别是**不锈钢圆形标签**的激光雕刻，和 **铝制名片**的激光雕刻。

## 所需工具及材料

- **拓竹 3D 打印机及激光模组：**  
  [H2C 多色激光全能套装](https://item.jd.com/10198832928382.html#switch-sku)  
  [H2D 激光全能套装](https://item.jd.com/10143821589764.html#switch-sku)  
  [H2S 激光全能套装](https://item.jd.com/10174563227919.html#switch-sku)
- **激光夹具**
- **Bambu Studio:** 用于打印激光夹具。
- **Bambu Suite:** 用于激光雕刻设计。
- **耗材：** 用于打印激光夹具。
- **激光雕刻材料：** 本篇将使用到 [20/30 mm 圆形不锈钢吊牌](https://item.jd.com/10145052666125.html)，以及 [黑色铝制名片](https://item.jd.com/10145052635852.html)。

## 不锈钢吊牌的雕刻步骤

### 步骤一. 打印激光夹具

在本例中，我们将打印 Orbrak 的[圆形不锈钢标签激光夹具](https://makerworld.com/zh/models/1338639-h2d-laser-jig-round-stainless-steel-tag#profileId-1378535)，用来放置不锈钢吊牌，进行激光雕刻。

首先，[点击此处](https://makerworld.com/zh/models/1338639-h2d-laser-jig-round-stainless-steel-tag#profileId-1378535) 打开模型详情页，选择“**在 Bambu Studio 中打开**”。

![1.png](https://wiki.bambulab.com/material/1.png)

将模型导入 Bambu Studio 后，参考下图完成打印前的基础设置：

1. 选择您的**3D打印机**型号。
2. 选择与您要打印的耗材相匹配的**打印板类型**。
3. 选择**耗材类型和颜色**。
4. 选择**层高**。较低的图层高度可以提供更多细节，但也会增加打印时间。
5. 点击**切片单盘**，对模型进行切片。

![2._bambu_studio_基本设置.png](https://wiki.bambulab.com/material/2._bambu_studio_%E5%9F%BA%E6%9C%AC%E8%AE%BE%E7%BD%AE.png)

6. 点击“**打印单盘**”。

![3.打印单盘.png](https://wiki.bambulab.com/material/3.%E6%89%93%E5%8D%B0%E5%8D%95%E7%9B%98.png)

7. 确认打印机和耗材，然后单击“**发送**”。

![](https://wiki.bambulab.com/material/4.单击“发送”.png)

8. 等待激光夹具打印完成。

![5.打印完成.png.png](https://wiki.bambulab.com/material/5.%E6%89%93%E5%8D%B0%E5%AE%8C%E6%88%90.png.png)

### 步骤二. 安装激光模组以及激光垫板

安装激光模组以及激光垫板，详细教程请参考 [H2S 激光模组安装指南](../../h2s/manual/laser-module-lnstallation-guide.md)。

![setting_up_the_laser_module.png](https://wiki.bambulab.com/material/setting_up_the_laser_module.png)

安装完成后，启动激光挂载校准。

### 步骤三. 放置激光切割材料

在本例中，我们将雕刻两个不锈钢吊牌，它们的直径分别为 20 mm 与 30 mm。

首先，将这两个吊牌放置在打印好的激光夹具凹槽内，如下图所示。

![2placing_tags.png](https://wiki.bambulab.com/material/2placing_tags.png)

然后，将激光夹具放在打印机内的激光垫板上。

![3放在激光垫板上.png.png](https://wiki.bambulab.com/material/3%E6%94%BE%E5%9C%A8%E6%BF%80%E5%85%89%E5%9E%AB%E6%9D%BF%E4%B8%8A.png.png)

### 步骤四. 准备激光雕刻图案

本例中，我们将在不锈钢吊牌上雕刻 Makerworld 上的[宠物身份牌](https://makerworld.com/zh/models/1257220-pet-id-tag#profileId-1280819)图案。

首先，[点击此处](https://makerworld.com/zh/models/1257220-pet-id-tag#profileId-1280819) 打开宠物身份牌图案设计详情页，点击 “**在 Bambu Suite 中打开**”，导入该设计至 Bambu Suite。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-2.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-2.png)

导入后，请点击右上角打印机型号左侧的小箭头，选择你的打印机型号。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-3.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-3.png)

然后，图案将显示在中间的工作区中。

![7.设计图.png](https://wiki.bambulab.com/material/7.%E8%AE%BE%E8%AE%A1%E5%9B%BE.png)

我们可以放大查看图案，并调整大小。在本例中，我们只保留了第一个图案，删除了其余两个。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-4.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-4.png)

双击文本即可输入你想雕刻的文本内容。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-5.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-5.png)

在“**工艺类型**”中，选择“**激光填充雕刻**”选项。有关工艺类型的更多详细信息，请参考 [2D 工艺类型介绍](../../software/bambu-suite/manual/2d-processing-type-intro.md)。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-6.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-6.png)

然后，在“**材料组**”选择“**不锈钢吊牌**” 。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-7.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-7.png)

增加图案数量，可以通过复制粘贴来操作。

如果您想制作多个相同的图案（例如 6 个），也可以选择“**阵列**”>“**阵列类型**"，通过调整 X 轴和 Y 轴上的**个数**来指定数量，如下图所示。

![how_to_use_laser_jigs_for_batch_engraving-chinese-array.gif](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-array.gif)

为了方便在激光夹具上预览图案效果，我们可以从工具栏菜单中更改图案颜色。然后单击**准备制作**。

> **注意：** 激光雕刻的实际颜色默认为黑色。更改后的颜色是为了方便在激光夹具上预览图案效果；并不会改变实际雕刻出的颜色。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-8.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-8.png)

点击顶部工具栏中的“**拍照**”按钮，可以预览打印机内部的俯视实时画面。

|  |  |
| --- | --- |
|  |  |

在画面中，将图案拖放到吊牌的位置。你还可以根据需要调整**图案大小**和**旋转角度**。

![how_to_use_laser_jigs_for_batch_engraving-chinese-positioning_the_designs.gif](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-positioning_the_designs.gif)

在“**厚度**”部分，单击下拉图标，然后选择“**快速测量**”，打印机将进行厚度测量以设置激光高度。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-11.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-11.png)

### 步骤五. 开始激光雕刻

点击“**预览**”，查看雕刻路径。

![how_to_use_laser_jigs_for_batch_engraving-chinese-previewing_the_model.gif](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-previewing_the_model.gif)

点击“**制作**”开始激光雕刻。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-12.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-12.png)

检查信息无误后，点击**发送**。

|  |  |
| --- | --- |
|  |  |

发送任务后，请根据弹出的窗口提示，前往打印机并按照打印机屏幕上的说明进行操作。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-15.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-15.png)

操作完成后，打印机将会开始进行激光雕刻。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-16.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-16.png)

激光雕刻后的效果如下图所示。

![final_design.png](https://wiki.bambulab.com/material/final_design.png)

## 名片的雕刻步骤

### 步骤一. 定制名片激光雕刻夹具

首先， [点击此处](https://makerworld.com/zh/models/2071296-business-card-alignment-jig-for-the-h2-laser#profileId-2237213)，打开名片对齐夹具模型详情页，点击”**定制**“。

![名片1.png](https://wiki.bambulab.com/material/%E5%90%8D%E7%89%871.png)

跳转至 MakerLab 页面后，选择打印机型号①，在本例中我们将使用 H2D 激光套装②。

![名片2.png](https://wiki.bambulab.com/material/%E5%90%8D%E7%89%872.png)

在 **“自定义”** 菜单中，输入卡片的尺寸： **① 宽度**和 **② 长度**。

系统会自动为每个尺寸增加 0.2 mm 的间隙，以确保尺寸合适并允许一定的打印误差。

接下来，指定 **③ X 方向的卡片数量**和 **④ Y 方向的卡片数量**，这决定了激光夹具上可以放置多少张卡片。

设置完成后，点击 **⑤ 生成**以应用所选参数并更新实时查看器中的模型。

单击模型可以查看其尺寸，并 **⑥ 确保其适合打印机**的打印大小。

确认模型显示正常后，点击 **⑦ 下载**导出文件。您可以选择 .3mf 或 STL 文件用于 Bambu Studio。

![名片3.png](https://wiki.bambulab.com/material/%E5%90%8D%E7%89%873.png)

将设计导入 Bambu Studio 后，进行基本设置：

1. **选择 3D 打印机型号**.
2. **选择打印板** 来匹配要打印的耗材。
3. 选择**耗材类型**和颜色。
4. **选择图层高度**较低的图层高度可以提供更多细节，但也会增加打印时间。
5. 点击**切片单盘**。

![名片4.png](https://wiki.bambulab.com/material/%E5%90%8D%E7%89%874.png)

切片后，点击**打印单盘**。  
![名片5.png](https://wiki.bambulab.com/material/%E5%90%8D%E7%89%875.png)

确认打印机和耗材，然后单击 **“发送”**。

![名片6.png](https://wiki.bambulab.com/material/%E5%90%8D%E7%89%876.png)

等待打印完成。

![3d_printing_process.jpg](https://wiki.bambulab.com/material/3d_printing_process.jpg)

### 步骤二. 安装激光模组以及激光垫板

安装激光模组以及激光垫板的详细教程请参考 [H2S 激光模组安装指南](../../h2s/manual/laser-module-lnstallation-guide.md)。

![laser_module_setting_up.png](https://wiki.bambulab.com/material/laser_module_setting_up.png)

安装完成后，启动校准过程。

### 步骤三. 放置激光雕刻材料

将要雕刻的名片放在打印好的激光夹具上。

![placing_the_material_to_engrave.jpg](https://wiki.bambulab.com/material/placing_the_material_to_engrave.jpg)

然后将夹具放在打印机内部的激光垫板上，如下图所示。最好尽可能靠在背面的校准卡槽处。

![placing_it_on_top_of_honeycomb.jpg](https://wiki.bambulab.com/material/placing_it_on_top_of_honeycomb.jpg)

### 步骤四. 准备激光雕刻设计图

打开 Bambu Suite， ① 创建一个新项目。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-17.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-17.png)

点击界面右侧的设备下拉菜单 ① ，然后点击 ② “连接打印机”。请注意，要提前在打印机上登录相同的账号，此处才会显示您的打印机。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-18.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-18.png)

机器连接成功后，右上侧会出现一个小图标，如图所示：

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-19.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-19.png)

点击左侧的 ① **“图片”** 按钮导入您的名片设计。建议使用矢量图，因为矢量图可以缩放而不损失细节。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-20.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-20.png)

然后在弹出的窗口选择 **“激光加工”**。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-21.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-21.png)

我们将添加两个拓竹 logo，一个设置为实心填充的效果，另一个设置为只有轮廓线的空心效果。

先在 **“工艺类型”** 的下拉菜单中，为这两个 logo 配色分组。通过设置不同的颜色，可以为指定 logo 进行分组，不同的组可以采用不同的激光工艺，例如切割、雕刻等。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-22.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-22.png)

对于红色组，在 ① **“工艺类型”** 菜单下选择 **“激光线”工艺**，然后选择 ② **“激光线条雕刻”**，即只有图案的外轮廓线会被雕刻。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-23.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-23.png)

左侧 logo 应用了“激光填充”功能，整个图案面会被雕刻；

右侧 logo 应用了“激光线条”功能，只有图案外轮廓线会被雕刻。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-24.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-24.png)

然后，点击 **① “材料组”选项**，**② 选择雕刻材料**。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-25.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-25.png)

我们将使用 ① **“黑色铝制名片”**。如果界面上没有这种材料，请点击 **② “更多材料”** 查看完整的材料库。

|  |  |
| --- | --- |
|  |  |

基本设置已完成，点击 ① **“准备制作”** 继续。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-26.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-26.png)

进入激光平台预览页面后，点击顶部工具栏中的 **① 拍照图标**，可以预览打印机内部的俯视实时画面。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-27.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-27.png)

在预览画面中，将图案设计拖动到所需位置。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-28.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-28.png)

在 ① **“厚度”** 部分，单击**下拉小图标**，然后选择 **“快速测量”**。打印机将进行厚度测量以设置激光高度。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-29.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-29.png)

一切准备就绪。开始之前，请检查： **① 设计是否正确， ② 机器是否已连接，③ 材料类型， ④ 激光工艺。**

在左下角可以找到 **⑤“参数”菜单**，在这里可以调整激光的速度和功率。此功能需要根据所选材料类型进行设置，仅推荐资深用户使用。

点击 **⑥ “预览”**，查看雕刻路径。

点击 **⑥ “制作”**，开始雕刻。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-30.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-30.png)

### 步骤五. 开始激光雕刻

点击 **“制作”** 后，屏幕会提示您进行雕刻前的检查，请仔细按照提示操作。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-32.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-32.png)

您还可以在 Bambu Studio 中监控任务状态。

![how_to_use_laser_jigs_for_batch_engraving-chinese-image-33.png](https://wiki.bambulab.com/material/how_to_use_laser_jigs_for_batch_engraving-chinese-image-33.png)

> ❗ **注意：** 任务启动后，请勿打开前门或顶盖。

您可以在打印机屏幕上监控机腔内的雕刻进度。雕刻过程中，建议实时监控任务，不用离开打印机。

![](https://wiki.bambulab.com/material/laser_engraving_progress.jpg)

**❗ 雕刻完成后，请勿立即打开前门或顶盖。❗**

等待排气系统清除烟雾、内部空气净化完毕后，屏幕将显示提示信息。此时即可打开前门取出卡片！

![](https://wiki.bambulab.com/material/completed_design.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
