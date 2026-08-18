---
path: zh/x2d/manual/tpu-printing-guide
title: "X2D TPU 打印指南"
description: "本文介绍了如何使用 X2D 打印 TPU 95A  HF、TPU 90A  和 TPU 85A "
tags: []
created: 2026-04-14T13:20:30.650Z
updated: 2026-08-06T03:54:57.548Z
source: https://wiki.bambulab.com/zh/x2d/manual/tpu-printing-guide
---

## **前言**

TPU（热塑性聚氨酯）是一种柔性耗材，有弹性、能被拉伸但又能回弹。根据其软硬程度可以分为 TPU For AMS、TPU 95A HF、 TPU 90A、TPU 85A。该材料性能优异、应用广泛，不同硬度可满足多样化场景的使用需求。

其中，TPU for AMS 硬度较高，进退料要求较低，能够直接放入 AMS 中使用；而 95A 及以下硬度的耗材，其进料要求偏高，需避免因进料阻力过大而影响打印质量。

## 耗材存储

TPU 容易吸湿，受潮会影响打印质量。为了避免这种情况，建议：

- 将料盘存放在湿度低于 20% RH 的环境中；
- 使用收纳盒进行存放；
- 在收纳盒内放置干燥剂。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/002.jpg)

## 打印前准备

### 耗材烘干

TPU 具有较强的吸湿性，在自然环境中容易吸收水分。若含有水分的 TPU 直接用于 3D 打印，打印过程中水分受热会迅速汽化，从而在打印制品中形成气泡、空洞等缺陷严重影响打印质量，甚至可能导致打印失败。因此我们推荐您使用下述设备及参数进行烘干。详情请参考[耗材准备——干燥](../../filament-acc/filament/dry-filament.md)。

| 鼓风式烤箱 | 热床 | AMS HT |
| --- | --- | --- |
| 70 ℃, 8 h | 90 ℃, 16 h | 75 ℃，18 h |

烘干前，料盘外沿宽度约为 65.4 mm。在烘干过程中，TPU 受热膨胀会导致料盘变形，**因此烘干后料盘边缘宽度可能增大到约 69.4 mm**。

|  |
| --- |
| 烘干前后料盘涨大对比 |

### **主热端规格**

> 由于 X2D 右侧采用辅助挤出机设计，进料阻力较大，因此**仅支持使用主热端打印 TPU，不可使用辅助热端打印 TPU**。

若不是全新热端，请检查热端中是否有残料；若有，请升温后用 PLA / PETG [冷拔](https://wiki.bambulab.com/zh/x2d/maintenance/cold-pull-maintenance-hotend#cold-pull-x2d) 2 - 3 次，**切忌使用纤维增强料线冷拔**，请参考 [X2D 堵塞排查指南](../troubleshooting/clogging.md)。

| 耗材类型 | 0.2 喷嘴普通热端 | 0.4 喷嘴普通热端 | 0.6 喷嘴普通热端 | 0.8 喷嘴普通热端 | 任意尺寸大流量热端 |
| --- | --- | --- | --- | --- | --- |
| TPU 85A | × | × | √ | √ | × |
| TPU 90A | × | √ | √ | √ | × |
| TPU 95A HF | × | √ | √ | √ | √ |
| TPU for AMS | × | √ | √ | √ | √ |

### **挤出机**

- 检查并保养挤出机，如有异物，请拆卸后清洁；若进料齿轮有磨损，则需要更换，否则可能会出现料线打滑的情况。
- 检查切刀刀片是否磨损，磨损后会影响 TPU 的切料，使得打印失败率提升。建议定期检查切刀刀片的磨损状态，并根据教程进行更换，请参考：[X2D 切料组件更换指南](../maintenance/replace-filament-cutter.md)。

### **打印板**

- PEI 纹理打印板涂胶后可能会出现 TPU 过于粘附的现象，因此在使用纹理板打印时不建议涂胶。
- 其他类型的打印板则需要涂胶，防止模型首层质量不佳、粘附不牢甚至导致打印失败的情况。

| TPU 类型 | 低温打印板 | 工程材料打印板 | 光面 PEI 打印板/高温打印板 | 纹理 PEI 打印板 | 是否涂胶 |
| --- | --- | --- | --- | --- | --- |
| TPU 85A/90A/95A HF/TPU for AMS | 不适配 | 推荐 | 推荐 | 推荐 | 是（除 PEI 纹理板外） |

## 视频教程

## TPU 95A HF（使用外挂料盘）

> 建议使用外挂料盘打印 TPU 95A HF。

### 进料步骤

1. X2D 外挂料盘底座默认为左侧安装，需将其移至右侧；  
   ![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/017.png)
2. 将料盘支架从料盘轴上拆下，插入另一侧；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/005.webp)

