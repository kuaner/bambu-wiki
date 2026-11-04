---
path: zh/h3c/maintenance/replace-power-supply
title: "电源更换指南"
description: ""
tags: []
created: 2026-11-03T12:41:24.328Z
updated: 2026-11-03T12:41:25.390Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-power-supply
---

## 电源

打印机的电源是一个输入电压为 AC 100-240V，输出电压为 DC 24V 的电源转换器，它为整台打印机直流供电。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_27e7638438.jpg)

> 电源连接端子示意图如下，请根据电源上的标识和线缆颜色来连接。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_a8e1a37313.png)

| 序号 | 端子用途 | 线材颜色 | 序号 | 用途 | 线材颜色 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直流正极输出 | 白色 | 4 | 高压零线输入 | 蓝色 |
| 2 | 直流负极输出 | 黑色 | 5 | 高压火线输入 | 棕色 |
| 3 | 共用地线 | 黑色 （直流）/黄绿色（交流） | / |  |  |

## 何时更换

当您确定电源模块的输出电压不正常，或者电源模块板上的元器件有明显的烧坏现象时，可能需要更电源模块。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手
- 十字螺丝刀

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除电源

### 第 1 步 移除 背板

请参考 WIKI：[背板更换指南](replace-back-panel.md)，移除背板。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/12_z________z_motor_replacement_guide_9284139891.jpg)

### 第 2 步 移除电源散热风扇

用 H2.0 内六角扳手移除 2 颗螺丝，然后将散热风扇移动到线费上暂时放置。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_d7970e5b62.jpg)

### 第 3 步 移除电源

用 十字螺丝刀拧松 5 个锁有线缆的端子螺丝，然后将插头全部从电源上松出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_0eca8f6dec.jpg)

用 H2.0 内六角扳手移除 2 颗螺丝，然后向右取下电源。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_a241c59c7e.jpg)

## 安装电源

### 第 1 步 安装电源

将电源装入空置的电源槽位中，锁入 2 颗螺丝进行固定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_0534285110.jpg)

根据以下接线图，将各插头连接到对应的端子上，锁紧螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_ab07258be8.jpg)

| 序号 | 端子用途 | 线材颜色 | 序号 | 用途 | 线材颜色 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直流正极输出 | 白色 | 4 | 高压零线输入 | 蓝色 |
| 2 | 直流负极输出 | 黑色 | 5 | 高压火线输入 | 棕色 |
| 3 | 共用地线 | 黑色 （直流）/黄绿色（交流） | / |  |  |

### 第 2 步 安装电源散热风扇

用 H2.0 内六角扳手移除 2 颗螺丝，然后将散热风扇移动到线缆上暂时放置。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_d7970e5b62.jpg)

将散热风扇上的定位柱与立柱上的安装孔对准，安装电源散热风扇，锁入 2 颗螺丝固定。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/105________power_supply_replacement_guide_1a04ae725d.jpg)

### 第 3 步 安装 背板

请参考 WIKI：[背板更换指南](replace-back-panel.md)，将背板及其他配件安装好。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-power-supply/zh/12_z________z_motor_replacement_guide_2980526540.jpg)

## 功能验证

连接电源线并启动打印机，打印机能正常启动即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
