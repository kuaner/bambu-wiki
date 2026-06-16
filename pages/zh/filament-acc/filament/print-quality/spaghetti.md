---
path: zh/filament-acc/filament/print-quality/spaghetti
title: "3D 打印炒面问题排查与解决方案"
description: "本文介绍了首层炒面与打印过程中炒面的常见原因与针对性的排查方法。"
tags: []
created: 2026-05-29T06:49:55.699Z
updated: 2026-06-15T06:22:15.399Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/spaghetti
---

## 问题概述

“炒面”是 FDM 3D 打印中最常见的打印问题之一。当模型在打印过程中出现翘边、悬垂塌陷、或未能与打印板粘附等异常时，喷嘴会继续按 G-code 路径在空中挤出耗材，最终在打印区域内堆积成一团杂乱缠绕、形似炒面的废料。炒面不仅会导致打印件报废，还可能造成耗材浪费、喷嘴粘料、设备清理困难等连锁问题。

本文分别介绍了**首层炒面**与**打印过程中炒面**的常见原因与针对性的排查方法，帮助您系统应对炒面问题。

请根据问题发生的时间跳转对应章节了解详情：

- 打印刚开始，发生炒面，请跳转：[首层炒面](#%E9%A6%96%E5%B1%82%E7%82%92%E9%9D%A2)
- 模型已成型一定高度后发生炒面，请跳转：[打印过程中炒面](#%E6%89%93%E5%8D%B0%E8%BF%87%E7%A8%8B%E4%B8%AD%E7%82%92%E9%9D%A2)

|  |  |
| --- | --- |
|  |  |

> 💡 **小贴士：**
>
> 当您打印的是**一盘多件**任务，且只有**部分零件**发生了炒面时，无需取消整个打印任务，可以先使用 **「零件跳过」** 功能跳过失败的模型，让打印机继续完成其余完好的模型，最大程度减少耗材和时间的浪费。详细操作指南请参考：[零件跳过](../../../general/skipping-objects.md)。
>
> |  |  |
> | --- | --- |
> |  |  |

## 首层炒面

**现象描述:**

失败发生在**第 1 层至前几层**。耗材未能粘附在热床上，被喷嘴反复拖拽，在打印区域内形成乱丝团；或模型首层打印不完整，出现变形与缺损。

|  |  |
| --- | --- |
|  |  |

**原因分析:**

首层炒面的**直接原因**是首层耗材未能与打印板牢固粘附。

**解决方案:**

### 1. 清洁打印板

打印板表面残留的灰尘、油污或指纹会显著降低耗材粘附力，是导致首层炒面**最常见**的原因。

因此，建议打印前**使用温水 + 洗洁精 + 全新 / 无油污的海绵清洗打印板**；清洗后避免用手指直接接触打印板表面，建议从侧面手持打印板。

**详细清洁方法**请参考 [纹理 PEI 板清洁指南](../../acc/pei-plate-clean-guide.md)。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E6%B8%85%E6%B4%97%E6%89%93%E5%8D%B0%E6%9D%BF.jpg)

### 2. 检查打印板类型

切片时选择的 **「打印板类型」** 必须与实际使用的打印板**完全一致**，错误选择往往会导致模型粘附失败。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/image1.png)

### 3. 执行**自动热床调平**

热床调平异常会导致喷嘴与打印板的距离不均匀，部分区域出现首层不粘。

- 请在打印机屏幕上进入“**校准**”-“**打印校准**”，重新进行**自动热床调平**。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E6%A0%A1%E5%87%86cn.jpeg)

- 检查打印板的背面是否有耗材碎屑等异物，确保打印板平整贴合热床。
- 如果自动调平后仍存在异常，可参考下方指南进行热床手动调平：

  - [X1 / P1 系列热床手动调平](../../../x1/manual/manual-bed-leveling.md)
  - [P2S & X2D 热床手动调平](../../../p2s/maintenance/manual-bed-tramming.md)
  - [A1 mini 热床手动调平](../../../a1-mini/maintenance/manual-bed-tramming.md)
  - [A1 热床手动调平](../../../a1/maintenance/manual-bed-tramming.md)
  - [A2L 热床手动调平](../../../a2l/maintenance/manual-bed-tramming.md)
  - [H2D & H2C 热床手动调平](../../../h2/manual-bed-leveling.md)

### 4. 烘干耗材

耗材受潮后，水分在喷嘴内汽化会导致挤出不均匀，进而影响首层粘附。建议在打印前对耗材进行烘干，此外，长期未使用的耗材建议密封存储，并在容器内放置足量干燥剂。

> 📖 详细烘干方法请参考 [**耗材烘干操作指南**](../dry-filament.md)。

