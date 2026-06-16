---
path: zh/h2s/manual/screen-operation
title: "H2S 屏幕操作指南"
description: "本指南旨在介绍 H2S 打印机屏幕按钮和操作功能。"
tags: []
created: 2025-08-26T13:25:14.151Z
updated: 2026-06-04T09:47:42.936Z
source: https://wiki.bambulab.com/zh/h2s/manual/screen-operation
---

## H2S

本指南将介绍 H2S 打印机的屏幕按键功能。

如果您拥有 H2SL 打印机，可以[点击此处](#h2s-%E6%BF%80%E5%85%89%E6%A8%A1%E7%BB%84)了解更多关于 H2S 激光模组的信息，或[点击此处](#h2s-%E5%88%80%E5%88%87%E6%A8%A1%E7%BB%84)了解更多关于 H2S 刀切模组的信息。

## 主页

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**耗材**、**设置**和 **HMS**；右侧为**打印文件**、**喷嘴温度、网络设置**和**HMS**，点击图标可快速跳转至对应的控制界面。

![extruder.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/extruder.png)

## 控制

![screenshot_20260603_155052.png](https://wiki.bambulab.com/h2s/manual/screen-operation/screenshot_20260603_155052.png)

### 1. **空调系统**

可根据耗材的不同选择合适的空调系统。

- **冷却模式**：适合打印 PLA/TPU 等**耐热性较低的耗材；**在此模式下，腔体加热循环风扇保持关闭状态。在冷却模式下，可开启自适应空气循环系统的过滤功能，该功能主要用于低温耗材打印过程中，将空气通过过滤器过滤再进行排出。

![空调系统-过滤.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E7%A9%BA%E8%B0%83%E7%B3%BB%E7%BB%9F-%E8%BF%87%E6%BB%A4.png)

- **腔温保持模式**：适合打印 ABS/ASA/PC/PA 等**具备高耐热性的耗材。**腔体加热时，系统会自动切换至腔温保持模式；在此模式下，腔体加热循环风扇将自动开启，辅助部件冷却风扇将保持关闭状态。

![fan.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/fan.png)

- **部件冷却风扇：**安装在工具头上，用于确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。

![abcd.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/abcd.png)

- **辅助部件冷却风扇：**安装在机腔内左侧，能为高速打印提供更好的冷却条件。

![](https://wiki.bambulab.com/h2/manual/screen-operation/fuzhubujian.png)

- **腔体外排风扇：** 安装在打印机右内衬上，当腔体冷却时，打印机循环系统会切换至冷却模式，腔体外排风扇转速会随腔温升高而加快。如果当前打印机的腔温不高，且机箱内打印耗材的散热需求较低，则腔体外排风扇的转速会降至 30%。

![](https://wiki.bambulab.com/h2/manual/screen-operation/5.png)

- **腔体加热循环风扇：**安装在打印机右内衬上，当腔体加热时，打印机会自动切换至腔温保持模式。设置腔温后，腔温加热器（由 PTC 和腔体加热循环风扇组成）开始工作，PTC 全功率加热，风扇全速运转。当腔体温度达到目标值后，风扇转速不变，PTC 功率下降，以维持恒定温度。

![](https://wiki.bambulab.com/h2/manual/screen-operation/7.png)

- **腔温：**根据打印耗材的不同，可设置合适的腔温。低腔温适合打印 PLA、PETG 等耗材；高腔温适合打印 ABS 等的易翘曲耗材。

![qiangwen.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/qiangwen.png)

### 2. **速度**

设置打印速度模式。

- **狂暴**：正常打印速度和加速度的 166%
- **运动**：正常打印速度和加速度的 124%
- **标准**：正常打印速度和加速度
- **静音**：正常打印速度和加速度的 50%

![sudu.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/sudu.png)

### 3. **运动**

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。

![](https://wiki.bambulab.com/h2/manual/screen-operation/xyz.png)

### 4. **喷嘴和挤出机**

![喷嘴和挤出机-h2s.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E5%96%B7%E5%98%B4%E5%92%8C%E6%8C%A4%E5%87%BA%E6%9C%BA-h2s.png)

1. **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。如果挤出机内显示耗材颜色，则表示挤出机的霍尔开关检测到有耗材进入。

![挤出机显示耗材颜色.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E6%8C%A4%E5%87%BA%E6%9C%BA%E6%98%BE%E7%A4%BA%E8%80%97%E6%9D%90%E9%A2%9C%E8%89%B2.png)

2. **喷嘴类型**：可手动设置喷嘴的类型、材质及直径。

![喷嘴类型.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E5%96%B7%E5%98%B4%E7%B1%BB%E5%9E%8B.png)

3. **喷嘴温度**：输入数值，设置喷嘴温度。

![喷嘴温度.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E5%96%B7%E5%98%B4%E6%B8%A9%E5%BA%A6.png)

### 5. **腔温**

同上述腔温。

### 6. **热床**

输入数值，设置热床温度。

![热床.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E7%83%AD%E5%BA%8A.png)

### 7. **照明**

点击此按钮可控制 LED 补光灯。

![冷却3.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E5%86%B7%E5%8D%B43.png)  
![led3.jpg](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/led3.jpg)

## 耗材

![ams-h2s.png](https://wiki.bambulab.com/h2s/manual/screen-operation/ams-h2s.png)

### 1. **料盘**

点击任一料盘图标，可进行耗材编辑、进退料和 RFID 重读操作；

![screenshot_20260603_155425.png](https://wiki.bambulab.com/h2s/manual/screen-operation/screenshot_20260603_155425.png)

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

![screenshot_20260603_155107.png](https://wiki.bambulab.com/h2s/manual/screen-operation/screenshot_20260603_155107.png)

### 4. **工具**

![xvliaoo.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/xvliaoo.png)

1. **自动续料**：该功能允许用户查看哪些槽位的耗材可以相互续料。当耗材的品牌、类型和颜色完全相同时，系统将建立自动续料关系。当前耗材用完时，打印机会自动切换到相同属性的耗材继续打印。

![zzidongxvliao.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/zzidongxvliao.png)

2. **AMS 烘干：** 同“2. 烘干和湿度”

### 5. **指南**

对进料操作进行说明：选择特定槽位，点击料盘图标，再点击进料按钮，即可触发自动进料。

![](https://wiki.bambulab.com/h2/manual/screen-operation/guidecn.png)

> 耗材页面更多相关信息请参考：
>
> [AMS 2 Pro 工作流程和功能介绍](../../ams-2-pro/manual/setup-and-printting.md)
>
> [AMS HT工作流程和功能介绍](../../ams-ht/Intr-to-ams-ht-workflow-and-features.md)

## 设置

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-11.png)

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

> U 盘规格要求和使用建议请参考：[H2D U 盘规格要求和使用建议](../../h2/manual/usb-pecifications-and-usage-recommendations.md)

![](https://wiki.bambulab.com/h2/manual/screen-operation/usb.png)

### 4. **固件**

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![gujian.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/gujian.png)

### 5. **校准**

![jiaozhun.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/jiaozhun.png)

1. **打印校准**：包括电机降噪、振动补偿、高温热床调平和自动热床调平。

![打印校准.png](https://wiki.bambulab.com/h2s/manual/screen-operation/%E6%89%93%E5%8D%B0%E6%A0%A1%E5%87%86.png)

- **电机降噪：**减少打印过程中电机产生的噪音，特别是在进行长时间或高速打印时。通过优化电机的运行算法和控制策略，不仅能降低噪音，还能提升打印表面的光滑度，从而改善最终打印效果。
- **振动补偿：** 在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。尤其在打印复杂或细致模型时，通过此校准能够有效防止因震动引起的误差，确保每层都准确无误地完成。
- **自动热床调平：**通过智能算法调整喷嘴与打印板之间的距离，确保每个角落的间隙一致，能够有效避免因热床不平整导致的打印缺陷，从而提高打印精度。
- **高温热床调平：**使用 ABS/ASA/PC/PA 等高温耗材打印前，进行高温热床校准，能够确保热床在高温环境下保持稳定，有效防止首层翘曲或粘附不良，提高首层打印质量。

- **触碰裹头检测校准**：用于检测裹头检测起始位置是否准确，以此保证打印过程中裹头识别的准确性。具体请参考：[Bambu Studio 触碰裹头检测功能](../../software/bambu-studio/nozzle-clumping-detection-by-probing.md)

2. **实况摄像头校准：**通过识别热床上的特定标记，校准实况摄像头的位置和角度，减少因摄像头视角偏差和位置错误导致的检测误差，从而显著提升其检测精度，实现更高的图像捕捉质量。

![](https://wiki.bambulab.com/h2/manual/screen-operation/liveview.png)

3. **运动精度校准：**专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。

> 运动精度校准详情请参考：[运动精度校准](../../h2/manual/motion-accuracy.md)

![](https://wiki.bambulab.com/h2/manual/screen-operation/motion.png)

### 6. **工具箱**

![工具箱.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E5%B7%A5%E5%85%B7%E7%AE%B1.png)

- **烘干耗材：**选择耗材类型，设置烘干温度及时长，对耗材进行烘干处理。

![烘干.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E7%83%98%E5%B9%B2.png)

- **激光模组清洁：**激光模组的定期清洁可防止粉末和碎屑积累，确保设备正常运作并延长使用寿命。机器会根据 Bambu Suite 中的总工程时间和激光任务类型评估打印机的污染程度。屏幕左侧的绿色进度条长度会随着激光模组的清洁程度减少；如果进度条变为红色并显示“需要立即进行清洁”，则需进行清洁，具体教程可通过右侧二维码获取。详情请参考：[10w 激光模组定期维护建议](../../h2/maintenance/laser-module.md)。

![](https://wiki.bambulab.com/h2/manual/screen-operation/jiguangmozuqingjie.png)

- **喷嘴冷拔维护：**当挤出电机在常规打印流量下频繁出现过载报错，则表示喷嘴阻力过大，急需清理；同时，由于 TPU 对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，建议在打印 TPU 前对喷嘴进行冷拔清理，以保证打印顺畅。喷嘴冷拔维护详情请参考：[H2S 喷嘴冷拔维护清理](../maintenance/nozzle-cold-pull-maintenance-and-cleaning.md)。

![screenshot_20260603_155503.png](https://wiki.bambulab.com/h2s/manual/screen-operation/screenshot_20260603_155503.png)

- **XYZ轴清洁：** 定期对打印机的XYZ轴进行清理和维护，可以保证打印精度和设备稳定运行。

![xxyz.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/xxyz.png)

- **丝杆润滑：** 定期对打印机进行丝杆润滑，能降低摩擦、延长寿命并保证运动精度。

![丝杆.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E4%B8%9D%E6%9D%86.png)

### 7. **设置**

|  |  |
| --- | --- |
|  |  |

1. **打印选项**：

|  |  |
| --- | --- |
|  |  |

- **AI 打印监控**：在打印过程中检测炒面、废料槽堆积以及裹头问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。
- **打印板检测**：检测打印板标记。如果标记不在预定义范围内，或与切片文件不符，打印机将停止打印，可避免未放置或放错打印板的情况。

> 有关视觉检测的更多内容，请参考：[H2S视觉检测介绍](../../h2/manual/h2s-visual-detection.md)。

- **丢步自动恢复**：当电机检测到位置偏移（丢步）时，X、Y 和 Z 轴会重新定位，并回到偏移前的位置继续执行未完成的 G-code，以保证打印质量。
- **开门检测**：开启后，打印机将检测前玻璃门是否打开，可选择在门打开时触发通知或暂停打印。
- **缓存远程打印文件到外部存储中**：通过云端发起的打印，打印文件将缓存到外部存储中。
- **运动精度增强**：专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。

2. **AMS 选项：**

|  |  |
| --- | --- |
|  |  |

- **插入耗材时读取：**在插入耗材预上料后，AMS 会进行 RFID 读取操作。
- **开机时读取**：每次重启打印机时，AMS 会自动读取插入的耗材信息，并且读取过程中会转动耗材。
- **剩余容量估计**：在读取 RFID 过程时对耗材进行余料估算。开启该功能后，会对 RFID 进行两次读取，分别获取耗材信息和估算剩余量。在读取完耗材的 RFID 和余量信息后，可以在每个槽位上方查看耗材名称，耗材名称下方的小横条中显示的就是估算出来的耗材余量。

![xvliao1.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/xvliao1.png)

- **AMS 自动续料**：当 AMS 某个槽的耗材用完时，可自动切换到其他槽位上属性完全相同的耗材。这些属性包括品牌、类型、颜色和打印温度等。请确保在打印前配置好所有耗材的信息，以满足自动续料的要求。
- **重新排序 AMS**：每个 AMS 都会分配一个顺序，并在屏幕上显示。分配 AMS ID 的目的是方便识别它们之间的连接。分配 ID 的逻辑为：直接连接到打印机的是 AMS-A，连接到 AMS-B 的是 AMS-C，以此类推。如果需要重新排序 AMS，可以点击“重置”，即可重置 AMS 的顺序信息。重置完成后，请按需依次连接 AMS 进行排序。

3. **录像：**设置录像的清晰度。清晰度越高，所需的存储空间越大。
4. **声音：**如果开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。
5. **自动休眠：**选择打印机自动休眠的时长。

![](https://wiki.bambulab.com/h2/manual/screen-operation/autosleep.png)

6. **机箱灯模式：**可根据实际的使用需要选择手动模式或节能模式。

![](https://wiki.bambulab.com/h2/manual/screen-operation/chamberlight.png)

7. **状态指示灯：**用于提示打印机健康状态和打印任务状态。

![氛围灯2.jpg](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E6%B0%9B%E5%9B%B4%E7%81%AF2.jpg)

8. **语言：**选择打印机屏幕的显示语言。

![](https://wiki.bambulab.com/h2/manual/screen-operation/lan-cutting-cn.png)

9. **设备和序列号：**查看打印机设备名、设备使用时间和序列号。选择是否加入“用户体验改进计划”，加入后可将机器数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

|  |  |
| --- | --- |
|  |  |

10. **仅局域网：**开启仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-14.png)

11. **导出日志到外部存储：**可根据需求，选择是否导出所有打印日志、关键照片（判断炒面等问题）和 G-code（判断打印质量问题）。

![](https://wiki.bambulab.com/h2/manual/screen-operation/export.png)

12. **恢复出厂设置：**将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![](https://wiki.bambulab.com/h2/manual/screen-operation/factory.png)

## 助手

如果打印机出现故障，此处将会显示报错信息。

![](https://wiki.bambulab.com/h2/manual/screen-operation/hmscnpage.png)

## 介绍

本指南旨在介绍安装激光模组和刀切模组的 H2S 打印机屏幕按键及操作功能。

> 注意：由于 H2S 激光/刀切模组不涉及“耗材”界面，本文将不作详细解释。

## H2S 激光模组

### 主页

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**文件夹**、**设置**和 **HMS**；右侧为**打印文件**、**激光模组**、**网络设置**和**HMS**，点击图标能快速跳转至对应的控制界面。

![homee.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/homee.png)

### 控制

![控制_(1).png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E6%8E%A7%E5%88%B6_(1).png)

#### 1. **外排风扇**

安装在打印机右内衬上，当腔体冷却时，打印机循环系统会切换至冷却模式，腔体外排风扇转速会随腔温升高而加快。如果当前打印机的腔温不高，且机箱内打印耗材的散热需求较低，则腔体外排风扇的转速会降至 30%。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/qiangtiwaipaifengshan.png)

#### 2. 主动气流辅助

在主动气流辅助模块工作时，机器会实时检测其状态，当状态异常时会报错提示用户。打开主动气流辅助，有助于提高雕刻质量，还能在加工一些材料时避免热量堆积导致的起火风险。

#### 3. 运动

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/xyz.png)

#### 4. 俯视摄像头

显示俯视摄像头状态。如果俯视摄像头未安装或未进行初始化，则会显示“未安装”或“尚未初始化”。

|  |  |
| --- | --- |
| 未安装 | 尚未初始化 |

#### 5. 工具头

显示激光模组功率类型及状态。如果激光模组未进行初始化，则会提示“尚未初始化”。

![工具头未初始8.jpg](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E5%B7%A5%E5%85%B7%E5%A4%B4%E6%9C%AA%E5%88%9D%E5%A7%8B8.jpg)

#### 6. 急停按钮和安全钥匙

显示急停按钮和安全钥匙是否安装。如果某一配件未安装，则会显示“未安装”。

![急停按钮8.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E6%80%A5%E5%81%9C%E6%8C%89%E9%92%AE8.png)

#### 7. **火焰安全**

![火焰安全1.png](https://wiki.bambulab.com/h2/h2s/manual/%E7%81%AB%E7%84%B0%E5%AE%89%E5%85%A81.png)

1. **温度：**可实时监控机箱内的工具头温度、机箱温度和热床温度。
2. **火焰安全状态：**当机器发起激光任务时，火焰检测功能将自动开启，会持续监控直至任务结束。“空闲”则表示未进行监控。
3. **火焰传感器：**包括机箱四个角落的红外传感器，以及激光模组自带的温度传感器和火焰传感器。如果传感器检测到火焰，屏幕上的传感器图标将闪烁红灯。
4. **自动灭火装置：**

![自动灭火装置.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E8%87%AA%E5%8A%A8%E7%81%AD%E7%81%AB%E8%A3%85%E7%BD%AE.png)

5. **实况摄像头：**实况摄像头会实时监控机箱内的加工过程，并结合 AI 算法分析图像特征，判断是否发生火灾。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-9.png)

6. **蜂鸣器：**测到任何火焰特征时，机器会通过蜂鸣器发出警报声，或在屏幕上弹出报警窗口，提醒用户介入处理。可在此处手动开关蜂鸣器，测试其是否正常。

> 火焰检测功能详情请参考：[H2D 火焰检测功能介绍](../../../en/h2/manual/flame-detection-feature.md)。

#### 8. **照明**

点击此按钮可控制 LED 补光灯。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-8.png)

### 设置

![主页.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E4%B8%BB%E9%A1%B5.png)

#### 1. 账号

用 Bambu Handy 扫描二维码，即可登入账号。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-4.png)

#### 2. Wi-Fi

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-5.png)

#### 3. **USB 存储**

- **存储：**显示 U 盘已使用容量和该 U 盘的最大容量；
- **弹出：**点击“弹出”，可将 U 盘安全弹出；
- **格式化外部存储：**可将 U 盘存储格式化。一旦重设，存储将无法恢复。

> U 盘规格要求和使用建议请参考：[H2D U 盘规格要求和使用建议](../../h2/manual/usb-pecifications-and-usage-recommendations.md)。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/usb.png)

#### 4. 固件

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![gujiann.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/gujiann.png)

#### 5. 挂载校准

每次打印机重新上电、电机重新启动或电机丢步等情况发生后，如果想要使用激光模组，就需要重新进行校准，目的是调整激光焦点位置，并使机器进入绝对位置模式。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/guazaijiaozhun.png)

需要校准时，HMS 页面会自动弹出提示。在校准前，请确保在热床上放置激光垫板。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/hmscode.png)

#### 6. 工具箱

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/toolboxlaser.png)

- **激光模组初始化**：在首次安装激光模组时，需要进行初始化，之后便无需再执行该过程。如果更换了另一个激光模组，则需要重新初始化。在进行此步骤时，需要在热床上放置激光平台和耗材（校准卡）。有关激光焦点标定的更多信息，请参考[激光焦点标定介绍](../../h2/manual/laser-focus-calibration-intro.md) 中的相关介绍。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/jiguangmozuchushihua.png)

- **激光模组挂载校准：**同上述“挂载校准”。
- **俯视摄像头初始化**：俯视摄像头出厂时已完成校准，用户可以直接使用。然而，由于运输或长期使用等原因，俯视摄像头的校准参数可能会逐渐失效。当您对激光加工的精度不满意时，可以触发俯视摄像头初始化，重新对摄像头进行校准。在进行摄像头初始化时，需要配合热床上的四个标记（marker）。因此，在此步骤中，热床上无需放置任何物品，务必确保热床上的标记暴露给俯视摄像头，以提高拍照正向的精度。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/fushishexiangtou.png)

- **激光模组清洁：**激光模组的定期清洁可防止粉末和碎屑积累，确保设备正常运作并延长使用寿命。机器会根据 Bambu Suite 中的总工程时间和激光任务类型评估打印机的污染程度。屏幕左侧的绿色进度条长度会随着激光模组的清洁程度减少；如果进度条变为红色并显示“需要立即进行清洁”，则需进行清洁，具体教程可通过右侧二维码获取。

> 激光模组清洁详情请参考：[10w 激光模组定期维护建议](../../h2/maintenance/laser-module.md)。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/jiguangmozuqingjie.png)

- **火焰安全：**同上述“火焰安全”。

#### 7. 设置

|  |  |
| --- | --- |
|  |  |

1. **录像：**选择开启或关闭录像功能。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/temp.png)

2. **声音：**如开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。
3. **自动休眠：**选择打印机自动休眠的时长。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-12.png)

4. **机箱灯模式：**可根据实际的使用需要选择手动模式或节能模式。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/chamberlight.png)

5. **状态指示灯：**如果机器报错，状态指示灯将闪红灯。

![氛围灯2.jpg](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E6%B0%9B%E5%9B%B4%E7%81%AF2.jpg)

6. **语言：**选择打印机屏幕的显示语言。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/lan-laser-cn.png)

7. **设备和序列号：**查看打印机设备名、设备使用时间和序列号。选择是否加入用户体验改进计划，加入后可将机器的数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

|  |  |
| --- | --- |
|  |  |

8. **仅局域网：**开启后仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-21.png)

9. **导出日志到外部存储：**可根据需求，选择是否导出所有打印日志、关键照片（判断激光雷达和炒面问题）和 G-code（判断打印质量问题）。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/export.png)

10. **恢复出厂设置：**将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/factory.png)

### 助手

如果打印机出现故障，此处将会显示报错信息。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/hmscode-1.png)

