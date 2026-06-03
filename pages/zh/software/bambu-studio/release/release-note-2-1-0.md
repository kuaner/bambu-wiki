---
path: zh/software/bambu-studio/release/release-note-2-1-0
title: "Bambu Studio 2.1.0 版本说明"
description: ""
tags: ["bambu studio"]
created: 2025-05-29T12:08:40.254Z
updated: 2025-06-04T13:12:42.711Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-1-0
---

### 已知问题

**H2D 自建耗材存在换料冲刷参数错误**：对于在 V2.1.0 之前版本中创建的自建耗材，其换料时冲刷体积流量速度与温度设置可能不正确。请更新预设至**02.01.00.15**版本以规避该问题。我们将在后续版本中修复剩余问题。

## 新功能

新增Locked zag 填充，是一种兼顾外观与强度的填充结构，针对性解决打印软材料时候强度不足的问题。这个纹理由两部分组成：

- Skin（表层）：包裹模型外轮廓，使用 Cross Zag 纹理，确保表面效果与标准 Cross 填充一致，提升外观质量。
- Skeleton（骨架）：内部主体使用 Zigzag 纹理，增强结构强度

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-1.png)

为了解决两个区域的密度参数不同，或是线宽参数不同时，模型的轮廓被切割导致生成的填充中断问题，Locked zag提供了四个参数可以改变选取的密度和线宽时，保证不同区域之间的连接。如下图所示。

|  |  |
| --- | --- |
|  |  |

## 改进

1. 避免跨越外墙功能优化：降低了部分模型表面拉丝的问题。(<https://github.com/bambulab/BambuStudio/issues/6597>)

|  |  |
| --- | --- |
|  |  |

2. Windows平台的设备页新增机器列表的搜索功能：方便多机器用户快速定位到所需设备。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-6.gif)

3. 优化了H2D延时摄影时挤出机的移动到的位置：降低了额外的空驶和切刀顶杆运动的噪声。
4. 优化了Arachne模式下计算效率：使用新悬垂计算方式，显著提升Arachne墙体路径生成速度。(<https://github.com/bambulab/BambuStudio/issues/6634>)

|  |  |
| --- | --- |
|  |  |

5. 单喷嘴机型（X系列/P系列/A1/A1 mini）支持打印机同步功能：点击该按钮后，可一键同步设备页面中当前选中的打印机的机型、喷嘴信息，以帮助用户快速开始切片任务。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-9.png)

6. 支持复制对象的打印参数到其他对象。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-10.gif)

7. 新增冲刷与换头时换料的参数项：包括换头回抽量、冲刷温度、冲刷速度。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-11.png)

8. 发送打印界面优化。

a. 界面交互优化：调整了界面控件的布局，将打印高级选项调整为分段按钮，并新增喷嘴信息显示。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-12.png)

b. 外挂映射逻辑优化：为简化现有外挂映射的操作流程，支持在外挂耗材类型与切片耗材类型不一致的情况下发起映射，同时增加二次确认弹框提醒用户。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-13.gif)

c. 外挂自动匹配逻辑优化：当机器只有外挂耗材时，切片耗材可以根据耗材匹配规则进行自动匹配。

(<https://github.com/bambulab/BambuStudio/issues/6534>  
<https://github.com/bambulab/BambuStudio/issues/6540>  
<https://github.com/bambulab/BambuStudio/issues/6850>  
<https://github.com/bambulab/BambuStudio/issues/6803>  
<https://github.com/bambulab/BambuStudio/issues/6203>  
<https://github.com/bambulab/BambuStudio/issues/6587>)

9. 支持导出切片路径为.obj文件。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-14.png)

10. 新增精准外墙尺寸功能（Precise Wall,开发者模式中选项）：该功能通过增加外壁和内壁之间的间距来提高打印件的尺寸精度，并提升层间一致性。感谢OrcaSlicer的贡献。

|  |  |
| --- | --- |
|  |  |

11. 修改H2D机型Bambu PLA（除了AERO和Support for PLA之外全部）、Bambu PETG HF耗材在0.4/0.6/0.8喷嘴的回抽参数，减少打印过程中的拉丝问题，优化大喷嘴打印时出现孔洞气泡的现象。优化了PLA Lite的打印参数以提升其层间强度。

