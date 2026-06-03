---
path: zh/x2d/manual/screen-operation
title: "X2D 屏幕操作指南"
description: "本指南介绍了 X2D 的屏幕操作及相关功能"
tags: []
created: 2026-04-14T14:11:48.118Z
updated: 2026-04-14T14:11:49.194Z
source: https://wiki.bambulab.com/zh/x2d/manual/screen-operation
---

## 主页

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**耗材**、**设置**和 **HMS**；右侧为**文件**、**主/辅助喷嘴温度、耗材、网络设置**和**HMS**，点击图标可快速跳转至对应的控制界面。

![screenshot_20260330_121847.png](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/screenshot_20260330_121847.png)

点击**文件**，可查看模型和影像。其中，“模型”包括机内存储、历史记录和外部存储中的模型；

- **机内存储：**缓存在打印机本地的模型文件；
- **历史记录：** 打印机缓存空间内的模型列表；
- **外部存储：**缓存在打印机上 U 盘内的模型文件；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/010.png)

“影像”包括机内存储和外部存储中的延时摄影录像，关于延时摄影内置存储的详细信息，请参考：[延时摄影内置存储和素材管理](../../knowledge-sharing/timelapse-internal-storage-and-video-management.md)。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/044.png)

## 控制

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/055.png)

### 1. **空调系统**

可根据耗材的不同选择合适的空调系统。

- **强力冷却**：适合打印 PLA/TPU 等**耐热性较低的耗材；**腔体降温时，系统会自动切换至强力冷却模式。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/033.png)

- **腔温保持模式**：适合打印 ABS/ASA/PC/PA 等**具备高耐热性的耗材。**腔体加热时，系统会自动切换至腔温保持模式；在此模式下，腔体加热风扇将自动开启。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/022.png)

- **部件冷却风扇：**位于工具头上，用于确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/064.png)

- **左/右侧板辅助冷却风扇：**位于机箱内两侧，能为高速打印提供更好的冷却条件。

|  |  |
| --- | --- |
|  |  |

- **腔体加热风扇：**位于机箱左侧，与 PTC 加热片构成腔温加热组件；设定腔温后，PTC 将全功率加热，腔体加热风扇会以最大转速运行。当腔温达到设定值后，风扇会降速至 40%，PTC 加热片功率也会降低，以恒定功率维持腔温。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/097.png)

- **腔体过滤风扇：**安装在机箱内右侧；打印高温耗材时，打印机会自动处于腔温保持模式。自适应风道切换组件与机箱内的空气滤芯会形成内循环，使机箱内空气持续经过滤芯过滤，在保持腔体温度的同时，最大程度减少异味和微粒排放。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/141.png)

- **腔体外排风扇：**位于打印机背板；打印 PLA 等低温耗材时，可实现打印气体外排，并联动自适应空气循环系统强化散热；打印高温耗材时，通过在屏幕开启“打印结束时净化空气”功能，可在打印完成后自动排出机箱残留气体。配合排气管使用，可将打印废气直接引导至室外或指定区域。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/011.png)

- **腔温：**根据打印耗材的不同，可设置合适的腔温。低腔温适合打印 PLA、PETG 等耗材；高腔温适合打印 ABS 等的易翘曲耗材。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/130.png)

### 2. **速度**

设置打印速度模式。

- **狂暴**：正常打印速度和加速度的 166%
- **运动**：正常打印速度和加速度的 124%
- **标准**：正常打印速度和加速度
- **静音**：正常打印速度和加速度的 50%

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/108.png)

### 3. **运动**

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/119.png)

1. **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
2. **热床**：点击 1 格或 10 格的移动按钮，升降热床。
3. **自由移动：**开启该功能后，当 XYZ 电机空闲时，支持手动自由移动工具头和热床，方便维护修理。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/059.png)

### 4. **喷嘴和挤出机**

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/060.png)

1. **左边/右边（辅助）**：点击左边/右边（辅助），可触发喷嘴切换拨杆组件碰撞内衬上的顶块组件，完成主/辅助喷嘴的切换。

![switch-hotend1.webp](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/switch-hotend1.webp)

2. **喷嘴温度**：输入数值，可设置喷嘴温度，最高 300 ℃。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/061.png)

3. **喷嘴类型**：可手动设置喷嘴的类型、材质及直径。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/155.png)