## H2S 刀切模组

### 主页

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**文件夹**、**设置**和 **HMS**；右侧为**打印文件**、**刀切模组**、**网络设置**和**HMS**，点击图标能快速跳转至对应的控制界面。

![主页2.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E4%B8%BB%E9%A1%B52.png)

### 控制

![cutcontrolcn.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/cutcontrolcn.png)

#### 1. 运动

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/xyz-1.png)

#### 2. 俯视摄像头

- 如果俯视摄像头未安装，则不会显示俯视摄像头图标。
- 如果安装到位了但未进行初始化，则会显示“尚未初始化”。

|  |  |
| --- | --- |
| 未显示图标 | 尚未初始化 |

#### 3. 工具头

显示刀切模组状态以及安装的模组类型，如果未进行校准，则会进行提示。

|  |  |
| --- | --- |
| 精细刀 | 笔 |

#### 4. 照明

点击照明按钮可控制 LED 补光灯。

![冷却3.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E5%86%B7%E5%8D%B43.png)  
![image_-_2025-04-23t180241.039.png](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image_-_2025-04-23t180241.039.png)

### 设置

![image-35.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/image-35.png)

#### 1. 账号

用 Bambu Handy 扫描二维码，即可登入账号。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-34.png)

#### 2. Wi-Fi

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-33.png)

