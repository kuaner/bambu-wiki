---
path: zh/makerworld/cyberbrick/component-list
title: "CyberBrick 模块列表"
description: "本章节列举了 cyberbrick 每个零件的基础规格和典型连接设置。"
tags: ["cyberbrick"]
created: 2025-05-23T08:36:11.834Z
updated: 2025-08-19T06:34:34.825Z
source: https://wiki.bambulab.com/zh/makerworld/cyberbrick/component-list
---

## 核心板

核心板顾名思义是CyberBrick提供逻辑控制、无线连接和编程功能的核心，目前，所有CyberBrick项目都共用一款核心板，这使得创作者们有一个统一的标准进行开发，而用户可以在不同项目之间轻松切换而无需反复购买相对昂贵的主控板。  
核心板的本质是一块搭载了基于ESP32-C3微处理器(MCU)的主控板，引出了关键的GPIO引脚、并提供蓝牙和WiFi连接功能。其配备有CyberBrick专属的底层运行库、可支持蓝牙升级的固件，并允许创作者在上层使用MicroPython进行开发，编程相关详情请参考[代码库链接](https://makerworld.com/en/cyberbrick/api-doc/)。

### 核心板-XA003

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename.png)  
Type-C接口输入电压：5V  
电池输入电压：3.7V-12.6V  
遥控距离：4m

- 邮票口:焊接引脚。允许用户焊接引线实现自定义电路连接。
- 复位按键:按键开关。按下以复位核心板主控程序。
- 用户按键:按键开关。用户可编程自定义按键功能。
- Type-C接口:Type-C接口。通过数据线连接至PC以编程和烧录程序。
- 排针:排针引脚。用于连接至扩展板。

#### 核心板灯语

1. - 开机但未连接:绿灯常亮
2. - 蓝牙已连接:蓝灯常亮
3. - 主从机2.4G连接:黄色常亮
4. - 蓝牙与主从机2.4G均连接:蓝黄交替闪烁
5. - 发送与更新配置:绿灯闪烁,频率2Hz持续至传输结束
6. - 识别灯效:绿灯闪烁,频率1Hz,持续5s
7. - 固件升级错误：红灯常亮
8. - 固件等待升级：白灯常亮
9. - 固件升级中：白灯快速闪烁

#### Pinout图

如需自行设计和连接电路，可参考下图:  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-14.png)

## 功能底板

除了有核心板来提供运算能力，还需要连接各种外围设备才能完成有趣的功能。CyberBrick首批项目中，最广泛的应用就是各类遥控模型，车辆上往往会用到电机、舵机、LED等输出设备，而遥控器端则需要能读取按钮、摇杆等输入设备的信号。因此，我们推出了两款功能底板分别用于发射端和接收端，他们的作用一方面是把主控板GPIO转接为外围设备的接口，另一方面是搭载驱动电机等功能所需要的额外电路。  
标准化、免焊接的连接器和标准库也是CyberBrick相较于传统开发板的一大优势：您只需要按照说明插上所需的模块并在软件里调用相应的控件，而无需过多操心接口、电压等参数的兼容性，或是四处寻找需要调用的代码库。

### 发射底板-XA005

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-13.png)  
遥控器发射板的左右分别有3个模拟量输入通道、下方有4个开关输入通道,背面灰色插槽同样为核心板插槽。可以通过XH2.54电源接口供电，通电时，电源接口旁白灯亮起。

- 4模拟量输入通道L1~L3, R1~L3:3pin SH1.0母座。可连接单/双通道摇杆模块、船型开关模块等。
- 开关输入通道K1~K4:2pinSH1.0母座。可连接开关模块,按键模块等。
- XH2.54电源接口:2pin XH2.54母座。可连接4.5V~12.6V锂电或干电池盒子。

输入电压：4.5V-12.6V  
工作电流：65mA  
通道数：6x模拟量通道（SH1.0 3P）、4x数字量通道（SH1.0 2P）

### 接收底板-XA004

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-10.png)  
遥控器接收板的左右分别有1个直流电机接口、1个LED灯接口,中央有4个舵机接口。可以通过XH2.54电源接口供电。同电池电源接口旁白灯亮起。

- 直流电机接口M1、M2:2pinSH1.0母座。可以连接直流有刷电机,支持电机正反转和PWM调速。
- 灯珠转接板接口D1、D2:3pin SH1.0母座。可以连接灯珠转接板或其他使用WS2812协议的灯带。
- 舵机接口S1~S4:3pin插针。可以连接常见的5V舵机。
- 核心板插槽:双排灰色插槽,用于连接核心板。
- XH2.54电源接口:2pin XH2.54母座。可连接7.4V~12.6V锂电或干电池盒。  
  输入电压：7.4V-12.6V  
  最大工作电流：3A  
  通道数：2x直流电机口（SH1.0 2P）、4x舵机接口、2xLED接口（SH1.0 3P）

