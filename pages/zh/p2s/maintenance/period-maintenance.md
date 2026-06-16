---
path: zh/p2s/maintenance/period-maintenance
title: "P2S 定期清洁维护建议"
description: "关于 P2S 打印机的一些日常维护和保养建议。"
tags: []
created: 2025-10-14T13:14:40.579Z
updated: 2026-06-04T06:47:19.408Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/period-maintenance
---

## XYZ 轴清洁润滑

### 保养周期

根据设备使用频率差异，建议执行以下保养周期：

- **高频使用场景**（日均打印时长≥5 小时）：XY 轴每月进行 1 次全面清洁润滑保养；Z 轴每 3 个月进行 1 次深度保养。
- **常规使用场景**（日均打印时长 1-5 小时）：XY 轴每 2 个月进行 1 次保养；Z 轴每 4 个月进行 1 次保养。
- **低频使用场景**（日均打印时长＜1 小时）：XY 轴每 3 个月进行 1 次保养；Z 轴每 5 个月进行 1 次保养。

### 所需材料

- 润滑油
- 润滑脂
- 无纺布
- 酒精

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，**避免在高温状态下操作**，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### X 轴润滑保养

沿 X 轴光轴轴向进行往复擦拭，直至表面无可见油污及耗材碎屑。建议同步检查皮带表面，若存在污渍可使用无纺布进行清洁

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/015.webp)

采用点滴方式沿光轴轴向均匀涂抹**润滑油**（每 5cm 长度滴加 1-2 滴），上下两根光轴均需处理。

> 请勿涂抹润滑脂

![点滴润滑油.webp](https://wiki.bambulab.com/p2s/maintenance/period-maintenance/%E7%82%B9%E6%BB%B4%E6%B6%A6%E6%BB%91%E6%B2%B9.webp)

手动推动工具头沿 X 轴全程往复运动 3-5 次，确保润滑油在光轴表面形成均匀油膜。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/010.webp)

完成后可以用无尘布轻擦光轴两端，去除多余油防止吸附灰尘。

|  |  |
| --- | --- |
| 擦拭多余润滑油1.jpg | 擦拭多余润滑油2.jpg |

> 推动工具头时请保持缓慢速度，以确保石墨套能充分吸收润滑油；若移动速度过快，易导致润滑油被直接推至中框，影响润滑效果。

### Y 轴润滑保养

使用淋喷酒精的无纺布对左右两侧 Y 轴光轴进行全面擦拭。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/011.webp)

完成以上动作后为光轴涂抹润润滑油。（用量参照 X 轴标准）

> 请勿涂抹润滑脂

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/020.png)

手动驱动工具头沿 Y 轴前后往复运动 3-5 次，使润滑油充分渗透至轴承内部。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/002.webp)

如果油脂光轴过多请用无尘布擦拭光轴表面多余油脂。

### Z轴润滑保养

> ℹ️ **注意：** 极少数情况下，Z轴皮带在运转时可能会发出吱吱声。在皮带与Z轴皮带张紧器惰轮的接触处滴一小滴润滑油可以帮助降低噪音。过多的润滑油可能会导致Z轴运转不正常。

打开打印机电源，在控制面板上执行“**回零**”命令，等待热床返回其回零位置，然后点击向下按钮将热床降至最低点。

|  |  |
| --- | --- |
|  |  |

使用蘸有酒精的无纺布对左右两侧丝杆、光轴及热床尾部丝杆进行擦拭，确保螺纹间隙内无残留物。同时重点清理丝杆螺母与丝杆接触部位，可配合镊子清理耗材残留。

|  |  |
| --- | --- |
|  |  |

完成后为三根丝杆均匀涂抹润滑脂，左右两侧光轴涂抹润滑油。

|  |  |
| --- | --- |
|  |  |

完成以上步骤后通过控制面板驱动热床从最低位升至最高位，再降至最低位，重复 3-5 个循环，使润滑脂和润滑油均匀分布于丝杆和光轴。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/006.webp)

接下来我们还需要润滑 Z 轴轴承。

如下图所示，为三根丝杆底部轴承添加润滑油。如果底部有存在耗材碎屑异物，可以使用无纺布擦拭干净。

|  |  |
| --- | --- |
|  |  |

### 全面校准

完成打印机 XYZ 三轴的清洁润滑后，需进入设备校准界面执行**全面校准程序**，以确保机械部件在最佳状态下协同工作。具体包括：**电机降噪、振动补偿、自动热床调平**

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/lubricate-x-y-z-axis/022.png)

## 更换活性炭滤芯

当滤芯出现严重脏污时，为保证过滤效果，建议及时更换。从侧边卡扣处打开并拆除活性炭滤芯盖，拉住滤芯上下拉手即可取出。

|  |  |
| --- | --- |
|  |  |

![00112.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/period-maintenance/00116.png)

> 若滤芯盖脏污严重且常规清洁无效，可将其置于水龙头下冲洗，同时用刷子清理。**注意**：水洗后必须彻底擦干滤芯盖，因其周围存在电子器件，残留水分可能影响器件正常功能。

