---
path: zh/h2/troubleshooting/extruder-assembly
title: "H2D 挤出机拆解与组装指引"
description: "本文介绍如何拆解与组装 H2D 挤出机"
tags: []
created: 2025-03-25T07:06:39.585Z
updated: 2025-12-03T07:18:50.445Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/extruder-assembly
---

## 何时需要该指南

挤出机应定期进行维护，挤出机组件对打印起到非常重要的作用。

随着使用时间的积累，耗材碎屑、灰尘和其他进入挤出机中的颗粒会在挤出机内部逐渐积累，严重时可能会对打印质量造成影响。当出现以下几种情况，建议您参考本指南的步骤进行操作。

- 由于温度过高，挤出机齿轮，导向组件或从动杆组件中的耗材变形，造成堵塞。
- 由于耗材碎屑或灰尘等异物在挤出机组件内部逐渐积累，从而影响打印质量，如打印纹理不一致
- 需要更换挤出机组件内部的零部件，如挤出机前盖，导向组件，从动杆，凸轮组件，左右切刀及刀柄或挤出齿轮等部件。

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-13.png)

(挤出机零部件购买链接)

挤出机前盖；导向组件；从动杆组件；凸轮组件；左右切刀及刀柄或挤出齿轮

这里补充说明，对于堵塞排查，强烈建议您先查看这篇wiki文章：[H2D堵塞排查](clogging.md)，以确认堵塞是否确实由挤出机组件引起，避免误判故障现象，导致不必要的拆装工作。您可以先拆除热端，观察耗材是否能够正常挤出。如果拆除热端后，耗材仍能正常挤出，则说明并非挤出机堵塞，更可能是热端堵塞。此时，您可以通过清理喷嘴或更换喷嘴来解决问题。

本文的撰文思路是以最少步骤实现挤出机堵塞清理，同时挤出机拆装也可以参考这些步骤。

1. 若完成部分操作后，已将堵塞清理干净，则可跳跃阅读，例如清理耗材碎屑或灰尘一般只需要拆解挤出机前盖导向。若发生堵塞，只要不发生严重卷料，也只需要拆开挤出机前盖，而不需要拆除挤出机从动杆，请按需拆装。
2. 若单独更换左右刀柄或右切刀，可跳过拆除挤出机前盖导向和前盖的步骤，移除工具头前盖后，可直接拆装更换，注意保存好扭簧和切刀刀柄，切刀刀片安装时缺口朝上。
3. 对于挤出机前盖导向的拆装，强烈建议您查看视频操作，因为前盖导向与左右切刀及刀柄存在一定程度的干涉，需要利用技巧拆除。若您觉得跟随视频操作仍然困难，可以先拆切刀刀柄，再拆前盖导向。
4. 为了简化挤出机的拆装步骤，经过验证，我们决定取消这颗螺丝。因此，市面上同时存在带有和不带有这颗螺丝的版本，具体以您收到的为准。

![extruder screw](https://wiki.bambulab.com/h2/troubleshooting/extruder_assembly/extruder-screw-cancel.jpg)

5. 如果从动杆组件发生卡料，您可以参考此教程清理断料：[H2D 从动杆卡料处理指南](dual-extruder-Idlers-clogging.md)

## 所需工具和材料

这次维护预计需要10至60分钟完成，具体所需时间将取决于拆解的程度。

- H2.0和H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 视频指南（拆解挤出机组件）

## 拆解教程

### 步骤 1：降低热床以创造工具头拆装的空间

通过屏幕下降热床，以便于工具头的拆装。确保热端位于室温，关机。

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-11.png)

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-12.png)

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-14.png)

### 步骤 2：移除工具头上方的PTFE管与前面盖

捏住工具头前盖顶部的两角处，向上提起以移除工具头前盖。

以对称的方式，按住黑色外圈，解锁挤出机上方的两个气动接头，释放PTFE管。

![imgi_6_image-8.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_6_image-8.jpg)

![imgi_7_image-9.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_7_image-9.jpg)

### 步骤 3：拆除左右热端

