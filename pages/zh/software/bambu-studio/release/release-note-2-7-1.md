---
path: zh/software/bambu-studio/release/release-note-2-7-1
title: "Bambu Studio 2.7.1 版本说明"
description: ""
tags: []
created: 2026-06-01T09:07:11.054Z
updated: 2026-06-02T01:49:49.886Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-7-1
---

2.7.1 Public Release是基于2.6.1 Public Beta以及2.7.0 Public Beta的新版本。相较于V2.6.0 Public Release，该版本新增对Bambu Lab A2L的支持，并新增纹理转涂色、耗材管理器等重要功能，同时包含部分改进及 Bug 修复。

> ⚠️2.7.0 Public Beta用户注意：因机型预设配置及部分 G-Code 占位符新增，请尽快升级至V2.7.1 Public Release版本避免部分场景下的切片报错问题。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/1.png)

## 新功能

### 纹理转涂色

新增将贴图纹理直接转换为模型涂色的能力。适合需要将彩色图案（Logo、装饰图）应用到3D模型表面的多色打印场景。目前支持OBJ、glTF、GLB、FLB、FBX纹理格式导入。

![2.gif](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/2.gif)

> ⚠️注意事项：
>
> - 暂不支持同时加载多个纹理模型进行转换，请逐个导入。
> - 暂不支持Draco压缩的 glTF / GLB。
> - 受依赖的第三方库影响，macOS对压缩FBX支持受限。

### 耗材管理器

耗材管理器用于统一管理用户的耗材信息及使用状态，当前版本支持：

- 支持查看、编辑与删除耗材，提供搜索、分组与筛选功能。  
  ![3.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/3.png)
- 支持从 AMS 自动读取耗材信息，或手动录入。

|  |  |
| --- | --- |
| 4.1.png | 4.2.png |

> ⚠️注意：
>
> 1. 耗材管理器中的耗材修改（新增/编辑/删除）与余量同步，目前仅支持在联网状态下进行。
> 2. 耗材管理器数据存储于Bambu Cloud, 并在Bambu Studio与Bambu Handy间同步。

### 混色打印渐变效果新增层高曲线控制

渐变效果现支持更自由的层高控制。渐变颜色增加颜色曲线面板，用户可以自由通过左键添加锚点（右键删除）并拖拽颜色曲线，自定义双色在不同 Z 高度上的混合比例，获得更丰富的渐变效果。  
![5.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/5.png)  
![5.1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/5.1.png)

### 混色渐变效果新增“按零件独立应用”模式

混色的渐变效果新增“按零件独立应用”选项：

- 开启：组合体内每个零件独立应用渐变，各零件（part）从自己的底层平滑过渡到自己的顶层。
- 关闭（默认）：保持原行为，组合体作为整体在Z范围统一渐变。  
  适合多个高度不一的零件组合打印的场景，每个小件都能呈现单独的完整渐变效果。

![6.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/6.png)  
![7.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/7.png)

### Liveview支持全屏

