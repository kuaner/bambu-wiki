---
path: zh/a1/maintenance/A1_Extruder_motor_replacement
title: "A1 系列挤出机电机更换指南"
description: "本指南提供了详细的挤出机电机更换步骤。"
tags: ["a1", "a1 mini"]
created: 2025-03-10T01:48:19.006Z
updated: 2025-03-14T09:14:29.345Z
source: https://wiki.bambulab.com/zh/a1/maintenance/A1_Extruder_motor_replacement
---

## 挤出机电机

本指南中，我们将展示 A1 挤出机电机的更换过程。

![motor.jpg](https://wiki.bambulab.com/a1/maintenance/replace-extuder-motor/motor.jpg)

## 适用打印机型号

A1、A1 mini

## 何时使用

- 电机堵转、丢步。
- 挤出存在较大波动。
- 拓竹技术支持建议更换。

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的挤出机电机
- H2.0 内六角扳手
- H1.5 内六角扳手
- 25 分钟

## 移除旧的挤出机电机

### 1.移除工具头后盖

请按照下面所示的方法，小心地扣住后盖底部的扣位，缓慢向后拉动打开后盖。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

### 2.取下 USB-C 数据线

用 H1.5 内六角扳手拆下 A1 工具头上固定 USB-C 数据线的四颗螺钉，然后向上移除 USB-C 数据线。

![](https://wiki.bambulab.com/a1/maintenance/toolhead-board/remove_the_usb_c_cable_of_a1.jpeg)

### 3.移除挤出主板固定螺丝

卸下固定挤出主板的 3 颗黑色螺丝。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_th_board_screws.jpeg)

### 4.断开连接线

移除连接到工具头板的四根电缆。小心地从接头处拔出它们，避免将电线从接头处直接拉出。建议使用扁平工具轻轻撬出，以避免潜在的损坏。

![](https://wiki.bambulab.com/a1m/replace-th-board/disconnect_the_th_board_cables.jpeg)

移除两颗螺丝，取下涡流传感器的线缆。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_eddy_sensor_screws.jpeg)

### 5.移除挤出板

现在您可以缓慢取出挤出主板；打开固定排线的卡扣，然后断开霍尔传感器排线。

取出时应小心地慢慢向上拉直，避免晃动电缆，以免造成损坏。

如果它损坏了，您可以在[这里](https://detail.tmall.com/item.htm?abbucket=8&id=742413890652&rn=fdccba1f0182bc3695d538e65c3b3337&spm=a1z10.3-b-s.w4011-25177047232.53.1e811c79Wuo3TI&skuId=5118758836326)购买。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_filament_sensor_ribbon_cable.jpeg)

### 6.移除工具头前盖

扣住前盖的底部，缓慢地按图示方向把它拉向自己。之后，固定前盖的卡扣会松开，您即可将其取下。

![](https://wiki.bambulab.com/a1m/replace-filament-cutter/remove_the_print_head_front_cover.jpeg)

### 7.松开切刀刀柄

按住切刀刀柄并用螺丝刀移除螺丝，待螺丝完全取下后，缓慢释放切刀刀柄。

![](https://wiki.bambulab.com/a1m/replace-filament-cutter/press_the_filament_cutter_lever_and_remove_the_screw.jpeg)

### 8.移除挤出机压料块

取下旋转轮，移除挤出机压料块。

|  |  |
| --- | --- |
|  |  |

### 9.移除打印机喷嘴组件

移除喷嘴硅胶套，打开加热组件卡扣取下喷嘴组件；执行此步骤后，才能在下一步中移除挤出机前盖。

|  |  |
| --- | --- |
|  |  |

### 10.移除五通及底座

用 H2.0 内六角扳手移除 2 颗螺丝，然后取出五通及底座。需要注意的是，请小心不要损坏黑色的 FPC 线缆，取出五通后可以将其放在工具头上面，如图所示。

|  |  |
| --- | --- |
|  |  |

### 11.移除挤出机前盖

接下来移除挤出机前盖，首先取出前盖 4 颗固定螺丝；再拧松侧边压紧螺丝（不用完全移除，防止内部弹簧垫片掉落），即可取下前盖。

|  |  |
| --- | --- |
|  |  |

### 12.取出挤出机齿轮

移除前盖之后，将侧边压紧螺丝完全移除，取下垫片和弹簧，之后移除挤出机齿轮。

|  |  |
| --- | --- |
|  |  |

### 13.取出挤出机电机

移除正面电机 4 颗固定螺丝，此时可以从**背面取出电机**。

![](https://wiki.bambulab.com/a1/maintenance/replace-extuder-motor/步骤6-移除挤出齿轮-2.jpg)

## 安装新的挤出机电机

### 1.固定挤出机电机

首先需要将电机从工具头背面装入，从正面使用 4 颗螺丝固定电机。

> 注意：需要将电机引出线缆的位置朝上，螺丝型号为 M2.5\*5 。

|  |  |
| --- | --- |
|  |  |

### 2. 安装挤出机齿轮

首先需要将黄色齿轮安装到轴承内，接下来安装从动轮支架；  
同时需要按住垫片以及弹簧，并拧入螺丝。

> 注意：侧边螺丝型号为 M3\*11，此时不需要完全锁紧，否则会导致前盖较难安装。

|  |  |
| --- | --- |
|  |  |

> 注意：请务必正确安装弹簧和垫片，否则可能会出现挤出机无法咬合耗材，导致挤出异常。

|  |  |
| --- | --- |
|  |  |

### 3.安装挤出机前盖

安装前盖 4 颗固定螺丝，并锁紧侧边压紧螺丝。

> 注意：前盖4颗螺丝型号为 BT2.3\*7。

|  |  |
| --- | --- |
|  |  |

### 4.安装五通组件

将五通及底座装回挤出机上方，锁紧两颗固定螺丝。

> 注意：五通底座 2 颗螺丝型号为 BT2.6\*5。

|  |  |
| --- | --- |
|  |  |

### 5.安装喷嘴组件和硅胶套

然后，将喷嘴组件安装到加热组件上将卡扣锁紧，并安装硅胶套。

![install_the_nozzle.gif](https://wiki.bambulab.com/a1/maintenance/replace-extuder-motor/install_the_nozzle.gif)

安装完成喷嘴组件之后，注意检查安装是否正确。

|  |  |
| --- | --- |
| **正确安装方式** | **错误安装方式** |
|  |  |

### 6.安装切刀刀柄

安装时需要确保将刀片与挤出机的孔对齐。  
在重新固定螺丝之前，请紧握切刀刀柄并保持其位置；在拧紧螺丝时，请注意不要过用力，以防螺丝滑牙。

> 注意：切刀固定螺丝型号为 BT2.6\*14。

|  |  |
| --- | --- |
|  |  |

### 7.装工具头前盖

将工具头顶部的卡扣对准，然后轻轻按压前盖的底部。

安装完成后，您可以听到“咔嗒”声。

![](https://wiki.bambulab.com/a1m/replace-filament-cutter/attach_the_front_cover.jpeg)

### 8.安装挤出主板

首先安装霍尔板 FPC 排线，再安装挤出机电机接头。

|  |  |
| --- | --- |
|  |  |

将挤出主板安装回工具头内，并锁紧三颗固定挤出主板螺丝，您可以按照下图重新连接剩余线缆。

![螺丝.png](https://wiki.bambulab.com/%E8%9E%BA%E4%B8%9D.png)

- 1.热端加热组件（购买链接：[京东](https://item.jd.com/10086621431814.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742608647813&rn=85cf658c1b1b317c1571024be894ae11&spm=a1z10.3-b-s.w4011-25177047232.13.352f1c79UnoIGf&skuId=5293816695460)）
- 2.挤出机电机
- 3.热端冷却风扇（购买链接：[京东](https://item.jd.com/10085237113101.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742494478597&rn=50348b313765fa58496bd7e872f33726&spm=a1z10.3-b-s.w4011-25177047232.13.2b001c79zzjU9Z&skuId=5122905509690)）
- 4.部件冷却风扇（购买链接：[京东](https://item.jd.com/10085237672213.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742158008755&rn=e96fdc9668de1bfe06ae88dd77fe78a2&spm=a1z10.3-b-s.w4011-25177047232.29.69711c792eXiBU&skuId=5122266397335)）
- 5.6.涡流传感器  
  ![线缆.png](https://wiki.bambulab.com/%E7%BA%BF%E7%BC%86.png)

### 9.连接 USB-C 线缆

将 USB- C 以正确的方向插入接口后，锁紧四颗固定螺丝。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_usb_cable_and_4_screws.jpeg)

> **重要提醒！**
>
> **请不要过度拧紧螺丝，否则可能会导致螺纹损坏**。请注意对齐 USB-C 数据线的方向和背面的小凹槽。 USB-C 数据线只能用一种方式安装，正确的方向是数据线接头的凸起对准后方的凹槽。
>
> ![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/usb_cable_orientation.jpeg)

### 10.安装工具头后盖

后盖使用卡扣固定。只需将后盖上的两个卡扣对准，然后推入后盖，直到听到几声“咔嗒”声。

![](https://wiki.bambulab.com/a1m/replace-th-board/back_cover_of_the_print_head_a1m.jpeg)

## 功能验证

打开打印机并尝试进料。如果操作成功，您可以看到耗材从喷嘴组件挤出。

## 操作后的校准步骤

建议您在更换挤出机电机后进行一次全面校准，以确保打印机顺畅运行。

此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换挤出机电机的过程中，打印板可能会受到污染。

## 潜在问题和解决方案

如果您在安装新的挤出机电机时遇到问题，请查阅以下列出的问题及其解决方案：

### 热端温度为0

参照[**安装步骤 8**](#intro)重新连接，检查热端加热组件接头是否正确插入。

务必仔细对齐接头的引脚和挤出主板。

如果问题仍然存在，热敏电阻线缆可能已损坏（白线）。

### 加热组件无法加热

参照[**安装步骤 8**](#intro)重新接线，检查热端加热组件接头是否正确插入。 务必仔细对齐接头的引脚和挤出主板。  
如果问题仍然存在，加热器线可能已损坏（半透明线）。

### 打印机无法正确回中

参照[**安装步骤 8**](#intro)重新接线，检查涡流传感器线缆（5 和 6）是否正确连接至挤出主板。

### 进料霍尔板不再工作

参照[**安装步骤 8**](#intro)检查 FPC 排线是否正确连接至挤出主板。

如果 FPC 排线已损坏，您需要更换进料霍尔板。（购买链接：[京东](https://item.jd.com/10086620804757.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742413890652&rn=a2c4a71cc1ebc454113082a1179bbdfd&spm=a1z10.3-b-s.w4011-25177047232.13.59d31c79bCV2UL&skuId=5118758836326)）

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
