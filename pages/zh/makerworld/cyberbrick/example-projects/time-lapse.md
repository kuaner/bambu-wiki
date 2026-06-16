---
path: zh/makerworld/cyberbrick/example-projects/time-lapse
title: "延时摄影套件 使用指南"
description: "本页面介绍了延时摄影套件与打印机的连接、设置和相关技术参数。"
tags: ["cyberbrick", "makerworld"]
created: 2025-06-09T01:50:49.437Z
updated: 2026-06-11T04:14:16.759Z
source: https://wiki.bambulab.com/zh/makerworld/cyberbrick/example-projects/time-lapse
---

## 一 . 套件简介

延时摄影套件专为拓竹系列3D打印机研发设计，为外置摄影设备提供蓝牙快门、有线快门、机械舵机快门。打印机发送快门信号以触发外置摄影设备的快门操作，通过将每一层打印过程中捕捉到的静止图像合成视频，进而实现延时摄影效果。

### **核心板**

延时摄影套件的核心处理单元，内置蓝牙和WiFi功能，不仅适用于本套件，也可用于其他RC项目。通过两排针脚快速插拔，以便在不同的扩展板之间灵活切换。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-9.png)

### **扩展板**

核心板插接安装在扩展板上，为延时摄影提供必要的IO功能。延时摄影扩展板具备：一个2.5mm通用型快门线接口、一组舵机连接端口、两个打印机连接端口（4-pin 和 6-pin）、一个功能按键、一个RGB指示灯。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-8.png)

### **外壳**

两款3D打印外壳方案可供选择。其中一款采用滑盖式设计，便于快速打开核心板插件区域，轻松取出和更换核心板。若需要在多个设备间切换核心板，这款滑盖式外壳将是理想之选。若无需频繁更换核心板，那么固定顶盖的版本将更加适合。

##### 滑盖版本

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-7.png)

##### 固定盖版本

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-6.png)

##### IO接口说明

（1）打印机4pin接口； （2）AMS 6pin接口； （3）2.5mm快门线接口；

（4）舵机连接口； （5）多功能按钮 & 指示灯。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-5.png)

##### 固定方式

延时摄影套件配备了两套便捷的收纳固定方案，插接式固定和磁吸式固定，需要自行购置背胶和磁铁。

背胶规格：Rectangular Transparent Double-Sided Adhesive - NB008 / 透明双面胶 - NB008

磁铁规格：Round Magnet - CA005 / 圆形磁铁 - CA005

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image.png)

##### 外壳打印文件

耗材推荐：

Bambu PLA Basic Light Gray - 10104（浅灰色），外壳主体结构。

Bambu PLA Basic Dark Gray - 10105（深灰色），logo部分。

Bambu PETG Translucent - 32101（透明），多功能按钮，需要透光。

[延时摄影 20250316.3mf](https://makerworld.com/en/models/1409319-cyberbrick-time-lapse-kit#profileId-1462810)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-1.png)

盘01上的是滑盖版本文件，盘02上的是固定盖版本文件。根据你的具体需求，选择其中一盘进行打印。Logo和图标部分采用多色打印，由于仅涉及1-2层的颜色更换，换色不会耗费过多时间。

盘03为透明按钮文件，请使用透明PETG材料进行打印。按钮有更改填充模式以优化透明效果。请保留默认打印参数，以免影响打印效果。

盘04为磁吸底座文件，需要自行购置背胶和磁铁。

盘05为舵机快门文件，通过舵机模拟按键操作，从而控制快门释放，目前适配 DJI ACTION 4-5Pro 。

舵机规格：9g Servo Motor with Clutch Protection - PG001 / 9g离合数字舵机 - PG001

弹簧规格：Compression Spring - BB007 / 压簧 - BB007

## 二. 与打印机连接与设置

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0384.jpg)

### A 系列

连接方式：

