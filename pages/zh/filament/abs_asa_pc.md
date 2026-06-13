---
path: zh/filament/abs_asa_pc
title: "ABS / ASA / PC 使用指南"
description: ""
tags: ["耗材"]
created: 2025-10-11T00:14:18.253Z
updated: 2026-06-12T09:24:05.200Z
source: https://wiki.bambulab.com/zh/filament/abs_asa_pc
---

> **重要提醒**：由于 ABS 与 ASA 材质特性，其在打印过程中会**释放带有刺激性气味的气体**，因此打印时必须确保环境通风良好，避免在密闭空间操作。

## 耗材基本信息

### 耗材介绍

以下为五款工程耗材的核心特性简述，如需更详细的产品信息，可点击对应 “商品详情” 链接查看。

|  | **ABS** | **ASA** | **ASA Aero** | **PC** | **PC FR** |
| --- | --- | --- | --- | --- | --- |
| **介绍** | 具有良好耐热性和抗冲击性的工程塑料，适合功能零件（如下图所示），但打印难度较高。 | 具备卓越抗紫外线能力的户外专用材料，是 ABS 的升级版。 | 极轻量化的发泡材料，兼具耐候性，专为航模和轻量化应用设计。 | 高强度、耐高温的高性能工程塑料，适用于工业部件。 | 拥有顶级阻燃等级（V-0）的聚碳酸酯，满足严格的防火安全需求。 |
| **商品详情** | 国内商详：[ABS](https://detail.tmall.com/item.htm?abbucket=9&id=694264787018&pisk=grGrkwbsmQdy84SXNmFFuQEMvVF8gW-_-XZQ-203PuqkpLhULViDye33AXPEDm2nN7gS0koISYi7NJOngya1ryfuEi205yenAkg5yxnsS_GWeW1UwWFHfhO61U389W4YnepCyS4QJMAQE_20wyNJufbv1438vaSH5xA18hLnULX3xDV0nzaatyf3-EP0SyVhZJfoooqY-WVhEWV0iyUQrMqnxtA0Wy6ht_fhmq4QrWqnxWYqooUUtkm3tEumMx0o-sz_EErpUhmMHYwzj4qV_qh4rjB-Po7F-jo_UlA_06fngzuf_AXP_pZiBuw_YmAfaWu08mysUh5rY20tK-lFqUiimvo3kxKFLlknPAH33UAou7rrbjncr9PrK0hUeY7pWqVoDAETEKKYubG_LleVm30juu2ZL0tAtuMZomysGi1_sAnqTRVG4bSLoMFo9YShL84YulT2uyISbE8ixBB1p9e06rr6Pz6hKGtGOTlN19BLnrz4fU1h.&rn=e877f59b47f666c321fc4e2bc1d98a92&spm=a1z10.5-b-s.w4011-25176969463.40.57eb38563mEcBk)海外商详：[ABS](https://asia.store.bambulab.com/products/abs-filament) | 国内商详：[ASA](https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-25176969463.48.57eb38563mEcBk&id=718106932700&rn=e877f59b47f666c321fc4e2bc1d98a92&abbucket=9&pisk=g59ok0VrxQ55vw27ZDXSwQwwpAlAwT6CveedJ9QEgZ7jA0t-OJoHJeCUp3hSxDbDRaCRU46hYFL1yMFJ4tPV2MUP485U3Z7DzJCJKHwhYH8IVwnSM3t5d9utWeD9V3NKoBnpK_y4ggtVYyyEMtuSJVljWAH9mbS5pnu9pE_Z8iITL95PTxyVlMUUTe5z0x7fAMzPLaoD0Z_44w5Pan5VvgyFL85z0tSCXuyPT8-20ZsFLg8FLmXVlMWF8eWEgUeFSpJX32JKTszD-YJfq_bw4a-J2KzAa7tVoXcenFCP7AQ0LJJcqneM_72i9NR1y1QHuxelKnSHo1doS8YHYhOFip4r2F82teSXG2VhSB-J1B5m4Y-cEaYMhErztTAePpfWZki60T8X1N1rGqsDedCh5s4qznKcz1AHyqwFyCx2o1pYkRBw1Evh_OSz8SPaB62C0Dp4OW1Pcib9iCRvsXxldHimm5G5ais-Wpn0tnz_LR0immV_s_Sf2I5..)海外商详：[ASA](https://asia.store.bambulab.com/products/asa-filament) | 国内商详：[ASA Aero](https://detail.tmall.com/item.htm?abbucket=9&id=782811914568&pisk=gi9rkZZ6oYHyoKajFEBU0YQiJhBR99u1xp_CxHxhVabo9bpFThTm2DKhRpWekEfHFTtWuw8BjQT5F6MH3Ms_qM2lZrfcfMCHRwt72IL6j89Sw9wFe9Bn5VMsC0KRp9jAiDhQ2tjFx8DCq_qceM6-0dqxC3KRJuznfID_YVnHPbVh-eXcigs1KM2hxmWcjgW3E62kmZbAx9X3Z9XcnMICqybH-rqcYgjlq7flm-jNq9bH-9m2mZIFKwYhKm-mgJtkx-S1Zm7KaVYgoS1lS3b4KRrO4_0B4WwLpnSla3KluisX3g5PSse0o_vklHvWeshzZ9KX_eRHSqN5rCSwu1Or788wyMxFxUkTbZvyYK5JGzVlbT7PsLY0XctNtIJVFL0L6ntVr1WXGj35OT8y6NCoMqLe0aTHUs4rlwO6cLf2Sqw2J6RHFtvooASPayI0JTvpayVFZiIV5moVvzTZ0cYnp5NL9sXO0Ni5VWV35V2Qady_9WCc0i7sVJf..&rn=e877f59b47f666c321fc4e2bc1d98a92&spm=a1z10.5-b-s.w4011-25176969463.56.57eb38563mEcBk&skuId=5344601428372)海外商详：[ASA Aero](https://asia.store.bambulab.com/products/asa-aero) | 国内商详：[PC](https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-25176969463.36.57eb38563mEcBk&id=693741117439&rn=e877f59b47f666c321fc4e2bc1d98a92&abbucket=9&pisk=gMDqlrjIrKpV0H_Wh4eN4KUHWDeYhR8QjAa_jcmgcr4D6IHa_DgkDhng5AyZy4Vih-ijzPusxjgbh59iUlZCmlX0iaVuAlFi5PifDb3IxtMXMR6aHReMRe9BdnnYBRq8Zhd1kLqQjdZ0jo2YE-YZKQpBdmnPcoxIqpM6JyDz41XiSSVkEkUujNqiS8XuczX0jt2gr3rTrRj0IS2oqlrNSO0gjL4uxkq0mSX0qzqbrP2gIVmk4lauSR2iS0cAimmGUkND4Pd2-2ATxSznmzWE2Yr0qsn4zN7iU2N4-9aPIODz006EtsWe1ycLlWaZrL64Q0qZzWG28tuZjDhgaA7Dc20o_Vq-wF5a8fmj9fVymKmz3ruEe4jc_-likAPxgGKKq-0-9yFDwUErhvNaJ77ko0izoWlZlUBglXoozWM5P9wn94katJjPTNElW-DtgNfaiuEzR3-zXZge4H0MB61O672L4ytbc1fGReX1gvWC61Fu4uzBcOf..)海外商详：[PC](https://asia.store.bambulab.com/products/pc-filament) | 国内商详：[PC FR](https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-25176969463.44.57eb38563mEcBk&id=867797040833&rn=e877f59b47f666c321fc4e2bc1d98a92&abbucket=9&pisk=gHyjk3OrQEYXgMNKGASyNEmKfdD6CgWE6hiTxlp2XxHx1Aaz7IkNi1VSXzzsQArOoPwsyPjDQi245fEqPmd9MfL-eDnwMKETQcesn8P2Qq7mClUECw7FL9r0mYDO8wlu2CGinc9xXdLZyunECmHfNwwUmADO53JOT9Z0oKv8Rnnt2giZbndYWfKJw4m6DCUtkbL-jcDtWPUOeunZfVntMdnRVmmekEdvHun-jmpvHPHOVu3oXAnYWAI724mtgaKIfsg0cMCmrqtfQHrmPdpTF0QiJoOwC0yxccgQDlJ6CGmjG2ExPw2U5LG8jfwMjdGLDW4ivrLA5V272-FLJaRqkWi_Y5ZAHLH4noFK6JQM6yMb5XexNhI_0o3sF0edbB0zFqzThbIedfk8LXHYa_bq_xiQW-4XfdUL4kymZR_ByVVqxYn_IMds5fIrRpuQS8O6VXvsV2S5VCAMDDyOJDEN1wlxqmGPVgTYsev9IgwNVIVKM0mjJgsWk71..)海外商详：[PC FR](https://asia.store.bambulab.com/products/pc-fr) |

![abs.jpg](https://wiki.bambulab.com/filament-acc/abs-asa-pc/abs.jpg)

### **核心特性**

下表对比了各耗材与 PLA Basic 的关键性能参数，包含强度、韧性、耐热性等，同时提供技术参数表（TDS）与化学品安全说明书（MSDS）的下载链接。

| 特性 | PLA Basic | ABS | ASA | ASA Aero | PC | PC FR |
| --- | --- | --- | --- | --- | --- | --- |
| 强度 （弯曲强度-XY） | 76 Mpa | 62 Mpa | 65 Mpa | 58 ± 6 MPa | 108 Mpa | 90±4 Mpa |
| 韧性（冲击强度-XY） | 26.6 KJ/m² | 39.3 KJ/m² | 41 KJ/m² | 32.0 ± 2.5 kJ/m² | 34.8 KJ/m² | 55±2.1 KJ/m² |
| 层间附着力（冲击强度-Z） | 13.8 KJ/m² | 7.4 KJ/m² | 4.9 KJ/m² | 3.4 ± 0.5 kJ/m² | 9 KJ/m² | 8±0.4 KJ/m² |
| 耐热性（HDT，0.45 MPa压力） | 57 ℃ | 87 ℃ | 100 ℃ | 85 ℃ | 117 ℃ | 113 ℃ |
| 技术参数表下载 （TDS） | [TDS-PLA](https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_pla_basic_technical_data_sheet.pdf) | [TDS-ABS](https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_abs_technical_data_sheet_v3.pdf) | [TDS-ASA](https://wiki.bambulab.com/filament-acc/abs-asa-pc/6eaf4c432d1d4014a1975e55a55ed00b.pdf) | [TDS-ASA Aero](https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_asa_aero_technical_data_sheet.pdf) | [TDS-PC](https://wiki.bambulab.com/filament-acc/abs-asa-pc/a52afdccddfd448583d119587122c8c5.pdf) | [TDS-PC FR](https://wiki.bambulab.com/filament-acc/abs-asa-pc/4adf3c9827a0475d8777e9b8cfd11fbe.pdf) |
| 化学品安全说明书下载 （MSDS） | [MSDS-PLA](https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_pla_basic_msds.pdf) | [MSDS-ABS](https://wiki.bambulab.com/filament-acc/abs-asa-pc/bambu_abs_msds.pdf) | [MSDS-ASA](https://wiki.bambulab.com/filament-acc/abs-asa-pc/dfa0f27f3aae4ae0bb00974aea6bac88.pdf) | [MSDS-ASA Aero](https://wiki.bambulab.com/filament-acc/abs-asa-pc/b71c59a936ff48c09e0a8273888d9c84.pdf) | [MSDS-PC](https://wiki.bambulab.com/filament-acc/abs-asa-pc/2208b0211816466bb1fa591e5c9c0c3b.pdf) | [MSDS-PC FR](https://wiki.bambulab.com/filament-acc/abs-asa-pc/74e912f5fa17467c94e92af2ab913346.pdf) |

### 硬件兼容性

| 材料 | 机型兼容性 | 喷嘴兼容性 | 打印板兼容性 | 配件兼容性 |
| --- | --- | --- | --- | --- |
| **ABS / ASA / PC / PC FR** | 需要封箱打印机，不适配 **P1P** 与 **A** 机型 | 兼容所有喷嘴( P2S/X2D 机型不支持 0.2mm 喷嘴打印 PC/PC FR) | 需涂胶打印，不适配低温增稳板 | **AMS lite 不兼容** |
| **ASA Aero** | 同上 | 兼容 **0.4mm 喷嘴**，不建议使用其他规格喷嘴 | 建议使用 **光面 PEI 打印板** 并涂胶打印，不适配低温增稳板 | 同上 |

## 打印准备

**打印准备的核心要点**：

- 通风与安全：打印时保持良好通风，避免在生活区使用；带滤芯的机型建议定期更换活性炭过滤芯。
- 耗材干燥：ABS / ASA / PC 易吸湿，打印前务必烘干（约 80 ℃×8 h），并用密封盒或 AMS + 干燥剂保存。
- 打印床准备：清洁打印板，建议涂固体胶增强附着，防止翘边。
- 温控管理：提高腔室温度可减少翘边；若无腔温控制，可提升热床温度；打印时避免过高填充率与过厚外壁。

> **健康与设备要求**  
> 1.**通风要求**：打印全程需处于通风良好的环境，避免异味积聚。  
> 2.**健康提示**：ABS/ASA 在打印时会挥发有毒物质，切勿在卧室、客厅等生活区域长时间打印。  
> 3.**设备维护**：X/P/H 系列打印机配备活性炭过滤功能，需定期更换滤芯，建议累计打印 1440 小时（60 天）后更换一次。

### 烘干耗材与密封保存

ABS、ASA、PC 类耗材易吸水受潮，潮湿会导致打印件强度下降、表面气泡、拉丝等问题，因此打印前需进行烘干处理，具体烘干参数如下。

> 提示：烘干流程可以参考[耗材打印前的干燥指南](../filament-acc/filament/dry-filament.md)。

### 材料烘干参数对照表

| 耗材类别 | 鼓风式烤箱 | 热床 | AMS HT |
| --- | --- | --- | --- |
| **ASA Aero** | **80 °C × 8 h** | 90 – 100 °C × 12 h | 80 °C × 12 h |
| **ABS / ASA / PC / PC FR** | 75 – 85 °C × 8 h | 90 – 100 °C × 12 h | 80 °C × 12 h |

> **注意：**
>
> 1. **ABS 银色耗材** 为确保表面光泽，需严格遵守烘干条件。
> 2. **建议**：拆封后立即烘干。
>
> - 鼓风式烤箱：**85 °C × 12 h**
> - 热床：**90–100 °C × 18 h**，并**每隔 6 小时翻面一次**。
>
> 3. 使用热床烘干时，请在耗材上方覆盖**耗材包装盒或 PC 盒**，以保持受热均匀。

### 准备打印板

ABS / ASA / PC 这三类耗材属于高温耗材，打印时会存在翘边问题，主要是以下两点原因造成：

1. 材料熔融加工时普遍存在的热胀冷缩物理特性导致收缩翘曲。
2. 玻璃化转变温度较高，分子链在较低环境温度下的各向异性松弛会产生较大的内应力，导致模型收缩翘曲。

因此需做好以下准备：

1. **清洁打印板**：打印前彻底清洁打印板表面，去除残留杂质；
2. **涂抹固体胶**：建议使用官方固体胶增强粘附力，显著提升打印成功率，具体操作可参考 [Bambu Lab 胶水使用指南](../general/how-to-use-bbl-liquid-glue.md)。

![image90.png](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image90.png)

### 提高打印机仓内温度

适当提高打印腔室温度，可有效减少打印过程中材料收缩导致的内应力，提升 ABS、ASA、PC 等工程材料打印的成功率和成品质量。

- 主动腔温：  
  H2 系列、X1E、X2D 配备主动腔温控制系统，可以很好地抑制模型翘边。默认参数即可自动开启。  
  如果需要额外设置腔体温度，可以参考 [Bambu Studio 腔温设置指南](../software/bambu-studio/chamber-temperature.md)。

|  |  |
| --- | --- |
| 有腔温控制时模型边缘平整 | 无腔温控制时模型底部发生翘边 |

- 使用热床预热增温：  
  增加热床温度间接提高仓温若环境温度较低，X1C 与 P1S 在打印前可以先升高热床温度至最高，预热 15min 后发起打印。

同时在参数上尽量避免填充率大于50%，墙层数大于6层，以降低收缩趋势；对于大多数对强度要求较低的非结构件，则可以直接选择默认的 2 层墙和 15% 的填充率。具体可以参考[模型翘边处理指南](../knowledge-sharing/printed-model-warping.md)。

![image93.png](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image93.png)

### 发泡耗材打印建议（ASA Aero）

与其他工程耗材不同，ASA Aero 流动性强、体积膨胀明显，空驶过多易漏料，因此**不推荐打印空驶较多的复杂模型**。如下图左侧所示的测试件就有许多空驶路线。

**预设配置文件**可以帮助您获得更好的打印参数。您可以下载下面的 3mf 文件，在 Studio 打开后导入目标打印模型，便可获得下述的推荐预设（用其他型的打印机打印时，可迁移下述 X1C 的相应的工艺参数和耗材丝参数）：

- X1C，0.4 mm 喷嘴：[asa-aero.3mf](https://wiki.bambulab.com/filament-acc/filament/asa-aero-printing-guide/asa-aero.3mf)

![image95.png](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image95.png)

## 耗材保存及模型后处理

### **耗材密封保存**

干燥线材后，在使用过程中要把它放在带有干燥剂的密封盒或 AMS 中，防止它再次受潮。如果将线料存放在 AMS 内，请确保 AMS 内干燥剂有效，并始终将 AMS 扣好。如果发现干燥剂无效（建议定期更换干燥剂），请在下次打印前更换干燥剂并烘干耗材。

### 模型后处理

模型[打印结束后的工作（取下模型、清洁打印板、外观处理、退火、胶水粘结等）](../filament-acc/acc/print-finish-adv.md)有相关的处理操作提示，具体可以点进链接中查看。

> 打印机维护提示：
>
> - 打印 ABS、ASA 等耗材，会有挥发物质在打印机内聚集。较多的挥发物质聚集会导致碳管阻力变大、打印机精度下降。建议每打印完5卷（5千克）ABS、ASA 耗材进行一次清洁。
> - 需要注意的是，挥发物同样会聚集在上盖玻璃、玻璃门以及其他部件上，您可以一并用清洁剂擦拭清理。
> - 清洁教程可以参考：[碳管的清洁指南](../general/carbon-rods-clearance.md)

## **常见打印问题与解决方案**

### 模型翘边

相较于 PLA，工程耗材打印过程中更易出现收缩翘曲问题，可以参考以下两个方法减少翘边风险。

![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-4.png)

#### 增加打印板和模型粘附

- 增加打印板的粘附：涂抹固体胶（如下左图）
- 开启裙边：增大模型与打印板接触面积（如下右图）  
  ![image-23.png](https://wiki.bambulab.com/filament-acc/petg/image-23.png)

#### 控制腔体温度以延缓收缩

1. 主动腔温功能  
   部分打印机配备**主动腔温功能**，能够显著抑制模型翘边问题。具体操作可参考 [Bambu Studio 腔温设置指南](../software/bambu-studio/chamber-temperature.md)。
2. 通过热床提升仓温

对于不具备主动腔温的机型，可以通过提高热床温度来间接增加仓温。  
在环境温度较低时，建议 **X1C 与 P1S** 在打印前将热床加热至最高温度，并**预热 15 分钟后再启动打印**。

3. 参数优化建议

- 避免使用 **超过 50% 的填充率**，以减少材料收缩趋势。
- 对于大多数对强度要求不高的非结构件，可直接采用**默认的 2 层墙 + 15% 填充率**。
- 更多细节可参考官方[模型翘边文档](../knowledge-sharing/printed-model-warping.md)

### 层间开裂

导致下图所示**层间开裂**的根本原因是：模型在打印过程中产生的**冷却内应力**大于其**层间粘接力**，从而使模型表面出现裂纹。这种情况常见于打印 **ABS、ASA、PC** 等高温材料时。可以根据下面的表格进行自查，具体问题具体分析。

![q14ybaqg2opcokxahw8c1urencd.png](https://wiki.bambulab.com/filament-acc/abs-asa-pc/q14ybaqg2opcokxahw8c1urencd.png)

| 问题类别 | 可能原因 | 改善方法 |
| --- | --- | --- |
| **挤出不足** | - 耗材熔融不充分，导致熔体粘度高、流动性差； - 喷嘴堵塞，挤出不畅。 | - 适当**提高喷嘴温度**或**降低打印速度**，确保耗材充分熔融； - 若为堵塞，**清洁或更换喷嘴**。 |
| **粘接强度或结构问题** | - 层间粘接力不足； - 模型局部结构过薄或支撑不足。 | - **增加墙层数**或**提高填充率**，增强整体强度和层间结合力。 |
| **冷却过度** | - 风扇转速过高，导致冷却过快； - 打印腔温过低，模型热收缩应力大。 | - **降低风扇转速**，避免过度冷却； - **提高热床温度**，并**关闭前门、盖上顶盖**，保持腔内温度稳定。 |

### 模型表面出现环形凸起纹路

在盒子类模型的大底面与薄壁交界处，或小船模型的腰部区域，外壁表面可能出现异常的环形凸起纹路，这类现象我们通常统称为变截面类层纹。若想要彻底解决此类问题，最推荐的做法是直接为模型添加一个内侧圆角。

![image-29.png](https://wiki.bambulab.com/filament-acc/pla/image-29.png)

> 注意：加内侧圆角需要在其他建模软件如 **Fusion 360 / SolidWorks** 中操作。

- 模型增加内侧圆角后，切片后桥接将不再与内墙接触。

![](https://wiki.bambulab.com/filament-acc/petg/image-19.png)

- 在增加了**模型增加内侧斜角**后，对模型进行切片后可观察打印轨迹，桥接几乎不与内墙接触。

> 名词解释：
>
> - 在 3D 打印 中，打印头会一层层地挤出融化的塑料丝。如果某一层的部分区域 没有下面的支撑结构，而喷嘴又要在空中跨越这段“悬空的间隙”进行打印，这段横跨空隙的部分就叫：桥接（Bridge）。
> - **桥接 = 打印机在“空中”跨越两个点之间打印一条或多条丝线，就像搭一座桥一样。**

![](https://wiki.bambulab.com/filament-acc/petg/output.gif)

> 提示：如遇到的打印问题非以上几点，可以进入该链接中根据图片展示的现象对应处理：[打印质量与解决办法](../filament-acc/filament/print-quality.md)

## 进阶调整

### 使用 ASA Aero 打印航模

ASA Aero 适用于航模打印，需结合**航空模型的轻量化需求**进行参数调整。

> 提示：下载下面的 .3mf 文件，在 Studio 打开后导入目标打印模型，便可获得下述推荐预设（以 X1C 机型为例）：
>
> - [asa-aero.3mf](https://wiki.bambulab.com/filament-acc/abs-asa-pc/asa-aero.3mf)
>
> 另外，用其他型的打印机打印时，可直接迁移上述 X1C 的相应的工艺参数和耗材丝参数。

以下为针对**流量比例、工艺质量、工艺强度、工艺速度和工艺支撑**的关键调整方向与参考值。

#### 核心参数调整步骤

##### 1. 调节流量比例

为了获得不同的发泡效果可以通过调节流量比例值来控制，**推荐：0.42 - 0.7 。** 具体数值需要根据实际情况进行调节，不同运用场景和机器会有不一样的最佳参数值。

![image96.png](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image96.png)

**补充说明：** 在打印航模时需要考虑打印温度与性能关系，即其轻量化需求，Bambu ASA Aero 的最大发泡倍率、最小打印件密度与打印温度的关系大致如下，不同模型的实际所需流量比例、成品密度可能有所不同：

> 下面测试参数表格的**条件说明**：喷嘴尺寸为 0.4 mm，打印速度为 80 mm/s，模型尺寸为长\*宽\*高 = 80\*10\*4 mm³（XY 方向）。

| **打印温度 /°C** | 220 | 230 | 240 | 250 | 260 | 270 |
| --- | --- | --- | --- | --- | --- | --- |
| **最小流量比例** | ~ 0.93 | 0.9 | 0.74 | 0.6 | 0.51 | 0.45 |
| **最大体积倍率** | ~ 100% | 106% | 128% | 158% | 186% | 211% |
| **最大发泡倍率** | ~ 0% | 6% | 28% | 58% | 86% | 111% |
| **最小打印件密度 (g/cm³）** | ~ 0.97 | 0.92 | 0.78 | 0.61 | 0.52 | 0.46 |

##### 2. 工艺质量参数调整

为了提高其打印的质量可以调节以下几个参数。

![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-10.png)

##### 3. 工艺强度参数调整

调节壳体数量可避免反复的空驶。

![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-122.png)

### 提高表面质量——减少空驶，逐件打印

单层打印时间对打印件的层间粘接强度有很大影响，一般而言，单层打印时间越长，小模型的层间粘接强度越低（上一层早已完全冷却）。若需要打印多个小件，**建议不要放在一整盘中选用逐层打印（默认的打印顺序是逐层打印）**，而应该尽量一次只打少数几个，且最好把模型**分组**甚至**分盘**后选用**逐件打印**方式。

![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-17.png)

![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-18.png)

### 提高模型强度

1. **改变墙层数以及稀疏填充密度**

我们可以通过改变墙层数以及稀疏填充密度来改善模型的强度。推荐墙层数不大于6层，填充密度不大于50%，并选择**螺旋体**为稀疏填充图案（如下图所示）；具体参数需要**根据实际情况减小调节幅度**，否则会有**翘边**风险。

> 注意：提高墙层数以及稀疏填充密度后会增大耗材冷却收缩的翘边风险，建议在有强度打印需求时在打印板表面[涂胶](../general/how-to-use-bbl-liquid-glue.md)打印或在 Bambu Studio 中增加 Brim 裙边。

![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-19.png)

2. **确定模型的受力方向**

在打印前，建议您先考虑模型在实际使用中的主要受力方向。然后可以根据这一方向来调整打印时的摆放角度，建议受力方向与耗材挤出平面呈90度的夹角，这样能够显著提升打印成品的强度和耐用性。

> 提示：您可以参考下方示意图，对比不同摆放方式，从而判断当前的打印摆放方式是否已经接近模型最佳的受力方案。
>
> ![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-20.png)
>
> ![](https://wiki.bambulab.com/filament-acc/abs-asa-pc/image-21.png)

> 温馨提示：
>
> 如果以上的进阶调整无法满足您的需求，可以进入到“拓竹学院”——“[Bambu Studio](https://bambulab.cn/zh-cn/support/academy)”中进行学习，这是一个 3D 打印学习平台，致力于为用户提供从基础到进阶的全方位 3D 打印知识培训，助力用户在 3D 打印领域不断提升技能，实现创新与发展。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
