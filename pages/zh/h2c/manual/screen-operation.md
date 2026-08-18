---
path: zh/h2c/manual/screen-operation
title: "H2C 屏幕操作指南"
description: "本指南介绍了 H2C 的屏幕操作"
tags: []
created: 2025-11-18T12:40:41.435Z
updated: 2026-07-31T09:46:27.808Z
source: https://wiki.bambulab.com/zh/h2c/manual/screen-operation
---

本指南将介绍 H2C 打印机的屏幕按键功能。

由于 H2CL 打印机的屏幕操作和 H2DL 相同，请[点击此处](https://wiki.bambulab.com/zh/h2/manual/screen-operation#h2dl-%E6%BF%80%E5%85%89%E6%A8%A1%E7%BB%84)了解关于 H2C 激光模组和刀切模组的屏幕指南。

## 主页

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**耗材**、**设置**和 **HMS**；右侧为**打印文件**、**左/右喷嘴温度、耗材、网络设置**和**HMS**，点击图标可快速跳转至对应的控制界面。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091116.png)

## 控制

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-2.png)

### 1. **空调系统**

可根据耗材的不同选择合适的空调系统。

> 注意：工具头散热增强风扇已默认安装。

- **冷却模式**：适合打印 PLA/TPU 等**耐热性较低的耗材；**在此模式下，腔体加热循环风扇保持关闭状态。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091135.png)

- **腔温保持模式**：适合打印 ABS/ASA/PC/PA 等**具备高耐热性的耗材。**腔体加热时，系统会自动切换至腔温保持模式；在此模式下，腔体加热循环风扇将自动开启，辅助部件冷却风扇将保持关闭状态。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091220.png)

- **部件冷却风扇：**安装在工具头上，用于确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091142.png)

- **辅助部件冷却风扇：**安装在机腔内左侧，能为高速打印提供更好的冷却条件。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091156.png)

- **腔体外排风扇：** 安装在打印机右内衬上，当腔体冷却时，打印机循环系统会切换至冷却模式，腔体外排风扇转速会随腔温升高而加快。如果当前打印机的腔温不高，且机箱内打印耗材的散热需求较低，则腔体外排风扇的转速会降至 30%。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091150.png)

- **腔体加热循环风扇：**安装在打印机右内衬上，当腔体加热时，打印机会自动切换至腔温保持模式。设置腔温后，腔温加热器（由 PTC 和腔体加热循环风扇组成）开始工作，PTC 全功率加热，风扇全速运转。当腔体温度达到目标值后，风扇转速不变，PTC 功率下降，以维持恒定温度。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-1.png)

- **腔温：**根据打印耗材的不同，可设置合适的腔温。低腔温适合打印 PLA、PETG 等耗材；高腔温适合打印 ABS 等易翘曲的耗材。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091210.png)

### 2. **速度**

设置打印速度模式。

- **狂暴**：正常打印速度和加速度的 166%；该模式以速度优先，适合简单模型或对外观和强度无要求的快速测试件。此模式下**可能出现表面缺陷或层间结合弱化**，因此只建议在草模或测试中使用。
- **运动**：正常打印速度和加速度的 124%；该模式适合需缩短打印时间、且对零件质量与功能有基础要求的场景，常用于功能件、原型件或表面精度要求不高的零件，但**仍可能对打印质量产生一定影响**。
- **标准**：正常打印速度和加速度；该模式兼顾速度、质量和可靠性，能为零件提供良好的精度与强度，适合对噪音无特殊要求的使用场景。
- **静音**：正常打印速度和加速度的 50%；该模式适合夜间打印、办公室等需安静运行的场景，通过降低速度减少噪音，同时优化耗材熔化与粘合效果，以获得出色的表面质量和层间粘合。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091234.png)

### 3. **运动**

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。

> 注意：工具头回中或升降热床时，会提前进行一次热端挂架粗回中。

