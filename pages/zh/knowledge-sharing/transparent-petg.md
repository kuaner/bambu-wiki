---
path: zh/knowledge-sharing/transparent-petg
title: "透明/半透明 PLA/PETG 耗材打印指南"
description: "了解如何使用透明或半透明的 PLA 和 PETG 耗材打印高透明度模型。本指南涵盖关键切片技巧、Bambu Studio 参数设置，以及预设 3MF 配置文件下载。"
tags: ["petg", "透明料"]
created: 2023-06-17T17:00:48.000Z
updated: 2026-07-27T02:30:08.722Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/transparent-petg
---

> 📌 **耗材使用注意事项**：
>
> 1. 请在**阴凉、避光、干燥**环境中存放耗材，避免阳光直射或高温环境。
> 2. 请将耗材及折断的碎屑放在**婴幼儿及宠物无法触及的地方**，避免吞咽和窒息的风险。
> 3. 已拆封耗材建议使用前按指南推荐的温度和时间进行烘干。半透明 PETG 属于**吸水性较强**的材料，使用完应立即放入含有有效干燥剂的**密封容器**内，并且在打印前按照指南中推荐的温度和时间进行**充分烘干**。
> 4. 建议在**通风良好**的区域使用打印机，或安装有效的空气过滤、外排风系统。
> 5. 本耗材**不属于**食品接触级耗材，请避免将打印成品用于存放或接触食品。

## 切片打印的技巧和注意事项

打印透明模型时，可参考以下技巧：

- **打印前先烘干耗材**：避免水汽在挤出线条中形成气泡、孔洞，从而降低透明度。
- **建议使用 0.8 mm 喷嘴**：较大的喷嘴尺寸可尽量减少打印线条数量，从而减少线条间的交接线，提高模型透光率。此外，建议将顶部和底部外壳层设为 `0`，并使用直线排列作为填充图案，以确保层方向一致且无重叠。
- **使用高温设置**：在保证耗材干燥的前提下，高温能让 PLA/PETG 熔融更充分、均匀，并具有更好的附着力。
- **提高流量比例**：适度提高流量比例可减少打印线条间的空隙，是提升透明度的有效方法。
- **打印时关闭所有风扇**：让挤出的线体自然冷却，避免冷却过快导致温度、收缩不均。
- **打磨表面**：打印完成后，可适当打磨模型表面，进一步提升透光度。

> **ℹ️ 说明：** 在 3D 打印中实现高透明度还取决于模型的几何形状，因此即使参数最佳，复杂结构的模型也很难达到高透明度。此外，`PLA` 为半结晶型聚合物，内部晶粒会影响光的折射；而 `PETG` 为非结晶型聚合物，所以一般而言，`PETG` 的透明度高于 `PLA`。

## 切片参数设置

> **ℹ️** 以下图片示例均为 `0.4 mm` 喷嘴的参数。

首先，在 **Bambu studio** 左侧栏的「**项目耗材列表**」，点击耗材右侧的 ![](https://wiki.bambulab.com/bambu-studio/filament-manager/edit.jpg) 标志 →「**编辑**」。

![filament_editing.png](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/filament_editing.png)

### 1. 关闭冷却风扇

|  |  |
| --- | --- |
|  |  |
| PETG 设置 | PLA 设置 |

> **⚠️ 注意：** 完全关闭风扇会增加 `PLA` 翘曲的风险，需根据实际需要和模型厚度适度降低风扇速度。

### 2. 提高流量比例和喷嘴打印温度

|  |  |
| --- | --- |
|  |  |
| PETG 设置 | PLA 设置 |

  

### 3. 设置层高与线宽

将层高设为 `0.1 mm`，线宽设为 `0.5 mm`。

![set_layer_height_and_line_width.png](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/set_layer_height_and_line_width.png)

  

### 4. 调整墙层数与填充

- 将墙层数设为 `1`。
- 去掉顶壳和底壳。
- 将填充密度设为 `100%`。
- 将填充方向修改至 `0°` 或 `90°`。

|  |  |
| --- | --- |
|  |  |

  

### 5. 调整打印速度

将所有速度调整为 `20 mm/s`。

> **ℹ️ 说明：** 降低速度后会延长打印时间。

![speed.png](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/speed.png)

  

## 打印模型展示

- **PETG**  
  ![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E6%89%93%E5%8D%B0%E9%80%8F%E6%98%8E%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)
- **PLA**  
  ![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/pla%E5%8D%8A%E9%80%8F%E6%98%8E%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)
- **PLA transparent 不同厚度下的效果展示如下**（使用 `0.6 mm` 喷嘴打印，从左往右厚度依次为 `1 mm`、`2 mm`、`3 mm`）：  
  ![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E4%B8%8D%E5%90%8C%E5%8E%9A%E5%BA%A6%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)
- **调整参数前（下图右侧）与调整参数后（下图左侧）的 PETG 打印模型效果对比：**  
  ![调整参数前后.png](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E8%B0%83%E6%95%B4%E5%8F%82%E6%95%B0%E5%89%8D%E5%90%8E.png)

  

## 预设配置文件

下载预设 `3MF` 文件，并替换为您想打印的模型即可。

> **ℹ️ 说明：** 使用其他机型打印时，可迁移下述 `X1C` 的相应工艺参数和耗材丝参数。

| 机型 | 喷嘴 | 下载链接 |
| --- | --- | --- |
| X1C | `0.4 mm` | [**petg\_-*transparent\_parameters*-\_0.4\_mm\_nozzle.3mf**](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.4_mm_nozzle.3mf) |
| X1C | `0.6 mm` | [**petg\_-*transparent\_parameters*-\_0.6\_mm\_nozzle.3mf**](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.6_mm_nozzle.3mf) |
| X1C | `0.8 mm` | [**petg\_-*transparent\_parameters*-\_0.8\_mm\_nozzle.3mf**](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.8_mm_nozzle.3mf) |
| X1C | `0.4 mm` | [**PLA\_-*transparent\_parameters*-\_0.4\_mm\_nozzle.3mf**](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/pla_-_transparent_parameters_-_0.4_mm_nozzle_.3mf) |

\*部分参数参考：[How To Print Glass by Rygar1432 | Download free STL model | Printables.com](https://www.printables.com/model/15310-how-to-print-glass)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