堵嘴片位于升降连杆上，通过拨动连杆，堵嘴片会左右移动。如果您需要拆卸某个热端，而堵嘴片挡住了热端，必须先拨动堵嘴连杆，将堵嘴片移开，然后再进行拆卸，以防在拆除热端时不小心压弯堵嘴片。拨动时，堵嘴片可能因连杆倾斜限位而未能一次拨到位，这时需要粗拨动后再进行精细调整，确保堵嘴片完全到位。

![imgi_8_image-5.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_8_image-5.jpg)

![imgi_9_image-7.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_9_image-7.jpg)

在开始拆热端之前，请先按压两侧切刀进行切料，方便拆除热端。先移除未被堵嘴片堵住的热端硅胶套，解锁卡扣以取下该热端，预扣回加热组件的卡扣。

![imgi_10_image-10.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_10_image-10.jpg)

![imgi_11_image-4.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_11_image-4.jpg)

![imgi_12_image-6.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_12_image-6.jpg)

![imgi_13_image.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_13_image.jpg)

拨动堵嘴连杆，将堵嘴片移至另一边，拆下剩余热端的硅胶套，解锁卡扣以取下热端，预扣回加热组件的卡扣。

![imgi_14_image-1.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_14_image-1.jpg)

![imgi_15_image-2.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_15_image-2.jpg)

![imgi_16_image-3.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_16_image-3.jpg)

![imgi_17_image-15.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_17_image-15.jpg)

### 步骤 4：拆除挤出机前盖导向与左切刀

拧出前盖导向上的4颗螺丝（M2.5x7 \* 3；BT2x6 \* 1）后，用手指向上抵住黑色热端连接件，同时按压左切刀刀柄，使左切刀从切刀螺丝附近的开口槽中脱出一点，然后从前盖导向右下角向外用力撬出前盖导向。

左切刀位于前盖导向中，拆除前盖导向时会被一同带出，请注意保存，防止丢失。

![imgi_18_image-16.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_18_image-16.jpg)  
![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-17.png)

> 如下图所示，挤出机前盖导向部件分为三颗螺丝与四颗螺丝两种版本，该差异不会对打印机使用造成任何影响。
>
> |  |  |
> | --- | --- |
> |  |  |

### 步骤 5：拆除挤出机前盖

拧出挤出机前盖上的2颗螺丝（M2.5x7）， ***取下挤出机前盖时请小心操作，防止FPC线缆被扯断。*** 解开FPC线缆卡扣，即可将挤出机前盖拆除。

![imgi_22_image-18.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_22_image-18.jpg)

![image19.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image19.png)

![imgi_24_image-20.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_24_image-20.jpg)

### 步骤 6：拆除右切刀及左右刀柄

拧下右切刀螺丝（MG2.5x19x5），将右切刀和右刀柄取下。拧下左切刀螺丝（MG2.5x19x5），取下左刀柄。在移除切刀的时候，请注意保存好安装在内部的切刀弹簧。

![imgi_25_image-21.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_25_image-21.jpg)

![imgi_26_image-22.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_26_image-22.jpg)

![imgi_27_image-23.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_27_image-23.jpg)

### 步骤 7：松开左右从动杆上的霍尔排线螺丝并拔掉霍尔板插头

拧下左右从动杆上的霍尔排线螺丝（BT2x5），并松开霍尔排线的插头。将FPC排线小心地从插头中取出，避免损坏FPC排线。

![imgi_28_image-24.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_28_image-24.jpg)

![imgi_29_image-25.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_29_image-25.jpg)

![imgi_30_image-26.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_30_image-26.jpg)

![imgi_31_image-27.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_31_image-27.jpg)

### 步骤 8：拆除挤出机从动杆组件与凸轮组件

拧下从动杆下方的两颗固定螺丝（M2.5x19x5），用手略微将从动杆组件向上推，将从动杆组件与凸轮组件同时取出。

![imgi_32_image-28.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_32_image-28.jpg)

![imgi_33_image-29.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_33_image-29.jpg)

![imgi_34_image-30.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_34_image-30.jpg)

![imgi_35_image-31.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_35_image-31.jpg)

