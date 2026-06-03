---
path: zh/h2s/maintenance/period-maintenance
title: "H2S 定期维护清洁建议"
description: ""
tags: []
created: 2025-08-24T11:21:50.399Z
updated: 2026-04-23T01:24:56.857Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/period-maintenance
---

## 前言

激光加工过程中会产生烟雾，激光气泵在激光工作时提供高压气流，用于吹散切割过程中产生的烟尘。这不仅可以防止材料切割边缘被熏黑，降低着火风险，还能保护激光头镜片免受烟尘污染。当与顶部自动风门、过滤切换风门、腔体外排风扇、自动排气格栅、排烟管转接件及排烟管配合使用时，激光切割产生的烟尘将通过打印机的外排风扇排出机箱外。有关更多排烟管的安装指南，请参考相关文档。[激光模组安装指南（以10W激光模组为例）](../../h2/manual/laser-module-lnstallation-guide.md)

虽然大部分烟雾会通过排烟管排出，但仍会有一些烟雾留在机箱内部。因此，如果使用激光模组，打印机内部的污染情况会比仅使用打印功能时更加严重，需要更频繁地进行维护。

如果长时间不清理机箱周围的内壁，污垢会容易堆积，前门和侧板的附着物可能会影响视线。因此，定期使用酒精和无纺布擦拭这些区域也是必要的。同时，应定期清洁工具头上的冷却风扇风道、堵嘴片及其磁铁支架等部件。此外，X轴线轨、Y轴和Z轴的光杆与丝杆也需要定期使用酒精和无纺布清洁。特别需要注意的是，金属轴承类部件在使用酒精擦拭后，建议补充润滑油（适用于线轨和光杆）或润滑脂（适用于丝杆）。

为了保证各类智能视觉检测和传感器检测工作正常，定期清洁各类摄像头镜头表面和火焰传感器也十分重要，建议使用酒精和无纺布擦拭镜头，同时清洁激光扳手标记、热端标记、打印板及激光垫板标记，以及热床内侧的平行四边形限位块，以防止图像模糊或标记识别错误。**清洁摄像头时，请沾少量的酒精，并在擦拭前将无纺布捏干一些，以防酒精渗入塑料外壳内部**。有关智能检测功能的介绍，请参考相关文档 [H2D智能检测介绍](../../h2/manual/intelligent-detection.md)

此外，机箱与外部空气交换的相关部件容易积聚灰尘。建议定期使用毛刷清理积灰。对于滤芯盖和背面的排气格栅，也可以拆下进行清洁，以确保设备的正常运行和延长使用寿命。

## 维护频次

H2S可以基于任务类型和任务时长评估打印机的污染程度，并给出对应的清洁维护提醒。**请务必按照要求对激光模组和打印机各部件进行维护清理，如果不按时清理，可能导致机器损坏并产生安全风险。**

关于激光模组的维护指南，请参考[10w 激光模组定期维护建议](../../h2/maintenance/laser-module.md)

如果仅使用3D打印功能，各部件的维护频率如下：

| 部件 | 清洁维护频率 | 注意事项 | 部件 | 清洁维护频率 | 注意事项 |
| --- | --- | --- | --- | --- | --- |
| 打印机外表面和屏幕 | 3个月 |  | X轴线轨 | 1个月 | 清洁后涂抹润滑油 |
| 热床 | 3个月 |  | Y轴光杆 | 1个月 | 清洁后涂抹润滑油 |
| 工具头 | 3个月 |  | Z轴丝杆和光杆 | 1个月 | 清洁后涂抹润滑脂 |
| 工具头相机 | 3个月 | 无纺布沾涂少量酒精，并且捏干一些 | 实况相机 | 3个月 | 无纺布沾涂少量酒精，并且捏干一些 |
| 俯视相机 | 3个月 | 无纺布沾涂少量酒精，并且捏干一些 | 上盖组件 | 3个月 |  |
| 火焰传感器 | 3个月 | 无纺布沾涂少量酒精，并且捏干一些 | 左右侧板 | 3个月 |  |
| 辅助部件冷却风扇 | 3个月 |  | 活性碳滤芯盖 | 3个月 |  |
| 左右内衬 | 3个月 |  | 排气格栅 | 3个月 |  |
| 腔体外排风扇 | 3个月 |  | 挤出机齿轮 | 3个月 | 与使用频次以及使用的耗材种类有关，可以参考[这篇wiki](../troubleshooting/clogging.md)进行清洁清理。 |