## 挤出机清洁

1. 用镊子打开挤出接口板的连接器盖子，断开进料霍尔板线缆。

   ![dipsconnect_fpc_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/dipsconnect_fpc_007.png)
2. 使用H2.0内六角扳手移除4颗螺丝，取下挤出机。

   |  |  |
   | --- | --- |
   |  |  |
3. 使用H1.5内六角扳手移除2颗螺丝，取下霍尔开关板组件。

   |  |  |
   | --- | --- |
   |  |  |

> 挤出机内部包含较多小型配件，为防止零件脱落，需将其放置在洁净平台上，且保持齿轮朝上进行操作。

4. 用H2.0内六角扳手拧松1颗螺丝，从挤出机上取下黄色挤出主动轮。

   ![yellow_gear_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/yellow_gear_014.png)
5. 对下图所示的两个齿轮位置进行润滑处理（润滑脂）。请勿涂抹过量润滑脂，飞溅到耗材上将导致打印不沾。

   ![555.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/period-maintenance/555.png)

> 关于挤出机齿轮的详细拆装步骤，可参考 [P2S 挤出机拆装指南](replace-extruder-components.md)。

## 喷嘴清洁

屏幕上控制喷嘴加热到250℃左右，小心取下喷嘴并用干净的纸巾擦拭。

![喷嘴擦拭清理.webp](https://wiki.bambulab.com/h2/maintenance/period-maintenance/%E5%96%B7%E5%98%B4%E6%93%A6%E6%8B%AD%E6%B8%85%E7%90%86.webp)

> 建议带上隔热手套完成这项清洁工作，注意高温烫伤。

清理完喷嘴后请检查屏幕上加热组件的温度是否仍维持在250℃，再清理加热组件表面。

> H2S 与 P2S加热组件结构相似，清理操作相同

![h2s加热组件.webp](https://wiki.bambulab.com/h2/maintenance/period-maintenance/h2s%E5%8A%A0%E7%83%AD%E7%BB%84%E4%BB%B6.webp)

## 工具头风扇维护

P2S 的工具头上有部件冷却风扇以及热端风扇，长期使用后可能附着灰尘，导致风扇转速降低。

|  |  |
| --- | --- |
| 部件冷却风扇 | 热端风扇 |

- **保养工具、材料：** 镊子、毛刷、无尘布
- **保养方案：** 清洁
- 部件冷却风扇：长时间使用风扇内可能有较多异物或灰尘堆积，可以拧下背部四颗螺丝，再用手指顶住扇叶，推出风扇后进行清洁；  
  ![部件冷却风扇.jpg](https://wiki.bambulab.com/p2s/maintenance/period-maintenance/%E9%83%A8%E4%BB%B6%E5%86%B7%E5%8D%B4%E9%A3%8E%E6%89%87.jpg)
- 热端风扇：根据[更换 P2S 热端加热组件/热端风扇](replace-hotend-heating-assembly-and-cooling-fan.md)指南拆下热端风扇，检查风扇是否有异物阻挡或灰尘堆积，进行清理。

## 工具头切刀维护

P2S 挤出机中使用的工具头切刀在换料过程切割耗材。 随着长时间的切割，切刀的刀片可能会变钝，因此应定期检查以确保刀片仍然锋利。

对于 PLA/PETG/ABS/PC 等常规耗材，应每 8-12 卷检查一次刀片。 如果刀片变钝，请更换它。

对于 PA+CF/PA+GF/PPA+CF 等磨料耗材，刀刃会很快变钝，因此我们建议在打印 4-10 卷磨料耗材后进行检查。 如果刀片变钝，请更换它。

![cutter_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace_cutter_lever/cutter_005.png)

> 详细更换步骤请参考[切刀刀片更换指南](replace-filament-cutter-lever.md)。

## 清洁实况摄像头

打印机长期使用后，挥发性有机物颗粒可能附着在摄像头镜头上，导致远程查看画面模糊等问题。建议每6个月清洁一次摄像头（强挥发材料如ABS等需要缩短清洁时间）。

![00112.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/period-maintenance/00113.webp)

## 更换擦嘴硅胶

硅胶擦嘴用于清除喷嘴上的残余废料。若硅胶擦嘴出现损坏或变形，为确保喷嘴清洁效果，建议及时更换。

![00112.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/period-maintenance/00116.webp)

## 打印板清洁

P2S 标配了纹理 PEI 打印板，它由 PEI 材料喷涂在不锈钢板上而成，能够用于打印多种常用的材料，并无需使用任何的粘合剂。为保持最佳的粘附力，建议定期清洁打印板，同时应避免手指直接接触打印板表面的情况，以防止皮肤油脂附着到打印板表面，影响附着效果。PEI 打印板的清洁方式请查阅以下链接：

[Bambu Textrued PEI Plate 清理指南](../../filament-acc/acc/pei-plate-clean-guide.md)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