![](https://wiki.bambulab.com/filament-acc/filament/pla-pure/3.3dry_the_filament_zh.png)

### 5. 降低首层打印速度

较慢的首层速度可以让耗材有更多时间与打印板充分粘合。建议首层外壁速度 ≤ 30 mm/s，首层填充速度 ≤ 60 mm/s。

![](https://wiki.bambulab.com/filament-acc/filament/print-quality/spaghetti/reduce_first_layer_print_speed.png)

## 打印过程中炒面

打印过程中炒面是指模型已成型一定高度后发生炒面。常见现象有以下三种：

### 模型翘边导致炒面

**现象描述**：模型边角在打印过程中逐渐翘起，当翘起高度超过喷嘴间隙时，模型会被喷嘴撞飞或整体脱离热床，导致后续耗材在空中堆积形成炒面。该问题常见于 ABS、ASA、PC、PA、PA-CF 等高收缩耗材。

![打印机检测到炒面缺陷](https://wiki.bambulab.com/h2/troubleshooting/hmscode/0c00-0300-0003-0008/images-4_cn.png)

**解决方法：**

1. **清洁打印板**：使用**温水 + 洗洁精 + 全新 / 无油污的海绵**清洗打印板；清洗后避免用手指直接接触打印板表面，建议从侧面手持打印板。详细清洁方法请参考 [**纹理 PEI 板清洁指南**](../../acc/pei-plate-clean-guide.md)。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E6%B8%85%E6%B4%97%E6%89%93%E5%8D%B0%E6%9D%BF.jpg)

2. **检查打印板类型**：切片时选择的「打印板类型」必须与实际使用的打印板**完全一致**，错误选择往往会导致模型粘附失败。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/image1.png)

3. **启用 Brim 加强首层粘附**：教程请参考 [Brim 设置指南](../../../software/bambu-studio/auto-brim.md)。

![](https://wiki.bambulab.com/filament-acc/filament/pla-pure/outer_brim.jpg)

> ℹ️ 如果模型仍然容易翘边、倒塌，请参考 [**模型翘边、脱落或倒塌问题排查指南**](warping-falling-off-collapsing.md) 来调整 Bambu Studio 切片参数进行优化。

4. **执行热床调平**：

   - 在打印机屏幕上进入“**校准**”-“**打印校准**”，重新进行**自动热床调平**。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E6%A0%A1%E5%87%86cn.jpeg)

- 检查打印板的背面是否有耗材碎屑等异物，确保打印板平整贴合热床
- 如果自动调平后仍存在异常，可参考下方指南进行热床手动调平：

  - [X1 / P1 系列热床手动调平](../../../x1/manual/manual-bed-leveling.md)
  - [P2S & X2D 热床手动调平](../../../p2s/maintenance/manual-bed-tramming.md)
  - [A1 mini 热床手动调平](../../../a1-mini/maintenance/manual-bed-tramming.md)
  - [A1 热床手动调平](../../../a1/maintenance/manual-bed-tramming.md)
  - [A2L 热床手动调平](../../../a2l/maintenance/manual-bed-tramming.md)
  - [H2D & H2C 热床手动调平](../../../h2/manual-bed-leveling.md)

### 悬垂区域塌陷导致炒面

**现象描述**：模型悬垂部分由于缺少支撑或冷却不足而塌陷，喷嘴撞到塌陷区域后造成连锁失败。

![](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E6%82%AC%E5%9E%82%E5%AE%9E%E7%89%A9-cn_compressed.png)

**解决方法**：

- **开启支撑**：具有悬垂区域的模型，打印时可能会因为**缺少支撑**而塌陷，形成炒面。因此，请检查模型是否具有角度大于 45° 的悬垂区域，若有，请在 Bambu Studio 支撑栏中**启用支撑结构**。

  > ℹ️ 支撑功能的更多信息详见 [支撑耗材与支撑功能的介绍](../../../software/bambu-studio/support.md)。
- **悬垂降速**：在 **Bambu Studio** 左侧栏的 **“工艺”** 栏中，点击 **① “速度” → ②** 勾选**悬垂降速**，并参照**下图参数**修改“**悬垂速度**”。

  ![](https://wiki.bambulab.com/filament-acc/filament/pla-pure/3.1_overhang_zh.png)

  > 📖 完整的悬垂优化方案请参考 [如何打印模型悬垂部分](overhang.md)。
- **支撑降速**：在 **Bambu Studio** 左侧栏的“**工艺**”栏中，点击 **① “速度” → ②** 参照下图参数修改“**支撑**”与“**支撑面**”速度。

  |  |  |
  | --- | --- |
  |  |  |

必要时可点击 **① “支撑” → ② “类型”**，改为“**普通支撑**”，以获得更佳的支撑面。

- **普通支撑**：适合结构规则、体积大、稳定性强，适合大面积悬空或对承重要求高的模型（如下图右边模型）。
- **树状支撑**：适合接触点少、节省材料、极易拆除，特别适合细节丰富或几何形状不规则的模型（如下图左边模型）。

![support_type.png](https://wiki.bambulab.com/filament-acc/filament/print-quality/spaghetti/support_type.png)

### 喷嘴剐蹭导致炒面

**现象描述**：打印中听到「咔哒」声，之后模型被整体撞飞，同时发生炒面。

**可能的原因：**

- A. Z 轴抬升不足：喷嘴空驶时刮蹭模型已打印部分
- B. 模型重心不稳、与打印板接触面小：模型本身站不稳，喷嘴正常接触即可晃倒

**解决方法**：

**针对原因 A：修改 Z 抬升方式**

在 **Bambu Studio** 左侧栏的“**打印机**”栏目，点击打印机右上角的 **① 编辑符号**，在弹出的窗口中选择 **② “挤出机” → ③ “Z 抬升方式”** 改为“**普通**”。

|  |  |
| --- | --- |
|  |  |

**针对原因 B：增强模型稳定性**

1. **启用 Brim 增大首层接触面积**

- 在 Bambu Studio 左侧栏 **「工艺」** 栏中，选择 **「其他」**→**「Brim 类型」**→**「仅外侧 Brim」**；
- 推荐 Brim 宽度 5 ~ 8 mm，接触面越小可适当加宽；
- 详细教程请参考 [Brim 设置指南](../../../software/bambu-studio/auto-brim.md)。

![](https://wiki.bambulab.com/filament-acc/filament/pla-pure/outer_brim.jpg)

2. **使用手绘支撑加固关键位置**

- 针对模型分叉、细长结构等几何特殊位置，使用手绘支撑添加额外稳定结构；
- 详细教程请参考 [支撑绘制](../../../software/bambu-studio/support-painting.md)。

![](https://wiki.bambulab.com/software/bambu-studio/support-painting/screenshot-20250213-114524.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
