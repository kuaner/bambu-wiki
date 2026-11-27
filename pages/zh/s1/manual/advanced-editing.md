---
path: zh/s1/manual/advanced-editing
title: "高级编辑功能"
description: ""
tags: []
created: 2026-11-26T14:00:45.627Z
updated: 2026-11-26T14:00:45.627Z
source: https://wiki.bambulab.com/zh/s1/manual/advanced-editing
---

> ⚠️注意：除快速测量和坐标摆正外，高级编辑中的其他功能仅在连接Bambu Lab S1设备时开放。

### 快速测量

快速测量适用于在扫描数据上快速获取距离、角度、体积、面积的方法，适用于较为简单、单一的数据测量场景。

1. 距离测量

- 点到点：支持在模型上点选两点进行测量
- 点到面：先点一个点，再点目标面上的一个点，软件用该点附近的面拟合平面并计算距离。

![20261008231151_rec_.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/20261008231151_rec_.gif)

- 连续围长：支持在模型上进行连续的围长点选，并计算连续的围长，以及显示围长上每个路径的长度。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_12.png)

2. 角度测量：适用于三点间角度，或者面面之间的夹角的测量。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_26.png)

3. 体积测量：适用于封闭体积的场景测量。

> 注意：模型体积测量必须为封闭才会有有效体积参数值。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_10.png)

4. 面积：适用于特定框选面积的测量，可使用套索、画笔或魔棒选择需要测量的区域，或使用橡皮擦去除相关区域。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_5.png)

### 坐标摆正

通常扫描完毕的模型需要进行摆正操作，来辅助后续导出后的测量或逆向建模操作。目前分为快速摆正和特征对齐两种方式。

- 快速摆正：适用于有明确的平面或者几何特征的场景，可以根据指引逐步快速摆正。
- 放平底面：快速定位底面，将当前面对齐到XY底面。可以有两种方式指定底部面片，其中贴合表面为以选中点附近快速拟合一个平面来辅助摆放，外轮廓为基于扫描的平面快速拟合一个平面进行定位。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_18.png)

- 摆正水平朝向：选择一个水平面，点击后根据方向的需求，随鼠标拖动选择前后左右四个平面之一进行快速定位。

![PixPin_2026-10-10_09-59-14.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/pixpin_2026-10-10_09-59-14.gif)

- 对齐到原点：选择需要的对齐方式对齐到原点，支持包围盒中心、包围盒最小角、底面中心三种方式。

  - 自由调整：可通过左下角方块快速切换视角，并微调模型的角度与位置。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_7.png)

- 特征对齐：已经创建特征的情况下，可使用特征进行对齐。

  - 特征对齐会基于几何特征的约束来定义模型的坐标系，推荐使用**面-线-点**等组合来定义各特征。参考特征将按设定顺序依次定义坐标系的方向和位置，前面的约束规则优先级更高。创建特征方法请参考后文的创建特征、特征拟合功能。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_14.png)

- 面-线-点对齐方法中，第一参考的面作为 **XY**（图中XoY平面）**平面**存在，第二参考的线**投影至第一参考面的直线\*\*\*\*（图中 L 的投影）****视为**** ****X**** ****轴****或 Y 轴**（原视角下更靠近哪一轴为准），第三参考的点投影至第二参考线上的点，则被**视为原点**（图中点O）。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_6.png)

### 添加参考模型

添加的参考模型可用于进行数据比对，或作为热力图相关功能时使用的模型。可支持导入 STL、OBJ、PLY 以及 STP 文件作为参考模型的基准。

> ⚠️注意：单个扫描项目中仅支持导入 1 个 STP 文件，如已导入一个 STP 文件，后续导入的参考模型仅支持obj、ply、stl。

#### 数据比对

将导入模型与扫描结果对齐，即可开始比对数据。默认使用自动对齐进行初步对齐，如果对自动对齐结果不满意，可使用手动对齐。和手动拼接相同，需要在左右不同位置至少选择 3 对点。

点击预览对齐来检查对齐结果，如果不满意，可选择重新对齐，最后点击应用确认对齐。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_8.png)

### 特征拟合

特征拟合主要是对网格或CAD模型进行快速点选，或使用魔棒、套索、画笔工具对网格数据进行特征拟合。拟合的类型包含平面、圆、球、圆柱与圆台。所有创建的特征都会保存在左侧项目树中。

![new2.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/new2.png)

- CAD 点选：CAD 点选主要针对已经导入 STP 参考模型并对齐的场景。需要先选择目标特征的类型，再选择 CAD 模型上对应的特征，当指针识别到特征后，即可创建。

![new1.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/new1.png)

