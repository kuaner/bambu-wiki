---
path: zh/h2s/maintenance/replace-cooling-fan-for-hotend
title: "更换 H2S 热端风扇"
description: ""
tags: []
created: 2025-08-26T12:57:07.526Z
updated: 2026-01-19T04:20:07.011Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-cooling-fan-for-hotend
---

## 何时使用本指南？

本指南用于解决热端风扇出现的问题。

需要更换热端风扇的常见情况包括：

- 热端风扇发出噪音
- 热端风扇发生故障，不会转动
- 联系拓竹售后技术支持后建议更换

## **工具和材料**

- H2S 热端风扇

- H1.5 六角扳手
- 25 分钟

> ⚠️ 注意事项
>
> 如果您收到的热端风扇 SKU 为 **FAH047**, 请在安装前 **确认风扇朝向是否正确**。若发现颠倒， 参考 [附录步骤](#fan-appendix) 进行调整。若您收到的是 **FAH047-V1**，则无需执行附录中的操作，可直接进行安装。
>
> ![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/0.png)
>
> 正确安装后，**带有标签的一面**应朝向出风口，以便将气流吹向热端的散热片。
>
> ![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/10.jpg)

## 螺丝清单

![image_-_2025-08-14t201101.568.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image_-_2025-08-14t201101.568.png)

- 螺丝 A: 部件冷却风扇左右两侧螺丝，共 2 颗： BT2x5
- 螺丝 B: 部件冷却风扇背面（和后盖共锁）以及工具头后盖螺丝，共 3 颗：BT2x6.5
- 螺丝 C: 热端风扇螺丝，共 2 颗：BT2x4

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## **拆除热端风扇**

### 步骤 1：松开部件冷却风扇

- 拧下部件冷却风扇的 3 颗螺丝，其中背面的 1 颗螺丝与工具头后盖共锁。

![image_98.png](https://public-cdn.bblmw.com/wiki/new/aether/image_98.png)

![image_97.png](https://public-cdn.bblmw.com/wiki/new/aether/image_99.png)

![image_100.png](https://public-cdn.bblmw.com/wiki/new/aether/image_100.png)

- 松开螺丝后，风扇会自然下垂。请勿拉扯风扇，以免损坏连接器！

![image_-_2025-08-06t120707.663.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image_-_2025-08-06t120707.663.png)

### 步骤 2：松开工具头后盖

- 移除工具头后盖上方的 2 颗螺丝，打开模块接口盖子；

![image_-_2025-08-06t121047.140.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image_-_2025-08-06t121047.140.png)  
![image_-_2025-08-06t120718.885.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image_-_2025-08-06t120718.885.png)

- 打开接口盖子后，可将手指伸入，从内壁轻微用力，往后推工具头后盖。

![image.png](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-1.png)

### 步骤 3：断开 TH 板上的连接器

- 断开热端加热组件插头；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-2.png)

- 撕开热端风扇插头的醋酸胶布；

> 注意：安装时需要贴回此醋酸胶布，请妥善保管！

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-3.png)

- 捏住插头根部，从垂直 PBC 板的方向施力，断开热端风扇插头。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-4.png)  
![4.webp](https://public-cdn.bblmw.com/wiki/new/aether/4.webp)

### 步骤 4：移除热端

参考此教程移除热端：[点击此处跳转](replace-silicone-sock-and-hotend.md)

### 步骤 5：移除热端风扇

- 卸下热端风扇的 2 颗螺丝，移除热端风扇；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-5.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-6.png)

- 从理线槽中取出线缆；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-7.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-8.png)

![1.webp](https://public-cdn.bblmw.com/wiki/new/aether/1.webp)

## **安装热端风扇**

### 步骤 1：安装新的热端风扇

- 将新的热端风扇线缆卡入理线槽中；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-9.png)

- 将风扇带标签的一面朝向热端，对准螺丝孔位（参考下图红色和黄色圆圈）；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-10.png)

- 将风扇线缆折在图示凹槽内，安装风扇。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-11.png)

![hotend_fan_cable.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/hotend_fan_cable.webp)

- 锁紧固定风扇的两颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-12.png)

### 步骤 2：安装热端

参考此教程安装热端（[点击此处跳转](replace-silicone-sock-and-hotend.md)）

### 步骤 3：连接 TH 板上的连接器

- 连接风扇线缆，将插头的插孔面朝 TH 板上的插座（插头金属焊点面朝机箱背面），对齐后下压插头；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-13.png)

![1.webp](https://public-cdn.bblmw.com/wiki/new/aether/3.webp)

- 贴回醋酸胶布；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-14.png)

- 预对准风扇的螺丝孔位，将风扇线缆排在 TH 上，并向上拉动，将多余的线缆折叠，避免被风扇外壳或工具头后盖压破导致风扇异常。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-hotend-heating-assembly/manage_cable.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-15.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-16.png)

- 整理好线缆后，插入热端加热组件插头，并用热端加热组件插头和线缆压住部件冷却风扇线缆。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-17.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-18.png)

> 插入热端加热组件时，确保对准孔位，不要错排。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-19.png)

### 步骤 4：安装工具头后盖

- 安装工具头后盖；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-20.png)

- 安装后，注意检查部件冷却风扇线缆是否位于专用的缺口处，避免被后盖边框挤压；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-21.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-22.png)

- 锁入 2 颗后盖固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-23.png)

### 步骤 5：安装部件冷却风扇

- 对准螺丝孔，安装部件冷却风扇；卡入风扇时，注意不要压住风扇线缆。

> 如果线缆过长，需退回至安装指南的步骤一，先折叠多余的线缆。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-24.png)

- 锁入3颗螺丝，固定部件冷却风扇。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-25.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-26.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-cooling-fan-for-hotend/image-27.png)

## 功能验证

为确保一切正常，请打开打印机，设置热端温度至 100℃。几秒后，热端风扇应开始转动，表示上方操作均正确。

## 操作后的校准步骤

建议您在更换完热端风扇后进行一次全面校准，以确保打印机顺畅运行。

此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换热端风扇的过程中，构建板可能会受到污染。

## 附录：风扇方向更换步骤

1. 用 **H1.5 六角扳手**拧下热端风扇上方的 **2 颗螺丝**；

![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/1.webp)

2. 从风扇框架内侧轻轻顶出风扇，将风扇取出后反转，使**带有标签的一面朝向热端**：

![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/3.webp)

3. 对齐孔位，锁回 2 颗螺丝并确保风扇牢固固定

![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/5.webp)
> ⚠️ 注意事项
>
> 热端风扇仅有 **两颗固定螺丝**。这两颗螺丝均位于靠近直角凸起的高边缘处，如下图所示：
>
> ![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/8.png)
>
> 热端风扇的 **线缆**位于这两颗螺丝的对侧，如下图所示：
>
> ![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/9.png)
>
> 安装完成后请在次确认 **风扇朝向是否正确**。
>
> ![](https://wiki.bambulab.com/h2s/maintenance/replace-cooling-fan-for-hotend/0.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
