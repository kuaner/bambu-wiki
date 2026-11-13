---
path: zh/h3c/manual/ams-connection-guide
title: "拓竹H3C 外接多台 AMS 指南"
description: ""
tags: []
created: 2026-11-03T13:20:11.389Z
updated: 2026-11-11T01:28:59.307Z
source: https://wiki.bambulab.com/zh/h3c/manual/ams-connection-guide
---

## 前言

拓竹H3C 支持**单独连接一/二代 AMS**，且支持**同时连接一/二/三代 AMS**。如果您有更高阶的多色打印需求，可以通过连接已有的或额外购买的 AMS 设备进行扩展。拓竹H3C 最多可同时连接 **1 台 AMS 3 和 4 台 AMS/AMS 2 Pro/AMS HT**，实现最高 **24 色**打印。

![h3c______ams___-image-14.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-14.png)

本指南将详细介绍最高 24 色配置的连接方法、配件需求及 AMS ID 分配规则。

## 固件版本要求

需将打印机固件更新至 01.01.00.00 及以上版本。

## 所需配件

| **名称** | **数量** | **备注** |
| --- | --- | --- |
| AMS | 4 | 根据所需的 AMS 数量而定 |
| 外接 AMS 缓冲器 | 1 | 外观与 P2S 缓冲器相似，但与以往机型的缓冲器均不通用 |
| 6-pin 线缆 | 4 | 等同于 AMS 数量 |
| 四进一料管拓展口 | 1 | 需自行购买，黑色白色均可，当连接2台以上一/二代 AMS时必须； |
| AMS 料管 | 4 | 等同于 AMS 数量，推荐长度：  - AMS 放打印机**同侧**：700 mm\*2；1100 mm\*2 - AMS 放打印机**异侧**：700 mm\*4 |
| 缓冲器——气动接头料管 | 1 | 480mm 左右 |
| 缓冲器——四进一料管拓展口料管 | 1 | 70mm 左右 |

**模型打印**

