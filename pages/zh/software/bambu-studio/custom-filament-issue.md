---
path: zh/software/bambu-studio/custom-filament-issue
title: "自定义材料存在的问题"
description: ""
tags: []
created: 2024-01-10T07:24:30.868Z
updated: 2024-09-18T14:36:51.617Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/custom-filament-issue
---

在Studio版本1.8.2.56中，创建自定义材料存在两个问题。

### 1.1 不支持局域网模式

目前，Studio和打印机只支持新创建的自定义材料功能的云模式。

因此，如果您想使用此功能，请将打印机切换到云模式连接，并确保Studio的云同步已启用。

如果您想在局域网模式中使用此功能，可以先使用云连接创建自定义材料，然后转到打印机屏幕选择材料。此时，打印机将从云中获取材料信息。 （目前，打印机获取云数据的操作是自动的，在登录并进入材料设置页面时自动获取一次。）

### 1.2 创建自定义材料后，从Studio的设备页面直接选择返回到"？"

有两种工作流会导致这种现象。

#### 1.2.1 在创建材料后，打印机屏幕上没有同步。

在创建自定义材料后，直接在Studio的AMS上设置会导致打印机返回"？"。  
这是因为您创建的预设只上传到了云端，而打印机当前没有您创建的材料数据。您需要首先在打印机屏幕上设置它。当您进入打印机的材料设置界面时，材料数据将保存到打印机本地。此时，如果您从Studio端设置材料，将不会再返回"？"。

#### 1.2.2 创建流程不正确

在1.8.2.56版本及更早版本的Studio中，创建材料的工作流存在问题。以下是创建材料的详细流程：

1. 选择“基于当前材料预设进行复制”作为创建方法。
2. 选择的预设是用户预设。如下图所示。  
   ![create_filament_base_on_preset.png](https://wiki.bambulab.com/create_filament/create_filament_base_on_preset.png)

这将导致即使通过打印机的材料设置入口进入，打印机也无法获取材料。

## 2. 自定义材料的解决方案

首先，1.2.2的问题将在新版本中解决。  
接下来是处理打印机无法使用的现有材料的步骤。

### 2.1 手动删除现有材料预设

根据情况，Studio将通过在您创建的自定义材料页面的名称之前添加"[Action Required] ..."，并在列表末尾添加"[Action Required]"来提醒您材料需要操作。这两项中的有问题的预设将逐一介绍如下。  
![action_required_filament.png](https://wiki.bambulab.com/create_filament/action_required_filament.png)

点击"[Action Required] ..."进入材料的编辑页面，那里会突出显示问题的父预设的“删除预设”按钮，例如图中的"CCC PLA Base on Custom preset @ Bambu Lab X1C 0.4 nozzle"。此时，只需删除每个突出显示的预设并重新创建材料。  
![delete_required_edit_filament.png](https://wiki.bambulab.com/create_filament/delete_required_edit_filament.png)

点击"[Action Required]"进入编辑材料页面，所有预设都是有问题的预设。您可以点击左下角的“删除材料”按钮删除所有预设。请注意，此页面可能存在不同的材料预设，Vendor Type Serial可能不太准确，但这没关系。  
![delete_filament_required_edit_filament.png](https://wiki.bambulab.com/create_filament/delete_filament_required_edit_filament.png)

## 3. 总结

注意：在完全删除有问题的项目之前，如果基于有问题的预设创建与有问题的材料相同的材料以覆盖它，可能会导致提示"[Action Required] ..."、"[Action Required]"和"Delete Preset"不准确。在这种情况下，方法是确保您的云同步已启用，然后删除"%appdata%\BambuStudio\user\user\_id\username"文件夹，并登录到您的帐户。云同步后，这些提示将再次变得准确。

只要在2.1中的两个项目在自定义材料列表中不可见，就表示您的所有材料都可以从云中由打印机接收。不用担心使用它。

"创建自定义材料"是v1.8 Studio的重要功能之一。很高兴大家都能使用它并提出问题。对于这个功能中的此错误造成的不便，我们深感抱歉。但我相信Studio将继续改进，并为您提供更好的体验。
