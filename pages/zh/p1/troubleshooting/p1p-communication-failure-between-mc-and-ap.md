---
path: zh/p1/troubleshooting/p1p-communication-failure-between-mc-and-ap
title: "P1 系列打印机通信异常排查(二) AP—MC 通信异常"
description: "本指南介绍 P1 系列打印机 AP 板与 MC 板通信异常时，如何排查故障部件。"
tags: ["通信异常", "mc与ap通信失败"]
created: 2023-02-13T12:56:04.475Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/p1/troubleshooting/p1p-communication-failure-between-mc-and-ap
---

### 故障现象

1. 打印机空闲状态下无法通过按键控制工具头进行 XY 移动（Rx 异常）；

2. 屏幕上无法获取温度信息，挤出温度和热床温度均显示为“0” （Tx 异常）;

3. 无法控制工具头移动，同时温度显示异常（Rx 和 Tx 同时异常）。

#### 故障原因和解决方案

1. AP 板元器件损坏，需要更换 AP 主板；

2. MC 板（运动控制板）故障，需要更换 MC 板；

3. MC-AP 连接线接触不良，需要重新连接或更换 MC-AP 连接线。

## 安全和操作提示

拆装打印机上的连接线时，打印机必须处于断开电源线的状态。

## 所需的工具

- H2.0 内六角扳手
- 万用表
- 镊子

## 排查指引

### 步骤 1 - 确认故障现象

打印机开机且空闲的状态下，通过屏幕显示的温度信息和控制工具头运动的响应情况，来判断打印机是 RX 异常、TX 异常还是 RX 和 TX 均异常，然后进行下一步。

|  |  |
| --- | --- |
|  |  |

### 步骤 2 - 确认 MC 板工作状态

如果第 1 步确认到的情况是 RX 和 TX 均异常，可通过保持开机状态，然后透过废料滑梯观察 MC 板工作指示灯（不肯定的情况下，可以先拆下后面板，直接观察指示灯状态），如果 MC 板指示灯正常闪烁，可进行下一步； 如果 MC 板指示灯不工作，建议更换 MC 板。

![](https://wiki.bambulab.com/p1/troubleshooting/mc_to_ap_fail/check_the_led_status.jpg)

（点击  [MC 板](../maintenance/mc-board.md) 了解如何更换 MC 板）

### 步骤 3 - AP-MC 连接线接触不良预检

如果是 Tx 异常(无温度示数)，可以继续在开机状态下，去除 AP-MC 连接线的固定胶布，然后摇晃整条电缆，观察屏幕上的温度界面是否有变化 ，如果无变化，进行下一步； 如果有变化，说明是接触不良，进入第 5 步。

![](https://wiki.bambulab.com/p1/maintenance/mc-ap-cable/fixing_tapes.jpg)

### 步骤 4 -检查 AP 主板

移除 AP 主板遮盖泡棉，断开摄像头连接排线，检查卡槽下方元器件的状态，确认无缺失或烧坏的情况，如有，需更换 AP 主板； 如无异常，进行下一步。

|  |  |
| --- | --- |
|  |  |

（点击  [AP主板](../maintenance/ap-board.md) 了解如何更换AP主板）

### 步骤 5 -检查连接器

参考 [MC-AP 连接电缆](../maintenance/mc-ap-cable.md)的相关步骤，找到连接线在 AP 板和 MC 板上的连接器，确认连接状态正常，并拔下插头，检查确认插头和座子都正常，无损坏。然后进行下一步。

|  |  |
| --- | --- |
|  |  |

### 步骤 6 - MC-AP 连接线导通测试

用万用表测量 AP 插头从左到右第二第三个触点是否分别和 MC 插头从左到右第二第三个触点导通（如下图所示）。如果两个红色箭头所示的触点是导通的，两个黄色箭头所示触点也是导通的，可进行下一步。如果有任何一条不导通则需要更换连接线缆。

![cable_test.png](https://wiki.bambulab.com/p1/cable_test.png)

### 步骤 7 - 检查 MC 板

如果以上步骤均无查出异常，且 MC 板的指灯在第 1 步已确认是正常工作的，可以尝试从表面观察 MC 板是否有元器件损坏，如有，更换 MC 板； 如无发现，可提供日志文件给售后服务团队进行分析确认，或检查 MC-TH 的连接线（这应该会是另外一篇排查指引了）。

![](https://wiki.bambulab.com/p1/troubleshooting/mc_to_ap_fail/mc_board.jpg)
