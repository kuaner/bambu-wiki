---
path: zh/x1/maintenance/x1e-replace-power-switch-assembly
title: "X1E 电源开关座更换指南"
description: "更换 X1E 电源开关座的操作步骤"
tags: ["x1e"]
created: 2024-10-15T10:51:38.127Z
updated: 2024-10-25T07:19:54.631Z
source: https://wiki.bambulab.com/zh/x1/maintenance/x1e-replace-power-switch-assembly
---

## 适用打印机型号

X1E

## 电源开关

电源开关组件是安装在打印机背面左下角的一个模块。它包含一个电源线插座、一个控制打印机电源的开关以及用于连接打印机电源、交流电板和地线的电缆。

## 何时使用

- 开关损坏
- 连接线缆损坏
- 开关座接触不良

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的电源开关座
- H1.5 内六角扳手
- H2.0 内六角扳手
- 十字螺丝刀
- 镊子、撬棒或其他扁平工具

## 移除电源开关

### 步骤 1：断开电源线

关闭电源，从电源插座上拔下电源线。

### 步骤 2：拆除背板

1. 移除玻璃上盖。根据下图所示，用 H2.0 内六角扳手移除 9 颗螺丝 A （红色），4 颗螺丝 B（橙色），1 颗螺丝 C（紫色）;

![](https://wiki.bambulab.com/x1/maintenance/x1e/rear_panel_screws_2.jpg)

2. 将背板向右推动少许，将背板从右侧张紧器处松出；然后向左用力，将背板从左侧张紧器处松出，取下背板。

|  |  |
| --- | --- |
|  |  |

### 步骤 3：移除废料滑梯

1. 用 H1.5 内六角扳手移除 2 颗螺丝；

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/excess_chute_screws_2.jpg)

2. 用 H2.0 内六角扳手移除 1 颗螺丝，并移除废料滑梯。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：拆除右侧板

1. 用 H2.0 内六角扳手移除右侧板后方的 4 颗螺丝；

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_rear_4_screws.jpg)

2. 撕开 EVA 垫，用 H2.0 内六角扳手移除右侧板顶部的 1 颗螺丝;

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_top_1_screw.jpg)

3. 用 H2.0 内六角扳手移除右前立柱处的 4 颗螺丝;

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_front_4_screws.jpg)

4. 侧放打印机，使右侧板朝上，用 H2.0 内六角扳手移除底下的 2 颗螺丝;

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_bottom_2_screws.jpg)

5. 从右侧板两边同时用力，将右侧板从从打印机上取下。

> 注意：右侧板除了螺丝外，在中间横梁处与打印机有泡棉粘接，所以拆除右侧板时会比较费力，建议至少两个人一起配合操作。

|  |  |
| --- | --- |
|  |  |

### 步骤 5：移除网线及 AMS 接口板

用 H2.0 内六角扳手移除 3 颗螺丝，将接口板松出。

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/ams_interface_board_screws_2.jpg)

### 步骤 6：移除风道

用 H2.0 内六角扳手移除 3 颗螺丝，取下风道。

|  |  |
| --- | --- |
|  |  |

### 步骤 7：移除电源冷却风扇

移除 4 颗螺丝，取下电源冷却风扇。

仅需移除螺丝取下风扇，无需断开风扇的连接线，以便于移除电源保护盖。

![电源风扇.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E7%94%B5%E6%BA%90%E9%A3%8E%E6%89%87.jpg)

### 步骤 8：移除电源保护盖

1. 用 H1.5 内六角扳手移除 7 颗螺丝；

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/power_cover_screws.jpg)

2. 再用 H1.5 内六角扳手移除线缆上方的一颗螺丝，将热床线缆从走线槽中取出，并移除电源保护盖。

![线槽螺丝.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E7%BA%BF%E6%A7%BD%E8%9E%BA%E4%B8%9D.jpg)

### 步骤 9：断开电源线与电源模块和 AC 板的连接

1. 用十字螺丝刀拧松下图红框中的 3 根线缆，向左拔出断开连接;

![开关-ac连接.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E5%BC%80%E5%85%B3-ac%E8%BF%9E%E6%8E%A5.jpg)

2. 然后从电源上断开输入线，移除地线插头上的胶套，按压解锁插头并移除供电线地线。

![开关-电源连接.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E5%BC%80%E5%85%B3-%E7%94%B5%E6%BA%90%E8%BF%9E%E6%8E%A5.jpg)

> 如果无法直接拔出，您可以将电源先拆下再拔出。

### 步骤 10：取下地线

从靠近电源开关座竖梁外侧使用 H2.0 扳手松开地线固定螺丝，取下地线。

![地线.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E5%9C%B0%E7%BA%BF.jpg)

> 注意：竖梁处固定有两根地线，一根为整机接地（连接到电源开关座上）另一根为热床地线。只需松下整机接地地线即可。

### 步骤 11：取出电源开关

使用扁平工具从电源开关座两侧框架上的四个开口处翘松 4 个卡扣，随后即可将电源开关座松出。

