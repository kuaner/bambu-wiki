---
path: zh/p2s/manual/screen-operation
title: "P2S 屏幕操作指南"
description: "本指南将介绍 P2S 打印机的屏幕按键功能。"
tags: []
created: 2025-10-14T13:13:22.972Z
updated: 2026-06-02T06:09:51.995Z
source: https://wiki.bambulab.com/zh/p2s/manual/screen-operation
---

本指南将介绍 P2S 打印机的屏幕按键功能。

## 主页

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**耗材**、**设置**和 **HMS**；右侧为**打印文件**、**喷嘴温度、网络设置**和**HMS**，点击图标可快速跳转至对应的控制界面。  
![homepage-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/homepage-cn.png)

## 控制

![control--cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/control--cn.png)

### 1. **空调系统**

- **冷却模式**：在打印 PLA 等低温耗材时，打印机处于外部吸风冷却模式。在该模式下，右侧的辅助部件冷却风扇直接将外部环境的冷空气吸进打印机腔体内部，降低腔体内温度，腔体内原有的热空气会通过打印机背板散热孔和吐料组件缝隙排出。

![air-condition-cn-1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/air-condition-cn-1.png)

- **腔温保持模式**：在该模式下，打印机通过热床与热端加热后的高温辐射加热腔体内空气；辅助部件冷却风扇不再从外部吸取冷空气，而与空气滤芯共同形成内循环，在保证腔体内部热空气均匀性的同时对空气进行过滤和净化。

![air-condition-cn-1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/air-condition-cn-2.png)

- **部件冷却风扇：**安装在工具头上，用于确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。

![cooling-en.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/part-cooling-fan--cn.png)

- **右侧辅助风扇：**安装在机腔内右侧，能为高速打印提供更好的冷却条件。

![cooling-en.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/heat--cn.png)

### 2. **速度**

设置打印速度模式。

- **狂暴**：正常打印速度和加速度的 166%
- **运动**：正常打印速度和加速度的 124%
- **标准**：正常打印速度和加速度
- **静音**：正常打印速度和加速度的 50%

![sppeed-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/sppeed-cn.png)

### 3. **运动**

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。

