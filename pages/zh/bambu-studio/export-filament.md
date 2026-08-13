---
path: zh/bambu-studio/export-filament
title: "导出打印机预设、材料预设和工艺预设"
description: "本文介绍如何在 Bambu Studio 中导出和导入打印机预设、材料预设与工艺预设。"
tags: ["bambu studio"]
created: 2026-08-10T00:36:20.849Z
updated: 2026-08-12T01:18:37.130Z
source: https://wiki.bambulab.com/zh/bambu-studio/export-filament
---

## 功能介绍

Bambu Studio 允许您导出打印机、材料和工艺预设，用于备份或分享。之后您可以导入已导出的预设，以恢复您的设置，或将其转移到另一台电脑。以下是导出或导入预设的具体步骤。

## 导出预设功能

通过文件下拉菜单，点击 **导出 --> 导出预设包...**。

![export-options.png](https://wiki.bambulab.com/bambu-studio/export-filament/export-options_zh.png)

## 导出预设包界面

当您点击导出预设包时，会显示以下界面。

![export_presets_interface.png](https://wiki.bambulab.com/bambu-studio/export-filament/export_presets_interface_zh.png)

## 导出预设类型

### 1. 打印机预设包

![export_presets_interface.png](https://wiki.bambulab.com/bambu-studio/export-filament/export_presets_interface_zh01.png)

当您选择此导出类型时，可导出的打印机预设包符合以下条件：

- 该打印机预设为用户预设。
- 该打印机预设关联有用户材料预设或用户工艺预设。

选择您想要导出的打印机预设，然后点击 **确认**。

![okay.png](https://wiki.bambulab.com/bambu-studio/export-filament/okay_zh.png)

Bambu Studio 会在所选位置创建一个 Printer Preset Bundle 文件夹。该文件夹包含一个或多个扩展名为 .bbscfg 的文件，每个文件以对应的打印机预设命名。

![exported_preset.png](https://wiki.bambulab.com/bambu-studio/export-filament/exported_presetz_zh.png)

您可以将导出的 .bbscfg 文件导入 Bambu Studio。每个文件都包含所选的打印机预设，以及所有关联的用户耗材预设和用户工艺预设。

### 2. 材料预设包

![filament_preset_bundle.png](https://wiki.bambulab.com/bambu-studio/export-filament/filament_preset_bundle_zh.png)

当您选择此导出类型时，会根据以下规则列出可导出的材料预设包：

- 该材料包含用户自定义的材料预设。
- 仅与第三方打印机关联的材料预设不会显示。

选择您想要导出的耗材，然后点击 **确认**。

![export_filament_presetsz_zh.png](https://wiki.bambulab.com/bambu-studio/export-filament/export_filament_presetsz_zh.png)

Bambu Studio 会在所选位置创建一个 Filament Preset Bundle 文件夹。该文件夹包含一个或多个扩展名为 .bbsflmt 的文件，每个文件以对应的耗材命名。  
您可以将导出的 .bbsflmt 文件导入 Bambu Studio。每个文件都包含与所选耗材关联的所有用户自定义材料预设。

### 3. 打印机预设

![printer_presets_option.png](https://wiki.bambulab.com/bambu-studio/export-filament/printer_presets_option_zh.png)

当您选择此导出类型时，会列出可供导出的用户打印机预设。

> 有关**创建打印机预设**的详细说明，请参阅 [创建自定义打印机或喷嘴](../software/bambu-studio/3rd-party-printer-profile.md)

选择您想要导出的打印机预设，然后点击 **确认**。

![printer_preset_generated.png](https://wiki.bambulab.com/bambu-studio/export-filament/printer_preset_generated_zh.png)

Bambu Studio 会在所选位置创建一个 Printer Presets.zip 文件。该 .zip 文件包含所选的打印机预设，之后可导入 Bambu Studio 以恢复或转移这些预设。

### 4. 材料预设

![filament_presets_zip_zh.png](https://wiki.bambulab.com/bambu-studio/export-filament/filament_presets_zip_zh.png)

当您选择此导出类型时，会使用与导出材料预设包相同的条件列出可供导出的材料名称。

选择您想要导出的耗材，然后点击 **确认**。

![selecting_the_filament_and_exporting.png](https://wiki.bambulab.com/bambu-studio/export-filament/selecting_the_filament_and_exporting_zh.png)

Bambu Studio 会在所选位置创建一个 Filament Presets.zip 文件。该 .zip 文件包含与所选耗材关联的所有用户自定义材料预设，之后可导入 Bambu Studio 以恢复或转移这些预设。

### 5. 工艺预设

![process_presets.png](https://wiki.bambulab.com/bambu-studio/export-filament/process_presets_zh.png)

当您选择此导出类型时，会根据以下规则列出可供导出的打印机名称：

- 仅显示非自定义第三方打印机的用户预设。

选择与您想要导出的工艺预设关联的打印机，然后点击 **确认**。  
![x2s_process_type_zh.png](https://wiki.bambulab.com/bambu-studio/export-filament/x2s_process_type_zh.png)

Bambu Studio 会在所选位置创建一个 Process Presets.zip 文件。该 .zip 文件包含与所选打印机关联的所有用户自定义工艺预设，之后可导入 Bambu Studio 以恢复或转移这些预设。

## 导入预设功能

导入预设功能支持以下文件类型：

- .json – 导入单个预设文件。
- .bbscfg – 导入打印机预设包，包括打印机预设及其关联的用户材料预设和工艺预设。
- .bbsflmt – 导入材料预设包，包括所选耗材的所有用户自定义材料预设。
- .zip – 导入已导出的打印机、材料或工艺预设压缩包。

![import_feature.webp](https://wiki.bambulab.com/bambu-studio/export-filament/import_feature.webp)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn?from=5)，它能够即时解答常见问题，并为您提供操作指导。
