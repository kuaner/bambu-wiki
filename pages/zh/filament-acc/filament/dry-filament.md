---
path: zh/filament-acc/filament/dry-filament
title: "耗材烘干操作指南"
description: ""
tags: []
created: 2023-09-18T12:14:02.019Z
updated: 2026-07-29T03:52:21.755Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/dry-filament
---

## 耗材烘干

耗材会从空气中吸收水分。在打印过程中，这些水分会在高温喷嘴内迅速汽化，导致熔融耗材膨胀、挤出不稳定并产生气泡，从而引发**拉丝、渗料、孔洞、表面粗糙以及强度下降**等问题。随着环境湿度升高或耗材暴露时间变长，这些问题会更加明显。

因此，在开始打印前——**尤其是对外观和质量要求较高的模型**——如果耗材的保存状态不确定，**建议先进行烘干**。日常存放时，也应注意**密封保存并做好防潮措施**。

如下图所示是**受潮的（左） 和干燥的（右）PETG 半透明**。

|  |  |
| --- | --- |
|  |  |
|  |  |

烘干方式有两种：使用 AMS HT 或 AMS 2 Pro 烘干；使用打印机热床烘干。

- [AMS HT 购买链接](https://item.jd.com/10143824753819.html)
- [AMS 2 Pro 购买链接](https://item.jd.com/10143824027483.html)

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-9.png)

## 1. 使用 AMS 2 Pro \ AMS HT 烘干

### 1.1 烘干操作流程

**放入耗材 -> 选择类型 -> 启动烘干 -> 烘干结束**

![a4_-_6.png](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/a4_-_6.png)

### 1.2 注意事项

|  | AMS 2 Pro | AMS HT |
| --- | --- | --- |
| 适用耗材 | - 适用于烘干温度不高于65℃的耗材 - 部分材料所需烘干温度高于65℃，AMS 2 Pro 可能无法完全干燥 - 烘干高温耗材时需要将低温耗材取出，如烘干 ABS 时，AMS 中不能放置 PLA 耗材 | - 所有耗材均可使用 AMS 来烘干 - 部分需高温烘干的材料可能无法完全干燥，例如 PVA、PPS-CF、PPA-CF |
| 电源要求 | - H2 系列 / P2S / X2D 打印机支持 1 台 AMS 2 Pro 从打印机取电烘干 - 若多台 AMS 2 Pro 同时烘干，其余的 AMS 2 Pro 需要连接电源适配器 - 如果 AMS 2 Pro 连接了 X1 / P1 / A2L 系列打印机，则每台都必须通过电源适配器才能使用烘干功能 | - 必须使用标配电源线独立供电（打印机无法为 AMS HT 的烘干功能供电） |

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

### 1.3 烘干模式说明

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image.png)

> **注意事项：**
>
> 选择旋转料盘烘干时，需要手动从进料口中拔出耗材，并将其收纳至料盘侧面；  
> 料盘的**静止烘干不适用以下几种耗材**：**PLA、PVA、support for PLA/PETG 和 TPU**。原因是上述耗材软化温度低于烘干温度，静置烘干会导致耗材之间发生粘黏或者膨胀变形。

### 1.4 烘干时打印

为了保证进料过程以及打印质量稳定，发起打印任务后烘干温度会自动降低，通常会低于耗材的软化温度，避免耗材堵塞在 AMS 中。

> 如果您烘干 PLA 时打印其他耗材 或使用 PLA 进行打印，烘干温度会设定 45 ℃；如果您烘干 PETG 时打印 ABS 耗材或使用 PETG 进行打印，烘干温度会设定 55 ℃。

![drying.png](https://wiki.bambulab.com/filament-acc/filament/dry-filament/drying.png)

## 2. 使用打印机热床烘干

封闭式打印机可以利用热床的加热功能来创造一个干燥耗材的环境。

> **注意事项：**
>
> **使用时请注意遵守说明和注意事项，避免设备损坏。** 耗材干燥的过程中可能有以下风险，请在烘干前提前检查：
>
> - 一些第三方的料盘不够耐温，所以在干燥过程中料盘有可能变形。
> - **P1P / A1 / A2L / A1 mini** 由于是开放式打印机，因此**无法使用热床干燥耗材**。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-2.png)

