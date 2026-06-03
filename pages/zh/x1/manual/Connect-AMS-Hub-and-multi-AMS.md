---
path: zh/x1/manual/Connect-AMS-Hub-and-multi-AMS
title: "连接 AMS Hub 和多台 AMS"
description: "本指南介绍如何使用 AMS Hub 连接多台 AMS。"
tags: ["x1", "ams hub"]
created: 2022-12-18T14:30:49.922Z
updated: 2026-02-09T11:34:05.290Z
source: https://wiki.bambulab.com/zh/x1/manual/Connect-AMS-Hub-and-multi-AMS
---

## **供料缓冲器和 AMS Hub**

打印机的原装供料缓冲器只能连接1个 AMS。更换为 AMS Hub 后，打印机最多可连接 4 个 AMS。

![](https://wiki.bambulab.com/ams/ams-hub/buffer_hub.png)

供料缓冲器购买链接：  
[京东](https://item.jd.com/10060212416887.html)  
[天猫](https://detail.tmall.com/item.htm?abbucket=8&id=694049363219&rn=3f1570182437f0b131adfd3122648cc0&spm=a1z10.3-b-s.w4011-25177047232.22.42c01c79unkjoE&skuId=4927623665956)

AMS Hub 购买链接：  
[京东](https://item.jd.com/10059378244689.html)

### 连接 AMS Hub 和多台 AMS

在开始之前，请参考[AMS主要组件介绍](intro-ams.md)来熟悉 AMS。您还需要提前阅读[AMS的温馨提示](../../knowledge-sharing/notes-ams.md)，以了解一些注意事项。

### 将 AMS Hub 连接到打印机

请从打印机背面移除缓冲器（如已安装）并安装 AMS Hub，如下图所示。在安装了 AMS Hub 后，继续从 AMS Hub 连接 PTFE 管到气管接头。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/ptfe_couple.jpg)

另外，若您使用的是料管拓展口，您可以同时将 4 个来自不同模块的耗材连接到打印机，安装方式如下图所示。更多的相关信息请参考：[料管拓展口使用指南](../../parts-acc/ptfe_adapter.md)

|  |  |
| --- | --- |
| P1P | P1S & X1 |

请确保 PTFE 管从料盘支架下方穿过，而不是上方，如下图所示。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/avoid_ptfe_from_touching_spool_holder.png.jpg)

确保 AMS Hub 弹簧没有被卡住，而且滑块能够自由移动。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/check_if_spring_stuck.png.jpg)

用拓竹 4pin 线将 AMS Hub 连接到打印机:

**注意：4pin 线的方向不要插错，如果您使用的是 L 型插头线缆，请注意上面的文字提示，如果插错方向有可能导致打印机和 AMS 的主板烧毁。**

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/4p_dir.png)

4pin 电缆（正确插入方向）

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/l%E5%9E%8B%E6%8F%92%E5%A4%B4.png)

**L 型插头线缆**

4 pin 数据线购买链接：  
[天猫](https://detail.tmall.com/item.htm?abbucket=8&id=694052067560&rn=6dee6347fc0700796c6bbcc4a808a0c3&skuId=4926397845849&spm=a1z10.3-b-s.w4011-25177047232.78.7a331c792Hzkky)

### 将 AMS 连接到 AMS Hub

#### 连接线缆

将最常用的 AMS 连接到 AMS Hub 并打开打印机，然后继续将剩余的 AMS 连接到前一个 AMS 的另一个6 pin 数据线端口。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/cable_connect_and_id.png)

> 温馨提示：我们的商城售卖 2 种长度的 6 pin 总线（510 mm(常用于耗材缓冲器 和 AMS之间的连接)；1500 mm（常用于 Hub 和 AMS 之间的连接）），如果你需要更长的 6pin 数据线，请前往电商平台购买。具体需要什么长度的 6pin 总线，请以您的实际情况为准。

