---
path: zh/p2s/troubleshooting/purge-wiper-position-calibeation
title: "P2S/X2D 喷嘴吐料位置标定"
description: "本文将为您介绍当喷嘴吐料时偏离吐料组件应该如何重新进行位置标定。"
tags: []
created: 2025-10-20T17:07:34.488Z
updated: 2026-05-19T02:47:49.023Z
source: https://wiki.bambulab.com/zh/p2s/troubleshooting/purge-wiper-position-calibeation
---

## 故障现象

在使用过程中当出现吐料偏移或者堆料的情况，可能是由于吐料时喷嘴位置偏移导致。以下内容将指导您验证这种情况是否是因为喷嘴吐料偏移导致，以及如何进行位置标定。

|  |  |
| --- | --- |
|  |  |

## 吐料位置左右偏移（X 偏移）标定

### 标定前所需文件

判断吐料是否偏移（P2S/X2D 共用）：[purge\_pos\_test.gcode](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/purge_pos_test.gcode)

P2S 校准文件: [cali.7z](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/cali.7z)  
X2D 校准文件：[x2d\_trash\_cali.zip](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/x2d_trash_cali.zip)

### 验证是否存在吐料偏移

将吐料偏移检测文件（[purge\_pos\_test.gcode](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/purge_pos_test.gcode)）存入 U 盘根目录，插入设备后发起打印。

![9.png](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/9.png)

观察喷嘴是否对齐吐料组件挡板凹槽处。**不同的偏移程度，对应不同故障排查方法。**

> X2D 以左喷嘴与左侧吐料组件 V 型口为观察点。  
> ![x2d33.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/x2d33.jpg)

![图片1.png](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/%E5%9B%BE%E7%89%871.png)

#### 1. 对准：非工具头问题，请进行以下检查:

- 轻推垃圾盒推料板，确认是否存在不可弹回的左右偏移(推出状态下)。
- 目检垃圾盒是否歪斜，与内衬安装部是否发生变形；轻推垃圾盒，确认左右及上下固定是否牢固。
- 检查同步带是否松垮，确认张紧力，排除跳齿可能。

#### 2. 轻微偏移：工具头到垃圾桶的坐标偏移

- 请参照下文使用**校准文件**进行手动标定。

#### 3. 较大偏移：工具头回中出现问题

- 请检查下图框出的位置是否有物体阻碍工具头回中。

|  |  |
| --- | --- |
| P2S X 轴回中位置 | P2S Y 轴回中位置 |

|  |  |
| --- | --- |
| X2D X 轴回中位置 | X2D Y 轴回中位置 |

### 手动标定

#### 1. 准备校准文件

解压校准文件，并将解压后的所有 G-code 文件复制至 U 盘根目录。该文件包包含适配不同喷嘴与垃圾桶偏移量的专用校准文件。

![9.png](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/10.png)

> 例如:  
> “offset (-3\_0mm)\_cali” 表示喷嘴组件向左偏移 3mm，  
> “offset (+3\_0mm)\_cali” 则表示喷嘴组件向右偏移 3mm。

#### 2. 插入 U 盘

将存储有校准文件的 U 盘正确插入打印机的 USB 接口。

![u.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/offline-firmware-update/u.jpg)

#### 3. 执行校准文件

先运行基准校准文件（offset -0\_0mm），运行该文件后喷嘴会自动完成坐标设定，并移动至垃圾桶吐料位置；  
此时观察喷嘴与吐料组件凹槽的实际偏移量，根据偏移方向选择对应校准文件进行精准修正。

|  |  |
| --- | --- |
|  |  |

示例： 如下图所示，喷嘴在吐料组件凹槽位置明显偏右，请执行 -3\_0mm 对应的校准文件，以将喷嘴的目标坐标向左侧修正。

|  |  |
| --- | --- |
|  |  |

> 如果喷嘴位于凹槽左侧，请选择正值的校准文件向右，例如 offset（+2\_0mm）。

校准过程动图示例:

