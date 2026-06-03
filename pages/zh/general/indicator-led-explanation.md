---
path: zh/general/indicator-led-explanation
title: "拓竹打印机 LED 指示灯灯语解释"
description: ""
tags: []
created: 2024-06-12T03:28:02.473Z
updated: 2026-06-02T03:05:50.929Z
source: https://wiki.bambulab.com/zh/general/indicator-led-explanation
---

用户可以通过观察打印机上的指示灯来判断打印机的状态。本文列出了打印机正常情况下的灯语状态。如果您的打印机某一项灯语与本文描述的不符,那意味着打印机状态一定存在异常。这些指示灯能反映主要硬件模块如工具头电路板(TH)、运动控制板(MC)和应用控制板(AP)是否正常上电。

需要注意的是，即使TH、AP、MC指示灯显示正常,也不代表打印机就一定能正常工作，因为当某些传感器，例如霍尔传感器，温度传感器出现异常时，这些主要电路板的主控芯片的上电仍然是正常的，就意味着这些指示灯也是正常的。

总之，指示灯的状态可以反映主要硬件模块的供电情况，但并不能完全代表打印机的整体工作状态。用户需要综合考虑各种因素才能判断打印机的实际工作状态。

本指南中的部分视频在手机端的浏览器上可能无法正常加载,建议您改用电脑端浏览器观看。

## H2D/H2C 打印机

### 正常状态：AP 板指示灯快速闪烁（左）、常亮（右）

