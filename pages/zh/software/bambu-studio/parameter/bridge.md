---
path: zh/software/bambu-studio/parameter/bridge
title: "桥接设置"
description: ""
tags: []
created: 2023-12-15T11:21:17.538Z
updated: 2026-05-06T02:24:07.888Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/parameter/bridge
---

## 桥接表面质量优化

![bridge_optimizationbnail_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/bridge_optimizationbnail_zh.png)

## 概述

打印桥接结构时，耗材在没有下层支撑的情况下于空中挤出。与普通层不同，耗材不会被压平在表面上，而是保持更圆润的形状。这可能导致相邻桥接线之间出现间隙，从而影响表面质量。

> ℹ️ **注意**：我们的用户 [Make Wonderful Things on MakerWorld](https://makerworld.com.cn/zh/models/1700384-wu-zhi-cheng-qiao-jie-shi-yan?from=search#profileId-1871097) 进行了大量实验，本页面基于他的测试和结果编写，感谢他的贡献，让每个人都能实现近乎完美的桥接效果。

**首先，什么是桥接？**  
桥接是 3D 打印模型中耗材跨越开放间隙、下方无支撑的部分。材料在空气中挤出，必须在两个支撑区域之间延伸。

![bridge_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/bridge/bridge_wiki.jpg)

  

## 桥接线的问题

在桥接过程中，耗材缺乏支撑，保持圆形横截面而非扁平状。使用默认桥接流量值时，每条桥接线的直径可能小于线间距。

- 相邻桥接线可能不接触
- 线间可能出现间隙

![bridges_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/bridge/bridges_wiki.jpg)

由于重力会向下拉扯层，桥接表面可能看起来粗糙且下垂。

![gravity_pulling_the_bridge_down_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/bridge/gravity_pulling_the_bridge_down_wiki.jpg)

让我们探讨如何平衡 Bambu Studio 设置来解决这个问题。

  

## 桥接流量

首先，需要注意为什么桥接层不像常规表面那样完美粘合。  
在标准打印中，相邻线略有重叠，这种重叠有助于线融合在一起。

![horizontal_layer_bonding_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/horizontal_layer_bonding_wiki_zh.png)

增加桥接流量会为每条桥接线添加更多材料，使相邻线能够充分扩展以接触并粘合在一起。

![bridge_flow_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/bridge_flow_wiki_zh.png)

  

**精心平衡的流量有助于：**

- 桥接线之间更好的附着力
- 减少间隙
- 更光滑的桥接表面

![perfect_bridge_.jpg](https://wiki.bambulab.com/software/bambu-studio/bridge/perfect_bridge_.jpg)

> ℹ️ **注意**：由于流量增加，可能需要调整桥接速度。

> **设置位置：**
>
> ![where_to_find_bridge_flow_bambu_studio_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/where_to_find_bridge_flow_bambu_studio_wiki_zh.png)

## 桥接速度

降低桥接速度可以让耗材在打印下一条线之前有更多时间冷却和稳定，尽管速度越慢并不总是越好。必须针对每台机器和耗材仔细评估桥接速度。

> **设置位置：**  
> ⚠️ 请注意所选喷嘴。速度变化仅适用于当前选定的喷嘴。  
> ![where_to_find_bridge_speed_bambu_studio_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/where_to_find_bridge_speed_bambu_studio_wiki_zh.png)

**正确的桥接速度有助于：**

- 减少下垂
- 桥接线之间更好的附着力
- 保持更一致的桥接形状

|  |  |
| --- | --- |
| **桥接速度 - 10 mm/s** | **桥接速度 - 40 mm/s** |
|  |  |

  

## 厚桥接

厚桥接增加了桥接线的挤出宽度，适用于长跨度桥接。

**厚桥，也就是挤出和喷嘴直径相等的桥接线条。** 例如，使用0.4mm喷嘴，挤出0.4mm直径粗的桥接，就是厚桥。该参数仅适用于外部桥接，模型内部的桥接（例如内部稀疏填充上层的桥接）始终都是开启了厚桥。

未开启厚桥时，桥接和悬空墙的走线会按照原本走线的层高和线宽来计算挤出流量。如果原本的走线是 0.2mm 层高，0.4mm 线宽，当它是悬空墙或者桥接时，则是按照该层高和线宽的流量来计算桥接流量的。

以下是0.4mm喷嘴切片不同桥接的预览示例：

1. 内部桥接，始终都是厚桥，预览层高和喷嘴直径相同；

|  |  |
| --- | --- |
|  |  |

2. 外部桥接，未开启厚桥。预览层高依然和设置的层高相同，说明此时桥接是按照原本走线的层高和线宽计算的流量来挤出的。此时，如果原始层高较小的话，挤出的桥接有可能因为材料不足被拉断。

|  |  |
| --- | --- |
|  |  |

3. 外部桥接，开启厚桥，预览层高和喷嘴直径相同，说明此时挤出的桥接就是和喷嘴直径一样粗的圆柱；

|  |  |
| --- | --- |
|  |  |

所有在没开启厚桥的情况下，外部桥接就是按照层高线宽压扁的状态计算挤出流量的。开启了厚桥后，就按照喷嘴直径粗的圆柱计算桥接流量并挤出。

综上所述，我们还可以得出以下结论：

- **如果启用厚桥，桥接会更结实，可以桥接更长的距离，但可能会下坠。**

|  |
| --- |
| 桥接下坠 |

- **如果关闭厚桥，桥接看起来细，但只适用于较短的桥接距离。而且如果原本设置的层高较低的话，桥接流量可能太少会导致桥接被拉断。**

|  |
| --- |
| 桥接被拉断 |

> **设置位置：**
>
> ![softwarebambu-studiobridgewhere_to_find_thick_bridges_bambu_studio_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/softwarebambu-studiobridgewhere_to_find_thick_bridges_bambu_studio_wiki_zh.png)

  

## 桥接方向

桥接方向**控制桥接线跨越间隙的方向**。

所选方向决定了耗材如何跨越无支撑区域。

- 较短的桥接跨度通常更稳定，下垂更少
- 较长的跨度更难干净地打印

> **设置位置：**
>
> ![where_to_find_bridge_direction_bambu_studio_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/where_to_find_bridge_direction_bambu_studio_wiki_zh.png)  
> 通过减少无支撑距离，更改桥接方向可以提高桥接质量。最佳方向取决于模型几何形状和开口形状。

|  |  |
| --- | --- |
| **桥接方向 90°** | **桥接方向 0°** |
|  |  |

  

## 实用建议

  

### 优化桥接流量

> ⚠️ **注意**：盲目调整桥接流量很少能改善桥接质量。桥接性能取决于多个切片参数和所用耗材。请始终使用与计划用于打印的相同耗材和工艺设置进行测试。

首先打开 [Make Wonderful Things on MakerWorld](https://makerworld.com.cn/zh/models/1700384-wu-zhi-cheng-qiao-jie-shi-yan?from=search#profileId-1871097) 的测试模型 **(1)**。

![makerworld_open_project_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/makerworld_open_project_wiki_zh.png)

确保选择了您的**机器 (2)** 和**耗材 (3)**。  
对于此测试，我们只需要板 1 来调整**桥接流量 (4)**，板 2 来调整**桥接速度 (5)**。

![bambu_studio_project_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/bambu_studio_project_wiki_zh.png)

建议打印所有测试对象，但如切片结果 (1) 所示，这需要更多时间和耗材。

在对象选项卡 (2) 中，您可以选择要打印的测试方块。

![deselect_a_few_tests_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/deselect_a_few_tests_wiki_zh.png)

您可以打印整个构建板，或者只打印桥接流量值在 1.4 到 1.7 之间的测试，因为这些是 PLA 等材料最常见的值。

**未选中的对象不会被打印，节省时间和材料**

准备就绪后，点击**打印板 (1)**。

![ready_to_print_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/ready_to_print_wiki_zh.png)

打印后，检查每个测试。选择产生最光滑桥接表面和最佳整体质量的**桥接流量 (BF)** 值。

在这种情况下，1.5 和 1.6 的桥接流量效果最佳，因此我们将对两者进行速度优化，以获得最佳结果。

![bridge_flow_samples_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/bridge_flow_samples_wiki_zh.png)

  

### 优化桥接速度

优化桥接流量后，调整桥接速度也很重要。较高的桥接流量会挤出更多耗材，需要更多时间冷却。

> ℹ️ **注意**：降低桥接速度可以让每条桥接线在挤出过程中有更多时间冷却和稳定。这可以提高表面质量并减少下垂。但是，较慢的速度并不总是产生更好的结果。**最佳值取决于耗材和整体工艺设置。**

Bambu Studio 项目有 3 个测试行，每行有不同的桥接流量：1.4、1.5 和 1.6。  
如果您点击**对象选项卡 (1)** 并**选择一个方块 (2)**，在质量选项卡下找到**桥接流量 (3)** 并设置您从之前测试中获得的所需值，即可更改每个方块的桥接流量。

![edit_bridge_flow_of_a_specific_item_wiki_zh2.png](https://wiki.bambulab.com/software/bambu-studio/bridge/edit_bridge_flow_of_a_specific_item_wiki_zh2.png)

对于每个**测试方块 (4)**，在速度选项卡下找到**桥接 (5)**，也可以进行同样的速度调整。此项目使用 10 到 50 mm/s 的范围，**您可能需要更改这些值以获得良好结果。实验是关键。**

![bridge_speed_per_item_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/bridge_speed_per_item_wiki_zh.png)

打印后，检查样品。在此示例中，**1.5 流量在 [30 - 40] mm/s** 和**1.6 流量在 [10 - 20] mm/s** 都看起来不错。

![bridge_speed_optimization_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/bridge_speed_optimization_wiki_zh.png)

**如何选择？**  
这是打印质量和速度之间的平衡。在此示例中，桥接流量为 1.5 且速度为 40 mm/s 与流量为 1.6 且速度为 10 mm/s 之间没有明显差异。因此，优先选择 1.5 流量和 40 mm/s 速度，以实现更短的打印时间。

![15-at-40-mms_wiki.jpg](https://wiki.bambulab.com/software/bambu-studio/bridge/15-at-40-mms_wiki.jpg)

  

#### 保存打印配置

完成所有测试并获得所需结果后，我们需要保存打印工艺以备将来使用。

**1.** 确保选择了您的**机器**。  
**2.** 选择**耗材**。  
**3.** 选择用于测试的**打印工艺**。  
**4.** 在质量选项卡下，输入**桥接流量**值。  
**5.** 在速度选项卡下，输入**桥接速度**值。  
**6.** 点击保存图标。  
**7.** 重命名您的新打印工艺以便将来参考。  
**8.** 点击**确定**完成。

![save_print_process_wiki_zh.png](https://wiki.bambulab.com/software/bambu-studio/bridge/save_print_process_wiki_zh.png)

  

## 已知限制

- 超过一定长度的非常长的桥接仍然会下垂
- 结果取决于耗材类型和冷却性能
- 结果可能因模型几何形状而异

  

## **结束语**

> 希望我们提供的详细指南对您有所帮助且内容丰富。
>
> 如果本指南无法解决您的问题，请提交 [技术工单](https://bambulab.com/zh/my/support/tickets/create?from=5)。我们将回答您的问题并提供帮助。
>
> 如果您对本 Wiki 有任何建议或反馈，请在评论区留言。感谢您的支持和关注！
