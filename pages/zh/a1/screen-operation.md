---
path: zh/A1/screen-operation
title: "A1 系列屏幕操作指南"
description: "本指南介绍了 A1 系列的屏幕操作"
tags: ["a1", "a1 mini"]
created: 2024-09-14T03:53:36.749Z
updated: 2026-05-19T09:02:40.485Z
source: https://wiki.bambulab.com/zh/A1/screen-operation
---

## 介绍

本指南旨在介绍 A1 系列打印机屏幕按键及操作功能。

## 主页

![20240914-111044.jpg](https://wiki.bambulab.com/a1-screen-operation/20240914-111044.jpg)

主页包括**打印文件**、**耗材**、**控制**、**设置**和**助手**。右上角为喷嘴温度、热床温度、摄像头状态和网络状态图标。

## 打印文件

![打印文件-.jpg](https://wiki.bambulab.com/a1-screen-operation/%E6%89%93%E5%8D%B0%E6%96%87%E4%BB%B6-.jpg)

在主页点击**打印文件**，将进入打印准备页面。打印机将读取 SD 卡上的所有切片模型文件，包括之前打印过的和通过无线局域网发送至打印机的文件。选择想打印的文件，点击右上角**打印**，即可开始打印。

![文件打印-.jpg](https://wiki.bambulab.com/a1-screen-operation/%E6%96%87%E4%BB%B6%E6%89%93%E5%8D%B0-.jpg)

同时，可开启延时摄影、热床调平和动态流量校准。

- **延时摄影**：记录打印过程的每个阶段。
- **热床调平**：发起打印后，打印机可对热床进行调平。（1.9 及以上版本 Bambu Studio 支持对热床进行局部调平）
- **动态流量校准**：通过调整打印机对耗材的挤出量，以确保流量响应与工具头运动同步。请参考 [此wiki](../software/bambu-studio/calibration_pa.md) 获取更多相关信息。

## 耗材

### AMS lite

![20251218-120958.jpg](https://wiki.bambulab.com/a1/screen-operation/20251218-120958.jpg)

- **进料/退料**：使用 AMS lite 时，可选择某一料盘，点击**进料**或**退料**按钮，执行相应操作。
- **编辑**：选择耗材制造商、类型、颜色及动态压力控制。

### AMS/AMS 2 Pro/AMS HT

> 请将 A1 系列打印机升级至 [01.07.00.00](https://wiki.bambulab.com/zh/a1/manual/a1-firmware-release-history#%E5%9B%BA%E4%BB%B6%E7%89%88%E6%9C%AC-0107000020251027) 及以上的固件版本，以兼容 AMS、AMS 2 Pro 和 AMS HT。请参考[此文章](../a1/manual/ams-connection-guide.md)了解可连接的 AMS 搭配、数量和具体连接步骤。

![a1_屏幕_耗材_ams耗材设置.png](https://wiki.bambulab.com/a1/screen-operation/a1_%E5%B1%8F%E5%B9%95_%E8%80%97%E6%9D%90_ams%E8%80%97%E6%9D%90%E8%AE%BE%E7%BD%AE.png)

- **进料/退料**：使用 AMS、AMS 2 Pro 或 AMS HT 时，可选择某一料盘，点击**进料**或**退料**按钮，执行相应操作。
- **刷新**：读取耗材的 RFID 信息（仅支持拓竹官方耗材）。
- **编辑**：选择耗材制造商、类型、颜色及动态压力控制。

![a1_屏幕_耗材_湿度+烘干+切换ams.png](https://wiki.bambulab.com/a1/screen-operation/a1_%E5%B1%8F%E5%B9%95_%E8%80%97%E6%9D%90_%E6%B9%BF%E5%BA%A6+%E7%83%98%E5%B9%B2+%E5%88%87%E6%8D%A2ams.png)

1. **湿度（支持 AMS、AMS 2 Pro 和 AMS HT）**：展示实时舱内湿度或湿度档位，请参考[此文章](../ams/manual/humidity-detection-function.md)了解AMS湿度检测功能。

|  |  |  |
| --- | --- | --- |
| 湿度显示-AMS 2 Pro | 湿度显示-AMS 一代 | 湿度显示-AMS HT |

2. **烘干（支持 AMS 2 Pro 和 AMS HT）**：通过 AMS 设备内置的干燥模块烘干耗材，减少打印缺陷。在 AMS 烘干页面可以设置耗材的类型、烘干温度及时间，请参考[此文章](../ams-2-pro/manual/drying-function.md)设定合适的参数。

|  |  |
| --- | --- |
|  |  |

> **注意**：烘干时，务必使用电源适配器为 AMS 设备供电，否则屏幕会提示功率不足。
>
> - AMS HT：请使用随附的电源线。
> - AMS 2 Pro：请使用拓竹官方[电源适配器](https://item.jd.com/10145041049074.html)。

3. **切换 AMS 设备**：点击翻页按钮，可查看所有连接至此打印机的AMS设备。

### 外挂料盘

|  |  |
| --- | --- |
|  |  |

- **进料/退料**：使用 AMS 时，可选择某一料盘，点击**进料**或**退料**按钮，执行相应操作。使用外挂料盘时，可直接点击按钮进行相应操作。
- **编辑**：选择耗材制造商、类型、颜色及动态压力控制。

![a1_屏幕_耗材_外挂料盘进料.jpg](https://wiki.bambulab.com/a1/screen-operation/a1_%E5%B1%8F%E5%B9%95_%E8%80%97%E6%9D%90_%E5%A4%96%E6%8C%82%E6%96%99%E7%9B%98%E8%BF%9B%E6%96%99.jpg)

- **挤出机**：如果绿灯亮起，则表示挤出机的霍尔开关检测到有耗材进入。

## 控制

### 控制

![控制-中.jpg](https://wiki.bambulab.com/a1-screen-operation/%E6%8E%A7%E5%88%B6-%E4%B8%AD.jpg)

1. **喷嘴温度**：输入数值，设置喷嘴温度。
2. **热床温度**：输入数值，设置热床温度。
3. **打印速度**：设置打印速度模式。

![zh_speed.jpg](https://wiki.bambulab.com/a1/screen-operation/zh_speed.jpg)

- **狂暴**：正常打印速度和加速度的 166%
- **运动**：正常打印速度和加速度的 124%
- **标准**：正常打印速度和加速度
- **静音**：正常打印速度和加速度的 50%

4. **风扇设置**：开启或关闭部件冷却风扇，并设置转速。

![a1-fan中.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-fan%E4%B8%AD.jpg)

部件冷却风扇：

![](https://wiki.bambulab.com/a1m/part-cooling-fan/part_cooling_fan_a1.jpg)

5. **LED 补光灯**：点击按钮可控制 LED 补光灯。

![](https://wiki.bambulab.com/n1/manual/ui-explanation/cn-version/%E4%B8%BB%E7%95%8C%E9%9D%A2_2_%E6%89%93%E5%8D%B0%E8%BF%9B%E7%A8%8B_5.jpg)

6. **挤出机**：点击上下按钮，手动挤出或退出 1 cm 耗材。如果绿灯亮起，则表示挤出机的霍尔开关检测到有耗材进入。

### XYZ

![a1-xyz--.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-xyz--.jpg)

1. **XY 轴控制盘**

- X/-X：点击按钮，控制工具头在 X 轴上左右移动；
- Y/-Y：点击按钮，控制热床在 Y 轴上前后移动。
- 回中：点击中间回中按钮，控制所有轴归零。

2. **X 轴升降控制**：点击移动按钮，沿 Z 轴上下升降 X 轴。

## 设置

|  |  |
| --- | --- |
|  |  |
|  |  |

### 账号

![20240930-110951.jpg](https://wiki.bambulab.com/a1-screen-operation/20240930-110951.jpg)

用 Bambu Handy 扫描二维码，可登入账号。

### WLAN

![a1-wangluo.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-wangluo.jpg)

设置打印机网络，查看 IP 地址和 MAC 端地址。

### 设备

|  |  |
| --- | --- |
|  |  |

- **型号**：查看打印机型号。
- **打印机序列号**：查看打印机序列号。
- **AMS 序列号**：查看 AMS 序列号。
- **相机**：查看相机状态。
- **打印时间**：查看设备使用时长。
- **体验改善计划**：开启后，可将机器的数据（例如打印时长、报错信息等）上传至官方后台，方便后续统计和改善。

### SD 卡

|  |  |
| --- | --- |
|  |  |

查看打印机 SD 卡容量，弹出 SD 卡，或进行格式化设置。

### 维护

![20251218-120351.jpg](https://wiki.bambulab.com/a1/screen-operation/20251218-120351.jpg)

- **校准**：通过电机降噪、振动补偿和自动热床调平来进行打印机校准。

![校准.jpg](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/screen2-cn.jpg)

1. **电机降噪**：减少打印时电机的噪音，尤其是长时间或高速打印时，让打印表面更光滑。
2. **振动补偿**: 在打印中检测到振动时，可实时调整工具头的位置，保证打印的精确度。
3. **自动热床调平**：调整喷嘴与打印板的距离，确保每个角落间隙一致，提高打印精度。

- **喷嘴**：如更换过配件，可重新设置喷嘴，以保证打印质量。

![a1-喷嘴.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E5%96%B7%E5%98%B4.jpg)

- **维护模式**：选择是否开启维护模式。

![a1-维护模式.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E7%BB%B4%E6%8A%A4%E6%A8%A1%E5%BC%8F.jpg)

### 打印选项

|  |  |
| --- | --- |
|  |  |

- **声音**：如开启选项，打印机在开机、打印开始和打印结束时都会发出提示音。
- **缠料检测**：当打印机检测到料线打结后，会自动暂停打印并弹出缠料的提醒。请参考[此文章](../ams-lite/manual/filament-tangle-monitoring-intro.md)了解更多相关信息。
- **丢步自动恢复**：当电机在工作过程中检测到位置偏移（即丢步）时，X、Y 和 Z 轴将会重新回中进行定位，然后回到丢步前的位置重新执行未被执行的 G code，保证打印质量。请参考[此文章](https://wiki.bambulab.com/zh/studio-handy/print-options#%E8%87%AA%E5%8A%A8%E4%BB%8E%E4%B8%A2%E6%AD%A5%E4%B8%AD%E6%81%A2%E5%A4%8D)了解更多相关信息。
- **裹头检测**：当打印机检测到喷嘴被耗材包裹后，会自动暂停打印并提醒，尽可能避免裹头后继续打印对打印机造成更大的伤害。请参考[此文章](../a1-mini/manual/nozzle-warp-detection.md)了解更多相关信息。
- **打印板位置检测**：打印机在打印开始前能检测用户是否放置了打印板，避免直接在热床上打印，导致打印失败甚至损坏热床。请参考[此文章](../a1-mini/manual/build-plate-detection.md)了解更多相关信息。

### AMS 选项

|  |  |
| --- | --- |
|  |  |

- **AMS 类型**：选择需要连接的 AMS 类型（需升级至 01.07.00.00 及以上的固件版本），请参考[此文章](../a1/manual/ams-connection-guide.md)了解 A1 系列打印机可连接的 AMS 类型、数量和具体连接步骤。

- **开机时读取**：开机时读取耗材 RFID。
- **AMS 自动续料**：AMS lite 上某槽耗材用尽后，可自动切换到其他槽位相同属性的耗材。请参考[此文章](https://wiki.bambulab.com/zh/ams/manual/ams-function-introduction#%E6%96%AD%E6%96%99%E6%A3%80%E6%B5%8B%E5%92%8C%E8%87%AA%E5%8A%A8%E7%BB%AD%E6%96%99%E5%8A%9F%E8%83%BD)了解更多相关信息。
- **空打检测**：当打印机配合 AMS lite 打印时，打印机会实时监测 AMS lite 对应槽中里程轮传感器信息。当检测到挤出机无法挤出料，出现空打现象，打印机将自动切断耗材并退料，暂停打印任务并报告错误。请参考[此文章](../ams-lite/manual/air-printing-detectiong.md)了解更多相关信息。

- **重新排序 AMS**：连接多个 AMS 后，可选择重新排序 AMS，自定义每台 AMS 的 ID。

### 相机选项

![a1-相机选项.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E7%9B%B8%E6%9C%BA%E9%80%89%E9%A1%B9.jpg)

- **视频**：在打印过程中进行实时录制视频。
- **延时摄影渐变模式**：开启后，打印首层时会出现裁切放大的效果。随着层数的增加，画面逐渐由放大转变为缩小。请参考[此文章](../software/bambu-studio/Timelapse.md)了解更多相关信息。

### 固件

![a1-固件.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E5%9B%BA%E4%BB%B6.jpg)

查看设备当前版本、该版本的发行说明及离线更新。

### 语言

![a1-选语言.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E9%80%89%E8%AF%AD%E8%A8%80.jpg)

选择打印机屏幕的显示语言。

### 屏幕关闭时间

![a1-休眠时间.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E4%BC%91%E7%9C%A0%E6%97%B6%E9%97%B4.jpg)

选择打印机屏幕的自动休眠时长。

### 局域网模式

![a1-局域网.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E5%B1%80%E5%9F%9F%E7%BD%91.jpg)

开启后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。

### 使用条款

![a1-条款.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E6%9D%A1%E6%AC%BE.jpg)

扫码查看设备使用条款和隐私政策。

### 恢复出厂设置

![a1-恢复出厂.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E6%81%A2%E5%A4%8D%E5%87%BA%E5%8E%82.jpg)

将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

## 助手

![a1-助手.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E5%8A%A9%E6%89%8B.jpg)

如打印机出现故障，可在此查看相关故障和解决方案。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)