- 对于 A1 机型，可使用 4-pin 线缆连接至打印机的 4-pin 接口。对于 A1 机型，该接口位于打印机后部；对于 A1 mini 机型，接口则位于打印机右侧。
- 对于 A2L 机型，可以试用 4-pin 或 6-pin 线缆连接打印机后部的接口。

### X1 系列及 P1 系列

连接方式：若未安装 AMS，请使用 4-pin 线缆连接打印机的 4-pin 接口。若已安装AMS，则需使用 6-pin 线缆连接 AMS 的 6-pin 接口。

### X2D 及 P2S

连接方式：需要先安装缓冲器，然后使用 6-pin 线缆连接缓冲器的 6-pin 接口。

### H2 系列

连接方式：请使用 4-pin 线缆连接打印机背后的的 4-pin 接口，或需使用 6-pin 线缆连接 AMS 的 6-pin 接口。

## 三. 摄影设备连接

### **手机蓝牙配对连接**

1. 将延时摄影套件与打印机连接，长按1秒多功能按钮。
2. 在手机上打开蓝牙配对界面，选择 "BBL\_SHUTTER" 设备进行配对。

![btcn.jpg](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/btcn.jpg)

3. 若手机蓝牙无法检测到延时摄影套件，请先将延时摄影套件与打印机断开2秒后再连接。其他设备可能占用了蓝牙配对端口，造成无法检索到蓝牙配对连接信息。
4. 进行蓝牙配对时，请确保将待配对设备置于延时摄影套件附近，最佳配对距离为50厘米以内。
5. 如果无法正常绑定设备，可使用 CyberBrick USB 升级工具将延时摄影套件恢复至出厂设置。

请参考[Cyberbrick USB 升级工具指南](../../../cyberbrick/troubleshooting/wired-firmware-guide.md) 了解如何使用 USB 升级工具。

### **相机蓝牙配对连接**

##### sony a7c2 首次连接为例

1. 将延时摄影套件与打印机连接，长按1秒多功能按钮。
2. 进入相机菜单，找到 Bluetooth，开启 Bluetooth功能。
3. 开启 Bluetooth遥控，相机即可搜索到 “BBL\_SHUTTER” 设备，确定配对。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0420.jpg)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0421.jpg)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0423.jpg)

4. 若相机蓝牙无法检测到延时摄影套件，请先将延时摄影套件与打印机断开2秒后再连接。其他设备可能占用了蓝牙配对端口，造成无法检索到蓝牙配对连接信息。
5. 进行蓝牙配对时，请确保将待配对设备置于延时摄影套件附近，最佳配对距离为50厘米以内。

##### Canon EOSR7 首次连接为例

1. 将延时摄影套件与打印机连接，长按1秒多功能按钮。
2. 进入相机菜单，选择Wi-Fi/蓝牙连接，连接至无线遥控器。
3. 选择要连接的设备 ，相机即可搜索到 “BBL\_SHUTTER” 设备，确定配对。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-2.png)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-3.png)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-4.png)

4. 若相机蓝牙**无法检测**到延时摄影套件，请先将延时摄影套件与打印机断开2秒后再连接。其他设备可能占用了蓝牙配对端口，造成无法检索到蓝牙配对连接信息。
5. 进行蓝牙配对时，请确保将待配对设备置于延时摄影套件附近，最佳配对距离为50厘米以内。

> - 佳能部分机型需要在menu的 “拍照设置” 中的 “驱动模式” 里选择 “自拍” 来触发无线快门。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-10.png)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-11.png)

##### 尼康相机

由于尼康设备息屏后会导致蓝牙连接断连，请在执行延时摄影时将息屏时间调至最大，避免因蓝牙断连导致延时摄影无法正常进行。

### **GoPro HERO13 配对连接**

1. 将延时摄影配件与打印机相连，长按1秒多功能按钮。
2. 启动GoPro HERO13，点击 “配对设备” 按钮，启动蓝牙搜索功能，看到 “Quik应用” 提示，表明配对已完成。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0429.jpg)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0430.jpg)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0432.jpg)

3. 使用GoPro时，请手动修改G-code，将拍摄延时增加到600ms并开启擦料塔。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-12.png)

