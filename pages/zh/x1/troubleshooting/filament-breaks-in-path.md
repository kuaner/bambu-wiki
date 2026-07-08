---
path: zh/x1/troubleshooting/filament-breaks-in-path
title: "耗材断在管道中间"
description: ""
tags: []
created: 2022-08-01T04:35:14.024Z
updated: 2026-06-16T09:23:50.120Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/filament-breaks-in-path
---

## 这是什么

在 AMS 进料或回退耗材过程中，易碎的耗材可能在进料过程中断裂，断裂的耗材需要取出后才能继续。

## 何时使用

当屏幕上显示错误消息“耗材断裂在路径”时。

## 需要的工具和材料

- 尖嘴钳
- 1.5mm 内六角扳手
- 2.0mm 内六角扳手

![](https://wiki.bambulab.com/x1/troubleshooting/filament-break-in-path/tools.jpg)

## 故障排除指南

通常情况下，可能断裂的位置是：

1. AMS 内部；
2. 内部或接近工具头的位置
3. 在铁氟龙进料管弯曲较大的位置

### 情况 1：AMS 内部

##### 步骤 1

将铁氟龙进料管从 AMS 出口取出，如果耗材头部位于AMS出口，则将其拔出，将铁氟龙进料管重新装回AMS中，检查是否牢固，可以参考本视频：

#### 步骤 2

如果耗材断在 AMS 中，你可以参考本视频：

#### 步骤 3

在移除断裂的耗材后，点击打印机屏幕上的“重试”按钮以继续。

### 情况 2：在工具头内部或附近

移除工具头前盖后，用手向下按压图示的塑料夹。这样可以松开 PTFE 管，检查管内是否有残留的耗材，将它拉出。

![](https://wiki.bambulab.com/disconnect_ptfe.jpeg)

如果耗材卡在挤出机里，请参考此[Wiki](extruder-clog.md)清理它。

### 情况 3：在铁氟龙进料管弯曲较大的位置

由于 PTFE 管在进入挤出机之前会弯曲，因此较脆的耗材可能会在此处断裂。

#### 清洁方法

松开下图所示的两个螺钉，向下按压气动接头，取出料管。

![](https://wiki.bambulab.com/disconnect_ptfe.jpeg)

这样您就可以从打印机背面推/拉耗材，还可以移除可能卡在挤出机中的耗材。

如果问题仍然存在，请按照案例 3 的指导进行操作。

## 附录：耗材断在 AMS lite 内部

##### 步骤 1. 拆卸料管

按压工具头入料口接口和料盘支架上的料管接口，拔出料管。

|  |  |
| --- | --- |
|  |  |

##### 步骤 2. 取出断料

可用长耗材顶出断料。

![](https://wiki.bambulab.com/x1/troubleshooting/filament-break-in-path/用耗材顶出.jpg)

##### 步骤 3. 连接料管

重新安装料管。

|  |  |
| --- | --- |
|  |  |

## 如何验证

打印机能够正常进料，并恢复打印。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
