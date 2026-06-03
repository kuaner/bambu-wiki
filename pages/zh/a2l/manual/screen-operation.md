---
path: zh/a2l/manual/screen-operation
title: "A2L 屏幕操作指南"
description: "本指南旨在介绍 A2L 打印机屏幕按键及操作功能。"
tags: []
created: 2026-06-01T13:02:16.436Z
updated: 2026-06-01T13:18:26.742Z
source: https://wiki.bambulab.com/zh/a2l/manual/screen-operation
---

## 主页

主页包括**打印文件**、**耗材**、**控制**、**设置**和**助手**。右上角为喷嘴温度、热床温度、供料来源、摄像头状态和网络状态图标。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/081.png)

## 打印文件

在主页点击**打印文件**，将进入打印准备页面。机器出厂时，microSD 中会保存一些内置模型切片文件，可直接在打印机上对这些内置文件发起打印。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/016.png)

选择想打印的模型文件，屏幕会显示打印该模型所需的时间和耗材克数，也可在此开启**延时摄影**或进行**高级设置**；

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/pre-print-cn.png)

- **延时摄影**：打开延时摄影，打印机会在打印过程中记录每个阶段，并自动形成延时摄影视频。具体请参考[延时摄影](../../software/bambu-studio/Timelapse.md)；
- **高级设置**：包括**自动热床调平**和**动态流量校准**；
  - 自动热床调平：发起打印后，打印前可对热床进行调平；
  - 动态流量校准：通过调整打印机对耗材的挤出量，以确保流量响应与工具头运动同步。请参考[动态流量校准](../../software/bambu-studio/calibration_pa.md) 获取更多相关信息。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/015.png)

## 耗材

### AMS/AMS 2 Pro/AMS HT

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/036.png)

#### 1. **耗材图标**

点击任一装载耗材的槽位图标，均会显示以下四个按钮：

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/058.png)

1. **进料**：使用 AMS 时，可选择某一料盘，点击**进料**按钮，执行相应操作。
2. **退料**：使用 AMS 时，可选择某一料盘，点击**退料**按钮，执行相应操作。
3. **刷新**：读取耗材的 RFID 信息（仅支持拓竹官方耗材）。
4. **编辑**：选择耗材制造商、类型、颜色及动态压力控制。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/025.png)

#### 2. 挤出机图标

如果挤出机图标中亮起小绿灯，则表示挤出机的霍尔开关检测到有耗材进入。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/014.png)

#### 3. 烘干

当打印机连接 AMS 2 Pro 或 AMS HT 时，此处会显示舱内湿度；当连接 AMS 时，此处会显示湿度档位；具体可参考[AMS 湿度检测功能](../../ams/manual/humidity-detection-function.md)了解 AMS 湿度检测功能。

|  |  |  |
| --- | --- | --- |
|  |  |  |
| 湿度显示 - AMS 2 Pro | 湿度显示 - AMS | 湿度显示 - AMS HT |

点击"烘干"按钮，可对耗材进行烘干。在 AMS 烘干页面可以设置耗材的类型、烘干温度及时间，请参考 [AMS 2 Pro 和 AMS HT 烘干指南](../../ams-2-pro/manual/drying-function.md) 设定合适的参数。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/022.png)

> **注意**：烘干时，务必使用电源适配器为 AMS 设备供电，否则屏幕会提示功率不足。
>
> - AMS HT：请使用随附的电源线。
> - AMS 2 Pro：请使用拓竹官方[电源适配器](https://item.jd.com/10145041049074.html)。

#### 4. **切换 AMS 设备**

如果连接了多台 AMS 设备，可点击翻页按钮，可查看所有连接至此打印机的 AMS 设备。每个 AMS 页面左上角均会显示该 AMS 的 ID，具体的 AMS ID 分配规则可参考：[A2L AMS 连接指南](https://wiki.bambulab.com/zh/a2l/manual/a2l-ams-connection-guide#ams-id-assignment)。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/021.png)

### AMS lite

- **进料/退料**：使用 AMS lite 时，可选择某一料盘，点击**进料**或**退料**按钮，执行相应操作。
- **编辑**：选择耗材制造商、类型、颜色及动态压力控制。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/030.png)

### 外挂料盘

- **进料/退料**：使用 AMS 时，可选择某一料盘，点击**进料**或**退料**按钮，执行相应操作。使用外挂料盘时，可直接点击按钮进行相应操作。
- **编辑**：选择耗材制造商、类型、颜色及动态压力控制。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/018.png)

