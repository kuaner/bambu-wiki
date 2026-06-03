---
path: zh/studio-handy/print-options
title: "打印选项"
description: ""
tags: []
created: 2024-05-24T03:32:03.992Z
updated: 2025-04-22T01:33:36.102Z
source: https://wiki.bambulab.com/zh/studio-handy/print-options
---

所有打印机均配备了打印选项，用户可以根据自己的需求，自行选择打印中需要启用的功能。打印选项可在打印机的显示屏或者 Bambu Studio 的设备页面中设置。**请注意，由于不同机型支持的功能不一样，所以打印选项页面也各不相同。请以实际界面显示的选项为准。**

![print_options_a1_series_cn.png](https://wiki.bambulab.com/software/common/print_options_a1_series_cn.png)

![print_options_cn.png](https://wiki.bambulab.com/software/common/print_options_cn.png)

## 启用打印板位置检测

检测打印板的定位标记。如果标记不在预定义范围内时，或者打印板与切片文件中选择的不一致，则打印机将停止打印。避免用户在打印前忘记放置打印板或者放了错误类型的打印板。由于 X1 系列和 A1 系列打印机的检测原理不同，X1 系列能检测未放打印板和放错打印板，A1 系列只能检测未放打印板。

|  |  |
| --- | --- |
|  | 打印板定位标记 |
| no_plate_cn.png | 未放打印板 |
|  | 放错打印板 |

## 自动从丢步中恢复

当电机在工作过程中检测到位置偏移（即丢步）时，X、Y 和 Z 轴将会重新回中进行定位，然后回到丢步前的位置重新执行未被执行的 G code，保证打印质量。

**注意：如果您使用接近机器上限的加速度，建议关闭丢步自动恢复功能。因为在高加速度下，丢步自动恢复功能可能会出现误识别。该功能是靠电机检测负载判断的，在高速运动中，可能会由于电机负载较大，没有丢步也可有可能被误识别为丢步了。**

> 支持在打印过程中修改此选项。

## 支持提示音

在开机、打印开始和打印结束时，打印机会发出提示音。

## 缠料检测

当检测到料线打结后，由于送料阻力过大，会触发相应的传感器，打印机便会自动暂停打印并弹出缠料的提醒。用户可以重新整理好料盘上的料线再继续打印，避免打印机出现“空打”的情况。关于缠料检测的更多介绍请参见[此 wiki 页面](../ams-lite/manual/filament-tangle-monitoring-intro.md)。

打印机空打示意：

![](https://wiki.bambulab.com/n1/manual/air-printing-detection/%E7%A9%BA%E6%89%93%E7%A4%BA%E6%84%8F.gif)

## 启用打印过程的 AI 监控

在打印过程中实现[炒面检测](../knowledge-sharing/Spaghetti_detection.md)和废料槽堆积检测。灵敏度有低中高 3 个选项，灵敏度越高，更容易检测到小的缺陷，但同时可能也会增加暂停次数。

> 支持在打印过程中修改此选项。

- 废料堆积  
  ![](https://wiki.bambulab.com/x1/troubleshooting/hmscode/microlidar/470px-92760_spaghetti_pass-error_box.jpg)
- 炒面检测  
  ![](https://wiki.bambulab.com/spg_error0.jpg)

## 首层扫描

打印完首层后，自动检测首层的打印质量，如有异常会发出警告。

![first_layer_inspection_cn.png](https://wiki.bambulab.com/software/common/first_layer_inspection_cn.png)

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