勾选“同步检测尺寸偏差”后，软件会自动尝试拟合对齐的扫描数据的对应特征，并计算其相对偏差值。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_13.png)

以一组扫描数据和 CAD 文件数据为例，两者对齐后，可使用CAD点选功能对CAD上的特征进行快速拟合，并尝试在扫描数据上生成一组同类数据进行比较，计算偏差值并显示在对应的标签中。

> ⚠️注意：如果CAD文件与被对齐的文件在被拟合处的差距较大，可能会导致同步检测数据提取失败。请重新对齐文件，或者尝试重新拟合。
>
> ![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_21.png)

如果需调整偏差，可在标签右下角针对偏差值进行调整，调整完毕后刷新结果重新计算。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image.png)

- 非 CAD 点选拟合：除 CAD 点选外，支持使用魔棒、画笔、套索等涂抹工具对扫描数据进行特征拟合。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_1.png)

目前支持3种拟合区域选中方式：

- 魔棒：点选特定区域后，会根据点选区域附近的面片的角度自动进行拟合。可调整填充角度，值越大，越容易选中更多连续区域;值越小，选区越小。
- 画笔：通过涂抹的方式选定需要进行拟合的区域。
- 套索：通过套索框选的方式选定需要进行拟合的区域。
- 橡皮擦：如需取消选中区域的特定部分，可使用橡皮擦工具对该区域进行涂抹。

![PixPin_2026-10-10_10-17-26.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/pixpin_2026-10-10_10-17-26.gif)

### 创建特征

除特征拟合外，还可以直接拉伸或**基于已有特征的**方式快速创建特征，包含点、线、平面、圆、球、圆柱、圆台。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_20.png)

- 点：可以直接点选，或使用现有特征的中心点（圆、球或直线）。
- 线：可以直接指定2点创建，或基于现有圆柱、圆台的轴线进行创建。
- 平面：可以直接指定平面上3点创建， 或基于单个点与法向线创建特征。
- 圆：可以直接指定圆上3点创建，或基于圆柱、圆台的截面，或圆心、法向创建特征。
- 球：可以直接指定球上4点创建，或基于圆，或指定圆心和半径来创建特征。
- 圆柱：可以指定底面圆上3点与圆柱高度创建，或基于圆并指定高度，或基于轴线并指定半径来创建特征。
- 圆台（圆锥）：可以指定底面圆上3点与顶圆上1点创建，或者基于圆指定高度和锥角，或者基于圆柱和锥角来进行创建。

### 特征测量

当存在多个特征时，可对特征进行距离、角度测量。

以测量两个圆柱的相对轴心位置为例，当创建了两个模型特征并点击检测按钮后，即可得到轴心距离。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_24.png)

如果需要进行对比检测，可在打开相关按钮后输入理论值内容，并指定公差范围，点击检测后生成的测量标签可反映两圆柱体的距离误差是否在指定的公差范围内，这可以适用于部分需要检测输出的场景。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_3.png)

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_2.png)

- 快照视图：点击快照视图按钮，即可快速浏览目前所有公差检测结果，并底部菜单栏通过“拍照”截图输出。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_22.png)

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_19.png)

### 热力图

热力图是为了反映参考模型和扫描数据之间的局部误差大小，可以帮助用户了解整体零件在空间范围内误差的分布情况。

- 选择对比模型：支持从项目树列表中已有的模型进行选择，或新上传一个对比模型

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_4.png)

- 对齐操作：同添加参考模型步骤中的对齐操作，可使用自动对齐或手动选点对齐完成参考模型和扫描数据的对齐操作。并点击右上角生成热图按钮，进入热力图视图中。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_23.png)

- 创建热力视图：在热力视图中，可指定特定的参数来创建热力视图，主要包含以下特定参数

  - 搜索距离：偏差和色谱的显示范围（例如 ±0.20 mm），设置范围以外的数值不生成色谱图。
  - 显示极值标签：显示当前搜索范围内的最大值和最小值标签。
  - 色谱显示：色谱显示模式，目前支持4种色谱信息的显示。
  - 最大角度：最大角度影响纳入计算的热力图距离的邻近面片数量，角度越大则纳入计算的面片数量越多。
  - 显示公差与公差范围：适用于创建标签显示的检测结果所在的公差范围。

完成相关参数设置后，即可点击更新热力图按钮进行热力图创建或更新。或点击返回调整模型进行模型调整。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_25.png)

- 创建测量标签：热力图创建后，即可在模型上任意位置点击，创建局部的测量标签。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_11.png)

- 快照视图：同特征测量，热力图也可点击快照视图按钮，在视图中对生成的快照进行属性设置及拍照导出。

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_9.png)

![image.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/advanced-editing/image_15.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
