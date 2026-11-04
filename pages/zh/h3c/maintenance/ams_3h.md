---
path: zh/h3c/maintenance/ams_3h
title: "AMS 3H 定期维护指南"
description: ""
tags: []
created: 2026-11-03T12:49:32.274Z
updated: 2026-11-03T12:49:33.317Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/ams_3h
---

## 介绍

拓竹AMS 3H是一个智能系统，其中的干燥剂、料管以及齿轮组件需要定期维护以确保其最佳功能和使用寿命。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 更换干燥剂

[干燥剂](../../knowledge-sharing/desiccant-status.md)位于烘干仓盖上，可直接更换。保持 AMS 3H 烘干区域干燥能够提高烘干质量。建议定期检查其状态,失效时应及时烘干或更换。

|  |  |
| --- | --- |
| 图 | 图 |

## AMS 内部组件

### 拆卸 AMS

开机后，在屏幕上选择退出所有耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________d06d2ada93.png)

退料完成后 ，AMS 将自动变为“空状态”。确保 AMS 状态为 “空”后，关闭打印机电源。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________ae9a3869c2.png)

拆卸左右两侧磁吸侧板。

|  |  |
| --- | --- |
| 图 | 图 |

将料头固定在料盘侧孔中，取下所有耗材。

|  |  |
| --- | --- |
| 图 | 图 |

### 维护入料口组件

首先根据[入料口组件更换指南](../../ams3/maintenance/replace-filament-inlet-assembly.md)拆卸入料口组件。使用毛刷或者吹风机清理内部可能存在的碎屑。

> 注：后续操作请勿在该齿面涂抹润滑脂。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________4bc2cb2170.png)

使用一截耗材插入入料口组件，确保入料口中没有断料堵塞。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________024a6708ca.png)

### 维护进料齿轮组

进料组件的齿轮表面需要涂抹消音润滑脂。  
其中1、4与进料功能有关，2、3与选料功能有关。  
注：4 所代表的齿轮总共有 5 组，请勿遗漏。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________4345ebb661.png)

完成后装回设备，正常使用过程中齿轮将得到充分润滑。

### 维护烘干模块

日常使用过程中，烘干模块内风扇扇叶上可能会积累较多灰尘，这会导致风扇转速过低或停转，定期清理灰尘能够保证烘干功能正常进行。  
拧松 AMS 的 4 颗固定螺丝。

|  |  |
| --- | --- |
| 图 | 图 |

抱住 AMS 的前后侧，取下 AMS。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________0f914b3cac.png)

参考 [Wiki](../../ams3/maintenance/replace-heating-unit.md) 取下烘干组件后，使用毛刷清理风扇扇叶，确保外观干净，扇叶转动顺畅。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________6fe51ae1ba.png)

### 维护进/出气口组件

进/出气口组件的齿轮组也需要定期润滑，确保风门切换正常。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/ams_3h/zh/07_ams_3h________4d60a44c9b.png)

### 更换料管

随着时间推移，料管在耗材通过时可能会出现磨损，这会导致送料出现故障或耗材堵塞在料管中，需定期检查是否有磨损迹象,并根据需要更换,确保送料顺畅。请按照原装长度裁剪料管,过长或者过短都可能影响打印。  
料管拆装可参考[Wiki](replace-ptfe-tube.md)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
