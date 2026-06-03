---
path: zh/a1/manual/ams-connection-guide
title: "A1 系列 AMS 连接教程"
description: "本文介绍了 A1 系列通过料线选通器与 AMS 的连接指南"
tags: []
created: 2025-09-25T03:20:15.508Z
updated: 2026-05-21T10:07:24.528Z
source: https://wiki.bambulab.com/zh/a1/manual/ams-connection-guide
---

本指南涵盖了 A1 系列打印机与 AMS 的连接步骤以及 A1 系列料线选通器功能的详细说明。

> **注意：** 请将打印机升级至 01.07.00.00 及以上版本。

## 所需的工具和材料

- A1 系列料线选通器 （需额外购买）
- 料线选通器支架打印件（模型链接见 [步骤二：组装支架](https://wiki.bambulab.com/zh/a1/manual/ams-connection-guide#%E6%AD%A5%E9%AA%A4%E4%BA%8C%E7%BB%84%E8%A3%85%E6%94%AF%E6%9E%B6)）

- AMS/AMS 2 Pro/AMS HT

- 4-pin、6-pin 线缆
- 料管

## 为什么需要用到料线选通器？

A1 系列打印机此前适配的是 AMS lite，在使用 AMS lite 进行打印时，其本身不参与耗材助力功能，仅依靠打印机挤出机主动拉取耗材完成供料，因此无需使用料线选通器。

为适配在打印过程中具备助力功能的 AMS、AMS 2 Pro 及 AMS HT，我们专为 A1 系列推出了这款料线选通器配件。由于 AMS 在打印过程中会有内部助力电机参与推送耗材，该料线选通器的作用正是调节由此产生的材料张力，将其稳定在合适范围，确保挤出机能精准顺畅地工作。

![ams_hub.png](https://wiki.bambulab.com/a1/ams-connection-guide/ams_hub.png)

该料线选通器最多可同时连接 4 台 AMS 设备，**支持 AMS/AMS 2 Pro/AMS HT 之间任意组合，但不支持 AMS lite 与 AMS/AMS 2 Pro/AMS HT 混合使用。**

> **注意：** 请勿使用 AMS 自带的缓冲器或 AMS Hub 连接 A1 系列打印机至 AMS，否则会导致缓冲器使用功能异常或损坏，在此种情况下，该缓冲器或 AMS Hub 将不予保修。因此，请您根据本指南指引使用 **A1 专用的料线选通器**连接 AMS。

## 视频指南

## 连接教程

**本教程以 A1 mini 为例，A1 打印机的连接方法与其一致。**

### 步骤一：断开 AMS lite

- 关闭电源；

![image_-_2025-09-26t121255.538.png](https://wiki.bambulab.com/a1/ams-connection-guide/image_-_2025-09-26t121255.538.png)

- 断开 AMS lite 的 4-pin 线；

![image_-_2025-09-26t121258.846.png](https://wiki.bambulab.com/a1/ams-connection-guide/image_-_2025-09-26t121258.846.png)

- 断开五通处的四根料管。

|  |  |
| --- | --- |
|  |  |

### 步骤二：组装支架

**请下载料线选通器支架模型并完成打印。**

- **A1：** [A1 料线选通器支架](https://makerworld.com.cn/zh/models/1659360-a1-xi-lie-liao-xian-xuan-tong-qi-zhi-jia#profileId-1821367)
- **A1 mini：** [A1 mini 料线选通器支架](https://makerworld.com.cn/zh/models/1659360-a1-xi-lie-liao-xian-xuan-tong-qi-zhi-jia#profileId-1821371)

支架打印件分为三部分：L 形支架、轴套连接件和旋钮（从左至右）。

![image_-_2025-12-16t100936.643.png](https://wiki.bambulab.com/a1/ams-connection-guide/image_-_2025-12-16t100936.643.png)

- 将旋钮卡入 L 形支架的孔洞中；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-5.png)

- 将轴套连接件的凸起与圆环对准 L 形支架的孔洞进行安装；

|  |  |
| --- | --- |
|  |  |

- 用力将两部分零件按紧，完成组装；

![image_-_2025-10-10t224912.538.png](https://wiki.bambulab.com/a1/ams-connection-guide/image_-_2025-10-10t224912.538.png)

- 组装完成后，连接件与 L 形支架之间存在小角度活动空间。

![active.png](https://wiki.bambulab.com/a1/ams-connection-guide/active.png)

### 步骤三：安装支架和料线选通器

- 将组装好的料线选通器支架安装到 X 轴电机盒上；

|  |  |
| --- | --- |
|  |  |

- 从料线选通器包装中取出料线选通器、4-pin 线缆和料管；

![image_-_2025-10-14t095428.398.png](https://wiki.bambulab.com/image_-_2025-10-14t095428.398.png)

> **注意**：长料管（约 600mm）用于 A1，短料管（约 520mm）用于 A1 mini；  
> ![20250929-102225.jpg](https://wiki.bambulab.com/a1/ams-connection-guide/20250929-102225.jpg)

- 将料线选通器出口朝上，侧面凸起部分沿支架的凹槽向下滑动并扣合；

|  |  |
| --- | --- |
|  |  |

- 开启打印机。

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-16.png)

### 步骤四：切换 AMS 类型

- 在屏幕上点击 **设置 > AMS 选项 > AMS 类型**，选择需要切换的 AMS 类型；

![20250928-150712.jpg](https://wiki.bambulab.com/a1/ams-connection-guide/20250928-150712.jpg)

或在 Bambu Studio 中进入**设备**页面，点击 **AMS 设置**按钮，切换 AMS 类型；

![2025-10-09_21_46_47.png](https://wiki.bambulab.com/a1/ams-connection-guide/2025-10-09_21_46_47.png)

- 确认后，设备将切换至相应的 AMS 类型。

|  |  |
| --- | --- |
|  |  |

> **注意：**
>
> - A1 系列**不支持 AMS lite 与 AMS/AMS 2 Pro/AMS HT 混合使用**，跨类型切换 AMS 时，**需先断开原设备**，否则易引发报错；
> - 具体操作建议遵循：**拔掉原AMS → 切换AMS类型 → 连接对应AMS**，确保设备连接顺畅；
> - 若先连接设备再切换类型，可能导致通信丢失、报错，此时需**重新插拔 AMS 连接线**。

### 步骤五：连接单台 AMS

- 使用一根料管连接 AMS 和料线选通器；

|  |  |
| --- | --- |
|  |  |

- 使用另一根料管连接料线选通器和工具头上方的五通；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-20.png)

- 用集线器固定线缆和料管；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-21.png)

- 使用 4-pin 线连接打印机和料线选通器；

|  |  |
| --- | --- |
|  |  |

- 使用 6-pin 线连接料线选通器和 AMS。

|  |  |
| --- | --- |
|  |  |

### 步骤六：连接多台 AMS

- 使用 6-pin 线连接第二台 AMS 和第一台 AMS；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-28.png)

- 使用料管连接第二台 AMS 和料线选通器；

|  |  |
| --- | --- |
|  |  |

- 按照同样的方法连接其余 AMS，最多可连接 4 台；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-32.png)

> **注意**：为避免耗材拖拽，请确保料管没有过度弯曲；同时，也需整理好线缆，以确保打印过程顺畅。

- 四台 AMS 均连接完成后，放入耗材。

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-33.png)

- A1 连接示意图如下：

![a1_ams.png](https://wiki.bambulab.com/a1/ams-connection-guide/a1_ams.png)

> **注意**：当需要从 AMS/AMS 2 Pro/AMS HT 切换至 AMS lite 时，需先断开现有线缆和料管，再连接 AMS lite；**不可通过料管拓展口将 AMS lite 与工具头五通/料线选通器相连**，一旦出现 AMS lite 与其他 AMS 混接的情况，将导致进料失败。
>
> |  |  |
> | --- | --- |
> |  |  |

### 步骤七：进料和烘干

- 在屏幕上进入耗材页面，选择需要进料的耗材，点击**进料**；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-38.png)

- 进料完成；

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-40.png)

- 如需烘干耗材，则需要将电源适配器插入需要烘干的 AMS 中；否则，屏幕会显示功率不足；

> **注意**：如果想使用 AMS HT 进行烘干，则需插入电源线。

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-41.png)

- 在屏幕上进入耗材页面，选择需要烘干的 AMS，点击**烘干 > 开始**；

|  |  |
| --- | --- |
|  |  |

- 根据屏幕提示，将耗材收纳到料盘；

|  |  |
| --- | --- |
|  |  |

- 开始烘干。

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-45.png)

## AMS ID 分配

当打印机连接 AMS/AMS 2 Pro/AMS HT 时，每台 AMS 都会被自动分配唯一的 ID 并显示在打印机屏幕上，方便用户直观识别各设备间的连接关系。  
![20251011-181435.jpg](https://wiki.bambulab.com/a1/ams-connection-guide/20251011-181435.jpg)

### 操作步骤

- 确保打印机为**开机**状态；
- 将各 AMS **逐一连接**，例如先连第一台 AMS 到料线选通器，再连第二台 AMS 到第一台 AMS，以此类推。

### 分配逻辑

**AMS/AMS 2 Pro 排序**：

- 直接连接到料线选通器的 AMS，默认分配 ID 为 AMS-A；
- 连接到 AMS-A 的 AMS，分配 ID 为 AMS-B；
- 后续依次连接的 AMS，按 “AMS-C、AMS-D” 的顺序类推。

**AMS HT 排序**：

- 等 AMS/AMS 2 Pro 完成 ID 分配后，打印机才会对 AMS HT 进行排序；
- AMS HT 的 ID 默认从 “HT-A” 开始，后续依次按 “HT-B、HT-C……” 的顺序分配。

### 如何重置 AMS ID

1. 在屏幕上点击**设置 > AMS 选项 > 重新排序 AMS**，已连接的 AMS 的 ID 将被重置；

|  |  |
| --- | --- |
|  |  |

2. 待所有 AMS 的槽位都闪红灯后，断开所有线缆，按照所需顺序重新连接；

![pixpin_2026-05-19_11-28-07.webp](https://wiki.bambulab.com/a1/ams-connection-guide/pixpin_2026-05-19_11-28-07.webp)

3. 在屏幕上进入**耗材**页面，或在 Bambu Studio 中进入**设备**页面，检查 AMS ID 顺序是否完成更新。

![](https://wiki.bambulab.com/a1/ams-connection-guide/image-47.png)

## FAQs

#### Q：A1 系列能否同时连接 AMS lite 和 AMS/AMS 2 Pro/AMS HT?

通过料线选通器，A1 支持 AMS/AMS 2 Pro/AMS HT 之间任意组合使用，但不支持 AMS lite 与 AMS/AMS 2 Pro/AMS HT 混合使用。

#### Q：后续是否会支持 AMS lite 和 AMS/AMS 2 Pro/AMS HT 同时连接使用？

目前暂无计划。

#### Q：A1 系列能否同时连接 AMS 和外挂料盘？

不支持。

#### Q：能否使用料管拓展口连接 AMS lite？

不可以，当 A1 系列连接 AMS lite 或 AMS/AMS 2 Pro/AMS HT 时，料管只能直连工具头上方的五通，不可通过料管拓展口再转接。

#### Q：X1 和 P1 系列缓冲器是否可以用于 A1 系列连接AMS？

不可以，X1 和 P1 系列缓冲器并不是专为 A1 打印机设计，可能会导致通讯异常或缓冲器损坏。

#### Q：使用料线选通器时，A1 系列打印机最多可同时连接多少台 AMS？

最多可同时连接 4 台 AMS 设备，支持 AMS/AMS 2 Pro/AMS HT 之间的任意组合。

#### Q：A1 系列连接 AMS/AMS 2 Pro/AMS HT 时，6-pin 线能否共用？

A1 系列打印机连接 AMS 2 Pro/AMS HT 使用时，需搭配设备随附的 6-pin 线。若将一代 AMS 的 6-pin 线用于 AMS 2 Pro/AMS HT，可能会出现通信不良的问题；二代 AMS 的 6-pin 线可用于一代 AMS。

#### Q：A1 系列是否可以使用 AMS 2 Pro/AMS HT 进行烘干？

可以，但如果需要使用烘干功能，AMS 2 Pro 需要连接电源适配器，AMS HT 需要连接电源线，打印机本身提供的电力不足以支持烘干功能。

#### Q：A1 系列是否支持边烘边打？

暂时不支持打印过程中参与打印任务的 AMS 2 Pro/HT 进行烘干，包括本次打印有可能会用到的 AMS（即存在自动续料关系的 AMS）。

目前仅支持多台 AMS 连接至打印机时，打印过程中参与进料任务的 AMS 2 Pro/HT 或外挂料盘进行打印，与此同时，本次打印过程中不参与进料任务的 AMS 2 Pro/HT 可以开启烘干。

如果打印机正在进料或者打印，且同时通过打印机供电给 1 台 AMS 2 Pro 进行烘干，为了优先确保打印功率，烘干功率自动会降低，所以建议外接电源适配器以获得更好的烘干效果。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！
>
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
