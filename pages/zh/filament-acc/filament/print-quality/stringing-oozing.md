---
path: zh/filament-acc/filament/print-quality/stringing-oozing
title: "局部拉丝或漏料"
description: ""
tags: ["打印质量", "拉丝", "漏料"]
created: 2023-12-10T05:55:46.220Z
updated: 2026-02-09T09:06:30.815Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/stringing-oozing
---

## 局部拉丝或漏料

**直接原因：喷嘴出料过量或熔体异常膨胀、流动。**

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%A8%A1%E5%9E%8B%E6%8B%89%E4%B8%9D.png)

**拉丝模型和正常模型对比**

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%9D%90%E6%96%99%E5%8F%97%E6%BD%AE%E6%89%93%E5%8D%B0%E5%B0%8F%E8%88%B9.png)

**受潮材料打印模型**

1. 耗材受潮，打印过程中水分受热汽化而导致耗材熔体破裂、异常流动——建议先将耗材烘干，然后将其放在带有未失效的干燥剂的密封容器中使用。烘干耗材可以参考：[耗材烘干操作指南](../dry-filament.md)

2. 模型存在较长空驶距离且回抽长度偏小，导致空驶过程中耗材熔体流出喷嘴——打多个模型时，减小模型间距，及适当增加回抽长度或回抽速度。

> **注意：回抽长度设置得过大时容易引起堵头，一般建议不要超过 2 mm。**

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%9B%9E%E6%8A%BD%E8%AE%BE%E7%BD%AE.png)

3. 模型本身结构特殊或摆盘方式不当。当单个模型存在较多的不连续结构，或是单盘打印多个模型且摆放间距较大时，会使打印过程存在较多、较长距离的空驶，使得熔体在喷嘴空驶的过程中往下滴落，从而造成漏料、粘嘴等缺陷。这种情况下，可以减小模型间的摆放距离。同时可以开启“**避免跨越外墙**”来降低拉丝的概率。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%BC%80%E5%90%AF%E9%81%BF%E5%85%8D%E8%B7%A8%E8%B6%8A%E5%A4%96%E5%A2%99.png)

4. 喷嘴温度过高，导致耗材熔体的粘度过小——适当调低喷嘴温度。

5. 使用低密度的耗材（例如发泡 PLA）时，未适当调低打印温度或流量比例——建议适当调低打印温度和把流量比例调到 0.5 ~ 0.7 之间。低密度耗材，如发泡 PLA，内部存在较多孔洞、气体（含水），且打印过程还会产生气体，这会使耗材熔体产生较大膨胀、异常流动，所以，在打印前建议先烘干耗材，切片时选择较低的流量比例。

6. 喷嘴口径过大，造成流出喷嘴的耗材熔体偏多。

- 切片时选错了喷嘴配置，或者打印的时候误用了较大口径的喷嘴——在打印前要确保选用的配置和实际使用的喷嘴规格是一致的。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%89%93%E5%8D%B0%E6%9C%BA%E9%85%8D%E7%BD%AE%E9%80%89%E6%8B%A9.png)

- 喷嘴已长期使用，磨损明显——更换新喷嘴。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%96%B0%E6%97%A7%E5%96%B7%E5%98%B4%E5%AF%B9%E6%AF%94.png)

**左：磨损喷嘴；右：新喷嘴**