## 输入模块

输入模块负责获取用户的操作或环境中的变化，并将其转化为可被系统识别的信号。例如：摇杆、按钮、触摸传感器等模块。当你推动摇杆或按下按钮时，系统就能通过这些模块接收到相应的控制指令。

### 单通道摇杆-XA009

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-9.png)  
单通道摇杆模块是一个单通道模拟量输入模组,无操作时会自动回中。  
单通道摇杆相较双通道摇杆只能在一个方向上运动并输出一路格模拟量信号,适合在各种需要控制运动速度或控制时常归中的位置状态的场景作为控制杆,尤其是当这些运动的控制独立时。例如在车辆类模型中,以一个单通道摇杆模组控制运动速度,另一个单通道摇杆模组控制转向轮角度;或者是在塔吊杯模型上,用单通道摇杆模组控制吊钩升降;又或者在履带车辆模型上,用两个单通道瑶杆模组单独控制两侧履带的速度。

#### 硬件连接

将单通道摇杆模块端子连接一条SH1.0-3pin连接线,并将连接线另一端连接至遥控发射板两侧的模拟量通道输入口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-12.png)

#### 软件配置

行为控制会使得对应设备随通道的模拟量值对应输出,常用于用摇杆控制电机的速度与舵机的角度等情况,电机设备旁的查看硬件连接可以查看接接收机的硬件连接状态。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-1.png)  
事件控制将每个通道的大于,等于和小于中值分成了三种情况,对应控制某个设备的状态,可以用于将例如转向灯与转向舵的情况绑定等情况。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-2.png)  
当发现摇杆回中后仍然飘移时,使用参数设置,可以进行中点0校准并调整列死区大小。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list//image3.png)  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list//image6.png)

### 双通道摇杆-XA011

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-8.png)  
双通道摇杆模块是一个双通道模拟量输入模组,无操作时会自自动回中。  
双通道摇杆适合在各种需要控制运动速度与方向的场景作为控制杆,尤其是当这些运动彼此关联时。例如在车辆类模型中,以一个轴控制移动速度,另一个轴控制转向;或者是在塔吊模型上,以一个轴控制旋转,另一个轴控制距离。

#### 硬件连接

将双通道摇杆模块两端子各连一条SH1.0-3pin连接线,并将连接线另一端连接至遥控发射板两侧的模拟量通道输入口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-7.png)

#### 软件配置

行为控制会使得对应设备随通道的模拟量值对应输出,常用于用摇杆控制电机的速度与舵机的角度等情况,电机设备旁的查看硬件连接可以查看接接收机的硬件连接状态  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-11.png)  
事件控制将每个通道的大于,等于和小于中值分成了三种情况,对应控制某个设备的状态,可以用于将例如转向灯与转向舵的情况绑定等情况。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-4.png)  
当发现摇杆飘移时,使用参数设置,可以进行中点0校准并调整列死区大小。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list//image5.png)  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list//image26.png)

### 三档开关-XA010

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-27.png)  
三档开关模块是一个单通道模拟量输入模组,有三段位置。  
三档开关可以固定在左中右三个状态上,因此非常适合在各种需要切换灯光,变形等状态的场景作为状态开关。例如在车辆模型中用于切换车灯的开启关闭状态;或者在遥控器一对多控制时用于切换控制的车辆。

#### 硬件连接

将三档开关模块端子连接一条SH1.0-3pin连接线,并将连接线我另一端连接至遥控发射板两侧的模拟量通道输入口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-23.png)

#### 软件配置

在三档开关模块配置界面，可以设置开关状态对应的设备的状态，例如灯光的光效，电机的转速，舵机的位置等。适用于切换灯光状态，控制模型变形等场景。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-28.png)

### 开关板-XA007

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-29.png)  
开关板是一个两位开关，常用于在不拆下电池的情况下控制电源的通断。  
开关板上有两个2pin XH2.54接口，一般串联于电源如锂电池，与拓展板如遥控发射与接收板间。通过开关板可以在不直接取出电池的情况下切断电源，避免持续的待机状态造成电池电量损耗。

#### 硬件连接

将开关板一侧端口与电源相连，另一端与XH2.54 2pin连接线相连；连接线另一端连接至扩展板上XH2.54 电源连接口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-20.png)

### 瞬时按钮-XA008

瞬时按钮模块是一个二进制输入模块，可以识别短按，长按，按下与抬起等多种动作。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-21.png)  
瞬时按钮模块相较于三段开关，只有按下和弹起两个状态，且总会回到弹起。通过瞬时按钮模块可以实现在多种模式间按指定顺序切换，实时触发和停止一些动作等。例如在具有发射机构的模型上触发发射，或者是在使用彩灯的模型上切换灯光的模式和颜色。

#### 硬件连接

