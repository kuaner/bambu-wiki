---
path: zh/ams-2-pro/manual/drying-function
title: "AMS 2 Pro 和 AMS HT 烘干指南"
description: "本文将介绍 AMS 2 Pro 和 AMS HT 的烘干工作流程。"
tags: ["ams 2 pro", "ams ht"]
created: 2025-05-27T11:28:24.077Z
updated: 2026-07-29T03:46:14.005Z
source: https://wiki.bambulab.com/zh/ams-2-pro/manual/drying-function
---

## 功能概述

AMS 2 Pro 和 AMS HT 都内置了烘干模块，当耗材长时间未使用时，您可以通过 AMS 2 Pro 或 AMS HT 干燥耗材。

|  |  |
| --- | --- |
|  |  |

## 操作指南

### 打印机上操作流程

1. 关闭 AMS 上盖

![ams.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams.png)

2. 进入打印机的 「烘干和湿度」 页面

- 如果您有多个 AMS，请选择正确的设备开启烘干。

![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(6).png)

3. 选择烘干参数

- 根据您的需求选择合适的烘干参数。当烘干 PLA 时，AMS 中可以存放其他耗材。当**烘干 ABS/PETG 时**，PLA 和 TPU 耗材需要从 AMS 中**取出**，否则耗材可能融合。

![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(7).png)

> 当AMS中存在 PLA 时，首次进入烘干页面将默认为 PLA 耗材烘干参数；  
> 当AMS中不存在 PLA，但是有 PETG 时，首次进入烘干页面将默认为 PETG 耗材烘干参数；
>
> ![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(8).png)
>
> ![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(9).png)

4. 确认 AMS 中的耗材类型，并选择烘干方式。如烘干 ABS 时，设备会提示将 PLA 抽出。

![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(12).png)

- 方法一：旋转料盘烘干（推荐）  
  **操作方式：** 将耗材从进料口拔出，并整理收纳到料盘中，然后勾选“烘干时旋转料盘”。**此时已经拔出的槽位将开启旋转烘干，未从进料口拔出的耗材不会旋转。**  
  **工作原理：** 料盘每 5 分钟旋转 30°，使耗材受热更均匀

  > ✅ 适用于大多数耗材，烘干效果更佳
- 方法二：静止烘干  
  **操作方式：** 耗材保持插入进料口  
  **工作原理：** 料盘不转动，仅依靠腔体内热风循环

  > H2D 固件版本 01.03.00.00 开始支持烘干 PLA 和 TPU 时，无需收起耗材并开启旋转料盘功能。  
  > 其他设备或较低固件版本情况下，请按照方法一烘干 PLA 和 TPU。

5. 点击开始

- 点击开始后，AMS 将进行一次自检，完毕后将进入烘干计时。

![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(14).png)

![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(15).png)

### 远程操作流程

> 固件最低支持版本：
>
> - H2D： 01.03.00.00 版本及以上
> - H2S： 01.02.00.00 版本及以上
> - P2S： 01.02.00.00 版本及以上
> - X2D： 01.01.00.00 版本及以上
> - A2L：01.01.00.00版本及以上
> - P1S/P1P/X1C/A1/A1mini 暂不支持

从 Bambu Handy 或 Bambu Studio 软件的“设备”页面控制 AMS 烘干功能，以 Bambu Studio 进行演示。

- 软件上点击对应 AMS 的“烘干”按钮，打开对应控制弹框。

![ams_(3).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(3).png)

- 选择耗材烘干设置

![ams_(3).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(4).png)

- 检查 AMS 中的耗材情况，部分耗材需拉出入料口。

![ams_(3).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(5).png)

- 启动或停止烘干。

![ams20.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams20.png)

## 边烘边打功能介绍

AMS 的边烘边打是在开启 AMS 烘干功能的同时，使用 AMS 的自动上下料功能。

该功能在屏幕/软件界面不具备独立的开启/关闭按钮。若要使用该功能，可直接在开启烘干的同时进行打印即可。

> 注：开启 AMS HT 的烘干功能，并将耗材从 TPU 出料口送出的方式并非边烘边打，这仅使用了烘干功能，所有机型都能使用该方式。

为确保自动送料的顺畅和打印稳定，当开始打印任务后，系统会**自动降低烘干温度**，这样能够有效防止耗材在 AMS 内部提前软化，避免 AMS 中的送料齿轮压碎耗材，并且烘干温度将不会高于 AMS 舱内耗材的最低软化温度。

- 烘干 PLA 并打印其他耗材 / 使用 PLA 打印  
  → 烘干温度自动设定为 45 °C（不高于 PLA 的软化温度）
- 烘干 PETG 并打印 ABS / 使用 PETG 打印  
  → 烘干温度自动设定为 55 °C（不高于 PETG 的软化温度）

