---
path: zh/ams-lite/manual/intro-ams-lite
title: "AMS lite模块和功能介绍"
description: ""
tags: []
created: 2023-09-18T12:58:35.677Z
updated: 2026-02-11T08:50:06.499Z
source: https://wiki.bambulab.com/zh/ams-lite/manual/intro-ams-lite
---

AMS指的是自动供料系统（Automated Material System），它可以配合3D打印机实现自动化多色打印功能。AMS lite是Bambu lab推出的其中一款自动供料系统，本文将介绍AMS lite供料系统的几大模块、主要功能和工作流程。

|  |  |
| --- | --- |
|  |  |

## 使用前注意事项

1. A1 系列打印机只能接1台 AMS lite，所以最多只能支持4色打印；

2. AMS lite 与 X1 和 P1 系列打印机不兼容；

3. AMS lite 上装的料管有两种规格，1/2 号槽料管的标准长度为 580mm，3/4号槽的料管标准长度为700mm，注意料管别装错；

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E6%91%86%E6%94%BE%E8%B7%9D%E7%A6%BB50mm.jpg)

4.注意不要把AMS lite放在距离打印机太远的位置（建议距离50mm，如上图所示），过度弯折料管会产生过大的送料阻力导致送料失败（如下图）。

![](https://wiki.bambulab.com/n1/hms/filament_stuck/bad_place.png)

**AMS lite 放置距离打印机太远**

5. AMS lite的上下料器一次性最长只能送出1.2m长的料线，所以如需更换更长的料管需要酌情考虑。

6. 在AMS lite上放置料盘的时候，请注意各个槽的耗材配重合适，防止重心不稳打印过程中倒塌。**可以把重一点的耗材放在下面两个槽（2、3号槽）**，重心更低一些会更稳定。

## AMS lite 供料系统

从AMS lite送料到打印机，整个供料系统分为以下两大模块：

**1. AMS lite: 上下料器+回转轴，每个槽各有一个上下料器和回转轴。**

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E4%B8%8A%E4%B8%8B%E6%96%99+%E5%9B%9E%E8%BD%AC%E8%BD%B4.png)

**2. 工具头：缠料检测模块+挤出机+热端。**

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E5%B7%A5%E5%85%B7%E5%A4%B4.png)

### **上下料器**

AMS lite的每个槽都有一个上下料器，负责把耗材送入或者拉出工具头。它有一个耗材检测传感器，如下图所示：

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E4%B8%8A%E4%B8%8B%E6%96%99%E8%BF%9B%E6%96%99%E4%BC%A0%E6%84%9F%E5%99%A8.png)

**耗材检测传感器**

每个上下料器的咬合轮处都有一个里程轮传感器，里程轮是被动轮，只有当它与挤出齿轮一起抓住耗材丝并将其送出时，它才会转。所以它可以用来判断耗材丝是否从AMS中被送出，也可以用来计算送的耗材丝长度。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E9%87%8C%E7%A8%8B%E8%BD%AE.png)

**里程轮**

此外，每个上下料器的直流电机底部各有一个速度传感器，这个速度传感器计算得到的电机转速v1，以及里程轮传感器计算得到的速度v2，比较v1和v2的差值可以判断料线是否在送料的时候打滑了。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA%E9%80%9F%E5%BA%A6%E4%BC%A0%E6%84%9F%E5%99%A8.png)

**电机速度传感器**

### 回转轴

AMS lite的每个槽都有个回转轴，用于放置料盘。回转轴有自动回转的功能，当退料的时候，上下料器会把料线从挤出机中拉出，卷轴也会自动往回转一些，确保收紧料盘上的料线，使其保持张力。回转轴的最大回转角度是150°，所以它无法自动回收太长的料线。

|  |  |
| --- | --- |
|  | **回转轴会自动回转一定角度** |

### 缠料检测模块

工具头上方的缠料检测模块由五通和进料支架组成。AMS lite每个槽对应的送料管接到工具头的五通上，五通将四个料管固定在一块。进料支架侧边连接着霍尔传感器小板，内部有个弹簧，五通下方还有个磁铁，把五通和进料支架组装在一起后，就构成了一个缠料检测模块。当进料阻力过大的时候，缠料检测模块会下压，磁铁就会更靠近霍尔传感器而触发缠料报警。  
请参考Wiki：[缠料检测功能介绍](filament-tangle-monitoring-intro.md)

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E7%BC%A0%E6%96%99%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9D%97.png)

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E7%BC%A0%E6%96%99%E6%A3%80%E6%B5%8B.gif)

## AMS Lite 功能介绍

### 预上料

空闲状态下，插入料线到上下器后，上下料器会自动把料线送入料管约40cm，这个过程就是预上料。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E9%A2%84%E4%B8%8A%E6%96%99.gif)

### 读取 RFID

