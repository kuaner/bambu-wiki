---
path: zh/software/bambu-studio/release/release-note-1-7
title: "Bambu Studio 1.7 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-07-28T03:33:34.868Z
updated: 2024-05-28T10:52:00.995Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7
---

# Summary

本次发布根据用户反馈添加了一些功能、改进和修复。  
**该版本融入了 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) 和社区的许多功能。我们尝试尽可能多地注释每个项目。如有遗漏，欢迎大家指出。再次感谢社区做出的杰出贡献。**

## 为 BambuLab 打印机添加流量动态校准和流量校准

![](https://github.com/bambulab/BambuStudio/assets/112537880/19179940-47aa-404b-b5f3-1aabe9b649d9)
![](https://github.com/bambulab/BambuStudio/assets/112537880/ba825d9e-2223-4ba3-9c17-1c3350418540)

通常这些校准是不必要的，使用预先校准和微调的默认参数在大多数情况下正常打印将获得良好的结果。关于绝对流量校准步骤 [wiki](../../../../en/software/bambu-studio/calibration_flow_rate.md)， 更多信息可以参考 [wiki](../../../../en/knowledge-sharing/flowrate-calibration-by-microlidar.md)。

## 支持打印时跳过某些模型

从该版本生成的 3mf/.gcode.3mf 文件可用于打印机端可选择跳过的部件。需要单一材料打印，并且每版少于 64 个物体。请将打印机固件也更新至V01.06。  
![](https://github.com/bambulab/BambuStudio/assets/112537880/5b022b1b-3a61-4988-8e91-1035601f11bc) ![](https://github.com/bambulab/BambuStudio/assets/112537880/c05d14bd-4e2e-4325-ad60-f7c1b7ef60bf)

## 设备模型文件浏览和打印

通过 Studio 管理打印机上的模型文件并启动打印。请将打印机固件也更新至X1 V01.06。  
![](https://github.com/bambulab/BambuStudio/assets/112537880/6c8a3a8e-c593-442f-ae7b-1c6e8c6aac40)

<https://www.youtube.com/watch?v=BV1Vx4y1X777&src=bilibili>

## 3D布尔运算

Bambu Studio 现在支持布尔运算。使用最新的3D布尔运算工具，您可以在两个零件之间进行并集、差集（减法）或交集。然而，请注意，网格布尔本身是一个复杂的话题，即使对于专业的 CAD 软件也是如此。它可能会在某些网格上失败，包括内置的“Cone”模型。我们正在努力增强这些业务的稳定性。 该功能基于 [mcut](https://github.com/cutdigital/mcut)，感谢 mcut 的所有贡献者。  
![](https://github.com/bambulab/BambuStudio/assets/112537880/4ed3afa7-26da-49f2-b21d-4668b7c52aec)

## 支持更多第三方打印机配置文件

支持更多第三方打印机配置文件，包括Anker、Anycubic、Creality、Elegoo、Prusa、Qidi、Voxelab；还支持第三方打印机的预览/校准和大量切片设置。 该函数是从 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) 移植的，感谢 @SoftFever以及社区的所有贡献者。  
![](https://github.com/bambulab/BambuStudio/assets/112537880/bb32a446-2794-475b-8054-899ab096ef30)

<https://www.youtube.com/watch?v=BV1Gu4y127p2&src=bilibili>

## 改进

1. P1P 实时直播增强  
   此版本的 Bambu Studio 支持我们之前在 P1P 中引入的新固件功能，现在支持从本地网络外部进行实时查看。这意味着您现在可以从世界任何地方直接从 Bambu Studio 访问相机。  
   请将打印机固件也更新至V01.04。
2. LAN only 描述实时直播增强 (X1)  
   我们收到了客户关于在仅 LAN 模式下提供实时查看的多个请求。X1 系列的最新固件与最新版本的 Bambu Studio 相结合，支持从本地打印机访问视频，无需连接互联网。  
   请注意，当打印机设置为仅 LAN 模式时，您将无法访问 Bambu Handy 的实时查看流。  
   请将打印机固件也更新至V01.06。
3. 支持 Bambu Lab P1S.  
   ![](https://github.com/bambulab/BambuStudio/assets/112537880/492d0e13-b9c9-4bac-8820-b0db3d690e08)
4. 支持 Linux 系统的深色模式  
   我们知道很多客户喜欢深色模式。为了确保 Bambu Studio 在所有平台上具有相同的功能，该版本引入了对 Linux 系统的深色模式的支持。
5. 添加开发者模式以查看和编辑更多参数。很多参数是从 OrcaSlicer 移植的，或者是从 PrusaSlicer 移植的。谢谢！  
   ![](https://github.com/bambulab/BambuStudio/assets/112537880/b5e9f36d-5de7-49f0-9347-1c5038f2f9b6)
6. 支持装配视图选项卡下的着色  
   ![](https://github.com/bambulab/BambuStudio/assets/112537880/045e8cba-bdb7-4006-b53e-7d5cb91e7f7b)
7. 支持从“设备”或“发送打印”显示打印机的“耗材自动补充信息”。  
   ![](https://github.com/bambulab/BambuStudio/assets/112537880/244787cb-336c-45f5-b69e-2f2bd68f72ee)
8. 支持 Bambu 透明 Filament  
   可以在 3D 视图、切片预览中查看透明材料  
   ![](https://github.com/bambulab/BambuStudio/assets/112537880/92759484-36b5-47d7-a266-4b66dfbf40b3)
9. 改进了着色工具中的旋转角度体验。  
   选择对象并输入着色工具，然后旋转相机。如果相机水平旋转，则模型也会水平旋转；如果相机垂直旋转，模型也会垂直旋转。  
   ![](https://github.com/bambulab/BambuStudio/assets/112537880/fe4a8580-dd11-464a-97ca-9c4ca4d15cd2)
10. 优化多色打印工件的行进路径，减少打印时间。

![](https://github.com/bambulab/BambuStudio/assets/112537880/342a38e5-8f88-4827-b572-18f3dc0cb2e3) ![](https://github.com/bambulab/BambuStudio/assets/112537880/301c35be-affa-4652-954d-6bf5bff8d54e)

11. 优化顶一墙功能性能，减少切片时间
12. 添加同心熨烫图案
13. 添加设置以更改内部实心填充图案
14. 为第一层仅添加一个墙功能  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/3155fcdd-ef24-4a95-b6bf-2e23c1f49493)
15. 将打印机预设中的默认 z 跳类型从螺旋切换为自动提升以节省打印时间  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/bcc9ac71-acc5-4848-809a-4835db9f2e4c) ![](https://github.com/bambulab/BambuStudio/assets/112537880/d9649c4a-546e-4f29-b7ce-e799f0a2b3ba)
16. 将默认墙体生成器更改为arachne，并将默认墙体循环更改为3。  
    注意：只有顶面上的一堵墙与arachne有冲突，因此启用arachne时禁用。未来将会修复。
17. 在“3D 准备选项卡”中显示悬垂区域  
    支持通过菜单->视图->显示悬垂直接在“3D 准备选项卡”中显示模型的悬垂区域  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/13ef4820-4a9a-4240-bba5-d3265971dcf0)
18. 支持命名打印面板  
    您可以通过单击面板顶部的“编辑板名称”按钮来自定义板的名称，或者右键单击所选板并选择“编辑面板名称”，或者通过单击左侧板的右键菜单，选择“编辑面板名称”。  
    该函数是从 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) 移植的，感谢@SoftFever用于初步实施。  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/393ffcfe-7241-411f-82bb-7f5b9e7464c4)
19. 选择多个对象时显示选择的部分数量
20. 通过交替层间网格填充路径的方向来增强打印稳定性。  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/4e4c94e5-d844-472a-a974-1b82afe731c4)

<https://www.youtube.com/watch?v=BV17V4y1i7dh&src=bilibili>

21. 重新添加“用实例填充床”功能
22. 通过右键菜单添加3个基准模型。感谢 @[thrutheframe](https://www.printables.com/model/222285-bambu-xyz-cube), @ [Creative Tools](https://www.3dbenchy.com/about/), @[kickstarter-autodesk-3d](https://github.com/kickstarter/kickstarter-autodesk-3d).  
    添加这些基准和功能的想法来自 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)。谢谢！  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/00294f20-53ce-4d9f-8c27-6a8ff7480d21)
23. 右键菜单中的3D布尔运算  
    感谢 @[PrusaSlicer](https://github.com/prusa3d/PrusaSlicer/releases/tag/version_2.6.0-alpha6) 开发了“导出到STL 以减去负网格”功能。我们进一步提高了其稳定性和功能。现在，您可以通过右键单击零件并从菜单中选择“网格布尔”来执行此操作。可以通过与负零件的相交来雕刻出零件的一段。另一方面，多个正部分可以合并为单个部分。此外，我们禁用了“导出为STL”中的隐式布尔运算以避免混淆。“导出为 STL”现在按原样导出模型。  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/c0674b31-91f9-46da-b180-46b44e0f4b79)
24. 允许禁用“小悬垂去除”
25. 允许设置树支撑边缘宽度  
    以前，树支撑边缘宽度是自动计算的，无法手动设置。现在我们打开设置，值 0 表示自动计算的边缘宽度。
26. 优化了保存3MF时的文件大小。  
    当模型对象和零件有多个副本时，3MF 文件中仅保存一组模型数据。
27. 显示各种网络错误信息  
    绑定打印机/发送打印失败时会显示更详细的错误描述  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/29aafa1c-30fe-4e6f-9497-37e207839ceb)
28. 更改校准线的样式。直接在准备页面上显示校准图案的想法来自 [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)。谢谢！  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/d98a1369-e83d-4b47-94a8-38b153810e4d)  
    ![](https://github.com/bambulab/BambuStudio/assets/112537880/b46e5820-1ec7-4e9a-819f-57d2c5e183e6)