为优化多台 AMS 的摆放空间，建议您一并打印 AMS 双层支架模型（[推荐支架模型](https://makerworld.com/en/models/1358146-ams-1-2-pro-dual-rack-stack-fully-3d-printed?from=search#profileId-1453787)）。

![h3c______ams___-image-9.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-9.png)

## 操作步骤

连接开始前，请先**关闭打印机电源**，并按照下图建议摆放 AMS，同侧/异侧均可。本文将以**异侧**为例，介绍具体连接步骤。

|  |  |
| --- | --- |
| h3c______ams___-image-10.png | h3c______ams___-image-11.png |

### 步骤一：移除 6-pin 接口板

- 移除 6-pin 接口板的两颗螺丝；

![h3c______ams___-image.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image.png)

- 松开金属板，露出连接器；按压插头卡扣进行解锁，断开插头。

|  |  |
| --- | --- |
| h3c______ams___-image-1.png | h3c______ams___-image-2.png |

### 步骤二：安装外接 AMS 缓冲器

- 将插头对准缓冲器接口插入；

|  |  |
| --- | --- |
| h3c______ams___-image-3.png | h3c______ams___-image-4.png |

- 将缓冲器安装至背板上；

![h3c______ams___-image-5.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-5.png)

- 锁紧两颗螺丝进行固定。

![h3c______ams___-image-6.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-6.png)

### 步骤三：连接 AMS 线缆

参考下图，使用 4 根 6-pin 线将打印机与 4 台 AMS 连接，AMS 间通过线缆串联。

> 注：可根据打印机位置摆放自行选择合适长度的线缆。

![h3c______ams___-image-7.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-7.png)

### 步骤四：连接 AMS 料管

- 按压 1 号打印头气动接头，移除后半部分料管；

![h3c______ams___-image-15.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-15.png)

- 取一根 **480 mm** 左右的料管，下端插入缓冲器，上端从打印机背板的外挂料盘进料口穿进，插入 1 号打印头气动接头处；

|  |  |
| --- | --- |
| h3c______ams___-image-16.png | h3c______ams___-image-17.png |

- 使用一根 **70 mm** 左右的短料管连接四进一料管拓展口和缓冲器的任意一接口；

![h3c______ams___-image-18.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-18.png)

- 使用 4 根至少 **700 mm** 的料管连接 4 台 AMS。

![h3c______ams___-image-19.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-19.png)

> **注意：**如果将 4 台 AMS 放在机器同侧，则推荐的料管长度为：
>
> - 靠近打印机的两台 AMS：约 **700 mm**
> - 远离打印机的两台 AMS：约 **1100 mm**
>
> ![h3c______ams___-image-20.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-20.png)

## AMS ID 排序

> 注：只连接 AMS 3H 时无此功能。

AMS 的 ID 由打印机根据线缆连接关系自动分配，而非根据设备摆放位置分配。当打印机连接多台 AMS 时，每台 AMS 都会被自动分配唯一的 ID 并显示在打印机屏幕上，方便用户直观识别各设备间的连接关系。

### 分配逻辑

**AMS/ AMS 2 Pro 排序**：

- 直接连接打印机的 AMS，ID 默认为 AMS-A；
- 连接 AMS-A 的 AMS，ID 为 AMS-B；
- 后续依次连接的 AMS，按 “AMS-C、AMS-D” 的顺序类推。

**AMS HT 排序**：

- 等 AMS/AMS 2 Pro 完成 ID 分配后，打印机才会对 AMS HT 进行排序；
- AMS HT 的 ID 默认从 “HT-A” 开始，后续依次按 “HT-B、HT-C……” 的顺序分配。

### 如何重置 AMS ID？

AMS ID 由打印机根据线缆连接顺序自动分配。若连接时未按照**从打印机到 AMS 依次串联**的顺序操作（例如先将所有 AMS 串联后再接入打印机），开机后屏幕显示的 AMS ID 可能与预期顺序不符。如需调整，可参考以下步骤重置 AMS ID：

1. 在屏幕上点击“**设置 > AMS 选项 > 重新排序 AMS”**；

![h3c______ams___-img_v3_02156_0b9b00a3-9ddc-4fc2-bd24-bd28ae7085fg.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-img_v3_02156_0b9b00a3-9ddc-4fc2-bd24-bd28ae7085fg.png)

- **待所有 AMS 的槽位都闪红灯后**，再断开线缆，按照所需顺序重新连接；

> 注意：请务必等到 AMS 四个槽红灯闪烁后再断开线缆，否则重置不会生效。

![h3c______ams___-xbq1h5ns.webp](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-xbq1h5ns.webp)

3. 在屏幕上进入**耗材**页面，或在 Bambu Studio 中进入**设备**页面，检查 AMS ID 顺序是否完成更新。

> 注：重新排序后，屏幕和软件中的 AMS 标识顺序可能发生变化，请确认当前使用的耗材槽位是否与实际一致。

## FAQ

**Q：拓竹H3C 能否只连接一/二代 AMS？**

拓竹H3C 可以只外接一/二代 AMS 进行打印。

**Q：拓竹H3C 连接不同 AMS 时，6-pin 线能否共用？**

目前已统一一代和二代的 AMS 6-pin 线，因此可以共用。

**Q：已有 AMS，如果想购买拓竹H3C，能否直接用拓竹H3C 连接 AMS？还需购买什么配件？**

拓竹H3C 可直接连接一/二代 AMS 设备，但需要额外购买全新的外接 AMS 缓冲器配套使用；

![h3c______ams___-image-21.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/ams-connection-guide/zh/h3c______ams___-image-21.png)

请注意，连接**两台以上**（最多 4 台）AMS 时，还需额外购买**四进一料管拓展口**（以下两款皆可）。

|  |  |
| --- | --- |
| h3c______ams___-image-22.png | h3c______ams___-image-23.png |

> 需要说明的是，拓竹H3C 虽然可以不连接AMS 3H单独使用1代和2代AMS，但必须正常连接打印头和控制板；同时，因打印头与打印头控制板随AMS 3H一体包装，您仍需完成AMS 3H的安装，只是无需连接AMS 3H 的6pin线缆。

**Q：只有1号打印头支持外接AMS吗？**

拓竹H3C 配备了 9 个打印头，已经能够很好地满足绝大多数用户在多色、多材料打印方面的需求。目前我们仅让 1 号打印头支持外接 AMS，主要是出于两方面的考虑：

- 更简洁的料管排布，提升整机的稳定性与可靠性；
- 这一设计能够覆盖绝大部分用户的日常使用需求。

**Q：能否同时在 1 号打印头使用 AMS 3H 的 1 号槽和外接 AMS 为 1 号打印头供料？**

关于同时使用旧款 AMS 和 AMS 3H 为 1 号打印头送料的需求：软件上是支持同时调用的，不过硬件结构上需要您进行一点小改装。

具体的操作方案和注意事项如下：  
**1. 硬件改装方案（实现“两进一出”）**  
要在同一个打印任务中同时调用两台 AMS 供料，为了避免平常频繁手动插拔气动接头，您需要在硬件上加装 Y 通（或类似转接件）：将目前 1 号打印头料管上的气动接头改装为 Y 通（或类似产品），为 1 号头提供两个进料入口。

> 改装提示：
>
> - 目前官方暂无现成的 Y 通转接头售卖，只有一通四的转接口。由于一通四的转接口长度比普通气动接头稍长，安装时务必注意进料阻力和走线，建议使用特氟龙内衬结构，并确保料管没有过大的弯折角度，防止因阻力过大导致送料异常。
> - 我们出厂在 1 号打印头料管上标配单气动接头，主要是为了帮用户将料管阻力严格控制在安全范围内，这是平衡“打印成功率”与“便捷度”的最佳方案。DIY 加装 Y 通后，需要有经验的用户自行把控好料管路径。

**2. 软件提示与摆放技巧（避免手动换料）**  
由于 AMS 3H 没有自动退料功能，如果您在同一个打印任务中同时调用了 AMS 3H 槽位 和 外接 AMS 槽位，软件可能会弹出提示：“由于 AMS 3H 没有退料功能，打印过程中可能需要手动换料……”  
为了实现全自动无缝切换、规避手动换料，您需注意耗材的摆放顺序：**先将打印任务中先要用的耗材放到旧款 AMS 中（因为旧 AMS 具备自动退料功能），然后将后要用的耗材放到 AMS 3H 中。**

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