|  |  |
| --- | --- |
|  |  |

从右向左将断开的电源开关线缆穿过扣中取出，随后即可将电源开关座连同电缆一起取下完成拆卸。

![电源开关线缆.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E7%94%B5%E6%BA%90%E5%BC%80%E5%85%B3%E7%BA%BF%E7%BC%86.jpg)

## 安装电源开关座

### 步骤 1：安装电源开关座

将新的电源开关座所有缆线穿过电源开关座框架后向内推，将电源开关座通过卡扣固定到位。

![电源开关安装或取下.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E7%94%B5%E6%BA%90%E5%BC%80%E5%85%B3%E5%AE%89%E8%A3%85%E6%88%96%E5%8F%96%E4%B8%8B.jpg)

### 步骤 2：连接地线

将地线穿过竖梁后使用 H2.0 内六角固定在竖梁上。

![](https://wiki.bambulab.com/x1/maintenance/replace-power-switch-assembly/ground-connection.png)

> 注意：接地为保证用电安全的重要措施，请务必牢固固定地线。

### 步骤 3：连接电缆

将电缆左向右依次卡入两个线槽中。用十字螺丝刀将电缆接头通过十字螺丝固定在 AC 板上，并将插头插入电源中。

|  |  |  |
| --- | --- | --- |
| 电源开关线缆.jpg | 开关-ac连接.jpg | 开关-电源连接.jpg |

> 注意：在连接顶部 AC 板时，线序从上向下应为零-火-地，即颜色为蓝-棕-黄。

### 步骤 4：安装电源保护盖

1. 安装电源保护盖，锁入 7 颗螺丝；

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/power_cover_screws.jpg)

注意：安装电源保护盖前，请检查电源线的安装位置，避开螺丝孔：

![](https://wiki.bambulab.com/x1/maintenance/x1e/cable_layout.jpg)

2. 将热床线缆插入走线缆和线扣，并锁紧走线槽上方 1 颗螺丝。

![线槽螺丝.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E7%BA%BF%E6%A7%BD%E8%9E%BA%E4%B8%9D.jpg)

### 步骤 5：安装电源冷却风扇

安装电源冷却风扇，注意风扇电缆的出口方向应在左下角。锁入 4 颗螺丝固定电源冷却风扇。

![电源风扇.jpg](https://wiki.bambulab.com/x1/maintenance/x1e-replace-power-switch-assembly/%E7%94%B5%E6%BA%90%E9%A3%8E%E6%89%87.jpg)

### 步骤 6：安装网线及 AMS 接口板

将网线及 AMS 接口板装回打印机，并用 H2.0 内六角扳手锁紧 3 颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/ams_interface_board_screws_2.jpg)

### 步骤 7：安装风道

在机箱控温风扇下方安装好风道，锁入 3 颗螺丝固定。

![](https://wiki.bambulab.com/x1/maintenance/x1e/power-supply/air-duct_screws.jpg)

### 步骤 8：安装废料滑梯

1. 将废料滑梯安装到打印机上，滑梯两侧的卡扣要滑到位，并确认没有压到连接线，然后先使用 H2.0 内六角扳手拧紧一颗螺丝；

|  |  |
| --- | --- |
|  |  |

2. 再使用 H1.5 内六角扳手拧紧一颗螺丝

![](https://wiki.bambulab.com/x1/maintenance/replace-heat-bed-v3/excess_chute_screws_2.jpg)

### 步骤 9：安装右侧板

1. 将右侧板安装到侧放的打印机上，对齐安装位置；

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/remove_the_right_panel.jpg)

2. 在底座处锁入 2 颗螺丝 C；

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_bottom_2_screws.jpg)

3. 正放打印机，对齐螺丝孔，在顶部横梁处锁入 1 颗螺丝 C，可以将 EVA 垫贴回原位；

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_top_1_screw.jpg)

4. 在右前立柱处锁入 4 颗螺丝 C;

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_front_4_screws.jpg)

5. 在右侧板后方锁入 4 颗螺丝 A。

![](https://wiki.bambulab.com/x1/maintenance/x1e/heater-unit/rp_rear_4_screws.jpg)

> **注意**：在锁右侧板螺丝时，可能会因为放置位置的偏差导致螺丝拧入困难。因此，可以先不锁紧右前立柱和后方的 8 颗螺丝，待所有螺丝 F 都拧上后，再一起锁紧。

### 步骤 10：安装背板

1. 先将料管支架穿过背板，将右侧张紧器处的位置安装到位，可以使用扳手按压边缘，将其安装好；
2. 然后向左用力拉着背板，将左侧张紧器处的位置安装到位，可以使用扳手按压边缘，辅助安装；
3. 最后锁入 9 颗螺丝 A（红色），4 颗螺丝 B（橙色）和 1 颗螺丝 C（紫色），将背板固定。

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 功能确认

连接电源线并启动电源。运行设备自检/校准流程，如果没有报错，更换电源开关座完成。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