4. **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。

- **主挤出机：**如果主挤出机的料管中显示耗材颜色，则表示主挤出机的霍尔开关检测到有耗材进入。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/062.png)

- **辅助挤出机：** 辅助挤出机中的耗材颜色位置对应其在打印机中的进料位置。以下三张图示分别为：

辅助挤出机内有耗材：

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/063.png)

工具头内有耗材：

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/069.png)

辅助挤出机和工具头内均有耗材：

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/070.png)

> 注：手动插入耗材时，设备未读取 RFID 芯片，屏幕显示的耗材颜色可能有误，此时显示的为耗材页面对应的耗材颜色。

### 5. **机箱**

同上述腔温。

### 6. **热床**

输入数值，设置热床温度。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/065.png)

### 7. **照明**

点击此按钮可控制机箱内部 LED 补光灯。

|  |  |
| --- | --- |
|  |  |

## 耗材

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/066.png)

### 1. **耗材信息**

如果 AMS 已通过 RFID 识别该料盘信息，则耗材上方会显示耗材类型和余量。

### 2. 料盘

点击任一料盘图标，可进行耗材编辑、进退料和 RFID 重读操作；

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/068.png)

- **编辑：**如果 AMS 已通过 RFID 识别该料盘信息，可在此处查看料盘信息，但无法修改耗材参数；如果未读取 RFID，则可在此处修改耗材信息。

|  |  |
| --- | --- |
|  |  |

- **进料：**点击按钮，AMS 会自动将耗材进料至挤出机；
- **重读：**点击按钮，AMS 会重新读取该槽位的 RFID。

### 3. **烘干/湿度**

可查看 AMS 内部湿度和温度，并烘干耗材。

> 注意：您也可以在“设置”>“工具箱”>“烘干耗材”中开启烘干功能。

如果打印机连接了 AMS 2 Pro 或 AMS HT，此处会显示 AMS 内部湿度和温度；选择耗材类型后，点击“开始”，可对耗材进行烘干。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/004.png)

如果打印机连接了一代 AMS，则会显示舱内干燥等级。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/082.png)

### 4. 辅助挤出机状态

如果辅助挤出机内有料，送料路径将显示对应的耗材颜色，且屏幕会显示“辅助挤出机已进料”。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/084.png)

### 5. **工具**

共有自动续料、AMS 初始化和 AMS 烘干三种工具。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/083.png)

1. **自动续料**：该功能允许用户查看哪些槽位的耗材可以相互续料。当耗材的品牌、类型和颜色完全相同时，系统将建立自动续料关系。当前耗材用完时，打印机会自动切换到相同属性的耗材继续打印。

> 注意：当两个相同耗材来自同一个挤出机连接的 AMS 时，才能形成续料关系，即左对左，右对右。如果两个耗材来自不同的挤出机，则无法建立续料关系。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/003.png)

2. **AMS 初始化**：首次将 AMS 连接到 X2D 打印机时，需要进行一次初始化，目的是检测 AMS 连接到了哪一侧的挤出机。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/079.png)

- **自动模式：**开启自动 AMS 初始化，AMS 会自动将耗材送至挤出机，主挤出机和辅助挤出机上各有一个霍尔传感器，可通过霍尔传感器触发信号来判断 AMS 所配对的挤出机。

> 注意：
>
> - 在 AMS 任一槽位内插入一卷耗材；
> - 已进料的耗材需提前退料；
> - 确保缓冲器内部无残留耗材（避免断料残留在内部）。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/078.png)

- **手动模式：**当 AMS 中无耗材时，可手动调整 AMS 与挤出机的配对关系。若 AMS 已进料至挤出机，则该 AMS 图标为灰色（如下图中的 AMS-A），并且无法修改配对关系。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/081.png)

3. **AMS 烘干：**同上“烘干/湿度”。

### 6. **指南**

对界面操作和耗材的安装与进料进行教学。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/080.png)

## 设置

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/071.png)

### 1. **账号**

用 Bambu Handy 扫描二维码，即可登入账号。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/072.png)

### 2. **Wi-Fi**

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/073.png)

### 3. **USB 存储**

- **存储：**显示 U 盘已使用容量和该 U 盘的最大容量；
- **弹出：**点击“弹出”，可将 U 盘安全弹出；
- **格式化外部存储：**可将 U 盘存储格式化。一旦重设，存储将无法恢复。

