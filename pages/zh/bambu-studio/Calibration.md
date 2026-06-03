---
path: zh/bambu-studio/Calibration
title: "第三方打印机校准"
description: "介绍如何在 Bambu Studio 中校准第三方打印机。"
tags: ["bambu studio"]
created: 2024-09-24T07:11:17.258Z
updated: 2026-05-25T09:47:25.506Z
source: https://wiki.bambulab.com/zh/bambu-studio/Calibration
---

本文主要介绍如何在 Bambu Studio 中选择第三方打印机时执行一系列校准，**内容为进阶用户设计，初学者不建议使用。**

部分内容灵感来自 [Orca Slicer](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration)，感谢 Orca！

> **注意**：
>
> - 需提前创建自定义打印机或喷嘴，详情请参考 [此wiki](../software/bambu-studio/3rd-party-printer-profile.md)。
> - 完成校准过程后，请创建一个新项目以退出校准模式。

### 🛠️ 如何启用开发者模式

启用开发者模式对于解锁本页介绍的校准功能至关重要。

启用开发者模式——点击此处展开逐步说明

**Step 1 - 进入偏好设置**  
点击顶部导航栏中的菜单选择偏好设置，或使用快捷键 Ctrl+P。

## s1.jpg

**Step 2 - 启用开发者模式**  
在偏好设置中，下拉找到开发者模式，勾选该功能。

