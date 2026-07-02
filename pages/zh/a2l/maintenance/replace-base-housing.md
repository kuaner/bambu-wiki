---
path: zh/a2l/maintenance/replace-base-housing
title: "A2L 更换底座"
description: "本文介绍了如何更换 A2L 底座"
tags: []
created: 2026-06-30T09:58:03.054Z
updated: 2026-07-01T01:56:16.639Z
source: https://wiki.bambulab.com/zh/a2l/maintenance/replace-base-housing
---

## A2L 底座

![faz069.png](https://public-cdn.bblmw.com/wiki/new/a2l/danpintu/faz069.png)

如果您收到的是底座+底盖合并组件包，请根据更换需求从中取出对应部件操作。

## 何时使用本指南？

- 底座破损/变形
- 拓竹售后技术支持建议更换

## 所需的工具和材料

- A2L 底座
- H2.0 内六角螺丝刀
- 尼龙扎带
- 镊子（可选）

### 安全警告

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## 拆卸步骤

更换底座操作难度较大，建议每拆卸一个组件就转移到新的底座上，依次完成所有组件更换。

### 1. 分离龙门架

使用 H2.0 内六角螺丝刀拆除两颗螺丝，拔除连接线缆。

|  |  |
| --- | --- |
| lmj001.jpg | lmj002.jpg |

打开 Z 电机转接线盖，断开 Z 电机插头。

![lmj004.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/lmj004.webp)

移除 Y 轴上盖，使用 H2.0 内六角螺丝刀拆除图示的 10 颗螺丝。

|  |  |
| --- | --- |
| yzgb001.webp | lmj006.jpg |

向上抬升 X 轴，取下底座部分。

|  |  |
| --- | --- |
| lmj007.jpg | lmj008.webp |

### 2. 移除前后底盖

将底座部分翻转放置在桌面上，注意屏幕部分需要悬空。

![rc011.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc011.jpg)

使用 H2.0 扳手拆除图示 17 颗螺丝，其中蓝色标记的螺丝与其他螺丝不同，请注意分别保存。

|  |  |
| --- | --- |
| dz002.jpg | 4pin001.jpg |

取下 Y 轴张紧器盖板、前底盖、后底盖。

|  |  |  |
| --- | --- | --- |
| dz003.jpg | dz004.webp | 4pin002.webp |

### 3. 移除电源模块

使用十字螺丝刀拧松对应螺丝，将电源模块连接线依次移除。

|  |  |
| --- | --- |
| ac012.jpg | ac013.jpg |

使用 H2.0 六角螺丝刀拆下图示两颗螺丝，取下电源模块。

|  |  |
| --- | --- |
| ac015.jpg | ac014.webp |

### 4. 移除 AC 板

参照下方提示依次拔出 AC 板上的插头。

![ac001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac001.jpg)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 热床信号线 | 4 | 电源模块转接线 |
| 2 | 热床加热线 | 5 | 主板 — AC 连接线 |
| 3 | 市电输入 |  |  |

> 后续操作涉及市电部分，请务必再次确认设备已经完全断电。

1 号连接器可以直接向上拔出，5 号位置连接器需按下卡扣解锁后拔出。

![ac009.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac009.webp)

2 号位置有两个独立插头，需要使用螺丝刀等尖锐工具将插头弹片向后顶出一段距离解锁，然后拔出插头。

|  |  |
| --- | --- |
| ac003.webp | ac002.jpg |

3 号位置有两个插头，掀开盖板，使用十字螺丝刀拧松对应螺丝后可拔出对应线缆。

![ac005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac005.webp)

使用 H1.5 内六角螺丝刀拆除两颗螺丝，取下 AC 板。

|  |  |
| --- | --- |
| ac008.jpg | ac007.webp |

### 5. 移除热床

使用 H2.0 内六角螺丝刀拆下一颗螺丝，取下热床地线。

![rc002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc002.jpg)

参照图示向上抬起热床线缆卡扣解锁，将热床线缆从底座拉出。

|  |  |
| --- | --- |
| rc004.jpg | rc006.webp |

翻转底座，使用 H2.0 螺丝刀拧出图示四颗螺丝，取下热床组件。

![rc007.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc007.jpg)

### 6. 移除主板和 WiFi 天线

使用镊子或铲刀从底座上移除 WiFi 天线。

![wifi001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/wifi001.webp)

使用 H1.5 内六角螺丝刀拆下图示两颗螺丝，拔除工具头线缆。

|  |  |
| --- | --- |
| dz005.jpg | dz006.jpg |

依照标号顺序移除插头，1、2 端子需按下锁扣拔出，3-4 号端子可以直接拔出。

|  |  |
| --- | --- |
| ap001.jpg | ap002.jpg |

向上掀起排线扣，移除 5 号屏幕排线。

![pm001.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/pm001.webp)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 4/6 Pin 接口板 | 4 | Y 电机 |
| 2 | AC 板 | 5 | 屏幕组件 |
| 3 | Z 电机 |  |  |

将电源线从线槽中取出。

![dy113.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy113.webp)

使用 H2.0 内六角螺丝刀移除 1 颗固定螺丝。

![ap003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap003.jpg)

使用 H1.5 内六角螺丝刀移除 4 颗主板固定螺丝，取下主板（含主板散热片、电源线、WiFi 天线、防火罩）。

![ap005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap005.jpg)

> 此时主板仍连接着电源线和 WiFi 天线，请小心托住主板，注意保护线缆。

### 7. 移除屏幕组件

将屏幕转动到与底座约 45° 夹角，观察屏幕转轴处的凸起结构，将其与安装孔的缺口对齐，然后用力拔出屏幕。

|  |  |
| --- | --- |
| pm009.jpg | pm003.webp |

### 8. 移除 Y 轴导轨

使用 H2.0 内六角螺丝刀拧下 1 颗螺丝，断开地线。

![rc012.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc012.jpg)

断开 Y 电机连接线。

![y003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/y003.webp)

使用 H2.0 内六角螺丝刀拧下图示 10 颗螺丝，取下 Y 轴组件。

|  |  |
| --- | --- |
| y002.png | y005.webp |

### 9. 移除接口板

按住插头卡扣，拔出连接线插头。

![4pin003.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/4pin003.webp)

使用 H1.5 内六角螺丝刀拧松两颗螺丝，取下 4/6 Pin 接口板。

![4pin005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/4pin005.jpg)

移除 4/6 Pin 接口板连接线。

![4pin010.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/4pin010.webp)

### 10. 移除剩余线缆

使用 H1.5 内六角螺丝刀拧下图示两颗螺丝，将工具头线缆卡扣向外推出。

|  |  |
| --- | --- |
| dz010.jpg | dz008.webp |

取出工具头线缆（底座端）。

![dz011.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz011.webp)

取出主板-AC 连接线。

![rc013.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc013.jpg)

断开 Y 电机插头，将 Y、Z 电机转接线从卡扣内依次取出。

![xcb002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/test/xcb002.jpg)

## 安装步骤

### 1. 安装 Y 轴组件

![y025.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/y025.jpg)

将 Y 电机线穿过底座，装回 Y 轴组件。

> 注意：如果更换了新的 Y 轴组件，还需要擦除主板和 Y 轴导轨上旧的导热硅脂并在图示位置涂抹附赠的蓝色导热硅脂。

|  |  |
| --- | --- |
| y009.jpg | y006.webp |

使用 H2.0 内六角螺丝刀锁入图示 10 颗螺丝。

![y002.png](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/y002.png)

### 2. 安装热床组件

将热床固定孔对齐滑车螺纹孔放好，使用 H2.0 内六角螺丝刀锁入四颗螺丝固定。

![rc007.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc007.jpg)

将热床线缆穿进底座，并卡入线槽固定。

![rc008.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc008.jpg)

装回地线，使用 H2.0 内六角螺丝刀锁入两颗螺丝。

![y001.png](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/y001.png)

### 3. 安装线缆

安装工具头线缆（底座端），将工具头线缆（底座端）穿入底座内部。

![dz012.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz012.webp)

使用 H1.5 内六角螺丝刀锁入两颗螺丝固定线缆卡扣。

![dz010.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz010.jpg)

安装 4/6 Pin 接口板连接线。

![4pin008.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/4pin008.webp)

将 4/6 Pin 接口板装回，使用 H1.5 内六角螺丝刀锁入两颗螺丝固定。

|  |  |
| --- | --- |
| 4pin006.webp | 4pin005.jpg |

连接 4/6 Pin 接口板连接线。

![4pin011.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/4pin011.jpg)

安装 Y、Z 电机连接线。参照图示将 Y、Z 电机转接线重新穿好，连接 Y 电机插头。

![xcb002.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/test/xcb002.jpg)

安装主板—AC 连接线。将主板—AC 连接线装回。

![rc013.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/rc013.jpg)

### 4. 安装 AC 板

将 AC 板装入原位，使用 H1.5 内六角螺丝刀锁入两颗螺丝固定。

|  |  |
| --- | --- |
| ac010.webp | ac008.jpg |

1、2、5 号位置插头可以直接插入，注意将 2 号插头保护套装回。

![ac001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac001.jpg)

3 号插头，先将端子插入方形垫片下方，然后使用十字螺丝刀锁紧螺丝固定。**注意插头及线缆颜色需要与图示保持一致**。

![ac111.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/ac111.jpg)

> 插头位置和线缆颜色必须与图示完全一致，接错可能导致设备烧毁！

### 5. 安装主板和 WiFi 天线

将主板小心放回原位，注意不要挤压或卡住周围的线缆。使用 H1.5 内六角螺丝刀锁入四颗固定螺丝。

![ap005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap005.jpg)

使用 H2.0 内六角螺丝刀锁入 1 颗螺丝。

![ap003.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap003.jpg)

将电源线按图示路径卡入线槽。

![dy115.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy115.jpg)

**确保插头凸起面向上**，将其插入 AP 板插座，然后用 H1.5 内六角螺丝刀锁入两颗固定螺丝。

|  |  |
| --- | --- |
| dz007.jpg | dz005.jpg |

将剩余插头依次装回主板，插头均有防呆措施，请仔细核对方向并安装到位，5 号插头会在后续步骤安装。

![ap001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap001.jpg)

将天线粘贴到图示位置。

![wifi002.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/wifi002.webp)

### 6. 安装电源

将电源模块放入对应位置，使用 H2.0 六角螺丝刀锁入两颗螺丝。

|  |  |
| --- | --- |
| ac016.webp | ac015.jpg |

参照图示位置依次将连接线插入，并使用十字螺丝刀锁紧对应螺丝。

![ac017.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ac017.jpg)

> 所有插头位置必须与图示完全一致，否则有损坏设备风险。

### 7. 安装屏幕

将屏幕转动到与底座约 45° 夹角，轻微左右转动对准孔位缺口，推动屏幕安装到位。

![pm004.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/pm004.webp)

插入屏幕排线，注意排线有金手指的一面向下安装，按下排线扣。

![pm002.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/pm002.webp)

### 8. 安装前后底盖

参照图示装回前、后底盖，按压确保卡扣到位。

|  |  |
| --- | --- |
| gjtxl014.webp | 4pin007.webp |

装回 Y 轴张紧器盖板。

![gjtxl015.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/gjtxl015.jpg)

使用 H2.0 内六角螺丝刀锁入图示 17 颗螺丝，其中蓝色标记的两颗螺丝与其他位置不同，请注意区分。

|  |  |
| --- | --- |
| dz002.jpg | 4pin001.jpg |

### 9. 安装龙门架

参照图示将底座放入龙门架，使用 H2.0 内六角螺丝刀锁入 10 颗螺丝固定。

|  |  |
| --- | --- |
| lmj009.webp | lmj006.jpg |

将热床向后移动一小段距离，插入 Y 轴上盖，对齐上盖前方并推动到位，然后下压上盖后方安装到位。

|  |  |
| --- | --- |
| yzgb002.webp | yzgb003.webp |

连接 Z 电机线，装回 Z 电机转接线盖。

![lmj005.webp](https://public-cdn.bblmw.com/wiki/new/a2l/replace-printer-frame/lmj005.webp)

将线缆有凸起一侧对齐插入插槽缺口，使用 H2.0 内六角螺丝刀锁入两颗螺丝。

|  |  |
| --- | --- |
| lmj012.jpg | lmj001.jpg |

## 功能验证

打开打印机，观察首页 WiFi 信号是否正常，然后进入设置选择校准，运行校准流程，校准正常完成则表示上述操作正确。

|  |  |  |
| --- | --- | --- |
| pm101.jpg | pm102.jpg | pm103.jpg |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