![1.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/1.png)

### 固件最低支持版本

- H2D： 01.03.00.00 版本及以上
- H2S： 01.02.00.00 版本及以上
- P2S： 01.02.00.00版本及以上
- X2D：01.01.00.00版本及以上
- A2L：01.01.00.00版本及以上

> - P1S/P1P/X1C/A1/A1mini 暂不支持

### 烘干时整机功能限制

| 机型 | 未连接电源适配器 | 连接电源适配器 |
| --- | --- | --- |
| H2 系列 | 为了优先确保打印功率，烘干功率自动会降低到正常烘干功率的 86% 进行烘干 | 无限制 |
| P2S/X2D | 打印机无法执行热床热端升温、XYZ 移动和 AMS 进退料等操作 | 无限制 |

## 硬件功能介绍

### 烘干模块

- **AMS 2 Pro：** 内置加热烘干模块（位于中框两侧），最高烘干温度 65 °C。  
  最高温度需在环境温度 ≥25°C 的条件下方可实现。当环境温度低于25°C时，**受自然散热影响**，实际烘干温度可能无法达到最高值，这并非是产品故障。由于低温环境可能影响烘干效果，**建议在适宜的室温条件**下使用该功能，或在低温环境中采取相应的保温措施，以获得更稳定的的烘干效果。

![prodryer.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/prodryer.png)

- **AMS HT：** 内置加热烘干模块（位于中框下方），最高烘干温度 85 °C  
  由于 AMS HT 的 170W 加热器功率较高，因此在 10℃ 至 25℃ 环境下也能够稳定加热并维持最高 85 °C 的烘干温度。

![htdryer.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/htdryer.png)

✅ 所有耗材均可使用 AMS 2 Pro 或 AMS HT 进行烘干。（后文统称 AMS）  
⚠️ **工程材料**所需烘干温度高于 65 °C，为获得更好的烘干效果，此类耗材推荐使用 AMS HT 烘干。

### 风门控制逻辑

AMS 具备主动控制的进气口与出气口。在烘干过程中，系统会根据温度状态自动调节风门，实现高效加热与排湿。

|  |  |
| --- | --- |
| ht_door.jpeg | door2.png |

1. **未开启烘干时：** 进出气口关闭，防止外部潮湿空气进入。
2. **开始烘干时：** 进出气口会开合一次，用于提示用户烘干已启动，并进行系统自检。
3. **腔体温度低于目标温度：** 进出气口关闭，集中加热，快速升温。
4. **腔体温度达到目标温度：** 进出气口打开，通过外循环将腔内湿气排出。
5. **送料前温度检测：** 在 AMS 开始送料前，若检测到腔内温度高于当前耗材的软化温度，系统会先启动风扇进行降温，待温度安全后再开始送料，以避免堵料。

### 电源要求说明

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

#### 不同机型的供电方式

1. H2 系列 / P2S / X2D（ **1 台 AMS 2 Pro 烘干**）

   - AMS 2 Pro 可通过 6-pin 线直接从打印机取电
   - 无需额外电源适配器
   > **说明**：若未接电源适配器直接开启烘干时，P2S / X2D 打印机将无法执行热床热端升温、XYZ 移动和 AMS 进退料等操作（功率优先分配给 AMS）
2. H2 系列 / P2S / X2D（**多台 AMS 2 Pro 同时烘干**）

   - 仅 1 台 AMS 2 Pro 可通过 6-pin 线供电
   - 其余 AMS 2 Pro 需使用 电源适配器（需单独购买）  
     ![adapter.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/adapter.png)
3. X1 / P1 / A2L 系列打印机

   - 每台 AMS 2 Pro 都 **必须使用电源适配器**才能开启烘干功能
4. AMS HT

   - 烘干功能**必须连接自带电源线**
   - 不支持通过 6-pin 线供电烘干  
     ![cable.png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/cable.png)

---

5. 电源状态指示说明

- 未连接电源：页面右下角电源图标为灰色，此时仅支持 1 台 AMS 2 Pro 从打印机供电烘干。
- 已连接电源：页面右下角电源图标显示为绿色，此时烘干将通过适配器或电源线供电。

|  |  |
| --- | --- |
| sign2.png | sign2.png |

> 多台 AMS 可参考[多机型 AMS 连接指南](../../ams/manual/multi-model-AMS-compatibility-guide.md)了解连接方式以及所需配件。

---

### 注意事项

**未读取 RFID 信息**或**未进行手动编辑**的耗材，在 AMS 中将显示为“？”，并且在烘干时默认为 PLA，这可能影响烘干操作流程。  
您可以点击“编辑”或“重新读取”来确认耗材信息后，再开启烘干功能。

![ams_(6).png](https://wiki.bambulab.com/ams-2-pro/manual/drying-function/ams_(2).png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