![move.webp](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/move.webp)

完成手动标定后，请确保喷嘴与下方吐料组件的凹槽保持中心对齐； 正确坐标信息将自动保存至打印机的固件中。

![7.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/%E4%BF%AE%E6%94%B9%E5%9B%BE%E7%89%87%E8%99%9A%E7%BA%BF%E9%A2%9C%E8%89%B2d.png)

## 吐料位置前后偏移（Y 偏移）调整

当打印机出现吐料偏出吐料刮板外侧时，请按以下步骤调整吐料刮板位置。

![吐料偏移示意图](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/%E5%A0%86%E6%96%99_compressed.png)

### 步骤一：打开废料滑梯顶盖

1. 拧松吐料滑梯顶盖的四颗固定螺丝
2. 向上抬起顶盖（注意：无需完全移除）

![打开顶盖](https://wiki.bambulab.com/p2s/1.jpg)

### 步骤二：调整刮板固定螺丝

1. 找到刮板下方的两颗固定螺丝
2. 将螺丝拧松（拧松即可，无需移除）

![固定螺丝位置](https://wiki.bambulab.com/p2s/2.jpg)

### 步骤三：安装废料滑梯顶盖

拧松螺丝后，用螺丝刀将金属刮片向前推到最前位置：

|  |  |
| --- | --- |
|  |  |

### 步骤四：固定刮板

1. 调整到位后，重新锁紧两颗固定螺丝
2. 确保刮板位置稳固无松动  
   ![锁紧螺丝](https://wiki.bambulab.com/p2s/3.jpg)

### 步骤五：测试运动

1. 重新安装吐料组件顶盖
2. 前后推动顶盖，测试刮板运动是否顺畅

|  |  |
| --- | --- |
|  |  |

## 吐料位置上下偏移（Z 偏移）调整

喷嘴与擦嘴块距离过远的调整方法，需要打印调整块辅助，请下载 [p2s\_scrap\_block.3mf](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/p2s_scrap_block.3mf) 并打印一个。  
![far.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/far.jpg)

### 第 1 步 - 移除背板

参考 [更换 P2S 背板](../maintenance/replace-rear-panel.md)的相关指引，移除料管支架、缓冲器及背板。

### 第 2 步 - 松开线缆

松开理线扣，取下线缆，露出固定吐料组件的两颗螺丝。  
![release_cables002.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-purge-wiper/release_cables002.jpg)

### 第 3 步 - 移除吐料组件

用 H2.0 的螺丝刀拧松 2 颗固定吐料组件的螺丝，确保吐料组件能够上下推动。  
![remove_the_purge_wiper003.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-purge-wiper/remove_the_purge_wiper003.jpg)

### 第 4 步：安装调整块

将擦嘴块取下后，安装调整块。

![flash.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/flash.jpg)  
![install.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/install.jpg)

### 第 5 步：调整吐料组件

向上推动吐料组件，当调整块上表面接触喷嘴时，拧紧吐料组件固定螺丝。  
![adjust1.webp](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/adjust1.webp)

当调整块上表面接触喷嘴时，拧紧吐料组件固定螺丝。  
![look.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/look.jpg)  
![remove_the_purge_wiper003.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-purge-wiper/remove_the_purge_wiper003.jpg)

### 第 6 步：安装擦嘴块

将调整块取下，安装擦嘴块，并观察喷嘴是否能够接触到擦嘴块。

![adjust.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/adjust.jpg)  
![finish.jpg](https://wiki.bambulab.com/p2s/troubleshooting/purge-wiper-position-calibeation/finish.jpg)

### 第 7 步：安装剩余组件

将线缆固定在理线扣中。  
![install_cables006.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-purge-wiper/install_cables006.jpg)

再参考这篇 Wiki 重新装回背板、缓冲器及料管支架：[更换 P2S 背板](../maintenance/replace-rear-panel.md)

## 功能验证

再次执行打印测试，确认没有出现吐料偏移或堆料的情况。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