![s1.jpg](https://wiki.bambulab.com/software/bambu-studio/dev-mode/s2.jpg)

---

**Step 4 - 校准选项会立即显示**  
勾选后将能够在软件顶部点击“校准”。

![s1.jpg](https://wiki.bambulab.com/software/bambu-studio/dev-mode/s3.jpg)

---

✅ 您可随时通过重复这些步骤来关闭它。

## 温度塔

![动画_温度塔.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_%E6%B8%A9%E5%BA%A6%E5%A1%94.apng)

温度塔是用于测试打印机打印温度的模型，呈现为垂直塔状结构，内部包含多个区块，每个区块的打印温度各不相同。

在校准中选择温度塔模型打印。打印完成后，通过对塔内每个区块的检查，可以确定该耗材的最佳打印温度，即打印质量最高且问题最少（如拉丝、层粘连、翘曲和桥接）的打印温度。

![温度塔.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E6%B8%A9%E5%BA%A6%E5%A1%94.jpg)

## 流量比例

关于 Bambu 官方打印机的流量比例校准以及流量比例校准对打印的影响，您可以参考 [流量比例校准](../software/bambu-studio/calibration_flow_rate.md) 查看更多相关信息。

### 粗略校准

![动画_通过1.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_%E9%80%9A%E8%BF%871.apng)

在校准菜单中选择**通过 1**，将创建一个由 9 个区块组成的模型，每个区块都有不同的流速修改器。打印完成后，检查每个区块顶面的光滑程度。以确定该耗材的最佳流量比例。

![流量比例通过1.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E6%B5%81%E9%87%8F%E6%AF%94%E4%BE%8B%E9%80%9A%E8%BF%871.jpg)

使用以下公式计算耗材设置中的流量比： `初始流量比 ×（100 + 修改器）/100`

例如，如果之前的流量比为 `0.98`，而最光滑区块的流量修改器为 `+5`，则新的流量比为：`0.98 x (100+5) / 100 = 1.029`

> **注意：切记将流量比例保存至耗材设置**

### 精确校准

![动画_通过2.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_%E9%80%9A%E8%BF%872.apng)

在校准菜单中选择**通过 2**，将创建一个由 10 个区块组成的模型，每个区块都有不同的流速修改器。此项目的流速修改器范围为 -9 至 0。

打印完成后，检查每个区块顶面的光滑程度。以确定该耗材的最佳流量比例。

![通过2.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E9%80%9A%E8%BF%872.jpg)

在此情况下，如果之前粗略校准后得出的流量比为 `1.029`，而最光滑区块的流量修改器为 `-6`，则新的流量比为：`1.029 x (100-6)/100 = 0.96726`

> **注意：切记将流量比例保存至耗材设置**

## 压力提前测试

### PA 塔

![动画_pa塔.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_pa%E5%A1%94.apng)

在压力提前测试中选择 PA 塔模型打印。打印完成后，可观察打印件的每个角，标出整体效果最佳的高度。

|  |  |
| --- | --- |
|  |  |

**在 PA 塔测试中，模型的高度每增加 1 毫米，模型的 PA 值增加 0.002。**

此测试中，整体效果最佳的高度为 15mm，因此 PA 值为 `0.002 x 15 = 0.03`

### PA 线

![动画_pa线.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_pa%E7%BA%BF.apng)

在压力测试中选择 PA 线模型打印。PA 线测试的准确性很大程度上取决于首层质量，**建议在测试时开启热床调平。**

打印完成后，可观察打印件上每条线的速度变化。选择最均匀线的值，并在耗材设置中更新 PA 值。

![pa_线.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/pa_%E7%BA%BF.jpg)

### PA 图案

![动画_pa图案.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_pa%E5%9B%BE%E6%A1%88.apng)

在压力测试中选择 PA 图案模型打印。打印完成后，可观察打印件的转角表现，选出挤出饱满但不过量的线，并在耗材设置中更新 PA 值。

在此测试中，耗材的最佳 PA 值是 0.03。

![pa_图案.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/pa_%E5%9B%BE%E6%A1%88.jpg)

## 回抽测试

回抽测试会自动生成一个回抽塔。回抽塔是一个带有多个凹槽的垂直结构，每个凹槽都以不同的回抽长度打印。

![动画_回抽.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_%E5%9B%9E%E6%8A%BD.apng)

在校准中选择回抽测试模型进行打印。打印完成后，注意图层从哪里开始失效，质量在哪里开始下降，以及打印件的光泽变化，以此确定产生最整洁塔身的最短回抽长度，即耗材的最佳回抽长度。

![20240925-103831.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/20240925-103831.jpg)

> **注意**：在**测试 PLA 或 ABS 等渗出极少的耗材**时，回抽塔可能从一开始就很干净。在此情况下，可以**将回抽长度设置为 0.2 毫米 - 0.4 毫米**。如果塔顶仍有大量拉丝，建议擦干耗材并确保喷嘴安装正确无泄漏。

## 最大流速

通用或第三方耗材可能没有在耗材中设置正确的流速。最大流速测试旨在校准特定耗材的最大流速。

![动画_最大流速.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_%E6%9C%80%E5%A4%A7%E6%B5%81%E9%80%9F.apng)

在校准中选择最大流速模型进行打印。打印完成后，观察图层从哪里开始失效，质量从哪里开始下降，以及打印件的光泽变化。

![最大流速.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E6%9C%80%E5%A4%A7%E6%B5%81%E9%80%9F.jpg)

使用以下方法确定耗材的最大流速：

- 使用卡尺或直尺测量该点的打印高度，并使用最大流速计算方法：  
  `起始值 +（测量高度 × 值步长）`  
  例如，起始流量速度为 `10`， 值步长为 `1`，打印质量在第 `14 毫米`处开始下降，因此最大流速为： `10 + (14 × 1) = 24`

![20240925-104824.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/20240925-104824.jpg)

- 返回**预览**界面，选择**流量**颜色方案。向下滚动到测量的层高 14 毫米，然后点击工具头滑块，将显示耗材的最大流速为 24。

![screenshot-20240925-110749.png](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/screenshot-20240925-110749.png)

> **注意**：可以保守地将流量降低 5-10%，以确保打印质量。

## VFA

![动画_vfa.apng](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/%E5%8A%A8%E7%94%BB_vfa.apng)

VFA (Vertical Fined Artifacts) 即电机连续运动振纹，与耗材条件、打印速度和挤出校准等因素有关。VFA 校准用于测试打印机在不同打印速度下，VFA 振纹的明显程度。

![vfa.jpg](https://wiki.bambulab.com/bambu-studio/3rd-party-printer-calibration/vfa.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