### 步骤 9：拆除挤出机齿轮

最后取下挤出机齿轮。

![image32.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image32.png)

![imgi_37_image-33.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_37_image-33.jpg)

## 安装教程

### 步骤 1：安装挤出机齿轮

将挤出机齿轮重新装回齿槽中。

![imgi_38_image-34.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_38_image-34.jpg)

![imgi_39_image-35.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_39_image-35.jpg)

### 步骤 2：安装凸轮组件与挤出机从动杆组件

先将凸轮组件装回，请注意确保凸轮的凸台处于水平状态，可以接受5°左右的偏差，不用完全处于水平状态。

将从动杆组件的弹簧卡入凸轮下方的位置，圆弧对圆弧。然后向下用力推从动杆组件，当听到一声“咔嗒”的契合声，说明从动杆组件安装到位了。

![image36.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image36.jpg)

![imgi_41_image-37.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_41_image-37.jpg)

![image38.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image38.png)  
![imgi_43_image-39.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_43_image-39.jpg)  
安装左右从动杆固定螺丝（M2.5x19x5），请先将从动杆上的螺孔与框架上的螺孔对齐才能顺利拧入螺丝。同时也可以略微将从动杆组件往前拉出来一点，从从侧面观察螺丝孔。

安装左从动杆螺丝时请不要完全拧紧，让右从动杆保持一定的活动性，便于拧入右从动杆螺丝。待右从动杆螺丝完全拧紧后，再重新将左从动杆螺丝完全拧紧。

![image40.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image40.png)  
![imgi_45_image-41.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_45_image-41.jpg)

![image42.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image42.png)

![imgi_47_image-43.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_47_image-43.jpg)

### 步骤 3：插回左右霍尔板的插头，并锁紧霍尔排线螺丝

将FPC线缆重新插入霍尔板的插头中，请确保FPC线缆的头部完全进入插头中（白线处于水平状态，代表FPC线缆插入到位），再扣合插座。

![imgi_48_image-44.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_48_image-44.jpg)

![imgi_49_image-45.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_49_image-45.jpg)  
拧紧左右从动杆上的霍尔排线螺丝（BT2x5）。

![imgi_50_image-46.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_50_image-46.jpg)

![imgi_51_image-47.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_51_image-47.jpg)

### 步骤 4：安装右切刀及左右刀柄

放回左切刀扭簧，将刀柄上的孔与螺丝孔对齐，然后拧紧切刀螺丝（MG2.5x19x5）。安装左切刀刀柄时左扭簧上臂需要靠着左切刀刀柄  
**注意区分左右切刀扭簧和左右切刀刀柄，左扭簧上臂靠左，右扭簧上臂靠右。左切刀刀柄比右切刀刀柄更长**。

![imgi_52_image-48.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_52_image-48.jpg)

![imgi_53_image-49.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_53_image-49.jpg)  
![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-50.png)

如果切刀螺丝拧得太紧，可能导致切刀卡住，如果遇到这种情况，只需略微拧松切刀螺丝即可。

![imgi_55_image-51.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_55_image-51.jpg)

![imgi_56_image-52.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_56_image-52.jpg)  
接下来安装右刀柄和右切刀（切刀刀片不区分左右）。安装切刀时请确保切刀的缺口面朝上，然后将其放入刀柄的切刀槽中。

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-53.png)

![imgi_58_image-54.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_58_image-54.jpg)  
放回右切刀弹簧，将右切刀刀柄上的孔与螺丝孔对齐，然后拧紧切刀螺丝（MG2.5x19x5）。安装时右扭簧上臂也需要靠着右切刀刀柄。

![imgi_59_image-55.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_59_image-55.jpg)

![imgi_60_image-56.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_60_image-56.jpg)  
![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-57.png)

### 步骤 5：安装挤出机前盖

在安装挤出机前盖之前，需要使用螺丝刀调整凸轮组件的角度，方便后续安装。

将螺丝刀捅入凸轮组件的小孔中，同时用手固定住左从动杆组件，然后并使凸轮旋转，一直旋转到凸台平面与从动杆平行为止。