### 2.1 H 系列 \ X 系列 \ P2S \ X2D 热床烘干步骤

#### 步骤1：检查干涉，退出耗材

清空打印板上部和底部，避免打印板运动时干涉；通过屏幕检查进料情况，若此时有进料，应点击“**退料**”按钮，将耗材退出工具头，避免耗材在挤出机内软化，导致堵塞风险。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-3.png)

#### 步骤2：准备烘干，下降热床

屏幕操作提示如下图：（以 H2 系列为例）

![ui.png](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/ui.png)

单击"准备"按钮后，工具头和热床将移动到预设位置。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-5.png)

#### 步骤3：盖住耗材，保持高温环境

将耗材放在打印板上并盖上用 PA-CF 或者 PC 这一类高温材料打印的盖子（模型可以从 [Bambu Filament Drying Cover](https://wiki.bambulab.com/knowledge-sharing/filament-drying-cover/bambu_filament_drying_cover.stl)下载），盖子也可以用包装盒代替。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-7.png)

#### 步骤4：开始烘干，中途翻面

请选择耗材类型，设置打印板温度和烘干时间，点击"开始"按键即可开始烘干。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-11.png)

> **注意事项：** **建议烘干中途为耗材翻面，确保耗材均匀受热。请佩戴手套将耗材翻面！避免烫伤！**

#### 步骤5：烘干完成、密封保存

当达到烘干时间后，请将热床温度设置为 0 ℃，等待耗材不烫手后尽快取出进行后续操作。

烘干结束后，请立即用有效干燥剂和密封盒或 AMS 存放耗材，并尽快使用，以免耗材重新受潮。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-13.png)

### 2.2 P1S 烘干注意事项

P1S 需要手动控制热床下降并设置热床温度，您可以参考本文结尾的[耗材烘烤参数表](#%E8%80%97%E6%9D%90%E7%83%98%E7%83%A4%E5%8F%82%E6%95%B0%E8%A1%A8)，设置对应耗材所需要的烘干温度与时间。主要操作步骤如下：

#### 步骤1：检查干涉，退出耗材

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-14.png)

#### 步骤2：点击回中，下降热床

通过打印机屏幕执行回中功能，并等待热床完成回中：

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-15.png)

|  |  |
| --- | --- |
| 选中热床并下降 | 下降热床到低处 |

#### 步骤3：盖住耗材，保持高温环境

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-18.png)

#### 步骤4：设置热床温度，烘干计时

由于 P1S 没有“烘干耗材”的功能，需手动设置对应的热床温度，并自行记录烘干时间。以 ABS 为例，设置热床温度为 100℃，然后记录开始烘干的时间。

![pixpin_2025-11-12_14-39-47.png](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/pixpin_2025-11-12_14-39-47.png)

#### 步骤5：烘干完成、密封保存

当达到烘干时间后，请将热床温度设置为 0 ℃，等待耗材不烫手后尽快取出进行后续操作。

烘干结束后，请立即用有效干燥剂和密封盒或 AMS 保护易受潮的耗材，并尽快使用，以免耗材重新受潮。

![](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/image-20.png)

## 耗材烘烤参数表

各类耗材的建议烘烤参数如下表:

> 注意：如果您购买的是无盘耗材，请将耗材安装在料盘上再进行烘干。安装方法您可以参考这篇 Wiki：[无盘耗材安装至可重复使用料盘的指南](../../general/swaping-new-filament-with-bambu-reusable-spool.md)

💡 提示：表格可上下、左右滑动查看更多内容

