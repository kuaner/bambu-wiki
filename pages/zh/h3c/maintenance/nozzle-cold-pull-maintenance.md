---
path: zh/h3c/maintenance/nozzle-cold-pull-maintenance
title: "拓竹H3C 喷嘴冷拔指南"
description: ""
tags: []
created: 2026-11-03T12:38:47.890Z
updated: 2026-11-10T11:48:21.617Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/nozzle-cold-pull-maintenance
---

## 冷拔

在 3D 打印过程中，确保喷嘴干净、通畅至关重要，这直接关乎打印效果与质量。我们强烈建议您在日常使用中，对喷嘴进行维护从而有效延长喷嘴的使用寿命。

以下是几种场景您必须进行冷拔维护：

1. 挤出电机频繁报错阻力异常：当挤出电机在常规打印流量下频繁出现阻力异常报错，这意味着喷嘴阻力过大，急需清理。
2. 打印耗材切换至 TPU 前：鉴于 TPU 材料对喷嘴阻力极为敏感，若此前喷嘴打印过其他耗材，我们建议您在打印 TPU 前，对喷嘴进行冷拔清理，以保障打印顺畅。

> 注意：若喷嘴完全堵塞，将无法冲刷出耗材，此时需要先参考[热端堵塞清理](../../h2/troubleshooting/unclogging.md)，使用通针将堵塞物推向内部，再进行冷拔操作。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 流程图

flowchart TD
A["开始冷拔"]
B["观察冲刷"]
C{"是否能够挤出？"}
D["停止冷拔"]
E["设置热端温度"]
F["通针疏通"]
I["完成冷拔"]
A --> B
B --> C
C -->|否| D
C -->|是| I
D --> E
E --> F
F --> A
classDef process fill:#D6ECFF,stroke:#4A90E2,stroke-width:1px,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
class A,B,D,E,F,I process;
class C decision;

### 冷拔过程

点击工具箱。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______0bef4ceb3d.png)

选择喷嘴冷拔。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______01f8cb86a8.png)

点击下一步。

|  |  |
| --- | --- |
| 图 | 图 |

选择冷拔耗材以及熔化温度，点击开始。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______ccd94066d0.png)

根据提示确认热床表面无异物后开始冷拔。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______496910cd16.png)

取下 AMS 的磁吸侧板。

|  |  |
| --- | --- |
| 图 | 图 |

根据提示按压侧边的黑色压块，向内轻推料管后，再拔出。

|  |  |
| --- | --- |
| 图 | 图 |

插入一截长度大于 30 cm 的耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______eb0c633d58.png)

等待耗材冲刷。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______b6a0c9cfc2.png)

观察热端是否能够挤出耗材，若无法挤出，请停止冷拔，使用通针疏通几次，然后重新开始冷拔操作。若挤出非常顺畅，可跳过该步骤。

> 请注意此方法**不适用于直径小于 0.4mm 的热端**。

![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______0914bb1a16.webp)

等待降温。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______c8f10fa374.png)

根据提示缓慢拉出耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______efa9b1611f.png)

检查冷拔质量。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______a40fb0e405.png)

> 耗材尾部呈锐角，则代表本次冷拔成功。若冷拔区域存在异色杂质，请重复冷拔，直到耗材表面干净。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______35e7a8d339.png)

重新插回料管。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/nozzle-cold-pull-maintenance/zh/04_h3c_______e9edc7fbf8.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
