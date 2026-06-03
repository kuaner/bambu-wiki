---
path: zh/a1-mini/maintenance/x-motor-replacement-guide
title: "A1 mini X 电机更换"
description: "本文提供A1 mini X 电机拆解和组装的相关指引和注意事项。"
tags: ["a1 mini"]
created: 2025-06-13T09:00:17.146Z
updated: 2025-07-16T04:16:08.394Z
source: https://wiki.bambulab.com/zh/a1-mini/maintenance/x-motor-replacement-guide
---

## X 电机

X 电机是安装在打印机 X 轴上，用于驱动工具头在 X 轴方向上移动的步进电机。

## 何时使用

- X 电机烧坏
- 经官方技术支持通过分析日志，确认是 X 电机故障

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击此处联系在线技术支持 （服务时间 9:00-21:00）](hhttps://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的 X 电机（购买链接：[京东](https://item.jd.com/10086620136322.html) [天猫](https://detail.tmall.com/item.htm?spm=a21n57.sem.item.8.35c33903oaIL3p&priceTId=2147803317497775368038390e1dbc&utparam=%7B%22aplus_abtest%22%3A%226ddccf99a11ab2bdd1f9e20485044f06%22%7D&id=742508255527&ns=1&abbucket=3&xxc=taobaoSearch&pisk=gHJqYsGjuxHV-dQAiL6azCZL56BAnOuBid_1jhxGcZbccF6w_eQ7CmBj6O8NzFQfGtbbQd7kxcejDjCG7EBc6I_1lNWwXeoSRvMBDnBOt2gIdYdGsmWLmrbg57xlxOS0AkXownBOIVr7IXMeDEpxCgPcjgmPfGNcSF2iEubRb-VMSZfurMSdIOYGiT4lviScSZjgZ0ShxGVcIRfuEMsFjrYGI05lyGXGjFXiNC-Dj8SCicC7X0x7_T1V-nbzL3pPmNVv0ar4mLRPMwDCzR2MUi-wy90LLf_H9Z1C-UD73O-lbU5Bg2y27hxps_JaomTHrC8G2Q3a_wRMcBpRGlVD4d7VtKfzxRtF3GYG_Q3UdiWXa6J2McUkme_2ttK_YqtPTQ5dq_qaitOBAdCHnxzdP6Iwz6Oq8-8h4DUOqIhXBIzg_sjR4wir46s0IFPxIXV365Clpg7IciNT6sjR4wir45FOZaIPRmsf.)）
- H2.0 内六角扳手
- H1.5 内六角扳手
- 剪钳

## 移除 X 电机

### 步骤 1：移除底板

向后放倒打印机，使 Z 轴的支柱接触桌面。  
用 H2.0 内六角扳手移除 2 颗螺丝 (BT2.6×8)，再移除 14 颗螺丝 (BT3×8)，拉扯尼龙扎网使底板松动，移除底板。

![a1_mini_x电机拆装_底板螺丝拆装-23.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_%E5%BA%95%E6%9D%BF%E8%9E%BA%E4%B8%9D%E6%8B%86%E8%A3%85-23.png)

### 步骤 2：移除主板风扇

用 H2.0 内六角扳手移除 2 颗螺丝 (MG2.5×15)，再从主板上断开主板风扇连接线。

![](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1mini_x_motor_2_2.png )

### 步骤 3：断开连接线

移除 2 颗螺丝 (BT2×5) 和压片，从主板上断开USB线、摄像头连接线和 X 电机连接线，请注意摄像头连接线是带锁扣的，要按压解锁后断开。  
![a1_mini_x电机拆装-24.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85-24.png)

### 步骤 4：移除摄像头线和 X 电机罩

从电机罩前盖下方用力，移除电机罩前盖，断开摄像头连接线，用内六角扳手穿过线夹并撬出，移除线夹;

![a1_mini_x电机拆装_4.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_4.png)

去除留在线材上的线夹，撕掉尼龙扎网一端的胶布，抽出摄像头连接线和 X 电机线；

![a1_mini_x电机拆装_5.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_5.png)

移除 1 颗螺丝 (M3×10)，2 颗螺丝 (M3×6)，取下 X 电机罩组件。

![a1_mini_x电机拆装_6.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_6.png)

### 步骤 5：拧松 X 皮带

拧松 X 轴张紧螺丝一圈（请勿完全松开），使皮带变松。

![](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x电机拆装_7.png)

### 步骤 6：移除 X 电机

移除 2 颗螺丝 (M2×4.5) 移除电机罩后盖；移除 4 颗螺丝 (M3×5)，取下 X 电机。

![a1_mini_x电机拆装_8.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_8.png)

## 组装指引

### 步骤 1：安装 X 电机

安装 X 电机，电机的排线朝下，将电机主动轮穿过 X 皮带，锁入 4 颗螺丝 (M3×5)。

![a1_mini_x电机拆装_9.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_9.png)

### 步骤 2：张紧 X 皮带

将 X 轴移动到移动到靠近 Z 轴中间位置，避免移动工具头时划伤热床；

![a1_mini_x电机拆装_10.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_10.png)

确保张紧螺丝已被拧松且不是完全松开的状态，用手移动工具头沿 X 轴方向来回运动 3 次，然后重新拧紧张紧螺丝。

![a1_mini_x电机拆装_11.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_11.png)

### 步骤 3：安装 X 电机罩和摄像头线

按箭头方向将电机罩安装到转接支架上，注意电机电缆要穿过电机罩，在 X 轴上锁入 1 颗螺丝 (M3×10)、在电机罩内锁 2 颗螺丝 (M3×6) 将电机罩固定;

![a1_mini_x电机拆装_12.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_12.png)

将摄像头电缆小头的一端连接到摄像头上，然后依次将 X 电机线和摄像头线穿过编织网管；

![a1_mini_x电机拆装_13.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_13.png)

确认线夹的方向，将线夹安装到电机罩上，然后确认安装方向，盖上电机罩前盖；

![a1_mini_x电机拆装_14.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_14.png)

将X电机罩后盖安装到电机罩上，锁入 2 颗螺丝 (M2×4.5)；

![a1_mini_x电机拆装_15.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_15.png)

用胶布将编织网管的另一端缠住。

![](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x电机拆装_16.png)

### 步骤 4：连接电缆

将 X 电机线、摄像头线连接到主板上，连接USB线，确认磁环的位置，并用 2 颗螺丝 (BT2×5) 将压片锁定，整理好线缆，以确保底板能顺利安装，并且主板风扇在运行中不会碰到线缆。

![a1_mini_x电机拆装_17.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_17.png)  
![a1_mini_x电机拆装_18.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_18.png)

### 步骤 5：安装主板风扇

安装主板风扇，风扇的排线朝左，锁入 2 颗螺丝 (MG2.5×15) 固定，连接风扇排线。

![a1_mini_x电机拆装_19.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_19.png)

### 步骤 6：安装底板

安装底板，对齐位置后，锁入 14 颗螺丝（BT3×8）固定; 然后安装走线夹，锁 2 颗螺丝 (BT2.6×8) 固定；正放打印机。  
![a1_mini_x电机拆装_底板螺丝拆装-23.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_%E5%BA%95%E6%9D%BF%E8%9E%BA%E4%B8%9D%E6%8B%86%E8%A3%85-23.png)

## 功能确认和设备校准

完成以上组装指引的全部操作步骤后，启动打印机，进入控制界面，点击屏幕上的 “-X” 或 “X” 按钮移动 X 轴，以确认 X 电机是否正常运行。

![a1_mini_x电机拆装-25.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85-25.png)

在校准页面，仅选择振动补偿，点击开始。  
请执行此步骤以确保打印机正常工作。

![a1_mini_x电机拆装_21.png](https://wiki.bambulab.com/a1-mini/aimini-x-motor-replacement/a1_mini_x%E7%94%B5%E6%9C%BA%E6%8B%86%E8%A3%85_21.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
