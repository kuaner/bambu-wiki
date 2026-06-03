---
path: zh/software/bambu-studio/release/release-note-1-10-0
title: "Bambu Studio 1.10.0 Public Release 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2024-10-15T09:32:47.776Z
updated: 2024-11-12T09:29:35.628Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-10-0
---

## 新功能

1. **冲刷优化**：在不产生混色的前提下，部分颜色的官方耗材多色打印冲刷平均节省20.9%。

- 更多材料启用长回抽：X/P/A系列的PLA Basic、PLA Matte、PLA Galaxy、PLA Marble、PLA Glow、PLA-CF、PETG HF、PETG Translucent、PETG-CF、ABS、ABS-GF、ASA、Support for PLA/PETG、Support for ABS支持长回抽。
- 针对12种颜色冲刷优化：目前支持Bambu PLA Basic的Red/Black/Brown/Gray/Yellow/Bambu Green/Blue Gray/Light Gray/Dark Gray/Purple/Blue/Orange共12种颜色耗材之间的换料节省，使用这些耗材将能显著减少多色打印的浪费。(注意：自动冲刷优化目前只针对Bambulab的官方耗材，第三方耗材品牌众多，配方差异无法保证换色效果的一致性，如使用第三方耗材请自行调整)。  
  感谢[@SnK3DD](https://makerworld.com/zh/@SnK3DD)的可爱南瓜模型。  
  ![flush1.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/flush1.png)  
  ![flush2.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/flush2.png)

2. **Brim Ear工具**：新版本可以自动或手动在物体的特定边缘添加“鼠耳状的”Brim了，自动模式对应参数功能如下：

- Head Diameter：Brim Ear直径大小。
- Max Angle：自动模式下最大生成Brim Ear的角度，高于该阈值的边缘不会生成Brim Ear。
- Detect Radius：自动模式下检测生成的最小半径。  
  也可以使用绘制方式进行Brim Ear的添加、删除。更多详情参见[Wiki](../brim-ears.md)。  
  (<https://github.com/bambulab/BambuStudio/issues/1281> ,<https://github.com/bambulab/BambuStudio/issues/3618> ,<https://github.com/bambulab/BambuStudio/issues/3290> ,<https://github.com/bambulab/BambuStudio/issues/2002>)  
  ![brimear1.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/brimear1.gif)  
  注意，如果需要使用Brim Ear工具，需要将Brim Type先设置为绘制模式，切片时才能生效。  
  ![brimear2_2.jpg](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/brimear2_2.jpg)

3. **多种材料Scarf Seam默认开启**：Bambu PLA Basic/Matte/Silk/Galaxy/Dynamic/Glow/Marble/Sparkle and PLA-CF将会默认启用Scarf Seam功能，Scraf Seam常用参数被调整至耗材丝设置下，方便对不同耗材做差异化的参数配置：  
   ![scarfseam.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/scarfseam.png)
4. **首页底部新增打印历史**：现在可以方便的追溯过往的打印记录了。  
   ![print_history.jpg](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_release/print_history.jpg)
5. **子网绑定支持**：支持在不同子网内直接输入打印机IP地址和Access Code进行绑定。（配合P系列固件版本：01.07.00.00，配合A系列固件版本：01.04.00.00，配合X系列固件：下一个release版本）  
   (<https://github.com/bambulab/BambuStudio/issues/702> ,<https://github.com/bambulab/BambuStudio/issues/4202> ,<https://github.com/bambulab/BambuStudio/issues/4878> )  
   ![subnet.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/subnet.png)
6. **打印中允许编辑耗材信息**：P系列/A系列打印机支持在打印过程中编辑耗材丝信息(不包含正在被使用的耗材丝或与当前使用的耗材丝存在自动续料关系的耗材丝)，包含外挂料槽和AMS槽位。在打印过程中，用户可以在耗材耗尽之前放入新的料卷，并设置其信息，让新料卷自动续接当前正在使用的料卷(配合P系列固件版本：01.07.00.00，A系列固件版本：01.04.00.00)。  
   ![20241011121840_rec_.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/20241011121840_rec_.gif)
7. **A系列机型支持在校准页触发自动标定**。(配合A系列固件版本：01.04.00.00)  
   ![changhuichou.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/changhuichou.png)
8. **耗材丝缩放补偿设置**：在耗材丝设置中新增了缩放补偿选项，用于冷却后材料收缩的百分比补偿（例如：X方向上为100mm的方块，打印后X轴实际测量值为94mm而不是100mm，则收缩百分比为94%）。此功能将对模型 XY 平面的尺寸进行缩放补偿，而 Z 方向尺寸保持不变。  
   注意：若将补偿值调整为小于 100%，请确保对象间留有足够空间以避免碰撞。  
   (<https://github.com/bambulab/BambuStudio/issues/350>, <https://github.com/bambulab/BambuStudio/issues/2769>)  
   ![shrinkage.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_release/shrinkage.png)
9. **首页新增MakerWorld搜索框**.  
   ![searchbar.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_release/searchbar.png)

## 改进

1. **改进3mf多机型适用性**：当大热床向小热床(或相反)切换时会自动摆盘，并移动擦料塔位置保证其不会与零件碰撞，方便用户使用A1 mini机器打印X或P系列机器的3mf项目文件(model from [@linus3d](https://makerworld.com/zh/@linus3d))  
   ![bigbedtosmall.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/bigbedtosmall.gif)
2. **料塔防剐蹭优化**：  
   (1)当换料后，刚开始在料塔上进行打印时，喷嘴腔压未完全稳定，导致刚开始打印的GCode存在挤出不足的问题，从而导致开始打印的位置存在瑕疵。料塔换料后每层的起始位置都在同一个位置，导致瑕疵不断累积，从而增加了剐蹭的风险。本次优化，将换料后，刚开始打印外墙的位置分散到4个角，避免瑕疵的累积，从而降低剐蹭风险。  
   (2)将料塔的外墙和内部填充的铆接长度降低到0mm，当先打印填充后打印外墙时，可以降低外墙打印过程中剐蹭到已打印的填充走线。  
   ![liaota.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/liaota.png)
3. **显示打印结束的时间**：该时间为预估仅供参考，特定场景下可能存在较大的误差。  
   (<https://github.com/bambulab/BambuStudio/issues/3923> ,<https://github.com/bambulab/BambuStudio/issues/4748> ,<https://github.com/bambulab/BambuStudio/issues/4428> ,<https://github.com/bambulab/BambuStudio/issues/3302> ,<https://github.com/bambulab/BambuStudio/issues/2517>)  
   ![resttime.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/resttime.png)
4. **拆分到对象/零件保持涂色信息**：不用再担心右键拆分STL会丢失涂色信息了。  
   ![spiltobjkeepcolor.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/spiltobjkeepcolor.gif)
5. **熨烫inset功能**：可以通过该参数控制不熨烫外墙区域，避免熨烫多料造成边缘不均。  
   (<https://github.com/bambulab/BambuStudio/issues/2872> )  
   ![ironing_inset.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/ironing_inset.png)  
   ![inroning_inset2.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/inroning_inset2.png)
6. **支持竖直面涂抹生成支撑**：对于瘦高零件垂直面涂抹生成支撑能够降低打印中倒塌的可能性。  
   ![wall_support.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/wall_support.png)
7. **预设包更新提示强化**：预设更新时会有类似版本更新时的自动弹框，我们同时提供了手动检查最新预设包入口。  
   ![check_for_update.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/check_for_update.png)
8. **Boolean 工具选中交互改进**：现在可以从对象列表选中需要布尔运算的对象。
9. **第三方模型添加泪滴状圆柱体**：可以用该模型作为负零件制作适合3D打印的水平孔，感谢[@Ro3Deee](https://www.printables.com/@Ro3Deee)提供的模型。  
   (<https://github.com/bambulab/BambuStudio/issues/4023>)  
   ![new_third-party_model.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/new_third-party_model.png)
10. **SVG贴图功能交互升级**：感谢[@Jony01](https://github.com/Jony01)和[@Noisyfox](https://github.com/Noisyfox)的贡献。  
    ![svg_update.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/svg_update.png)
11. **支持创建带有特定区域徽标的热床**：感谢[@emberprototypes](https://github.com/emberprototypes)提供的范例文件。  
    (<https://github.com/bambulab/BambuStudio/issues/3634>)  
    ![plate_svg_logo_support.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/plate_svg_logo_support.gif)
12. **增加应用可变层高的零件图标**。  
    ![variable_layer_heigth_icon.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/variable_layer_heigth_icon.png)
13. **冷却参数拆解**：增加一个参数，可以控制悬垂的走线是否参与冷却降速。(model from [@bubujiaoqv](https://makerworld.com/zh/@bubujiaoqv))  
    (<https://github.com/bambulab/BambuStudio/issues/3816>)  
    ![canshujieou.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/canshujieou.png)
14. **增加导入step时mesh精度选项**：现在支持通过修改线偏移值、角偏移值，来设置想要的step导入精度。  
    (<https://github.com/bambulab/BambuStudio/issues/3437>)  
    ![step_input_presicision_(2).png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_release/step_input_presicision_(2).png)
15. **移动、旋转功能坐标系优化**：现在可以使用World coordinates/Object coordinates/Part coordinates来自由的对组合体中的零件进行平移及旋转。感谢Prusa3D和[@enricoturri1966](https://github.com/enricoturri1966)。  
    (<https://github.com/bambulab/BambuStudio/issues/4024> ,<https://github.com/bambulab/BambuStudio/issues/4088> ,<https://github.com/bambulab/BambuStudio/issues/4868>)  
    ![corrdiante_add_local.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/corrdiante_add_local.gif)
16. **设备回中增加二次确认**:避免误触。  
    ![homing.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/homing.png)
17. **新增一款打印板**：新增Bambu Plate Cool SuperTack，此打印板**仅支持**以下材料：PLA、PETG、PET、Support for PLA/PETG、PVA 和 PLA Aero。请注意，Support for PLA/PETG**不适用于首层打印**。
18. **停止打印按钮的优化**：避免机箱中有打印件时误触。  
    (<https://github.com/bambulab/BambuStudio/issues/3867>)
19. **新导入零件初始化位置更改**：避免某些零件导入后与已有零件过近不便操作的情况。
20. **增加第三方机型的预设**:新增第三方机型见下，感谢[@Geeetech3D](https://github.com/Geeetech3D)和OrcaSlicer.
    1. K1(0.6mm/0.8mm nozzle)
    2. K1C(0.4mm/0.6mm/0.8mm nozzle)
    3. K1Max(0.6mm/0.8mm nozzle)
    4. Ender V3(0.4mm/0.6mm nozzle)
    5. Ender V3Plus(0.4mm/0.6mm nozzle)
    6. Ender KE(0.4mm nozzle)
    7. Anycubic korbra plus
    8. Elegoo Neptune 4
    9. Eleego Neptune 4 Max
    10. Elegoo Neptune 4 plus
    11. Elegoo Neptune 4 pro
    12. Geeetech
21. **更新韩语翻译**：感谢[@bluesoul33](https://github.com/bluesoul33)的奉献。
22. **更新葡萄牙语翻译**。
23. **优化了Device界面下的内存消耗，大幅减少了新增的Page Faults。**  
    (<https://github.com/bambulab/BambuStudio/issues/3702>)
24. **优化文字工具坐标系**：修复零件缩放、旋转或镜像后导致贴文字位置异常。
25. **Preview模式下mesh透明壳体显示**：感谢Prusa3D。  
    ![touming_mesh.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/touming_mesh.png)  
    ![touming_mesh2.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/touming_mesh2.png)
26. **Role-based wipe speed参数添加**：我们添加了该选项来保证擦嘴将会根据当前挤出的走线类型决定其速度大小，例如外墙挤出后有擦嘴行为，那么擦嘴行为的速度将会使用外墙挤出速度。感谢OrcaSlicer。  
    ![role-based_wipe_speed.jpg](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_release/role-based_wipe_speed.jpg)
27. **调整MakerWorld上传按钮的位置**：避免原先使用时可能产生的歧义，用户误以为上传到打印机。  
    ![move_upload_makeworld_icon.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/move_upload_makeworld_icon.png)
28. **平移、旋转功能下抓手大小可调。**  
    (<https://github.com/bambulab/BambuStudio/issues/3753>)  
    ![gizmo_size.gif](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/gizmo_size.gif)
29. **Beta版本支持自动推送**：勾选“Preference-General Settings-Support beta version update”，当有新Beta版本时也能第一时间收到弹窗提示。  
    ![support_beta_push.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/support_beta_push.png)
30. **网络状态提示**：云服务器无法连接时增加弹窗提醒。  
    ![network_pop_up.jpg](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_beta/network_pop_up.jpg)
31. 如果该材料的PA profile中存在与材料名称相同的选项，在您切换材料时候能够为您自动匹配名称相同的PA值。  
    ![filaments_pa.png](https://wiki.bambulab.com/studio_releasenote/1_10_0_public_release/filaments_pa.png)
32. 一些编译问题的改进，感谢[@hadess](https://github.com/hadess)、[@FFY00](https://github.com/FFY00)和[@dankamongmen](https://github.com/dankamongmen).
33. 感谢[@fatih5228](https://github.com/fatih5228)贡献的土耳其语翻译更新。
34. 感谢[@HYzd766](https://github.com/HYzd766)贡献的QiDi新机器配置。
35. 感谢[@iZonex](https://github.com/iZonex)贡献的乌克兰语翻译更新。

## Bugs 修复

1. 修复了打印概览中的格式错误和支撑消耗统计错误。  
   (<https://github.com/bambulab/BambuStudio/issues/4864> ,<https://github.com/bambulab/BambuStudio/issues/4873> ,<https://github.com/bambulab/BambuStudio/issues/4879> ,<https://github.com/bambulab/BambuStudio/issues/4906> ,<https://github.com/bambulab/BambuStudio/issues/4911> ,<https://github.com/bambulab/BambuStudio/issues/4922> ,<https://github.com/bambulab/BambuStudio/issues/4925> ,<https://github.com/bambulab/BambuStudio/issues/4946> ,<https://github.com/bambulab/BambuStudio/issues/4976>)
2. 修复了部分模型顶部切片颜色错误的问题。  
   (<https://github.com/bambulab/BambuStudio/issues/4870>)
3. 修复涂色模块界面与物体重叠的选中bug。  
   (<https://github.com/bambulab/BambuStudio/issues/4871>)
4. 修复Z轴缩放错误。  
   (<https://github.com/bambulab/BambuStudio/issues/4747>)
5. 修复部分切片的飞线错误。  
   (<https://github.com/bambulab/BambuStudio/issues/4876> ,  
   <https://github.com/bambulab/BambuStudio/issues/4962> ,  
   <https://github.com/bambulab/BambuStudio/issues/4742> ,  
   <https://github.com/bambulab/BambuStudio/issues/4056> ,  
   <https://github.com/bambulab/BambuStudio/issues/2484>)
6. 修复部分切片的问题崩溃。  
   (<https://github.com/bambulab/BambuStudio/issues/4898>)
7. 修复Fuzzy Skin的产生竖向规律性条纹的问题。  
   (<https://github.com/bambulab/BambuStudio/issues/4746> ,<https://github.com/bambulab/BambuStudio/issues/4825>)
8. 修复Support for ABS识别错误的问题。  
   (<https://github.com/bambulab/BambuStudio/issues/4900>)
9. 将“Initial layer density”参数位置从“Raft”调整到“Advance”选项卡下。  
   (<https://github.com/bambulab/BambuStudio/issues/4773>)
10. 修复了构建板纹理图像错误的问题。  
    (<https://github.com/bambulab/BambuStudio/issues/5029>)
11. 修复了特殊多色模型切片crash 的问题。  
    (<https://github.com/bambulab/BambuStudio/issues/5037>)
12. 修复了打印机跳过多色打印对象时换色行为不正确的问题。  
    (<https://github.com/bambulab/BambuStudio/issues/4940> ,<https://github.com/bambulab/BambuStudio/issues/4501>)
13. 修复了复制对象时未复制对应的Brim Ears的错误。  
    (<https://github.com/bambulab/BambuStudio/issues/5048>)
14. 增加变量以解决Linux Flatpak环境下的编译错误。  
    (<https://github.com/bambulab/BambuStudio/issues/5008>)
15. 修复了Linux系统下启动时的复选框显示问题。  
    (<https://github.com/bambulab/BambuStudio/issues/2711>)
16. 修复了打印时间未显示的错误。  
    (<https://github.com/bambulab/BambuStudio/issues/5028>)
17. 修复了发起打印后，设备页目标温度未正确显示的错误。  
    (<https://github.com/bambulab/BambuStudio/issues/5018>)
18. 修复了特定角度下自动朝向功能的错误问题。  
    (<https://github.com/bambulab/BambuStudio/issues/5092>)
19. 修复了逐件打印中可能出现的碰撞问题。  
    (<https://github.com/bambulab/BambuStudio/issues/4804>)
20. 修复了跳转到层失败的问题。  
    (<https://github.com/bambulab/BambuStudio/issues/4957>  
    ,<https://github.com/bambulab/BambuStudio/issues/5170>)
21. 修复了跨子网模式连接时的crash问题。  
    (<https://github.com/bambulab/BambuStudio/issues/5135>)
22. 修复了部分情况下AMS无法正确同步的问题。  
    (<https://github.com/bambulab/BambuStudio/issues/5181>  
    ,<https://github.com/bambulab/BambuStudio/issues/4863>  
    ,<https://github.com/bambulab/BambuStudio/issues/4949>)