> 注：U 盘规格要求和使用建议请参考 [U 盘规格要求和使用建议](../../h2/manual/usb-pecifications-and-usage-recommendations.md)。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/076.png)

### 4. **固件**

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/077.png)

### 5. **校准**

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/074.png)

1. **打印校准**

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/101.png)

- **电机降噪：**减少打印过程中电机产生的噪音，特别是在进行长时间或高速打印时。通过优化电机的运行算法和控制策略，不仅能降低噪音，还能提升打印表面的光滑度，从而改善最终打印效果。
- **振动补偿：** 在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。尤其在打印复杂或细致模型时，通过此校准能够有效防止因震动引起的误差，确保每层都准确无误地完成。
- **自动热床调平：**通过智能算法调整喷嘴与打印板之间的距离，确保每个角落的间隙一致，能够有效避免因热床不平整导致的打印缺陷，从而提高打印精度。
- **高温热床调平：**使用 ABS/ASA/PC/PA 等高温耗材打印前，进行高温热床校准，能够确保热床在高温环境下保持稳定，有效防止首层翘曲或粘附不良，提高首层打印质量。
- **喷嘴偏移校准：**如果两个喷嘴的定位出现偏移，则可能导致打印过程中模型出现错位或层移现象。在打印过程中发现切换喷嘴后模型出现明显的层移时，建议进行一次喷嘴偏移校准。此过程利用工具头内的涡流传感器和热床后面的喷嘴偏移校准传感器，确保喷嘴位置的准确性，以提高打印质量和精确度。通过有效的校准，可以减少打印错误，确保每个层次的完美对齐。

2. **高精度喷嘴偏移校准：**将一深一浅两种耗材分别进料至两个喷嘴，利用 AI 视觉检测技术，精确校准两个喷嘴在 XY 方向上的偏移量，以提高打印质量和精度。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/099.png)

3. **实况摄像头校准：**通过识别热床上的特定标记，校准实况摄像头的位置和角度，减少因摄像头视角偏差和位置错误导致的检测误差，从而显著提升其检测精度，实现更高的图像捕捉质量。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/100.png)

4. **运动精度校准：**专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/098.png)

5. **首层质量校准：**支持微调首层打印时喷嘴与热床间的距离，从而提升首层附着力与表面平整度，有效解决首层偏高或偏低导致的打印质量问题。

> 注意：该功能是为了满足用户不同场景差异化的调参需求，一般情况无需用到，建议按需使用。

![](https://public-cdn.bblmw.com/wiki/new/x2d/release_note/13-cn.png)

### 6. **工具箱**

|  |  |
| --- | --- |
|  |  |

1. **烘干耗材：**选择耗材类型，设置烘干温度及时长，对耗材进行烘干处理。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/096.png)

2. **光杆清洁：** 光杆的定期清洁可防止碎屑积累，确保设备正常运作并延长使用寿命。屏幕左侧进度条长度会随光杆的清洁程度减少；如果进度条变为红色，则需进行清洁，具体教程可通过右侧二维码获取。详情请参考：[X2D 定期清洁维护](../maintenance/periodic-maintenance.md)。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/092.png)

3. **丝杆润滑：**丝杆需要定期润滑，以确保热床上下移动运行平稳。详情请参考：[X2D 定期清洁维护](../maintenance/periodic-maintenance.md)。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/089.png)

4. **喷嘴冷拔维护：**当挤出电机在常规打印流量下频繁出现过载报错，则表示喷嘴阻力过大，急需清理；同时，由于 TPU 对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，建议在打印 TPU 前对喷嘴进行冷拔清理，以保证打印顺畅。喷嘴冷拔维护详情请参考：[X2D 喷嘴/热端堵塞清理指南](../maintenance/cold-pull-maintenance-hotend.md)。

|  |  |
| --- | --- |
|  |  |

5. **加热底座维护模式：**开启该功能后，即便未安装热端，加热底座仍可正常升温；升温完成后请务必注意操作安全，避免高温接触导致烫伤。
6. **新手引导：**可查看新手引导流程，快速完成首次打印。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/085.png)

### 7. **设置**

|  |  |  |
| --- | --- | --- |
|  |  |  |

