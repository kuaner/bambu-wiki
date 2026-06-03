---
path: zh/filament-acc/filament/h2d-pla-and-petg-mutual-support
title: "PLA Basic 与 PETG HF、PETG Basic 互相支撑打印指南"
description: "本文介绍了如何使用拓竹耗材 PLA Basic 与 PETG HF / PETG Basic 互相支撑打印，并提供了在 Bambu Studio 中设置参数的教程及预设参数文件的下载链接。"
tags: ["petg hf"]
created: 2024-08-02T02:11:38.792Z
updated: 2026-05-20T06:49:56.431Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/h2d-pla-and-petg-mutual-support
---

拓竹耗材 PLA Basic 和 PETG HF / PETG Basic 之间的粘附力不强，使用这两种耗材的组合可获得更好的支撑界面效果，也能使支撑更容易移除。

## 注意事项

1. 本指南仅适用于拓竹 PLA Basic 和 拓竹 PETG HF、拓竹 PETG Basic 这三款耗材，**不适用**下列其他类型的 PLA 和 PETG：
   - PLA Matte、PLA Silk、PLA-CF 等其他类型的 PLA
   - PETG Translucent、PETG-CF 等其他类型的 PETG
   - 其他品牌的 PLA 或 PETG
2. 请务必按照本指南提供的参数和配置进行打印。否则，无法保证打印效果或打印成功率。

## 耗材准备

**PETG HF / PETG Basic** 耗材具有较强的吸湿性，在自然环境中容易吸收水分。在不烘干的情况下打印会造成打印质量问题，甚至可能导致打印失败。

因此，打印前，**必须**对 PETG HF / PETG Basic 耗材**进行烘干**。打印后，需将耗材放入 AMS / 密封盒中**密封保存**，并放入**干燥剂**，确保存储环境**湿度 < 20% RH**。

PETG HF / PETG Basic 耗材的烘干方式与要求，请参考下表：

| **烘干方式** | **烘干要求** |
| --- | --- |
| 鼓风型烤箱 | 65 ℃，8 小时 |
| AMS 2 Pro / AMS HT | 65 °C，8 小时 |
| X / P / H2 系列打印机热床 | 80 ℃，12 小时 |

![filament_drying_method.png](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/filament_drying_method.png)

> 📌 具体的烘干方法请参考：[耗材烘干操作指南 | Bambu Lab Wiki](dry-filament.md)

## 打印指南

1. **打印板要求**

   必须使用光面 PEI 打印板、高温打印板或纹理 PEI 打印板。

- **散热要求**

  对于封闭式打印机（X / P / H2 系列打印机），打印时需遵循以下散热要求：

  1. 模型主体耗材为 PLA Basic，支撑耗材为 PETG HF / PETG Basic，且模型首层存在 PETG 耗材时：打印过程中需要打开打印机的前门和（或）顶盖。
  2. 模型主体耗材为 PETG HF / PETG Basic，支撑耗材为 PLA Basic，且模型首层存在 PLA 耗材时：打印过程中需要打开打印机的前门和（或）顶盖。
- **参数设置**

  在 Bambu Studio 中，默认支撑参数并不适合作为 PLA Basic 与 PETG HF / PETG Basic 互相支撑的参数。因此，打印前，需要在 Bambu Studio 中调整耗材与支撑的参数，才能获得更好的打印质量。你可以直接下载"预设配置文件"章节的参数文件，也可以参考"切片参数设置"章节进行手动调参。

  > 📌 **注意：**
  >
  > - **使用 0.2 mm 喷嘴**进行 PLA / PETG 互相支撑打印时，建议参考下图增加线宽，以增加粘性，否则可能会导致炒面。此外，也可以使用修改器来修改支撑接触面附近的区域。  
  >   ![printing_parameters_for_0.2mm_nozzle.png](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/printing_parameters_for_0.2mm_nozzle.png)
  > - **热床温度说明：** 参数中热床温度提高为 60 ℃，这是因为 PETG 耗材使用 PLA 耗材的热床温度时，粘附力会降低，适当升温能够增加打印板粘附力。

