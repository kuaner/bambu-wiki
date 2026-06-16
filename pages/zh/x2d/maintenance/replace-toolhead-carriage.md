---
path: zh/x2d/maintenance/replace-toolhead-carriage
title: "更换 X2D 工具头滑车组件"
description: ""
tags: []
created: 2026-05-20T08:32:10.522Z
updated: 2026-05-26T10:35:05.566Z
source: https://wiki.bambulab.com/zh/x2d/maintenance/replace-toolhead-carriage
---

## 工具头滑车

工具头滑车组件主要由滑车前盖和滑车后盖组成，安装在 X 轴组件的石墨铝套上，可以在 XY 皮带的牵引下实现在 X 方向上的移动。

配件包装内包含：  
工具头滑车前盖 \* 1（含辅助热端升级滑块）  
工具头滑车后盖 \* 1  
堵嘴片 \* 1 （备用）  
螺丝 \* 8  
弹簧 \* 4

![fae057.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/fae057.png)

## 适用场景

- 工具头滑车组件损坏 (如螺丝孔滑牙)
- 升降滑块故障

## 所需工具与材料

- 新的工具头滑车组件
- H1.5 内六角扳手
- H2.0 内六角扳手

## 拆卸工具头滑车组件

### 步骤 1. 移除工具头外壳和热端

