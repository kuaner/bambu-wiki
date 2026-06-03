---
path: zh/filament-acc/filament/pva-printing-guide
title: "PVA 打印指南"
description: ""
tags: []
created: 2024-02-20T08:18:56.284Z
updated: 2026-05-12T06:39:02.492Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/pva-printing-guide
---

## 打印前的干燥准备与要求

PVA ，即聚乙烯醇，是一种柔软且可生物降解的聚合物。它对水分高度敏感，非常容易从空气中吸收水分，也可溶解在液态水中。PVA 耗材在干燥状态下相对较硬，可适配 AMS、AMS lite；受潮后会变软、发粘，不再适配 AMS、AMS lite，且不建议直接使用，以免因耗材受潮而带来进料失败、拉丝、卡挤出轮、堵头等问题。

为避免这些问题和获得较高的打印质量，需在打印前将受潮的耗材烘干，且**打印过程中始终把耗材存储在关闭的 AMS 中，并用干燥剂保护，确保其中的湿度小于 20% RH**，以避免烘干的耗材过快地再次受潮。推荐使用下图中的密封容器适合储存 PVA。

> 注意：**只有**使用 **H2D** 时可以配合使用下图的密封容器进行**打印**。

![](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/%E4%BF%9D%E5%AD%98.jpg)

> 保存 PVA 时请使用吸湿性能更好的氯化钙干燥剂，硅胶干燥剂无法长期保持 PVA 的干燥。

由于 PVA 的吸水速率相比其他耗材非常的快，所以烘干后**无需等它冷却**就要立刻放入干燥环境内（干燥箱或 AMS ）。在 20% RH 的干燥环境中，PVA 耗材保持干燥时长约为 1 ~ 3 天；**在通常的 55% RH 左右的室内环境中，刚烤干的 PVA 耗材会在约 1 ~ 3 小时内受潮到会使打印质量下降的程度**，潮湿天气时会更快。

**使用鼓风型烤箱或打印机烘干 PVA 耗材的建议参数如下表:**

![table.png](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/table.png)

> 注意：使用打印机的热床烘烤时需要使用一个盒子（如原装耗材纸盒）将耗材盖住。如果需要，可查阅此篇 wiki 来获知耗材烘干、防潮的更多相关信息：[耗材准备——干燥。](dry-filament.md)

**可通过如下图方式弯折 PVA耗材，可快速判断 PVA 耗材的干燥程度**，烤干后的 PVA 手感掰弯硬度会比 PLA Basic 耗材较硬。

|  |  |
| --- | --- |
| 烤干 PVA | 放置空气 15 分钟后 PVA |
| 飞书20250604-172927.gif | 飞书20250604-172927.gif |

## 切片时的参数设置

在 Bambu Studio 中，用 PVA 打印支撑结构时推荐把 **PVA 同时作为支撑主体和支撑界面**。

具体设置方法如下：

把**支撑耗材 PVA 同时作为支撑主体和支撑界面** 。在 Bambu Studio 中的设置位置：**工艺 → 支撑 → 支撑耗材**  
| ![](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/22.jpg)

大多数打印机的默认支撑参数并不适合同时以 PVA 为支撑主体和支撑界面的情况，而需进行适当更改。这种情况下，**应尽量避免切片时使用树状支撑（局部过于瘦高、单薄），** 以免打印过程中树状支撑倒塌。为了获得较好的效果，推荐按照以下切片设置，使用**普通支撑**进行打印。

|  |  |
| --- | --- |
| **1. 速度设置** | **2. 支撑设置** |
|  | 55-3.jpg |

### 预设参数文件下载

