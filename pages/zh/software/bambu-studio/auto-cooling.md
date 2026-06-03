---
path: zh/software/bambu-studio/auto-cooling
title: "冷却模式"
description: "讲解耗材丝设置中的冷却模式参数"
tags: []
created: 2023-07-21T08:51:52.300Z
updated: 2025-12-31T03:31:50.583Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/auto-cooling
---

冷却对于 FDM 打印机的打印质量至关重要，尤其是在模型包含悬垂、桥接或尖锐等细小结构时。如果打印速度过快而冷却不足，往往会导致打印质量下降。下图展示了一些因冷却不足而产生质量问题的示例模型。

![bambustudio_冷却模式_示例.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E7%A4%BA%E4%BE%8B.png)

冷却相关的设置可以在耗材丝的设置页面里操作，如下图：

![bambustudio_冷却模式_导航.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E5%AF%BC%E8%88%AA.jpg)

这些设置用于控制冷却风扇速度并限制单层打印速度。部分参数较为复杂，可参考下文获取更详细的说明。

## 特定层冷却

### **特殊冷却设置**

该设置用于调整前 **n** 层的辅助部件冷却风扇速度。前 **n** 层可统一使用指定的辅助风扇速度，同时部件冷却风扇保持关闭。

若未启用此特殊冷却设置，则部件冷却风扇和辅助部件冷却风扇将分别按照各自的常规参数执行。

> 📌**注意**：通常情况下，为了提升首层与打印平台的附着力，首层的两种冷却风扇默认关闭，因此在默认设置中，首层的风扇速度为 0。

![bambustudio_冷却模式_特殊冷却设置.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E7%89%B9%E6%AE%8A%E5%86%B7%E5%8D%B4%E8%AE%BE%E7%BD%AE.png)

## 部件冷却风扇

### **最小/最大风扇速度阈值**

部件冷却风扇速度会根据每层的打印时间自动调整，由两个速度阈值和对应的层时间阈值控制。

例如将其设定为：

- 最小风扇速度阈值为 10%，对应层时间为 30 秒
- 最大风扇速度阈值为 80%，对应层时间为 3 秒。

对应的单层打印时间与风扇速度的关系则是：

- 当单层打印时间达到 30 秒时，风扇速度降至 10%
- 当单层打印时间不超过 3 秒时，风扇速度达到 80%。
- 若单层打印时间在 3 ~ 30 秒之间，风扇速度将根据这两个阈值进行线性插值，速度会在 10%~80%之间变化。

![bambustudio_冷却模式_风扇速度阈值.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E9%A3%8E%E6%89%87%E9%80%9F%E5%BA%A6%E9%98%88%E5%80%BC.png)

实际单层打印的风扇速度可以参考下图，大于层时间阈值后风扇会关闭：

![bambustudio_冷却模式_折线图1.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E6%8A%98%E7%BA%BF%E5%9B%BE1.png)

### **保持风扇常开**

启用此设置，部件冷却风扇将永远不会停止，并且将至少以最低转速运行，以减少启动和停止的频率，最低转速就是“**最小风扇速度阈值**”中的速度。

![bambustudio_冷却模式_保持风扇常开.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E4%BF%9D%E6%8C%81%E9%A3%8E%E6%89%87%E5%B8%B8%E5%BC%80.png)

如下图所示，风扇至少会以最小速度运行：

![bambustudio_冷却模式_折线图2.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E6%8A%98%E7%BA%BF%E5%9B%BE2.png)

### **降低打印速度以得到更好的冷却**

当风扇转速已经达到最大阈值，但单层打印时间仍短于“最大风扇速度阈值”里的层时间时，散热可能仍然不足。

为改善这种情况，可以启用“**降低打印速度以获得更好的冷却**”选项。该功能会自动降低打印速度，使单层打印时间不小于“最大风扇速度阈值”里的层时间，从而延长每层的冷却时间。这对于尖顶、小细节等需要充分冷却的部位尤其有效。

> 📌**注意**：当打印速度降低到“**最小打印速度**”后，如果单层打印时间仍未达到最小层时间阈值，打印机会维持最小打印速度，而不会继续降低。  
>   
> **如下图所示**：如果单层打印时间小于 4 秒，系统会尝试降速以保证至少 4 秒的打印时间，从而延长冷却时间。但如果打印速度降到 20 mm/s 后仍无法达到 4 秒，则会保持 20 mm/s 的速度打印，不再进一步降速。

![bambustudio_冷却模式_降低打印速度.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E9%99%8D%E4%BD%8E%E6%89%93%E5%8D%B0%E9%80%9F%E5%BA%A6.png)

左图为开启“**降低打印速度以获得更好的冷却**”；右图为关闭此选项。  
![bambustudio_冷却模式_冷却速度对比.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E5%86%B7%E5%8D%B4%E9%80%9F%E5%BA%A6%E5%AF%B9%E6%AF%94.jpg)

### 不减慢外墙速度