4. 若相机蓝牙无法检测到延时摄影套件，请先将延时摄影套件与打印机断开2秒后再连接。其他设备可能占用了蓝牙配对端口，造成无法检索到蓝牙配对连接信息。
5. 进行蓝牙配对时，请确保将待配对设备置于延时摄影套件附近，最佳配对距离为50厘米以内。
6. 蓝牙连接GoPro后，GoPro无法正常关机，需断开蓝牙连接才能关机。

### **多设备蓝牙配对连接**

1. 本设备支持同时连接两台蓝牙无线设备，一台手机设备和一台相机设备。
2. 设备已配对两台设备且两者同时在线时，将无法再进行新设备的配对。若需配对新设备，需断开其中一台设备的蓝牙连接。新设备配对成功后，将自动替换掉一个较早配对的设备。
3. 当旧设备被新设备替换并需要重新配对时，请先删除配对设备原有的蓝牙配对记录，然后进行新的配对过程。
4. 若相机蓝牙无法检测到延时摄影套件，请先将延时摄影套件与打印机断开2秒后再连接。其他设备可能占用了蓝牙配对端口，造成无法检索到蓝牙配对连接信息。
5. 如果相机已通过蓝牙与延时摄影套件配对，但在相机重启后无法建立蓝牙连接，请长按多功能按键2秒钟，延时摄影套件将尝试重新连接之前配对的设备。

### **快门线连接**

1. 延时摄影套件配备了2.5mm通用快门线接口，适用于具备外接快门线功能的相机。连接后即可直接使用，无需进行任何额外配置。
2. 使用快门线拍摄的同时，也可以并行使用无线蓝牙快门，这样即可实现多机位同步拍摄，增强拍摄灵活性和多样性。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0388%E5%A4%84%E7%90%86.jpg)

### **舵机快门连接**

1. 若你的拍摄设备既不兼容蓝牙协议，也没有快门线接口，你可以尝试使用舵机快门套件。通过机械方式按键操作，从而控制快门释放。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0389.jpg)

2. 使用舵机快门时，请手动修改G-code，将拍摄延时增加到1000ms并开启擦料塔。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-13.png)

## 四. 如何开启一段延时摄影

> 注意：请将 Bambu Studio 升级到最新版本！

### 切片

1. 开启 Bambu Studio 导入模型，设置打印参数。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-14.png)

2. 在 “工艺” 界面中，找到 “其他” 选项，向下滚动至 “特殊模式” 设置。将 “延时摄影” 模式更改为 “平滑模式” 。热床上将生成一个擦拭塔，以便在延时摄影拍摄过程中清理漏料。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-15.png)

3. 在界面的右上角，点击 “切片单盘” 按钮以执行切片操作。在切片预览中检查打印切片的相关参数。确认切片信息准确无误后，点击 “打印单盘” 。在随后出现的发送打印任务界面中，打开 “延时摄影” 选项，然后点击 “发送” 开始打印。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-17.png)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-16.png)

### 手机

1. 手机与延时摄影套件通过蓝牙连接，在手机设置中增加自动锁屏时间，避免拍摄期间屏幕锁定。由于拍摄持续时间较长，请确保手机连接充电器。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0402%E5%A4%84%E7%90%86.jpg)

2. 将手机置于打印机前方，A系列机型需要留出热床移动空间，避免热床移动时撞击到手机。
3. 放置一个与打印模型大小相近的参照物在热床上，调整手机角度获得最佳视角。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0407%E5%A4%84%E7%90%86.jpg)

4. 在拍摄预览时，长按屏幕上的拍摄区域，锁定对焦和曝光。

![锁定对焦.png](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/%E9%94%81%E5%AE%9A%E5%AF%B9%E7%84%A6.png)

5. 若手机具备专业拍摄模式，可手动调整焦点、快门速度、光圈、ISO和白平衡，以实现更专业的拍摄效果。