#### 3. USB 存储

- **存储：**显示 U 盘已使用容量和该 U 盘的最大容量；
- **弹出：**点击“弹出”，可将 U 盘安全弹出；
- **格式化外部存储：**可将 U 盘存储格式化。一旦重设，存储将无法恢复。

> U 盘规格要求和使用建议请参考：[H2D U 盘规格要求和使用建议](../../h2/manual/usb-pecifications-and-usage-recommendations.md)。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/usb-1.png)

#### 4. 固件

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![firmm.png](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/firmm.png)

#### 5. 挂载校准

每次打印机重新上电时，都需要进行一次刀切模组挂载校准，目的是帮助刀切模组回中。为此，必须在热床上放置切割垫板，以确保校准过程的准确性。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/daoqieguazaijiaozhun.png)

#### 6. 工具箱

- **刀切模组挂载校准：**同上述挂载校准。
- **俯视摄像头初始化：**俯视摄像头出厂时已完成校准，用户可以直接使用。然而，由于运输或长期使用等原因，俯视摄像头的校准参数可能会逐渐失效。当您对激光加工的精度不满意时，可以触发俯视摄像头初始化，重新对摄像头进行校准。在进行摄像头初始化时，需要配合热床上的四个标记（marker）。因此，在此步骤中，热床上无需放置任何物品，务必确保热床上的标记暴露给俯视摄像头，以提高拍照正向的精度。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/fushishexiangtou-1.png)

