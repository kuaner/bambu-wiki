---
path: zh/h3c/maintenance/replace-x-axis-assembly
title: "X轴组件更换指南"
description: ""
tags: []
created: 2026-11-03T13:06:43.348Z
updated: 2026-11-09T12:58:46.783Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-x-axis-assembly
---

## X轴组件

X 轴组件是安装了工具头滑车的 X 轴导轨，通过电机和皮带的驱动，可实现工具头在左右方向的移动，用于控制工具头沿 X 轴方向的运动。  
（补单品图）

## 何时更换

- X 轴滑车上的螺丝孔滑牙或结构损坏
- 光轴异常，影响滑动

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![img_01457bbe50f0.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_01457bbe50f0.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 1. 由于需要将工具头上功能组件都移除，需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 拆装 X 轴的方案有两种，一种是将整个 X 轴工具头组件从打印机上拆下来后，再移除上面的配件，这种方案请参考 WIKI：[X 轴工具头组件更换指南](replace-tool-head-with-x-axis-assembly.md)， 将 X 轴工具头组件取出，然后依据各功能配件的拆装指引逐一移除；二是直接在打印上将工具头配件逐一移除后，再将 X轴组件从打印机上取下。
> 3. 由于**操作步骤比较多**，如果在产品质保期内出现需要更换 X轴组件的需求，请与我们的技术支持人员沟通是否有其他解决方案后再处理。

## 移除 X 轴组件

### 第 1 步 移除工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 移除工具头前盖、顶盖和后盖。

### 第 2 步 移除工具头电路板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)，移除 TH 板和挤出接口板。

### 第 3 步 移除工具头滑车盖上的所有配件

请参考以下 WIKI 列表中相应的内容，移除对应的配件。

| WIKI 列表 | 参考内容 |
| --- | --- |
| [涡流线圈更换指南](replace-nozzle-eddy-sensor.md) | 拆解部分：第 2 步 移除涡流线圈 |
| [工具定位槽更换指南](replace-tool-holder.md) | 拆解部分：第 2 步 移除涡流线圈 |
| [从动轮组件更换指南](replace-idler-assembly.md) | 拆解部分： 第 3 步 调整变距凸轮位置 第 4 步 移除从动轮组件 |
| [工具头切料组件更换指南](replace-cutter-push-arm-assembly.md) | 拆解部分：第 2 步 移除工具头切料组件 |
| [热端风扇更换指南](replace-hotend-cooling-fan.md) | 拆解部分： 第 2 步 松出风扇线缆 第 3 步 移除热端风扇 |
| [工具识别传感器更换指南](replace-tool-reader.md) | 拆解部分：第 3 步 移除工具识别传感器 |
| [泊位标定传感器更换指南](replace-dock-alignment-sensor.md) | 拆解部分：第 3 步 移除泊位标定传感器 |
| [锁紧组件更换指南](replace-toollock-assembly.md) | 拆解部分：第 3 步 移除锁紧组件 |
| [部件冷却风扇更换指南](replace-part-cooling-fan.md) | 拆解部分：第 2 步 移除部件冷却风扇 |
| [裹头检测组件更换指南](replace-nozzle-clumping-sensor-assembly.md) | 拆解部分：第 4 步 移除裹头检测霍尔板 |

### 第 4 步 移除 USB 线缆和工具头电机

请参考以下 WIKI 列表中相应的内容，移除对应的配件。

| WIKI 列表 | 参考内容 |
| --- | --- |
| [工具头摄像头](replace-toolhead-camera.md) | 拆解部分：第 2 步 移除工具头摄像头 |
| [USB-C 线 及 拖链更换指南](replace-cable-chain.md) | 拆解部分：第 5 步 移除 USB- C 线 |
| [变矩电机更换指南](replace-2012-flexfeed-motor.md) | 拆解部分：第 4 步 移除变距电机 |
| [挤出电机更换指南](replace-2521-extruder-servo-motor.md) | 拆解部分：第 4 步 移除挤出电机 |
| [锁紧电机更换指南](replace-2012-toollock-motor.md) | 拆解部分：第 4 步 移除锁紧电机 |

### 第 4 步 移除左右视窗

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，移除打印机的左右两侧视窗。

（提示：以下两步直接使用了 拆装 X轴工具头组件的步骤和照片，请忽略实际照片的差异，只关注操作步骤）

### 第 5 步 将 XY 皮带从工具头组件上移除

用 H2.0 内六角扳手按图中螺丝标识的顺序，移除 3 颗螺丝，将左侧 XY 皮带固定支架松出。

|  |  |
| --- | --- |
| img_8a033665262a.jpg | img_1f79bad44c7c.jpg |

用 H1.5 内六角扳手将皮带末端的压紧块撬出，移除固定支架。

|  |  |
| --- | --- |
| img_2314ee5ec558.jpg | img_10f0e2b21a85.jpg |

从 X 电机一侧拉 XY 皮带，将两根皮带都从 Y 滑车上移除。

|  |  |
| --- | --- |
| img_d3071053ecb9.jpg | img_631ee6148384.jpg |

同样的操作步骤，将右侧的 XY 皮带从工具头和 Y 滑车上移除。

|  |  |
| --- | --- |
| img_2a5824c33947.jpg | img_65c52fcec2d1.jpg |

> **温馨提示：**  
> 为了避免在操作时，误将 XY 皮带完全拉到打印腔体外，导致要从后侧重新穿皮带，可以在将 XY 皮带从 Y 滑车中松出后，重新将固定支架装上。  
> ![img_66efb43dfb39.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_66efb43dfb39.jpg)

### 第 6 步 移除 X 轴工具头组件

（左右两侧操作一样）  
前后移动 X 轴，使固定金属盖板的螺丝露出，用 H1.5 内六角扳手移除 4 颗螺丝。

|  |  |
| --- | --- |
| img_20031997bd20.jpg | img_bdf51d5caca8.jpg |

移动 X 轴使金属盖板完全露出，从 Y 光轴下侧取出金属盖板。

|  |  |
| --- | --- |
| img_7811fc1dd34f.jpg | img_ceeb0840537f.jpg |

同样的操作移除另一侧的金属盖板。  
然后在两侧 Y 滑车处反向使力移动 Y 滑车，X 轴会倾斜并从 Y 轴承上松出，移除 X轴工具头组件。  
![img_39a48e540013.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_39a48e540013.jpg)

## 安装 X 轴组件

### 第 1 步 安装 X 轴工具头组件

手动调整 Y 直线轴承的位置，使轴承外缺口处于约呈45度朝外的状态。

|  |  |
| --- | --- |
| img_87c91e6263fa.jpg | img_403d446f76d1.jpg |

然后呈 45 度放置 X 轴工具头组件卡入滑车组件，若 Y 轴承有很明显的凸出部分，可横放内六角扳手压平（后面安装金属盖板时也会微调）  
![img_384aa394a595.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_384aa394a595.jpg)

检查金属盖板上的字母标识来区分安装位置： L 安装在左侧，R 安装在右侧。  
![img_58d7c0c4f596.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_58d7c0c4f596.jpg)

将右侧盖板从边框与 Y 光轴间隙处放置到横梁上，注意字母标识是正向的。

|  |  |
| --- | --- |
| img_fb5c5b949196.jpg | img_7811fc1dd34f.jpg |

然后移动 X 轴并调整位置将金属盖板安装到滑车上，对齐螺丝孔，锁上 4 颗螺丝固定。如果螺丝位置没有对齐，盖板上的挂钩卡住 Y 轴承后，可以进行移动和调整。

|  |  |
| --- | --- |
| img_9949d8fbcb9b.jpg | img_cb54615b2222.jpg |

同样的操作，安装另一侧的金属盖板。

### 第 2 步 安装 XY 皮带到工具头

（如果在前面拆除皮带时，选择了使用支架固定皮带，这时请先将支架移除）  
先安装需要穿过前立柱的皮带（左侧是靠上的皮带，右侧是靠下的皮带）。具体步骤如下：

1. 皮带直接穿过 Y 轴上的通孔；  
   ![img_be3f6acb2843.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_be3f6acb2843.jpg)
2. 皮带从前惰轮外侧穿入并送内侧穿出，穿出后用另一只手将皮带拉向 Y 滑车；

|  |  |
| --- | --- |
| img_bbda532a9f40.jpg | img_c5eaae64c496.jpg |

温馨提示：如果穿皮带有阻力，可以将手更靠近惰轮位置再用力推，也可以稍微将皮带沿背面折弯后再穿。  
3. 将皮带再次穿到 Y 滑车上，但需要折向工具头位置。 为了避免皮带直接穿过 Y 滑车，这里可以用另一根皮带先穿过 Y 滑车进行遮挡，并作为引导皮带辅助穿过。

|  |  |
| --- | --- |
| img_8a4f1a6ae36b.jpg | img_9fc205bbbfa6.jpg |

4. 将另一条皮带从另一个惰轮位置穿入，皮带先折向工具头。  
   ![img_dee680ff0501.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-x-axis-assembly/zh/img_dee680ff0501.jpg)

两条皮带都穿过 Y 滑车后，可以将皮带穿到固定支架上，并用压块压紧，压反向拉皮带可以使压块更好地压紧皮带。

|  |  |
| --- | --- |
| img_b37975677dc8.jpg | img_81527551f7a0.jpg |

将 XY 皮带固定支架安装到工具头上，用手压着固定支架，先锁中间位置的 1 颗螺丝，然后再锁上下 2 颗螺丝。

|  |  |
| --- | --- |
| img_fdeec0f0fd9f.jpg | img_0ab80a41add1.jpg |

类似的操作步骤，安装另一侧的皮带并固定到工具头上。

### 第 3 步 安装左右视窗

请参考 WIKI: [视窗更换指南](replace-side-glass-left.md)，安装打印机的左右两侧视窗。

### 第 4 步 安装工具头电机、工具头摄像头和 USB 线缆

请参考以下 WIKI 列表中相应的内容，安装对应的配件。

| WIKI 列表 | 参考内容 |
| --- | --- |
| [锁紧电机更换指南](replace-2012-toollock-motor.md) | 安装部分：第 1 步 安装锁紧电机 |
| [挤出电机更换指南](replace-2521-extruder-servo-motor.md) | 安装部分：第 1 步 安装挤出电机 |
| [变矩电机更换指南](replace-2012-flexfeed-motor.md) | 安装部分：第 1 步 安装变距电机 |
| [USB-C 线 及 拖链更换指南](replace-cable-chain.md) | 安装部分：第 2 步 安装拖链 |
| [工具头摄像头](replace-toolhead-camera.md) | 安装部分：第 1 步 安装工具头摄像头 |

### 第 5 步 安装工具头滑车盖上的所有配件 （连接线缆除外）

请参考以下 WIKI 列表中相应的内容，安装对应的配件。

| WIKI 列表 | 参考内容 |
| --- | --- |
| [裹头检测组件更换指南](replace-nozzle-clumping-sensor-assembly.md) | 安装部分：第 2 步 安装裹头检测霍尔板 |
| [部件冷却风扇更换指南](replace-part-cooling-fan.md) | 安装部分：第 1 步 安装部件冷却风扇 |
| [锁紧组件更换指南](replace-toollock-assembly.md) | 安装部分：第 1 步 安装锁紧组件（含润滑锁紧插好销） |
| [泊位标定传感器更换指南](replace-dock-alignment-sensor.md) | 安装部分：第 1 步 安装泊位标定传感器 |
| [工具识别传感器更换指南](replace-tool-reader.md) | 安装部分： 第 1 步 安装工具识别传感器 第 2 步 锁工具识别传感器螺丝 |
| [热端风扇更换指南](replace-hotend-cooling-fan.md) | 安装部分： 第 1 步 安装热端风扇 第 2 步 整理风扇线缆 |
| [工具定位槽更换指南](replace-tool-holder.md) | 拆解部分：第 1 步 安装工具定位槽 |
| [从动轮组件更换指南](replace-idler-assembly.md) | 安装部分： 第 1 步 调整凸轮位置，检查轴承 第 2 步 安装从动轮组件 |
| [涡流线圈更换指南](replace-nozzle-eddy-sensor.md) | 安装部分：第 1 步 安装涡流线圈 |
| [工具头切料组件更换指南](replace-cutter-push-arm-assembly.md) | 安装部分：第 1 步 安装工具头切料组件 |

### 第 6 步 安装 TH 板

请参考 WIKI：[工具头电路板更换指南](replace-extruder-connection-board.md)，安装 TH 板和挤出接口板。

### 第 7 步 安装工具头外壳

请参考 WIKI：[工具头外壳更换指南](replace-toolhead-front-cover.md)， 移除工具头前盖、顶盖和后盖。

### 第 8 步 张紧 XY 皮带

拧松 **左右两个** XY 张紧器的螺丝，让张紧器自然张紧，前后移除工具头 2~ 3 次，然后重新锁紧张紧器螺丝。

## 功能验证

连接电源并打开打印机，发起打印无报错即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
