---
path: zh/bambu-studio/create-filament>
title: "创建自定义材料预设"
description: ""
tags: ["bambu studio", "预设", "自定义材料", "自建材料"]
created: 2024-03-27T11:26:50.404Z
updated: 2026-03-30T06:26:19.052Z
source: https://wiki.bambulab.com/zh/bambu-studio/create-filament>
---

# 在Bambu Studio中创建自定义材料

在过去，添加新的材料依赖于Bambu Studio的开发人员添加预设来实现，通常增加新预设可能需要等待较长的时间。Bambu Studio提供了两种方法来直接创建自定义材料，可以参考本文介绍的操作步骤来创建它们：

## 方法一

### 创建材料

在耗材丝页面，点击**设置图标——自建材料——新建。**

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/耗材丝页面选择自建材料.png)

填写材料的基本信息，如供应商、类型、系列等，然后选择“基于当前材料创建”，下面的列表会出现您当前已添加并拥有你选择材料类型的打印机。选择对应的打印机型号后，我们将为每个选择的打印机创建一个用户材料预设。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/基于当前材料创建预设1.png)

如果您希望将相同类型的系统预设和用户材料预设合并为一个新材料，请选择“复制当前材料预设”。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/复制当前材料创建预设1.png)

之后，在耗材丝下拉列表中可以看到新创建的材料。新材料预设的命名格式如下：“供应商 类型 系列@打印机型号”

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/在用户配置列表里看到新增耗材1.png)

在耗材丝设置页面修改所需的材料打印参数并保存，自定义材料就创建成功了。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/修改耗材丝设置并保存2.png)

### 编辑、删除预设

如果您在Bambu Studio添加了一台新的打印机，并且想要为此材料创建一个新的打印机预设，或者如果您想要删除您已经创建的材料预设，您可以访问编辑页面来执行这些操作。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/点击编辑自定义材料.png)

我们可以看到，这个界面分为两部分，一部分包含了材料的基本信息，另一部分包含了材料的详细信息和相关功能，包括预设信息显示，添加预设，删除材料。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/编辑材料页面.png)

当您想要将此材料预设添加到新打印机或为现有打印机创建新的预设时，请单击“+添加预设”按钮，选择要添加的打印机，并选择适当的基本预设。点击“确定”按钮将更新预设树。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/为新打印机添加预设.png)

如果你不再需要这个材料，你可以点击左下角的“删除材料”按钮，这将删除与这个材料相关的所有预设。

### 同步自定义材料

和系统预设材料一样，用这个方法创建的**自定义材料可以在 X1 和 X1C 打印机AMS上选择并开始打印。这项功能在固件更新到1.6.6版本及之后版本可用。**

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/x1显示屏显示自定义耗材.jpg)

且用该方法创建的预设，你可以Studio设备页面里，把AMS的槽位的材料信息选择成刚创建的自定义材料。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/studio的耗材丝列表里选中.png)

也可以在耗材丝页面，点击同步材料，把AMS中的自定义材料信息同步到耗材丝列表里。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/同步ams材料列表.png)

## 方法二

### 根据已有材料另存为新预设

在耗材丝设置中，选择当前已有的耗材丝设置，修改参数后另存为，也可以创建一个新的自定义材料。用该方法可以保存为**用户预设**或者**项目预设**，**如果保存为项目预设，它仅会被保存在当前的这个项目（3mf）中。不过该方法一次只能为一个打印机预设创建自定义材料，无法批量创建。**

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/耗材丝页面另存为新材料.png)
![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/项目预设.png)

**相比方法一，方法二是在已有材料预设的情况下快速修改并创建新预设的最快方式。但是用方法二创建的材料，无法像方法一中创建的自建材料成为系统级别的材料预设，所以无法将它同步到打印机中。也无法在Studio的设备页面为AMS插槽选择该材料并将其同步到耗材丝列表中。**

### 删除预设

用这种方法创建的材料，可以在耗材丝设置里，点击“删除此预设”来删除它。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/删除此预设.png)

# 云端用户预设限制

当你在“偏好设置”中启用同步用户预设时，新创建的材料预设将被上传到云服务器。但是，服务器只能存储有限数量的用户预设。**目前我们只支持20个打印机预设，100个工艺预设和200个材料预设。**当所有用户预设超过上述限制时，新创建或导入的预设将只保存在本地，不能与其他计算机上当前帐户下的用户预设同步。在这种情况下，Studio将会有提示。

不过您可以通过导出和导入预设来手动同步多台计算机上的预设。

![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/材料数量超过上限弹窗.jpg)
![](https://wiki.bambulab.com/bambu-studio/parameter/create-custom-filament/预设数量超过上限右下角提醒.jpg)
