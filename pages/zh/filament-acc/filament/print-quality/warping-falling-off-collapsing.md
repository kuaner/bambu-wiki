---
path: zh/filament-acc/filament/print-quality/warping-falling-off-collapsing
title: "模型翘边、脱落或倒塌"
description: ""
tags: ["打印质量", "翘边", "脱落", "倒塌"]
created: 2023-12-10T05:42:42.482Z
updated: 2026-07-02T04:07:51.732Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/warping-falling-off-collapsing
---

## 速查指南

对照现象快速定位问题、查看解决办法。

**边角翘起 / 翘曲**

✅ 清洁打印板（肥皂 + 清水）  
✅ 将热床温度提高 5–10 °C  
✅ 在切片软件中添加 Brim

**打印中途模型脱落**

✅ 重新进行自动热床调平  
✅ 检查 Z 方向偏移值，首层必须被适当压实  
✅ 确认在 Bambu Studio 中选择了正确的打印板类型

**模型坍塌**

✅ 将速度和加速度降低 20–30 %  
✅ 为高而细的模型启用支撑  
✅ 检查皮带张力，皮带应紧实不松垮

## 问题类型

请先根据现象判断问题类型，再选择对应的解决措施，对症下药，**以免选错方法、浪费时间和耗材。**

  

### 1. 边角翘曲

**表现：** 模型边缘向上卷曲、脱离热床，通常发生在打印中途。喷嘴重新碰到翘起层的位置，会在模型侧面留下一条水平波纹线。

**根本原因：** 热收缩。打印件的外缘比中心冷却得快，产生的张力将边角向上拉起。常见于较大的打印件、填充密度较高时，或所用耗材属易收缩的耗材时（如 `ABS`、`ASA`、`PC`、`PA` 和 `PA-CF`）。

![abs-warping.gif](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/abs-warping.gif)

> **小贴士：** 耗材按易收缩程度从高到低排列为：`PC` → `PA-CF` → `PA` → `ABS` → `ASA` → `PETG` → `PLA`。因此，建议在进行大尺寸打印时，建议优先选择 `PLA`、`PLA-CF`、`PETG` 或 `PETG-CF`。

> ℹ️ **注意：** 有时翘曲非常轻微，难以察觉，但仍会在打印件的侧壁和顶层造成明显缺陷。因此，容易将翘曲误判为挤出或流量问题，而实际起因其实是打印件轻微抬起或翘曲。
>
> ![small_corner_warp.gif](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/small_corner_warp.gif)

  

### 2. 热床附着失败

**表现：** 整个模型在打印过程中发生位移，或完全从热床上脱落。

**根本原因：** 首层与打印表面之间的附着力不足。

**直接原因：**

- 打印板上有**脏污**（皮肤油脂是首要原因）
- 在切片软件中选择了错误的**打印板类型**（例如，切片时选择了低温增温板，实际在纹理 PEI 板上打印）
- 首层打印期间 **Z 轴偏移过高**，喷嘴离热床太远。

![model_detach.gif](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/model_detach.gif)

> **小贴士 —— 选对打印板类型很重要：** 打印使用的打印板和切片软件中选择的“打印板类型”不一致——同一种材料通常可以在不同的热床打印板使用不同的热床温度进行打印，如果选错打印板类型，则有可能因为打印的热床温度不足而导致粘接力不足。另外，纹理 PEI 板由于表面有颗粒物，所以在热床调平后，打印机会下压喷嘴 0.04mm 确保首层粘接。如果您使用PEI板打印却在切片时选择其他的“热床类型”，则会导致喷嘴高度过高，影响首层粘接。  
> ![change_build_plate_bambu_studio_zh.webp](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/change_build_plate_bambu_studio_zh.webp)

  

### 3. 模型坍塌

**表现：** 打印件上部呈现出乱作一团的"鸟巢"状，或者顶层相对于底部发生横向偏移。

**根本原因：**

- 高速运动时的振动导致喷嘴撞倒了高而细的模型
- 稀疏填充图案（如“网格”、“三角形”）可能在单层内形成小凸起，喷嘴在下一次经过时会撞到它们
- **皮带松动**导致工具头移动时松晃、定位不准

|  |  |
| --- | --- |
|  |  |
| 工具头撞到细而高的模型 | 添加支撑结构，帮助稳定模型、提高打印成功率 |

> **小贴士 —— 留意咔哒声或咯咯声：** 如果打印时听到 X 或 Y 轴发出不规则的咔哒声，说明皮带很可能松了。张力正常的皮带手感如同吉他弦 —— 紧实且略带弹性。

  

