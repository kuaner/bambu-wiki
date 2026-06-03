---
path: zh/h2/h2d-tpu-printing-guide
title: "H2 系列的 TPU 打印准备工作"
description: ""
tags: []
created: 2025-03-25T02:38:44.805Z
updated: 2026-06-02T04:13:03.670Z
source: https://wiki.bambulab.com/zh/h2/h2d-tpu-printing-guide
---

> H2S 及 H2C 在打印特定类型的 TPU 时，进料方式和 H2D 基本相同，以下内容以 H2D 机型展示，不影响实际操作。

## 前言

TPU 耗材根据软硬程度可以分为 TPU For AMS、TPU 95A、 TPU 90A、TPU 85A。其中 TPU For AMS 硬度较高，进退料要求较低，能够直接放入 AMS 中使用；而 95A 及以下的耗材，其进料要求偏高，需避免进料阻力过大影响打印质量。

关于 TPU 耗材的详细介绍，请跳转至《[TPU 介绍](../knowledge-sharing/tpu-printing-guide.md)》。

## TPU 进料视频指南

## 准备工作

### 耗材烘干

TPU 具有较强的吸湿性，在自然环境中容易吸收水分。含有水分的 TPU 会严重影响打印质量，因此我们推荐您使用前烘干 TPU 耗材。详情请参考此 wiki：[耗材准备——干燥](../filament-acc/filament/dry-filament.md)

在烘干过程中，TPU 受热膨胀会导致料盘变形，**可能从 65.4 mm 增大到约 69.4 mm**，这是正常现象。可使用耐高温重物压在 TPU 料盘上抑制变形。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/20250211-112835.jpg)

### 硬件适配

| 项目 | TPU 85A | TPU 90A | TPU 95A HF | TPU for AMS |
| --- | --- | --- | --- | --- |
| **打印机适配性** | H2 系列（H2D / H2C 仅能从右进料口进料） | H2 系列（H2C 仅能从右进料口进料） | H2 系列（H2C 仅能从右进料口进料） | H2 全系列 |
| **喷嘴兼容性** | **推荐：** 0.6 mm / 0.8 mm / TPU 高流量喷嘴  **不推荐：** 高流量喷嘴  **不支持：** 0.2 mm / 0.4 mm | **推荐：** 0.4 mm / 0.6 mm / 0.8 mm / TPU 高流量喷嘴  **不推荐：** 高流量喷嘴  **不支持：** 0.2 mm | **推荐：** 0.4 mm / 0.6 mm / 0.8 mm / TPU 高流量喷嘴  **不支持：** 0.2 mm / 高流量喷嘴 | **推荐：** 0.4 mm / 0.6 mm / 0.8 mm / TPU 高流量喷嘴  **不支持：** 0.2 mm / 高流量喷嘴 |
| **配件兼容性（打印板 / 胶水 / AMS 等）** | - 打印板：光面 PEI、纹理 PEI  - 胶水：无需涂胶  - AMS / AMS lite / AMS 2 Pro：**不兼容**  - AMS HT：兼容 | - 打印板：光面 PEI 板、纹理 PEI 板   - 胶水：无需涂胶   - AMS / AMS lite / AMS 2 Pro：**不兼容**  - AMS HT：兼容 | - 打印板：光面 PEI 板、纹理 PEI 板   - 胶水：Bambu 液体胶 / 固体胶棒   - AMS / AMS lite / AMS 2 Pro：**不兼容**  - AMS HT：兼容 | - 打印板：光面 PEI、纹理 PEI  - 胶水：Bambu 液体胶 / 固体胶棒   - AMS / AMS lite / AMS 2 Pro / AMS HT：**兼容** |
| **耗材混合适配性** | - H2D / H2C ：**支持**与其他耗材混合打印 | - H2D / H2C ：**支持**与 PLA/PETG 多材料混合打印 | - H2D / H2C ：**支持**与 PLA/PETG 多材料混合打印 | - H2D / H2C ：**支持**与 PLA/PETG 多材料混合打印 |

> 📌 **重要提醒：**  
> **使用 TPU 耗材时需特别注意喷嘴适配，请勿使用 0.2mm 喷嘴与普通高流量喷嘴，其中 85A TPU 不兼容普通 0.4mm 喷嘴。**  
> 建议不要使用曾打印过碳纤增强、玻纤增强等纤维类耗材的热端，这类耗材残留的纤维会大幅增加挤出阻力，极易引发堵塞问题，若需打印 TPU，建议先冷拔 3-5 次而后发起打印。  
> 关于 H2D 如何使用 TPU 高流量喷嘴，请点击 [TPU 高流量套件使用指南 - H2D系列](../h2d/manual/tpu-high-flow-hotend.md) 查看。

## 进料工作

### AMS HT/5.8L 米桶

若使用米桶进料，请务必打印米桶支架（模型链接如下），确认料线旋转顺畅。  
[5.8L 米桶干燥箱支架](https://makerworld.com.cn/zh/models/437644?from=search#profileId-353897)

此外，为了减小进料阻力，请从料桶的侧边开口。

|  |  |
| --- | --- |
|  |  |

#### 使用 AMS HT / 米桶打印

> **注意事项**
>
> 1. 进料前，确保 TPU 已经充分干燥。
> 2. 除 TPU For AMS 以外其他 TPU 都需要手动进料，不可以使用 AMS 进行自动进料。
> 3. TPU 85A 不能通过 PTFE 管进料，需直接送入挤出机。TPU 90A(95A) 可使用 PTFE 管，连接到打印机背面的专用进料口。
> 4. 建议固定 AMS HT 或料桶，防止出料口位置变动增加进料阻力，导致打印失败。

- 断开右热端的 PTFE 管。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/image-17.png)