**注意：若长期打印高温或工程类耗材，建议适当提高维护频率——将上述表格中每 3 个月一次的维护周期调整为每月一次；每月一次的调整为每半个月一次**

## 清洁所需要的材料

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-14.png)

1. 酒精
2. 清洁刷
3. 润滑油和润滑脂（润滑脂分为瓶装和袋装，具体以你收到的版本为准）
4. 无纺布或不含纤维的其他清洁布
5. 手套

### 清洁剂说明

在上述维护过程中，建议使用少量酒精（75%的乙醇或70%的异丙醇）和无纺布擦拭摄像头、金属和塑料等表面。对于特殊部位，如滤芯盖、格栅、风扇叶片和散热片，建议使用毛刷进行清理。

**使用液体清洁剂后，请适当拧干无纺布再进行清理。同时，强烈建议您增加清洁频率，以防油污结块，难以去除。**

如果污染严重，可以使用威猛先生等油污清洁剂进行深层清洁。

### 易损消耗件的保养更换说明

| 易损部件 | 建议更换频率 |
| --- | --- |
| [切刀刀片](replace-cutter.md) | 对于 PLA/PETG/ABS/PC 等常规耗材，应每 3-5 卷检查一次刀片。 如果刀片变钝，请更换它。对于 PA+CF/PA+GF 等磨料耗材，刀刃会很快变钝，因此我们建议在打印 1-2 卷磨料耗材后进行检查。 如果刀片变钝，请更换它。 |
| [挤出齿轮](../troubleshooting/clogging.md) | 当您看到挤出机齿轮上有少量灰尘时，您应该清理挤出机内部的灰尘。我们建议每月检查并清洁一次挤出机齿轮，如果发现挤出机齿轮磨损，则需要进行更换。 |
| 吐料组件上的擦嘴硅胶 | 如果硅胶擦嘴损坏或变形了，为确保喷嘴清洁效果，需要进行更换 |
| [热端硅胶套](replace-silicone-sock-and-hotend.md) | 如果硅胶套上有磨损迹象，或者硅胶套不能牢固地固定在热端上，则应更换硅胶套。 |
| [热端](replace-silicone-sock-and-hotend.md) | 正常情况下，打印 PLA、PETG 这类非碳纤耗材时，建议每打印5卷耗材后冷拔清洁一次热端；打印碳纤耗材时，每打印2卷耗材冷拔清洁一次热端。如果发现热端有明显的磨损导致漏料，常规清理已经无法解决问题，请更换一个新热端。 |

## 维护步骤

在正式开始清洁维护操作之前，请先将打印机关机。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-12.png)

## 与激光模组相关的部件清洁（如无激光模组，可以跳过前3步，从第4步开始）

### 步骤1. 取出激光垫板

打开打印机前门并移除上盖，然后从热床上取下激光垫板。

|  |  |
| --- | --- |
|  |  |

### 步骤2. 清理激光垫板和支撑条

戴上手套，拆下激光垫板上的所有支撑条。

|  |  |
| --- | --- |
|  |  |

先在激光垫板四周的标记处喷涂酒精，并用无纺布仔细擦拭，将污渍清理干净。  
![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-8.png)

|  |  |
| --- | --- |
|  |  |

然后在激光垫板内部喷涂酒精，使用无纺布仔细擦拭。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-4.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-1.png)

在支撑条上喷涂酒精，同样使用无纺布擦拭，将污渍清理干净。清理完成后，重新将支撑条安装回激光垫板的卡槽中。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-29.png)

### 步骤3. 拆除激光模组

断开激光连接线，并解锁快拆锁扣，取下激光模组。

|  |  |
| --- | --- |
|  |  |

## 整机部分清洁（与3D 打印功能相关）

### 步骤4. 清理打印机前门和屏幕

使用沾了酒精的无纺布擦拭打印机屏幕，前门外侧和前门内侧，将灰尘清理干净。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-26.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-25.png)

### 步骤5. 清理热床

在热床上喷酒精，并用无纺布擦拭热床表面。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-24.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-23.png)

热床表面擦拭干净后，继续擦拭热床四周边缘，将污渍清理干净，尤其是对于相机识别所需要用的热床表面marker。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-18.png)

### 步骤6. 清理工具头

