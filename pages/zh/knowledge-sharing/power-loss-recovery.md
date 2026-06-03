---
path: zh/knowledge-sharing/power-loss-recovery
title: "断电续打"
description: "什么是断电续打功能，应该如何使用？让我们深入了解一下。"
tags: []
created: 2025-12-10T04:12:04.945Z
updated: 2026-02-11T08:50:06.611Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/power-loss-recovery
---

## 什么是断电续打

Bambu Lab 3D 打印机的断电续打是一套在意外停电后继续打印的系统。

虽然概念简单，但其实现依赖于运动控制器、存储系统、传感器以及热管理系统之间高度协调的配合。  
Bambu 打印机能够提前检测到电源中断，保存关键打印状态，并在重新上电后安全、有序地重建打印环境。

断电续打的主要目的，是防止长时间打印任务因为突发停电而报废，避免材料和时间的浪费。

![20251211-104119.jpg](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/20251211-104119.jpg)

## 功能预期与局限

断电续打无法做到完全无痕恢复。  
在恢复位置处几乎总会有轻微的纹理变化或小痕迹。

对于功能件来说通常可以接受，但对于高精度或外观件，这些痕迹可能更明显。

受到材料物理特性与热变化限制的影响：  
**断电续打更应视为一种“抢救”机制，而不是保证完美连续性的功能。**

  

## Bambu Lab 如何检测到断电？

当主电源电压开始下降时，电压监测电路会立即发出警告信号。主板持续监听该信号，一旦低于安全阈值，系统就会立刻启动应急保存程序。

通过硬件检测与小型电容保持供电，打印机能在断电后继续运行最后几毫秒，执行关键保存操作。

  

## 断电时系统保存哪些信息？

当检测到断电时，打印机会立即保存恢复打印所需的核心参数，包括：

- XYZ 三轴当前坐标
- 挤出机和耗材位置
- 当前 G-code 行号
- 热端和热床温度
- 封闭舱状态（如有）
- AMS 材料配置信息

  

## 断电续打流程

重新上电时，打印机会检查是否存在有效恢复文件。如有，系统会提示是否继续打印。

如果用户选择继续，打印机会执行特殊的恢复初始化流程，而不是完整开机过程。

> ℹ️ **注意：第一层打印阶段无法进行断电续打。**

![重启.gif](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/%E9%87%8D%E5%90%AF.gif)

- X/Y 轴将重新归零（通常不会撞到模型）
- Z 轴无法探测，因此打印机会依赖之前保存的 Z 值
- 恢复热端与热床至断电前的温度
- 进行短暂挤出
- 回到断电前的 G-code 行继续打印

![power_loss_in_action.gif](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/power_loss_in_action.gif)

## 材料特性与热稳定性

断电续打成功率高度依赖材料特性：

- **PETG、TPU**：冷却慢，恢复成功率高
- **PLA**：冷却快，断电期间容易从热床脱附
- **ABS、PC 等工程材料**：极度敏感，易翘曲、开裂

封闭式结构的机型可提高恢复成功率。

![h2-series-heated-chamber.jpg](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/h2-series-heated-chamber.jpg)

## 潜在问题

### 1. 翘边

热床若完全冷却，再次加热后附着力可能变化，模型可能因收缩而翘起，尤其是 ABS。

> ℹ️ **提示：使用 工程材料打印板 可减少 ABS、ASA、PA 等材料的翘曲风险。**

![curling_corner.jpg](https://wiki.bambulab.com/knowledge-sharing/printing-issues/curling_corner.jpg)

  

### 2. 模型脱离（炒面）

冷却后材料会自然收缩，即使是 PLA，也可能在长时间断电后脱离热床。

> ℹ️ **提示：使用固体胶或胶水可增强附着力。**

![model_detach2.png](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/model_detach2.png)

### 3. 小料点

断电瞬间喷嘴停在原地，会留下一个小料点。  
恢复时喷嘴可能撞到它，导致层移或把模型顶掉。

![power_loss_deffect_wiki.jpg](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/power_loss_deffect_wiki.jpg)

  

### 4. 可见恢复线

由于材料冷却速率不同，断电层会出现明显的水平线。  
ABS、ASA 较为明显，断电越久越显眼。

![power_loss_line_wiki22.jpg](https://wiki.bambulab.com/knowledge-sharing/power-loss-recovery/power_loss_line_wiki22.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
