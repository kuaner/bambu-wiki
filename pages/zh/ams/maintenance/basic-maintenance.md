---
path: zh/ams/maintenance/basic-maintenance
title: "AMS定期维护建议"
description: "关于AMS的一些日常维护和保养建议"
tags: ["ams", "ptfe管", "产品维护", "保养，维护", "干燥剂", "维护", "气动接头"]
created: 2024-09-10T11:20:53.924Z
updated: 2026-03-20T07:42:22.866Z
source: https://wiki.bambulab.com/zh/ams/maintenance/basic-maintenance
---

Bambu Lab AMS 是一个智能系统，需要进行维护，以确保稳定的进料和自动切换耗材打印。以下是一些关于定期检查和维护的建议：

## PTFE 管

PTFE管是消耗品，并且有磨损的风险，因为它们可能会随着时间耗材丝摩擦。我们建议您在维护机器时检查PTFE管是否磨损。如果料管磨损，不及时更换，这可能导致进料故障，耗材堵在AMS内等。如果需要，请参考这些关于更PTFE管的教程视频。

[AMS 中 PTFE 料管的磨损情况及维护建议 | Bambu Lab Wiki](../troubleshooting/ptfe-damage-in-AMS.md)

### PTFE 料管维护更换周期

在正常使用频率的情况下，应当**每两个月**对PTFE 料管进行更换，以确保在任何使用场景下耗材移动不受阻碍。当使用磨损性较强的耗材（如碳纤维和夜光系列耗材）进行打印时，应当**每个月**或者**料管出现明显磨损时**对PTFE 料管进行检查更换，定期进行维护可确保机器平稳运行，延长 AMS 的使用寿命。

#### AMS内部PTFE料管可能的损坏图

内部PTFE 料管损坏位置图片如下图所示。

|  |  |
| --- | --- |
|  |  |
|  |  |

#### **更换 AMS 内部的PTFE料管**

[在哔哩哔哩中观看视频。](https://www.bilibili.com/video/BV1Ue4y197ry?spm_id_from=333.999.0.0&vd_source=6b9d039fb07523b17eab38cc9702177e)

## 气动接头

当您遇到以下的情况时候，可以通过更换气动接头来解决问题：

- PTFE管无法被固定，比如PTFE管无法被固定在挤出机上；
- 耗材无法通过气动接头，比如耗材无法通过缓冲器（如下图所示的位置，一般可能是由于气动接头内部损坏所导致）；
- 气动接头损坏

![](https://wiki.bambulab.com/filament-acc/acc/replacing-the-pneumatic-connector/00-%E6%96%99%E7%BA%BF%E5%8D%A1%E5%9C%A8%E7%BC%93%E5%86%B2%E5%99%A8%E7%9A%84%E7%A4%BA%E6%84%8F.png)

[更换气动接头 | Bambu Lab Wiki](../../filament-acc/acc/replacing-the-pneumatic-connector.md)

## AMS入料口组件

当漏斗状进料口严重磨损，上下料造成了影响，例如出现助力电机过载或其他与进退料相关的HMS报错，或经售后人员确认为上下料器电路板件故障，建议你更换该组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-feed-funnel-assay/worn_funnel_assy.jpg)

[更换AMS入料口组件 | Bambu Lab Wiki](../../x1/maintenance/replace-the-feed-funnel-assy.md)

## AMS主动支撑套筒组件

若主动支撑套筒组件出现明显的损坏（图示的3个位置），或者安装不牢固，导致上下料组件的黄色齿轮和支撑套组件的黑色齿轮咬合不畅，导致进料失败

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/install_the_driving_sleeve_units.png)

### 拆卸主动支撑套筒组件

按照如下方向拆下主动支撑套筒单元。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/remove_the_driving_sleeve_units.png)

### 安装 **AMS主动支撑套筒组件**

安装 AMS主动支撑套筒组件，注意对齐齿轮位置，防止装反。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/install_the_driving_sleeve_units.png)

## AMS干燥剂

AMS 内部有两个存放干燥剂袋的隔间，以保持内部空气干燥，从而保护您的耗材免受湿气影响。

[干燥剂状态 | Bambu Lab Wiki](../../knowledge-sharing/desiccant-status.md)

当你收到新的干燥剂后，请勿忘记拆掉外包装，拆掉外包装后，内部产品为下图图1中的左图：

![](https://wiki.bambulab.com/knowledge-sharing/pa-cf-printing-tips/desiccant-status1.jpg)

图 1   干燥剂的三种状态，从左至右，依次是新，部分受潮和完全受潮的干燥剂

**建议每两周检查一次干燥剂的状态，如果干燥剂已经失效请及时更换。如果长时间不更换干燥剂，它会失去吸水能力，从而失去对干燥过的耗材的保护能力。另外，超过 3 个月不更换时，干燥剂还可能会渗水，使AMS内部的电路或电子元件短路或损坏。**

![](https://wiki.bambulab.com/knowledge-sharing/desiccant/ganzaojibaozhuang.jpg)

图 2   带有外包装的干燥剂