6pin 数据线购买链接：  
[京东 (6pin数据线AMS HUB 1.5m)](https://item.jd.com/10060214717858.html)  
[天猫 (6pin数据线AMS HUB1.5m)](https://detail.tmall.com/item.htm?abbucket=8&id=693215008278&rn=6dee6347fc0700796c6bbcc4a808a0c3&spm=a1z10.3-b-s.w4011-25177047232.94.7a331c792Hzkky&skuId=4927623013811)  
[天猫 (6pin数据线AMS HUB 510mm)](https://detail.tmall.com/item.htm?abbucket=8&id=694052067560&rn=6dee6347fc0700796c6bbcc4a808a0c3&skuId=4926397845848&spm=a1z10.3-b-s.w4011-25177047232.78.7a331c792Hzkky)

### 将 AMS 的 PTFE 管连接到 Hub 上

合适的 PTFE 管长度是很重要的。我们建议在不过度弯曲的情况下，使其尽可能短，以减少 AMS 进给阻力和进料/退料时间：

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/multi_ams_and_hub_connect.jpg)

**注意：连接多 AMS 到 Hub 时，建议 PTFE 管最长不超过 3.5m，送料路径太长有可能导致过大的阻力从而影响正常进退料。同时也要注意不要让 PTFE 管弯曲过多而导致额外的阻力。**

### 检查连接是否成功

安装已完成，请检查您的打印机，确保 AMS Hub 和其他 AMS 单元已正确安装。以下图片为成功安装的示例，请参考。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/check_the_connection.jpg)

您可以参考这篇 Wiki：[多色打印操作指导 | Bambu Lab Wiki](multi-color-printing.md)，了解更多多色打印相关内容。

> 连接成功后，您需要**通过离线升级或者在线升级将 AMS Hub 和 AMS 升级至最新版本**。如果打印机与 AMS Hub 和 AMS 的版本不一致，很可能打印失败。

## 提示

### 1. AMS ID 分配

每个 AMS 都会被分配一个 ID 并显示在屏幕上。分配 AMS ID 是为了让人容易识别它们之间的连接，分配 ID 的逻辑是直接连接到 AMS Hub 的是 AMS 1，连接到 AMS 1 的是 AMS 2，以此类推。

> 注意  
> 您需要分别连接它们，以便能够按顺序分配 ID。**执行此操作时，请确保打印机处于开机状态**。
>
> 但是，如果您提前将多个 AMS 组件连接在一起，然后在最后连接到 AMS Hub，或者在打印机开机之前将所有 AMS 连接到 AMS Hub，则打印机将随机为这些 AMS 分配 ID。

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/assign_ams_id.png)

AMS 1 连接到 Hub，AMS 2连接到 AMS 1

![](https://wiki.bambulab.com/x1/manual/connect-ams-hub/ams_id.png)

AMS 有“映射”功能（参考[多色打印操作指南](multi-color-printing.md)），所以 AMS 的 ID 不会影响新的打印，但内置的型号会受到影响。请参考提示2。

**如何重置 AMS ID**

即使关闭打印机，AMS ID 也会被保存而不会被清除。你可以参考下图来重置 AMS ID：

![](https://wiki.bambulab.com/x1/manual/release-note/u3/%E9%87%8D%E7%BD%AEams_id.png)  
**注意：点击重置AMS ID后，AMS会暂时丢失通信（四个槽全闪红灯），这是正常现象。你可以拔掉 AMS 背后的6-pin线缆，按照想要的顺序依次重新连接即可。**

### 2. 打印内置模型

目前**打印内置模型只支持从 AMS 1 的 1 号槽位开始打印**，不支持映射到其他槽位。您需要根据打印准备页面上的提示，按顺序从左到右将料线放入 AMS 插槽：

![](https://wiki.bambulab.com/x1/manual/muti-color-print/%E5%86%85%E7%BD%AE%E6%A8%A1%E5%9E%8B%E5%B1%8F%E5%B9%95%E6%8F%90%E7%A4%BA.png)