![](https://wiki.bambulab.com/h2/manual/screen-operation/xyz.png)

### 4. **喷嘴和挤出机**

#### 挤出机

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image.png)

1. **左边/右边**：点击左边，左热端下降，堵嘴片移至右热端堵住右喷嘴；点击右边，左热端上升，堵嘴片移至左热端堵住左喷嘴。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/switchhotend.webp)

2. **喷嘴温度**：输入数值，设置喷嘴温度，最高可加热至 350℃。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091303.png)

3. **左喷嘴类型**：可手动设置左喷嘴的类型、材质及直径。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091256.png)

右侧智能感应热端的规格信息由感应加热组件自动读取，无法进行手动编辑。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-10.png)

4. **识别左喷嘴信息**：开启后，机器将自动识别左喷嘴信息，请避免将手伸入打印机内。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091311.png)

5. **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。如果挤出机绿灯亮起，则表示挤出机的霍尔开关检测到有耗材进入。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-9.png)

#### 热端 & 挂架

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-6.png)

##### 1. **R 热端**

显示感应加热组件上 “R（Right）热端”的状态，共分为两种：

- **热端信息：**如果感应加热组件上安装了感应热端，则屏幕会显示热端内的耗材颜色及热端规格信息。

> 注意：如果热端经历过打印任务，则屏幕会显示上一次打印所使用的耗材颜色。由于所有热端出厂时都经过测试，因此新购买的热端也会自动显示出厂时用于测试的耗材颜色，且暂不支持清空感应热端内耗材颜色的功能。

在该状态下，点击R 热端，选择**放置**，打印机会将 R 热端自动放置于热端挂架的空位上；若挂架上存在多个空位，系统将优先选择编号最小，即最靠近工具头的空位，例如空位为 1、3、5 时，将优先放置于 1 号位。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-8.png)

- **空：**如果感应加热组件上并未安装热端，则会显示“空”，此时点击右热端位置，将不会显示任何按钮。

在该状态下，点击挂架上任一热端，选择**取用**，即可将该热端安装至感应加热组件上。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-7.png)

##### 2. **感应热端（1~6 号）**

显示热端挂架上感应热端的状态，共分为三种：

1. **热端信息：**

如果热端信息已被读取，则会显示热端内的耗材颜色以及热端的规格信息。

2. **未知：**

- 手动将感应热端从挂架上取下，放置到其他空位，且间隔超过一分钟时，热端规格信息无法读取，屏幕会显示 “未知”。
- 安装新热端时，因感应加热组件未读取其规格信息，屏幕同样会显示 “未知”。

在这两种状态下，点击单个热端，可进行**读取**、**取用**或**卸载**。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091801.png)

- **读取：**打印机会读取该感应热端的规格信息，进行以下操作：放置 R 热端（如有）——安装目标热端——读取热端信息——放回目标热端——重新安装 R 热端。
- **取用：**打印机会先执行一次精回中，然后将 R 热端（如有）放置在热端挂架的空位上，将目标热端安装至感应加热组件上。
- **卸载：**若需要卸载的感应热端所在的挂架已升起，可手动卸载该热端；若未升起，需等待挂架升起后再进行卸载。挂架准备升起时，请勿将手伸入打印机内，避免受伤。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091952.png)

3. **空：**如果该泊位组件上无感应热端，则会显示“空”。

在该状态下，点击该空位，可选择**放置**或**安装**热端。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091807.png)

- **放置：**将工具头上的 R 热端安装至该空位上。如果工具头上未安装 R 热端，点击挂架空位则不会显示放置按钮，只能进行手动安装。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_113014.png)

- **安装：**如果该空位所在的挂架已上升，则可以直接将热端手动放置于空位；若挂架并未上升，无法手动放置，则需待挂架上升后再手动放置热端。

> 注意：打印机（感应加热组件和热端挂架）上最多共可安装 6 个感应热端；如果安装了 7 个感应热端，则进行放置、读取或取用操作时，屏幕会提示“热端挂架上热端已装满”的报错。
>
> ![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092048.png)

