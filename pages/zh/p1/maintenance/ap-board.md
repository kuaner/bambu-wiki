---
path: zh/p1/maintenance/ap-board
title: "更换 P1 系列 AP 板"
description: "拆装P1P打印机AP主板的操作步骤"
tags: ["p1"]
created: 2022-12-11T15:08:13.008Z
updated: 2026-05-29T08:14:25.807Z
source: https://wiki.bambulab.com/zh/p1/maintenance/ap-board
---

## AP 板

AP 板的全称为应用处理器主板（Application Processor Main Board），是打印机内用于处理信息交互的电路板。它为打印机提供独立的操作环境，并支持打印机应用所需的系统功能，包括内存管理、系统固件、图形处理和多媒体解码等。

![p1_apboard_display.png](https://wiki.bambulab.com/p1/maintenance/ap-board/p1_apboard_display.png)

## 适用打印机型号

- P1S
- P1P

> **注意：** P1S 和 P1P 的 AP 板外观相同，安装方法也相同，但两者并不兼容。也就是说，P1P 只能使用专为 P1P 设计的 AP 板，而 P1S 只能使用专为 P1S 设计的 AP 板。

## 何时更换

更换 AP 板后，由于新的 SN 未注册，机器将无法进行绑定。因此，在更换 AP 板后首次开机时，可先跳过绑定机器步骤，并检验更换 AP 板是否已解决问题（网络连接问题除外）。

## 所需要工具和材料

- H 2.0/1.5 内六角扳手
- 镊子

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

> **注意：** 关闭打印机电源，并移除 SD 卡。在开始安装前，请先拍照并留存 AP 板上的序列号（即图中二维码），以便在后续注册流程中使用。请联系售后并提供新、旧序列号以完成序列号替换（P1P 的序列号是以 01S 开头的编码）。请参考：[如何查找序列号及注册新序列号](../../general/find-sn.md)  
> ![p1_apboard_sn.png](https://wiki.bambulab.com/p1/maintenance/ap-board/p1_apboard_sn.png)

## 移除旧的 AP 主板

### 移除屏幕和前面盖

参考[屏幕组件](screen.md)、[P1P 前面盖](front-cover.md) 或 [P1S 前面盖](p1s-front-cover.md) 的相关内容，移除屏幕和前面盖。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/front_cover_removed.jpg)

### 移除密封泡棉

用手移除密封泡棉。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/remove_the_foam.jpg)

### 移除固定螺丝并断开连接线

揭开摄像头排线连接器盖子，断开摄像头连接。按压补光灯连接线插头，断开补光灯连接线。断开 WIFI 天线连接。使用 H 2.0 内六角扳手，移除 4 颗螺丝。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/ap-p1.jpg)

### 取下 AP 主板

将上盖向上拉起一些，然后将 AP 主板从横梁中取出。断开屏幕连接线缆和 MC 板连接线缆后，移除 AP 主板。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/connect_cables.jpg)

## 安装新的 AP 主板

### 连接线缆

连接 MC-AP 线缆和屏幕线缆。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/connect_cables.jpg)

### 安装 AP 主板

将显示器排线穿过线孔，并注意避让 WIFI 线缆。然后根据 SD 卡槽的缺口位置，将 AP 主板安装到横梁上。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/install_the_ap_board1.jpg)

### 固定螺丝并连接线缆

锁入 4 颗螺丝，连接 WIFI 天线、补光灯连接线和摄像头排线。

![](https://wiki.bambulab.com/p1/maintenance/ap-board/ap-p1.jpg)

### 贴附密封泡棉

![](https://wiki.bambulab.com/p1/maintenance/ap-board/attach_the_foam2.jpg)

### 安装前面盖和屏幕

参考[前面盖](front-cover.md)和[屏幕组件](screen.md)的相关内容，安装前面盖和屏幕。

![](https://wiki.bambulab.com/p1/maintenance/front-cover/display_installed.jpg)

### 绑定新序列号（SN）

> **注意：**  
> 新 SN 注册成功后，旧 SN 将会作废，旧的 AP 板也将不能再被注册或绑定。

更换 AP 板后，由于新的 SN 未注册，无法进行绑定操作。因此，在更换 AP 板后首次开机时，可跳过绑定机器步骤，并检验更换 AP 板是否解决问题（网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。

![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 功能验证

### 根据电路板灯语判断

**正常状态：AP 板有 1 个每秒闪烁 1 次的绿色指示灯，需要先根据该方法解锁屏幕，才能找到该指示灯。**

在拧回所有螺丝前，可先预装盖子或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常。确认灯语正常后，再拧回螺丝，以避免返工。

![](https://wiki.bambulab.com/p1/maintenance/screen/press_to_unlock_the_display.jpg)

按压屏幕下方的扣位，解除锁定，然后向右推动屏幕，使屏幕松脱，检查灯语是否正常。

<https://public-cdn.bblmw.com/wiki/video/P1-AP.mp4>

### 连接电源线并打开电源，发起设备自检，检查是否有报错

> **注意：**
>
> 1. 更换了 AP 板的机器，在首次开机时，应跳过绑定机器的步骤；
>
> 2.在确认更换完成后，还需要进行 SN 的替换，请联系售后并提供新、旧 SN 以完成 SN 替换（P1P 的 SN 是以 01S 开头的编码），请参考：[如何查找序列号及注册新序列号](../../general/find-sn.md)。

1. 启动打印机，确认屏幕能够正常显示，且按键功能正常。

![](https://wiki.bambulab.com/p1/maintenance/screen/screen_ok.jpg)

2. 运行设备自检流程。如果自检通过，则说明操作成功。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/self-test.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导.
