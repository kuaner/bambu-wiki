---
path: zh/software/bambu-studio/stacking-objects
title: "堆叠模型"
description: ""
tags: []
created: 2023-08-23T10:02:47.591Z
updated: 2024-05-28T10:54:10.868Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/stacking-objects
---

如果您需要将多个模型堆叠成一个整体，这篇内容将帮助您。

# 如何堆叠多个模型

1. 选中要堆叠在一起的多个对象（可以通过Ctrl + 鼠标左键逐个选中对象，或者Shift + 鼠标左键拖动，框选多个对象）
2. 右键打开菜单栏
3. 选择“组合”
   - 这样所有所被选中的对象将被组装成一个整体，每个原始对象都变成了新组合对象里的“零件”。
   - 注意：如果没有执行"组合"操作，则无法让对象在Z方向向上移动。因为单个对象必须要有一个面是贴合在打印板上的，而零件没有这个限制（零件和对象的具体区别可以参考 [拆分为对象/零件 | Bambu Lab Wiki](split-to-objects-parts.md)）
4. 将需要堆叠的零件移动到适当的位置
   - 您可以通过Alt + 鼠标左键选择零件或者在“对象”列表选择它

# 示例

![](https://wiki.bambulab.com/software/bambu-studio/stack-objects/duidieduixiang.gif)
