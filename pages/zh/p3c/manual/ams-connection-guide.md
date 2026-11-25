---
path: zh/p3c/manual/ams-connection-guide
title: "P3C 连接多台 AMS 指南"
description: "本文介绍如何为 P3C 连接多台 AMS。"
tags: ["manual", "p3c"]
created: 2026-11-24T14:02:06.534Z
updated: 2026-11-24T14:02:06.534Z
source: https://wiki.bambulab.com/zh/p3c/manual/ams-connection-guide
---

## 前言

P3C 支持**单独连接一/二代 AMS**，且支持**同时连接一/二/三代 AMS**。如果您有更高阶的多色打印需求，可以通过连接已有的或额外购买的 AMS 设备进行扩展。P3C 最多可同时连接 **1 台 AMS 3 和 4 台 AMS/AMS 2 Pro/AMS HT**，实现最高 **22 色**打印。

> 注：标配 5 个打印头最多可实现 20 色打印；如需实现最高 22 色打印，则需另购 2 个打印头。

![001.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/001.jpg)

本指南将详细介绍最高 22 色配置的连接方法、配件需求及 AMS ID 分配规则。

## 所需配件

| **名称** | **数量** | **备注** |
| --- | --- | --- |
| AMS | 4 | 根据所需的 AMS 数量而定 |
| 外接 AMS 缓冲器 | 1 | 外观与 P2S 缓冲器相似，但与以往机型的缓冲器均不通用 |
| 6-pin 线缆 | 4 | 等同于 AMS 数量 |
| 四进一料管拓展口 | 1 | 需自行购买，黑色白色均可，连接**两台以上**（最多 4 台）AMS 时 Image Image |
| AMS 料管 | 4 | 等同于 AMS 数量，推荐长度： - AMS 放打印机**同侧**：700 mm\*2；1100 mm\*2 - AMS 放打印机**异侧**：700 mm\*4 |
| 缓冲器——气动接头料管 | 1 | 460 mm 左右 |
| 缓冲器——四进一料管拓展口料管 | 1 | 70mm 左右 |
| 打印头 \* 2（选购） |  | 标配 5 个打印头最高支持 20 色打印，加购 2 个打印头后最高可达 22 色。 |

**模型打印**

为优化多台 AMS 的摆放空间，建议您一并打印 AMS 双层支架模型（[推荐支架模型](https://makerworld.com/en/models/1358146-ams-1-2-pro-dual-rack-stack-fully-3d-printed?from=search#profileId-1453787)）。

![004.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/004.png)

## 操作步骤

连接开始前，请先**关闭打印机电源**，并按照下图建议摆放 AMS。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/005.jpg)

### 步骤一：移除 6-pin 接口板

- 移除 6-pin 接口板的两颗螺丝；

![006.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/006.png)

- 松开金属板，露出连接器；按压插头卡扣进行解锁，断开插头。

![007.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/007.png)

### 步骤二：安装外接 AMS 缓冲器

- 将插头对准缓冲器接口插入；

![008.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/008.png)

- 将缓冲器安装至背板上；

![009.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/009.png)

- 锁紧两颗螺丝进行固定。

![010.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/010.png)

### 步骤三：连接 AMS 线缆

参考下图，使用 4 根 6-pin 线将打印机与 4 台 AMS 连接，AMS 间通过线缆串联。

> 注：可根据打印机位置摆放自行选择合适长度的线缆。

![011.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/011.png)

### 步骤四：连接 AMS 料管

- 按压 1 号打印头气动接头，移除后半部分料管；

![012.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/012.png)

- 取一根 **460 mm** 左右的料管，下端插入缓冲器，上端从打印机背板的外挂料盘进料口穿进，插入 1 号打印头气动接头处；

|  |  |
| --- | --- |
| 013.png | 014.png |

- 使用一根 **70 mm** 左右的短料管连接四进一料管拓展口和缓冲器的任意一接口；

![015.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/015.png)

- 使用 4 根至少 **700 mm** 的料管连接 4 台 AMS。

![016.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/016.png)

> \*\*注意：\*\*如果将 4 台 AMS 放在机器同侧，则推荐的料管长度为：靠近打印机的两台 AMS：约 \*\*700 mm；\*\*远离打印机的两台 AMS：约 **1100 mm。**
>
> ![017.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/017.png)

## AMS ID 排序

> 注：只连接 AMS 3P 时无此功能。

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

![018.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/018.png)

2. **待所有 AMS 的槽位都闪红灯后**，再断开线缆，按照所需顺序重新连接；

> 注意：请务必等到 AMS 四个槽红灯闪烁后再断开线缆，否则重置不会生效。

![019.webp](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/019.webp)

3. 在屏幕上进入**耗材**页面，或在 Bambu Studio 中进入**设备**页面，检查 AMS ID 顺序是否完成更新。

> 注：重新排序后，屏幕和软件中的 AMS 标识顺序可能发生变化，请确认当前使用的耗材槽位是否与实际一致。

## FAQ

**Q：P3C 能否只连接一/二代 AMS？**

P3C 可以只外接一/二代 AMS 进行打印。

**Q：P3C 连接不同 AMS 时，6-pin 线能否共用？**

目前已统一一代和二代的 AMS 6-pin 线，因此可以共用。

**Q：已有 AMS，如果想购买 P3C，能否直接用 P3C 连接 AMS？还需购买什么配件？**

P3C 可直接连接一/二代 AMS 设备，但需要额外购买全新的外接 AMS 缓冲器配套使用；

![020.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/ams-connection-guide/zh/020.png)

请注意，连接**两台以上**（最多 4 台）AMS 时，还需额外购买**四进一料管拓展口**（以下两款皆可）。

|  |  |
| --- | --- |
| 021.png | 022.png |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
