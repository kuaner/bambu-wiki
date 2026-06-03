---
path: zh/h2c/how-to-connect-ams
title: "H2C + 多台 AMS 连接指南"
description: "本文介绍了如何将 H2C 与多台 AMS 进行连接"
tags: []
created: 2025-11-18T12:40:45.348Z
updated: 2026-03-20T10:05:30.443Z
source: https://wiki.bambulab.com/zh/h2c/how-to-connect-ams
---

针对 H2C 打印机的双喷嘴特性与 AMS 的耗材切换能力，本文为 H2C 打印机搭配 AMS 实现多色打印提供完整配置指南，帮助用户快速上手多色打印。

## H2C 连接多台 AMS

如果您有多台 AMS，可将其连接至右热端，利用多个感应热端减少切换耗材时浪费的耗材，并提高打印速度。

H2C 最多可安装 6 个右热端交替使用，满足多耗材打印的切换需求。**推荐您在 H2C 右热端连接 2 台 AMS**，以获得更好的多色打印体验。

如需连接多台 AMS，请使用 H2C 专用的四进一料管拓展口。与其他系列的拓展口不同，H2C 新版本四进一料管拓展口在出口端集成了一块清洁刮片，可以有效拦截耗材碎屑与表面灰尘，防止碎屑在热端与切刀之间堆积，避免切刀卡住，进而减少因为碎屑堆积导致的小概率右侧感应热端切换失败问题。

|  |  |
| --- | --- |
| X/P 系列料管拓展口 | H2C 四进一料管拓展口 |

### **AMS 摆放建议**

**方法一：**一台 AMS 2 Pro 和 AMS HT 放置在打印机顶部，另一台 AMS 2 Pro 放置在地面。此方法需预留约 900\*1020\*1100 ㎜³ 的空间。

> 注意：为保证不同摆放方式下料管长度足够，随机器附送的铁氟龙料管长度为 900mm。将 AMS 2 Pro 和 AMS HT 放置在打印机顶部时，**适当剪短料管长度**（最短可剪短至 600mm）可以缩短换料时间，提高打印速度。

|  |  |
| --- | --- |
|  |  |

**方法二：**打印 AMS 双层支架（[推荐支架模型](https://makerworld.com/en/models/1358146-ams-1-2-pro-dual-rack-stack-fully-3d-printed?from=search#profileId-1453787)），将两台 AMS 2 Pro 放置在打印机顶部的支架上，AMS HT 放置在地面。此方法需预留约 650\*1020\*1300 ㎜³ 的空间。

|  |  |
| --- | --- |
|  |  |

## 视频指南

## 连接步骤

> 注意：本指南将演示方法一的连接步骤。

### 步骤一：连接四进一料管拓展口和打印机

- 从配件盒中取出最短的料管，插入打印机背面的上进料口中，确保向前推送铁氟龙料管直至无法前进。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/how-to-connect-ams/image-2.png)

- 将四进一料管拓展口插入料管另一端。

![screenshot-20251113-112735.png](https://public-cdn.bblmw.com/wiki/new/h2c/manual/how-to-connect-ams/screenshot-20251113-112735.png)

### 步骤二：连接打印机和 AMS 2 Pro

- 使用 AMS 2 Pro 的料管（900mm）连接四进一料管拓展口和打印机上 AMS 2 Pro 的出料口。

|  |  |
| --- | --- |
|  |  |

- 使用另一根长料管连接四进一料管拓展口和地面上的 AMS 2 Pro。

|  |  |
| --- | --- |
|  |  |

### 步骤三：连接打印机和 AMS HT

使用 AMS HT 随机附送的铁氟龙料管连接打印机机箱下的进料口和 AMS HT 出料口，确保向前推送料管直至无法前进。

|  |  |
| --- | --- |
|  |  |

### 步骤四：连接线缆

- 使用 6-pin 线连接打印机和打印机上 AMS 2 Pro 的 6-pin 接口。

|  |  |
| --- | --- |
|  |  |

- 使用 6-pin 连接打印机上的 AMS 2 Pro 和 AMS HT。

|  |  |
| --- | --- |
|  |  |

- 使用一根长的 6-pin 线连接 AMS HT 与地面上的 AMS 2 Pro。

|  |  |
| --- | --- |
|  |  |

> 注意：如需[连接多台 AMS](../ams/manual/multi-model-AMS-compatibility-guide.md)，方法同理，H2C 最多支持同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT。

### 步骤五：烘干耗材

如果需要使用 AMS 2 Pro 的烘干功能，除了直接连接至打印机的 AMS 2 Pro，其余 AMS 2 Pro 必须使用官方电源适配器供电。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/how-to-connect-ams/image-13.png)

如果需要使用 AMS HT 的烘干功能，则需要使用外接交流电源线供电。

![screenshot-20251113-115045.png](https://public-cdn.bblmw.com/wiki/new/h2c/manual/how-to-connect-ams/screenshot-20251113-115045.png)

### 步骤六：连接完成

连接完成后的背面图如下：

|  |  |
| --- | --- |
| 方法一 | 方法二 |

可在打印机屏幕的耗材页面查看 AMS 连接。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/how-to-connect-ams/z30_7884.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