##### 3. **A 排/B 排**

热端挂架分为两排，A 排为1、3、5 号感应热端泊位组件，B 排为 2、4、6 号感应热端泊位组件。点击“A 排”或“B 排”，打印机会自动上升该排挂架，上升后的挂架将显示“已经升起”。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092023.png)

##### 4. **感应热端挂架回中**

当 A 排或 B 排挂架已经升起时，点击回中按钮，热端挂架会进行一次粗回中。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_113034.png)

##### 5. **热端信息**

点击可查看打印机上所有读取过的感应热端信息规格、SN 及版本号。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_091816.png)

##### 6. **读取全部**

点击此按钮，打印机会将挂架上的感应热端依次安装至感应加热组件上，通过热端 PCB 板获取热端规格信息；当打印机上所有热端的信息都被读取完后，流程结束。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_113045.png)

##### 7. **指南**

可查看安装感应热端和刷新热端信息的具体操作步骤。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251030_202219.png)

### 5. **机箱**

同上述腔温。

### 6. **热床**

输入数值，设置热床温度。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092109.png)

### 7. **照明**

点击此按钮可控制腔内 LED 补光灯。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-12.png)

## 耗材

![](https://wiki.bambulab.com//h2/manual/screen-operation/image-7.png)

### 1. **设备**

可在此处切换不同的设备（AMS 或外挂料盘）。

![](https://wiki.bambulab.com//h2/manual/screen-operation/image-5.png)

### 2. **料盘**

点击任一料盘图标，可进行耗材编辑、进退料和 RFID 重读操作；

![](https://wiki.bambulab.com//h2/manual/screen-operation/image-6.png)

- **编辑：**如果 AMS 已通过 RFID 识别该料盘信息，可在此处查看料盘信息，但无法修改耗材参数；如果未读取 RFID，则可在此处修改耗材信息。

|  |  |
| --- | --- |
| 已读取 RFID | 未读取 RFID |

- **进料：**点击按钮，AMS 2 Pro 会自动将耗材进料至挤出机；
- **重读：**点击按钮，AMS 2 Pro 会重新读取该槽位的 RFID。

### 3. **烘干和湿度**

可查看 AMS 内部的湿度和温度，也可在此处对耗材进行烘干。

> 注：也可在设置 > 工具箱 > 烘干耗材中开启烘干功能。

![](https://wiki.bambulab.com//h2/manual/screen-operation/drying.png)

如果连接多台 AMS 2 Pro/HT，可点击左上角图标切换不同设备，查看每台 AMS 的实时湿度和温度数据，或启动烘干。

![](https://wiki.bambulab.com//h2/manual/screen-operation/image-3.png)

### 4. **外挂料盘**

点击外挂料盘图标，可进行耗材编辑和进退料操作。

![](https://wiki.bambulab.com//h2/manual/screen-operation/image-1.png)

### 5. **工具**

![](https://wiki.bambulab.com//h2/manual/screen-operation/image-2.png)

1. **自动续料**：该功能允许用户查看哪些槽位的耗材可以相互续料。当耗材的品牌、类型和颜色完全相同时，系统将建立自动续料关系。当前耗材用完时，打印机会自动切换到相同属性的耗材继续打印。

> 注意：当两个相同耗材来自同一个挤出机连接的 AMS 时，才能形成续料关系，即左对左，右对右。如果两个耗材来自不同的挤出机，则无法建立续料关系。

![](https://wiki.bambulab.com//h2/manual/screen-operation/cn-autorefill.png)

2. **AMS 初始化**：首次将 AMS 连接到 H2C 打印机时，需要进行一次初始化，目的是检测 AMS 连接到了哪一侧的挤出机。

![](https://wiki.bambulab.com//h2/manual/screen-operation/amssetup0-cn.png)

- **自动 AMS 初始化：**开启自动 AMS 初始化，AMS 会自动将耗材送至挤出机，左右挤出机各有一个霍尔传感器，可通过霍尔传感器触发信号来判断 AMS 所配对的挤出机。

> 注意：
>
> - AMS 2 Pro 内需插入一卷耗材（任意一个槽位即可）；
> - 已进料的耗材需提前退料；
> - 确保缓冲器内部无残留耗材（避免断料残留在内部）。

![](https://wiki.bambulab.com//h2/manual/screen-operation/autoamssetup.png)

- **手动 AMS 初始化：**当 AMS 中无耗材时，可手动调整 AMS 与挤出机的配对关系。若 AMS 已进料至挤出机，则该 AMS 图标为灰色（如下图中的 AMS-A），并且无法修改配对关系。

![](https://wiki.bambulab.com//h2/manual/screen-operation/manualsetup2.png)

### 6. **指南**

对进料操作进行说明：选择特定槽位，点击料盘图标，再点击进料按钮，即可触发自动进料。

![](https://wiki.bambulab.com//h2/manual/screen-operation/guidecn.png)

> 耗材页面更多相关信息请参考：
>
> [AMS 2 Pro 工作流程和功能介绍](../../ams-2-pro/manual/setup-and-printting.md)
>
> [AMS HT工作流程和功能介绍](../../ams-ht/Intr-to-ams-ht-workflow-and-features.md)

## 设置

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-15.png)

### 1. **账号**

用 Bambu Handy 扫描二维码，即可登入账号。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-14.png)

### 2. **Wi-Fi**

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-9.png)

### 3. **USB 存储**

- **存储：**显示 U 盘已使用容量和该 U 盘的最大容量；
- **弹出：**点击“弹出”，可将 U 盘安全弹出；
- **格式化外部存储：**可将 U 盘存储格式化。一旦重设，存储将无法恢复。

> 注意：U 盘规格要求和使用建议请参考：[H2C U 盘规格要求和使用建议](../../h2/manual/usb-pecifications-and-usage-recommendations.md)

![](https://wiki.bambulab.com/h2/manual/screen-operation/usb.png)

### 4. **固件**

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092135.png)

### 5. **校准**

![image_-_2025-11-13t162843.906.png](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image_-_2025-11-13t162843.906.png)

1. **打印校准**：包括电机降噪、振动补偿、自动热床调平、高温热床调平和喷嘴偏移校准。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092154.png)

- **电机降噪：**减少打印过程中电机产生的噪音，特别是在进行长时间或高速打印时。通过优化电机的运行算法和控制策略，不仅能降低噪音，还能提升打印表面的光滑度，从而改善最终打印效果。
- **振动补偿：** 在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。尤其在打印复杂或细致模型时，通过此校准能够有效防止因震动引起的误差，确保每层都准确无误地完成。
- **自动热床调平：**通过智能算法调整喷嘴与打印板之间的距离，确保每个角落的间隙一致，能够有效避免因热床不平整导致的打印缺陷，从而提高打印精度。
- **高温热床调平：**使用 ABS/ASA/PC/PA 等高温耗材打印前，进行高温热床校准，能够确保热床在高温环境下保持稳定，有效防止首层翘曲或粘附不良，提高首层打印质量。
- **喷嘴偏移校准：**如果喷嘴的定位出现偏移，则可能导致打印过程中模型出现错位或层移现象。在打印过程中发现切换喷嘴后模型出现明显的层移时，建议进行一次喷嘴偏移校准。此过程会校准工具头上的热端以及热端挂架上的每个热端，利用工具头内的涡流传感器和热床后面的喷嘴偏移校准传感器，确保喷嘴位置的准确性，以提高打印质量和精确度。

2. **高精度喷嘴偏移校准：**将一深一浅两种耗材分别进料至工具头上的两个喷嘴，利用 AI 视觉检测技术，精确校准两个喷嘴在 XY 方向上的偏移量，以提高打印质量和精度。此次操作不会对热端挂架上的热端进行校准。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092159.png)

3. **实况摄像头校准：**通过识别热床上的特定标记，校准实况摄像头的位置和角度，减少因摄像头视角偏差和位置错误导致的检测误差，从而显著提升其检测精度，实现更高的图像捕捉质量。

![](https://wiki.bambulab.com/h2/manual/screen-operation/liveview.png)

4. **运动精度校准：**专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。

> 运动精度校准详情请参考：[运动精度校准](../../h2/manual/motion-accuracy.md)

![](https://wiki.bambulab.com/h2/manual/screen-operation/motion.png)

5. **感应热端挂架初始化：**通过初始化流程，可确保工具头在切换热端时能够准确定位热端挂架的位置，避免因挂架变形造成打印故障。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251110_150726.png)

### 6. **工具箱**

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_113059.png)

- **烘干耗材：**选择耗材类型，设置烘干温度及时长，对耗材进行烘干处理。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092212.png)

- **XYZ 轴清洁：**光杆的定期清洁可防止碎屑积累，确保设备正常运作并延长使用寿命。屏幕左侧进度条长度会随光杆的清洁程度减少；如果进度条变为红色，则需进行清洁，具体教程可通过右侧二维码获取。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092216.png)

- **丝杆润滑：**丝杆需要定期润滑，以确保热床上下移动运行平稳。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092221.png)

- **激光模组清洁：**激光模组的定期清洁可防止粉末和碎屑积累，确保设备正常运作并延长使用寿命。机器会根据 Bambu Suite 中的总工程时间和激光任务类型评估打印机的污染程度。屏幕左侧的绿色进度条长度会随着激光模组的清洁程度减少；如果进度条变为红色并显示“需要立即进行清洁”，则需进行清洁，具体教程可通过右侧二维码获取。详情请参考：[10w 激光模组定期维护建议](../../h2/maintenance/laser-module.md)。

![](https://wiki.bambulab.com/h2/manual/screen-operation/jiguangmozuqingjie.png)

- **感应热端挂架 & 锁紧拉柄维护：**热端挂架与锁紧拉柄在长期使用过程中，容易积累灰尘，这些灰尘会影响热端更换时拉柄的锁紧效果。通过对热端挂架及锁紧拉柄进行润滑保养，既能减少部件磨损概率，还能保障喷嘴更换的成功率。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_113104.png)

- **喷嘴冷拔维护：**当挤出电机在常规打印流量下频繁出现过载报错，则表示喷嘴阻力过大，急需清理；同时，由于 TPU 对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，建议在打印 TPU 前对喷嘴进行冷拔清理，以保证打印顺畅。喷嘴冷拔维护详情请参考：[H2C 喷嘴冷拔维护清理](../maintenance/nozzle-cold-pull-maintenance-and-cleaning.md)。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092236.png)

### 7. **设置**

|  |  |
| --- | --- |
|  |  |

#### **打印选项**

|  |  |
| --- | --- |
|  |  |

1. **AI 检测**

H2C 配备了伺服挤出电机、缓冲器、实况摄像头、俯视摄像头（选装）等智能传感模块，因此支持多种智能检测功能，包括**炒面检测、堆料检测、裹头检测**（实况摄像头检测）和**空打检测**（伺服挤出电机检测）等。针对打印机检测到异常后的暂停策略，可在此处自定义暂停灵敏度，共分为三档：高（发现微小异常即立即暂停）、中（异常达到一定程度时暂停）和低（仅当出现明显异常时暂停），以适配不同场景下的打印质量需求。

2. **打印板检测**

实况摄像头可对热床上的打印板进行**类型检测**和**在位检测**。

- **类型检测：**若实际使用的打印板与切片文件中的打印板不匹配，则及时停止打印，避免打印失败。
- **在位检测：**若打印板的标记未处于预定义范围内，打印机将自动停止打印，以避免打印板未放置或放置不当导致的打印异常。

> 注意：有关智能检测的更多内容，请参考：[H2D智能检测介绍](../../h2/manual/intelligent-detection.md)。

|  |  |
| --- | --- |
|  |  |

3. **丢步自动恢复**：当电机检测到位置偏移（丢步）时，X、Y 和 Z 轴会重新定位，并回到偏移前的位置继续执行未完成的 G-code，以保证打印质量。
4. **开门检测**：开启后，打印机将检测前门玻璃是否打开，可选择在门打开时触发通知或暂停打印。
5. **缓存远程打印文件到外部存储中**：通过云端发起的打印，打印文件将缓存到外部存储中。
6. **运动精度增强**：专为对打印质量有高要求的用户设计，旨在解决 3D 打印过程中的绝对定位问题，从而提高打印精度，尤其是大尺寸打印的精度。通过这一过程，可以显著抑制运动迟滞和运动畸变，确保打印结果更加精准。
7. **打印结果快照：**打印任务完成后，打印机会自动拍摄打印件照片并上传至云端，该照片将同步显示在 Bambu Handy 的打印完成弹窗中。

#### **AMS 选项**

|  |  |
| --- | --- |
|  |  |

- **插入耗材时读取：**在插入耗材预上料后，AMS 会进行 RFID 读取操作。
- **开机时读取**：每次重启打印机时，AMS 会自动读取插入的耗材信息，并且读取过程中会转动耗材。
- **AMS 自动续料**：当 AMS 某个槽的耗材用完时，可自动切换到其他槽位上属性完全相同的耗材。这些属性包括品牌、类型、颜色和打印温度等。请确保在打印前配置好所有耗材的信息，以满足自动续料的要求。
- **重新排序 AMS**：每个 AMS 都会分配一个顺序，并在屏幕上显示。分配 AMS ID 的目的是方便识别它们之间的连接。分配 ID 的逻辑为：直接连接到打印机的是 AMS-A，连接到 AMS-B 的是 AMS-C，以此类推。如果需要重新排序 AMS，可以点击“重置”，即可重置 AMS 的顺序信息。重置完成后，请按需依次连接 AMS 进行排序。

#### **录像**

设置录像的清晰度。清晰度越高，所需的存储空间越大。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092412.png)

#### **自动休眠**

选择打印机自动休眠的时长。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092419.png)

#### **声音**

如果开启声音选项，打印机在开机、打印开始和打印结束时都会发出提示音。

#### 状态指示灯

用于提示打印机健康状态和打印任务状态。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-19.png)