使用粘上酒精清洁剂的湿润无纺布擦拭工具头中框前后左右四周表面和切刀刀柄

|  |  |
| --- | --- |
|  |  |

取下工具头前盖以清洁挤出机的表面

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-20.png)

清洁工具头摄像头和部件冷却风扇

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-19.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-15.png)

清洁拖链及PTFE管卡扣

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-17.png)

### 步骤7. 清理并润滑X轴线轨

使用无纺布擦拭X轴线轨，皮带也可以一起清理。需要移动工具头，以确保清洁工具头左右两边的线轨都可以被清洁到位，确保线轨上下滚珠槽都清洁到位。

|  |  |
| --- | --- |
|  |  |

> X轴线轨表面的灰尘和异物都清理干净后，需要在线轨的滚准槽上补充润滑油，并左右移动工具头，使润滑油在线轨上均匀分布。请注意，工具头左右2边都要确保均润滑充分，线轨的上侧和下侧都需要涂润滑油。

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-40.png)

### 步骤8. 清理并润滑Y轴光杆

使用喷涂酒精的无纺布擦拭Y轴光杆，然后移动工具头，以清理被滑车遮挡住的部分光杆。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-39.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-35.png)

将这段光杆完全清理干净后，在光杆上涂抹润滑油，涂抹时，上下都需要涂抹，并且推荐画S形涂抹，前后移动工具头，使润滑油均匀分布在Y轴光杆上，进行充分润滑。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-37.png)

![lubricate-y.webp](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/lubricate-y.webp)  
接下来使用同样的方法清洁并润滑另一根Y轴光杆。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-38.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-36.png)

### 步骤9. 清理并润滑Z轴丝杆和光杆

将沾了酒精的无纺布包裹住光杆，上下移动进行擦拭，确保光杆清理干净。然后用同样的动作擦拭丝杆。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-34.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-33.png)

然后在丝杆上涂**润滑脂，**光杆上涂**润滑油**，请注意润滑油和润滑脂不要用混。丝杆指有螺纹的杆，光杆指光滑的杆，润滑脂和润滑油相比更粘稠。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-32.png)

|  |  |
| --- | --- |
|  |  |

除了左侧的光杆和丝杆，H2S内部还有右侧以及内侧的光杆和丝杆，总共3组。对于另外2组光杆、丝杆，也需要进行相同的清理和润滑操作。

下图为右侧光杆和丝杆的清理、润滑过程。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-58.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-55.png)

下图为内侧光杆和丝杆的清理、润滑过程。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-54.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-53.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-50.png)

润滑完毕后，重新将打印机上电，在打印机屏幕上控制热床上下移动，目的是让润滑油和润滑脂完全浸润Z轴丝杆和光杆，确保充分润滑。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-51.png)

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-45.png)

在继续清洁工作之前，请再次将打印机关机。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-46.png)

### 步骤10. 清理火焰传感器

打印机内共有4个火焰传感器，它们位于打印机框架的4个角落。使用无纺布擦拭每个火焰传感器。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-72.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/%E7%81%AB%E7%84%B0%E4%BC%A0%E6%84%9F%E5%99%A8.webp)

### 步骤11. 清理俯视相机和实况相机

使用喷了酒精的无纺布，擦拭俯视相机和实况相机的镜头。

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
|  |  |

### 步骤12. 清理上盖组件，左右内衬，及左右侧板内部和打印机底部

使用喷了酒精的无纺布清理上盖组件的内衬，左右侧板内衬，四周都需要擦拭，左右内衬的上侧以及左内衬的表面，同时擦拭一下吐料组件，清理残余的耗材。如果有部分位置难以清理，可以将工具头移开，方便清理。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-67.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-66.png)

适当上升热床，然后清洁打印机底部的灰尘和异物。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-64.png)

### 步骤13. 清理辅助部件冷却风扇

使用沾了酒精的无纺布清理左侧板玻璃以及辅助部件冷却风扇上侧的灰尘，然后擦拭辅助部件冷却风扇的表面及两侧。辅助部件冷却风扇的上侧有减震结构，清理时请尽量不要用力往外侧拉，防止减震钉脱落。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-65.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-63.png)

### 步骤14. 清理活性碳滤芯盖

用刷子清洁滤芯盖，如果滤芯盖特别脏，或者需要更换滤芯，可以按照下文的方法进一步清洁。

