---
path: zh/h2/h2d-filament-printing-guide
title: "H2D 耗材打印建议"
description: ""
tags: []
created: 2025-03-25T14:10:54.162Z
updated: 2025-04-12T06:39:16.639Z
source: https://wiki.bambulab.com/zh/h2/h2d-filament-printing-guide
---

# 左右热端的耗材限制

## **PPS/PPA-CF需使用左热端打印**：

由于 PPS/PPA-CF 材料较脆，若使用右热端打印，回中时料管的弯曲可能导致耗材断裂。如下图所示，当工具头在热床偏后方位置回中时，工具头会撞击右侧限位，此时料管的弯曲程度较大，尤其是右热端的料管弯曲更为明显，更容易导致材料在料管中断裂。因此，建议此类材料使用左热端打印。

![](https://wiki.bambulab.com/h2/manual/filament-printing-guide/large-stress.png)

## **TPU 需使用右热端打印：**

目前，由于多种因素的综合影响，使用左热端挤出 TPU 时存在较高的堵料风险。因此，现阶段推荐仅使用右热端打印 TPU。

更多关于H2D TPU的打印建议，请参考此页面：[H2D 的 TPU 85A 和 90A 打印指南](h2d-tpu-printing-guide.md)

# H2D 3D打印材料混打指南

更多关于H2D 材料混打指南，请查阅此指南：[H2D 材料混打指南](../filament-acc/filament/h2d-filament-config-limit.md)
