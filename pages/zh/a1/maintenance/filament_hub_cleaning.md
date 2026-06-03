---
path: zh/a1/maintenance/filament_hub_cleaning
title: "A1 系列五通组件拆解与清理"
description: "本文介绍了如何清理 AMS lite 五通组件内的异物和废料，以及如何拆解与检查进料霍尔板底座。"
tags: ["五通组件", "a1", "ams lite"]
created: 2023-12-21T14:57:47.738Z
updated: 2026-05-25T09:03:28.662Z
source: https://wiki.bambulab.com/zh/a1/maintenance/filament_hub_cleaning
---

## AMS lite 五通组件 与 进料霍尔板底座

**AMS lite 五通组件**：安装在 A1 系列打印机挤出机上方，是实现多耗材打印的重要部件，它一端连接 4 根铁氟龙管，另一端连接至挤出机顶部以输送耗材。

**进料霍尔板底座**：用于安装与固定进料霍尔板，同时也用于固定 AMS lite 五通组件。

![a1_hub_base.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/a1_hub_base.png)

## 何时使用

若出现以下某一种情况，可参考本篇指南的步骤进行清洁检查。

1. **手动进料时受阻，感觉五通组件内部有异物卡住;**
2. 或 **使用 AMS 进料时**观察到耗材已送入五通，却**报错"耗材送往挤出机失败"**，同时挤出机的霍尔开关无法检测到耗材，即**屏幕"耗材"页工具头图标无绿点**;
3. 或 **未插入耗材时** 屏幕"耗材"页工具头图标的绿点持续亮起。

这些情况通常表明五通内部存在耗材碎屑，造成堵塞，需要进行拆解检查。

|  |  |
| --- | --- |
| 绿点不亮 | 绿点持续亮起 |

---

💡 **注意：** **拆解前，请确保铁氟龙管中的耗材位置在五通外。**

|  |  |
| --- | --- |
| ❌ 多个耗材同时插入五通 | ✔️ 耗材位置在五通外 |

**如果有多个耗材同时插入五通，请先根据下方指引进行操作：**

1. 将所有耗材退出到五通组件以外，然后重启打印机。
2. 在打印机屏幕的 **“AMS”** 界面，选中需要使用的耗材，点击 **“进料”** 按钮，查看是否能够顺利进料。

- **如果能够顺利进料，** 则表明五通内部没有堵塞，无须进行本篇指南的拆解检查。
- **如果无法顺利进料，** **建议参考本篇指南的步骤**对五通组件与进料霍尔板底座进行清洁与检查。

|  |  |
| --- | --- |
|  |  |

## 视频教程

  

## 所需工具和材料

- H1.5 & H2.0 内六角扳手
- 平头镊子

## 操作指引

### 拆解与清理五通组件

#### 步骤 1. 移除五通组件

使用镊子按压黑色部分，拔出料管。

![image1.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/image1.png)

用扳手或镊子轻微撬起五通的盖子，将五通组件取下。

![pry.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/pry.png)

> ⚠️ **注意**：
>
> - 进料霍尔板底座处涂布有**阻尼脂**，可能**会有些粘手**，请在操作时小心。
> - 取下五通组件后，请注意不要损坏底部含有**磁铁**的结构，该磁铁与进料霍尔板协同工作，如若丢失将影响工具头进料检测功能。  
>   ![magnet_position_1.jpg](https://wiki.bambulab.com/n1/troubleshooting/blockage-troubleshoot/magnet_position_1.jpg)

#### 步骤 2. 用耗材进行疏通

移除有断料的料管，然后用一段打印丝从料管接头处插入，尝试将断料从五通组件出口处通出。

![image10.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/image10.png)

#### 步骤 3. 拆解五通

如果正常状态下无法直接通出堵塞在五通内部的耗材或异物，需要对五通进行拆解。

> **注意**：为了避免拆装时，五通内的小配件弹出，建议在有铁氟龙管连接的状态下进行拆解。

如下图所示，可以使用平头镊子从侧面卡扣位置切入，解除左右两侧的卡扣锁定，松出铁氟龙管接口端盖。

![image2.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/image2.png)

#### 步骤 4. 清洁五通

将五通内部的配件倒出，对卡住的断料，从五通出口处用一段耗材反向通出即可。

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
|  |  |

### 拆解与检查进料霍尔板底座

#### 步骤 1. 拆解进料霍尔板底座

用 H2.0 内六角扳手移除进料霍尔板底座顶部的 2 颗螺丝，然后将底座取出。

![_拆解进料霍尔板底座.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/_%E6%8B%86%E8%A7%A3%E8%BF%9B%E6%96%99%E9%9C%8D%E5%B0%94%E6%9D%BF%E5%BA%95%E5%BA%A7.png)

#### 步骤 2. 移除霍尔板

用 H1.5 内六角扳手移除霍尔板上的 2 颗螺丝。  
![_移除霍尔板.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/_%E7%A7%BB%E9%99%A4%E9%9C%8D%E5%B0%94%E6%9D%BF.png)

#### 步骤 3. 检查摇臂

插入一段耗材，观察摇臂是否正常运作，取出耗材后是否会自动归位。

![摇臂检查.webp](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/%E6%91%87%E8%87%82%E6%A3%80%E6%9F%A5.webp)

#### 步骤 4. 检查出料口

检查出料口是否有磨损或缺口。

![出料的地方是否有磨损和缺口.jpg](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/%E5%87%BA%E6%96%99%E7%9A%84%E5%9C%B0%E6%96%B9%E6%98%AF%E5%90%A6%E6%9C%89%E7%A3%A8%E6%8D%9F%E5%92%8C%E7%BC%BA%E5%8F%A3.jpg)

#### 步骤 5. 检查霍尔传感器

1. 盖上霍尔板，用 H1.5 内六角扳手装回霍尔板的 2 颗螺丝。

![_霍尔板_2_颗螺丝安装.png](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/_%E9%9C%8D%E5%B0%94%E6%9D%BF_2_%E9%A2%97%E8%9E%BA%E4%B8%9D%E5%AE%89%E8%A3%85.png)

2. 将进料霍尔板底座放回，用 H2.0 内六角扳手安装底座顶部的 2 颗螺丝。若余留线缆过程，请小心将其塞入挤出仓内。

|  |  |
| --- | --- |
|  |  |

3. 开启打印机，点击屏幕上的**耗材**。

![点击屏幕耗材.jpg](https://wiki.bambulab.com/a1/maintenance/filament-hub-cleaning/%E7%82%B9%E5%87%BB%E5%B1%8F%E5%B9%95%E8%80%97%E6%9D%90.jpg)

4. 插入一段耗材后，检查挤出机图标是否出现小绿点。当霍尔传感器检测到材料时，屏幕上会显示小绿点；取出后，绿点将消失。

|  |  |
| --- | --- |
|  |  |

### 组装指南

#### 步骤 1. 组装五通组件

将五通内的配件逐一安装到位，然后将入口端盖处 3 个较长卡扣的位置对齐五通主体的左右两侧和后侧的窗口，按压安装到位，扣合好。如果料管咬合弹片脱出，请按图示位置重新安装好。

|  |  |
| --- | --- |
| image6.png | image7.png |

|  |  |
| --- | --- |
| image8.png | image9.png |

#### 步骤 2. 安装五通

将五通组件安装到底座上，对齐安装卡扣，下压五通主体，锁定五通组件。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