1. 请参考 [更换 X2D 工具头外壳](replace-toolhead-housing.md) 移除工具头外壳并断开料管；
2. 请参考 [更换 X2D 热端和硅胶套](https://wiki.bambulab.com/zh/X2D/maintenance/replace-hotend-and-silicone-sock)、移除热端硅胶套和热端；

![010_remove_mid_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_toolhead_cover/010_remove_mid_cover.png)

### 步骤 2. 移除皮带固定座

使用 H2.0 内六角扳手拧松（拧松 2 圈即可，不需要完全卸下螺丝）四颗张紧螺丝，放松 XY 皮带。

![tension_screws.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/tension_screws.png)

使用 H2.0 内六角扳手移除 6 颗工具头上皮带固定座的螺丝，将两侧的皮带固定块从工具头上移除。

![belt_screws.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/belt_screws.png)

### 步骤 3. 将工具头滑车从 X 轴上移除

1. 请参考 [更换 X2D 切料拨杆组件](replace-filament-cutter-lever.md) 移除左右两侧的切料拨杆。  
   ![cutter_lever.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/cutter_lever.png)
2. 断开 TH 板上的连接器，用 H1.5 内六角扳手移除4颗螺丝，将 TH 板从工具头上移除。  
   ![th_board.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/th_board.png)  
   ![remove_th_board.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_th_board.png)
3. 使用 H2.0 内六角扳手拆下八颗固定滑车组件的螺丝。  
   ![unlock_8_screws.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/unlock_8_screws.png)
4. 用手握住工具头滑车前盖，防止工具头滑车前壳顶部的四个弹簧掉落，移除工具头滑车后盖。  
   ![remove_the_rear_part.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_the_rear_part.png)

> 如果只是工具头滑车后盖损坏或螺丝孔滑牙，在这里换上新的工具头滑车后盖即可，不需要再进行后面的拆装。

5. 然后将工具头滑车前盖与上光杆分离，避免弹簧脱出，最后将整个滑车前盖组件与 X 轴分离并取下。

![remove_the_front_part.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_the_front_part.png)

### 步骤 4. 分解工具头滑车前盖组件

这里说的分解是指把安装在工具头滑车前盖上的配件从滑车前盖上移除，用于安装到新的工具头滑车前盖上。这个过程步骤比较多，请根据拆解的顺序进行处理，避免不必要的拆除动作。

1. 移除加热组件接口板和挤出接口板

使用 H1.5 内六角扳手移除 2 颗热端加热组件连接器支架固定螺丝，取下支架，断开除工具头前盖连接线缆外的其他线缆；

![disconect_the_connectors.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/disconect_the_connectors.png)  
移除挤出接口板和热端加热组件接口板。  
![remove_connection_boards.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_connection_boards.png)

2. 将挤出机两侧的线缆松出，移除主热端风扇  
   将卡在挤出机左右两侧的线缆松出，分别用 H2.0 和 H1.5 内六角扳手移除主热端风扇上下两侧的螺丝，取下主热端风扇。

![remove_the_left_fan.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_the_left_fan.png)

3. 移除挤出机组件

用 H2.0 内六角扳手移除 3 颗螺丝，将挤出机从工具头滑车前盖上取下，这里不需要撕掉捆绑线缆的胶布。  
![remove_extruder.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_extruder.png)

4. 移除涡流线圈  
   用 H1.5 内六角扳手移除左右涡流线圈上的螺丝，将涡流线圈从滑车前盖上移除。  
   ![coils.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/coils.png)
5. 移除热端加热组件  
   移除辅助热端涡流线圈下的金属支架，用 H2.0 内六角扳手移除热端加热底座的固定螺丝，将两个加热组件从滑车前盖上取下。

![hotend_heating_assy.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/hotend_heating_assy.png)  
6. 移除辅助热端风扇  
用 H1.5 内六角扳手拧松辅助热端风扇的固定螺丝，移除辅助热端风扇，继续用扳手拧下两螺丝螺丝，取下风扇压片。  
![remove_the_right_fan.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_the_right_fan.png)  
7. 移除工具头摄像头  
用大拇指向上扳动工具头摄像头的上盖，使其松脱；  
![open_camera_cover.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/open_camera_cover.png)  
用 H1.5 内六角扳手拧下工具头摄像头的固定螺丝，移除工具头摄像头，在拧螺丝时，注意避让排线。  
![remove_the_camera.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_the_camera.png)  
8. 移除堵嘴组件  
用 H2.0 内六角扳手将固定堵嘴组件的 3 颗螺丝完全拧松，取下堵嘴组件。

![remove_the_flow_blocker_assembly.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_the_flow_blocker_assembly.png)

9. 移除挤出电机  
   用 H2.0 内六角扳手将固定挤出电机的 2 颗螺丝移除，取下挤出电机，并将轴承从滑车前盖上移除。  
   ![remove_extruder_motor.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_extruder_motor.png)

至此，工具头滑车前盖上的配件被全部移除。

## 安装工具头滑车组件

### 步骤 1. 组装工具头滑车前盖组件

1. 安装挤出电机  
   将挤出电机安装到工具头滑车前盖的背面，对齐两个螺丝孔，注意挤出电机的软排给应在右侧，同时将旧滑车前盖上的挤出机齿轮轴承安装到新的滑车前盖上。

![install_extruder_unit.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_extruder_unit.png)

2. 安装堵嘴组件

> 安装提醒：  
> 在安装堵嘴组件时，需要确认升降滑块向下滑到底，喷嘴组件的拨杆向右拨到底，并能清楚地识别出下图黄色箭头所示的位置，这两个位置在安装时，用于确认安装位置正确：左侧的缺口标识要位于右侧两个带凸起的齿轮中间。  
> ![position.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/position.png)

将堵嘴组件安装到工具头滑车前盖上，根据以上的安装提醒，将堵嘴组件安装到位，如果发现 3 颗螺丝对组件安装的位置有影响，可以调整一下螺丝的位置，然后逐个将 3颗螺丝预紧，检查无倾斜等安装不到位的情况后，再将 3 颗螺丝锁紧。  
![install_blocker.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_blocker.png)

3. 安装工具头摄像头  
   将工具头摄像头安装到工具头滑车左侧，注意避让排线，锁入 2 颗螺丝固件工具头摄像头，然后对齐工具头摄像头的上下盖，将上盖安装好。  
   ![install_the_camera.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_the_camera.png)  
   ![close_camera_cover.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/close_camera_cover.png)
4. 安装辅助热端风扇  
   将辅助热端风扇压片安装到工具头滑车前盖上，参考下图确保压片的方向正确，然后锁入 2 颗螺丝，不要锁紧。最后再辅助热端的固定支架安装到压片下方，锁紧 2颗螺丝将风扇压紧。

![install_the_right_fan.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_the_right_fan.png)

5. 安装热端加热组件

将两个加热组件安装到工具头滑车前盖，并分别锁入 3 颗螺丝固定，在辅助热端加热组件上装回辅助热端涡流线圈的金属支架。

![hotend_heating_assy.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/hotend_heating_assy.png)

6. 安装涡流线圈

将两个涡流线圈安装到对应的位置上，分别锁入两颗螺丝进行固定，其中左侧线圈使用螺帽较小的螺丝。  
![coils.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/coils.png)

> 如果在之拆解时，整理线缆的有金属卡扣有脱落，请装回下图所示位置。![clip.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/clip.png)

7. 安装挤出机组件  
   请再次检查，黄色箭头所示位置安装了齿轮组件的轴承，右霍尔检测板组件已滑入挤出机的内部，然后将挤出机组件安装到工具头滑车前盖，注意避让所有的线缆，避免压伤线材，然后紧锁 3 颗固定螺丝。

![install_extruder.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_extruder.png)

8. 安装主热端风扇  
   将主热端风扇安装到左热端加热组件旁边，然后依次锁入大、小银色螺丝各 1 颗，整理好线缆，避免损坏。

![install_the_left_fan.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_the_left_fan.png)

9. 安装加热组件接口板和挤出接口板

将热端加热组件接口板和挤出接口板安装到挤出机上方位置  
![remove_connection_boards.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_connection_boards.png)

将线缆连接到挤出接口板对应的连接器上，并整理好线缆后，连接两个热端加热组件的连接线，然后安装热端加热组件连接器支架，并锁入 2 颗螺丝进行固定。  
![disconect_the_connectors.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/disconect_the_connectors.png)

### 步骤 2. 安装工具头滑车到 X轴

1. 将步骤 1 中组装好的工具头滑车前盖组件安装到 X 轴上，先贴着下方的石墨铝套安装到位，然后再向上旋转滑车前盖与上方的石墨铝套接到一起，避免弹簧脱落。  
   ![mount_the_front_part.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/mount_the_front_part.png)
2. 用手扶着滑车前盖，避让下方的线缆，将滑车后盖安装到 X 轴上，对齐螺丝孔，然后按下图的顺序依次锁入 8 颗螺丝。

![install_the_rear_part.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/install_the_rear_part.png)

3. 检查确认 连接到 TH 板的工具头线缆连接状态正常，然后将 TH 板安装到工具头滑车后盖上，锁入 4 颗螺丝进行固定，连接 TH 板上的线缆。  
   ![remove_th_board.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/remove_th_board.png)  
   ![th_board.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/th_board.png)
4. 参考 [更换 X2D 切料拨杆组件](replace-filament-cutter-lever.md) 安装左右两侧的切料拨杆。  
   ![cutter_lever.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/cutter_lever.png)

### 步骤 3. 安装皮带固定座并张紧皮带

将左右两侧的同步带固定块连接到工具头的两侧，并锁紧螺丝。 为了降低皮带拉力的影响，可以先将两侧的螺丝进行预锁，最后再一起锁紧。  
![belt_screws.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/belt_screws.png)

将工具头沿 X 方向和 Y 方向 各移动 3 次完整的行程，然后锁紧 XY 皮带张紧螺丝。

![tension_screws.png](https://wiki.bambulab.com/x2d/maintenance/toolhead-carriage/tension_screws.png)

### 步骤 4. 安装热端和工具头外壳

1. 请参考 [更换 X2D 热端和硅胶套](https://wiki.bambulab.com/zh/X2D/maintenance/replace-hotend-and-silicone-sock)安装热端硅胶套和热端；
2. 请参考 [更换 X2D 工具头外壳](replace-toolhead-housing.md) 移除工具头外壳并连接料管；

![017_front_cover.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_toolhead_cover/017_front_cover.png)

## 成功验证

接通电源并启动打印机，运行整机校准流程，确认校准能够顺利完成。  
如果出现调平失败的问题，可先参考 [X2D 涡流线圈调整](adjust-the-eddy-sensor.md) 调整涡流线圈后重新执行校准。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
