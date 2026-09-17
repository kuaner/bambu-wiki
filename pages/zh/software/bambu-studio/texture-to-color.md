---
path: zh/software/bambu-studio/texture-to-color
title: "纹理转涂色"
description: "本文介绍如何在 Bambu Studio 中应用纹理转涂色功能，将带有纹理贴图的模型转换为多色模型。"
tags: ["bambu studio"]
created: 2026-08-31T07:05:15.055Z
updated: 2026-09-15T01:55:59.538Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/texture-to-color
---

## 功能介绍

「**纹理转涂色**」可将带有纹理贴图的模型直接导入 Bambu Studio 并转换为多色模型，适用于将彩色图案应用到 3D 模型表面的多色打印场景。您可以自己建模、AI 生成，或从其它模型库中下载包含纹理贴图的模型，导入 Studio 后通过「纹理转涂色」功能将纹理贴图自动转换为模型涂色，减少手动涂色的工作量，让多色打印更轻松。

|  |  |
| --- | --- |
|  |  |
| 带有纹理贴图的模型 | 导入 Bambu Studio 的多色模型 |

## 软件版本

- Bambu Studio 2.7.1 版本及以上

> ✅ **说明**： 「纹理转涂色」是 Bambu Studio 2.7.1 版本的新增功能，使用前请将 Bambu Studio 升级至 2.7.1 或更高版本。软件说明详见：[Bambu Studio 2.7.1 版本说明](release/release-note-2-7-1.md)

## 操作步骤

### 步骤 1. 导入模型

点击顶部工具栏的「**添加**」，选择模型文件，点击「**打开**」，导入模型。本文以 obj 模型作为示例。

> ℹ️ **目前支持纹理转换的格式**：OBJ、glTF、GLB、FBX（需包含纹理贴图）

![1_add_zh.webp](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/1_add_zh1.webp)

> ⚠️**注意事项**：
>
> - 暂不支持同时加载多个纹理模型进行转换，请逐个导入。
> - 暂不支持 Draco 压缩的 glTF / GLB。
> - 受依赖的第三方库影响，macOS 对压缩 FBX 支持受限。

### 步骤 2. 预览模型

在弹出的窗口中，左侧窗口可以预览导入后的模型。通过鼠标操作，可以在预览窗口对模型进行旋转、缩放、拖动等查看，操作方式与 Bambu Studio 主界面一致。

![2_import_mode_zh.webp](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/2_import_mode_zh.webp)

预览窗口左上角有「**原项目**」和「**多色**」两个按钮。预览默认展示处理后的多色模型，您也可以将鼠标悬停在「**原项目**」按钮上，以查看导入的原始纹理模型。

![3_original_switch__zh.webp](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/3_original_switch__zh.webp)

### 步骤 3. 调整参数

![3_parameter_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/3_parameter_ui_zh.png)

在导入模型界面，通过调整「**颜色数目**」1 和「**光滑程度**」2两个参数，可以改变将纹理贴图转换为模型涂色的效果，并在「**耗材映射**」3下以清单形式呈现转换后的所有颜色。接下来将对这两个参数进行详细介绍：

  

#### 1. 颜色数目（Color Count）

含纹理贴图的模型通常有成千上万种颜色，无法直接打印。此参数会将这些颜色聚类并映射为有限的几种颜色，从而实现可打印。受限于当前打印机的多色打印能力，该功能目前最多支持 32 色。

![3.1_auto_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/3.1_color_auto_zh.png)

- **取值范围**：1 - 32
- **调节方式**：点击「**4**」「**8**」「**16**」按钮快速设置；或拖动滑块；或在右侧直接输入数值
- **参数效果**：数值越大，还原纹理越精细，但换色和耗材管理越复杂

> ℹ️ **提示**：如果点击「**自动**」，软件将自动确定最佳「**颜色数目**」并重新计算耗材映射。

下图展示了**不同颜色数目**下的多色模型效果（光滑程度均为 5）：

|  |  |  |
| --- | --- | --- |
| 颜色数目 = 4 | 颜色数目 = 8 | 颜色数目 = 16 |

  

#### 2. 光滑程度（Smooth Level）

控制不同颜色交界处的平滑程度。

![3.2_smooth_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/3.2_smooth_zh.png)

- **取值范围**：0 - 10
- **调节方式**：拖动滑块；或在右侧输入数值
- **参数效果**：数值越小，边界越锐利；数值越大，边缘越柔和。可根据实际模型效果选择合适的数值

下图展示了**不同光滑程度**下的多色模型效果（颜色数目均为 8）：

|  |  |  |
| --- | --- | --- |
| 光滑程度 = 0 | 光滑程度 = 2 | 光滑程度 = 10 |

  
> ℹ️ **提示**：每次调整参数后，需要点击「**应用**」按钮，调整后的参数才会生效，并将效果显示在左侧预览窗口。  
> ![3_apply_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/3_apply_zh.png)

### 步骤 4. 耗材映射

耗材映射的含义，是将由纹理贴图聚类得到的模型涂色（左列），分配给实际参与打印的耗材（右列）。

![4_mapping_ui_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/4_mapping_ui_zh.png)

#### 更改耗材映射

软件已自动完成默认的耗材映射，**通常无需改动即可打印**。如需调整某个颜色对应的耗材，可点击右侧的下拉菜单进行更改。

![4_adjust_filament_zh.webp](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/4_adjust_filament_zh.webp)

下拉菜单中的耗材分为三类：

- **项目耗材列表** 1：项目中现有的耗材颜色。
- **新增耗材** 2：纹理转涂色后新增的耗材颜色。
- **新增混色耗材** 3：使用「拆解颜色」功能后新增的混色耗材，详见下文。

![4.1_mapping_list_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/4.1_mapping_list_zh.png)

> ℹ️ **提示**：如果勾选「**自动合并相同的耗材**」4，软件会自动将新增耗材合并到项目中现有的相同耗材中。

#### 添加耗材（可选）

如需使用项目和新增列表之外的颜色，可点击下拉菜单中的「**添加耗材**」，手动添加自定义颜色的耗材。

![4.2_add_zh.webp](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/4.2_add_zh.webp)

#### 拆解颜色（可选）

> **ℹ️ 提示**：拆解颜色属于**进阶功能，仅在需要混色打印时使用**。如果无需混色，可跳过本节。

如果希望用少数几种基础耗材混合出更丰富的颜色，可点击下拉菜单中的「**拆解颜色**」，将选中的模型涂色拆解为可混色的基础色组合（如 CMYW、RYBW 或自定义材料组合）。拆解后新增的耗材会归入「**新增混色耗材**」列表。

关于拆解颜色、一键自动混色等完整说明与操作方法，请参阅：[混色打印-使用纹理转涂色功能](https://wiki.bambulab.com/zh/bambu-studio/color-mixing#color-mixing-texture-to-painting)

![4.1_decompose_zh.webp](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/4.1_decompose_zh1.webp)

### 步骤 5. 完成

在参数调整和耗材映射完成后，点击「**确定**」1 ，多色模型就被成功导入 Bambu Studio。

> ℹ️ **提示**：如果点击「**跳过匹配**」2 ，软件将不再执行贴图转涂色与耗材匹配，并直接导入为**单色模型**。

![5_ok_zh.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/5_ok_zh.png)

将多色模型导入 Bambu Studio 之后，可以对模型进行旋转、缩放等调整，并继续接下来的切片打印操作。

![5.2_results.png](https://wiki.bambulab.com/software/bambu-studio/texture%E2%80%91to%E2%80%91color/0_print_model1.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