![手机专业拍摄模式.png](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/%E6%89%8B%E6%9C%BA%E4%B8%93%E4%B8%9A%E6%8B%8D%E6%91%84%E6%A8%A1%E5%BC%8F.png)

6. 测试遥控快门功能，短按延时摄影套装的多功能按键，检查相机是否成功触发快门。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0411.jpg)

7. 确保拍摄设备在延时摄影过程中保持稳固，防止移动导致画面错位。

### 相机

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0384-1.jpg)

1. 相机与延时摄影套件通过蓝牙连接或者通过快门线连接，在相机设置中增加自动锁屏时间，避免拍摄期间屏幕锁定。由于拍摄持续时间较长，可将相机连接充电器。
2. 将相机架设于打印机前方，A系列机型需要留出热床移动空间，避免热床移动时撞击到相机。
3. 放置一个与打印模型大小相近的参照物在热床上，调整相机取景角度获得最佳视角。
4. 将相机调至M档手动模式，通常建议使用f/5.6至f/11的小光圈范围，以确保获得充足的景深，这样的设置适合大多数拍摄需求。
5. 若您追求背景虚化的拍摄效果，可以增大光圈。同时，准确预估焦点位置至关重要。大光圈虽能突出主体，但拍摄难度相对较高。
6. 手动设置快门速度，建议范围在1/60秒至1/200秒。若使用闪光灯进行补光，请将快门速度匹配至闪光灯的同步速度。ISO值推荐设置在100至800之间，以减少噪点。手动调节白平衡至合适色温，避免不锁定白平衡导致的色温波动问题。
7. 推荐使用JPG格式进行照片拍摄，尺寸选择S级即可。照片分辨率只要超过4K即可满足视频制作需求。请注意，过高的分辨率可能会导致后期处理软件运行缓慢。
8. 上述相机设置参数仅供参考，摄影并无固定限制。我们鼓励大家探索更多摄影技巧和发挥无限的创意思维。
9. 测试遥控快门功能，按下延时摄影套装的多功能按键，检查相机是否成功触发快门。
10. 确保拍摄设备在延时摄影过程中保持稳固，防止移动导致画面错位。

### **GoPro HERO13**

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0390%E5%A4%84%E7%90%86.jpg)

1. GoPro HERO13 与延时摄影套件通过蓝牙连接，在 GoPro HERO13 设置中增加自动锁屏时间，避免拍摄期间屏幕锁定。由于拍摄持续时间较长，可将 GoPro HERO13 连接充电器。
2. 将 GoPro HERO13 架设于打印机前方，A系列机型需要留出热床移动空间，避免热床移动时撞击到相机。
3. 放置一个与打印模型大小相近的参照物在热床上，调整取景角度获得最佳视角。
4. 将 GoPro HERO13 切换至照片模式，需注意镜头的最近对焦距离以避免图像模糊。拍摄时，选择手动模式，操作方法与普通相机相似。由于运动相机体积小巧、对焦距离短，它能捕捉到一些普通相机难以达到的独特画面角度。

> 注意：延时摄影套件通过蓝牙连接GoPro后，GoPro无法正常关机，需断开蓝牙连接才能关机。

### 拍摄技巧

#### 1. **片段拍摄：**

若仅需记录特定时段的延时摄影，如80层至150层的打印过程，可先通过 Bambu Studio 打印时间线确定所需拍摄的具体时段。例如80层开始于打印开始后的26分钟，而150层结束于40分钟，因此只需在此时间段内架设摄影设备拍摄。采用此方法可大幅减少拍摄的照片数量，特别适合存储空间有限的手机用户。

延时摄影套件具备热插拔功能，这意味着可以在打印过程中随时连接或断开设备，无需担心在打印已经开始后进行调试会对打印过程造成影响。确保你能在合适的时刻开始记录所需的延时摄影片段。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-18.png)

#### **带环境的延时摄影：**

