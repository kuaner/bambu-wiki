---
path: zh/h2/manual/soft-and-hard-filament-multi-material-printing-guide
title: "H2D 软硬材料混打指南"
description: "本文介绍如何使用 H2D 进行软硬材料混打"
tags: []
created: 2025-03-26T11:53:35.185Z
updated: 2025-03-27T06:18:06.991Z
source: https://wiki.bambulab.com/zh/h2/manual/soft-and-hard-filament-multi-material-printing-guide
---

## 1. 前言

H2D 机型支持硬料线（左热端）以及 TPU 料线（右热端）一起打印，可以实现软硬材料混打。为了优化软硬料混打体验在 H2D 上推出了两项新功能来帮助用户更好地将 TPU 和硬质材料结合在打印件上。

![Studio 互锁梁](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-10.png)

![高低温材料混打](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/img_v3_02ju_f7ebd7f1-b71a-4aae-98cd-531cb38ea6cg-1.jpg)

## 2. 适用机型，配件以及耗材

![multi-filament-zh.png](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide-en/multi-filament-zh.png)

## 3. Studio 梁联锁功能

为了提升软硬材料的结合强度，Bambu Studio 中预设有 “使用梁联锁” 选项（切片选项以及互锁结构如下图所示）该功能将增强两种不同材料之间界面的连接，这将提升软硬混打模型的应用价值。

### 3.1 操作流程

**以 PETG-CF 以及 TPU 95A HF 为例，说明如何进行互锁结构打印**

1. 进料：PETG-CF 从左热端进料，TPU 95A HF 从右热端进料。

注：当热床温度高于 80℃ 时，需取下上盖玻璃。

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image.png)

2. 切片设置：开启 “使用梁联锁” 选项，根据实际模型需要修改相关参数，并确认腔温已关闭。

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-2.png)

3. 支撑主体材料设定为硬质材料后即可发起打印（模型需要支撑的情况下）。

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-4.png)

## 4. 高低温材料混打 (实验性功能)

前言：

在持续拓展 H2D 性能边界的征程中，我们开发这项功能，旨在赋予创造者更强有力的工具，充分释放每一次打印背后潜藏的无限可能。借助该功能，用户能够在同一打印件上，巧妙融合柔软的 TPU 与性能可靠的工程耗材，达成前所未有的卓越产品效果。TPU 和工程材料结合的打印方式在众多领域都有着不可估量的应用潜力。比如在工业设计领域，能够直接打印出软硬结合的零部件模型，为产品研发提供更真实的参考。

不过，需要特别提醒的是，为了打印机顺利地将您的创造力变为产品，使用该功能时请务必严格遵循我们提供的教程指导进行操作。如果操作不当，很可能会对打印机造成损坏，影响您的正常使用和后续体验。

您可以继续阅读来了解详细步骤：

### 4.1 耗材准备

强烈推荐使用 Bambu Lab 官方耗材，以保障打印效果和设备安全。鉴于打印过程中的高温会致使耗材软化，所以目前**本功能仅支持 [TPU 95A HF](https://asia.store.bambulab.com/products/tpu-95a-hf) 材料**。且打印软质耗材仅限在右热端进行打印。

**若您打算使用第三方耗材，务必仔细阅读其说明书并咨询厂商是否支持该功能，请确认无误后使用。**

此外，所使用的 TPU 耗材必须在打印前进行烘干处理。若未烘干，打印过程中极有可能出现阻塞问题，进而导致打印任务无法顺利完成。我们推荐使用 AMS HT，使用时设置温度为 75 ℃ 烘干时长为 18 小时。倘若您的耗材受潮情况较为严重，可根据实际状况酌情调整烘干参数，以优化烘干效果，确保耗材处于最佳打印状态。

您可以参考下面的 Wiki 来了解耗材烘干以及 TPU 的打印指南：

[烘干耗材](../../filament-acc/filament/dry-filament.md)

[TPU 打印建议](../h2d-tpu-printing-guide.md)

加载耗材时，推荐使用 AMS HT 或料桶作为耗材的存储容器。如果您采用的存储方式使得 TPU 在进料过程中，挤出机需要施加过大的拖拽力，就会导致 TPU 不出料，进而出现空打现象，最终导致打印失败。因此，请务必确保在送料链路上尽可能减少送料阻力，比如避免使用过长的 PTFE 管和保证料盘转动顺畅，不出现卡顿情况。

### 4.2 基于模型的打印模式选择

⛔**打印模型限制：**

如果您的模型首层均由 TPU 组成或 TPU 作为模型主要承载结构，请选择低腔温打印切片。在热床温度设置中，请注意以下：

- 请勿修改 TPU 的热床温度；
- 将工程耗材的热床温度设置为 70℃ 以下，避免模型结构主体在模型自身重力下导致的变形。

![首层均为 TPU 的模型](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-6.png)

![TPU 作为结构承载主体的模型](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-8.png)

**打印模式选择**

在模型打印设置的选择上，若您的模型**大部分使用 TPU 进行打印**，并且**期望较高的打印成功率**，推荐进行低腔温打印。低腔温环境能较好地适应 TPU 材料特性，减少打印过程中的异常状况。此外如果您的模型中与热床连接的部分均由 TPU 组成，请修改工程耗材温度热床至 70℃ 以下。

而如果您希望充分释放工程材料的强度特性，追求打印成品的高强度表现，则可以选择高腔温打印。不过，高腔温打印对耗材和设备有更严格要求，需要您的耗材充分干燥，并且该模式仅限使用外挂料盘加载的 TPU 95A HF，并且务必使用新热端或您专门用于 TPU 打印的热端进行 TPU 打印，以此保证打印效果和设备安全。

### 4.3 低腔温打印切片及其机器准备

#### 4.3.1 机器准备

在进行低腔温打印前，需要对打印机进行相应准备。

首先移除上盖玻璃，这样做是为了避免热床烘烤致使腔温上升，具体移除步骤可参考下图：

![移除上盖_00_00_00-00_00_30.gif](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/%E7%A7%BB%E9%99%A4%E4%B8%8A%E7%9B%96_00_00_00-00_00_30.gif)

高温的打印板会与 TPU 产生十分强烈的粘接，打印前，务必在打印板涂满胶水，以此保护打印板。**若未涂胶，可能会出现如下图所示的损坏情况。**

![未提前涂胶在取下模型时候损坏打印板情况](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/img_v3_02jr_d9a1d52d-7032-4b9e-be57-397b22d18d9g.jpg)

您可以参考这篇 Wiki 来了解涂胶的详细步骤：<https://wiki.bambulab.com/zh/general/how-to-use-bbl-liquid-glue>

> 请务必确认在打印前已完成打印板的涂胶工作。如果您不幸忘记涂胶，**请使用酒精浸润模型与打印板粘接的地方，缓慢取下即可**。

#### 4.3.2 切片设置示例以及步骤

设置流程：

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/diagram.png)