## 解决方案

### 1. 基础检查

> 这三个步骤可解决约 80 % 的翘曲和附着失败问题。在调整切片设置前，请先完成这三项检查。

**1. 清洁打印板**

- 使用温水和洗洁精清洗打印板并擦干。
- 清洁后切勿用裸手触摸打印表面。
- 教程详见 [打印板清洁指南](../../acc/pei-plate-clean-guide.md) 。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/clean-the-build-plate3.jpg)

**2. 执行自动热床调平**

执行自动热床调平校准，尤其是当打印机被移动、维护或固件更新之后。

![](https://public-cdn.bblmw.com/wiki/new/a2l/maintenance/manual-bed-tramming/bedlevelone.jpg)

**3. 检查喷嘴是否安装正确。**

卡扣必须以正确的方式扣紧，确保喷嘴不松动。

![](https://public-cdn.bblmw.com/wiki/new/x2d/first-layer-printing-optimization-guide/024.png)

**4. 进阶方法 - 调整首层**

> ℹ️ **注意：**本方法仅适用于首层质量不稳定的情况。

**请根据机型选择对应的指南进行调整：**

[P2S](../../../p2s/troubleshooting/first-layer-printing-optimization-guide.md)
[H2D](../../../h2/troubleshooting/first-layer-printing-optimization-guide.md)
[X2D](../../../x2d/troubleshooting/first-layer-printing-optimization-guide.md)
[H2S](../../../h2s/troubleshooting/first-layer-printing-optimization-guide.md)
[H2C](../../../h2c/troubleshooting/first-layer-printing-optimization-guide.md)
[A1 系列](../../../a1-mini/troubleshooting/print-issues-troubleshooting.md)

  

### 2. Bambu Studio 参数调整

### 📌 热床附着

**边角翘起 — PLA**

|  |  |
| --- | --- |
| **需更改的设置** | 热床温度 |
| **推荐参数调整** | 提高 `+ 5 到 10 °C` |
| **备注** | 纹理 PEI 板的热床温度建议设为 `55 – 65 °C`。同时添加宽度为 `8–10 mm` 的 Brim。 |

![pla_temp.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/pla_temp_zh.png)

**边角翘起 — ABS / ASA**

|  |  |
| --- | --- |
| **需更改的设置** | 热床温度 + 封闭腔体 |
| **推荐参数调整** | 提高 `+10–15 °C` |
| **备注** | 关闭所有舱门和顶盖。腔体温度应达到 `40 °C+`。 |

![abs_settings.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/abs_settings_zh.png)

**首层不粘**

|  |  |
| --- | --- |
| **需更改的设置** | 部件冷却风扇、辅助部件冷却风扇 |
| **推荐参数调整** | 前 3 层禁用 |
| **备注** | 在耗材设置 → 冷却模式中，将 **"起始层风扇层数"** 设为 `3`。 |

![disable_cooling_on_first_layer.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/disable_cooling_on_first_layer_zh.png)

**尖角翘起**

|  |  |
| --- | --- |
| **需更改的设置** | Brim / 耳状 Brim |
| **推荐调整方向** | 添加针对性的 耳状 Brim |
| **备注** | 在 Bambu Studio 中：将 **Brim 类型**设为 “绘制”，然后使用 **耳状 Brim** 工具。绘制于易翘起的边角。 |

![add_brim_ear_zh.webp](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/add_brim_ear_zh1.webp)

---

### ⚠️ 稳定性

**高而细的模型坍塌**

|  |  |
| --- | --- |
| **需更改的设置** | 打印速度 + 加速度 |
| **推荐参数调整** | 降低 `20–30 %` |
| **备注** | 建议开启或增加支撑。也可重新调整模型朝向，使其平放，或将模型切割后打印。 |

![reduce_speed_and_acc.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/reduce_speed_and_acc_zh.png)

---

### 🌡️ 翘曲

**大型平面模型翘曲**

|  |  |
| --- | --- |
| **需更改的设置** | 填充图案 + 密度 |
| **推荐参数调整** | 设置为“螺旋体”，密度 `≤25 %` |
| **备注** | “网格”和 “立方体”图案会产生内部线性张力。“螺旋体”在各方向的收缩更为均匀。 |

![reduce_infill.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/reduce_infill_zh.png)

**辅助风扇速度不当导致翘曲**

|  |  |
| --- | --- |
| **需更改的设置** | 辅助部件冷却风扇 |
| **推荐参数调整** | 降低约 `20 到 30 %` |
| **备注** | 主要适用于小物件或高悬垂区域。辅助风扇速度过高会使外壁冷却过快。 |

![reduce_aux_fan_speed.png](https://wiki.bambulab.com/knowledge-sharing/print-quality/model-warping/reduce_aux_fan_speed_zh.png)

---

### 🔧 喷嘴问题

**喷嘴撞击 / 刮擦打印件**

|  |  |
| --- | --- |
| **需更改的设置** | 填充速度 + 图案 |
| **推荐参数调整** | 降低填充速度；图案设置为“线”、“直线”、“螺旋体” 或 “同心” |
| **备注** | “网格” 和 “立方体”填充图案在单层内交叉，形成小凸起，喷嘴在下一次经过时会撞到它。 |

|  |  |
| --- | --- |
| Grid infill 网格填充，单层内有交叉 | Line filling 直线填充，单层内无交叉 |

  

### 3. 环境与耗材因素

> 这些因素常被初学者忽视，却可能让前述所有排查措施前功尽弃。

💨 **气流**

打印机附近开着的窗户、空调出风口或桌面风扇，都可能使打印件一侧冷却过快，造成受冷不均而翘曲。打印期间应避免打印机周围出现气流扰动。对于封闭式打印机，打印时请关闭前门和顶盖。

🌡 **室内环境温度**

如果室温低于 `20 °C`，即使是 PLA 和 PETG 耗材也可能发生翘曲。对于 `ABS`、`ASA`、`PA` 和 `PC` 等耗材，请使用可保持腔体温度的封闭式打印机。如果使用开放式打印机（例如 A1），可将热床温度额外提高 `+10 °C`。

💧 **受潮的耗材**

如果打印时听到噼啪或爆裂声，或看到粗糙、起泡或拉丝的表面，说明所使用的耗材已严重受潮。**请烘干耗材。**  
详细信息请参阅 [耗材烘干指南](../dry-filament.md)

> **小贴士：** 将未使用的耗材存放在密封袋或装有硅胶干燥剂的密封容器中。尼龙和 `PC` 在潮湿环境中数小时内就会受潮 —— 切勿长时间暴露空气中。

❌ **耗材选择不当**

用 `ABS`、`ASA` 或 `PC` 耗材打印的大型平面模型在没有封闭腔体的情况下易翘曲。如果没有封闭腔体，大型打印件请改用 `PLA`、`PLA-CF`、`PETG` 或 `PETG-CF`。

  

---

## 硬件建议：打印平台

### 打印板 - 使用正确类型

针对不同的耗材选择合适的打印板能带来明显差异，具体建议请参阅下方指南：

[➡ Bambu Lab 打印板介绍](../../acc/plates.md)

![engineering_plate_2.png](https://wiki.bambulab.com/filament-acc/plates/engineering_plate_2.png)

### 固体胶 - 应急附着增强剂

使用固体胶，在打印板上均匀涂覆薄薄的一层，可显著改善顽固耗材的附着力，尤其是 `ABS`、`ASA`、`PA` 和 `PC`。

- 涂抹薄而均匀的一层。厚涂会导致首层不平整。
- 用水即可轻松溶解清理胶水残留。
- 详细说明请参阅 [Bambu Lab 胶水使用指南](../../../general/how-to-use-bbl-liquid-glue.md)。

  

## 预防措施

> **请像对待精密仪器一样对待打印机。** 维护不当时，即使使用最佳切片设置，也会出现打印件翘曲和偏移。

### 定期维护

✅ 用洗洁精和清水清洗打印板；使用前完全晾干

✅ 检查挤出机齿轮周围是否有耗材残留或碎屑

✅ 检查料管是否有裂纹、发黄或堵塞

✅ 确认工具头在所有轴（X、Y、Z）上都能自由移动，无卡顿或摩擦

  

## 相关页面

- [Brim - Bambu Studio](../../../software/bambu-studio/auto-brim.md)
- [耳状 Brim - Bambu Studio](../../../software/bambu-studio/brim-ears.md)
- [纹理 PEI 板清洁指南](../../acc/pei-plate-clean-guide.md)
- [如何使用 Bambu Lab 胶水](../../../general/how-to-use-bbl-liquid-glue.md)

  

## 结束语

> 我们希望本指南能为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[支持工单](https://bambulab.com/en/my/support/tickets/create)，并附上您近期的打印机日志以及其他图片或详细信息。我们的技术团队将审核您的请求并提供详细的协助。  
> 您也可以访问 [Bambu AI](https://support.bambulab.com/en?from=6&lang=en-us)，它可以即时回答常见问题并为您提供操作指导。
