---
path: zh/filament-acc/filament/asa-aero-printing-guide
title: "发泡 ASA （ASA Aero）打印指南"
description: ""
tags: []
created: 2024-04-01T07:23:45.511Z
updated: 2026-05-12T06:39:02.492Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/asa-aero-printing-guide
---

## 目的

本文指导如何使用发泡 ASA（ASA Aero）耗材切片打印航模。

## 切片打印的技巧和注意事项：

- **打印前先把耗材烘干，** 以避免材料潮湿使得挤出线条中存在气泡、孔洞，拉丝等问题。请查看[耗材准备——干燥](dry-filament.md)了解烘干温度和时长建议。
- **建议使用高温与低速打印，** 以使 ASA Aero 发泡充分、均匀，并有较强的附着力。
- **推荐选用工程打印板或光面 PEI 打印板（高温打印板）并涂胶；不推荐使用纹理 PEI 打印板，以免其凹凸纹理导致部分模型的首层过粘，使得部分模型在拆卸时底面的局部发生破损或首层和次层的薄弱处发生撕裂。**
- **打印时避免过低或过高的风扇转速，** 以确保冷却充足和避免冷却过度，从而兼顾外观质量和层间强度。
- **打印尺寸较大、填充率较高的模型时，可能会发生翘曲。**  
  抑制翘曲的方法有：  
  (1) 尽量避免打印尺寸较大、填充率较高的模型；  
  (2) 选用封闭式机型，给热床涂胶；  
  (3) 切片时适当降低打印速度、提高热床温度、打开 Brim 等。  
  要获得更详细的信息，请查阅 wiki：[常见打印质量问题和解决办法](../../knowledge-sharing/common-print-quality-problem.md)。
- **与 ASA 一样，在打印过程会释放有刺激性气味的气体，请注意封闭打印机箱和保证良好的通风。**
- **尽量一次打印单个模型，或使用 “逐件打印“ 方式一次打印少量模型，避免使用 “逐层打印“ 方式一次打印多个模型，否则打印过程会有较多的空驶、跳跃区，造成拉丝、漏料等缺陷。**

**请注意，在打印航模时，由于模型结构、尺寸具有多样性，默认的推荐打印参数无法保证完美地适配所有模型，因此，对于某些模型，可能要进行多次的参数调整、打印。**

打印件的平均密度会随着实际的打印温度、打印速度、流量比例、模型尺寸、壁厚（墙层数）和填充密度等参数的变化而变化，其一般规律如下表：

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **参数** | **打印温度** | **打印速度** | **流量比例** | **模型尺寸** | **壁厚（墙层数）** | **填充密度** |
| 参数变化情况 | 增大 | 增大 | 增大 | 增大 | 增大 | 增大 |
| 平均密度变化情况 | 减小 | 不变或增大 | 增大 | 减小 | 增大 | 增大 |

Bambu ASA Aero 的最大发泡倍率、最小打印件密度与打印温度的关系大致如下\*：

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **打印温度 /°C** | 220 | 230 | 240 | 250 | 260 | 270 | 280 |
| **最小流量比例** | ~ 0.93 | 0.90 | 0.74 | 0.60 | 0.51 | 0.45 | 0.44 |
| **最大体积倍率** | ~ 100% | 106% | 128% | 158% | 186% | 211% | 216% |
| **最大发泡倍率** | ~ 0% | 6% | 28% | 58% | 86% | 111% | 116% |
| **最小打印件密度 / (g/cm³）** | ~ 0.97 | 0.92 | 0.78 | 0.61 | 0.52 | 0.46 | 0.45 |

**说明：**

（1）测试参数：喷嘴尺寸为 0.4 mm，打印速度为 80 mm/s，模型尺寸为长\*宽\*高 = 80\*10\*4 mm³（XY 方向）；

（2）打印时，不同模型的实际所需流量比例、成品密度可能有所不同。

## 切片参数设置（图片示例为推荐用于打印的 0.4 mm 喷嘴的参数）

### 1. 使用默认 Bambu ASA Aero 参数：

**注：由于 ASA Aero 发泡倍率较高，推荐在实际打印模型时根据模型实际调整流量比例。（推荐：0.42 - 0.7 ）**

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E6%B5%81%E9%87%8F%E6%AF%94%E4%BE%8B.jpg)

### 2. 工艺质量参数调整

- 线宽设置为 0.48 mm
- 切片间隙闭合半径设置为 0.02 mm
- 桥接流量设置为 0.7
- 勾选避免跨越外墙且最大绕行长度为 90 %

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E5%B7%A5%E8%89%BA%E8%B4%A8%E9%87%8F.jpg)

### 3. 工艺强度参数调整

- 墙层数设置为 1
- 顶部壳体层数设置为 0
- 顶部壳体厚度设置为 0 mm（需要开启顶部时调整）
- 底部壳体层数设置为 2
- 稀疏填充密度设置为 0 %

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E5%B7%A5%E8%89%BA%E5%BC%BA%E5%BA%A6.jpg)

### 4. 工艺速度/加速度参数调整

- 外墙、内墙、稀疏填充、内部实心填充、顶面（需要时开启）、填缝均设置为 80 mm/s
- 普通打印调整为 5000 mm/s
- 外墙调整为 3000 mm/s

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E5%B7%A5%E8%89%BA%E9%80%9F%E5%BA%A6.jpg)

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E5%B7%A5%E8%89%BA%E9%80%9F%E5%BA%A62.jpg)

### 5. 工艺支撑参数调整（需要时开启，普通航模不推荐开启支撑打印）

- 阈值角度设置为 50°
- 顶部底部 Z 距离设置为 0.26 mm
- 顶面接触面层数设置为 3
- 顶部接触面线距设置为 0.2 mm
- 普通支撑拓展设置为 0.6 mm
- 支撑/模型 XY 间距设置为 0.6 mm

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E5%B7%A5%E8%89%BA%E6%94%AF%E6%92%91.jpg)

### 6. 工艺其他参数调整

- Brim 类型设置为仅外侧
- Brim 宽度设置为 3 mm
- Brim 与模型的间隙设置为 0.2 mm
- 擦拭塔关闭
- 切片模式设置为奇偶

![](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/%E5%B7%A5%E8%89%BA%E5%85%B6%E4%BB%96.jpg)

## 预设配置文件

下载下面的 3mf 文件，在 Studio 打开后导入目标打印模型，便可获得上述推荐预设（除 P2S 外用其他型的打印机打印时，可迁移下述 X1C 的相应的工艺参数和耗材丝参数），P2S 用户可直接下载下面的第二个文件：

1. X1C，0.4 mm 喷嘴：[asa-aero.3mf](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/asa-aero.3mf)
2. P2S，0.4 mm 喷嘴：[asa-areo@p2s.3mf](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/asa-areo@p2s.3mf)