参阅 wiki 内容[取下 AP 板盖](https://wiki.bambulab.com/zh/h2/maintenance/replace-ap-board#%E6%AD%A5%E9%AA%A4-2%E5%8F%96%E4%B8%8B-ap-%E6%9D%BF%E7%9B%96)，使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖，观察 AP 板指示灯。

![h2_ap1.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2_ap1.gif)

您也可以不拆除 AP 板盖，在特定的角度透过 AP 板盖的散热孔来观察指示灯。

![h2_ap2.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2_ap2.gif)

### 正常状态：MC 板指示灯常亮（左上）、慢速闪烁（左下）、快速闪烁（右）

参阅 wiki 内容[移除背板](../h2/maintenance/replace-rear-panel.md)，[拆下废料槽](../h2/maintenance/replace-purge-chute.md)后，观察 MC 板指示灯状态。

![h2_mc.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2_mc.gif)

- 本动图包含了开机后的初始化状态，故左下的指示灯有一小段常亮。

### 正常状态：TH 板指示灯常亮（上&中）、快速闪烁（下）

参阅 wiki 内容[移除部件冷却风扇](../h2/maintenance/replace-part-cooling-fan.md)后，观察 TH 板指示灯状态。

![h2d_h2c_th_1.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2d_h2c_th_1.gif)

您也可以不拆除冷却风扇，通过工具头侧面的小孔来观察指示灯。

![h2d_h2c_th_2.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2d_h2c_th_2.gif)

## H2S 打印机

### 正常状态：AP 板指示灯快速闪烁（左）、常亮（右）

参阅 wiki 内容[AP 板更换指南](../h2s/maintenance/replace-ap-board.md)，使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖，观察 AP 板指示灯。

![h2_ap1.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2_ap1.gif)

您也可以不拆除 AP 板盖，在特定的角度透过 AP 板盖的散热孔来观察指示灯。

![h2_ap2.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2_ap2.gif)

### 正常状态：MC 板指示灯常亮（左上）、慢速闪烁（左下）、快速闪烁（右）

参阅 wiki 内容[移除背板](../h2/maintenance/replace-rear-panel.md)，[拆下废料槽](../h2/maintenance/replace-purge-chute.md)后，观察 MC 板指示灯状态。

![h2_mc.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2_mc.gif)

- 本动图包含了开机后的初始化状态，故左下的指示灯有一小段常亮。

### 正常状态：TH 板指示灯快速闪烁

参阅 wiki 内容[更换 H2S TH 板](../h2s/maintenance/replace-th-board.md)的步骤一与步骤二，移除工具头后盖，观察 TH 板指示灯状态。

![h2s_th_1.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2s_th_1.gif)

您也可以不拆除工具头后盖，通过打开工具头模块接口盖子，来观察 TH 板指示灯状态。  
![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-11.png)

![h2s_th_2.gif](https://wiki.bambulab.com/general/bbl-indicator-led/h2s_th_2.gif)

## X1 系列打印机

### 正常状态：TH板指示灯常亮红灯

![x1-th.gif](https://wiki.bambulab.com/general/bbl-indicator-led/x1-th.gif)

### 正常状态：MC板每5秒闪烁一次红灯

![new-x1-mc.gif](https://wiki.bambulab.com/general/bbl-indicator-led/new-x1-mc.gif)

如果MC板的指示灯不是5s闪烁一次（比如30s闪烁一次），请检查USB-C线的连接是否正确。

注意字母A和凸点朝外：

![](https://wiki.bambulab.com/x1/troubleshooting/usbc-cable-connection-issue/400px-connect1.png)

### 正常状态：AP板有2个指示灯,一个常亮红灯,一个1秒闪烁一次红灯

![x1-ap.gif](https://wiki.bambulab.com/general/bbl-indicator-led/x1-ap.gif)

- [打印机电路故障排查 - X1 系列](../x1/troubleshooting/circuit-board-power-failure.md)

## X2D 打印机

### 正常状态：TH 板指示灯快速闪烁

请参考[更换 X2D 工具头外壳](../x2d/maintenance/replace-toolhead-housing.md)来移除工具头后盖，观察 TH 板指示灯。

![th_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/th_light.webp)

### 正常状态：MC 板指示灯常亮（左上）、慢速闪烁（右下）

请参考[更换 X2D 背板](../x2d/maintenance/replace-rear-panel.md)移除打印机背板，观察 MC 板指示灯。

![mc_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/mc_light.webp)

### 正常状态：AP 板指示灯快速闪烁（左下）、常亮（右上）

从靠近前门一侧打开 AP 板盖，断开左 LED 灯，观察 AP 板指示灯。

|  |  |
| --- | --- |
|  |  |

![ap_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/ap_light.webp)

## P1S 打印机

### 正常状态：TH板指示灯常亮绿灯

![p1-th.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p1-th.gif)

### 正常状态：MC板每5秒闪烁一次绿灯

![p1-mc-new.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p1-mc-new.gif)

如果MC板的指示灯不是5s闪烁一次（比如30s闪烁一次），请检查FPC线连接是否正确：

![connectors_on_interface_board_cn.jpg](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/connectors_on_interface_board_cn.jpg)

### 正常状态：AP板有1个每秒闪烁一次的绿灯指示灯，需要先根据该方法解锁屏幕，才能找到该指示灯。

![](https://wiki.bambulab.com/p1/maintenance/screen/press_to_unlock_the_display.jpg)

按压屏幕下方的扣位，解除锁定，然后向右推动屏幕，使屏幕松脱。

![p1-ap.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p1-ap.gif)

- [打印机电路故障排查 - P1 系列](../p1/troubleshooting/circuit-board-power-failure.md)

## P2S 打印机

### 正常状态：TH 板指示灯常亮（上&右下）、快速闪烁（左下）

参考[更换 P2S 工具头外壳](https://wiki.bambulab.com/zh/p2s/maintenance/replace-toolhead-housing#%E7%AC%AC2%E6%AD%A5-%E7%A7%BB%E9%99%A4%E5%B7%A5%E5%85%B7%E5%A4%B4%E5%90%8E%E7%9B%96)，取下**工具头后盖**，观察 TH 板指示灯状态。

![p2s_th.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p2s_th.gif)

### 正常状态：MC 板指示灯常亮（上）、慢速闪烁（下）

参考[更换 P2S 背板](../p2s/maintenance/replace-rear-panel.md)，移除 P2S 背板，观察 MC 板指示灯状态。

![p2s_mc.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p2s_mc.gif)

### 正常状态：AP 板指示灯快速闪烁（左）、常亮（右）

从靠近前门的一侧打开 AP 板盖，观察 AP 板指示灯。

![01_open_the_service_end_of_the_ap_board_cover_001.png](https://wiki.bambulab.com/knowledge-sharing/knowledge/01_open_the_service_end_of_the_ap_board_cover_001.png)

![p2s-ap.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p2s-ap.gif)

### 正常状态：电源模块指示灯常亮

![p2s-pw.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p2s-pw.gif)

## A2L 打印机

### 正常状态：TH 板指示灯常亮（上 & 左下）、快速闪烁（右下）

请参考[更换工具头外壳](https://wiki.bambulab.com/zh/a2l/maintenance/replace-toolhead-rear-housing)来移除工具头后盖，观察 TH 板指示灯。

![th板.webp](https://wiki.bambulab.com/general/bbl-indicator-led/th%E6%9D%BF.webp)

### 正常状态：主板（集成 MC 板和 AP 板）指示灯

请参考[更换底盖](https://wiki.bambulab.com/zh/a2l/maintenance/replace-bottom-cover)移除打印机底壳，观察主板指示灯。

- **通信状态灯**：常亮（左绿灯 & 右白灯）

![mcmodel.jpg](https://wiki.bambulab.com/general/bbl-indicator-led/mcmodel.jpg)

- **工作指示灯**：上方绿灯每 1 秒闪烁一次，下方左绿灯每 1 秒闪烁一次，右绿灯每 5 秒闪烁一次

![ap2.webp](https://wiki.bambulab.com/general/bbl-indicator-led/ap2.webp)

## A1 mini 打印机

### 正常状态：TH板指示灯常亮绿灯

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

如图所示，拉住后盖底部，小心撬开后盖。

![a1m-th.gif](https://wiki.bambulab.com/general/bbl-indicator-led/a1m-th.gif)

### 正常状态：MC板和AP板集成在主板上

#### 正常状态：MC板每5秒闪烁一次绿灯（该指示灯需要在特定的角度下观察）

![a1m-mc.gif](https://wiki.bambulab.com/general/bbl-indicator-led/a1m-mc.gif)

#### 正常状态：AP板每秒闪烁一次绿灯

![a1m-ap.webp](https://wiki.bambulab.com/general/bbl-indicator-led/a1m-ap.webp)

## A1打印机

### 正常状态：TH板指示灯常亮绿灯

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

如图所示，拉住后盖底部，小心撬开后盖。

![a1m-th.gif](https://wiki.bambulab.com/general/bbl-indicator-led/a1m-th.gif)

### 正常状态：MC板和AP板集成在主板上

#### 正常状态：MC板每5秒闪烁一次绿灯

![a1-mc.webp](https://wiki.bambulab.com/general/bbl-indicator-led/a1-mc.webp)

#### 正常状态：AP板有1个每秒闪烁一次的绿灯指示灯

![a1-ap.webp](https://wiki.bambulab.com/general/bbl-indicator-led/a1-ap.webp)

## A1系列打印机的HMS指示灯

A1 系列还有一个HMS指示灯，当出现HMS错误时会快速闪烁，提示用户查看HMS错误信息。当没有HMS信息时，如果屏幕是点亮的，该指示灯是常亮的，如果屏幕没有点亮，该指示灯是缓慢的呼吸。

### 异常状态：出现HMS报错时

![a1-hms-on.webp](https://wiki.bambulab.com/general/bbl-indicator-led/a1-hms-on.webp)

如果该指示灯快速闪烁，您可以在屏幕的HMS页面获取更详细报错信息，并扫描跳转到相应的wiki获取故障排查指南。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### 正常状态：无HMS报错，且屏幕是点亮时

![a1-screen-always-on.gif](https://wiki.bambulab.com/general/bbl-indicator-led/a1-screen-always-on.gif)

### 正常状态：无HMS报错，且屏幕是熄灭时

![a1-screen-idle.gif](https://wiki.bambulab.com/general/bbl-indicator-led/a1-screen-idle.gif)