以下是提供的分机型（X1/H2D）和分支撑主体和界面耗材的预设参数文件，打印时可使用以下 3mf 文件导入模型进行打印或对照检查对应参数（用其他型号的打印机打印时，可迁移下述的相应的工艺参数和耗材丝参数）：  
**X1C:**  
[bambu\_pva\_（pva\_支撑主体\_+\_pva\_支撑界面）\_x1c.3mf](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/bambu_pva_%EF%BC%88pva_%E6%94%AF%E6%92%91%E4%B8%BB%E4%BD%93_+_pva_%E6%94%AF%E6%92%91%E7%95%8C%E9%9D%A2%EF%BC%89_x1c.3mf)  
[bambu\_pva\_（pla\_支撑主体\_+\_pva\_支撑界面）\_x1c.3mf](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/bambu_pva_%EF%BC%88pla_%E6%94%AF%E6%92%91%E4%B8%BB%E4%BD%93_+_pva_%E6%94%AF%E6%92%91%E7%95%8C%E9%9D%A2%EF%BC%89-_x1c.3mf)

**H2D:**  
[bambu\_pva\_（pla\_支撑主体\_+\_pva\_支撑界面）\_h2d.3mf](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/bambu_pva_%EF%BC%88pla_%E6%94%AF%E6%92%91%E4%B8%BB%E4%BD%93_+_pva_%E6%94%AF%E6%92%91%E7%95%8C%E9%9D%A2%EF%BC%89-_h2d.3mf)  
[bambu\_pva\_（pva\_支撑主体\_+\_pva\_支撑界面）*h2d*.3mf](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/bambu_pva_%EF%BC%88pva_%E6%94%AF%E6%92%91%E4%B8%BB%E4%BD%93_+_pva_%E6%94%AF%E6%92%91%E7%95%8C%E9%9D%A2%EF%BC%89_h2d_.3mf)

H2D 打印 PVA 特殊的打印建议：

> 🚫 **不支持使用 PVA 来支撑 PETG 耗材。**

## 建议的打印流程

1. 在打印过程中需始终保持 PVA 耗材的干燥，可以将其放在密封盒中打印，并确保干燥剂生效（请使用吸湿性能更好的氯化钙干燥剂），盒中的湿度小于 20% RH。  
   ![](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/%E6%B9%BF%E5%BA%A6%E8%AE%A12.png)
2. 或者使用 AMS HT 打印，就可以不使用干燥剂，但需**开启烘干模式，并关闭烘干时旋转料盘**功能，将温度设置为 80 ℃ 左右。  
   即在烘干时，AMS HT 无法使用自动进退料功能，但可作为干燥箱使用，防止材料受潮。  
   ![](https://wiki.bambulab.com/filament-acc/filament/pva-printing-guide/ht.png)
3. 建议将 AMS HT 放置在机器上方，**使用 TPU 出料口出料**，其出料口到打印机的进料口（如 H2D 应使用 TPU 进料口）间最好有料管连接，以避免材料过早的变形。

|  |  |
| --- | --- |
|  |  |

4. 进料时先尝试手动进料，检查喷嘴是否能正常挤出耗材。在确认耗材已经完全干燥且挤出温度正确设置（240℃ -250 ℃）后，如仍挤出不畅或挤出时料线不是直线向下，请冷拔喷嘴或更换新的喷嘴。

| 正常挤出示意 | 异常挤出1 | 异常挤出2 |
| --- | --- | --- |
|  |  |  |

## 打印结束后的支撑溶解

打印结束后，将模型放入水中浸泡，可以轻松溶解、去除  PVA  支撑。溶解过程可能要几个到十几个小时。**使用温水和搅拌可加速 PVA 的溶解，但如果模型主体为耐热性较低的 PLA 时，水温不宜超出 50 ℃，以免模型变形。**

|  |  |  |
| --- | --- | --- |
| **1. 浸泡前** | **2. 浸泡几小时后（部分溶解）** | **3. 浸泡完全后（随后晾干即可）** |
|  |  |  |

**因 FDM 3D 打印的大部分模型内部有较多孔隙，泡水溶解支撑时，部分模型内部可能会进水。若要降低模型内部进水的风险，可参考此篇 wiki 中的部分参数设置：**

[降低打印件漏液风险的指南](../../filament/reduce-vase-leaking-guide.md)

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