启用此设置后，外墙打印速度不会因为满足最小层时间而被降低，以保证外墙质量。这在以下情况下尤其有用：

- 打印光泽丝材时，避免光泽度因速度变化而出现差异。
- 保持外壁均匀，防止产生类似 Z 形条纹的轻微缺陷。
- 避免不同速度导致的外墙细微缺陷。

![bambustudio_冷却模式_不减慢外墙速度.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E4%B8%8D%E5%87%8F%E6%85%A2%E5%A4%96%E5%A2%99%E9%80%9F%E5%BA%A6.png)

左图为开启“**不减慢外墙速度**”；右图为关闭此选项。

![bambustudio_冷却模式_外墙速度对比.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E5%A4%96%E5%A2%99%E9%80%9F%E5%BA%A6%E5%AF%B9%E6%AF%94.jpg)

### 最小打印速度

“降低打印速度以得到更好的冷却”功能中所能降到的最小打印速度。

![bambustudio_冷却模式_最小打印速度.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E6%9C%80%E5%B0%8F%E6%89%93%E5%8D%B0%E9%80%9F%E5%BA%A6.png)

### 悬垂/桥接强制冷却

开启此设置后，悬垂和桥接区域的风扇转速将不再受上述层打印时间限制。当悬垂角度超过阈值时，可对悬空区域设置更高的风扇转速，以增强局部冷却效果。

> **注意**：如果没有其他特殊原因，请保持它默认启用。

![bambustudio_冷却模式_悬垂.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E6%82%AC%E5%9E%82.png)

### **冷却悬空阈值**

当打印件的悬垂程度超过该阈值时，冷却风扇将被强制提升至特定速度。该数值以百分比表示，用于描述挤出线条不受下层的支撑的部分所占挤出线宽的比例。（悬垂度的计算可以参考wiki：[悬垂降速 | Bambu Lab Wiki](slow-down-for-overhang.md)）

当设置为 0% 时，表示不论悬垂程度如何，所有外壁均会强制冷却。

![bambustudio_冷却模式_冷却悬空阈值.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E5%86%B7%E5%8D%B4%E6%82%AC%E7%A9%BA%E9%98%88%E5%80%BC.png)

### **参与冷却降速的悬垂阈值**

该参数在 Bambu Studio 1.10 版本中引入。此前版本中，悬垂走线不参与“降低打印速度以得到更好的冷却”机制计算，可能导致异常情况，例如同一条走线中，悬垂部分的打印速度反而高于非悬垂部分。

启用该参数后，超过悬垂阈值的区域将一并参与冷却降速计算，从而避免局部悬垂区域打印速度突然升高的问题。

- 该百分比表示悬垂度阈值，例如：

  - 设置为 **25%**，表示悬垂度不超过 25% 的走线将参与冷却降速
  - 设置为 **100%** 时，表示所有存在悬垂的走线均参与冷却降速。
- 降速后的最终打印速度将取**悬垂降速**与**冷却降速**计算结果中的**较小值**（即更低的打印速度）。

![bambustudio_冷却模式_参与冷却悬空阈值.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E5%8F%82%E4%B8%8E%E5%86%B7%E5%8D%B4%E6%82%AC%E7%A9%BA%E9%98%88%E5%80%BC.png)

左图为**悬垂未参与冷却降速**；右图为**悬垂参与冷却降速**。

![bambustudio_冷却模式_悬垂降速对比.jpg](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E6%82%AC%E5%9E%82%E9%99%8D%E9%80%9F%E5%AF%B9%E6%AF%94.jpg)

### **悬垂风扇速度**

当打印桥接或悬垂度超过设定阈值时，将强制部件冷却风扇在特定速度下运行。强制冷却能够使悬垂和桥接获得更好的打印质量。

![bambustudio_冷却模式_悬垂风扇速度.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E6%82%AC%E5%9E%82%E9%A3%8E%E6%89%87%E9%80%9F%E5%BA%A6.png)

### 风扇预启动时间

当即将打印悬垂结构时，由于风扇转速提升需要一定时间，可提前 **0–5 秒**启动冷却风扇，以确保悬垂区域获得及时、充分的冷却效果。

![bambustudio_冷却模式_风扇预启动时间.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E9%A3%8E%E6%89%87%E9%A2%84%E5%90%AF%E5%8A%A8%E6%97%B6%E9%97%B4.png)

## 辅助部件冷却风扇

### 风扇速度

该参数用于设置打印机侧边辅助部件冷却风扇的转速。打印过程中风扇将以固定转速运行，不会自动调节。若打印机未安装辅助部件冷却风扇，则该设置将被忽略。

![bambustudio_冷却模式_风扇速度.png](https://wiki.bambulab.com/bambu-studio/toolbar/cooling/bambustudio_%E5%86%B7%E5%8D%B4%E6%A8%A1%E5%BC%8F_%E9%A3%8E%E6%89%87%E9%80%9F%E5%BA%A6.png)
