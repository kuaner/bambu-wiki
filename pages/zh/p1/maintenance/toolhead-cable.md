---
path: zh/p1/maintenance/toolhead-cable
title: "更换 P1 系列工具头数据线"
description: "本文介绍拆装 P1 系列打印机工具头数据线的详细步骤和注意事项。"
tags: ["p1", "p1p", "p1s"]
created: 2022-12-08T09:37:49.421Z
updated: 2026-10-10T06:53:42.290Z
source: https://wiki.bambulab.com/zh/p1/maintenance/toolhead-cable
---

## 工具头数据线

即 MC 板到工具头的通信线。

![](https://wiki.bambulab.com/p1/maintenance/mc-th-cable/toolhead_cable_new_1.jpg)

## 工具

H2.0/1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆除

### **第 1 步 -** 拆除后面板

移除[P1P 后面板](rear-panel.md)/[P1S 后面板（金属）](p1s-rear-panel.md)， 然后从 MC 板上断开工具头数据线的连接。

|  |  |
| --- | --- |
|  |  |

### **第 2 步 -** 移除工具头后盖

用 H1.5 内六角扳手拧下工具头后盖的 4 颗螺丝，移除工具后盖。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 - 移除**挤出主板(TH 板)

断开挤出排线和电机线，用 H1.5 内六角扳手拧下 3 颗螺丝，松出挤出主板。然后翻转挤出板，断开电缆在挤出主板端的连接，取下挤出主板。

|  |  |
| --- | --- |
|  |  |

### **第 4 步 -** 电缆与料管分离

请参考[更换 P1 系列拖链组件](cable-chain.md)相关内容，将电缆上的拖链拆除。

![分离线缆.jpg](https://wiki.bambulab.com/p1/maintenance/cable_chain/%E5%88%86%E7%A6%BB%E7%BA%BF%E7%BC%86.jpg)

然后将电缆从 3 个线卡上松脱出来，使其与料管分离。

![](https://wiki.bambulab.com/p1/maintenance/mc-th-cable/release_the_cable_from_clips.jpg)

### **第 5 步 -** 移除 MC-TH 连接线

将 MC-TH 连接电缆从线槽中松出，抽出电缆。

|  |  |
| --- | --- |
|  |  |

## 安装

### **第 1 步 -** 穿线

将电缆的两端分别穿过过线孔，并将线压入线槽内。

|  |  |
| --- | --- |
|  |  |

### **第 2 步 -** 连接电缆

先连接 MC 板，再连接挤出主板。

![](https://wiki.bambulab.com/p1/maintenance/mc-th-cable/2_connectors_2.jpg)

MC-TH 连接器是有方向性的，所以请确认插座没有浮起或者被错插排，或者插反（引线的方向应该朝上）。

![toolhead-cable-12.png](https://wiki.bambulab.com/p1/toolhead-cable-12.png)

左边 2 种情况属于插错排了，这会导致 HMS 报错。最右边的这种安装方式才是正确的

![toolhead-cable-56.png](https://wiki.bambulab.com/p1/toolhead-cable-56.png)

左边的插头被插反了，您可以通过对比工具头线缆座子上的文字方向是否和 TH 板上的文字方向是否一致来确认。如果该插头被插反了，会导致打印机的电源短路。

### **第 3 步 -** 安装挤出主板

将挤出主板翻转过来，电机接口朝外，安装到工具头上，锁入 3 颗螺丝固定，连接挤出排线和电机线。

![](https://wiki.bambulab.com/p1/maintenance/mc-th-cable/3_screws_and_2_connectors.jpg)

### **第 4 步 -** 安装工具头后盖

安装工具头后盖，锁入 4 颗螺丝。

|  |  |
| --- | --- |
|  |  |

### **第 5 步 -** 安装拖链与后面板

请参考[更换 P1 系列拖链组件](cable-chain.md)，将拖链安装到线缆上。

![取下尾部两节_(2).jpg](https://wiki.bambulab.com/p1/maintenance/cable_chain/%E5%8F%96%E4%B8%8B%E5%B0%BE%E9%83%A8%E4%B8%A4%E8%8A%82_(2).jpg)

最后，安装 [P1P 后面板](rear-panel.md)/[P1S 后面板（金属）](p1s-rear-panel.md) 。

![](https://wiki.bambulab.com/p1/maintenance/excess-chute/rear_panel_installed.jpg)

## 如何验证完成

1. 目视检查外观，接合位置无错位、浮起；

2. 启动打印机，运行设备校准流程，如校准通过，说明操作成功。

![32.校准.jpg](https://wiki.bambulab.com/p1/screen-operation/%E5%B1%8F%E5%B9%95%E6%93%8D%E4%BD%9C/32.%E6%A0%A1%E5%87%86.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
