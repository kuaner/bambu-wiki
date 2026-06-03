---
path: zh/h2/troubleshooting/hotend-not-installed
title: "05FF-4094：H2D/H2D Pro/H2C"
description: ""
tags: []
created: 2025-12-23T08:40:31.016Z
updated: 2025-12-31T08:40:15.920Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/hotend-not-installed
---

## 故障描述

打印机在校准前会检查热端是否正确安装，热端未安装或安装不到位就会触发本告警。

> **重要提醒 ！**  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，确保安全有效地执行维护工作。

## 排故措施：检查热端安装状态

- **第1至4步** 适用于H2D/H2D Pro两侧热端，H2C的左侧热端。
- **第5步** 适用于H2C的右侧感应热端

### 第1步 打开工具头前盖组件

捏住工具头前盖顶部的两角处，向上提起，解锁最上方的圆角矩形卡扣，移除工具头前盖。  
![](https://wiki.bambulab.com/h2/6.png)

### 第2步 移除热端硅胶套

向右拨动连杆，使堵嘴片堵住右热端。  
![](https://wiki.bambulab.com/h2/manual/%E6%8B%A8%E5%8A%A8%E8%BF%9E%E6%9D%86.webp)  
用手握住左侧热端硅胶套的两侧，用力斜向下拉，取下硅胶套。  
![](https://wiki.bambulab.com/h2/11.png)

### 第3步 检查热端是否正确安装

1. 检查热端与底座是否完全的贴合，热端上的突起会嵌入至加热底座上的凹槽。（此图示为P2S，但适用于H2S。）

![p2s_hotend.png](https://wiki.bambulab.com/h2/troubleshooting/calibrate-failed/p2s_hotend.png)  
2. 检查热端卡扣是否如图正确扣紧（先合上左侧金属板，再压紧右侧压环）。

![](https://wiki.bambulab.com/h2/17.%E6%89%A3%E7%B4%A7%E5%8D%A1%E6%89%A3.webp)

注意，图左的卡扣错误锁紧是因为同时向下拨动拨片与卡扣，导致拨片错误卡进了卡扣中。因此，请务必将左边的拨片完全贴合喷嘴后，再去拨动右边的卡扣。

|  |  |
| --- | --- |
| ams_int_board_1 | pry_up_the_interface_board |

3. 用手摇晃热端是否松动，若不松动则正确安装。

![](https://wiki.bambulab.com/h2/manual/%E9%AA%8C%E8%AF%81%E7%83%AD%E7%AB%AF%E5%8A%9F%E8%83%BD.gif)

### 第4步 安装热端硅胶套

将硅胶套自下而上安装到热端上。确保硅胶套安装后平整不和周围塑胶件接触。

![](https://wiki.bambulab.com/h2/20.png)

### 第5步 检查感应热端是否正确安装

向左推动感应热端锁紧拉柄至图示位置，用手晃动感应热端，无松动情况，确保感应热端被锁紧。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend/019.webp)

> 注意事项：请检查感应热端带有两个开孔的一端是否朝向前方，然后再进行固定操作。
>
> ![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend/009.png)

### 第6步 合上工具头前盖组件

装回工具头前面盖的时候，可以先扣入挤出机下方的位置，再往前推，听到咔哒声，即安装到位。

![](https://wiki.bambulab.com/h2/21.png)

### 第7步 重新校准

完成以上排查步骤后，请在打印机屏幕上点击**重新校准**。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
