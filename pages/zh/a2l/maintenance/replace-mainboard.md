---
path: zh/a2l/maintenance/replace-mainboard
title: "A2L 更换主板"
description: "本文介绍了如何更换 A2L 主板"
tags: []
created: 2026-06-01T13:12:55.684Z
updated: 2026-06-17T01:39:01.225Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-mainboard
---

## A2L 主板

![dlb077_or_dlb078.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/dlb077_or_dlb078.png)

## 何时使用本指南？

- XYZ电机工作异常
- 设备无法正常启动
- 主板外观损坏
- 拓竹售后技术支持建议更换

## 所需的工具和材料

A2L 主板

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀
- 十字螺丝刀
- 镊子（可选）

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子元件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## 视频指南

## **拆卸步骤**

### 1. 拆除前底盖

将Z轴降低至距离热床约 5-8 cm位置。  
![dk001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk001.webp)

翻转打印机露出底壳。  
![dk002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk002.jpg)

使用 H2.0 内六角螺丝刀拆下图示 12 颗螺丝，蓝色标记的两颗螺丝与其他 10 颗不同，请注意区分。  
![dk019.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk019.jpg)

取下 Y 轴张紧器盖板。  
![dk006.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk006.webp)

用手扣住前底盖边缘，向外解锁卡扣取下前底盖。  
![dk012.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk012.webp)

### 2. 移除WiFi天线

使用镊子或铲刀从底座上移除 WiFi 天线。  
![wifi001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/wifi001.webp)

### 3. 断开线缆

使用 H1.5 内六角螺丝刀拆下图示两颗螺丝，拔除工具头线缆。  
![dz005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz005.jpg)![dz006.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz006.jpg)

依照标号顺序移除插头，1、2端子需按下锁扣拔出，3-4号端子可以直接拔出。  
![ap001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap001.jpg)![ap002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap002.jpg)

向上掀起排线扣，移除5号屏幕排线。  
![pm001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/pm001.webp)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 4/6 Pin 接口板 | 4 | Y 电机 |
| 2 | AC 板 | 5 | 屏幕组件 |
| 3 | Z 电机 |  |  |

### 4. 移除主板

使用十字螺丝刀拧松固定电源插头的三颗螺丝，拔出电源插头。  
![dy114.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy114.jpg)

将电源线从线槽中取出。  
![dy113.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy113.webp)

使用 H2.0 内六角螺丝刀移除 1 颗固定螺丝。  
![ap003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap003.jpg)

使用 H1.5 内六角螺丝刀移除 4 颗主板固定螺丝，取下主板（含主板散热片、电源线、WIFI天线、防火罩）。  
![ap005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap005.jpg)

> 此时主板仍连接着电源线和WiFi天线，请小心托住主板，注意保护线缆。

## **安装步骤**

### 1. 安装主板

如果更换了新的主板（附赠蓝色导热硅脂），请先用无纺布擦除Y轴导轨上旧的灰色硅脂，然后均匀涂抹一层新的蓝色导热硅脂。**请勿混合使用不同颜色/类型的硅脂。** 若未更换主板，则跳过此步。  
![ap006.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap006.jpg)

将主板小心放回原位，注意不要挤压或卡住周围的线缆。使用 H1.5 内六角螺丝刀锁入四颗固定螺丝。  
![ap005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap005.jpg)

使用 H2.0 内六角螺丝刀锁入1颗螺丝。  
![ap003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap003.jpg)

将电源线按图示路径卡入线槽。  
![dy115.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy115.jpg)

将电源插头装回电源模块中，并使用十字螺丝刀锁紧固定螺丝。  
![dy114.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy114.jpg)

> 电源线插头位置和颜色必须与图示完全一致，接错可能导致设备烧毁！

### 2. 连接线缆

**确保插头凸起面向上**，将其插入AP板插座，然后用H1.5内六角螺丝刀锁入两颗固定螺丝。  
![dz007.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz007.jpg)![dz005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz005.jpg)

将剩余插头依次装回主板，插头均有防呆措施，请仔细核对方向并安装到位。  
![ap001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap001.jpg)

### 3. 安装WiFi天线

将天线粘贴到图示位置。  
![wifi002.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/wifi002.webp)

### 4. 安装前底盖

将前底盖装回，按压四周确保安装到位。使用 H2.0 内六角螺丝刀锁入 12 颗螺丝，蓝色标记的两颗螺丝与其他 10 颗螺丝不同，请注意区分。  
![dk011.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk011.webp)![dk019.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk019.jpg)

装回 Y 轴张紧器盖板。  
![dk007.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk007.webp)

小心地将打印机翻转回正常放置位置。  
![dk016.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dk016.jpg)

## 联系客户支持注册序列号

> 重要提醒：  
> 新 SN 注册成功后，旧 SN 将会作废，旧的主板也将不能再被注册或绑定。

更换了主板的机器，由于新的 SN 未注册，无法进行绑定操作。因此，在更换主板后首次开机时，可跳过绑定机器的步骤，并检验更换 AP 板是否解决问题 （网络连接问题除外）。确认问题解决后，您可登录拓竹官网 <https://bambulab.com/zh/support> 申请绑定新序列号（SN），或联系拓竹科技客服注册新 SN。  
![register_sn.jpg](https://wiki.bambulab.com/x2d/maintenance/ap-board/register_sn.jpg)

## 功能校验

注册新的序列号后，将打印机绑定至您的账户。

为确保更换顺利，请打开打印机并使用。

如果打印机如预期工作，则安装成功。

## **操作后的校准步骤**

建议您在更换完主板后进行一次全面校准，以确保打印机顺畅运行。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队。  
> 我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