Liveview 现支持全屏展示与播放。感谢[bdpdx](https://github.com/bdpdx)的贡献，我们基于他的工作优化了部分前端交互功能。

> 💡Tip：可按ESC键退出全屏。

![8.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/8.png)

### 新增交替额外墙

启用后，会在交替层增加一圈额外墙，其余层保持原有墙层数。该选项适用于在不需要每层都增加外墙的情况下提升模型结构强度。感谢 [igiannakas](https://github.com/igiannakas) 和 [jomixlaf](https://github.com/jomixlaf) 的贡献。

> ⚠️注意：该选项与花瓶模式（或填充为0%的场景）互斥。

![9.1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/9.1.png)![9.2.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/9.2.png)

## 改进

### 纹理转涂色功能优化

- 多纹理模型处理优化：提升了多纹理模型导入时的颜色采样稳定性，包括修复多纹理图集的 UV 映射方式、改进基础颜色材质处理逻辑、优化颜色聚类算法及平滑控制方式。
- 新增网格缺陷检测与修复确认流程：导入纹理模型时自动检测网格缺陷，优化内置修复能力以保障模型水密性，必要时可调用Windows网格修复工具。
- 支持 FBX 文件导入。

### 耗材管理器优化

1. 支持添加耗材时多选批量添加。
2. 重复添加同一卷耗材（RFID 识别）时，新增覆盖确认提示。
3. UI和交互细节优化。

![10.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/10.png)

### 网格缺陷检测优化

优化了网格缺陷检测部分算法，包含：

- 提升非流形边检测准确率
- 增加单独的开放边类别统计  
  ℹ️提示：当前非流形边以错误（Error）形式提示，开放边以普通信息（Info）形式提示

### H2C 优化耗材变轨器退料逻辑

为提升打印效率，带耗材变轨器的打印机在退料时目标位置由AMS调整为变轨器，从而缩短退料行程，节省进退料时间。

> ⚠️固件最低支持版本：01.02.00.00(H2C)

### 优化使用耗材变轨器时PETG料塔稳定性

针对X2D与H2C使用耗材变轨器的场景，通过关闭面熨烫、保留线熨烫，并在料塔旁增加额外挤出，进一步提升 PETG 打印时料塔的稳定性。

### 切割后涂色保留

平面切割（Plane Cut）后保留涂色信息，特别感谢 [solidblu](https://github.com/solidblu) 对此功能的贡献。([10613](https://github.com/bambulab/BambuStudio/pull/10613))

> ⚠️注意：切割面附近的涂色面片可能存在轻微贴合差异。

![11.gif](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/11.gif)

### LAN模式自动保存连接信息

现支持在用户本地记忆局域网连接信息，避免 Studio 重启后需重复绑定局域网机器的问题。([7891](https://github.com/bambulab/BambuStudio/issues/7891), [8270](https://github.com/bambulab/BambuStudio/issues/8270), [8409](https://github.com/bambulab/BambuStudio/issues/8409), [9042](https://github.com/bambulab/BambuStudio/issues/9042))

### G-Code Viewer增加侧板风扇显示

![12.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/12.png)

### 优化后处理脚本切片提醒

当项目文件中包含后处理脚本时，切片前将增加弹窗提醒，帮助用户再次确认脚本内容，提升使用安全性。([#10256](https://github.com/bambulab/BambuStudio/issues/10256))  
![13.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/13.png)

## 其他改进

1. 修复了GMP在GCC15的构建问题，感谢 [hadess](https://github.com/hadess) 和 [c2h5oh](https://github.com/c2h5oh) 的贡献。
2. 支持使用VS 2026与CMake 4.2版本进行编译。
3. 更新了装配视图中耗材控件的显示和交互效果。
4. 涂色“填充”模式默认修改为边缘检测模式。
5. 调整了混色打印的颜色预测方法，感谢 [ratdoux](https://github.com/ratdoux) 的贡献。
6. 多喷嘴机型在仅使用单喷嘴打印时，自动关闭喷嘴偏移校准功能。
7. A1/A1 mini耗材映射上限从16种提升至32种。

> ⚠️固件最低支持版本：01.08.00.00 (A1/A1 mini)

9. Linux迁移至 WebKitGTK 4.1，更好地兼容现代 Linux 发行版。特别感谢 [jijinbei](https://github.com/jijinbei) 的贡献。
10. 3D 视图预设快捷键（Ctrl + [0–7]）在画布失焦时仍可生效。特别感谢 [mpaperno](https://github.com/mpaperno) 的贡献。
11. 新增繁体中文（Traditional Chinese）语言入口：在“偏好设置 → 语言”中新增“繁体中文”选项，繁体中文用户现在可以将界面切换为对应语言显示。特别感谢 [hezhen0816](https://github.com/hezhen0816) 的贡献。

> ℹ️提示：部分界面翻译仍在完善中，少量文案可能暂时显示为英文。

12. 新增 PLA Pure 系列耗材预设。
13. 耗材管理器支持显示官方耗材的颜色信息，同时支持多拼色、渐变色耗材的展示和云端同步。

## Bug修复

1. 针对支撑底部引入倒角后在部分场景下可能造成的倒塌问题，将支撑2mm以下部分默认改为双层墙（指定 0 或单层墙时取消该行为）。( [10542](https://github.com/bambulab/BambuStudio/issues/10542),[10775](https://github.com/bambulab/BambuStudio/issues/10775) )
2. 针对部分场景下Object List顺序可能会影响到嵌入类模型的切片结果，新增选项进行控制（默认关闭）。  
   ![14.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_7_1/14.png)
3. 修复了逐件打印场景下碰撞检测算法未正确考虑裙边间距的问题。
4. 修复了逐件打印的若干报错，以及大小盘切换时的部分问题。( [8770](https://github.com/bambulab/BambuStudio/issues/8770))
5. 修复了切片所有盘时，中间因空盘或不可正常切片的盘导致切片中断的问题。( [10296](https://github.com/bambulab/BambuStudio/issues/10296) )
6. 修复了逐件打印部分场景下模型碰撞风险区显示异常的问题。( [10434](https://github.com/bambulab/BambuStudio/issues/10434) )
7. 修复了部分场景下耗材预设导入时喷嘴温度显示错误的问题。( [10583](https://github.com/bambulab/BambuStudio/issues/10583) )
8. 修复了部分场景下PA值请求失败的问题。( [10351](https://github.com/bambulab/BambuStudio/issues/10351) )
9. 修复了部分场景下A1 mini切片后无法发起打印的问题。( [10418](https://github.com/bambulab/BambuStudio/issues/10418) )
10. 修复了渐变混色模型首层和顶层颜色顺序错误的问题。
11. 修复了德语键盘布局下，文本工具中无法输入小写“e”的问题，同时将“按逐件显示标签”的快捷键从Ctrl+E改为Ctrl/Command+Shift+E。
12. 针对不闭合的stp模型增加导入时提示。
13. 修复了部分场景下铺满打印板的问题。( [8841](https://github.com/bambulab/BambuStudio/issues/8841) )
14. 修复了部分场景下，H2C 同步打印机时无法通过滚动选择 0.6 mm 喷嘴的问题。（ [10059](https://github.com/bambulab/BambuStudio/issues/10059) ）
15. 修复逐件打印模式下修改填充密度时可能发生的崩溃。（# [10350](https://github.com/bambulab/BambuStudio/issues/10350) ）
16. 修复支撑生成中部分阈值角度被错误约束的问题。（# [10553](https://github.com/bambulab/BambuStudio/issues/10553) ）
17. 修复部分场景下K值无法及时更新的错误，感谢 [maziggy](https://github.com/maziggy) 的贡献。（# [9984](https://github.com/bambulab/BambuStudio/issues/9984) ）
18. 修复耗材管理器部分语言显示错误问题，部分未翻译内容以英文替代。（# [10428](https://github.com/bambulab/BambuStudio/issues/10428) ）
19. 修复点击“查看所有对象的配置”的崩溃问题。特别感谢 [hadess](https://github.com/hadess) 的贡献。（# [10607](https://github.com/bambulab/BambuStudio/pull/10607) ）
20. 修复Linux上子下拉菜单显示时父菜单丢失焦点的问题。（# [10175](https://github.com/bambulab/BambuStudio/issues/10175) ）
21. 高收缩耗材警告改为每日提示。
22. 修复自定义盘类型在发送打印时被忽略的问题。（# [10171](https://github.com/bambulab/BambuStudio/issues/10171) ）
23. 修复拓竹官方耗材在 AMS 中被误判为第三方耗材的问题。（# [10279](https://github.com/bambulab/BambuStudio/issues/10279) ）
24. 修复了流量校准模型功能实际调整速度而非流量的错误。（ [10005](https://github.com/bambulab/BambuStudio/issues/10005) ）
25. 修复 X2D 等多AMS机型在“设备”页切换时崩溃的问题。（# [10364](https://github.com/bambulab/BambuStudio/issues/10364) ）
