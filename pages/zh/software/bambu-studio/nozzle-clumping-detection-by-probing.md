---
path: zh/software/bambu-studio/nozzle-clumping-detection-by-probing
title: "Bambu Studio 触碰裹头检测功能"
description: "本文介绍了 Bambu Studio 中的触碰裹头检测功能"
tags: []
created: 2025-08-04T03:16:04.272Z
updated: 2026-06-09T01:32:10.350Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/nozzle-clumping-detection-by-probing
---

## 为什么需要触碰裹头检测？

**裹头**是指打印过程中，耗材因未牢固粘附在构建板或其他原因导致挤出喷嘴被包裹的现象。这种情况不仅会导致打印失败，还可能损坏打印机部件（如下图所示）。

由于裹头可能对设备造成损害，Bambu Lab 某些系列打印机配备了裹头检测功能。当检测到喷嘴被耗材包裹时，打印机会自动暂停并发出提醒，以减少进一步损坏的风险。

![h2d_裹头.png](https://wiki.bambulab.com/h2/manual/h2d-intro/h2d_%E8%A3%B9%E5%A4%B4.png)

虽然 H2D 打印机配备了 AI 视觉裹头检测功能（详见 [H2D智能检测介绍](../../h2/manual/intelligent-detection.md)），但在打印高温材料（尤其是前几层）时，由于工具头较为靠近热床，喷嘴摄像头周围温度可能超过 85℃，导致检测功能自动关闭，可能影响裹头识别的准确性，所以我们也建议您在 Bambu Studio 中**开启触碰裹头检测功能**。

## 适用机型 & 固件版本

> 注意：该功能在各机型上所要求的 Bambu Studio 适配版本不同，请确保您已将其升级至最新版。

- **H2D：** 01.01.30.00 Public Beta 或更高版本
- **H2D Pro：** 01.01.00.00 或更高版本
- **H2S：** 01.01.60.00 Public Beta 或更高版本
- **H2C：** 全固件支持
- **P2S：** 01.01.00.00 或更高版本
- **X2D：** 01.01.00.00 或更高版本
- **A 系列：** 裹头检测无需在 Bambu Studio 中开启，请在屏幕上点击**设置——打印选项**开启，详情请参考：[A1系列裹头检测功能介绍](../../a1-mini/manual/nozzle-warp-detection.md) 或 [A2L 裹头检测介绍](../../a2l/manual/nozzle-clumping-detection.md)

## 检测原理与执行方式

在打印至**第 4、11、20 层**时，工具头会在当前层打印开始移动至热床后方，执行以下检测流程：

1. **喷嘴下探：** 热床向上移动，然后工具头向右移动，做出一个类似喷嘴下探的动作进行触碰检测；
2. **碰撞检测：**

- 若喷嘴被耗材包裹（裹头），下探时可能触碰到热床，涡流传感器会检测到碰撞，判定为裹头，打印自动暂停并提醒用户；
- 若未检测到碰撞，则判定为无裹头，继续正常打印。

### **H2D**

H2D 打印机触碰裹头检测动作如下动图所示：

![444.gif](https://wiki.bambulab.com/h2/manual/h2d-intro/444.gif)

### **H2S**

H2S 打印机触碰裹头检测动作如下动图所示：

![h2s触碰裹头.webp](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/h2s%E8%A7%A6%E7%A2%B0%E8%A3%B9%E5%A4%B4.webp)

### **P2S**

P2S 打印机触碰裹头检测位置为擦嘴片螺丝孔位置，检测动作如下动图所示：

![触碰裹头检测校准2.webp](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/%E8%A7%A6%E7%A2%B0%E8%A3%B9%E5%A4%B4%E6%A3%80%E6%B5%8B%E6%A0%A1%E5%87%862.webp)

### **X2D**

X2D 打印机触碰裹头检测动作如下动图所示：

![nozzle_clumping_detection_by_probing6.gif](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/nozzle_clumping_detection_by_probing6.gif)

**触碰裹头检测校准**

建议在以下两种情况开启校准：

1. 由于 P2S 裹头检测位置位于热床后方擦嘴片的螺丝孔内，因此**拆装或调整热床后必须重新校准**，否则可能导致检测不准确；
2. 若观察到无裹头，但喷嘴未在正确位置触碰导致误触发裹头检测报错时，也需执行一次校准。

**开启校准：**请点击屏幕的**设置 > 校准 > 打印校准 > 触碰裹头检测校准**进行校准。

![image_-_2025-10-12t171959.506.png](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/image_-_2025-10-12t171959.506.png)

**校准步骤：**校准过程中，工具头会先移动到擦嘴片位置清洁喷嘴，然后在擦嘴片螺丝孔位置校准，确定螺丝孔位置，用于后续裹头检测。

![触碰裹头检测校准.webp](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/%E8%A7%A6%E7%A2%B0%E8%A3%B9%E5%A4%B4%E6%A3%80%E6%B5%8B%E6%A0%A1%E5%87%86.webp)

## 功能设置

### 开启/关闭方式

您可以在 Bambu Studio 的**工艺——全局——其他——高级**中开启和关闭“**开启触碰裹头检测**”，**该功能需要手动开启。**

![打开触碰裹头检测.jpg](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/%E6%89%93%E5%BC%80%E8%A7%A6%E7%A2%B0%E8%A3%B9%E5%A4%B4%E6%A3%80%E6%B5%8B.jpg)

> 说明：在 Bambu Studio 中，“**触碰裹头检测**”默认关闭，如需使用，需在每次打印任务前的切片设置中手动开启。

### 擦料塔设置

由于检测过程中喷嘴可能漏料，系统会自动生成擦拭塔以吸收渗漏耗材，避免模型表面出现瑕疵。

![新擦料塔.jpg](https://wiki.bambulab.com/h2/manual/h2d-intro/%E6%96%B0%E6%93%A6%E6%96%99%E5%A1%94.jpg)

#### 擦拭塔生成规则

- **单色打印：**

  - 额外生成 20 层高的擦拭塔。
  - 若模型总层数不足 20 层，擦拭塔高度与模型高度一致。
- **多色打印：**

  - 若现有擦拭塔高度 ≥ 20 层，保持原结构。
  - 若擦拭塔不足 20 层但模型高度≥ 20 层，自动补足擦拭塔至 20 层。
  - 若模型总层数不足 20 层，擦拭塔高度与模型高度一致。

#### 关闭擦拭塔

如需禁用擦拭塔，可在 **工艺 —— 擦拭塔** 中关闭，但可能导致检测层出现轻微瑕疵。

### 可打印区域限制

开启触碰裹头检测后，工具头需移动至热床后方执行检测，因此会占用部分打印空间，可打印区域的限制如下图所示。

|  |  |
| --- | --- |
| H2D | P2S |

## 功能失效的场景

### 多件逐件打印

当**盘上超过一个模型**，并启用**逐件打印**时，无法同时支持裹头检测功能，需关闭裹头检测或逐件打印才可以切片。

![逐件.jpg](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/%E9%80%90%E4%BB%B6.jpg)

### 启用旋转花瓶

当启用**旋转花瓶**功能后，会默认关闭裹头检测功能。

![旋转花瓶2.jpg](https://wiki.bambulab.com/software/bambu-studio/nozzle-clumping-detection-by-probing/%E6%97%8B%E8%BD%AC%E8%8A%B1%E7%93%B62.jpg)

### 打印 TPU 等柔性耗材

柔性耗材的裹头故障无法被触碰裹头检测识别，当您使用 TPU 耗材发起打印时，可使用 AI 视觉裹头检测功能（详见 [H2D智能检测介绍](../../h2/manual/intelligent-detection.md)）

## 建议和注意事项

- 若热端硅胶套未安装，裹的耗材不容易成型，有可能导致漏检，建议在打印前确保热端硅胶套已正确安装；

![注意事项.png](https://wiki.bambulab.com/h2/manual/h2d-intro/%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9.png)

- 建议插入 U 盘并开启录像功能（[开启录像功能和导出录像视频](../../x1/troubleshooting/enable-the-video-recording-function.md)），以便后续分析裹头成因（如首层粘附不良）。
- 定期清洁打印板（[Bambu Lab纹理PEI打印板质量与预期不符](../../general/textured-PEI-plate-not-working-as-expected.md)）可提升粘附性，减少裹头风险。
- 若未开启裹头检测或其他原因发生裹头，请参考 wiki 中裹头处理指引进行清理。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
