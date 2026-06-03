---
path: zh/software/bambu-suite/manual/composability-of-different-process-types-processed-on-same-plate
title: "不同工艺对象同盘制作的可组合性"
description: ""
tags: []
created: 2025-03-25T12:55:58.625Z
updated: 2025-03-26T01:56:09.155Z
source: https://wiki.bambulab.com/zh/software/bambu-suite/manual/composability-of-different-process-types-processed-on-same-plate
---

在 [绑定和组合功能介绍](attach-and-group.md)一文中，介绍了绑定工具的作用。它可以把不同的图案绑定，使它们之间的相对位置保持不变，放到同一盘加工制作。然而该工具也无法做到完全自由组合。由于不同图案可能具有不同的加工工艺，由于硬件的限制，存在一些特定组合的工艺无法在同一盘上进行制作。

当把不支持同盘加工的对象绑定在一起的时候，软件的对象列表中将出现感叹号提示，点开之后可以查看详情。

![](https://wiki.bambulab.com/h2/manual/composability-of-different-process-types-processed-on-same-plate/image.png)

在材料支持相关的加工工艺的前提下，对于H2D 机型不同工艺对象同盘制作的可组合性如下表格所示。斜杠代表重复内容不填写。

| 工艺\工艺 | 激光线条雕刻 | 激光线条切割 | 激光图像/填充雕刻 | 基础刀切 | 线条绘画/填充绘画 | 打印后刀切 |
| --- | --- | --- | --- | --- | --- | --- |
| 激光线条雕刻 | \ | Yes使用激光垫板 | Yes 使用激光垫板 | Yes使用刀切垫板加工，且激光功率不能太大，只能表面雕刻不能切穿，否则会伤到刀切垫板 | Yes使用刀切垫板加工，且激光功率不能太大，只能表面雕刻不能切穿，否则会伤到刀切垫板 | No |
| 激光线条切割 | \ | \ | Yes 使用激光垫板 | No | No | No |
| 激光图像/填充雕刻 | \ | \ | \ | Yes 使用刀切垫板加工，且激光功率不能太大，只能表面雕刻不能切穿，否则会伤到刀切垫板 | Yes 使用刀切垫板加工，且激光功率不能太大，只能表面雕刻不能切穿，否则会伤到刀切垫板 | No |
| 基础刀切 | \ | \ | \ | \ | Yes 使用刀切垫板 | Yes 使用刀切垫板 |
| 线条绘画/填充绘画 | \ | \ | \ | \ | \ | Yes 使用刀切垫板 |
| 打印后刀切 | \ | \ | \ | \ | \ | \ |

一般来说，激光表面雕刻可以和刀切画笔等工艺同盘制作，对应的用户场景是用户在皮革等薄材料上同时使用激光在材料表面雕刻图案，雕刻完再进行刀切切割的场景。例如我们不建议使用激光切割皮革，因为有可能导致切割边缘过度碳化。
