---
path: zh/software/bambu-studio/preset
title: "如何创建自定义预设"
description: "自定义预设功能是可以让用户自定义并保存某些设置和参数，以便在以后的切片使用过程中快速调用。"
tags: ["bambu studio"]
created: 2023-07-26T02:09:19.411Z
updated: 2025-06-03T09:01:49.682Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/preset
---

## 系统预设

系统预设是 Bambu Studio 为每台支持的打印机提供的内置预设。选择打印机后，将自动导入内置文件，其中包含该打印机的打印机、耗材丝、和工艺的预设。

系统预设不允许直接修改。但是，您可以通过复制系统预设，修改为适合您需求的参数，并将结果保存为自定义的用户预设。

|  |  |  |
| --- | --- | --- |
|  |  |  |

**注意：**   
工艺参数的预设，会随着*打印机不同喷嘴型号*的选择而改变。 比如，当您选择了“Bambu Lab X1C 0.4 nozzle”，您看到的工艺参数是这样的：

![](https://wiki.bambulab.com/software/bambu-studio/preset/1280x1280_(3).png)

当您切换为“Bambu Lab X1C 0.2 nozzle”，您看到的工艺参数将是这样：

![](https://wiki.bambulab.com/software/bambu-studio/preset/1280x1280_(4).png)

## 用户预设

您可以通过创建用户预设来保存最常用的模型切片参数。比如，如果您的大多数模型对强度有严格要求，您可以创建一个预设来增加墙、填充密度和壳体层数，并选择蜂窝状等填充图案。另一个典型的例子，就是为第三方耗材丝创建新的耗材丝参数预设。

要创建用户预设，您可以首先选择系统预设作为基础。修改了相应的参数后，请单击“保存”图标，为新预设命名，并在弹出的对话框中选择“用户预设”类型。注意，不建议新手用户随意修改参数。 您可以为打印机、耗材丝、和工艺，进行用户预设，具体保存方法如下：

### **打印机用户预设**

![](https://wiki.bambulab.com/software/bambu-studio/preset/1280x1280_(6).png)

### **耗材丝用户预设**

![](https://wiki.bambulab.com/software/bambu-studio/preset/b9fe482b-98e7-4e7e-8d3c-3396c29ac95d.png)

### **工艺用户预设**

![](https://wiki.bambulab.com/software/bambu-studio/preset/b0972ce1-5012-4bfa-9a09-92e89203bd4f_(1).png)

新创建的用户预设将（请在偏好设置里，启用预设功能）上传到 Bambu Cloud 并属于当前登录帐户。

![](https://wiki.bambulab.com/software/bambu-studio/preset/pianhao.png)

此外，当用户每次登录Bambu Studio时，用户预设数据都可以自动从Bambu Cloud下载。

![](https://wiki.bambulab.com/software/bambu-studio/preset/login.png)
> *注意：云端资源有限，非  Bambu Lab  机型的预设暂时不支持云同步。*

## 项目预设

您还可以将打印机、耗材丝和工艺修改的参数保存为项目预设。项目预设仅保存在当前项目文件 (.3mf) 中。项目预设仅在 Bambu Studio 中加载该项目时可见，加载其他项目后将消失。与用户预设不同的是，它与任何用户帐户无关，也不会上传到Bambu Cloud。

 以工艺项目预设为例：

![](https://wiki.bambulab.com/software/bambu-studio/preset/xiangmu.png)

## 导出和导入预设

如果您想与其他人共享设置或创建自定义设置的备份，您可以**将当前使用的工艺中的用户预设**导出到本地文件夹。

### 导出预设

Bambu Studio 允许导出工艺中的用户预设，下面的gif图显示了如何导出用户预设文件。

![](https://wiki.bambulab.com/software/bambu-studio/preset/daochu.gif)

### 导入预设

Bambu Studio允许导入用户预设到工艺中，下面的gif图显示了如何导入用户预设文件。

![](https://wiki.bambulab.com/software/bambu-studio/preset/daoru.gif)

## 删除预设

在成功创建新的预设后，您可以注意到保存预设按钮右侧有一个 × 符号。点击该符号即可进行删除预设的操作。

**下面以耗材丝用户预设为例：**

![](https://wiki.bambulab.com/software/bambu-studio/preset/删除.png)
