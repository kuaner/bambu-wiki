---
path: zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-x-series
title: "X1 系列的 TPU 打印准备工作"
description: "使用 X1 系列机器打印 TPU 的指南"
tags: []
created: 2025-03-07T02:38:47.962Z
updated: 2026-08-06T03:57:32.392Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-x-series
---

## 前言

TPU 85A 和 TPU 90A 是热塑性聚氨酯（ TPU ）耗材中的两种不同硬度等级的产品。

- 硬度：TPU 的硬度通常以邵氏硬度 A（Shore A）来表示。85A 和 90A 分别表示这两种耗材的硬度等级，其中 90A 比 85A 更硬。
- 弹性与柔韧性：能够在较大的范围内拉伸和弯曲而不破裂，恢复性强。这种特性使得 TPU 85A 和 TPU 90A 在需要弹性和柔韧性的应用中表现出色。
- 耐磨性：TPU 耗材具有良好的耐磨性，能够在长时间的使用过程中保持稳定的性能。

在应用方面，TPU 85A 和 TPU 90A 可以用于制造鞋底、运动器材部件等需要弹性和耐磨性能的产品，也可以用于制造手机保护壳、智能手表表带等电子产品配件。总的来说，这二者是两种性能优异、应用广泛的热塑性聚氨酯耗材。不同硬度等级使得它们能够满足不同应用场景的需求。关于 TPU 耗材的详细介绍，请跳转至《[TPU 介绍](../../knowledge-sharing/tpu-printing-guide.md)》。

> 📌 **耗材使用注意事项**：
>
> 1. 请在**阴凉、避光、干燥**环境中存放耗材，避免阳光直射或高温环境。
> 2. 请将耗材及折断的碎屑放在**婴幼儿及宠物无法触及的地方**，避免吞咽和窒息的风险。
> 3. TPU 属于**吸水性较强**的材料，未使用完的耗材应立即放入含有有效干燥剂的**密封容器**内，并且在打印前按照指南中推荐的温度和时间进行**充分烘干**。
> 4. 建议在**通风良好**的区域使用打印机，或安装有效的空气过滤、外排风系统。
> 5. 本耗材**不属于**食品接触级耗材，请避免将打印成品用于存放或接触食品。

> X2D 打印机请参考：[X2D TPU 打印指南](../../x2d/manual/tpu-printing-guide.md)。

## 准备工作

### 耗材烘干

TPU 具有较强的吸湿性，在自然环境中容易吸收水分。含有水分的 TPU 会严重影响打印质量，因此我们推荐您使用前烘干 TPU 耗材。详情请参考此 wiki：[耗材准备——干燥](dry-filament.md)

在烘干过程中，TPU 受热膨胀会导致料盘变形，**可能从 65.4 mm 增大到约 69.4 mm**，这是正常现象。可使用耐高温重物压在 TPU 料盘上抑制变形。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/20250211-112835.jpg)

### TPU 系列硬件兼容表

| 项目 | TPU 85A | TPU 90A | TPU 95A HF | TPU for AMS |
| --- | --- | --- | --- | --- |
| **喷嘴兼容性** | **推荐：** 0.6 mm / 0.8 mm  **不推荐：** 高流量喷嘴  **不支持：** 0.2 mm / 0.4 mm | **推荐：** 0.4 mm / 0.6 mm / 0.8 mm  **不推荐：** 高流量喷嘴  **不支持：** 0.2 mm | **推荐：** 0.4 mm / 0.6 mm / 0.8 mm  **不支持：** 0.2 mm / 高流量喷嘴 | **推荐：** 0.4 mm / 0.6 mm / 0.8 mm  **不支持：** 0.2 mm / 高流量喷嘴 |
| **配件兼容性（打印板 / 胶水 / AMS 等）** | - 打印板：光面 PEI、纹理 PEI  - 胶水：无需涂胶  - AMS / AMS 2 Pro：**不兼容**  - AMS HT：兼容 | - 打印板：光面 PEI 板、纹理 PEI 板  - 胶水：无需涂胶  - AMS / AMS 2 Pro：**不兼容**  - AMS HT：兼容 | - 打印板：光面 PEI 板、纹理 PEI 板  - 胶水：Bambu 液体胶 / 固体胶棒  - AMS / AMS 2 Pro：**不兼容**  - AMS HT：兼容 | - 打印板：光面 PEI、纹理 PEI  - 胶水：Bambu 液体胶 / 固体胶棒  - AMS / AMS 2 Pro / AMS HT：**兼容** |

> 📌 **重要提醒：**  
> **使用 TPU 耗材时需特别注意喷嘴适配，请勿使用 0.2mm 喷嘴与普通高流量喷嘴，其中 85A TPU 不兼容普通 0.4mm 喷嘴。**  
> 建议不要使用曾打印过碳纤增强、玻纤增强等纤维类耗材的热端，这类耗材残留的纤维会大幅增加挤出阻力，极易引发堵塞问题，若需打印 TPU，建议先冷拔 3-5 次而后发起打印，请参考 [X1/P1 喷嘴/热端堵塞](../../x1/troubleshooting/nozzle-clog.md)。

## 进料工作