![imgi_62_image-58.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_62_image-58.jpg)

![image-59.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image-59.png)  
![imgi_64_image-60.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_64_image-60.jpg)  
将FPC线缆插入挤出机前盖插头，确保FPC线缆的头部完全进入插头中（白线处于水平状态，代表FPC线缆插入到位），再锁紧插头。安装挤出机前盖时，下图中前盖的凸面需要与凸轮组件的侧面保持平行，可以使用螺丝刀插入小孔中进行调整，直到挤出机前盖扣入合适的位置。

![imgi_65_image-61.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_65_image-61.jpg)

![imgi_66_image-62.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_66_image-62.jpg)

![imgi_67_image-63.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_67_image-63.jpg)  
折叠侧面的FPC线缆，并整理好FPC线缆，并将其塞入工具头侧面的缝隙中。

![image-64.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image-64.png)

![imgi_69_image-65.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_69_image-65.jpg)  
然后拧入挤出机前盖的两颗螺丝（M2.5x7）。

> 注意！锁紧螺丝前需要确保两端螺丝孔位完全对齐，如果一端存在翘起情况时强行拧入可能会导致挤出机前盖断裂。  
> 下右图为两侧螺孔正确对准示意，左图则没有对齐。  
> ![正确安装挤出机前盖final.jpg](https://wiki.bambulab.com/h2/maintenance/replace-quick-change-tool-interface/%E6%AD%A3%E7%A1%AE%E5%AE%89%E8%A3%85%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%89%8D%E7%9B%96final.jpg)

![imgi_71_image-74.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_71_image-74.jpg)

![imgi_72_image-72.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_72_image-72.jpg)

### 步骤 6：安装挤出机前盖导向与左切刀

左切刀需要跟随前盖导向一起安装。确保左切刀的缺口面朝上，然后将其放入前盖导向的切刀槽中。

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-71.png)

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-70.png)

安装前盖导向时，需要一直往上顶住黑色热端连接件，并轻微按压左切刀，将其调整到一个合适的角度便于左切刀进入，然后将前盖导向装入。最后按压两侧切刀，同时用力将前壳完全压平。

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-66.png)

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-67.png)

![](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/image-68.png)

然后重新锁紧前盖导向上的4颗螺丝（M2.5x7 \* 3；BT2x6 \* 1）。

![imgi_78_image-69.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_78_image-69.jpg)

### 步骤 7：安装左右热端

与拆卸的操作一样，如果您需要安装某个热端，而堵嘴片挡住了热端，必须先拨动堵嘴连杆，将堵嘴片移开，然后再进行安装，以防在拆除热端时不小心压弯堵嘴片。拨动时，堵嘴片可能因连杆倾斜限位而未能一次拨到位，这时需要粗拨动后再进行精细调整，确保堵嘴片完全到位。

安装右喷嘴，锁紧喷嘴卡扣并戴上硅胶套。

![imgi_79_image-73.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_79_image-73.jpg)

![imgi_80_image-78.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_80_image-78.jpg)  
拨动堵嘴连杆，将堵嘴片移至另一边，然后安装左喷嘴。同样锁紧喷嘴卡扣并戴上硅胶套。

请注意，安装左热端硅胶套时，需要保证硅胶套不能倾斜，以免造成旁边的挡风板片变形。

![image79.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image79.jpg)  
![imgi_82_image-77.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_82_image-77.jpg)

![imgi_83_image-76.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_83_image-76.jpg)

### 步骤 8：安装工具头的PTFE管与前面盖

连接2根PTFE管，拖链上方的PTFE管连接到右挤出机，拖链下方的PTFE管连接到左挤出机。

![imgi_84_image-75.jpg](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/imgi_84_image-75.jpg)  
装回工具头前面盖的时候，可以先扣入挤出机下方的位置，再往后推，将前面盖安装到位。

![image80.png](https://wiki.bambulab.com/h2/troubleshooting/excluder_assembly_zh/excluder_assembly_zh_new/image80.png)

## 如何验证完成/成功

重新打开打印机并在屏幕上控制左右挤出的切换以及进料来验证一切是否正常。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
