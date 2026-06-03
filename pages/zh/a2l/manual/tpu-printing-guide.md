---
path: zh/a2l/manual/tpu-printing-guide
title: "A2L TPU 打印指南"
description: "本指南介绍了如何在 A2L 上打印 TPU"
tags: []
created: 2026-06-01T13:02:28.530Z
updated: 2026-06-03T02:32:49.884Z
source: https://wiki.bambulab.com/zh/a2l/manual/tpu-printing-guide
---

## **前言**

TPU 85A、TPU 90A 及 TPU 95A HF 是不同硬度等级的热塑性聚氨酯（TPU）材料，硬度依次为：95A HF ＞ 90A ＞ 85A。该材料性能优异、应用广泛，不同硬度可满足多样化场景的使用需求。本文将介绍 A2L 使用 AMS HT 打印 TPU 90A 的详细步骤。

## 耗材存储

TPU 容易吸湿，受潮会影响打印质量。为了避免这种情况，建议：

- 将料盘存放在湿度低于 20% RH 的环境中；
- 使用收纳盒进行存放；
- 在收纳盒内放置干燥剂。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/017.png)

## 视频指南

## 打印前准备

### 烘干耗材

TPU 具有较强的吸湿性，在自然环境中容易吸收水分。若含有水分的 TPU 直接用于 3D 打印，打印过程中水分受热会迅速汽化，从而在打印制品中形成气泡、空洞等缺陷严重影响打印质量，甚至可能导致打印失败。因此我们推荐您使用下述设备及参数进行烘干。详情请参考[耗材准备——干燥](../../filament-acc/filament/dry-filament.md)。

- **鼓风式烤箱**：70 ℃ x 8 h
- **AMS HT**: 75 ℃ x 18 h

### 硬件兼容性

与刚性材料相比，TPU 对打印机硬件的要求更高。下表列出了不同类型 TPU 在 A2L 上的硬件兼容情况，供您在打印前参考。

| **硬件** | **TPU 90A** | **TPU 95A HF** | **TPU for AMS** |
| --- | --- | --- | --- |
| **热端** | 推荐：0.4/0.6/0.8mm 不支持：0.2mm 不推荐：高流量 | 推荐：0.4/0.6/0.8mm 不支持：0.2mm/高流量 | 推荐：0.4/0.6/0.8mm 不支持：0.2mm/高流量 |
| **AMS** | 仅兼容 AMS HT | 仅兼容 AMS HT | 全系列 AMS 兼容 |

### 耗材装载

- **AMS HT：**如果有 AMS HT，建议使用其 TPU 专用出料口进行送料。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/015.png)

为降低进料阻力并保证出料顺畅，建议将①出料口设置在高于②挤出机进料口的位置，可使用专用料架（[推荐模型](https://makerworld.com.cn/zh/models/983129#profileId-1004263)）抬高 AMS HT，并将其放置在打印机侧边。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/002.png)

- **5.8 L 料桶：**如果没有 AMS HT，建议使用 **5.8 L 料桶**进行进料，并搭配料桶支架（[推荐模型](https://makerworld.com.cn/zh/models/437644-5-8lgan-zao-xiang?from=search#profileId-2360379)），以确保耗材在出料过程中能够顺畅转动。使用料桶进料时，建议从**侧边开口**出料，以降低进料阻力。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/019.gif)

## TPU 打印步骤

### 进料

> 由于 TPU 材料具有高柔性和高黏性，因此打印过程中应降低进料阻力；若进料阻力过大（如料管过长），极易导致挤出齿轮打滑、磨损耗材，甚至造成供料中断。

- 移除连接在工具头端的料管，并确保挤出机内无其他耗材；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/003.png)

- 将一段约 50 mm 长的料管穿过 TPU 专用出料口；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/011.png)

- 放入 TPU 耗材；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/010.png)

- 再将耗材从 AMS HT 内部送入料管，并从料管另一端拉出；

|  |  |
| --- | --- |
|  |  |

- 将 AMS HT 放在支架上；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/009.png)

- 在打印机屏幕点击“控制 > 喷嘴”，输入 250 ℃ 后点击 “确定” ；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/007.jpg)

- 待热端升温完成后，将耗材从 AMS HT 中拉出并插入挤出机进料口，持续向前推送，直至感受到明显阻力；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/008.jpg)

- 多次点击挤出机的 **“向下箭头”** 进料，直到耗材连续顺畅挤出。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/020.webp)

> **📌 TPU 90A 进料方式注意事项：**
>
> - 从工具头进料过程中，若发现进料有明显阻力，请检查 AMS HT 内耗材转动是否流畅。
> - 当挤出机齿轮已经咬合住 TPU 耗材之后，慢慢点击挤出按钮，确保耗材从热端顺利挤出，避免进料失败。

### 设置打印参数

- **降低喷嘴温度：**由于 TPU 具有较强的流动性，在喷嘴温度较高时更容易出现拉丝、渗料或喷嘴溢出现象。为减少这类问题，建议在原有打印温度基础上适当下调 **5 ℃**。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/006.jpg)

- **降低打印速度：**较低的打印速度有助于耗材在热端内更充分地熔融，从而提高出料稳定性，并降低打印过程中出现缺料的概率。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/004.png)

### **退料**

> 注意：A 系列机型都需要升温后进行手动退料，不支持用切刀自动退料。

- 在打印机屏幕点击“控制 > 喷嘴”，输入 250 ℃ 后点击 “确定” ；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/005.jpg)

- 待热端升温完成后，缓慢点击挤出机 **“向上箭头”** ，跟随齿轮回转将耗材轻轻拉出工具头。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/021.webp)

- 退料后请及时剪除耗材末端的熔融部分，以免在下次打印时影响进料顺畅性。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/tpu-printing-guide/001.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