1. **打印选项**：

- **炒面检测**：在打印过程中检测炒面问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **堆料检测**：在打印过程中检测废料槽堆积问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **裹头检测**：在打印过程中检测裹头问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/117.png)

- **类型检测：**若实际使用的打印板与切片文件中的打印板不匹配，则及时停止打印，避免打印失败。
- **偏移检测：**若打印板的标记未处于预定义范围内，打印机将自动停止打印，以避免打印板未放置或放置不当导致的打印异常。
- **丢步自动恢复**：当电机检测到位置偏移（丢步）时，X、Y 和 Z 轴会重新定位，并回到偏移前的位置继续执行未完成的 G-code，以保证打印质量。
- **缓存远程打印文件到外部存储中**：通过云端发起的打印，打印文件将缓存到外部存储中。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/116.png)

- **运动精度增强**：专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。
- **打印结束时净化空气：**安装外排风扇后，打开该按钮，支持结束打印后自动开始净化腔内气体，通过外排风扇排出机箱残留气体。
- **打印状态快照：**打印任务完成后，打印机会自动拍摄打印件照片并上传至云端，该照片将同步显示在 Bambu Handy 的打印完成弹窗中。
- **异物检测：**发起打印任务后，实况摄像头会检查打印平台是否存在异物；若检测到异物，则无法开启打印。
- **打印件位移检测：**在打印过程中，如果打印件出现倒塌或位移现象，则会进行相关报错。

|  |  |
| --- | --- |
|  |  |

> 注：有关智能检测的更多内容请参考：[X2D 智能检测介绍](intelligent-detection.md)。

2. **AMS 选项：**

- **插入耗材时读取：**在插入耗材预上料后，AMS 会进行 RFID 读取操作。
- **开机时读取**：每次重启打印机时，AMS 会自动读取插入的耗材信息，并且读取过程中会转动耗材。
- **AMS 自动续料**：当 AMS 某个槽的耗材用完时，可自动切换到其他槽位上属性完全相同的耗材。这些属性包括品牌、类型、颜色和打印温度等。请确保在打印前配置好所有耗材的信息，以满足自动续料的要求。
- **重新排序 AMS**：每个 AMS 都会分配一个顺序，并在屏幕上显示。分配 AMS ID 的目的是方便识别它们之间的连接。分配 ID 的逻辑为：直接连接到打印机的是 AMS-A，连接到 AMS-B 的是 AMS-C，以此类推。如果需要重新排序 AMS，可以点击“重置”，即可重置 AMS 的顺序信息。重置完成后，请按需依次连接 AMS 进行排序。

|  |  |
| --- | --- |
|  |  |

3. **安全选项：**

- **开门检测**：开启后，打印机将检测前玻璃门是否打开，可选择在门打开时触发通知或暂停打印。
- **空闲加热保护：**开启此选项后，若打印机处于空闲状态且需对热端、热床进行升温，加热将在运行 5 分钟后自动停止，以避免干烧风险。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/106.png)

4. **录像：**设置录像的清晰度。清晰度越高，所需的存储空间越大。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/105.png)

5. **屏幕亮度：**设置屏幕显示的亮度。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/110.png)

6. **自动休眠：**选择打印机自动休眠的时长。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/111.png)

7. **声音：**如果开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。
8. **低功率模式：**在打印机供电功率受限的情况下，可通过延长热床升温时间，降低最大功率。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/107.png)

9. **机箱灯模式：**可根据实际的使用需要选择手动模式或节能模式。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/103.png)

10. **语言：**选择打印机屏幕的显示语言。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/102.png)

11. **设备和序列号：**查看打印机设备名、设备使用时间和序列号。选择是否加入“用户体验改进计划”，加入后可将机器数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/104.png)

12. **仅局域网：**开启仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/131.png)

13. **导出日志到外部存储：**可根据需求，选择是否导出所有打印日志、关键照片（判断炒面等问题）和 G-code（判断打印质量问题）。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/008.png)

14. **恢复出厂设置：**将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/128.png)

15. **认证信息：**可在此处查看机器的认证信息电子标签页。

![](https://public-cdn.bblmw.com/wiki/new/x2d/manual/screen-operation/129.png)

## 助手

如果打印机出现故障，此处将会显示报错信息及可能的错误原因。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