![](https://wiki.bambulab.com/studio_releasenote/2_1_0/%E6%8B%89%E4%B8%9D%E6%94%B9%E5%96%841_%E4%B8%AD%E6%96%87.jpg)

![](https://wiki.bambulab.com/studio_releasenote/2_1_0/%E6%8B%89%E4%B8%9D%E6%94%B9%E5%96%842_%E4%B8%AD%E6%96%87.jpg)

12. 优化H2D机型Bambu PLA Basic、Bambu PLA Matte、Bambu PETG HF耗材在0.4/0.6/0.8喷嘴的体积流量速度。
13. 经过测试验证，我们将A1/A1 mini系列在打印PLA和PETG材料时的风扇启动时间提前了2秒，以提升打印过程中的散热性能。
14. 支持多TPU在同一盘中进行切片：多TPU耗材可在同一盘中进行切片并增加暂停GCode，然后将所有TPU映射到外挂发起打印，并在打印过程中通过手动换料完成打印。(<https://github.com/bambulab/BambuStudio/issues/6834>)
15. URL处理器现支持从第三方网页打开文件，感谢[@LightDestory](https://github.com/LightDestory)的贡献。
16. 更新部分土耳其语翻译，感谢[@fatih5228](https://github.com/fatih5228)的贡献。
17. 准备页耗材列表优化：

a. 引入一二级分类结构，提升耗材选择效率；

b. 支持显示当前配置不兼容的材料选项。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-19.png)

18. 优化MQTT连接体验。
19. X1/X1C/H2D支持通过 TCP 在公网及 LAN 模式下发送文件：

- X1/X1C：固件版本不低于 01.09.00.00。
- H2D：固件版本不低于01.01.00.00。

20. 准备/预览页面增加预设选项卡折叠按钮：或点击Shift+Tab。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-20.gif)

21. HMS功能更新：

a. 重命名为Assistant (HMS)；

b. 新增若干HMS消息；

c. 修复部分HMS行动点的错误。

## Bug 修复

1. 修复了部分模型狭窄内部实心填充走线不正确问题。  
   <https://github.com/bambulab/BambuStudio/issues/6582>
2. 修复了H2D各喷嘴直径层高限制错误问题。  
   <https://github.com/bambulab/BambuStudio/issues/6647>
3. 修复了部分模型桥接下方铆线缺失问题。  
   <https://github.com/bambulab/BambuStudio/issues/6698>
4. 修复了软件安装在非默认安装目录时冲刷体积弹窗显示异常问题。  
   <https://github.com/bambulab/BambuStudio/issues/6895>  
   <https://github.com/bambulab/BambuStudio/issues/6798>  
   <https://github.com/bambulab/BambuStudio/issues/6740>  
   <https://github.com/bambulab/BambuStudio/issues/6739>  
   <https://github.com/bambulab/BambuStudio/issues/6282>
5. 修复擦料塔回抽值错误导致的模型质量下降的问题。  
   <https://github.com/bambulab/BambuStudio/issues/6733>  
   <https://github.com/bambulab/BambuStudio/issues/6730>
6. 修复了高度修改器输入异常数值后切片失败问题。  
   <https://github.com/bambulab/BambuStudio/issues/6755>
7. 修复H2D机型Timelapse抬升路径计算错误问题。  
   <https://github.com/bambulab/BambuStudio/issues/6869>
8. 修复了P系列/A系列打印机使用TPU 90A发送打印时的误报错问题。  
   <https://github.com/bambulab/BambuStudio/issues/6930>
9. 修复了GUI和命令行自动朝向功能行为不一致的问题。  
   <https://github.com/bambulab/BambuStudio/issues/6092>
10. 支持子object合并为“子合并体”功能。  
    <https://github.com/bambulab/BambuStudio/issues/5855>

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_1_0/image-cn-21.png)

11. 修复了部分模型切片失败问题。  
    <https://github.com/bambulab/BambuStudio/issues/6935>
12. 修复了有机树和普通支撑接触面未按交叠直线生效的问题。  
    <https://github.com/bambulab/BambuStudio/issues/6925>
13. 修复了X系列不支持使用polymaker Fiberon PA6-GF的问题。  
    <https://github.com/bambulab/BambuStudio/issues/6769>
14. 修复了自动摆盘模型超出热床范围问题。  
    <https://github.com/bambulab/BambuStudio/issues/6831>
15. 修复Studio全屏时无法打开任务栏问题。  
    <https://github.com/bambulab/BambuStudio/issues/6659>
16. 增加了在涂色时超过盘范围的界限标识。  
    <https://github.com/bambulab/BambuStudio/issues/6556>
17. 修复了多设备场景下机器耗材未自动同步到准备页的问题  
    <https://github.com/bambulab/BambuStudio/issues/6737>
