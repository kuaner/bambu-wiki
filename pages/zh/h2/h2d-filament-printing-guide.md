---
path: zh/h2/h2d-filament-printing-guide
title: "H2D 耗材打印建议"
description: ""
tags: []
created: 2025-03-25T14:10:54.162Z
updated: 2026-11-27T03:59:02.534Z
source: https://wiki.bambulab.com/zh/h2/h2d-filament-printing-guide
---

## 左右热端的耗材限制

### **PPS/PPA-CF需使用左热端打印**：

由于 PPS/PPA-CF 材料较脆，若使用右热端打印，回中时料管的弯曲可能导致耗材断裂。如下图所示，当工具头在热床偏后方位置回中时，工具头会撞击右侧限位，此时料管的弯曲程度较大，尤其是右热端的料管弯曲更为明显，更容易导致材料在料管中断裂。因此，建议此类材料使用左热端打印。

![](https://wiki.bambulab.com/h2/manual/filament-printing-guide/large-stress.png)

### **TPU：**

**左热端：** 目前不支持打印 TPU 85A，存在较高的堵头风险。可支持打印 TPU 95A HF/90A。

更多关于H2D TPU的打印建议，请参考此页面：[H2D 的 TPU 85A 和 90A 打印指南](h2d-tpu-printing-guide.md)

## H2D 3D打印材料混打指南

更多关于H2D 材料混打指南，请查阅此指南：[H2D 材料混打指南](../filament-acc/filament/h2d-filament-config-limit.md)
