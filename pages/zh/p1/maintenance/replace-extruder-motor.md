---
path: zh/p1/maintenance/replace-extruder-motor
title: "更换挤出电机"
description: "更换 P 系列挤出电机的操作步骤"
tags: ["p1"]
created: 2024-12-17T01:54:59.655Z
updated: 2024-12-31T06:33:16.068Z
source: https://wiki.bambulab.com/zh/p1/maintenance/replace-extruder-motor
---

## 适用打印机型号

P1

## 挤出电机

挤出电机是安装在工具头上，用于驱动挤出机进行动作的电机，它是一款 36 系列圆形步进电机。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/extrude_motor.jpg)

## 何时使用

- 电机烧坏，无法运转
- 售后人员通过 log 分析，确认是挤出电机故障

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的挤出电机（购买链接：[天猫](https://detail.tmall.com/item.htm?abbucket=6&id=732924900902&pisk=gYZm3AszSrufKuShcQifR2qls07-cmisl5Kt6chNzbl5CtwA5hWg653wX-QfIOcu1j3x0l4WjJw_DtiOhmwjfc5d9MFgh-i1Ltor6oxP4vyybnlNy0ot6CLh9MILE-isb6CLDVEXMvkpbcuq7b8rNAKZ_582aTDZBIlZg5WuUbMMunkqQU8rhADqbnlqzgkiLKlZbEyrzbMZbfPZbTmrTttZtlr74_mPOrStx0qonqcUEwtwjStKuXz-ah5UqxfIT-lkbhlfWj8UE-CDA8nb2WDLMg-0t-zU_yPPqn07u8qiRlOVUcuayy30rs-iwoHi8cukQhyo0bgZhDSeZYazHPrbidxZhoEKSXglQhgt4k3U8Sv1d8oqQ5gQX6tjgRyQAynhj3om7g-WzerQthMPBu865qkSEXLXAq6CKrqeITXkRZgqFxCLXTYrMqkSEb6lEeOiuYMYu&rn=fb97c03039ba017472cedc81d5a43783&spm=a1z10.3-b.w4011-25670817738.17.1ef63c0eLJgj7x&skuId=5071561788576) ；[京东](https://item.jd.com/10080126224525.html) ）
- H2.0 内六角扳手
- H1.5 内六角扳手
- 平头镊子
- 20 分钟

## 移除挤出电机

### 步骤 1：移除 TH 板组件

您可以参考这篇 Wiki 来移除 TH 板组件：[更换P1系列工具头电路板 | Bambu Lab Wiki](pcb-boards-on-toolhead.md)

|  |  |
| --- | --- |
|  |  |

### 步骤 2：移除固定螺丝

使用 H2.0 内六角扳手，依次移除 8 颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/remove_8_screws.jpg)

### 步骤 3：移除工具头滑车前盖（含挤出机）

将工具头的滑车前盖组件（含挤出机）移除。

|  |  |
| --- | --- |
|  |  |

注意：在上部铜套位置，工具头滑车后盖装有4根弹簧，要防止脱落丢失

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/springs_inside.jpg)

### 步骤 4：移除挤出机

使用 H2.0 内六角扳手移除 3 颗螺丝，取下挤出机和热端。

|  |  |
| --- | --- |
|  |  |

### 步骤 5：移除挤出电机

使用 H2.0 内六角扳手，移除 2 颗螺丝，取下挤出电机。

|  |  |
| --- | --- |
|  |  |

## 安装挤出电机

### 步骤 1：安装挤出电机

将新的挤出电机安装到滑车前盖上，注意电缆在上方，然后锁入 2 颗螺丝固定电机。

|  |  |
| --- | --- |
|  |  |

### 步骤 2：安装挤出机

将挤出机和热端一起安装到滑车前盖上，锁入 3 颗螺丝进行固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/install_the_extruder.jpg)

### 步骤 3：安装滑车前盖组件

安装前，先确认弹簧在位，上下铜套在滑车后盖对应的槽内，然后将装有挤出电机的滑车前盖装上，注意不要压到电机电缆。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：锁螺丝

锁螺丝固定滑车前盖，请按下图所示，按 1~8 的顺序依次锁紧螺丝。

|  |  |
| --- | --- |
|  |  |

### 步骤 5：安装 TH 板组件

您可以参考这篇 Wiki，将 TH 板组件以及工具头中框、后盖安装好：[更换P1系列工具头电路板 | Bambu Lab Wiki](pcb-boards-on-toolhead.md)

## 设备校准

连接电源，启动打印机，完成一次手动上料和退料的操作，如果没有异常，说明操作成功。

|  |  |
| --- | --- |
|  |  |

如果有异常，请按照操作步骤排查组装是否有问题，排除后，再次运行设备自检。  
如果问题仍然存在，请联系技术服务团队寻求进一步的帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
