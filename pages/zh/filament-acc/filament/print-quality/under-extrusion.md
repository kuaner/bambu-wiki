---
path: zh/filament-acc/filament/print-quality/under-extrusion
title: "模型缺料"
description: ""
tags: ["打印质量", "模型缺料"]
created: 2023-12-10T05:51:53.569Z
updated: 2026-03-16T06:48:51.955Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/under-extrusion
---

## 模型缺料

缺料通常是由于挤出不足导致的，现象有整体缺料和局部缺料两种。

**模型表面整体缺料，通常线间会很稀疏，表现如下：**

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E9%A1%B6%E9%9D%A2%E7%BC%BA%E6%96%99.png)

**模型局部缺料表现如下：**

|  |  |
| --- | --- |
|  |  |

**常见的原因和改善方法如下：**

**1. 挤出阻力过大。**

- 料盘转动受阻或料线缠结——排除故障后再重新打印。
- 料管进入异物、局部弯折或磨损——清除异物，修复或更换料管。
- 挤出机齿轮卡住或损——清洁或更换齿轮。
- 喷嘴内部通道阻塞，出料困难（长时间打印或打过含有纤维的料后易发生）——疏通喷嘴或更换新喷嘴（与前述相同）。

**2. 挤出量偏小。**

- 耗材的熔融、挤出速度跟不上打印速度——适当提高喷嘴温度或降低打印速度。如果要开启“狂暴模式”（更高速打印），最好适当提高喷嘴温度（提高10 ℃ 左右）来提高耗材的熔融速度。如果要使用第三方的耗材（可能不支持高速打印），请选择打印速度相对较低的 Generic 参数来切片、打印。
- 喷嘴内部通道阻塞，出料困难——疏通喷嘴或更换新喷嘴（与前述相同）。
- 如果模型的整个表面都明显缺料了，也有可能是流量比例不足导致的，可以在切片软件里适当提高一点流量比例。如果您使用的是Bambu官方耗材，建议使用默认的流量比例，不要随意修改它。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%B5%81%E9%87%8F%E6%AF%94%E4%BE%8B.jpeg)

**3. 压力提前值设置错误。**

当模型都是在转角处缺料（如下图），那么很有可能压力提前值设置错误了，需要重新进行流量标定（校准）。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%8E%8B%E5%8A%9B%E6%8F%90%E5%89%8D%E5%80%BC%E5%A4%AA%E5%A4%A7%E4%BA%86(pla0.1).png)

流量标定的作用是，确保工具头在加速和减速运动的时候，挤出机挤出的料能够保持均匀，避免在加速或减速的节点多料或者少料。如果压力提前值错误，则有可能导致打印头变速的瞬间挤出太多或者太少。P1P和X1系列打印机的流量标定方法如下图所示：

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/p1p%E6%B5%81%E9%87%8F%E6%A0%87%E5%AE%9A.png)

**X1 动态流量标定**

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/x1%E8%87%AA%E5%8A%A8%E6%B5%81%E9%87%8F%E6%A0%A1%E5%87%86.png)

动态流量校准的本质，就是测试在工具头加速——减速运动过程中，找到一个合适的挤出补偿值来保证挤出线条均匀。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%B5%81%E9%87%8F%E6%A0%87%E5%AE%9A%E7%BA%BF.png)