在记录打印机延时摄影的同时，不妨考虑同步捕捉背景的变化，以增强视觉效果。例如，将打印机放置在窗户旁边，调整拍摄角度，使画面中不仅包含打印过程，还能纳入窗外的景色。这样，不仅能记录打印过程，还能捕捉到窗外风云变幻的创意效果，从而创作出更具观赏性和艺术感的延时视频。

## 五. 合成延时摄影影像

将延时摄影照片导入电脑后，可根据个人习惯挑选合适的视频编辑工具来制作延时视频。

如果你对视频编辑没有经验，也不希望投入太多时间，那么 “Shutter Encoder” 是一个高效便捷的选择。对于视频编辑经验较少的朋友，推荐 “CapCut 剪映” ，其界面直观、操作简便，易于快速上手。而对于那些熟练掌握视频剪辑的频创作者，推荐使用 “Premiere Pro”，它能提供更专业的编辑和丰富的创作可能性。

| 软件 | 难度 | 平台 | 软件费用 | 推荐人群 | 下载地址 |
| --- | --- | --- | --- | --- | --- |
| CapCut 剪映 | 低 | PC \ Mac | 免费 | 视频创作者 | <https://www.capcut.com/https://www.capcut.cn/> |
| Premiere Pro | 低 | PC \ Mac | 收费 | 专业视频创作者 | <https://www.adobe.com/> |
| Shutter Encoder | 非常低 | PC \ Mac | 开源 | 纯小白、工程师 | <https://www.shutterencoder.com/> |

### Shutter Encoder

Shutter Encoder 是一款视频和音频编码软件，它专为快速和批量的编码任务而设计。适用于个人用户和小型工作室，特别是那些需要频繁转换视频格式或者进行大量视频编码工作的用户。它的目标是提供一种高效、稳定且易于使用的编码解决方案。

1. 打开Shutter Encoder，点击 “浏览…” 导入全部序列图片，确保所有图片被选中。在 “选择功能” 菜单中，选择H.264或H.265编码格式，并设置视频输出为MP4格式，以获得最佳的兼容性和压缩效果。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-19.png)

2. 在软件界面右侧，展开 “图像序列” 选项，勾择 “激活图像序列...” 调整右侧视频参数以满足你的需求，或直接采用默认设置。若电脑性能允许，可点击播放按钮进行视频预览。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-20.png)

3. 配置完成后，点击 “启动功能” 完成视频合成。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-21.png)

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/image-22.png)

## 六. 技术参数

### 灯语

| 灯光 | 状态 |
| --- | --- |
| 绿灯 | 打印机连接通信正常 |
| 白灯 | 打印机连接通信异常 |
| 快速闪烁 | 连接模式 |

### 按键功能表

| 操作 | 功能 |
| --- | --- |
| 短按 | 手动触发快门，用于测试连接状态 |
| 长按1s | 连接模式 |

### 蓝牙兼容列表

| 手机 | Android | Android 12 及以上 |
| --- | --- | --- |
|  | HarmonyOS | 4.2.0 及以上 |
|  | IOS | IOS16 及以上 |
| 相机 | SONY | α1 / α7C2 / α7M4 / α7R5 / α7S3 / FX30 / α6700 / a6400 / ZV-E10 II /ZV-E10 / ZV-1 / ZV-1 II / RX100VII / ZV-1F 等 |
|  | Canon | EOS R8 / EOS R7 / EOS R6 / EOS R6 Mark II / EOS R5 / EOS R5 Mark II / EOS R10 / EOS R50 / EOS R50V / M50 mark II 等 |
|  | Nikon | Z30 / Z50 / Z50II / Zfc / Z6II / Z6III / Zf / Z5 / Z5II 等 |
| 运动相机 | GoPro | HERO13等 |

### 快门线兼容

快门线需自行选购，请确保所选快门线一端为2.5mm通用插头，以适配延时摄影套件。

