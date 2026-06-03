---
path: zh/bambu-studio/submit-preset
title: "如何提交材料预设到 Bambu Studio"
description: ""
tags: []
created: 2025-04-10T02:37:26.870Z
updated: 2025-04-10T03:12:12.169Z
source: https://wiki.bambulab.com/zh/bambu-studio/submit-preset
---

Bambu Studio 作为一个开源软件，在 Github 上拥有公开的[Github仓库](https://github.com/bambulab/BambuStudio)。如果您有耗材预设希望提交到 Bambu Studio 中，给 Bambu 打印机使用，可以通过 github 提供的 Pull request 方式，将预设通过代码的形式提交到代码仓库中。

## 准备工作

1. 注册 [GitHub 账号](https://github.com/signup)；
2. 安装 [Git 工具](https://git-scm.com/downloads)，使用教程可以参考 [https://git-scm.com/docs/gittutorial。](https://git-scm.com/docs/gittutorial%E3%80%82)

## **获取项目副本**

1. Fork Bambu Studio 仓库

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-7.png)

2. 本地下载代码

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-8.png)

```
# 克隆你的副本到电脑（替换为你的仓库地址）
git clone https://github.com/你的用户名/BambuStudio.git

# 进入项目文件夹
cd 项目名

# 创建新分支
git checkout -b 分支名
```

## 预设创建与修改

### 预设结构介绍

在Bambu studio的代码路径 resources/profiles下，存储着打印机的各项预设。对于Bambu打印机而言，其预设与预设目录均存放在BBL文件夹与BBL.json下。

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-5.png)

BBL 文件夹下存放着 Bambu 打印机的所有预设文件。

BBL.json 中存放着每个预设文件相对 BBL 文件夹的路径，方便软件能够更快速地找到对应的预设文件。

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-6.png)

### 预设创建

Bambu Studio 的预设以树状结构的json文件存储。子节点可以继承父节点的所有属性，并可以对其中的属性进行覆盖。

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image.png)

以上述结构为例，对各个层级的文件进行介绍

1. fdm\_filament\_common：耗材基础文件

   包含了所有的属性以及默认值，后续文件缺省使用这个文件中的参数
2. fdm\_filament\_pla：PLA耗材基础文件

   包含了PLA类型材料的通用属性
3. Bambu PLA Basic @base：PLA Basic耗材基础文件  
   包含了PLA Basic材料的通用属性
4. Bambu PLA Basic @BBL X1C 0.2 nozzle

   包含了针对Bambu Lab X1 Carbon机型0.2喷嘴设定的耗材参数

每个文件中包含着一些关键的参数需要填写：

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-1.png)

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-2.png)

- **from**：标记当前预设是否为系统预设，提交的预设中应该填写 "system"
- **type**：标记当前预设的类型，提交的材料预设中应该填写 "filament"
- **name**：当前预设的名称
- **filament\_id**：材料 id，对应一个材料的唯一标识，以GF开头
- **instantiation**：决定该文件是否会在 Bambu Studio 中显示，instantiation 为 false 的文件，作用是提供通用参数，并不能在切片软件中选择。
- **setting\_id**：材料预设文件id，对应一个预设文件的唯一标识。仅 instantiation 为 true 的文件需要填写，以GFS开头
- **inherits**：决定该文件继承的父文件
- **compartible\_printers**：决定该预设文件可以被哪些机型使用

在创建完预设后，需要将新建的预设文件名与相对路径写入到 BBL.json 中，并保证父节点在子节点前写入。

为了方便您检查创建的预设文件，我们在`resources/profiles`路径下提供了检查脚本，可以运行检查脚本以校验是否存在重复的id

```
cd resource/profiles/
python ./check_duplicated_setting_id.py
```

## 预设提交

1. 提交代码修改

```
git add .

# 添加提交说明
git commit -m "你的修改描述"

# 推送到你的GitHub仓库
git push origin 你的分支名
```

- 创建 PR

  1. 访问你的 GitHub 仓库页面
  2. 点击 **Contribute > Open pull request**
  3. 确保：

     - `base repository` 选择Bambu Studio官方仓库
     - `head repository` 选择你的仓库
     - 正确选择分支
  4. 填写PR说明后点击 **Create pull request**

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-3.png)

![](https://wiki.bambulab.com/software/bambu-studio/submit-preset/image-4.png)