[该部分设置好的 3MF ]：

[Low chamber temperature TPU 95A HF PAHT-CF.3mf](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide-en/low_chamber_temperature_tpu_95a_hf_paht-cf.3mf)

1. **在 Bambu Studio 中左上角的位置进入偏好设置。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-12.png)

2. **在偏好设置中勾选如图选项。注意！在勾选次选项前请确认您已知悉高低温混打的风险并且仔细阅读了本篇文档。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-14.png)

3. **调整工程耗材的设置。以 PAHT-CF 为例，首先设置腔体温度为 0℃。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-16.png)

4. **修改高级里面的起始 G-code，删除 “M145 P1 ; set airduct mode to heating mode” 。下图为删除后的状态**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-18.png)

5. **记录工程材料所使用的打印板温度，如 PAHT-CF 为 100℃ 。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-20.png)

6. **在 TPU 的耗材设置中，修改打印板温度至工程材料所需要打印板温度：**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-22.png)

> **注意：如果您的模型满足限制（即首层均由 TPU 组成或 TPU 作为模型主要承载结构）, 则请勿修改 TPU 的热床温，反而需要将工程耗材床温修改至不超过 70℃ 。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-24.png)

7. **修改 TPU 95A HF 的体积流量至 3.6 mm³/s。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-26.png)

8. **最后切片执行打印即可**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-28.png)

### 4.4 高腔温打印切片及其机器准备

#### 4.4.1 机器准备

高温的打印板会与 TPU 产生十分强烈的粘接，打印前，务必在打印板涂满胶水，以此保护打印板。**若未涂胶，可能会出现如下图所示的损坏情况。**

![未提前涂胶在取下模型时候损坏打印板情况](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/img_v3_02jr_d9a1d52d-7032-4b9e-be57-397b22d18d9g-1.jpg)

涂胶操作可参考您可以参考这篇 Wiki 来了解涂胶的详细步骤：<https://wiki.bambulab.com/zh/general/how-to-use-bbl-liquid-glue>

> 请务必确认在打印前已完成打印板的涂胶工作。如果您不幸忘记涂胶，**请使用酒精浸润模型与打印板粘接的地方，缓慢取下即可**。

#### 4.4.2 切片设置示例以及步骤

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/diagram-1.png)

[该部分设置好的 3MF ]：

[High chamber temperature TPU 95A HF PAHT-CF.3mf](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide-en/high_chamber_temperature_tpu_95a_hf_paht-cf.3mf)

1. **在 Bambu Studio 中左上角的位置进入偏好设置。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-30.png)

2. **在偏好设置中勾选如图选项。**

> **注意！在勾选次选项前请确认您已知悉高低温混打的风险并且仔细阅读了本篇文档。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-32.png)

3. **在 TPU 95A HF 的耗材设置中，修改打印板温度至工程材料所需要打印板温度。**

**注意：如果您的模型满足限制（即首层均由 TPU 组成或 TPU 作为模型主要承载结构） , 则请勿修改 TPU 床温，反而需要将工程耗材床温修改至 70℃ 以下。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-34.png)

4. **删除下列信息：**

**TPU 95A HF 耗材信息 -> 高级 -> 耗材起始G-code中下面两行的信息。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-36.png)

5. **TPU 95A HF 的体积流量改至 3.6 mm³/s。**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-38.png)

6. **最后切片执行打印即可**

![](https://wiki.bambulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide/image-40.png)

7. **打印完成后，若想进行 TPU 退料操作，请等待腔温下降至 45℃ 以下再进行退料操作。**

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