![](https://wiki.bambulab.com/makerworld/cyberbrick/example-projects/time-lapse/dscf0221-2.jpg)

## 七. 常见问题

- **1. 无法与“BBL\_SHUTTER”设备配对？**

请删除手机中已配对的“BBL\_SHUTTER”设备信息，并重新尝试配对。

- **2. 相机无法找到“BBL\_SHUTTER”设备？**

若其他设备占用蓝牙端口，可能导致无法检索到蓝牙连接。请将延时摄影套件与打印机断开2秒后重新连接。

- **3. 相机重启后无法与已配对的延时摄影套件建立蓝牙连接？**

长按多功能按键2秒，以尝试重新连接之前配对的设备。若仍无法连接，请删除相机配对信息后重新配对。

- **4. 相机与延时摄影套件均已断电，相机开启后无法自动连接套件？**

长按多功能按键2秒，以重新连接之前配对的设备。

- **5. GoPro HERO13 拍摄延时视频画面抖动？**

由于GoPro HERO13蓝牙通信延迟，请手动增加延时时间，具体操作请参考GoPro G-code设置。

- **6. 如何在手机上设置M档手动曝光？**

iOS设备不支持，可下载专业相机应用实现。安卓设备通常内置专业相机模式，支持M档手动曝光。

- **7. 延时摄影视频亮度跳动，原因何在？**

拍摄时人员走动或观察可能造成光线遮挡或反射，影响视频曝光均匀性。

- **8. 合成的延时摄影视频出现丢帧现象？**

iOS设备在照片传输时可能遗漏文件，请重新连接手机到电脑，确保所有照片被拷贝。

- **9. 手机蓝牙连接套件后，音量键跳动？**

这是正常现象，因为手机蓝牙快门是通过音量键触发的。

- **10. 延时摄影套件兼容哪些3D打印机？**

兼容拓竹 X1、P1、A1、H2D。

- **11. 最多能同时控制几台拍摄设备？**

最多4台，包括手机蓝牙1台、相机蓝牙1台、快门线1台和舵机快门1台。

- **12. 延时摄影套件打印过程中是否支持热插拔？**

支持。

- **13. 延时摄影套件能否更新固件以支持更多相机？**

可以更新固件以增加相机兼容性。

- **14：打印时，手机无法正常启动拍照，应如何操作？**

如果在打印过程中手机无法正常启动拍照，请尝试以下步骤。

#### 检查手机息屏模式

检查手机在息屏状态是否影响拍照功能。如果拍照时屏幕自动关闭，请在设置中关闭自动息屏。

#### 检查手机拍照功能

延时摄影套件会利用蓝牙信号，启动手机音量键的拍照功能。使用前，请在手机相机设置中开启’音量键拍照‘功能。详细操作，请查阅手机说明书‘’音量键设为快门”章节。开启后，短按延时摄影套件扩展板上的功能按键，检查手机拍照功能是否正常。

##### **手机可以拍照**

如果手机可以正常拍拍照，请在 Bambu Studio 电脑端打开模型，进入预览 -> 工艺 - > 其他 -> 特殊模式 -> 延时摄影，开启平滑模式。在发送打印任务界面，确认延时摄影已开启。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/009.png)

##### **手机无法拍照**

如果手机无法拍照，请尝试以下步骤。

###### **步骤1: 检查延时摄影套件连接和指示灯状态**

1. **检查延时摄影套件连接**

**检查连接线**

确认使用拓竹官方提供的4针或6针连接线连接延时摄影套件。

下图展示了拓竹官方提供的4针和6针连接线的外观。左图: 4针连接线 (打印机连接到端口/缓冲器) 右图: 6针连接线 (AMS连接到AMS/端口/缓冲器)

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/004.png)

**检查多功能主控板**

检查多功能主控板的插入方向是否正确。下图所示为正确的插入方向。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/006.png)

2. **检查指示灯状态**

检查延时摄影套件扩展板指示灯状态，确认是否与说明一致。

| **指示灯** | **状态** |
| --- | --- |
| 绿灯常亮 | 延时摄影套件与打印机连接正常 |
| 白灯快速闪烁 | 延时摄影套件当前处于蓝牙发现模式，可通过蓝牙连接延时摄影套件 |
| 白灯常亮 | 延时摄影套件与打印机连接异常 |
| 指示灯未亮 | 延时摄影套件未接通电源或多功能主控板使用了非延时摄影项目 |