- **激光模组清洁：**激光模组的定期清洁可防止粉末和碎屑积累，确保设备正常运作并延长使用寿命。机器会根据 Bambu Suite 中的总工程时间和激光任务类型评估打印机的污染程度。屏幕左侧的绿色进度条长度会随着激光模组的清洁程度减少；如果进度条变为红色并显示“需要立即进行清洁”，则需进行清洁，具体教程可通过右侧二维码获取。

> 激光模组清洁详情请参考：[10w 激光模组定期维护建议](../../h2/maintenance/laser-module.md)。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/jiguangmozuqingjie-1.png)

#### 7. 设置

|  |  |
| --- | --- |
|  |  |

1. **刀切选项：**

**开门检测：**如果启用开门检测，在刀切任务中若前门被打开，则会发出通知或暂停当前任务。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/daoqiexuaniangcn.png)

2. **录像：**选择开启或关闭录像功能。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/video-cutting-cn.png)

3. **声音：**如开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。
4. **自动休眠：**选择打印机自动休眠的时长。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/cut-autosleep-cn.png)

5. **机箱灯模式：** 根据实际的使用需要选择手动模式或节能模式。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/chamberlight-1.png)

6. **状态指示灯：**用于提示打印机健康状态和打印任务状态。

![氛围灯2.jpg](https://wiki.bambulab.com/h2/h2s/manual/screen-operation/%E6%B0%9B%E5%9B%B4%E7%81%AF2.jpg)

7. **语言：**选择打印机屏幕的显示语言。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/lan-cutting-cn.png)

8. **设备和序列号：**查看打印机设备名、设备使用时间和序列号。选择是否加入用户体验改进计划，加入后可将机器的数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

|  |  |
| --- | --- |
|  |  |

9. **仅局域网：**开启后仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/image-43.png)

10. **导出日志到外部存储：**可根据需求，选择是否导出所有打印日志、关键照片（判断激光雷达和炒面问题）和 G-code（判断打印质量问题）。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/export-1.png)

11. **恢复出厂设置：**将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/factory-1.png)

### 助手

如果打印机出现故障，此处将会显示报错信息。

![](https://wiki.bambulab.com/h2/manual/screen-operation/h2dl/daoqiemozuhms.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