AMS Lite每个槽都有一个对应的RFID线圈。只需要将料盘放到每个槽的回转轴上，插入料线后就可以读取到该卷耗材的具体信息。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E7%BA%BF%E5%9C%88%E8%AF%BB%E5%8F%96rfid.png)

读取RFID功能默认在插入耗材时读取，无法关闭。

![](https://wiki.bambulab.com/software/zhstudio.jpg)

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E7%82%B9%E5%87%BB%E8%AF%BB%E5%8F%96rfid.png)

### 自定义材料信息

如果您使用的是第三方的材料，您也可以手动编辑材料信息。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E8%87%AA%E5%AE%9A%E4%B9%89%E8%80%97%E6%9D%90%E4%BF%A1%E6%81%AF.png)

### 自动映射功能

在发起多色打印任务时，会自动给模型匹配AMS上最接近颜色的耗材丝。您也可以在发送打印任务的窗口里自定义选择耗材丝。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E9%80%89%E6%8B%A9%E6%98%A0%E5%B0%84.png)

![](https://wiki.bambulab.com/x1/manual/muti-color-print/%E6%98%A0%E5%B0%84%E6%8C%87%E5%8D%97.png)

### 断料检测和自动续料功能

使用AMS lite打印依然具备断料检测功能，不过分为以下两种情况：

**1. 单材料打印：当**工具头的耗材检测传感器检测到没料后，先判断上下料器的传感器是否有检测到料，上下料器如果仍有检测到料的话，工具头会移动到吐料区，继续往挤出机送料，不报错。如果上下料传感器也到没料了，就会报材料用尽，需要插入新的耗材。

\*\*2. 多材料打印：\*\*多材料打印有一种特殊情况，即料盘上的尾料已经脱离料盘送入到进料管内部，此时如果打印中途需要更换耗材，由于料线已经脱离料盘无法拉回，会直接冲刷剩余的料，冲刷完毕后再切换到另一个槽的材料继续打印。屏幕会提示料线用尽，正在冲刷旧料。

\*\*3. AMS自动续料：\*\*AMS上某个槽的耗材用尽后可以自动切换到其他槽位上属性完全相同的耗材，这些属性包括材料品牌、材料类型、材料颜色、材料打印温度等，请在打印前配置好耗材信息。 该功能需要配置的耗材属性完全相同，建议Bambu耗材使用Bambu耗材作为替代料，非Bambu耗材使用非Bambu耗材作为替代料。

![](https://wiki.bambulab.com/software/zhstudio.jpg)

## AMS lite 工作流程

### 换料（进料&退料）

在进料过程，上下料器负责把料线送到工具头，待挤出机咬合轮咬合料线3mm后，上下料器停止工作。挤出机继续往下挤一段料线，如果上下料器对应的里程轮也跟着转动了，则认为此次进料咬合成功。

退料过程中，上下料器和挤出机同时工作，上下料拉回料线，挤出机电机反转送出料线，直到料线被拉回到五通口，则判断为退料成功。

### 料线位置检查

在屏幕上点击进料/退料或者发起打印，如果工具头内部有料线时，都会做料线位置检查。这个检查的目的是看工具头内部料线来自AMS哪个槽还是来自外挂料盘。

对于每个槽来说，而进料传感器只有1个，即上下料器内部的进料霍尔传感器。当4个槽都插着料时AMS lite无法根据进料霍尔准确判断是哪个槽的料线送出了。例如，当它送入1号槽的料，屏幕/Studio上显示1号槽的料线在工具头内（如下图所示）。但是你从工具头自行切断料线，将1号槽料线拉出，并手动进了2号槽的料线，此时由于打印机缺少足够的传感器信息，屏幕上依旧显示的是1号槽的料线与工具头相连接。所以在下一次进退料的时候，它需要做完一次料线位置检查，才可以知道当前料线是来自哪个槽。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/1%E5%8F%B7%E6%A7%BD%E6%96%99%E7%BA%BF%E9%80%81%E5%85%A5.png)

**工具头的料线来自1号槽**

**料线位置检查原理：当工具头有料的时候，它会试图挤出一小段，如果哪个槽的上下料器的里程轮动了，说明材料是来自这个槽。如果无法向下挤出，则会每个槽都依次尝试拉回一小段料线，如果哪个槽拉回后工具头的料线检测传感器检测到没料了，说明料线是来自这个槽。如果上述两个方法都没找到料线的归属槽位，则判断它来自外挂料盘或者是断料**。

![](https://wiki.bambulab.com/f1/ams-lite-introduction/%E6%96%99%E7%BA%BF%E4%BD%8D%E7%BD%AE%E6%A3%80%E6%9F%A5.gif)

### 打印过程

AMS lite 成功送料至挤出机并开始打印后，整个打印过程都由挤出机在拉动料线，AMS lite的上下料器电机并不会工作。所以此时上下料器内部的电机是不转的，而里程轮仍然会转动。
