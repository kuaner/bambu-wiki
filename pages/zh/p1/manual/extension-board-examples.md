---
path: zh/p1/manual/extension-board-examples
title: "Bambu Lab扩展板使用方法及示例"
description: ""
tags: ["扩展板"]
created: 2023-05-24T10:30:39.032Z
updated: 2026-02-02T08:42:25.000Z
source: https://wiki.bambulab.com/zh/p1/manual/extension-board-examples
---

# Bambu Lab扩展板使用方法及示例

## 简介

Bambu Lab扩展板是一款开发板，旨在为 Bambu Lab 添加高级和定制功能。它优先兼容 P1P 系列机型，且产品更新和迭代均为 P1P 优先。下面展示一些添加功能的示例，供其他机型参考。

## 前期准备

- 扩展板套件
- LED灯（可选）
- 散热风扇（可选）
- 您自己的相机和与您的相机兼容的相机快门电缆（可选）

在一些时候，可以使用几行**简单的 G-Code** 来实现更多的功能。请按照以下说明复制代码实现相关功能，或参考[其他 WIKI 页面进行高级编程](extension-board-gcode-reference.md)。

## 如何将 G-Code 应用到扩展板中

- 第一步，在 Bambu Studio 中打开“高级”设置。

![](https://wiki.bambulab.com/general/extension-board-examples/打开“高级”设置.png)

- 第二步，点击打印机栏中的“编辑”图标来配置 G-Code。

![](https://wiki.bambulab.com/general/extension-board-examples/点击“编辑”图标来配置g-code.png)

- 第三步，在 G-Code 中，分号后为文档注释。您可以在打印的开头、结尾或层变化期间插入您的代码。

![](https://wiki.bambulab.com/general/extension-board-examples/第三步，在g-code中.png)

## 扩展板引脚图及开关示意

下面为扩展板引脚图：

![](https://wiki.bambulab.com/general/extension-board-examples/扩展板中文说明.png)

## 扩展板预设说明

**扩展板内预设了一些配置，具体如下：**

- 0 号开关可以控制 2 个灯带的通断，0 号滑动变阻器可以控制 2 个灯带的亮度，灯带颜色默认为白色。
- 1 号开关可以控制 4 个风扇的通断，1 号滑动变阻器可以控制 2 个 4 引脚风扇的转速。
- 如果想要配置为仅控制单通路，例如：配置为使用 0 号开关和 0 号滑动变阻器分别控制 0 号灯带开关和亮度，则可以编辑如下代码：

```
; 配置0号开关（I=0）控制0号（D=0）灯带（F=1）开关
M1004 S7 I0 F1 D0
; 配置0号滑动变阻器（I=0）控制0号（D=0）灯带（F=0）亮度
M1004 S6 I0 F0 D0
```

## 示例1：使用开关控制继电器通断

1. 【硬件连接】
2. 在【起始G-code】中末行插入`M1004 S7 I0 F3 D0`命令，其中`I0`表示0号开关，`F3`表示控制继电器，`D0`表示0号继电器（由于只有一个继电器，`D0`也可以省略）。另外，如果您想让扩展板断电后依然保存配置信息，请输入`M1004 S0 P1`。

`M1004 S7 I0 F3 D0`  
`M1004 S0 P1`

如图所示：

![](https://wiki.bambulab.com/general/extension-board-interface-desp/起始g-code.png)

3. 发起打印任务，在打印的起始阶段配置的信息将被写入扩展板。

## 示例2：使用扩展板完成延时摄影

如果想要完成用您自己的相机完成完美的延时摄影，那么需要就需要相机在完成每层打印时拍摄下一张照片。

1. 使用一根快门线把你的相机和扩展板连接起来。
2. 在换层 Gcode 中插入命令，使相机在每次换层成时拍摄照片。拍摄前，你需要将相机的快门设置成手动模式，且禁用相机的自动休眠。

请注意，拍摄的命令和内置摄像头延时摄影的逻辑可能有冲突，所以请按照以下情况选择插入摄影的位置。

首先我们要了解内置延时摄影的命令如下：

```
; layer num/total_layer_count: {layer_num+1}/[total_layer_count]
M622.1 S1 ; for prev firware, default turned on
M1002 judge_flag timelapse_record_flag
M622 J1
{if timelapse_type == 0} ; timelapse without wipe tower
M971 S11 C10 O0
{elsif timelapse_type == 1} ; timelapse with wipe tower
G92 E0
G1 E-[retraction_length] F1800
G17
G2 Z{layer_z + 0.4} I0.86 J0.86 P1 F10000 ; spiral lift a little
G1 X65 Y245 F12000 ; move to safe pos
G17
G2 Z{layer_z} I0.86 J0.86 P1 F10000
G1 Y265 F3000
M400 P100
M971 S11 C10 O0
G92 E0
G1 E[retraction_length] F300
G1 X100 F5000
G1 Y255
{endif}
M623
```

如上代码中，每换一层，都会执行一遍这个判断逻辑：

如果延时摄影模式为0，内置摄像头会直接拍照（M971即为内置摄像头拍照指令）；

如果模式为1，则移动工具头到指定位置再拍摄。

### **Case 1：**

如果我们不使用内置的摄像头（P1P 平滑延时摄影模式将在下一版本固件中发布），我们可以在换层代码的最开始处插入如下代码：

- **随机拍摄**

```
; take a photo
M1004 S5 P1
```

- **定点拍摄**

```
; timelapse with wipe tower
G92 E0
G1 E-[retraction_length] F1800
G17
G2 Z{layer_z + 0.4} I0.86 J0.86 P1 F10000 ; spiral lift a little
G1 X65 Y245 F12000 ; move to safe pos
G17
G2 Z{layer_z} I0.86 J0.86 P1 F10000
G1 Y265 F3000
M400 P100 ; wait for 100 ms
M1004 S5 P1 ; take a photo
G92 E0
G1 E[retraction_length] F300
G1 X100 F5000
G1 Y255
```

### **Case 2：**

如果要同时使用内置的摄像头，则可以按照实际的情况在已存在的逻辑判断中加入拍摄的语句。此情况中，需要在 Studio 中打开延时摄影的平滑模式。

```
; layer num/total_layer_count: {layer_num+1}/[total_layer_count]
M622.1 S1 ; for prev firware, default turned on
M1002 judge_flag timelapse_record_flag
M622 J1
{if timelapse_type == 0} ; timelapse without wipe tower
M971 S11 C10 O0
{elsif timelapse_type == 1} ; timelapse with wipe tower
G92 E0
G1 E-[retraction_length] F1800
G17
G2 Z{layer_z + 0.4} I0.86 J0.86 P1 F10000 ; spiral lift a little
G1 X65 Y245 F12000 ; move to safe pos
G17
G2 Z{layer_z} I0.86 J0.86 P1 F10000
G1 Y265 F3000
M400 P100
M971 S11 C10 O0
M1004 S5 P1; only executed when smooth timelapse is on and take a photo when toolhead is at wipe tower
G92 E0
G1 E[retraction_length] F300
G1 X100 F5000
G1 Y255
{endif}
M623
```

## 示例3： 渐变灯光

本示例使用扩展板完成的功能为：在打印开始时开启风扇，在打印换层时渐变灯光颜色。

1. 将扩展板连接到LED灯带，风扇。
2. 在换层G-Code**起始位置**插入如下的命令：

```
; change the led color slightly with the number of layers
M1004 S1 L0 M0 B{30 + layer_num * 200 / total_layer_count} ; set red between 30-200
M1004 S1 L1 M0 B{255 - layer_num * 200 / total_layer_count} ; set green between 255 and 55
M1004 S1 L2 M0 B{55 + layer_num * 100 / total_layer_count} ; set blue between 55 and 155
```

如图所示：

![](https://wiki.bambulab.com/general/extension-board-interface-desp/换层g-code.png)