![brush.webp](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/brush.webp)

用手按住活性碳滤芯盖顶部，向外拉活性碳滤芯盖以解锁顶部的卡扣，拆除活性碳滤芯盖。移除活性碳滤芯时，请用纸垫在活性碳滤芯下方，防止灰尘掉落到打印机内部。

![remove-filter-cover.webp](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/remove-filter-cover.webp)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-60.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-62.png)

如果滤芯盖特别脏，取下后，可以先使用刷子清理滤芯盖正反面的灰尘，然后使用沾了酒精的无纺布将滤芯盖擦拭干净。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-61.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-86.png)

若滤芯盖脏污程度非常严重，普通方式已经无法清理滤芯盖。可以尝试将滤芯盖直接放在水龙头下进行冲洗，同时使用刷子清理。**请注意，水洗之后一定要将滤芯盖完全擦干，滤芯盖周围有一些电子器件，残留的水分可能会影响这些电子器件的功能。**

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-87.png)

### 步骤15. 清理腔体外排风扇内侧和空气滤芯槽

使用沾了酒精的无纺布擦拭右内衬内部的活性碳滤芯槽。

向上移动过滤切换风门，清理下半部分风门。清理完成后，再将过滤切换风门降下去。在清理过滤切换风门时，频繁上下移动过滤切换风门可能会减少舵机的使用寿命，请尽量减少推拉风门的次数。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-84.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-83.png)

清洁完毕后，将新的活性碳滤芯装入打印机右内衬。然后将活性碳滤芯盖斜着插入内衬，底部的五个插销插入内衬中，往内推活性碳滤芯盖，将顶部的四个卡扣和一个止口也卡入内衬。

![install-filter-cover.webp](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/install-filter-cover.webp)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-82.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-80.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-81.png)

### 步骤16. 清理排气格栅

排气格栅位于腔体外排风扇的外侧，共有7条排气格栅。**拆除排气格栅时，从上往下拆**。先略微用力将排气格栅往外凹，然后将右侧的定位块从小孔中取出。顺时针旋转排气格栅90°，向上提一下排气格栅即可顺利取出插销，拆除排气格栅。按照相同的步骤拆除剩余6条排气格栅。

![remove-leaf.webp](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/remove-leaf.webp)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-77.png)

![优化箭头.jpg](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/%E4%BC%98%E5%8C%96%E7%AE%AD%E5%A4%B4.jpg)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-78.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-76.png)

先用刷子扫除排气格栅上的灰尘，然后使用沾了酒精的无纺布擦拭排气格栅。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-75.png)

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-74.png)

若排气格栅的脏污程度非常严重，普通方式已经无法清理排气格栅。可以尝试将排气格栅直接放在水龙头下进行冲洗，同时使用刷子清理。**请注意，水洗之后一定要将排气格栅完全擦干，排气格栅周围有一些电子器件，残留的水分可能会影响这些电子器件的功能。**

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-90.png)

### 步骤17. 清理腔体外排风扇外侧

拆除排气格栅后，使用刷子清理风扇外侧的灰尘。

![](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/image-89.png)

清理完毕后，**安装排气格栅时从下往上装**，先从左侧开始，将左侧插销先放入箭头所指的孔中，同时将左侧的定位块对准圆圈所示的小孔并扣合上，然后将右侧的定位块也扣入右侧的小孔中。按照相同的步骤安装剩余6条排气格栅。

![install-leaf.webp](https://wiki.bambulab.com/h2s/maintenance/period-maintenance/install-leaf.webp)

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
|  |  |

### 步骤18. 清理喷嘴和加热组件表面

屏幕上控制喷嘴加热到250℃左右，小心取下喷嘴并用干净的纸巾擦拭。

![喷嘴擦拭清理.webp](https://wiki.bambulab.com/h2/maintenance/period-maintenance/%E5%96%B7%E5%98%B4%E6%93%A6%E6%8B%AD%E6%B8%85%E7%90%86.webp)

> 建议带上隔热手套完成这项清洁工作，注意高温烫伤。

清理完喷嘴后请检查屏幕上加热组件的温度是否仍维持在250℃，再清理加热组件表面

![h2s加热组件.webp](https://wiki.bambulab.com/h2/maintenance/period-maintenance/h2s%E5%8A%A0%E7%83%AD%E7%BB%84%E4%BB%B6.webp)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