### 预设配置文件

根据你的耗材组合，下载并打开下方对应 `.3mf` 文件，然后导入打印模型的 `.stl` 文件，即可应用这些参数，无需再次手动调整。

- [PLA Basic 支撑 PETG HF.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/pla_basic_%E6%94%AF%E6%92%91_petg_hf.3mf)
- [PETG HF 支撑 PLA Basic.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/petg_hf_%E6%94%AF%E6%92%91_pla_basic.3mf)
- [PETG Basic 支撑 PLA Basic.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/petg_basic_%E6%94%AF%E6%92%91_pla_basic.3mf)
- [PLA Basic 支撑 PETG Basic.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/pla_basic_%E6%94%AF%E6%92%91_petg_basic.3mf)

> 📌 注意：对于 **P2S** 打印机，其 PETG HF / PETG Basic 的**冷却设置**与其他机型略有不同，即特定层冷却风扇速度需保持默认的 40%。**如果您的打印机是 P2S，请下载下方参数文件**。
>
> - [PLA Basic 支撑 PETG HF\_@p2s.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/pla_basic_%E6%94%AF%E6%92%91_petg_hf_@p2s.3mf)
> - [PETG HF 支撑 PLA Basic\_@p2s.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/petg_hf_%E6%94%AF%E6%92%91_pla_basic_@p2s.3mf)
> - [PLA Basic 支撑 PETG Basic@p2s.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/pla_basic_%E6%94%AF%E6%92%91_petg_basic@p2s.3mf)
> - [PETG Basic 支撑 PLA Basic@p2s.3mf](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/petg_basic_%E6%94%AF%E6%92%91_pla_basic@p2s.3mf)

**如需手动设置参数或了解具体的参数设置**，请阅读下一章节。

### 切片参数设置

PLA Basic 与 PETG HF / PETG Basic 互相支撑的打印参数设置，主要涉及了**耗材参数**与**支撑参数**。

1. **耗材参数：**

由于不同耗材的物理和化学特性各不相同，其切片参数必须与其特性相匹配，才能保证打印质量。耗材参数主要包括喷嘴温度、热床温度、风扇速度等。

2. **支撑参数：**

在 Bambu Studio 中，用支撑耗材打印支撑结构时有 2 种选择：

- **支撑耗材同时作为支撑主体和支撑界面。**

  此选项更适用于需要较多支撑的情况，但打印时间更长。
- **模型主体耗材**作为 **支撑主体**，而**支撑耗材**仅作为 **支撑界面**。

  此选项更适用于仅需要少量支撑结构，且支撑结构易拆除的常规模型。

支撑参数的设置，主要是对于支撑主体耗材和支撑界面耗材的选择。

| 支撑耗材只用于支撑界面 | 支撑耗材用于支撑界面+支撑主体 |
| --- | --- |

**本章分别介绍：**

1. PLA Basic 支撑 PETG HF / PETG Basic 参数设置
2. PETG HF / PETG Basic 支撑 PLA Basic 参数设置

#### PLA Basic 支撑 PETG HF / PETG Basic 参数设置

此配置使用的模型主体耗材为 PETG HF、PETG Basic，支撑耗材为 PLA Basic。

##### 耗材参数设置

👉 耗材参数设置需要对**模型主体耗材 PETG HF / PETG Basic** 与**支撑耗材 PLA Basic** 的参数都进行设置。

**步骤 1.** 在 Bambu Studio 的左侧栏，项目耗材列表中，点击**耗材名称右侧的 "···" 图标 → "编辑"。**

**步骤 2.** 弹出的窗口中，进入"耗材丝设置"页面，修改下方参数。

