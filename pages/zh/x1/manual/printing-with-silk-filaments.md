---
path: zh/x1/manual/printing-with-silk-filaments
title: "PLA Silk/ Silk+ 丝绸耗材打印指南"
description: "本指南介绍了如何通过设置切片参数让拓竹丝绸 PLA（Silk / Silk+）耗材打印的模型丝绸光泽最大化。"
tags: []
created: 2022-07-29T07:24:29.221Z
updated: 2026-08-13T07:33:16.794Z
source: https://wiki.bambulab.com/zh/x1/manual/printing-with-silk-filaments
---

拓竹丝绸 PLA 耗材，通过在普通 PLA 基础上添加珠光剂，使表面呈现丝绸般的特殊光泽，视觉效果亮丽醒目，适合打印需要呈现丝绸质感或金属光泽的装饰件、摆件。

使模型的丝绸光泽最大化，最重要的是正确设置切片参数。影响模型丝绸光泽的核心因素可概括为三点：

1. **外墙速度**：速度越低，材料流平时间越充足，光泽通常越强；速度过高会增加表面微观凹凸，加剧光线散射，使光泽变弱。
2. **喷嘴温度**：温度适当偏高，有助于材料充分熔融、流动更连贯。
3. **速度一致性**：外墙局部忽快忽慢，会导致同一模型不同区域亮暗不一。

![silk-print-examples.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/silk-print-examples.png)

本指南将介绍如何打印 PLA Silk / Silk+ 耗材，使模型的丝绸质感最大化。

## 打印前的准备

打印前，请参考本章节的步骤烘干耗材并选择合适的配件。

### 烘干耗材

PLA Silk / Silk+ 耗材若未做特殊防护而长期暴露于空气中，较易吸湿受潮。若使用受潮的耗材打印，模型易出现拉丝，或光泽度不均等表面质量问题。

因此，**打印前请烘干耗材**。使用完毕后，将耗材储存在湿度 **< 20% RH** 的密封环境并放置有效的干燥剂。

具体烘干方法请参考：**[耗材烘干指南](../../filament-acc/filament/dry-filament.md)。**

烘干参数如下表：

| 烘干方法 | 烘干温度&时间 |
| --- | --- |
| **鼓风型烤箱** | 55 °C，8 小时 |
| **打印机热床** | 65–75 °C，12 小时 |
| **AMS 2 Pro / AMS HT** | 耗材插入状态： 45℃，12 小时； 耗材非插入状态： 55℃，8 小时 |

### 硬件适配

- **喷嘴**：适配于`0.2mm` 和 `0.4 mm` 喷嘴，不推荐使用 `0.6mm`，`0.8mm` 喷嘴打印。
- **打印板**：**不推荐**使用增稳低温打印板（英文：Cool Plate SuperTack）。
- **AMS 系列**：全兼容。
- **打印机**：**双色丝绸 PLA** 耗材采用特殊的成型工艺，耗材截面为椭圆形，但其在打印的过程中仍有小概率发生耗材旋转，可能产生不均匀的颜色过渡。由于结构的特殊性，**A 系列打印机**的旋转风险较大，不推荐用户在 A 系列打印机上使用。

## Bambu Studio 参数设置

参考本章节的步骤，正确设置切片参数，增强模型的丝绸光泽度。

### 1. 调整模型摆放方向

**说明**：对于曲面作为展示面的模型，若平放打印，层纹会更明显，从而导致光泽度低。因此，建议将模型关键的展示面垂直于打印板打印。

**具体步骤**：在 Bambu Studio 中选中模型 →「**选择底面**」，让主要展示面竖立起来打印。

![select-bottom-face.webp](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/select-bottom-face.webp)

### 2. 降低并统一外墙速度

**具体步骤**：进入「**工艺 → 速度**」，将「**外墙速度**」设在`40–60 mm/s` 范围内，优先试 `50 mm/s`。

![set-outer-wall-speed.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/set-outer-wall-speed.png)

切片后，切换到「**速度预览**」，检查外墙是否出现大段忽快忽慢。

![slice-speed-preview.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/slice-speed-preview.png)

### 3. 开启「不减慢外墙速度」

**作用**：启用此设置后，外墙打印速度不会因为满足最小层时间而被降低，以保证外墙质量，避免光泽度因速度变化而出现差异或不同速度导致的外墙细微缺陷。

**具体步骤**：

1. 开启「**开发者模式**」；

点此查看如何启用开发者模式

**步骤 1** - 点击顶部导航栏中的**菜单**，选择**偏好设置**，或使用快捷键 `Ctrl+P`。

![s1.jpg](https://wiki.bambulab.com/software/bambu-studio/dev-mode/s1.jpg)

**步骤 2** - 在偏好设置中，下拉找到**开发者模式**，勾选该功能。

![s2.jpg](https://wiki.bambulab.com/software/bambu-studio/dev-mode/s2.jpg)

✅ 若需关闭该模式，也可执行同样的操作步骤。

2. 在「**耗材丝设置 → 冷却模式**」中，勾选「**不减慢外墙速度**」，冷却减速逻辑设置为「**表面一致性**」。

![dont-slow-down-outer-wall.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/dont-slow-down-outer-wall.png)

### 4. 降低层高

**作用：** 对于有曲面或坡度的模型，更小的层高通常能让曲面的光影更润、更连续。层高过大会使表面不光滑，“阶梯感”比较明显，易显得光泽暗淡。

**具体步骤**：在「**工艺 → 质量 → 层高**」设置中，推荐修改参数为 **`0.16 mm`**。

![set-layer-height.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/set-layer-height.png)

### 5. 选择顶面填充图案

**作用：** 使用合适的顶面填充图案能够优化顶壳观感，提升光泽度与均匀性。

**说明**：由于模型顶面结构各异，效果以实际切片为准。

**具体步骤**：点击「**工艺 → 强度 → 顶面图案**」，选择「**阿基米德螺旋**」/ 「**同心**」。

![set-top-surface-pattern.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/set-top-surface-pattern.png)

### 6. 适度提高喷嘴温度

**说明**：丝绸 PLA 通常需要较高的温度来增加**层间粘接力**，这个温度通常在约 210℃至约 240℃之间。

**具体步骤**：进入「**耗材丝设置 → 耗材丝 → 打印温度**」，推荐设置「**喷嘴**」首层与其它层为 235℃。

![set-nozzle-temperature.png](https://wiki.bambulab.com/x1/manual/printing-with-silk-filaments/set-nozzle-temperature.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