- 断开缓冲器上，右热端连接的 PTFE 管；

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/image-1.png)

> 85A TPU 请直接取下 PTFE 管，耗材直接插入工具头。95A 或 90A 请继续下一步。
>
> |  |  |
> | --- | --- |
> |  |  |

- 将 PTFE 管末端**插入 H2D 后方的 TPU 专用进料口**；

|  |  |
| --- | --- |
|  |  |

- 把工具头推动屏幕后方的极限位置，此时仓内的料管长度为合适长度。

|  |  |
| --- | --- |
|  |  |

- 裁剪 5cm 长的 PTFE 管，并将 PTFE 管微微弯折。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/img_v3_02ko_bb2cc848-debd-4a87-b9b0-880dbaf36cfg.png)

- 打开 AMS HT 尾部的硅胶塞，将 PTFE 管凸起一侧朝上，将 PTFE 管插入硅胶塞的小孔，**确保插入 AMS HT 的长度为 5mm**。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/dsc00667.jpg)

- 将耗材放入 AMS HT 中，并将耗材穿过 PTFE 管，再扣紧 AMS HT 上盖。

![](https://wiki.bambulab.com/filament-acc/tpu/image10.png)

- 确认耗材的转动方向如下图所示。

![](https://wiki.bambulab.com/filament-acc/tpu/image11.png)

- 调整 AMS HT 的高度，保证出料口与 H2D 背后的进料口平齐，以减小进料阻力。您可以使用打印的[辅助模型](https://makerworld.com.cn/zh/models/983129-tpuxian-cai-juan-zhou-jia?from=search#profileId-1004263)来帮助调整高度。

![dsc00676.jpg](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/dsc00676.jpg)

- 从 AMS HT 上的 TPU 专用出料口扯出料线，手动将 95A/90A 料线推入 PTFE 管，直到 TPU 被推出。

|  |  |
| --- | --- |
|  |  |

- 设定热端温度为 250 ℃。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/image-16.png)

- 手动将料线前端推入挤出机，点击屏幕上挤出机 “向下箭头” 手动控制挤出机齿轮旋转。**请勿连续快速点击，避免 TPU 卷入挤出机齿轮中，造成堵塞。**

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/image-9.png)

- 当 TPU 耗材被顺利咬合并挤出后（热端处看见料线被连续挤出），再将 PTFE 管插回工具头(**85A 无需该插回 PTFE管**)，开始打印任务。

![](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/image-8.png)

> 若该方式下 95A/90A 耗材出现了打印报错或打印件缺料等异常现象，请使用 TPU 85A 进料方式或顶部进料架。

### 顶部进料架

H2 系列打印机打印 TPU 时，可**打开上盖从顶部进料**（搭配 [H2D 柔性耗材顶部进料架](https://makerworld.com/en/models/1421552-h2d-flexible-filament-top-feed-rack#profileId-1477010)。这种方式送料路径最短、阻力最小，能够更好地适配 **90A 和 85A** 等高柔性耗材，打印稳定性更高。

![顶部料架示意.png](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/%E9%A1%B6%E9%83%A8%E6%96%99%E6%9E%B6%E7%A4%BA%E6%84%8F.png)

#### 使用顶部料架

- 打开顶盖，并移除原有的 PTFE 管；

|  |  |
| --- | --- |
|  |  |

- 安装好顶部进料架，裁切新的 PTFE 管并安装。

![安装示意3.png](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/%E5%AE%89%E8%A3%85%E7%A4%BA%E6%84%8F3.png)

具体使用方法以及安装教程请参考该模型链接：[H2D Flexible Filament Top-feed Rack](https://makerworld.com/zh/models/1421552-h2d-flexible-filament-top-feed-rack#profileId-1477010)。

### TPU 送料助力模块

TPU 送料助力模块是一款专为柔性耗材打印设计的增强组件。能够降低 TPU 耗材在各种摆放场景下的进料阻力，有效解决柔性耗材进料卡顿、断料问题，大幅提升 TPU 打印的稳定性和成功率。并且简化 TPU 打印的进料流程，减少打印前的准备工作，支持封箱打印，可直接从 TPU 专用进料口进料，操作更便捷。请[点击此处](../general/manual/tpu-feed-assist-module.md)了解该模块的详情使用说明。

![](https://wiki.bambulab.com/general/tpu-feed-assist-module/036.jpg)

## **常见打印问题**

- 模型表面缺料（可能的原因是堵头、进料阻力过大、料线打滑），可参考 [H2D TPU 堵塞排查](troubleshooting/tpu-clogging.md)
- 挤出机缠料：料线弯曲卡住挤出齿轮，需拆开挤出机后扯出卡住料线，请参考：[H2D 挤出机拆解与组装指引](troubleshooting/extruder-assembly.md)
- 拉丝漏料： 微调回抽参数，每次增加 0.1mm 回抽量；进一步烘干料线；后处理清理拉丝。

## 耗材存储

建议将 TPU 耗材存放在湿度低于 20% RH 的环境中，可使用密封收纳盒进行存放，并且在收纳盒内放置足够量的干燥剂。注意湿度较低依然无法避免耗材受潮，这仅能够减缓受潮速度。

![img_v3_02ju_86ecc06d-55a3-4cb8-b0bf-0fd113f6de2g.jpg](https://wiki.bambulab.com/h2/manual/h2d-tpu-printing-guide/img_v3_02ju_86ecc06d-55a3-4cb8-b0bf-0fd113f6de2g.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