- **喷嘴**：首层和其它层设置为 230 °C。
- **光面 PEI 打印板 / 纹理 PEI 打印板**：仅当首层存在 PETG 耗材时，将首层和其他层设置为 60 °C。若首层没有 PETG，则使用默认温度，无须调整该参数。
- 其他参数保持默认，无需调整。

**步骤 3.** 点击窗口右上角的保存按钮，将修改后的参数保存并命名，下次使用可以直接选择，不需要重新设置参数。

|  |  |
| --- | --- |
|  |  |

##### 支撑参数设置

主体耗材为 PETG HF / PETG Basic，支撑耗材为 PLA Basic 时，推荐**仅将 PLA Basic 作为支撑接触面材料**。原因是 PLA Basic 同时用作支撑主体和支撑界面会导致打印时间过长，且支撑结构容易从模型表面脱落。

具体设置步骤如下图所示：

|  |  |
| --- | --- |
|  |  |

#### PETG HF / PETG Basic 支撑 PLA Basic 参数设置

此配置使用的模型主体耗材为 PLA Basic，支撑耗材为 PETG HF / PETG Basic。

##### 耗材参数设置

👉 需要对主体耗材与支撑耗材的参数都进行设置。

1. **主体耗材 PLA Basic 的参数设置：**

**步骤 1.** 在 Bambu Studio 的左侧栏，项目耗材列表中，点击 PLA Basic 右侧的 **"···" 图标 → "编辑"。**

**步骤 2.** 弹出的窗口中，进入"耗材丝设置"页面，修改下方参数。

- **喷嘴**：首层和其它层设置为 230 °C。
- **光面 PEI 打印板 / 纹理 PEI 打印板**：仅当首层存在 PETG 耗材时，将首层和其他层设置为 60 °C。若首层没有 PETG，则使用默认温度，无须调整该参数。
- 其他参数保持默认，无需调整。

**步骤 3.** 点击窗口右上角的保存按钮，将修改后的参数保存并命名，下次使用可以直接选择，不需要重新设置参数。

|  |  |
| --- | --- |
|  |  |

2. **支撑耗材 PETG HF / PETG Basic 的参数设置：**

**步骤 1.** 在 Bambu Studio 的左侧栏，项目耗材列表中，点击 **PETG HF / PETG Basic 右侧的 "···" 图标 → "编辑"。**

**步骤 2.** 弹出的窗口中，进入"耗材丝设置"页面，修改下方参数。

- **喷嘴**：仅 PETG HF 的首层和其它层设置为 265 °C，**PETG Basic 无须改动**。
- **光面 PEI 打印板 / 纹理 PEI 打印板**：将首层和其他层温度设置为 60 °C。
- **最大体积速度**：设置为 10 mm³/s。
- 其他参数保持默认，无需调整。

**步骤 3.** 点击窗口右上角的保存按钮，将修改后的参数保存并命名，下次使用可以直接选择，不需要重新设置参数。

|  |  |
| --- | --- |
|  |  |

##### 支撑参数设置

建议**仅使用 PETG HF / PETG Basic 作为支撑接触面材料**，因其作为支撑主体时，模型支撑容易脱落。

- PLA Basic 作为支撑主体，PETG HF / PETG Basic 作为支撑界面时，设置方法如下：

将**支撑/筏层主体**设置为 PLA Basic，**支撑/筏层界面**设置为 PETG HF / PETG Basic。

![petg_hf_petg_basic_supporting_pla_basic_support_settings_1.webp](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/petg_hf_petg_basic_supporting_pla_basic_support_settings_1.webp)

- PETG HF / PETG Basic 同时作为支撑主体和支撑界面时，设置方法如下：

将**支撑/筏层主体**和**支撑/筏层界面**都设置为 PETG HF / PETG Basic。

![petg_hf_petg_basic_supporting_pla_basic_support_settings_2.webp](https://wiki.bambulab.com/filament-acc/filament/pla-basic-petg-hf-support-each-other/petg_hf_petg_basic_supporting_pla_basic_support_settings_2.webp)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
