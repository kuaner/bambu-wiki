---
path: zh/software/bambu-studio/multi-color-printing
title: "多色打印指南"
description: ""
tags: []
created: 2023-03-14T13:44:33.396Z
updated: 2026-02-05T09:51:43.127Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/multi-color-printing
---

本页介绍如何在 Studio 中管理耗材以及如何在 AMS 中使用耗材映射功能。

![](https://wiki.bambulab.com/software/bambu-studio/filaments/color_printing_group.png)

欢迎来到多彩的世界！多色打印是 Bambu Studio 最令人惊叹的功能之一。导入模型后，只需几步即可完成彩色模型：

1. 根据您想要的颜色添加耗材丝。如果您想使用支撑材料以获得更好的悬垂质量，请在耗材丝栏中添加它；

2. 给模型上色；

3. 切片并打印。

## 管理项目中的耗材

项目中的耗材都列在左侧的耗材栏中

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E7%AE%A1%E7%90%86%E9%A1%B9%E7%9B%AE%E4%B8%AD%E7%9A%84%E8%80%97%E6%9D%90%E4%B8%9D.png)

在耗材栏中，你可以完成所有耗材的管理任务：

- **添加耗材**

单击 ➕ 按钮将新耗材添加到项目中。新添加的耗材将附加到耗材列表中。

- **删除耗材**

单击 ➖ 按钮删除最后一个耗材

- **设置耗材的颜色/类型**

设置每个耗材的类型和颜色。当连接打印机时，您可以从 AMS 插槽快速获取颜色和类型。

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E8%AE%BE%E7%BD%AE%E8%80%97%E6%9D%90%E7%9A%84%E9%A2%9C%E8%89%B2%E7%B1%BB%E5%9E%8B.gif)

- **配置耗材类型的可见性**

您可以通过单击耗材栏中 ⚙ 在对话框中配置每种耗材类型的可见性。只有选定的耗材类型才会在组合框的下拉列表中可见。

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E9%80%89%E6%8B%A9%E6%9D%90%E6%96%99.png)

耗材列表也保存在 3mf 项目文件中，加载 3mf 文件时将恢复。

## 给模型上色

Bambu Studio 为各种类型的模型提供了多功能的着色工具。

### 为物体/零件设置耗材

您可以通过多种方式将耗材绑定到对象或零件：

在左侧边栏的对象列表中为对象/零件选择耗材丝：

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E4%B8%BA%E9%9B%B6%E4%BB%B6%E9%80%89%E6%8B%A9%E8%80%97%E6%9D%90.png)

右键单击目标对象/零件并从上下文菜单中选择耗材丝

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E5%8F%B3%E5%87%BB%E6%9B%B4%E6%8D%A2%E8%80%97%E6%9D%90%E4%B8%9D.png)

**选中一个对象后，用快捷键 1-9 可以将对应编号的耗材丝匹配到选定的对象/零件。**

*提示：如果找不到对象列表，需要在这里切换到全局/对象模式*

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E5%88%87%E6%8D%A2%E5%85%A8%E5%B1%80&%E5%AF%B9%E8%B1%A1.png)

### 在对象上绘画

Bambu Studio 提供了一个强大的彩绘工具。使用此工具，您可以在所选对象上用不同颜色绘制几乎任何东西。

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E5%AF%B9%E8%B1%A1%E7%BB%98%E7%94%BB1.jpg)

![](https://wiki.bambulab.com/software/bambu-studio/filaments/%E5%AF%B9%E8%B1%A1%E7%BB%98%E7%94%BB2.jpg)

左图显示原始模型，右图显示涂漆模型。 详细请参考 [涂色工具使用指南 | Bambu Lab Wiki](color-painting-tool.md)。

## 设置多色切片参数

对于单个挤出机打印机，每次更换耗材时，挤出机中都会留下少量耗材。当新的耗材被送入挤出机时，它会将旧的耗材推出挤出机和喷嘴。在此期间，您会看到挤出的耗材颜色逐渐发生变化。 因此，为了确保模型的颜色不乱，需要足够的新耗材体积（冲刷体积）来冲洗掉旧耗材。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/print_not_clean.png)

但是过多的冲刷量意味着浪费耗材和打印时间。[减少多色打印时的材料浪费 | Bambu Lab Wiki](reduce-wasting-during-filament-change.md) 中描述的功能介绍了如何打印出所需的颜色效果，并减少浪费的耗材。

