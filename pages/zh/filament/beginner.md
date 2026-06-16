---
path: zh/filament/beginner
title: "耗材新手入门指南"
description: "耗材新手入门指南，帮助新手快速学会如何使用耗材。"
tags: []
created: 2025-09-29T09:08:23.945Z
updated: 2026-06-15T06:42:05.361Z
source: https://wiki.bambulab.com/zh/filament/beginner
---

**欢迎来到 3D 打印的世界！正确使用和保存耗材是获得高质量打印件的基础。本指南将引导您完成从拆封、打印到保存的全过程，助您轻松上手。**

- Bambu Lab 的耗材自带 RFID 芯片，设备自动识别耗材参数，默认参数即可获得较好的打印效果。
- **对于大部分的耗材（如 PLA）**，您只需参考以下列三个步骤即可完成打印。

1. 打印前请用热水和洗洁精清洁打印板，以确保最佳附着力。
2. 在 Bambu Studio 中发起打印。
3. 待打印完成后，请等打印板充分冷却，再取下打印件。

![23-1.png](https://wiki.bambulab.com/filament-acc/beginner/23-1.png)

> 提示： PLA 是对新手最友好的耗材类型，它是无味、易打印的材料，强烈推荐新手从 PLA 开始尝试。更多的详细操作步骤请参考下文。

## 耗材开封

**检查包装**是非常重要的一步， 打开耗材的**真空密封袋**前，请先检查包装是否有破损或漏气。良好的密封是保证耗材干燥的第一步。另外，工程耗材的**银色密封袋包装**有塑封条可**重复使用**。

|  |  |
| --- | --- |
| 普通密封包装袋 | 银色密封包装袋 |

> **重要提醒**  
> 在将带有料盘的耗材**放入 AMS 或正式使用前**，建议您**不要移除耗材上的任何固定胶带**。否则，耗材可能会散开，导致无法正常使用，或在打印过程中出现缠绕、打结等问题。即使重新卷绕，也容易在使用过程中再次出现打结，影响打印质量。

## 耗材烘干指南

在开始打印之前，确保耗材处于干燥状态非常重要。湿气会严重影响打印效果，因此您需要按照以下步骤进行操作，从确认耗材状态，确认烘干温度与时间，再到选择合适的烘干方式，都有清晰的指引。

> 提示：PLA 一般可以开箱即用，不需要进行烘干。PLA Silk/Silk+、PLA CF 和 PLA Wood 除外。

### 为什么要烘干耗材

耗材在空气中暴露后会吸收水分。打印时，这些水分会在高温喷嘴中汽化，可能导致以下问题：

- 模型表面拉丝
- 打印件粗糙
- 出现气孔
- 强度下降

环境湿度越高、暴露时间越长，受潮影响就越严重。因此，在开始打印前，建议您检查并烘干耗材。

### 确认耗材是否需要烘干

1. **打印前检测**：可以使用默认的测试文件打印一个**小模型**（在 Bambu Studio 中右键**添加标准模型**即可）。

![测试件模型位置.jpg](https://wiki.bambulab.com/filament-acc/beginner/%E6%B5%8B%E8%AF%95%E4%BB%B6%E6%A8%A1%E5%9E%8B%E4%BD%8D%E7%BD%AE.jpg)

2. **观察效果**：如果模型拉丝明显，如下面右图所示，则说明耗材受潮，需要烘干。

![dry_and_wet_petghf_cn.png](https://wiki.bambulab.com/filament-acc/filament-dry-prepare/dry_and_wet_petghf_cn.png)

### 选择合适的烘干方式

不同耗材对温度和时间要求不同，您可以参考： [耗材烘干操作指南](../filament-acc/filament/dry-filament.md)

1. **查阅参数**：了解耗材的推荐烘干温度与时间。
2. **选择设备**：常见方法包括：

   - 使用鼓风烤箱
   - 使用拓竹 \*\*P2S / P1S / X1 / H2 系列打印机
   > 注意：**P1P / A1 / A1 mini** 为开放式打印机，**无法**进行耗材烘干。

   - 使用 AMS 2 Pro / AMS HT
   > 注意：
   >
   > 1. AMS 2 Pro **最高烘干温度 65°C**；AMS HT **最高烘干温度 85°C**。
   > 2. 打印过程中,仅部分机型可使用 AMS 烘干功能，详细信息请参考[这篇 Wiki](../ams-2-pro/manual/drying-function.md)。
   > 3. 打印机无法为 AMS HT 提供烘干所需电力，必须使用标配电源线独立供电。
3. **确认烘干参数**：

| 耗材 | 使用前的烘干要求 | 使用时的干燥剂保护要求 | 鼓风型烤箱 温度(℃) | 鼓风型烤箱 时间(h) | 打印机 热床温度(℃) | 打印机 时间(h) | 翻面时间 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PLA Basic / PLA Matte | 推荐 | 不需要但推荐 | 50 | 8 | 60-70 | 12 | 每 6 小时 |
| PLA Silk | 推荐 | 不需要但推荐 | 50 | 8 | 60 - 70 | 12 | 6 |
| PLA-CF/GF | 推荐 | 不需要但推荐 | 50 - 60 | 8 | 65 - 75 | 12 | 6 |
| PLA Wood | 必须 | 必须 | 55 - 65 | 8 | 70 - 75 | 12 | 6 |
| PLA Aero | 推荐 | 不需要但推荐 | 55 | 8 | 60 - 70 | 12 | 6 |
| Support for PLA、Support for PLA/PETG | 推荐 | 不需要但推荐 | 50 - 60 | 8 | 65 - 75 | 12 | 6 |
| PETG、PETG-CF | 推荐 | 不需要但推荐 | 60 - 70 | 8 | 75 -85 | 12 | 6 |
| ABS、ASA | 推荐 | 不需要但推荐 | 75 - 85 | 8 | 90 - 100 | 12 | 6 |
| Support for ABS | 不需要但推荐 | 不需要但推荐 | 80 | 4 | 85 - 95 | 6 | 每 3 小时 |
| ASA Aero | 推荐 | 不需要但推荐 | 80 | 8 | 90 - 100 | 12 | 6 |
| TPU | 必须 | 必须 | 65 - 75 | 8 | 80 - 90 | 12 | 6 |
| PC | 必须 | 必须 | 75 - 85 | 8 | 90 - 100 | 12 | 6 |
| PVA、BVOH | 必须 | 必须 | 75 - 85 | 75 - 85 | 90 - 100 | 12 | 6 |
| Support for PA/PET | 必须 | 必须 | 75 - 85 | 8 - 12 | 90 - 100 | 12 | 6 |
| PA、PA-CF/GF、PAHT-CF/GF、PET-CF 等 | 必须 | 必须 | 75 - 85 | 8 - 12 | 90 - 100 | 12 | 6 |
| PPA-CF/GF | 必须 | 必须 | 100 - 130 | 8 - 12 | 110 - 120（最高值）效果不及鼓风型烤箱 | 12 | 6 |
| PPS、PPS-CF/GF | 必须 | 必须 | 110 - 140 | 8 - 12 | 110 - 120（最高值）效果不及鼓风型烤箱 | 12 | 6 |

> 注意：
>
> - 搭配打印机热床烘干需要配备一个**盖子**进行保温，盖子使用**耗材包装盒**或者 **PC 盒**即可。
> - **PPA-CF/GF** 和 **PPS、PPS-CF/GF** 由于所需烘干温度过高，建议您使用打印机热床或者鼓风型烤箱进行烘干。

## 安装耗材到打印机

拓竹耗材采用可重复使用的料盘，支持回收并可多次重复利用，有助于减少材料浪费。

在售耗材分为有盘耗材和无盘耗材。若已持有足够数量的料盘，您可单独选购无盘耗材，按实际需要灵活安装使用。

![](https://wiki.bambulab.com/filament-acc/beginner/image-10.png)

> 提示：使用有盘耗材的用户可以**省略**无盘耗材安装，直接跳转到[**初次安装耗材到 AMS 指引**](https://wiki.bambulab.com/zh/filament/beginner#ams-lite)。

### 无盘耗材安装

拓竹的耗材由耗材和可重复利用的料盘组成（如下图所示）。当您拥有足够多的空料盘，即可考虑购买无盘耗材自行安装。

![安装料盘.jpg](https://wiki.bambulab.com/filament-acc/beginner/%E5%AE%89%E8%A3%85%E6%96%99%E7%9B%98.jpg)

#### 安装指引视频

> **重要提醒**
>
> - 带有料盘的耗材在放入 AMS 前建议您先**不要**把四根胶带移除，以免导致耗材松散，产生“炸盘”等后果。
> - 请勿撕下 RFID 识别芯片。
> - 注意安装**无盘耗材**时需要**孔对孔卡到位**，即耗材纸筒缺口务必对准料盘**内侧凹起**处（如下图所示），否则耗材将无法顺利安装！！！  
>   ![](https://wiki.bambulab.com/filament-acc/beginner/image-4.png)

安装无盘耗材请参考下面的视频：

[

](https://public-cdn.bblmw.com/wiki/filament/beginner-1-cn.mp4)

#### 安装指引图解

1. 旋转打开料盘
2. 对准耗材与料盘限位孔
3. 旋转卡好另一侧的料盘。**请务必点对点卡到位！**
4. 建议安装到机器上后，再移除耗材上的固定胶带

![image-3-1.jpg](https://wiki.bambulab.com/filament-acc/beginner/image-3-1.jpg)

#### 检查安装位置

若您使用的不是上面视频中的透明料盘，在安装完成后，可以参考下图的位置，来检查**料盘转轴**是否安装到位：

|  |  |
| --- | --- |
| 安装到位，卡扣位置正确 | 未安装到位，卡扣位置错误 |

> 提示：推荐您可以**自行打印**料盘使用，相关的模型文件可以在 [MakerWorld 中的拓竹 3D 打印料盘](https://makerworld.com.cn/zh/models/125808-tuo-zhu-3dda-yin-liao-pan?from=search#profileId-8889)下载。

#### 移除末端固定胶带

1. **放入 AMS**  
   将料盘先放入 AMS 中，再准备处理末端胶带。
2. **解开绑带**  
   先用手摁住**耗材末端**，再小心解开固定耗材末端的胶带。
3. **剪成斜角**  
   使用剪刀或剪线钳将末端剪成斜角，便于送入打印机或 AMS；剪切时保持耗材张力，避免耗材散开。

|  |  |
| --- | --- |
| 使用剪刀移除固定胶带 | 耗材末端剪成斜角 |

将料盘放入打印机的料盘架或者 AMS 上。确保料盘可以顺畅转动，没有阻碍。耗材丝送入设备的方向如下图所示：

- 外挂料盘
- AMS
- AMS Lite

![12.png](https://wiki.bambulab.com/filament-acc/beginner/12.png)

- AMS Lite 耗材进料动态图

![送料.gif](https://wiki.bambulab.com/filament-acc/beginner/%E9%80%81%E6%96%99.gif)

### AMS Lite

下面是**新料盘初次放进 AMS Lite** 的详细教程，具体详细操作可以参考下面的视频。

[

](https://public-cdn.bblmw.com/wiki/filament/beginner-2-cn.mp4)

### 外挂料盘

外挂料盘需要手动将耗材送入工具头并进料才可以开始打印。所有机型的进料逻辑大致相同，您可以参考以下教程了解不同机型进料与退料的步骤：

1. 推动耗材到工具头

![](https://wiki.bambulab.com/filament-acc/beginner/image-17.png)

2. 确认耗材位置、点击进料

![](https://wiki.bambulab.com/filament-acc/beginner/image-16.png)

3. 观察挤出状态，等待进料完成

![](https://wiki.bambulab.com/filament-acc/beginner/image-19.png)

不同机型的进料与退料步骤略有差异，可参考对应机型指南：

- [A1 初次打印指南（使用外挂料盘）](../a1/manual/first-print-with-external-spool.md)
- [P1 系列装载打印耗材](../p1/manual/loading-filament.md)
- [X1 系列装载打印耗材](../x1/manual/loading-filament.md)
- [P2S 装载打印耗材](../p2s/manual/first-print.md)
- [H2 系列装载打印耗材](../h2s/manual/h2s-first-print.md)

## 打印前的检查

为了确保打印过程顺利进行，建议在设备启动打印前完成以下检查：

1. 检查耗材路径：确认从料盘到喷嘴的整个耗材通道畅通无阻，避免出现尖锐弯折或缠绕现象。（下图左侧示例为耗材打结情况）
2. 清洁打印板：在打印前请检查打印板是否保持干净，若有脏污，请使用酒精或专用清洁剂对打印板进行擦拭，避免用手直接触碰已清洁的打印板表面，以保持其清洁度。

![19.png](https://wiki.bambulab.com/filament-acc/beginner/19.png)

3. 务必将耗材末端固定在料盘上，不要随意松开。松散的耗材易发生缠绕，进而引发进料故障或打印异常。

![never_let_go.png](https://wiki.bambulab.com/filament-acc/beginner/never_let_go.png)

耗材缠绕时，打印机仍会试图进行送料，但无法成功送进。

![tangled_spool.gif](https://wiki.bambulab.com/filament-acc/beginner/tangled_spool.gif)

## 开启打印

### 配置耗材参数、发送打印任务

#### 普通耗材

官方耗材内置识别芯片，可通过 AMS 自动识别或手动配置，同步匹配推荐的打印参数。使用基础耗材（如 PLA）时，在切片软件中选择对应耗材类型及其配置进行切片，即可获得推荐打印配置。

#### 发泡耗材

另外，需要特别注意的是，**部分特殊功能耗材经出厂测试调整，可配合附带的 .3mf 配置文件使用。如下的配置文件已通过测试，可以在对应耗材的 Wiki 页面中下载。**

- [PLA Aero](../knowledge-sharing/studio-settings-for-rc-models.md)

  1. [PLA Aero 配置文件（花瓶模式）](https://wiki.bambulab.com/knowledge-sharing/rc-with-lwpla/pla_aero_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6(%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F)-%E6%96%B0.3mf): 请根据实际模型结构、用途和切片预览情况来确定是否手动添加顶部壳体层数
  2. [PLA Aero 配置文件（非花瓶模式）](https://wiki.bambulab.com/knowledge-sharing/rc-with-lwpla/pla_aero_%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6(%E9%9D%9E%E8%8A%B1%E7%93%B6%E6%A8%A1%E5%BC%8F)-%E6%96%B0.3mf)
- [ASA Aero](../filament-acc/filament/asa-aero-printing-guide.md)

  1. [ASA-Aero 配置文件](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/asa-aero.3mf)

#### 工程耗材

**如您使用工程材料，我们亦在相关 Wiki 中提供了常见问题的解决方案与参数建议，请根据需求进行查阅。**

## 打印完成后的耗材保存

打印完成后，若长时间不使用耗材，建议您对耗材进行防潮保存，并妥善收纳耗材末端，以防散开和缠料等风险。良好的存储可以延长耗材寿命并保持打印质量。

### 耗材存储要点

1. **防潮保存**：环境湿度较高会导致耗材吸湿变形或性能下降，因此防潮保存是首要任务。
2. **线头收纳**：耗材末端如不固定容易散开或缠绕，应及时整理并固定在料盘侧面。

#### 有官方自动供料系统（AMS）

AMS（自动供料系统）大多数型号都配备智能湿度检测功能，AMS 框架为气密封闭结构，可以保存耗材并提供湿度参考。  
建议定期更换 AMS 内的干燥剂，使仓内湿度保持在较低水平，避免耗材受潮。

![22.png](https://wiki.bambulab.com/filament-acc/beginner/22.png)

#### 普通耗材（无 AMS）

对于未使用 AMS 的耗材（如外挂料盘或普通料卷），建议使用密封袋或干燥箱保存：

1. **整理并固定耗材末端**  
   将耗材末端固定在料盘侧面，避免散开或缠绕，如下图所示：

   ![](https://wiki.bambulab.com/filament-acc/beginner/img_v3_02ps_95bc30d4-c148-436e-906f-a665ba12388g.jpg)
2. **密封防潮保存**  
   将耗材与干燥剂一起放入密封袋，排出多余空气保存（原包装破损时可使用自封袋代替）：

   ![](https://wiki.bambulab.com/filament-acc/beginner/img_v3_02ps_90f9e056-0390-446c-af11-3773614ebe2g.jpg)

### 长期存储

> **重要提示**：不使用耗材时，**务必固定好耗材末端**，以免造成耗材散开或缠绕等后果。

对于吸湿性较强且需要长期保存的耗材，可以使用专用防潮箱。  
参考开源模型网站的存储案例，例如[在 MakerWorld 中搜索“米桶”](https://makerworld.com/zh/search/models?keyword=%E7%B1%B3%E6%A1%B6)，可以获取更多耗材存储方案。

![](https://wiki.bambulab.com/filament-acc/beginner/image-33.png)

## 温馨提示

- 拿到新的耗材请**不要解开耗材上的任意一个固定带**，在完全放入 AMS 后再解开，并且放入时需要用手固定住耗材末端，以免耗材散开。
- 每次打印前请检查料盘是否缠绕，若发生缠绕请解开缠绕结以保持进料顺畅，避免打印中途卡料，以致打印失败；
- 打印前请做好准备工作，打印后需定期维护设备（可以在 [wiki](../home.md) 中搜索维护并找到对应机型参考操作），有助于延长打印机寿命。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
