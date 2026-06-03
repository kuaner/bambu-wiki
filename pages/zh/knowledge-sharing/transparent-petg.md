---
path: zh/knowledge-sharing/transparent-petg
title: "透明/半透明 PLA/PETG 耗材打印指南"
description: ""
tags: ["petg", "透明料"]
created: 2023-06-17T17:00:48.000Z
updated: 2026-04-01T10:14:26.868Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/transparent-petg
---

# 目的

本文指导如何使用透明、半透明 PLA/PETG 耗材切片打印出尽可能透明的模型。

# 切片打印的技巧和注意事项：

- \*\*打印前先把耗材烘干：\*\*以避免水汽使得挤出线条中存在气泡、孔洞，降低透明度。
- \*\*建议使用 0.8mm 喷嘴：\*\*较大的喷嘴尺寸可以最大限度地减少打印线条的数量，从而减少线条之间的交接线，增加模型的透光率。此外，将顶部和底部外壳层设置为 0，并使用直线排列作为填充图案以确保层方向一致且无重叠。
- \*\*使用高温设置：\*\*可以使 PLA/PETG 熔融得更充分、均匀并有较好的附着力，前提是保证耗材干燥。
- \*\*提高流量比例：\*\*适度提高流量比例是有效提高透明度的方法，它可以减少打印线条之间的空隙，增加模型的透光率。
- \*\*打印时关闭所有风扇：\*\*让挤出的线体自然冷却，避免过快冷却带来过多的温度、收缩不均。
- 打印完成后，可以适当地对模型表面进行打磨，增加透光度。

**\*请注意，在 3D 打印中实现高透明度还需要依赖于模型的几何形状。因此，即使具有最佳打印参数，也很难在具有复杂结构的模型上实现高透明度。此外，因为 PLA 是半结晶型聚合物，其中的晶粒会影响光的折射，而 PETG 是非结晶型聚合物，所以一般而言 PETG 的透明度会高于 PLA。**

# 切片参数设置（图片示例为 0.4 mm 喷嘴的参数）

### 1 关闭冷却风扇：

**PETG 设置**

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E5%85%B3%E9%97%AD%E6%89%80%E6%9C%89%E9%A3%8E%E6%89%87.png)

**PLA 设置**

PLA设置：完全关闭风扇会增加 PLA 翘曲的风险，需要根据需要和模型厚度适度降低风扇速度。

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E5%85%B3%E9%97%AD%E9%83%A8%E4%BB%B6%E5%86%B7%E5%8D%B4%E9%A3%8E%E6%89%87.png)

### 2 提高流量比例和喷嘴打印温度：

**PETG 设置**

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E4%BF%AE%E6%94%B9%E6%B5%81%E9%87%8F%E6%AF%94%E4%BE%8B%E5%92%8C%E5%96%B7%E5%98%B4%E6%B8%A9%E5%BA%A6.png)

**PLA 设置**

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E6%8F%90%E9%AB%98%E6%B5%81%E9%87%8F%E6%AF%94%E4%BE%8B%E5%92%8C%E5%96%B7%E5%98%B4%E6%B8%A9%E5%BA%A6.png)

### 3 设置层高为0.1mm，线宽为0.5mm：

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E4%BF%AE%E6%94%B9%E5%B1%82%E9%AB%98%E5%92%8C%E7%BA%BF%E5%AE%BD.png)

### 4 墙层数设为1，去掉顶壳和底壳，把填充密度设为100%，修改填充方向至0°或者90°：

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E4%BF%AE%E6%94%B9%E5%A2%99%E5%A1%AB%E5%85%85.png)

### 5 把速度全部调整为 20mm/s：

请注意，降低速度后会延长打印时间。

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E4%BF%AE%E6%94%B9%E6%89%93%E5%8D%B0%E9%80%9F%E5%BA%A6%E8%87%B320.png)

# 打印模型展示

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E6%89%93%E5%8D%B0%E9%80%8F%E6%98%8E%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)

PETG

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/pla%E5%8D%8A%E9%80%8F%E6%98%8E%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)

PLA

**PLA transparent 不同厚度下的效果展示如下（使用 0.6mm 喷嘴打印），从左往右厚度依次为 1mm，2mm，3mm：**

![](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E4%B8%8D%E5%90%8C%E5%8E%9A%E5%BA%A6%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)

**调整参数前（下图右侧）与调整参数后（下图左侧）的 PETG 打印模型效果对比：**

![调整参数前后.png](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/%E8%B0%83%E6%95%B4%E5%8F%82%E6%95%B0%E5%89%8D%E5%90%8E.png)

# 预设配置文件

下载预设 3MF 文件并替换成你想的打印模型（用其他打印机机型打印时，可迁移下述 X1C 的相应的工艺参数和耗材丝参数）：

1. X1C，0.4 mm 喷嘴：[petg\_-\_transparent\_parameters\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.4_mm_nozzle.3mf)
2. X1C，0.6 mm 喷嘴：[petg\_-\_transparent\_parameters\_-\_0.6\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.6_mm_nozzle.3mf)
3. X1C，0.8 mm 喷嘴：[petg\_-\_transparent\_parameters\_-\_0.8\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.8_mm_nozzle.3mf)
4. X1C，0.4 mm 喷嘴：[PLA\_-\_transparent\_parameters\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/knowledge-sharing/transparent-petg/pla_-_transparent_parameters_-_0.4_mm_nozzle_.3mf)

\*部分参数参考：[How To Print Glass by Rygar1432 | Download free STL model | Printables.com](https://www.printables.com/model/15310-how-to-print-glass)