![](https://wiki.bambulab.com/software/bambu-studio/reduce-wasting-during-filament-change/wasted_filament_in_printing.jpg)

## 使用 AMS 打印多色模型

使用 AMS 打印时，切片项目中的耗材列表不一定需要与 AMS 耗材列表完全相同。 发送打印任务时，根据颜色和材料类型（PLA/ABS/PC...）自动构建切片项目到 AMS 的耗材映射。

### AMS 操作

#### 进料

选择要装入耗材的槽。当指示灯开始闪烁时，向前按下按钮并插入耗材，直到耗材自动拉入。  
![screenshot-20240918-172704.png](https://wiki.bambulab.com/studio-ams/screenshot-20240918-172704.png)

#### LED 灯状态

- **白灯亮**  
  有料插入该槽且处于空闲状态。耗材可以拉出。(如果感觉槽内堵塞堵塞，请按下按钮释放耗材）。
- **白灯呼吸**  
  料槽繁忙，请勿拉出耗材。
- **红灯**  
  错误状态。 请检查错误信息或联系技术服务。

![20240919-153626.jpg](https://wiki.bambulab.com/studio-ams/20240919-153626.jpg)

### 耗材控制界面

图标说明：

- RFID 读取按钮和指示灯
- 耗材颜色和类型
- 编辑或查看耗材信息

![20240919-153621.jpg](https://wiki.bambulab.com/studio-ams/20240919-153621.jpg)

### AMS 映射

- **在 AMS 中查看耗材类型和颜色**  
  ![screenshot-20240918-172704.png](https://wiki.bambulab.com/studio-ams/screenshot-20240918-172704.png)
- **点击编辑图标设置耗材类型和颜色**  
  ![动画_颜色.gif](https://wiki.bambulab.com/studio-ams/%E5%8A%A8%E7%94%BB_%E9%A2%9C%E8%89%B2.gif)
- **Bambu Studio AMS 映射**  
  Bambu Studio 将对当前打印作业进行 AMS 映射（匹配耗材类型和颜色）。AMS 映射部件的上半部分是当前项目的源颜色和类型，下半部分是 AMS 料槽的目标索引和颜色。  
  ![颜色对应.png](https://wiki.bambulab.com/studio-ams/%E9%A2%9C%E8%89%B2%E5%AF%B9%E5%BA%94.png)

> **注意**：
>
> - 可在**设备**中选择要使用的打印机，然后在**准备**界面单击**从AMS同步材料列表**图标，再单击**重新同步**。
>
> |  |  |
> | --- | --- |
> |  |  |
>
> - 开启**多设备管理**可能会出现无法同步耗材丝的问题。可点击**多设备**界面中要使用的打印机**视图**，切换到指定设备界面，然后再回到**准备**页面同步，即可成功。
>
> |  |  |  |
> | --- | --- | --- |
> |  |  |  |

Bambu Studio 会自动获取匹配相同类型和相似颜色的耗材丝。 通常，您不需要修改任何内容。但是如果你对自动映射的结果不满意，也可以手动调整。

- **如下所示手动调整映射**  
  ![动画_mapping.apng](https://wiki.bambulab.com/studio-ams/%E5%8A%A8%E7%94%BB_mapping.apng)

### 同步 AMS 耗材

无需等到发送打印任务时，再将项目耗材与可用的 AMS 及打印机耗材进行匹配，我们可以通过两种方式同步 AMS 耗材与项目耗材。

操作前，请先点击下方所示的**从 AMS 同步耗材列表**按钮。

![bambu_studio_多色打印指南_同步.png](https://wiki.bambulab.com/software/bambu-studio/multi-color-printing/bambu_studio_%E5%A4%9A%E8%89%B2%E6%89%93%E5%8D%B0%E6%8C%87%E5%8D%97_%E5%90%8C%E6%AD%A5.png)

#### 匹配模式

第一种方式是通过匹配耗材类型与颜色，将 AMS 耗材与原始项目耗材进行匹配，同时支持手动编辑。该方式与发送打印任务时的匹配逻辑类似，但本次同步会直接更新项目耗材，且无法自动撤销。

1. 匹配式耗材同步模式
2. 待匹配的原始项目耗材
3. 与项目耗材对应的 AMS 耗材匹配关系（可手动修改）
4. 未使用的耗材添加至项目耗材列表末尾的选项（取消勾选则不会同步未使用的耗材）
5. 将重复的 AMS 耗材合并为单个项目耗材的选项
6. 完成同步的按钮

![bambu_studio_多色打印指南_匹配.png](https://wiki.bambulab.com/software/bambu-studio/multi-color-printing/bambu_studio_%E5%A4%9A%E8%89%B2%E6%89%93%E5%8D%B0%E6%8C%87%E5%8D%97_%E5%8C%B9%E9%85%8D.png)

> **说明**：您可随时使用该方式，将项目耗材更新为与打印机可用耗材保持一致。

#### 覆盖模式

第二种方式是按顺序使用首批可用的 AMS 耗材直接覆盖项目耗材。该方式为自动执行，不支持手动编辑耗材匹配关系。

其他 AMS 料槽中的额外耗材也会被添加为项目耗材，最终项目耗材列表将完全对应打印机的所有耗材。

1. 覆盖式耗材同步模式
2. AMS 至原始项目耗材的自动匹配关系
3. 完成同步的按钮

![bambu_studio_多色打印指南_覆盖.png](https://wiki.bambulab.com/software/bambu-studio/multi-color-printing/bambu_studio_%E5%A4%9A%E8%89%B2%E6%89%93%E5%8D%B0%E6%8C%87%E5%8D%97_%E8%A6%86%E7%9B%96.png)

> **说明**：该方式通常在模型涂色前使用最为实用，可将所有可用的 AMS 及打印机耗材同步至项目中，以便用于涂色操作。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们的客户服务团队。我们随时准备为您解答疑问并提供帮助。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
