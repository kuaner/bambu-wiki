---
path: zh/filament-acc/filament/h2d-filament-config-limit
title: "H2D/H2C 3D 打印材料混打指南"
description: ""
tags: []
created: 2025-04-01T12:19:53.723Z
updated: 2026-05-12T06:39:02.492Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/h2d-filament-config-limit
---

本指南为您详细介绍 H2D/H2C 设备使用不同耗材进行多材料打印的相关规范与注意事项。打印前，建议您查阅各耗材对应的 Wiki 页面，以获取更详尽的信息。

## 核心打印指南链接

- [H2D 软硬材料混打指南](../../h2/manual/soft-and-hard-filament-multi-material-printing-guide.md)
- [PLA Basic 与 PETG HF 互相支撑打印指南](h2d-pla-and-petg-mutual-support.md)

## 重要打印禁忌

### 1. PVA 与 PETG 不可通过左右热端同时打印

由于 PVA 的热变形温度相对较低，当热床温度设置为 70°C 以打印 PETG 时，若同时使用两个热端进行打印，极易导致喷嘴堵塞。

#### 💡 说明:

- 此处"同时打印"指使用左热端打印 PVA，使用右热端打印 PETG（或左热端使用 PETG，右热端使用 PVA）;
- 若使用 AMS 系统，可通过仅使用右热端打印 PETG，并将 PVA 作为支撑耗材；
- **请勿在左热端上使用 PVA 支撑 PETG。**

### 2. 不可混合打印温度差异过大的耗材

基于 Bambu Lab 的大量实测数据，为确保耗材在打印机内部不发生软化、变形，保障设备稳定运行，H2D/H2C 设备的耗材按温度需求划分为以下三类：

| 耗材类型 | 特性 | 常见类型 |
| --- | --- | --- |
| **高温耗材** | 需采用尽可能高的腔体温度打印，以此保障充足的层间结合强度，同时有效控制收缩率等关键打印质量参数。 | ABS、ASA、ASA-CF、PC、PA、PA-CF、PA-GF、PA6-CF、PET-CF、PPS、PPS-CF、PPA-CF、PPA-GF、ABS-GF、ASA-Aero |
| **中温耗材** | 具备优异的耐温特性，无需开启腔体加热即可实现优质的打印效果。 | HIPS、PE、PP、EVA、PE-CF、PP-CF、PP-GF、PHA |
| **低温耗材** | 热变形温度较低，当腔体温度高于 45℃时，耗材易在挤出机或热端内软化变形，进而引发堵塞风险，因此**严禁**在高温腔体环境下使用。 | PLA、PETG、PETG-CF、TPU、TPU-AMS、PLA-CF、PLA-AERO、PVA、BVOH、PCTG |
| **📌第三方耗材适配建议**：  非官方耗材因配方差异，同类基材的热变形温度可能存在显著不同，建议通过以下方式判定使用类型：  - 标准判定：参考 ISO 75 标准（1.8MPa 负载下），若耗材热变形温度低于 80℃，推荐按低温耗材规范使用； - 厂商咨询：直接联系耗材供应商获取官方分类建议，确保打印兼容性达到最佳状态。 | | |

#### 🔥 高、中、低温耗材打印提示：

- 高温料和低温料不能一起打印，Bambu Studio 切片时，也对这点进行了限制，禁止高温料和低温料混合切片。
- 高温料和中温料一起打印时，由于中温料可能会因为软化，增加挤出机和喷嘴堵塞损坏和堵塞的可能。在打印中建议谨慎的调整腔温，避免在打印的过程中由于耗材软化而导致堵塞。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
