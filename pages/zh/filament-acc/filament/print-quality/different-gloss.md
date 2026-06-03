---
path: zh/filament-acc/filament/print-quality/different-gloss
title: "模型不同区域的光泽差异大"
description: ""
tags: ["打印质量", "光泽差异", "光泽"]
created: 2023-12-10T05:57:53.523Z
updated: 2024-10-12T09:44:40.410Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/different-gloss
---

# 模型不同区域的光泽差异大

**直接原因：打印温度相同时，打印速度越低则表面越亮滑；打印速度相同时，打印温度越高则表面越亮滑。本质是材料熔融程度不同，流平性不同，造成打印件的表面粗糙度有差异，且这种现象在打印在反光性好的材料时更明显。**

**1. 模型的不同区域的打印速度有明显的差异（如存在悬垂降速区域）。**

- 建议将外墙速度（大模型）或整体速度（小模型）适当降低，或取消悬垂降速，确保外墙的打印速度相近或相同。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%88%87%E7%89%87%E8%BD%AF%E4%BB%B6%E5%B0%8F%E8%88%B9%E5%8F%98%E9%80%9F%E5%A4%A7.png)

**内置小船速度预览**

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%B0%8F%E8%88%B9%E8%A1%A8%E9%9D%A2%E5%85%89%E6%B3%BD%E5%BA%A6%E4%B8%8D%E5%90%8C.jpg)

**不同速度导致表面光泽度不同**

可以重新切片模型并降低外墙速度，使各个区域的外墙速度尽可能一致。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E9%87%8D%E6%96%B0%E5%88%87%E7%89%87%E5%B0%8F%E8%88%B9.png)

**2. 用低层高（如 0.08 mm 层高）打印模型时，如果打印速度较高，也可能导致模型表面出现呈鱼鳞样的光泽差异区。**

- 换用较大的打印层高，例如从 0.08 mm、0.12 mm 换为 0.16 mm、0.20 mm。
- 适当降低打印速度、提高打印温度。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/0.08%E5%B1%82%E9%AB%98%E4%B8%8D%E5%90%8C%E5%A4%96%E5%A2%99%E9%80%9F%E5%BA%A6%E5%AF%B9%E6%AF%94.png)

**左：外墙速度 200 mm/s；右：外墙速度 50 mm/s**