| 耗材 | 使用前的烘干要求 | 使用时的干燥剂保护要求 | 拓竹 H2 系列、X 系列、P1S、P2S 打印机热床温度 / ℃ | 干燥时间 / h | 翻面时间 / h | 盖子 | 鼓风型烤箱 温度 / ℃ | 干燥时间 / h | AMS 2 Pro 温度 / ℃ | 干燥时间 / h | AMS HT 温度 / ℃ | 干燥时间 / h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PLA Basic/PLA Matte | 推荐 | 不需要但推荐 | 60-70 | 12 | 每 6 小时 | 耗材包装盒或 PC 盒 | 50 | 8 | 45 | 12 | 45 | 12 |
| PLA Silk | 推荐 | 不需要但推荐 | 65-75 | 12 | 每 6 小时 | 耗材包装盒或 PC 盒 | 55 | 8 | 45 | 12 | 45 | 12 |
| PLA-CF/GF | 推荐 | 不需要但推荐 | 65-75 | 12 | - | - | 50-60 | 8 | 45 | 12 | 45 | 12 |
| PLA Wood | **必须** | **必须** | 70-75 | 12 | - | - | 55-65 | 8 | 45 | 12 | 45 | 12 |
| PLA Aero | 推荐 | 不需要但推荐 | 60-70 | 12 | - | - | 55 | 8 | 45 | 12 | 45 | 12 |
| PLA Galaxy | 推荐 | 不需要但推荐 | 65 - 75 | 12 | - | - | 55 | 8 | 45 | 12 | 45 | 12 |
| Support for PLA | 推荐 | 不需要但推荐 | 65-75 | 12 | - | - | 55 | 8 | 60 | 12 | 60 | 12 |
| Support for PLA/PETG | 推荐 | 不需要但推荐 | 65-75 | 12 | - | - | 75 | 8 | 60 | 12 | 60 | 12 |
| PETG、PETG-CF | 推荐 | 不需要但推荐 | 75-85 | 12 | - | - | 60-65 | 8 | 65 | 12 | 65 | 12 |
| ABS、ASA | 推荐 | 不需要但推荐 | 90-100 | 12 | - | - | 75-85 | 8 | 不适配 | 不适配 | 80 | 8 |
| ASA-CF、ABS-GF | 推荐 | 推荐 | 90-100 | 12 | - | - | 80 | 8 | 不适配 | 不适配 | 80 | 8 |
| ASA Aero | 推荐 | 不需要但推荐 | 90-100 | 12 | - | - | 80 | 8 | 不适配 | 不适配 | 80 | 8 |
| TPU 85A、TPU 90A | **必须** | **必须** | 90 | 16 | - | - | 70 | 8 | 65 （存在无法完全烘干的风险， 建议使用热床或 AMS HT 烘干） | 12 | 75 | 18 |
| TPU 95A HF | **必须** | **必须** | 80-90 | 12 | - | - | 70 | 8 | 65 （存在无法完全烘干的风险， 建议使用热床或 AMS HT 烘干） | 12 | 75 | 18 |
| TPU for AMS | **必须** | **必须** | 80-90 | 12 | - | - | 70 | 8 | 65 （存在无法完全烘干的风险， 建议使用热床或 AMS HT 烘干） | 12 | 75 | 18 |
| PC | **必须** | **必须** | 90-100 | 12 | - | - | 75-85 | 8 | 不适配 | 不适配 | 80 | 8 |
| PVA | **必须** | **必须** | 90-100 | 12 | - | - | 75-85 | 8-12 | 不适配 | 不适配 | 85 | 18 |
| Support for PA/PET | **必须** | **必须** | 90-100 | 12 | - | - | 75-85 | 8-12 | 不适配 | 不适配 | 80 | 12 |
| PA6-CF/GF、PAHT-CF/GF 等 | **必须** | **必须** | 90-100 | 12 | - | - | 75-85 | 8-12 | 不适配 | 不适配 | 85 | 12 |
| PET-CF | **必须** | **必须** | 90-100 | 12 | - | - | 80 | 8-12 | 不适配 | 不适配 | 80 | 12 |
| PPA-CF、PPS-CF | **必须** | **必须** | 110-120（最高值）    **效果不及鼓风型烤箱** | 10-12    **效果不及鼓风型烤箱** | - | - | 100-140 | 8-12 | 不适配 | 不适配 | 不适配 | 不适配 |
| Support for ABS | 不需要但推荐 | 不需要但推荐 | 85-95 | 6 | 每 3 小时 | - | 80 | 4 | 不适配 | 不适配 | 80 | 4 |

---

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn?from=5)，它能够即时解答常见问题，并为您提供操作指导。