## 控制

### 控制

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/017.png)

1. **喷嘴温度**：输入数值，设置喷嘴温度。
2. **热床温度**：输入数值，设置热床温度。
3. **打印速度**：设置打印速度模式。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/013.jpg)

- **狂暴**：正常打印速度和加速度的 166%
- **运动**：正常打印速度和加速度的 124%
- **标准**：正常打印速度和加速度
- **静音**：正常打印速度和加速度的 50%

4. **风扇设置**：开启或关闭部件冷却风扇，并设置转速。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/037.png)

5. **LED 补光灯**：点击按钮可控制 LED 补光灯。
6. **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。如果绿灯亮起，则表示挤出机的霍尔开关检测到有耗材进入。

### XYZ

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/039.png)

1. **XY 轴控制盘**

- **X/-X：**点击按钮，控制工具头在 X 轴上左右移动；
- **Y/-Y：**点击按钮，控制热床在 Y 轴上前后移动。
- **回中：**点击中间的回中按钮，可控制所有轴归零。

2. **X 轴升降控制**：点击移动按钮，X 轴可沿 Z 轴上下升降。

## 设置

|  |  |
| --- | --- |
|  |  |
|  |  |

#### 账号

用 Bambu Handy 扫描二维码，可登入账号。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/010.jpg)

#### WLAN

设置打印机网络，查看 IP 地址和 MAC 端地址。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/007.jpg)

#### 设备

- **型号**：查看打印机型号。
- **相机**：查看相机状态。
- **打印时间**：查看设备使用时长。
- **体验改善计划**：开启后，可将机器的数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。
- **使用条款：**可扫码查看设备使用条款和隐私政策。
- **序列号：**可查看打印机和 AMS 的序列号。

|  |  |
| --- | --- |
|  |  |

#### SD 卡

可查看打印机 SD 卡总容量和剩余容量；如需弹出 SD 卡，需在此页面点击"弹出 SD 卡"，再手动退出。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/050.png)

#### 维护

|  |  |
| --- | --- |
|  |  |

- **校准**：通过电机降噪、振动补偿和热床调平来进行打印机校准。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/044.png)

1. **电机降噪**：减少打印过程中电机产生的噪音，特别是在进行长时间或高速打印时。通过优化电机的运行算法和控制策略，不仅能降低噪音，还能提升打印表面的光滑度，从而改善最终打印效果。
2. **振动补偿**: 在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。尤其在打印复杂或细致模型时，通过此校准能够有效防止因震动引起的误差，确保每层都准确无误地完成。
3. **自动热床调平**：通过智能算法调整喷嘴与打印板之间的距离，确保每个角落的间隙一致，能够有效避免因热床不平整导致的打印缺陷，从而提高打印精度。
4. **80 ℃ 热床调平：**使用 ABS/ASA/PC/PA 等高温耗材打印前，进行高温热床校准，能够确保热床在高温环境下保持稳定，有效防止首层翘曲或粘附不良，提高首层打印质量。

- **喷嘴**：如果更换过配件，可重新设置喷嘴，以保证打印质量。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/003.jpg)

- **喷嘴冷拔维护：**当挤出电机在常规打印流量下频繁出现过载报错，则表示喷嘴阻力过大，急需清理；同时，由于 TPU 对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，建议在打印 TPU 前对喷嘴进行冷拔清理，以保证打印顺畅。喷嘴冷拔维护详情请参考：[A2L 喷嘴冷拔维护指南](https://wiki.bambulab.com/zh/a2l/maintenance/nozzle-cold-pull-maintenance)。

|  |  |
| --- | --- |
|  |  |

- **维护模式**：选择是否开启维护模式。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/009.jpg)

- **首层质量校准：**支持微调首层打印时喷嘴与热床间的距离，从而提升首层附着力与表面平整度，有效解决首层偏高或偏低导致的打印质量问题。

> 注意：
>
> - 该功能是为了满足用户不同场景差异化的调参需求，一般情况无需用到，建议按需使用。
> - 由于打印板存在批次和工艺差异，每台打印机对首层的要求略有不同。因此，机器在出厂前会对打印机及其配套打印板进行首层质量校准，部分机器会写入对应的 Z 偏移量。

|  |  |
| --- | --- |
|  |  |

#### 打印选项