3. 将支架插入背板上的底座，听到“咔哒”一声，即为插入到位；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/014.webp)

> 注意：请勿将支架装反。  
> ![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/018.png)

4. 截取一段 175mm 左右的料管连接外挂料盘支架和主挤出机进料口；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/029-.png)

5. 放置料盘；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/001.jpg)

6. 捏住耗材端部，手动往料管内送料；

|  |  |
| --- | --- |
|  |  |

7. 在屏幕上点击“进料”按钮；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/031-.png)

8. 观察喷嘴挤出，耗材均匀流畅挤出即为进料完成。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/007.webp)

### 退料步骤

1. 在屏幕点击“退料”按钮；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/032-.png)

2. 当弹出提示“请将左挤出机外挂料盘的耗材拉出”时，手动将耗材从支架上取出。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/033-.png)

## **TPU 90A/85A**

打印 TPU 90A 或 85A 时，可使用置顶支架或 TPU 进料助力模块进行打印。

### 置顶支架

#### **进料步骤**

> 请提前打印置顶支架并安装；X2D 与 P2S 机型尺寸一致，可在 MakerWorld 下载相关模型。推荐模型：[P2S/P1S 顶部料卷支架 TPU](https://makerworld.com.cn/zh/models/1883209-p2s-p1s-ding-bu-liao-juan-zhi-jia-tpu#profileId-2173759)  
> ![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/034.png)

1. 打开工具头前盖，断开主热端处料管；

|  |  |
| --- | --- |
|  |  |

2. 将料管从卡扣中抽出，放在打印机后方；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/012.webp)

3. 安装 TPU 置顶支架，并放置耗材；

|  |  |
| --- | --- |
|  |  |

4. 点击屏幕，将主热端温度设置为 250 ℃；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/039-.png)

5. 热端升温后，直接将耗材插入挤出机中，**缓慢点击进料按钮（下箭头）**，直到耗材均匀流畅挤出，即完成进料。

> 注意：**请勿连续点击**，以免 TPU 卷入挤出机齿轮造成堵塞。

|  |  |
| --- | --- |
|  |  |

#### 退料步骤

1. 点击屏幕，将主热端温度设置为 250 ℃；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/038.png)

2. 捏住耗材，缓慢点击挤出机退料按钮（上箭头），随齿轮回转，轻轻拉出耗材；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/008.webp)

3. 将主喷嘴料管沿拖链卡扣装回，并插入工具头进料口。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/013.webp)

### 助力模块

TPU 送料助力模块是专为柔性耗材打印设计的增强组件。该模块支持封箱打印 TPU，可通过 TPU 专用进料口直接进料，简化进料流程；同时能降低 TPU 耗材在不同摆放场景下的进料阻力，有效解决柔性耗材进料卡顿、断料问题，显著提升 TPU 打印的稳定性与成功率。关于使用 TPU 助力模块的详细说明请参考：[TPU 送料助力模块组装 & 使用指南](../../general/manual/tpu-feed-assist-module.md)。

![018.png](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/027.png)

## **打印参数**

> 注：除预设参数外，具体参数设定应当随模型的特点进行调整。

1. TPU 85A & 90A 推荐打印温度为 225 ℃，热床温度为 30 - 35 ℃，无需开启腔温；
2. 打印时请保留默认的体积速度上限，不建议增加打印速度；
3. 动态流量校准请选择 “自动” 或者 “关闭”；
4. 模型打印时，建议模型将放置在打印板中间靠前位置（如下图）以减小耗材与铁氟龙管之间的摩擦力。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/tpu-printing-guide/place_model_cn.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