将瞬时模块端子连接SH1.0 2pin连接线，连接线另一端接遥控发射板下方的数字信号输入口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-17.png)

#### 软件配置

在按键模块的配置界面，可以通过按键的短按，长按，按下和抬起动作控制对应元器件的状态值切换  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-16.png)  
点击值，可以在其中添加多个状态值，动作后会按顺序在状态间切换  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-25.png)

## 输出模块

输出模块则根据输入信号执行具体动作，用以表现模型的响应能力。例如：电机、舵机、LED 灯等模块。当系统接收到来自输入模块的信号时，输出模块会做出如转动、发光等反应，从而完成整个互动过程。

### LED灯珠转接板-XA006

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-22.png)  
灯珠转接板用于连接支持WS2812协议的灯珠和扩展板上的LED接口，从而实现对更多RGBW灯珠的独立控制。适用于各种需要使用多个LED灯的模型。

#### 硬件连接

将卧式的3pin SH1.0接口连接3pin SH1.0连接线，连接线另一端连接遥控接收板两侧的LED灯接口。将WS2812灯珠的连接线接至4个立式的端口。

#### 软件配置

配置内，点击激活的LED下面的1234选择该灯效控制的灯珠，模式选择灯效闪烁或常亮，颜色选择灯的颜色，重复时间和时间设置闪烁的频率。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-18.png)

### WS2812 LED灯珠-KB003

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-24.png)  
WS2812灯珠是一个带有连接线的，支持WS2812协议的RGBW灯珠，可以发出多种颜色的光  
配合灯珠转接板使用，多个WS2812灯珠可以提供各类视觉效果，适用于各种需要灯光的模型, 例如在车灯模型上作为车灯等。

#### 硬件连接

将WS2812灯珠的连接线插头插入灯珠转接板的立式端子中。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-15.png)

#### 软件配置

需搭配灯珠转接板使用，详见上文灯珠转接板软件配置部分。

### 030直流有刷电机-LA024

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-30.png)  
030有刷电机是一种小尺寸有刷电机。  
030有刷电机在尺寸和功率中保持了均衡，并且可以搭配不同减速比的减速齿轮包组成各种转速的单/双轴减速电机，适用于各类有持续运动需求，但不需要非常精确的速度的模型。例如车辆模型的底盘驱动电机，转台的驱动电机等。

#### 硬件连接

将030有刷电机的接头连接至遥控接收板两侧的电机输出口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-31.png)

#### 软件配置

在修改界面可以调整电机正反转的最高速度和偏置。偏置为摇杆归中时，电机的默认速度。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-32.png)  
手感优化允许将摇杆值与电机速度的关系变成非一次线性的，从而让低速控制更准确，高速响应更快。你可以在编辑中具体调整手感优化的作用。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-41.png)

### N20直流减速电机-LA002

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-33.png)  
N20有刷电机是一种微型尺寸有刷电机，目前的三种型号为：

- 150RPM - LA002
- 400RPM - LA003
- 1000RPM - LA004

N20有刷电机的尺寸比030有刷电机更小，有多种输出轴和转速可选。适用于各类有持续运动需求，尺寸较小，不需要很大扭矩，或者需要关节自锁（选用侧出轴N20电机）的模型上。例如车辆模型的底盘驱动电机，机械臂与转台的关节驱动电机等。

#### 硬件连接

将N20有刷电机的端子连接2pin SH1.0连接线一端，连接线另一端连至遥控接收板两侧的电机输出口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-34.png)

#### 软件配置

直流有刷电机的连接方式都相同，详情请参考上文030电机软件配置部分。

### 9g速度舵机-PG002

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-35.png)  
速度舵机是一种有速度闭环的电机。  
相对其他有刷电机，9g速度舵机的扭矩小，但可以保持一个恒定的运动速度，且运动较安静，常用于驱动模型上的一些轻小装饰件的运动。

#### 硬件连接

将9g速度舵机的接头插入遥控接收板的舵机接口。  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-38.png)

#### 软件配置

在设置界面调整速度舵机的最高和最低速度  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-36.png)

### 9g180°角度舵机-PG001

![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-37.png)  
180°角度舵机是一种具有位置闭环的电机。  
9g180°角度舵机在外观上看起来和速度舵机一样，但不同的在于180°角度舵机将会稳定在指定的角度而非速度。这种特性使得舵机非常适合用作转向机构，变形机构。例如在车辆模型中用于控制转向架，在机械臂模型中用于控制关节角度。

#### 硬件连接

将9g180°角度舵机的接头插入遥控接收板的舵机接口

#### 软件配置

在配置界面点击舵机接口+，添加角度舵机  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-39.png)  
在设置界面调整角度舵机的转动速度与最大最小角度  
![filename-5.png](https://wiki.bambulab.com/makerworld/cyberbrick/component-list/filename-40.png)