- **声音**：如开启选项，打印机在开机、打印开始和打印结束时都会发出提示音。
- **缠料检测**：主要用于防止耗材在外挂料盘或 AMS 内发生缠绕、卡料等送料故障。当检测到送料路径阻力异常增大时，系统会暂停打印并提示缠料风险。请参考 [A2L 空打缠料检测](https://wiki.bambulab.com/zh/a2l/manual/air-printing-and-filament-tangle-detection)了解更多相关信息。
- **丢步自动恢复**：当电机在工作过程中检测到位置偏移（即丢步）时，X、Y 和 Z 轴将会重新回中进行定位，然后回到丢步前的位置重新执行未被执行的 G code，保证打印质量。
- **裹头检测**：当打印机检测到喷嘴被耗材包裹后，会自动暂停打印并提醒，尽可能避免裹头后继续打印对打印机造成更大的伤害。请参考 [A2L 裹头检测](https://wiki.bambulab.com/zh/a2l/manual/nozzle-clumping-detection)了解更多相关信息。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/085.png)

- **打印板位置检测**：打印机在打印开始前能检测用户是否放置了打印板，避免直接在热床上打印，导致打印失败甚至损坏热床。请参考 [A 系列打印板检测](../../a1-mini/manual/build-plate-detection.md)了解更多相关信息。
- **空打检测：**主要用于应对因热端堵塞、耗材磨损/直径异常、温度设置不当等原因，导致喷嘴无法正常挤出耗材而进行"悬空打印"的情况。A2L 根据不同的供料方式和硬件配置，采用了多种检测方案协同工作，请参考 [A2L 空打缠料检测](https://wiki.bambulab.com/zh/a2l/manual/air-printing-and-filament-tangle-detection)了解更多相关信息。
- **热床保温：**通过在打印前让热床充分预热并维持稳定温度，减少因热形变导致的首层翘曲，从而提升首层打印质量。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/070.png)

#### AMS 选项

- **插入时读取**：在插入耗材预上料后，AMS 会进行 RFID 读取操作。
- **开机时读取：**每次重启打印机时，AMS 会自动读取插入的耗材信息，并且读取过程中会转动耗材。
- **AMS 自动续料**：当 AMS 某个槽的耗材用完时，可自动切换到其他槽位上属性完全相同的耗材。这些属性包括品牌、类型、颜色和打印温度等。请确保在打印前配置好所有耗材的信息，以满足自动续料的要求。请参考[此文章](https://wiki.bambulab.com/zh/ams/manual/ams-function-introduction#%E6%96%AD%E6%96%99%E6%A3%80%E6%B5%8B%E5%92%8C%E8%87%AA%E5%8A%A8%E7%BB%AD%E6%96%99%E5%8A%9F%E8%83%BD)了解更多相关信息。
- **重新排序 AMS**：每个 AMS 都会分配一个顺序，并在屏幕上显示。分配 AMS ID 的目的是方便识别它们之间的连接。如果需要重新排序 AMS，可以点击"重新排序 AMS"，即可重置 AMS 的顺序信息。重置完成后，请按需依次连接 AMS 进行排序。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/083.jpg)

#### **相机选项**

- **视频**：在打印过程中进行实时录制视频。
- **延时摄影渐变模式**：开启后，打印首层时会出现裁切放大的效果。随着层数的增加，画面逐渐由放大转变为缩小。请参考[此文章](../../software/bambu-studio/Timelapse.md)了解更多相关信息。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/012.jpg)

#### 固件

查看设备当前版本、该版本的发行说明及离线更新。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/011.jpg)

#### 语言

选择打印机屏幕的显示语言。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/001.jpg)

#### 屏幕关闭时间

选择打印机屏幕的自动休眠时长。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/004.jpg)

#### 局域网模式

开启后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/005.jpg)

#### 恢复出厂设置

将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/006.jpg)

#### 认证信息

可在此处查看机器的认证信息电子标签页。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/087.png)

## 助手

如打印机出现故障，可在此查看相关故障和解决方案。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/008.jpg)

## A2L +刀切模组

安装刀切模组后，屏幕会提示进行"校准"，可点击此按钮开始校准。

> 注意：安装画笔模组时，机器无法进行校准，需换成刀切模组才能进行校准。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/screen-operation/077.png)

后续也可点击“设置 > 挂载校准”进行校准。

|  |  |
| --- | --- |
|  |  |

> 挂载校准的具体介绍请参考：[A2L 刀切/画笔使用教程](https://wiki.bambulab.com/zh/a2l/manual/cutting-module-user-guide)。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