所有 TPU 耗材使用时均需要垫高料桶（料桶出料口高于工具头进料口）以确保进料顺畅。

**料桶架链接如下：**[TPU耗材卷轴架](https://makerworld.com.cn/zh/models/983129-tpuxian-cai-juan-zhou-jia?from=search#profileId-1004263)。

![耗材架.jpg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/%E8%80%97%E6%9D%90%E6%9E%B6.jpg)

### AMS HT

- 裁剪 5cm 长的 PTFE 管，并将 PTFE 管微微弯折。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/img_v3_02ko_bb2cc848-debd-4a87-b9b0-880dbaf36cfg.png)

- 打开 AMS HT 尾部的硅胶塞，将 PTFE 管凸起一侧朝上，将 PTFE 管插入硅胶塞的小孔，**确保插入 AMS HT 的长度为 5mm**。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/dsc00667.jpg)

- 将耗材放入 AMS HT 中，并将耗材穿过 PTFE 管，再扣紧 AMS HT 上盖。

![](https://wiki.bambulab.com/filament-acc/tpu/image10.png)

- 确认耗材的转动方向如下图所示。

![](https://wiki.bambulab.com/filament-acc/tpu/image11.png)

### 5.8L 米桶

若使用米桶进料，请务必打印米桶支架（模型链接如下），确保料线旋转顺畅。  
[5.8L 米桶干燥箱支架](https://makerworld.com.cn/zh/models/437644?from=search#profileId-353897)

为了减小进料阻力，请从料桶的侧边开口。

|  |  |
| --- | --- |
|  |  |

#### 使用 AMS HT / 米桶进料

> 进料前提示：
>
> 1. 进料前请确保耗材充分干燥。
> 2. TPU 都需要手动进料，仅 TPU For AMS 可使用 AMS 进行自动进料。

1. 提前摘除玻璃上盖，拆除在工具头端的铁氟龙管。

![移除上盖和ptfe管.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/%E7%A7%BB%E9%99%A4%E4%B8%8A%E7%9B%96%E5%92%8Cptfe%E7%AE%A1.gif)

2. 将料桶架摆放在合适的位置，确保出料口高于机身。

![料架放置.jpg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/%E6%96%99%E6%9E%B6%E6%94%BE%E7%BD%AE.jpg)

3. 进料时推荐将热端升温到 250 ℃，85A 耗材需从机器上方走线直接插入到挤出机中（不支持从铁氟龙管进料），而后缓慢点击进料按钮，确保耗材均匀挤出。

![进料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/%E8%BF%9B%E6%96%99.gif)

4. 90A/95A 耗材可从机器背后的气管接头处进料，轻推耗材通过料管，待耗材最前端从铁氟龙管口处通过后，捏住耗材前端扯出一定长度。  
   ![90a料架放置.jpg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/90a%E6%96%99%E6%9E%B6%E6%94%BE%E7%BD%AE.jpg)
5. 热端升温后（推荐 250 ℃），捏住耗材前端插入工具头，缓慢点击进料按钮直到耗材均匀流畅挤出，最后将铁氟龙管插回。

![90a进料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/90a%E8%BF%9B%E6%96%99.gif)

> **注意事项**
>
> - 在屏幕上点击挤出按钮的时候，请不要一直连续点击，否则将导致 TPU 卷进挤出机齿轮造成堵塞。
> - 当挤出机齿轮已经咬合住 TPU 耗材后，慢慢点击挤出按钮，确保耗材从热端中连续均匀挤出再发起打印。
> - 打印 TPU 时关闭动态流量校准。

|  |  |  |
| --- | --- | --- |
| 流量校准屏幕.jpg | 动态流量校准-handy.jpg | 动态流量校准-studio.png |

### 退料 （TPU 85A & TPU 90A 相同）

不支持自动退料程序。

**TPU 85A**

1. 推荐将热端升温至 250 ℃。
2. 缓慢点击挤出机退料按键，跟随齿轮回转将耗材轻轻拉出工具头。

![退料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/%E9%80%80%E6%96%99.gif)

**TPU 90A**

1. 推荐将热端升温至 250 ℃
2. 将铁氟龙进料管从工具头处拆卸下来，而后捏住耗材。
3. 缓慢点击挤出机退料按键，跟随齿轮回转将耗材轻轻拉出工具头。
4. 退料完成后将铁氟龙管插回工具头

![90a退料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/x-series/90a%E9%80%80%E6%96%99.gif)

### 耗材存储

建议将耗材放置在环境湿度低于 20% RH 的环境中，推荐使用收纳盒存放耗材，还需在其中放置干燥剂（推荐使用硅胶干燥剂）。

![收纳箱.jpeg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/%E6%94%B6%E7%BA%B3%E7%AE%B1.jpeg)  
请在收纳箱中放置硅胶干燥剂后存放耗材。

## 常见打印问题

TPU 耗材容易出现下列问题：

1. 缺料（堵头、进料阻力、耗材打滑）
2. 卡挤出（耗材弯曲卡柱挤出齿轮，需拆开挤出机后扯出卡住耗材）
3. 拉丝漏料（使用大口径热端，微调回抽，进一步烘干耗材，模型后处理）

详细问题解决方法，请参考：[常见打印质量问题和解决办法](print-quality.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
