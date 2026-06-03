---
path: zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-p-series
title: "P 系列机器打印 TPU 90A & 85A 的打印指南"
description: "使用 P 系列机器打印TPU 90A & 85A 的打印指南"
tags: []
created: 2025-03-07T02:37:44.822Z
updated: 2026-04-10T06:27:47.783Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/tpu-85a-90a-printing-guide-for-p-series
---

## 前言

TPU 85A 和 TPU 90A 是热塑性聚氨酯（ TPU ）材料中的两种不同硬度等级的产品。

- 硬度：TPU 的硬度通常以邵氏硬度 A（Shore A）来表示。85A 和 90A 分别表示这两种材料的硬度等级，其中 90A 比 85A 更硬。
- 弹性与柔韧性：能够在较大的范围内拉伸和弯曲而不破裂，恢复性强。这种特性使得 TPU 85A 和 TPU 90A 在需要弹性和柔韧性的应用中表现出色。
- 耐磨性：TPU 材料具有良好的耐磨性，能够在长时间的使用过程中保持稳定的性能。

在应用方面，TPU 85A 和 TPU 90A 可以用于制造鞋底、运动器材部件等需要弹性和耐磨性能的产品，也可以用于制造手机保护壳、智能手表表带等电子产品配件。总的来说，这二者是两种性能优异、应用广泛的热塑性聚氨酯材料。不同硬度等级使得它们能够满足不同应用场景的需求。

## 准备工作

### 耗材烘干

TPU 耗材具有较强的吸湿性，在自然环境中容易吸收水分。若直接打印含有水分的 TPU，会导致严重的打印质量问题。

因此，打印前需要对 TPU 耗材进行烘干。详细的烘干教程请参考此 wiki：[耗材准备——干燥](dry-filament.md)

在烘干过程中，TPU 受热膨胀会导致料盘变形，**可能从 65.4 mm 增大到约 69.4 mm**，这是正常现象。可使用耐高温重物压在 TPU 料盘上抑制变形。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/20250211-112835.jpg)

### 硬件选择

#### 热端

- **使用 TPU 耗材时需特别注意喷嘴适配，请勿使用 0.2mm 喷嘴与普通高流量喷嘴，其中 85A TPU 不兼容普通 0.4mm 喷嘴。**
- 强烈推荐选用全新热端，或是使用只打印过 TPU 的热端。
- **切勿使用曾打印过纤维增强耗材（如碳纤增强、玻纤增强耗材）的热端来打印 TPU。** 这类耗材残留的纤维会大幅增加挤出阻力，极易引发堵塞问题，若需打印 TPU，建议先冷拔 3-5 次而后发起打印，请参考 [X1/P1 喷嘴/热端堵塞](../../x1/troubleshooting/nozzle-clog.md)。

|  |  |
| --- | --- |
| **TPU 85A** | **支持：** 0.6 mm / 0.8 mm / TPU 高流量喷嘴    **不推荐：** 0.6 mm 高流量喷嘴 / 0.8 mm 高流量喷嘴    **不支持：** 0.2 mm / 0.4 mm / 高流量 0.4 mm |
| **TPU 90A** | **支持：** 0.4 mm / 0.6 mm / 0.8 mm / TPU 高流量喷嘴    **不推荐：** 0.4 mm 高流量喷嘴 / 0.6 mm 高流量喷嘴 / 0.8 mm 高流量喷嘴    **不支持：** 0.2 mm |

- 若不是全新热端，请检查热端状态（是否有残料，若有请升温后用 PLA / PETG 耗材冲刷 2 - 3 次，不可使用纤维增强耗材进行冲刷）。

**冲刷操作步骤（以 PLA Matte 为例）：**

1. 为操作方便，首先将工具头上的 PTFE 管与工具头断连；
2. 推荐将热端温度升至 250 ℃，取一截 PLA Matte 耗材插入工具头；
3. 点击操作界面 “向下挤出” 按键，观察耗材是否连续均匀挤出。（此步骤需重复 3 - 5 次）

![冲刷.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/%E5%86%B2%E5%88%B7.gif)

#### 打印板

**除了增稳低温打印板以外，** 其他类型打印板均适配 TPU 耗材的打印。

### 容器准备

建议使用 AMS HT 或 米桶来配合 TPU 耗材的打印。

两种容器的介绍与耗材装载方法如下：

#### 使用 AMS HT

使用 AMS HT 作为容器装载耗材的步骤如下：

- **步骤 1**：

先裁剪 50mm 长的 PTFE 管，并将 PTFE 管微微弯折，使其保持弯曲，便于后续进料。然后打开 AMS HT 尾部的硅胶塞，将 PTFE 管凸起一侧朝上，将 PTFE 管插入硅胶塞的小孔，确保插入 AMS HT 的长度为 5mm。

|  |  |
| --- | --- |
| 50mm 长的 PTFE 管 | 插入 AMS HT |

- **步骤 2**：

确认耗材的方向，将耗材放入 AMS HT 中，从下至上穿过铁氟龙管。

|  |  |
| --- | --- |
| 确认耗材的方向 | 将耗材从下至上穿过铁氟龙管 |

- **步骤 3**：

扣紧 AMS HT 上盖，即安装完成。

|  |  |
| --- | --- |
| TPU 出料口 | 耗材进料方向 |

#### 使用 5.8L 米桶

若使用米桶进料，请务必打印米桶支架（模型链接如下），确保料线旋转顺畅。