![](https://wiki.bambulab.com/h2/manual/screen-operation/xyz.png)

### 4. **喷嘴和挤出机**

![nozzle-cn-1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/nozzle-cn-1.png)

1. **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。如果挤出机的料管中显示了进料的耗材颜色，则表示挤出机的霍尔开关检测到有耗材进入。

![red_dot.jpg](https://wiki.bambulab.com/p2s/manual/screen/red_dot.jpg)

2. **喷嘴温度**：输入数值，设置喷嘴温度。

![nozzle-temp--en.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/nozzle-temp--cn.png)

3. **喷嘴类型**：可手动设置喷嘴的类型、材质及直径。

![](https://wiki.bambulab.com/h2/manual/screen-operation/penzuixinxi.png)

### 5. **腔温**

P2S 的腔体温度会根据热床设定温度被动升高，无法进行手动调温。

### 6. **热床**

输入数值，设置热床温度。

![heatbed-temp-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/heatbed-temp-cn.png)

### 7. **照明**

点击此按钮可控制左侧及前侧的 LED 补光灯。

![20250909-100033.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/20250909-100033.jpg)

## 耗材

![filament-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/filament-cn.png)

### 1. **料盘**

点击任一料盘图标，可进行耗材编辑、进退料和 RFID 重读操作；

![filament-edit--cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/filament-edit--cn.png)

- **编辑：**如果 AMS 已通过 RFID 识别该料盘信息，可在此处查看料盘信息，但无法修改耗材参数；如果未读取 RFID，则可在此处修改耗材信息。

|  |  |
| --- | --- |
| 已读取 RFID | 未读取 RFID |

- **进料：**点击按钮，AMS 2 Pro 会自动将耗材进料至挤出机；
- **重读：**点击按钮，AMS 2 Pro 会重新读取该槽位的 RFID。

### 2. **烘干和湿度**

可查看 AMS 内部的湿度和温度，也可在此处对耗材进行烘干。

> 注：也可在设置 > 工具箱 > 烘干耗材中开启烘干功能。

![](https://wiki.bambulab.com/h2/manual/screen-operation/drying.png)

如果连接多台 AMS 2 Pro/HT，可点击左上角图标切换不同设备，查看每台 AMS 的实时湿度和温度数据，或启动烘干。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-3.png)

### 3. **外挂料盘**

点击外挂料盘图标，可进行耗材编辑和进退料操作。

![20250908-183203.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/20250908-183203.jpg)

### 4. **工具**

![20250908-183304.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/20250908-183304.jpg)

1. **自动续料**：该功能允许用户查看哪些槽位的耗材可以相互续料。当耗材的品牌、类型和颜色完全相同时，系统将建立自动续料关系。当前耗材用完时，打印机会自动切换到相同属性的耗材继续打印。

> 注意：当两个相同耗材来自同一个挤出机连接的 AMS 时，才能形成续料关系，即左对左，右对右。如果两个耗材来自不同的挤出机，则无法建立续料关系。

![](https://wiki.bambulab.com/h2/manual/screen-operation/cn-autorefill.png)

2. **AMS 烘干：** 同上“烘干和湿度”。

![](https://wiki.bambulab.com/h2/manual/screen-operation/drying.png)

### 5. **指南**

对进料操作进行说明：选择特定槽位，点击料盘图标，再点击进料按钮，即可触发自动进料。

![guide-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/guide-cn.png)

## 设置

![2025-09-24_10_46_49.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/2025-09-24_10_46_49.png)

### 1. **账号**

用 Bambu Handy 扫描二维码，即可登入账号。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-10.png)

### 2. **Wi-Fi**

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-9.png)

### 3. **USB 存储**

- **存储：**显示 U 盘已使用容量和该 U 盘的最大容量；
- **弹出：**点击“弹出”，可将 U 盘安全弹出；
- **格式化外部存储：**可将 U 盘存储格式化。一旦重设，存储将无法恢复。

> U 盘规格要求和使用建议请参考：[U 盘规格要求和使用建议](../../h2/manual/usb-pecifications-and-usage-recommendations.md)

![](https://wiki.bambulab.com/h2/manual/screen-operation/usb.png)

### 4. **固件**

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![firmware-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/firmware-cn.png)

### 5. **校准**

![calibration-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/calibration-cn.png)

1. **打印校准**：包括电机降噪、振动补偿、高温热床调平和喷嘴偏移校准。

![nozzle.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/nozzle.png)

- **电机降噪：**减少打印过程中电机产生的噪音，特别是在进行长时间或高速打印时。通过优化电机的运行算法和控制策略，不仅能降低噪音，还能提升打印表面的光滑度，从而改善最终打印效果。
- **振动补偿：** 在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。尤其在打印复杂或细致模型时，通过此校准能够有效防止因震动引起的误差，确保每层都准确无误地完成。
- **自动热床调平：**通过智能算法调整喷嘴与打印板之间的距离，确保每个角落的间隙一致，能够有效避免因热床不平整导致的打印缺陷，从而提高打印精度。
- **高温热床调平：**使用 ABS/ASA/PC/PA 等高温耗材打印前，进行高温热床校准，能够确保热床在高温环境下保持稳定，有效防止首层翘曲或粘附不良，提高首层打印质量。

- **触碰裹头检测校准：** 校准裹头检测的起始位置，以保障其检测准确性。P2S 打印机初始化时会自动做一次触碰裹头检测校准。为了提高裹头检测的准确性，建议在拆装热床或发现裹头检测误报后进行一次触碰裹头检测校准。具体请参考：[Bambu Studio 触碰裹头检测功能介绍](../../software/bambu-studio/nozzle-clumping-detection-by-probing.md)。

2. **实况摄像头校准：**通过识别热床上的特定标记，校准实况摄像头的位置和角度，减少因摄像头视角偏差和位置错误导致的检测误差，从而显著提升其检测精度，实现更高的图像捕捉质量。

![](https://wiki.bambulab.com/h2/manual/screen-operation/liveview.png)

### 6. **工具箱**

![toolbox-cn1.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/toolbox-cn1.png)

1. **烘干耗材：**选择耗材类型，设置烘干温度及时长，对耗材进行烘干处理。

![drying-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/drying-cn.png)

2. **光杆清洁：** 光杆的定期清洁可防止碎屑积累，确保设备正常运作并延长使用寿命。屏幕左侧进度条长度会随光杆的清洁程度减少；如果进度条变为红色，则需进行清洁，具体教程可通过右侧二维码获取。详情请参考：[P2S 定期清洁维护建议](../maintenance/period-maintenance.md)。

![cleaning.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/cleaning.png)

3. **丝杆润滑：** 丝杆需要定期润滑，以确保热床上下移动运行平稳。详情请参考：[P2S XYZ 轴清洁润滑](../maintenance/lubricate-x-y-z-axis.md)。

![lubricating.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/lubricating.png)

4. **喷嘴冷拔维护：**当挤出电机在常规打印流量下频繁出现过载报错，则表示喷嘴阻力过大，急需清理；同时，由于 TPU 对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，建议在打印 TPU 前对喷嘴进行冷拔清理，以保证打印顺畅。喷嘴冷拔维护详情请参考：[P2S 喷嘴堵塞清理指南](https://wiki.bambulab.com/zh/p2s/maintenance/cold-pull-maintenance-hotend#h-2-%E5%86%B7%E6%8B%94)。

![cooling-pull-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/cooling-pull-cn.png)

5. **加热底座维护模式：** 开启该功能后，即便未安装热端，加热底座仍可正常升温；**升温完成后请务必注意操作安全，避免高温接触导致烫伤**。

### 7. **设置**

|  |  |
| --- | --- |
|  |  |

1. **打印选项**：

|  |  |
| --- | --- |
|  |  |

- **炒面检测**：在打印过程中检测炒面问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **堆料检测**：在打印过程中检测废料槽堆积问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **裹头检测**：在打印过程中检测裹头问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。

> 有关智能检测的更多内容，请参考：[P2S 视觉检测功能介绍](intelligent-detection.md)。

- **打印板检测**：通过检测打印板标记，来识别打印板类型，以确认是否使用了支持识别的打印板类型。
- **丢步自动恢复**：当电机检测到位置偏移（丢步）时，X、Y 和 Z 轴会重新定位，并回到偏移前的位置继续执行未完成的 G-code，以保证打印质量。

2. **AMS 选项：**

|  |  |
| --- | --- |
|  |  |

- **插入耗材时读取：**在插入耗材预上料后，AMS 会进行 RFID 读取操作。
- **开机时读取**：每次重启打印机时，AMS 会自动读取插入的耗材信息，并且读取过程中会转动耗材。
- **AMS 自动续料**：当 AMS 某个槽的耗材用完时，可自动切换到其他槽位上属性完全相同的耗材。这些属性包括品牌、类型、颜色和打印温度等。请确保在打印前配置好所有耗材的信息，以满足自动续料的要求。
- **重新排序 AMS**：每个 AMS 都会分配一个顺序，并在屏幕上显示。分配 AMS ID 的目的是方便识别它们之间的连接。分配 ID 的逻辑为：直接连接到打印机的是 AMS-A，连接到 AMS-B 的是 AMS-C，以此类推。如果需要重新排序 AMS，可以点击“重置”，即可重置 AMS 的顺序信息。重置完成后，请按需依次连接 AMS 进行排序。

3. **安全选项：**

![safety-cn--cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/safety-cn--cn.png)

- **开门检测**：开启后，打印机将检测前玻璃门是否打开，可选择在门打开时触发通知或暂停打印。
- **空闲加热保护**：开启此选项后，若打印机处于空闲状态且需对热端、热床进行升温，加热将在运行 5 分钟后自动停止，以避免干烧风险。

4. **录像：**设置录像的清晰度。清晰度越高，所需的存储空间越大。

![video-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/video-cn.png)

5. **声音：**如果开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。
6. **自动休眠：**选择打印机自动休眠的时长。

![auto-sleep-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/auto-sleep-cn.png)

7. **机箱灯模式：**可根据实际的使用需要选择手动模式或节能模式。

![light-cn11.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/light-cn11.png)

8. **语言：**选择打印机屏幕的显示语言。

![language--cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/language--cn.png)

9. **设备和序列号：**查看打印机设备名、设备使用时间和序列号。选择是否加入“用户体验改进计划”，加入后可将机器数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

![20250909-102154.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/20250909-102154.jpg)

10. **仅局域网：**开启仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-14.png)

11. **导出日志到外部存储：**可根据需求，选择是否导出所有打印日志、关键照片（判断炒面等问题）和 G-code（判断打印质量问题）。

![](https://wiki.bambulab.com/h2/manual/screen-operation/export.png)

12. **恢复出厂设置：**将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![20250909-103305.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/20250909-103305.png)

## 助手

如果打印机出现故障，此处将会显示报错信息。

![hms-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/hms-cn.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
