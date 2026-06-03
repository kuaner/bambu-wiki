---
path: zh/x1/manual/screen-operation
title: "X1 系列屏幕操作指南"
description: "本指南介绍了 X1 系列的屏幕操作"
tags: ["x1", "x1c", "x1e"]
created: 2024-09-11T07:25:06.007Z
updated: 2026-02-09T09:17:46.308Z
source: https://wiki.bambulab.com/zh/x1/manual/screen-operation
---

## 介绍

本指南旨在介绍 X1 系列打印机屏幕按键及操作功能。

## 主页

![home.png](https://wiki.bambulab.com/screen-operation/home.png)

主页左侧为屏幕菜单栏，包括**主页**、**控制**、**耗材**、**设置**和 **HMS**；右侧为**打印文件**、**喷嘴温度**、**耗材**、**网络设置**和**HMS**，点击图标能快速跳转至对应的控制界面。

## 控制

![控制.jpg](https://wiki.bambulab.com/screen-operation/%E6%8E%A7%E5%88%B6.jpg)

### 1. 风扇

开启或关闭部件冷却风扇、辅助部件冷却风扇及腔体外排风扇，并设置转速。

![fan.png](https://wiki.bambulab.com/screen-operation/fan.png)

- 部件冷却风扇：装在工具头上，用于确保在打印过程中充分冷却打印层，有助于在挤出时快速冷却耗材，使每一层都能在下一层沉积之前凝固并保持原始形状。

![部件冷却风扇.png](https://wiki.bambulab.com/screen-operation/%E9%83%A8%E4%BB%B6%E5%86%B7%E5%8D%B4%E9%A3%8E%E6%89%87.png)

![partcoolingfan.png](https://wiki.bambulab.com/screen-operation/partcoolingfan.png)

- 辅助部件冷却风扇：装在机腔内左侧，能为高速打印提供更好的冷却条件。

![](https://wiki.bambulab.com/x1/maintenance/replace-aux-fan/new_fan.jpg)  
![auxfan-cn.png](https://wiki.bambulab.com/screen-operation/auxfan-cn.png)

- 腔体外排风扇：装在打印机右内衬上，主要用于调节打印机机箱内部的温度。

![机箱风扇.png](https://wiki.bambulab.com/screen-operation/%E6%9C%BA%E7%AE%B1%E9%A3%8E%E6%89%87.png)  
![exhaustfan.png](https://wiki.bambulab.com/screen-operation/exhaustfan.png)

### 2. 速度

设置打印速度模式。

![speed.png](https://wiki.bambulab.com/screen-operation/speed.png)

- **狂暴**：正常打印速度和加速度的 166%
- **运动**：正常打印速度和加速度的 124%
- **标准**：正常打印速度和加速度的 100%
- **静音**：正常打印速度和加速度的 50%

> 注意：**从屏幕上更改速度只能提高打印速度，并不能调整热端温度来进行补偿**。建议在屏幕上调整较高打印速度时使用较低的层高，并正确调整打印设置，避免打印失败。

### 3. 运动

- **工具头**：点击 1 格或 10 格的移动按钮，控制工具头在 X 轴和 Y 轴上移动。
- **热床**：点击 1 格或 10 格的移动按钮，升降热床。

![](https://wiki.bambulab.com/h2/manual/screen-operation/xyz.png)

### 4. 喷嘴和挤出机

![20250513-165810.jpg](https://wiki.bambulab.com/screen-operation/20250513-165810.jpg)

1. **挤出机：** 点击上下按钮，手动挤出或退出 1 cm 耗材。

![霍尔.png](https://wiki.bambulab.com/x1/troubleshooting/hmscode/ams/filament_broken_in_extruder/%E6%8C%A4%E5%87%BA%E6%9C%BA%E9%9C%8D%E5%B0%94%E4%BC%A0%E6%84%9F%E5%99%A8%E4%BD%8D%E7%BD%AE.jpeg)

如果绿灯亮起，则表示挤出机的霍尔开关检测到有耗材进入。

![小绿点.jpg](https://wiki.bambulab.com/screen-operation/%E5%B0%8F%E7%BB%BF%E7%82%B9.jpg)

2. **喷嘴温度**：输入数值，设置喷嘴温度。

![nozzletemp.png](https://wiki.bambulab.com/screen-operation/nozzletemp.png)

3. **喷嘴类型**：可手动设置喷嘴的类型、材质及直径。

![nozzletype.png](https://wiki.bambulab.com/screen-operation/nozzletype.png)

### 5. 机箱

显示被动腔温。（X1E 可以主动设置腔温，请参考：[X1E 腔温设置指南](X1E-chamber-temp-guide.md)）

### 6. 热床

输入数值，设置热床温度。

![heatbedtemp.png](https://wiki.bambulab.com/screen-operation/heatbedtemp.png)

### 7. 照明

点击此按钮可控制 LED 补光灯。

![20250513-201218.jpg](https://wiki.bambulab.com/screen-operation/20250513-201218.jpg))

## 耗材

![20250513-172754.jpg](https://wiki.bambulab.com/screen-operation/20250513-172754.jpg)

### 1. **料盘**

点击任一料盘图标，可进行耗材编辑、进退料和 RFID 重读操作；

![20250513-173122.jpg](https://wiki.bambulab.com/screen-operation/20250513-173122.jpg)

- **编辑：**如果 AMS 已通过 RFID 识别该料盘信息，可在此处查看料盘信息，但无法修改耗材参数；如果未读取 RFID，则可在此处修改耗材信息。

已读取 RFID：  
![editfilament.png](https://wiki.bambulab.com/h2/manual/screen-operation/image-4.png)

未读取 RFID：  
![editfilament.png](https://wiki.bambulab.com/screen-operation/editfilament.png)

- **进料：**点击按钮，AMS 会自动将耗材进料至挤出机；
- **重读：**点击按钮，AMS 会重新读取该槽位的 RFID。

### 2. 湿度

可查看 AMS 内部的湿度。

如果连接了 AMS 2 Pro，则会显示 AMS 2 Pro 内部的湿度和温度，点击可进入烘干页面，对耗材进行烘干。

![20250513-175224.jpg](https://wiki.bambulab.com/screen-operation/20250513-175224.jpg)  
![](https://wiki.bambulab.com/h2/manual/screen-operation/drying.png)

### 3. **外挂料盘**

如使用外挂料盘，可在此处配置耗材颜色及类型。*无论外挂料盘是否有料，该项信息始终会显示。*

### 4. **工具**

![filamenttool.png](https://wiki.bambulab.com/screen-operation/filamenttool.png)

**自动续料**：当前耗材用完时，打印机会按设定顺序自动切换到其他槽位相同属性的耗材。需确保槽中有信息相同的耗材，且 AMS 上相应的槽信息一致。请在 AMS 设置中启用此功能。

![auto-refill-cn.png](https://wiki.bambulab.com/screen-operation/auto-refill-cn.png)

如果连接了 AMS 2 Pro，此处还会显示“AMS 烘干”功能，点击可进入烘干页面，对耗材进行烘干。

![20250513-180056.jpg](https://wiki.bambulab.com/screen-operation/20250513-180056.jpg)  
![](https://wiki.bambulab.com/h2/manual/screen-operation/drying.png)

### 5. **指南**

对进料操作进行说明：选择特定槽位，点击料盘图标，再点击进料按钮，即可触发自动进料。

![filament-guide.png](https://wiki.bambulab.com/screen-operation/filament-guide.png)

## 设置

![20250513-192437.jpg](https://wiki.bambulab.com/screen-operation/20250513-192437.jpg)

### 1. 账号

用 Bambu Handy 扫描二维码，可登入账号。

![20250513-192746.jpg](https://wiki.bambulab.com/screen-operation/20250513-192746.jpg)

### 2. **Wi-Fi**

可设置打印机网络，测试网络连接，查看当前网络，或查看和添加其他网络。

![network.png](https://wiki.bambulab.com/screen-operation/network.png)

### 3. **USB 存储**

- **存储：**显示 U 盘已使用容量和该 U 盘的最大容量；
- **格式化外部存储：**可将 U 盘存储格式化。一旦重设，存储将无法恢复。

![sdcard-.png](https://wiki.bambulab.com/screen-operation/sdcard-.png)

### 4. **固件**

查看设备当前版本和历史版本，或进行离线升级。如固件需更新时，右上角“更新”按钮会变亮。  
![firmware.png](https://wiki.bambulab.com/screen-operation/firmware.png)

### 5. **打印校准**

![calibration.png](https://wiki.bambulab.com/screen-operation/calibration.png)

- **激光雷达校准：** 调整激光器和相机的位置，确保激光线在不同位置的图像清晰准确。

- **电机降噪：** 减少打印时电机的噪音，尤其是长时间或高速打印时，让打印表面更光滑。
- **振动补偿：** 在打印中实时监测并检测到任何震动时，可自动调整工具头位置，以确保打印的精确度。
- **自动热床调平：** 调整喷嘴与打印板的距离，确保每个角落间隙一致，提高打印精度。

### 6. 工具箱

![toolbox.png](https://wiki.bambulab.com/screen-operation/toolbox.png)

1. **设备自检：** 打印机如遇故障，可通过检查来诊断设备，发现问题。

![selftest.png](https://wiki.bambulab.com/screen-operation/selftest.png)

2. **烘干耗材：** 设置烘干温度及时长，对耗材进行烘干处理。请参考[耗材烘干操作指南](../../filament-acc/filament/dry-filament.md)了解更多信息。

![drying.png](https://wiki.bambulab.com/screen-operation/drying.png)

3. **碳管清洁：** 较多挥发物质聚集会导致碳管阻力变大，导致打印机精度下降。如果打印机的碳管需要清洁时，此页面会进行提示，请扫描右侧二维码查看教程。

![carbonrodcleaning.png](https://wiki.bambulab.com/screen-operation/carbonrodcleaning.png)

4. **丝杆润滑：** 三根 Z 轴丝杆驱动热床执行垂直运动，需定期润滑以维持运动平稳性。如果打印机的丝杆需要润滑时，此页面会进行提示，请扫描右侧二维码查看教程。

![leadscrew.png](https://wiki.bambulab.com/screen-operation/leadscrew.png)

### 7. 设置

![settings-cn-1.jpg](https://wiki.bambulab.com/screen-operation/settings-cn-1.jpg)  
![settings-cn-2.jpg](https://wiki.bambulab.com/screen-operation/settings-cn-2.jpg)

1. **打印选项**：

![printoptions.png](https://wiki.bambulab.com/screen-operation/printoptions.png)  
![printoptions2-en.png](https://wiki.bambulab.com/screen-operation/printoptions2.png)

- **AI 打印监控**：在打印过程中检测炒面、废料槽堆积以及裹头问题，并选择暂停打印的灵敏度；暂停打印的灵敏度分为高（发现小问题立即暂停）、中（出现一定程度问题时暂停）和低（仅在明显异常时暂停），以适应不同的打印质量需求。

- **打印板检测**：检测打印板标记。如果标记不在预定义范围内，或与切片文件不符，打印机将停止打印，可避免未放置或放错打印板的情况。

- **首层扫描**：首层打印完成后，系统会自动检测打印质量，并在发现异常时发出警告。

- **丢步自动恢复**：当电机检测到位置偏移（丢步）时，X、Y 和 Z 轴会重新定位，并回到偏移前的位置继续执行未完成的 G-code，以保证打印质量。
- **开门检测**：开启后，打印机将检测前玻璃门是否打开，可选择在门打开时触发通知或暂停打印。

- **缓存远程打印文件到外部存储中**：通过云端发起的打印，打印文件将缓存到 SD 卡根目录的文件夹中。

2. **AMS 选项：**

![amssetting.png](https://wiki.bambulab.com/screen-operation/amssetting.png)  
![amssetting2.png](https://wiki.bambulab.com/screen-operation/amssetting2.png)

- **插入耗材时读取：**在插入耗材预上料后，AMS 会进行 RFID 读取操作。
- **开机时读取**：每次重启打印机时，AMS 会自动读取插入的耗材信息，并且读取过程中会转动耗材。
- **剩余容量估计**：在读取 RFID 过程时对耗材进行余料估算。开启该功能后，RFID 会进行两次读取，分别获取耗材信息和估算剩余量。在读取完耗材的 RFID 和余量信息后，可以在每个槽位上方查看耗材名称，耗材名称下方的小横条中显示的就是估算出来的耗材余量。请参考[AMS 主要功能和工作流程介绍](https://wiki.bambulab.com/zh/ams/manual/ams-function-introduction#%E4%BD%99%E6%96%99%E4%BC%B0%E7%AE%97)了解更多相关信息。

![剩余容量cn.jpg](https://wiki.bambulab.com/screen-operation/%E5%89%A9%E4%BD%99%E5%AE%B9%E9%87%8Fcn.jpg)

- **AMS 自动续料**：当 AMS 某个槽的耗材用完时，可自动切换到其他槽位上属性完全相同的耗材。这些属性包括品牌、类型、颜色和打印温度等。请确保在打印前配置好所有耗材的信息，以满足自动续料的要求。请参考[AMS 主要功能和工作流程介绍](https://wiki.bambulab.com/zh/ams/manual/ams-function-introduction#%E6%96%AD%E6%96%99%E6%A3%80%E6%B5%8B%E5%92%8C%E8%87%AA%E5%8A%A8%E7%BB%AD%E6%96%99%E5%8A%9F%E8%83%BD)了解更多相关信息。
- **重新排序 AMS**：每个 AMS 都会分配一个顺序，并在屏幕上显示。分配 AMS ID 的目的是方便识别它们之间的连接。分配 ID 的逻辑为：直接连接到打印机的是 AMS-A，连接到 AMS-B 的是 AMS-C，以此类推。如果需要重新排序 AMS，可以点击“重置”，即可重置 AMS 的顺序信息。重置完成后，请按需依次连接 AMS 进行排序。

3. **录像：**设置录像的清晰度。清晰度越高，所需的存储空间越大。

![video.png](https://wiki.bambulab.com/screen-operation/video.png)

4. **自动休眠：**选择打印机自动休眠的时长。

![autosleep.png](https://wiki.bambulab.com/screen-operation/autosleep.png)

5. **语言：**选择打印机屏幕的显示语言。

![language.png](https://wiki.bambulab.com/screen-operation/language.png)

6. **辅助部件冷却风扇：** 如更换过配件，可重新设置辅助部件冷却风扇，以保证打印质量。

![auxfaninstallaion.png](https://wiki.bambulab.com/screen-operation/auxfaninstallaion.png)

7. **设备和序列号：** 查看打印机设备名、设备使用时间和序列号。

![20250513-152516.jpg](https://wiki.bambulab.com/screen-operation/20250513-152516.jpg)

8. **仅局域网：** 开启仅局域网模式后，打印机只能在本地网络内进行连接和访问，不能通过互联网远程访问或控制。如果多个设备通过同一局域网连接，可进行视频直播或数据共享。

![lanonly.png](https://wiki.bambulab.com/screen-operation/lanonly.png)

9. **导出日志到外部存储：**可根据需求，选择是否导出所有打印日志、关键照片（判断炒面等问题）和 G-code（判断打印质量问题）。

![export.png](https://wiki.bambulab.com/screen-operation/export.png)

10. **恢复出厂设置：**将打印机恢复至出厂设置。一旦重设，设定将无法恢复。

![factory.png](https://wiki.bambulab.com/screen-operation/factory.png)

## HMS

如果打印机出现故障，此处将会显示报错信息。

![](https://wiki.bambulab.com/h2/manual/screen-operation/hmscnpage.png)

如需查看更多 HMS 相关信息，请参考 [HMS 主页面](../../hms/home.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[*点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)
