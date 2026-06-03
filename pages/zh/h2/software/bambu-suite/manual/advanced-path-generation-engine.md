---
path: zh/h2/software/bambu-suite/manual/advanced-path-generation-engine
title: "Bambu Suite 先进的加工路径生成引擎"
description: ""
tags: []
created: 2025-03-26T02:55:32.221Z
updated: 2025-07-18T12:46:00.105Z
source: https://wiki.bambulab.com/zh/h2/software/bambu-suite/manual/advanced-path-generation-engine
---

Bambu Suite更”聪明“的加工路径生成引擎，助力更高的加工精度和加工质量，其核心特性有以下几点：

## 1. 智能曲线加工

支持圆弧和贝塞尔走线路径，享受高精度顺滑体验。

- **曲线类型**：  
  ▸ **圆弧**：传统机械加工常用路径，适合规则曲线  
  ▸ **贝塞尔曲线**：计算机图形学标准曲线（通过控制点定义平滑路径），广泛用于工业设计、字体渲染等领域

Bambu Suite 配合 H2D 打印机，全流程支持圆弧和贝塞尔曲线的路径生成与加工处理。可以取得更高的加工精度和流畅性，这将减少机械振动和磨损，也更接近设计意图，并且命令存储使用的数据量更小，便于传输和存储。

- 支持圆弧贝塞尔曲线路径示意图：  
  ![group_2.png](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/group_2.png)
- 不支持圆弧和贝塞尔曲线路径示意图  
  ![group_1.png](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/group_1.png)

## 2. 高质量加工

合理的路径规划和参数设置，让你得到一个高质量的加工效果。

在加工细小图案时，通过**偏好设置-> 工艺 ->** 开启**高精度切割**后，高精度还原设计图案的路径。

![](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/image-1.png)

![group_4.png](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/group_4.png)

备注：启用高精度切割路径会将原始的圆弧和贝塞尔路径处理为小线段，建议需要加工细小图案时再开启。

## 3. 聪明的路径规划

### **扫描模式**

- **合并扫描**：

  - 路径：**偏好设置→工艺→填充模式→「合并扫描」**
  - 效果：效率优先，所有图案一起扫描。
- **逐对象扫描：**

  - 路径：**偏好设置→工艺→填充模式→「逐对象扫描」**
  - 效果：质量优先，每个图案分开扫描，不过将会花费更长的加工时间。

  ![](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/image-2.png)

|  |  |
| --- | --- |
|  |  |
| 合并扫描 | 逐个对象扫描 |

### **手写体模式**

- 路径：选择**画笔工艺→参数→绘画方向→「绘画手写方向」**
- 效果：模拟自然书写笔顺，按照手写方向进行线条绘制，如下图绘制。

![](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/image.png)

![手写体.gif](https://wiki.bambulab.com/h2/manual/%E6%89%8B%E5%86%99%E4%BD%93.gif)

## 4. 丰富的画笔玩法

执笔之手，与子同乐。

您可以使用多色画笔对单线字体和任意图案进行线条绘画，也可以使用填充来对图案进行填充绘画。

- 多色线条绘画示意图：  
  ![group_5_(1).png](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/group_5_(1).png)
- 填充绘画示意图：  
  ![img_v3_02kd_235791f6-d42c-4bdd-943a-5102e77355eg.jpg](https://wiki.bambulab.com/software/bambu-suite/manual/advanced-path-generation-engine/img_v3_02kd_235791f6-d42c-4bdd-943a-5102e77355eg.jpg)

关于更多加工参数的介绍，可以参考wiki：[Bambu Suite 加工参数介绍](processing-parameters-guide.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