#### 低功率模式

低功耗模式专为电力承载能力有限的用户设计。启用后，打印机会智能调配交流电加热模块（包括热床与腔温加热组件）的总功率输出，将整机峰值功率限制在约 860W，以适配家庭电力系统功率较低的环境，确保打印过程稳定。

此模式仅限制设备的最大功率输出，以提升与低功率电路的兼容性，**并不会减少整体能耗**。启用后，热床与腔体的加热速度将相应减慢。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251107_092432.png)

#### **机箱灯模式**

可根据实际的使用需要选择手动模式或节能模式。

![](https://wiki.bambulab.com/h2/manual/screen-operation/chamberlight.png)

#### **语言**

选择打印机屏幕的显示语言。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/screenshot_20251110_150735.png)

#### **设备和序列号**

查看打印机设备名、设备使用时间、序列号及热端的规格信息。选择是否加入“用户体验改进计划”，加入后可将机器数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-18.png)

#### **仅局域网**

开启仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-14.png)

#### **导出日志到外部存储**

可根据需求，选择是否导出所有打印日志、关键照片（判断炒面等问题）和 G-code（判断打印质量问题）。

![](https://wiki.bambulab.com/h2/manual/screen-operation/export.png)

#### **恢复出厂设置**

将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![factory.png](https://wiki.bambulab.com/h2/manual/screen-operation/factory.png)

## 助手

如果打印机出现故障，此处将会显示报错信息。

![](https://public-cdn.bblmw.com/wiki/new/h2c/manual/screen-operation/image-17.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
