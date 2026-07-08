---
path: zh/p1/troubleshooting/bearing-disengaged
title: "X/P 系列 Z 轴直线轴承脱出处理指南"
description: ""
tags: []
created: 2025-05-08T12:11:12.149Z
updated: 2026-07-02T02:50:40.099Z
source: https://wiki.bambulab.com/zh/p1/troubleshooting/bearing-disengaged
---

## Z轴直线轴承脱出

![](https://wiki.bambulab.com/x1/troubleshooting/homing-z-failed-1/abnormal_slider.jpg)

Z 轴直线轴承脱出可能是以下问题导致：

- 打印机底部的光轴凹槽中堆积异物长期积累未清理，导致热床下降时直线轴承被异物顶起。

![](https://wiki.bambulab.com/x1/troubleshooting/hmscode/mc-assets/500px-clean-the-chamber-botton-holes.png)

若未及时重新安装轴承，可能会造成**回中失败、热床调平失败**等一系列打印异常。

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 1. 移除屏幕

修复直线轴承需要将打印机倒置，为避免背压损坏屏幕组件，请先将显示屏从前壳上拆除。

### X 系列和 P2S

首先将屏幕向上倾斜，找到底部解锁卡扣。  
![](https://wiki.bambulab.com/x1/maintenance/replace-high-resolution-screen/350px-buckle.png)

按压下图所示位置以解锁卡扣，再向右推动屏幕以完成拆卸。

![](https://wiki.bambulab.com/x1/maintenance/replace-high-resolution-screen/350px-press_to_unlock.png)

### P1 系列

按压屏幕下方的锁扣解除锁定，然后向右推动，完成屏幕拆卸。

![](https://wiki.bambulab.com/p1/maintenance/screen/press_to_unlock_the_display.jpg)

## 2. 移除喷嘴组件

为防止维修过程中热床上升撞击喷嘴组件，请先将喷嘴组件拆除。

![移除.png](https://wiki.bambulab.com/x1/troubleshooting/bearing-disengaged/%E7%A7%BB%E9%99%A4.png)

可参考以下视频完成操作：

快拆式喷嘴只需打开卡扣即可取下。

![lock_clip_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/lock_clip_007.png)

## 3. 倒置打印机

将打印机倒置（底部朝上），逆时针拉动 Z 轴皮带，此时热床会缓慢下降，直至无法继续移动。

![底部皮带.jpg](https://wiki.bambulab.com/x1/troubleshooting/bearing-disengaged/%E5%BA%95%E9%83%A8%E7%9A%AE%E5%B8%A6.jpg)

## 4. 复位直线轴承

> 处理左右直线轴承时无需拆卸侧板，但处理后侧直线轴承时需**拆卸背板**。  
> [更换 X1C 背板](../../x1/maintenance/replace-rear-panel.md)  
> [更换 P1S 背板](../maintenance/p1s-rear-panel.md)  
> [更换 X2D 背板](../../x2d/maintenance/replace-rear-panel.md)  
> [更换 P2S 背板](../../p2s/maintenance/replace-rear-panel.md)

此时凸出的轴承会抵住光轴顶部的固定平台。

![20250509-154700.jpg](https://wiki.bambulab.com/x1/20250509-154700.jpg)

用力按压轴承周围的结构部分，将凸出的直线轴承压回原位。

![按压.jpg](https://wiki.bambulab.com/x1/troubleshooting/bearing-disengaged/%E6%8C%89%E5%8E%8B.jpg)

> 注意：请勿直接按压轴承本体。

操作演示视频参考：

<https://public-cdn.bblmw.com/wiki/X1/fix_bearing_up.mp4>

完成后，顺时针拉动皮带，使热床回升。

![顺时针.jpg](https://wiki.bambulab.com/x1/troubleshooting/bearing-disengaged/%E9%A1%BA%E6%97%B6%E9%92%88.jpg)

## 5. 恢复打印机摆放位置

将打印机恢复至正常摆放状态，检查轴承是否已完全压入导轨中。  
如仍有部分轴承突出，请重复步骤 3 和 4。

![安装完成.jpg](https://wiki.bambulab.com/x1/troubleshooting/bearing-disengaged/%E5%AE%89%E8%A3%85%E5%AE%8C%E6%88%90.jpg)

## 6.安装喷嘴组件

完成轴承复位后，请重新安装喷嘴组件。

![安装喷嘴.png](https://wiki.bambulab.com/x1/troubleshooting/bearing-disengaged/%E5%AE%89%E8%A3%85%E5%96%B7%E5%98%B4.png)

快拆式喷嘴请注意卡扣安装方式。

![correct_clip_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/correct_clip_011.png)

## 7. 执行校准

### X 系列和 P2S

在打印校准中选择“自动热床调平”，并开始校准任务。

![calibration-cn.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/calibration-cn.png)  
![nozzle.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/screen-operation/nozzle.png)

### P1 系列

点击右侧【设置】按钮，向下滚动找到【校准】选项，点击后选择相应的校准项目（如振动补偿、电机降噪、自动热床调平）。

![20250309-200209.jpg](https://wiki.bambulab.com/screen-operation/calibration/11/20250309-200209.jpg)  
![20250309-200203.jpg](https://wiki.bambulab.com/screen-operation/calibration/11/20250309-200203.jpg)

## 注意事项

轴承凸起通常是由于光轴底部的三个孔中存在异物，例如废料，导致轴承受到挤压而凸出。如果这些孔中有任何异物，请确保彻底清理干净，否则故障可能会再次发生。

![](https://wiki.bambulab.com/x1/troubleshooting/hmscode/mc-assets/500px-clean-the-chamber-botton-holes.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
