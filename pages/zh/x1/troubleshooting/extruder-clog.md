---
path: zh/x1/troubleshooting/extruder-clog
title: "挤出机维护指南：X1 系列挤出机维护"
description: "本指南提供 X1 系列挤出机堵塞清理、挤出机拆解与组装的详细步骤。"
tags: []
created: 2022-07-31T11:32:53.494Z
updated: 2026-06-03T07:53:43.425Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/extruder-clog
---

## 挤出机维护

在本指南中，我们将提供保养挤出机相关组件的常用方法  
挤出机应定期进行维护，挤出机组件对打印起到非常重要的作用。保持挤出机内部的清洁和润滑良好将有效延长挤出机组件的使用寿命，并能确保打印质量一致。

![back-part-removed.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/back-part-removed.png)

## 何时需要维护？

- 工具头内部温度过高，导致驱动齿轮附近的耗材变形。
- 挤出机发出咔嗒声或研磨声。
- 挤出机齿轮中可见耗材碎屑或损伤。

## 所需工具与材料

- H1.5 和 H2.0 内六角扳手
- 镊子或电吹风
- 小刷子
- 一小段耗材
- 少量润滑脂

## 安全警告

> **重要！**
>
> 在进行维护工作前，请务必**关闭电源并断开打印机电源**。否则存在**触电、短路及设备损坏**的风险。
>
> 当某些维护步骤需要打印机保持通电时，请务必佩戴**绝缘手套**，并特别注意**不要挤压、损坏或拉扯**任何裸露的电线、连接器或电路板。同时，喷嘴可能非常烫，请勿直接接触。
>
> 若您对以上内容或操作步骤有任何疑问，请[在支持页面提交工单](https://bambulab.com/zh/my/support/tickets?from=5)以获取帮助。

## 视频教程

## 拆卸与清理挤出机

### 步骤 1：移除工具头前盖

打开工具头前盖，并沿上方导轨滑动取下。

![open_the_cover.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/open_the_cover.png)

### 步骤 2：断开电缆

依次断开耗材传感器、部件冷却风扇、热端冷却风扇和热端加热组件的电缆。

> **注意：** 部分打印机 4 号线缆周围可能涂有胶，请用镊子划开胶或电吹风加热使胶融化后取下线缆，请勿用热风枪。断开电缆时请轻拿轻放，避免损坏。

![cables_to_disconnect.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/cables_to_disconnect.png)

### 步骤 3：松开切刀

按下切刀手柄，松开固定手柄的螺丝。松开螺丝后，让手柄自然下垂。

> **注意：** 拆螺丝时，确保内六角扳手垂直插入螺帽面，并完全插入后再轻轻旋转，以免滑丝。

|  |  |
| --- | --- |
| pressing-the-cutter.png | filament-cutter-removed.png |

### 步骤 4：取出挤出机

先拆下固定挤出机的 1、2、3 号螺丝，再拆下 4、5 号螺丝释放耗材导管。轻推导管朝向挤出机方向以取出 PTFE 管。

> **注意：** 请勿直接按压气动接头。由于堵塞原因，按压接头无法拔出 PTFE 管。  
> 若难以拔出，可沿气动接头末端切除一小段 PTFE 管（不影响正常使用），再拆卸挤出机。

![removing_the_extruder_screws.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/removing_the_extruder_screws.png)

用手取出挤出机。

![hold-and-remove-extruder.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/hold-and-remove-extruder.png)

### 步骤 5：拆下热端

用 H2.0 内六角扳手拧下热端的两颗螺丝。

![hotend_screws.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/hotend_screws.png)

轻轻左右晃动，将热端从挤出机上分离。

![separating_nozzle_from_extruder.gif](https://wiki.bambulab.com/x1/maintenance/extruder-clog/separating_nozzle_from_extruder.gif)

> **注意：** 由于堵塞，热端内部可能有残余耗材，拆卸时请小心操作并使用适当力度。

### 步骤 6：拆卸挤出机后盖

拆下固定挤出机的 4 颗螺丝，取下后盖。  
再松开用于调整挤出齿轮弹簧的 1 颗螺丝，释放弹力。

![back-screws.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/back-screws.png)

![screw.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/screw.png)

### 步骤 7：取出大齿轮

旋转齿轮，将其取出。

![removing_gears.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/removing_gears.png)

挤出机拆解完成。

![back-part-removed.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/back-part-removed.png)

> **注意：** 请注意保持轴承位置正确，以确保后续装配顺利。

![circular_screw.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/circular_screw.png)

### 步骤 8：清理挤出机

1. 用一小段耗材从挤出机内插入并清除残留耗材。

![removing_filament_stuck.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/removing_filament_stuck.png)

若耗材较长，可用手直接拉出。

![removing-filament-with-hand.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/removing-filament-with-hand.png)

2. 拆下齿轮和弹簧。

|  |  |
| --- | --- |
| removing-sprin.png | removing-spring.png |

3. 用刷子清洁齿轮。

|  |  |
| --- | --- |
| cleaning-large-gear.png | cleaning-small-gear.png |

4. 在惰轮齿轮（左图）齿面及主动齿轮（右图）红箭头所示部位涂抹少量润滑脂。

（下图为 P1S 机型示例，X1C 同样适用。）

![add_lubricant_on_extruder.jpeg](https://wiki.bambulab.com/x1/maintenance/extruder-clog/add_lubricant_on_extruder.jpeg)

也可在主动齿轮的侧面均匀涂抹少许润滑脂，并在重新安装前擦去多余部分。

![applying_lubricant.jpg](https://wiki.bambulab.com/x1/maintenance/extruder-clog/applying_lubricant.jpg)

## 重新组装挤出机

### 步骤 1：组装挤出机

1. 安装齿轮和弹簧。

|  |  |
| --- | --- |
| installing_the_spring!.png | installing_the_spring.png |

2. 装回大齿轮。

![yellow-gears.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/yellow-gears.png)

3. 装上后盖并使用 H2.0 内六角扳手拧紧 4 颗螺丝。

![screws.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/screws.png)

4. 拧回张力螺丝，直至“咔嗒”声确认到位。

![string-screw.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/string-screw.png)

5. 用手转动大齿轮，检查其是否能正常旋转。

![turning-screw.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/turning-screw.png)

### 步骤 2：安装热端

将热端放回原位，并用 H2.0 内六角扳手拧紧两颗螺丝。

|  |  |
| --- | --- |
| extruder-screwss.png | tightening_screws.png |

### 步骤 3：安装挤出机

将挤出机装回原位，并依次拧紧 1、2、3 号螺丝。

![screws-to-tighten.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/screws-to-tighten.png)

### 步骤 4：安装切刀

如图复位切刀手柄，并轻轻拧紧固定螺丝。

![installing_the_cutter.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/installing_the_cutter.png)

> **注意：** 若螺丝损坏，可[更换耗材切刀手柄组件](https://detail.tmall.com/item.htm?abbucket=2&id=733197978996&mi_id=0000zq37QRfcZhOZWfD3QUh9dWMqgBiV0l1Q6U7qmJMk6LU&ns=1&skuId=5246764675051&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%2208eedbc10aa15fc1ac3db4601f5bfadd%22%7D&xxc=taobaoSearch)，其中包含备用螺丝。

### 步骤 5：安装 PTFE 管

将耗材导管放置到位，先轻轻拧入两颗螺丝，不要过紧。

|  |  |
| --- | --- |
| filament-guide-screw.png | tighten-screw.png |

插入 PTFE 管，抬起导管并拧紧螺丝。  
![inserting-ptfe.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/inserting-ptfe.png)

### 步骤 6：连接电缆

依次连接耗材传感器、部件冷却风扇、热端冷却风扇和热端加热组件电缆。

> **注意：** 请确保每个端口方向正确并完全插入，错误插入可能导致设备报错。  
> ![connecting-cables.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/connecting-cables.png)

### 步骤 7：安装工具头前盖

![x1c-frontcover.png](https://wiki.bambulab.com/x1/maintenance/extruder-clog/x1c-frontcover.png)

## 功能验证

重新组装后，开启打印机并手动挤出耗材。  
若耗材流动顺畅且稳定，说明挤出机工作正常。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
