---
path: zh/software/bambu-studio/3mf-compatibility
title: "Bambu Studio 3MF 兼容性说明"
description: ""
tags: []
created: 2024-01-10T07:20:48.167Z
updated: 2024-06-26T03:10:24.198Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/3mf-compatibility
---

## 1. 介绍

从版本1.8.3开始，Bambu Studio的3D模型文件格式（.3mf）将与[3MF联盟](https://github.com/3mfconsortium)提供的3mf读取代码兼容；Bambu Studio的3MF文件也可以在[Microsoft 3D Viewer](https://apps.microsoft.com/detail/9NBLGGH42THS)中打开。

本文将介绍Bambu Studio的3MF文件格式与3MF联盟标准之间的兼容性，概述其特点和优势，并解释为什么其他一些切片软件无法打开由Bambu Studio生成的3mf文件。

## 2. 为什么Bambu Studio默认采用3MF生产扩展规范？

Bambu Studio目前使用3MF联盟的3MF生产扩展规范作为保存3MF文件的默认规范。这个决定是基于对用户体验和未来发展的全面考虑。

### 2.1 3MF生产扩展和3MF核心规范的关系

3MF生产扩展是3MF核心规范的补充，引入了新的功能以有效支持打包构建平台并确保负载的完整性，特别是在高产打印环境中。此扩展的主要重点是可以将模型数据存储在与根模型文件分离的文件中，并允许根模型文件的构建元素引用这些资源。

总的来说，遵循3MF核心规范的3mf文件只有一个根文件，其中包含着所有的模型数据，在解析3mf文件时，会从这个根模型文件中检索，同时只能读取一个模型文件。而遵循3MF生产扩展规范的3mf文件除了一个根文件，还将实际的模型数据保存到不同的文件中，在解析3mf文件时，会根据根模型文件中的索引，找到到其他包含模型数据的文件，可以同时读取多个模型文件，实现了模型数据的并行处理。

### 2.2 Bambu Studio 读取文件速度测试

通过采用[3MF生产扩展](https://github.com/3MFConsortium/spec_production/blob/1.1.2/3MF%20Production%20Extension.md)规范，Bambu Studio在加载和保存模型数据时实现了并行处理，显著提高了操作效率。该规范的特点使我们的用户无论是在设计阶段还是在打开和保存3D模型时，都能够快速处理大型3D模型。

下面是相同数据模型的两个3MF文件。右侧的Studio打开的文件使用了3MF生产扩展规范（命名为Muti-part-Production.3mf），而左侧的Studio打开的文件了使用了3MF核心规范（命名为Muti-part-Core.3mf）。在Bambu Studio中分别打开它们，右侧示例的加载速度明显快于左侧。  
![bambu_speed_of_opening_3mf.gif](https://wiki.bambulab.com/general/3mf_compatibility/bambu_speed_of_opening_3mf.gif)

## 3. 3MF联盟读取测试

成功从文件中检索3D模型的能力是3MF文件可用性的关键标准。在3mf联盟的lib3mf库中包含了一个读取3mf文件的示例。因此，使用Bambu Studio作为3mf文件的生产者，[lib3mf](https://github.com/3MFConsortium/lib3mf/releases/tag/v2.2.0)作为消费者进行读取测试。

通过Bambu Studio保存的3MF文件可以成功读取，检索模型数据没有问题。

下面是来自MakerWorld的一个[3mf文件](https://makerworld.com/zh/models/13716#profileId-14573)，通过Bambu Studio v1.8.3下载、打开和保存后，可以通过lib3mf成功读取数据。  
以下示例包含主要的模型数据：  
![part_of_read_test_result.jpg](https://wiki.bambulab.com/general/3mf_compatibility/part_of_read_test_result.jpg)

## 4. Microsoft 3D Viewer现在能够打开由Bambu Studio生成的3mf文件。

从版本1.8.3开始，由Bambu Studio生成的3MF文件可以成功在[3D Viewer](https://apps.microsoft.com/detail/9NBLGGH42THS)中打开。  
以下gif是由Bambu Studio保存的一个[MakerWorld 3mf](https://makerworld.com/zh/models/13716#profileId-14573)文件，可以被3D Viewer打开。  
![can_open_bambu_3mf.gif](https://wiki.bambulab.com/general/3mf_compatibility/can_open_bambu_3mf.gif)

我们要特别注意的是一个特殊情况。我们注意到，在3MF文件的3D模型描述文件中包含某些中文标点符号可能导致3D Viewer无法成功打开文件。  
这个问题不仅限于符合[3MF生产扩展](https://github.com/3MFConsortium/spec_production/blob/1.1.2/3MF%20Production%20Extension.md)规范的3MF文件，也适用于遵循[3MF核心规范](https://github.com/3MFConsortium/spec_core/blob/1.2.3/3MF%20Core%20Specification.md)的文件。

此外，某些软件和切片工具不支持[3MF生产扩展](https://github.com/3MFConsortium/spec_production/blob/1.1.2/3MF%20Production%20Extension.md)规范。这导致这些工具无法打开由Bambu Studio生成的3mf文件。  
对于广泛用于3D打印的PrusaSlicer和Cura，我们已在GitHub上提交了拉取请求以支持3MF生产扩展规范。

然而，截至目前，我们还没有收到任何反馈。  
<https://github.com/prusa3d/PrusaSlicer/pull/10808> ，  
<https://github.com/Ultimaker/Cura/pull/15761> 。

更新：PrusaSlicer于2024年3月21日合并了相关的补丁。

## 5. 总结

我们深刻理解文件兼容性对用户工作和创意努力的重要性。鉴于此，我们始终努力改进和优化，以符合标准，并积极与社区和相关组织进行沟通。

在这个过程中，感谢您的理解和耐心。如果您有任何问题，请随时联系我们；我们随时准备提供支持。

感谢您对Bambu Studio的理解和支持！
