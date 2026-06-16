---
path: zh/a2l/maintenance/replace-th-board
title: "A2L 更换 TH 板"
description: "本文介绍了如何更换 A2L TH 板"
tags: []
created: 2026-06-01T13:07:57.143Z
updated: 2026-06-05T07:48:26.813Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-th-board
---

## A2L TH板

![dlb074.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/dlb074.png)

## 重要提醒

TH板上的热端风扇、部件风扇和涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。

![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

## 所需的工具和材料

TH 板（请根据实际故障情况选择更换对应配件）

- H1.5 内六角螺丝刀
- 镊子（可选）

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子元件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## 视频指南

## 移除 TH 板

### 步骤 1：移除工具头后盖

用手或镊子尾部扣入工具头后盖底部凹槽内，向上发力即可取下后盖。  
![gjthg001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-toolhead-rear-housing/gjthg001.webp)

### 步骤 2：移除工具头线缆

使用 H1.5 内六角螺丝刀拆下图示四颗螺丝，向上拔除工具头线缆。  
![gjtxl016.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/gjtxl016.jpg)![gjtxl004.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-x-axis-motor-cover/gjtxl004.webp)

### 步骤 3：移除TH板部分插头

![th009.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th009.jpg)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 涡流线圈 | 4 | 热端加热组件 |
| 2 | 热端风扇 | 5 | 进料霍尔板 |
| 3 | 部件风扇 | 6 | A3508挤出电机 |

1、2、3号为同一类型连接器，拔出插头时，**请先清理插头上的胶水，然后用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。  
![th007.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th007.webp)

4号连接器可以直接向上拔出。  
![th008.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th008.webp)

### 步骤 4：移除TH板

使用 H1.5 内六角扳手拧下三颗螺丝。  
![th011.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th011.jpg)

将TH板向外拉出一段距离，断开5、6号连接器，**先向上掀起黑色卡扣解锁，再拔出 FPC 线缆**。  
![th009.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th009.webp)

断开TH板背部的连接线插头，取下TH板。  
![th001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th001.webp)

## 安装 TH 板

### 步骤 1：安装 TH 板

1. 连接转接板： 将新的TH板与麦拉片对齐（注意麦拉片方向），插入背面的插头。  
   ![th002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th002.jpg)![th003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th003.jpg)
2. 翻转TH板，插入进料霍尔板和挤出电机FPC排线。  
   ![th005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th005.webp)![th004.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th004.webp)

> 注意：排线金属触点一面面向TH板方向，将排线插入到底后再扣紧卡扣。

3. 整理两侧线缆，将TH板推入工具头支架内，使用 H1.5 内六角螺丝刀锁入三颗螺丝。  
   ![th006.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th006.jpg)

> 注意：拧紧螺丝前，请务必检查是否有线缆被压在TH板下方！避免锁入螺丝时损坏线缆。

### 步骤 2：连接TH板插头

依次将剩余线缆接回 TH 板。根据不同的插头类型您可以使用不同的方法来连接插头。

![th009.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th009.jpg)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 涡流线圈 | 4 | 热端加热组件 |
| 2 | 热端风扇 | 5 | 进料霍尔板 |
| 3 | 部件风扇 | 6 | A3508挤出电机 |

4号连接器可以直接插入。  
![th03.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/wiki-test/th03.jpg)

1、2、3号为同一类型连接器，将插头与母座对齐后按压到位即可。  
![th02.webp](https://public-cdn.bblmw.com/wiki/new/a2l/wiki-test/th02.webp)

### 步骤 3：安装工具头线缆

将工具头线缆插入工具头，注意需要将插头有凸起的一侧向后对齐槽位插入。  
![gjtxl005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-x-axis-motor-cover/gjtxl005.webp)![pm011.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/wiki-test/pm011.jpg)

使用 H1.5 内六角螺丝刀锁入四颗螺丝固定插头。  
![gjtxl016.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/gjtxl016.jpg)

### 步骤 4：安装工具头后盖

先对齐工具头后盖上方卡扣，然后合上后盖，按压后盖下方左右边缘位置，检查边缘是否扣好。

![rdfs008.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-cooling-fan-for-hotend/rdfs008.webp)

## 如何验证成功

连接电源开机，发起一次打印测试，如果打印过程正常，无异常报错即表示更换成功。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
