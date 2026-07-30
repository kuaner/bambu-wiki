---
path: zh/studio-handy/multi-plate-printing
title: "Bambu Studio 多盘打印指南"
description: "介绍 Bambu Studio 中的多盘打印"
tags: ["bambu studio"]
created: 2024-09-05T09:09:59.655Z
updated: 2026-07-22T07:08:31.781Z
source: https://wiki.bambulab.com/zh/studio-handy/multi-plate-printing
---

在Bambu Studio中使用多盘打印可以将单个项目分配到多个虚拟打印盘上。每个盘都将作为独立的打印任务处理，这能有效简化大体积模型、多组件装配模型和多色模型的管理。通过这种方式，你可以更好地整理模型，针对不同组件应用差异化的打印设置，并在需要时实现部分重印。

## 何时使用

- **模型体积大，单盘无法容纳**： 你可以将模型拆分为多组零件，为每组零件分配一个独立的盘。  
  ![大体积模型拆分.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E5%A4%A7%E4%BD%93%E7%A7%AF%E6%A8%A1%E5%9E%8B%E6%8B%86%E5%88%86.png)
- **使用单喷嘴 3D 打印机进行多色或多材料打印**：你可以将部件按颜色或材料分组，分布在不同的打印盘上。相比将所有模型堆叠在同一块打印盘，这种方法能有效减少打印过程中的换色冲刷，缩短整体打印时间。  
  ![按色分盘.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%8C%89%E8%89%B2%E5%88%86%E7%9B%98.png)
- **用于管理高风险或长时间的打印任务**： 将高风险零件分散至不同的打印盘上，可有效避免因单个零件打印失败而影响整个项目的成败。此外，对于长时间的打印任务，分盘打印也有助于减少喷嘴碰撞模型的概率，从而进一步降低打印失败的风险。

## 适用机型

- 支持拓竹 H2 系列、X系列 和 P2系列 3D 打印机。
- P1S 机型同样支持，但在打印前会提示“发送所有盘”。
- A 系列机型暂不支持。

## 操作步骤

### 添加新盘

- 导入第一盘模型零件后，点击工具栏中从左数第二个按键**添加新盘**，即可添加第二盘。一次可添加多盘，最多可添加36盘。  
  ![添加新盘.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%B7%BB%E5%8A%A0%E6%96%B0%E7%9B%98.png)
- 下图展示了将模型零件分布在七个盘上的效果。  
  ![七盘拆分效果.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E4%B8%83%E7%9B%98%E6%8B%86%E5%88%86%E6%95%88%E6%9E%9C.png)

### 切片所有盘

- 模型分盘布置完成后，点击界面右上方切片单盘左侧的**箭头**，然后选择**切片所有盘**。  
  ![切片所有盘.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E5%88%87%E7%89%87%E6%89%80%E6%9C%89%E7%9B%98.png)
- 再次点击**切片所有盘**，开始切片。  
  ![点击切片所有盘.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E7%82%B9%E5%87%BB%E5%88%87%E7%89%87%E6%89%80%E6%9C%89%E7%9B%98.png)
- 你可以看到按盘序号排列的文件，以及预估耗材用量和打印时间等详细信息。  
  ![切片预览信息.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E5%88%87%E7%89%87%E9%A2%84%E8%A7%88%E4%BF%A1%E6%81%AF.png)

## 开始打印

- 点击界面右上方打印单盘左侧的**箭头**，然后选择 **打印所有盘**。  
  ![打印所有盘.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%89%93%E5%8D%B0%E6%89%80%E6%9C%89%E7%9B%98.png)
- 再次点击**打印所有盘**，选择目标 3D 打印机，然后点击**发送**。  
  ![打印发送.png](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%89%93%E5%8D%B0%E5%8F%91%E9%80%81.png)

### 打印后续盘

- 第一盘打印完成后，待打印件冷却后取下，清洁打印板并放回热床。  
  ![removing_the_print_from_the_bed.gif](https://wiki.bambulab.com/software/bambu-studio/multi-plate/removing_the_print_from_the_bed.gif)
- 在确认打印完成的通知后，屏幕将自动返回至文件列表页面。在该页面中，选择你的模型（位于顶部）。  
  ![文件列表顶部.jpg](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%96%87%E4%BB%B6%E5%88%97%E8%A1%A8%E9%A1%B6%E9%83%A8.jpg)
- 点击**箭头翻页**选择下一个要打印的模型零件，点击**下一步**。  
  ![选择下一盘.jpg](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E9%80%89%E6%8B%A9%E4%B8%8B%E4%B8%80%E7%9B%98.jpg)
- 选择对应当前打印盘的耗材配置，点击右上角的**打印**，即可开始打印。  
  ![打印下一盘.jpg](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%89%93%E5%8D%B0%E4%B8%8B%E4%B8%80%E7%9B%98.jpg)

## 所有盘的打印顺序

多盘打印时，打印顺序与盘的添加顺序相反，即第一个添加的盘最后打印。如下方示例，首个开始打印的盘实际上是最后添加的。  
![打印顺序.gif](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E6%89%93%E5%8D%B0%E9%A1%BA%E5%BA%8F.gif)

## 使用建议

- **重命名打印盘以方便管理与查阅：** 右键点击打印盘，选择**编辑盘名**即可重命名。为打印盘自定义名称有助于在检查预览、排查故障及管理复杂项目时快速定位。  
  ![重命名.gif](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E9%87%8D%E5%91%BD%E5%90%8D.gif)
- **调整打印顺序：** 在 Bambu Studio 中，系统默认按照“后添加的盘优先打印”的逻辑执行。若需自定义顺序，可以采用逆序添加的方式进行规划；或者右键点击目标盘，选择**移动盘**，通过手动输入数字来调整其排序。  
  ![移动顺序.gif](https://wiki.bambulab.com/software/bambu-studio/multi-plate/%E7%A7%BB%E5%8A%A8%E9%A1%BA%E5%BA%8F.gif)
- **按颜色进行分组：** 对于多色打印任务，建议将相同颜色的零件组织在同一个打印盘上。这样可以有效减少打印过程中的换色冲刷次数，缩短整体打印时间。

## 结束语

> *我们希望这份指南为您提供了有效的信息，并真实地帮助了您。*
>
> *如果您对本文中描述的过程有任何疑问与顾虑，您可以在开始操作前联系我们的客户服务团队。*
>
> *我们随时准备为您提供帮助并回答您的任何问题。*
>
> [*点击这里提交服务工单*](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