**绿灯常亮**

绿灯常亮，表示延时摄影套件与打印机连接正常。

**白灯快速闪烁**

白灯快速闪烁，表示延时摄影套件处于蓝牙发现模式。

长按延时摄影套件扩展板上的功能按键，即可进入蓝牙发现模式。进入蓝牙发现模式后50秒内，如果扩展板未连接其他设备蓝牙，将自动退出蓝牙发现模式。

**指示灯白灯常亮或指示灯未亮**

- 指示灯白灯常亮或指示灯未亮，表示延时摄影套件与打印机连接异常。请检查4针或6针连接线是否损坏。如果连接线损坏，请更换连接线。如果连接线无损坏，建议尝试将连接线插入打印机的其它4针或6针接口进行测试。
- 如果插入打印机的其它4针或6针接口后问题仍未解决，可能是延时摄影套件的多功能主控板使用了非延时摄影项目。建议您通过TYPE C线连接多功能主控板，使用PC端USB升级工具将多功能主控板更新为延时摄影套件项目。具体操作步骤详见[CyberBrick USB 升级工具指南](../../../cyberbrick/troubleshooting/wired-firmware-guide.md)。项目更新后，请重新连接打印机与延时摄影套件，并观察指示灯是否为绿灯常亮。如问题仍未解决，可能为打印机或AMS HUB接口异常，或延时摄影套件硬件故障，导致延时摄影套件无法正常与打印机连接。请联系拓竹客户服务团队获取帮助。

###### **步骤2: 检查蓝牙连接**

确认手机已通过蓝牙连接延时摄影套件。

**蓝牙未连接**

如果蓝牙未连接，请尝试连接延时摄影套件蓝牙。

如果手机无法通过蓝牙连接延时摄影套件，请检查延时摄影套件是否已连接到其他设备。

如果延时摄影套件已连接到其他设备，请先断开连接，再尝试连接手机。

如果不确定延时摄影套件是否曾连接过其他设备，可使用USB升级工具将延时摄影套件恢复到出厂设置，以清空套件与其他设备的配对信息。具体操作步骤详见[CyberBrick USB 升级工具指南](../../../cyberbrick/troubleshooting/wired-firmware-guide.md)。

恢复出厂设置后，请尝试重新连接手机与延时摄影套件，更新延时摄影项目，然后检查拍照功能是否正常。

- **15：使用相机快门线后，无法正常拍照，应如何操作？**

使用相机快门线后无法正常拍照时，请尝试以下步骤。

#### **检查相机对焦模式**

确认相机设置为手动对焦模式，镜头对焦模式调节为 M 档。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/005.png)

#### 检查延时摄影套件与打印机连接及指示灯状态

##### **检查延时摄影套件连接**

###### 检查连接线

确认使用拓竹官方提供的4针或6针连接线连接延时摄影套件。

下图展示了拓竹官方提供的4针和6针连接线的外观。左图: 4针连接线 (打印机连接到端口/缓冲器) 右图: 6针连接线 (AMS连接到AMS/端口/缓冲器)

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/001.png)

###### 检查多功能主控板

检查多功能主控板的插入方向是否正确。下图所示为正确的插入方向。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/007.png)

###### **检查指示灯状态**

检查延时摄影套件扩展板指示灯状态，确认是否与说明一致。

| **指示灯** | **状态** |
| --- | --- |
| 绿灯常亮 | 延时摄影套件与打印机连接正常 |
| 白灯快速闪烁 | 延时摄影套件当前处于蓝牙发现模式，可通过蓝牙连接延时摄影套件 |
| 白灯常亮 | 延时摄影套件与打印机连接异常 |
| 指示灯未亮 | 延时摄影套件未接通电源或多功能主控板使用了非延时摄影项目 |

**绿灯常亮**

