---
path: zh/software/bambu-studio/parameter/elephant-foot
title: "象脚补偿"
description: "本文介绍了象脚以及如何在 Bambu Studio 中设置象脚补偿。"
tags: []
created: 2023-12-03T14:32:20.249Z
updated: 2026-08-14T03:28:50.406Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/elephant-foot
---

## 象脚

象脚是 FDM 3D 打印中常见的首层外扩现象：模型底部（通常是第 1 层，有时是最初几层）比上层更宽，形成一圈类似象脚的凸边。

FDM 3D 打印通过喷嘴挤出材料，逐层堆叠构建出 3D 模型。在打印过程中，首层会同时受到多重作用：

- **底部受热**：首层被压在加热的热床上，尚未完全冷却、仍处于软化状态，更容易变形。
- **上层重量**：后续层继续下压尚未完全定型的底部。模型越大、底座越宽，象脚通常越明显。

在两者共同作用下，**首层可能会向外扩展，形成一圈明显的凸出边沿，这种现象就称为象脚。**

多数外观件上，轻微象脚可以忽略。但装配件、卡扣、滑轨、轴孔等对公差敏感的模型，底部凸边会直接影响装配。首层象脚凸出较大时，配合流畅度会下降，甚至无法正常安装。

|  |  |
| --- | --- |
|  |  |
| **象脚示意图 1** | **象脚示意图 2** |

---

## 象脚补偿

象脚补偿是 Bambu Studio 中用于抵消首层外扩的参数。具体来讲，使用象脚补偿参数后，软件会**主动内缩第一层轮廓**，使实际打印出的首层与上层平齐，从而减少后续打磨工作。

打印对精度要求不高的一般模型时，使用系统默认数值即可。若要打印对精度要求高的模型，请继续阅读下一章节。

**设置路径**：进入「**工艺 → 质量 → 精度 → 象脚补偿**」即可设置。

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/compensation-setting-path.png)

下图为启用象脚补偿前后的切片对比：

|  |  |
| --- | --- |
|  |  |
| **未启用象脚补偿** | **象脚补偿 `0.3 mm`** |

## 象脚补偿值计算

若要打印对精度要求高、对公差敏感的模型，如装配件、卡扣、滑轨、轴孔等，请根据本章节步骤，打印测试模型，测量与计算象脚补偿值后，将参数应用于所要打印的模型。

### 1. 准备工作

- 打印前，使用温水和洗洁精清洗打印板，具体步骤详见这篇 wiki：[**打印板清洁指南**](../../../filament-acc/acc/pei-plate-clean-guide.md) 。

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/clean-build-plate.webp)

- 执行一次完整的**自动热床调平**及**动态流量校准**。具体请参考下方步骤：

  1. 在打印机屏幕上，进入“**设置**”——“**校准**”——“**打印校准**” ，勾选“**自动热床调平**”选项，并点击“开始”，如下图。
  2. 请参考这篇 wiki：[**动态流量校准**](../calibration_pa.md)，执行动态流量校准。

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/auto-bed-leveling.png)

### 2. 打印测试模型

**步骤 1. 选择并准备测试模型**

我们提供了两种测试模型，请选择其中一个打印即可。本教程以模型二为示例进行测试，模型一的测试方法一致。

🔽 模型一：Bambu Studio 自带的立方体模型

![test-model-1-cube.jpg](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/test-model-1-cube.jpg)

**设置步骤**：在 Bambu Studio 中，右击打印板，选择「**添加标准模型 → 立方体**」，点击立方体，选择「**缩放**」，取消「**等比例缩放**」，设置大小为  **`25 × 25 × 10 mm`**

|  |  |
| --- | --- |
|  |  |

🔽 模型二：象脚特征测量块

下载测试模型文件，并在 Bambu Studio 打开：[**点击下载.stl**](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/%E8%B1%A1%E8%84%9A%E8%A1%A5%E5%81%BF%E6%B5%8B%E8%AF%95%E4%BB%B6_partbody.stl)

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/test-model-2-gauge-block.jpg)

**步骤 2. 完成以下参数设置**

- 进入「**工艺 → 质量 → 精度 → 象脚补偿**」，参数修改为 **`0`**

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/set-compensation-to-0.png)

- 进入「**工艺 → 其他 → Brim 类型**」，修改为 **`无 brim`**

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/set-brim-type-none.png)

**步骤 3. 发起打印任务，等待打印完成**

> ⚠️ **注意**：打印完成后，**待热床完全冷却至室温**后再取下模型，避免强行剥离导致形变

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/printed-test-model.jpg)

### 3. 测量与计算

**所需工具**：精度不低于 0.01 mm 的游标卡尺或千分尺

**测量须知**：

- 模型四个边角可能受动态流量影响，因此测量时应**避开**模型四个边角，选取每条边的**中间段**测量。
- 象脚位于模型首层。测量底面时，卡尺**轻触**首层凸出的边缘即可；用力过大会使首层变形，导致读数偏小。

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/measure-notes.jpg)

**测量步骤**：

1. **基准尺寸测量**：测量模型顶部（非象脚区域）在 X 轴与 Y 轴方向上的实际尺寸，并记录数据；

|  |  |
| --- | --- |
|  |  |
| X 轴 | Y 轴 |

2. **象脚尺寸测量**：测量模型底部、贴打印板面，在 X 轴与 Y 轴方向上的尺寸，并记录数据。

|  |  |
| --- | --- |
|  |  |
| X 轴 | Y 轴 |

**计算象脚补偿值：**

将测量结果代入下方公式，计算象脚补偿值。

- X 轴象脚偏差：**象脚尺寸X－基准尺寸X=X偏差值**
- Y 轴象脚偏差：**象脚尺寸Y－基准尺寸Y=Y偏差值**
- 象脚补偿值：**（X偏差值+Y偏差值）/2=象脚补偿值**

**示例**：

- X 轴象脚偏差：25.07-24.98=0.09
- Y 轴象脚偏差：25.11-25.00=0.11
- 象脚补偿值：**（0.09+0.11）/2=0.10**

最后，即可将测得的**象脚补偿值**应用于需高精度打印的装配模型上。

设置路径：「**工艺 → 质量 → 精度 → 象脚补偿**」，输入**象脚补偿值。**

> ⚠️ **注意**：不同类型打印板的象脚补偿值会有一定的变化，因此无法彼此通用，建议更换打印板后重新测量计算象脚补偿值。

![](https://wiki.bambulab.com/software/bambu-studio/parameter/elephant-foot/apply-compensation-value.png)

## 说明

启用象脚补偿后，Brim 在预览中可能无法与模型完全贴合，这属于正常现象。象脚补偿会内缩首层，预览不会模拟真实打印时首层被压扁外扩。实际打印中，这圈缝通常会被压扁的材料填上。

若「Brim 与模型的间隙」已设为 0 mm，预览里仍有缝，多半是象脚补偿导致的。若希望预览里 Brim 与模型完全贴合，可设置象脚补偿为 0。

> **ℹ️ 什么是 Brim（裙边）：** Brim 是在模型首层四周额外打印的一圈扁平轮廓，像帽檐一样与模型底部相连。它能增大模型与打印板的接触面积，提升附着力。更多说明见 [**Brim 介绍**](../auto-brim.md)。

|  |  |
| --- | --- |
|  |  |
| **启用象脚补偿** | **关闭象脚补偿** |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