[5.8L 米桶干燥箱支架](https://makerworld.com.cn/zh/models/437644?from=search#profileId-353897)

为了减小进料阻力，请从料桶的侧边开口。

|  |  |
| --- | --- |
|  |  |

## 进料工作

所有 TPU 耗材使用时均需要垫高耗材容器（容器出料口高于工具头进料口）以确保进料顺畅。

您可以使用小凳子或小箱子等物品来垫高；若时间充裕，也可以选择打印 MakerWorld 上的 [TPU 耗材卷轴架](https://makerworld.com.cn/zh/models/983129-tpuxian-cai-juan-zhou-jia?from=search#profileId-1004263) 模型来垫高。

![耗材架.jpg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/%E8%80%97%E6%9D%90%E6%9E%B6.jpg)

### TPU 85A 进料

1. 提前摘除玻璃上盖，拆除在工具头端的铁氟龙管，并将铁氟龙管固定；  
   ![取下上盖玻璃.jpg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/%E5%8F%96%E4%B8%8B%E4%B8%8A%E7%9B%96%E7%8E%BB%E7%92%83.jpg)
2. 将料桶架摆放在合适的位置，确保出料口高于机身；  
   ![料架放置示意.jpg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/%E6%96%99%E6%9E%B6%E6%94%BE%E7%BD%AE%E7%A4%BA%E6%84%8F.jpg)
3. 进料时推荐将热端升温到 250 ℃，耗材从机器上方走线直接插入到挤出机中（不支持从铁氟龙管进料），而后缓慢点击进料按钮，确保耗材均匀挤出。  
   ![升温进料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/%E5%8D%87%E6%B8%A9%E8%BF%9B%E6%96%99.gif)

**注意事项：**

- 点击挤出按键的时候，请不要一直连续点击，否则将导致 TPU 卷进挤出机齿轮造成堵塞。
- 当挤出机齿轮已经咬合住 TPU 耗材后，慢慢点击挤出按钮，确保耗材从热端中连续均匀挤出再发起打印。

### TPU 90A 进料

1. 将耗材以及耗材架放置在打印机侧边，确保料桶出料口高于机身；
2. 将料桶开口处接上铁氟龙管，耗材可以通过铁氟龙管进入工具头；

![90a料架放置示意.jpeg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/90a%E6%96%99%E6%9E%B6%E6%94%BE%E7%BD%AE%E7%A4%BA%E6%84%8F.jpeg)

3. 进料：先将工具头处的铁氟龙管与工具头断开，轻推 90A 耗材通过料管，待耗材最前端从铁氟龙管口处通过后，捏住耗材前端扯出一定长度；
4. 热端升温后（推荐 250 ℃），捏住耗材前端插入工具头，缓慢点击进料按钮直到耗材均匀流畅挤出，最后将铁氟龙管插回。

![90a进料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/90a%E8%BF%9B%E6%96%99.gif)

**注意事项：**

- 从铁氟龙管进料时，若发现进料阻力过大，请检查料桶内耗材转动是否流畅，以及铁氟龙管是否出现弯曲角度过大的情况。
- 当挤出机齿轮已经咬合住 TPU 耗材之后，慢慢点击挤出按钮，确保耗材已经从热端挤出，避免料线卷入进料齿轮造成堵塞。

### 退料

**使用 P 系列机型打印 TPU 85A & TPU 90A 后都需要升温后进行手动退料，不支持用切刀自动退料。**

**TPU 85A**

1. 推荐将热端升温至 250 ℃；
2. 缓慢点击挤出机退料按键，跟随齿轮回转将耗材轻轻拉出工具头。

![退料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/%E9%80%80%E6%96%99.gif)

**TPU 90A**

1. 推荐将热端升温至 250 ℃；
2. 将铁氟龙进料管从工具头处拆卸下来，而后捏住耗材；
3. 缓慢点击挤出机退料按键，跟随齿轮回转将耗材轻轻拉出工具头；
4. 退料完成后将铁氟龙管插回工具头。

![90a退料.gif](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/p-series/90a%E9%80%80%E6%96%99.gif)

### 参数设定

除了预设参数外，具体参数设定应当随模型的特点进行调整。

1. TPU 85A & 90A 推荐打印温度为 225 ℃，热床温度为 30 - 35 ℃；
2. 打印时请保留默认的体积速度上限，不建议加快打印速度；
3. 用 TPU 90A耗材进行打印时，建议将模型放置在打印板中间靠前的位置以减小耗材与铁氟龙管之间的摩擦力。

![90a摆放.png](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/90a%E6%91%86%E6%94%BE.png)

## 耗材存储

建议将耗材放置在环境湿度低于 20% RH 的环境中。推荐使用收纳盒存放耗材，还需在其中放置干燥剂（推荐使用硅胶干燥剂）。

![收纳箱.jpeg](https://wiki.bambulab.com/filament-acc/filament/tpu-85a-90a-printing-guide/%E6%94%B6%E7%BA%B3%E7%AE%B1.jpeg)  
请在收纳箱中放置硅胶干燥剂后存放耗材。

## 常见打印问题

TPU 材料容易出现下列问题：

1. 缺料（堵头、进料阻力、耗材打滑）；
2. 卡挤出（耗材弯曲卡住挤出齿轮，需拆开挤出机后扯出卡住耗材）；
3. 拉丝漏料（使用大口径热端，微调回抽，进一步烘干耗材，模型后处理）。

详细问题解决方法，请参考此 wiki：[常见打印质量问题和解决办法](../../knowledge-sharing/common-print-quality-problem.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