绿灯常亮，表示延时摄影套件与打印机连接正常。

**白灯快速闪烁**

白灯快速闪烁，表示延时摄影套件处于蓝牙发现模式。

长按延时摄影套件扩展板上的功能按键，即可进入蓝牙发现模式。进入蓝牙发现模式后50秒内，如果扩展板未连接其他设备蓝牙，将自动退出蓝牙发现模式。

**指示灯白灯常亮或指示灯未亮**

- 指示灯白灯常亮或指示灯未亮，表示延时摄影套件与打印机连接异常。请检查4针或6针连接线是否损坏。如果连接线损坏，请更换连接线。如果连接线无损坏，建议尝试将连接线插入打印机的其它4针或6针接口进行测试。
- 如果插入打印机的其它4针或6针接口后问题仍未解决，可能是延时摄影套件的多功能主控板使用了非延时摄影项目。建议您通过TYPE C线连接多功能主控板，使用PC端USB工升级具将多功能主控板更新为延时摄影套件项目。具体操作步骤详见[CyberBrick USB 升级工具指南](../../../cyberbrick/troubleshooting/wired-firmware-guide.md)。项目更新后，请重新连接打印机与延时摄影套件，并观察指示灯是否为绿灯常亮。如问题仍未解决，可能为打印机或AMS HUB接口异常，或延时摄影套件硬件故障，导致延时摄影套件无法正常与打印机连接。请联系拓竹客户服务团队获取帮助。

#### **检查延时摄影套件与相机连接**

按照下图所示方式，使用快门线连接延时摄影套件与相机。连接快门线后，按下延时摄影套件扩展板上的功能按键，检查能否可以通过延时摄影套件启动相机快门进行拍照。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/008.png)

##### **可以启动快门**

如果可以启动快门，说明延时摄影套件与相机连接正常。请在 Bambu Studio 电脑端打开模型，进入预览 -> 工艺 - > 其他 -> 特殊模式 -> 延时摄影，开启平滑模式。在发送打印任务界面，确认延时摄影已开启。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/002.png)

##### **无法启动快门**

如果无法启动快门，请断开快门线与延时摄影套件的连接；按下图所示，短接快门线启动相机拍照。

如果仍无法拍照，说明快门线或相机快门接口可能出现问题。建议更换快门线或联系相机生产商售后服务。

![](https://wiki.bambulab.com/cyberbrick/manual/time-lapse/003.png)

> **注意**
>
> 延时摄影套件不包含快门线，请您自行购买。

- **16：使用相机快门线拍照后部分照片未保存，应如何操作？**

使用相机快门线拍照后，若部分照片未保存，可能原因如下。

- 相机快门模式未切换至M档;
- 相机快门接口接触不良;
- 快门线有破损/锈蚀导致连接不稳定。

请尝试以下步骤。

- 将相机快门模式切换至手动模式或M档。
- 更换快门线后再尝试拍照。
- 检查相机在拍照过程中是否自动息屏。如果出现自动息屏，请在设置中关闭自动息屏。
- 检查相机是否过热，过热可能影响SD 卡存储，造成照片未保存。如果相机过热，建议添加散热设备，或者更换正常相机继续拍照，以避免因相机过热导致拍照中断或SD卡存储异常。
- 检查 [Bambu Studio](https://bambulab.com/zh/download/studio) 是否为最新版本。如果版本过旧（低于Bambu Studio 2.0版本），请先更新，再尝试录制。
- **17：如何确认已更新至延时摄影项目？**

- 使用拓竹官方提供的4针或6针连接线连接延时摄影套件与打印机，并观察摄影套件扩展板上指示灯状态。
- 指示灯亮起5秒后变为绿灯常亮，说明延时摄影套件当前配置的项目为延时摄影项目且已与打印机成功连接。
- 指示灯未亮，说明为当前项目为非延时摄影项目。请使用手机连接延时摄影套件并更新延时摄影项目。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请提交服务工单](https://makerworld.com.cn/zh/my/support/tickets/create?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
