---
path: zh/software/bambu-scan/manual/project-system
title: "项目系统"
description: ""
tags: []
created: 2026-11-26T14:02:01.240Z
updated: 2026-11-27T01:54:29.403Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/manual/project-system
---

## 介绍

在使用 Bambu Scan 扫描时，往往难以一次完成全部数据采集，经常需要后续补充点云或网格。为满足多种使用场景，**Bambu Scan** 采用了基于 **子项目** 的项目管理体系，能够灵活组织和保存不同类型的扫描工作。

### 项目

在 Bambu Scan 中通常以主界面新建项目的入口来创建，在电脑磁盘上以**文件夹**的形式存在。

其中 \*.bspr 为项目索引文件，可通过主页对项目进行项目位置打开、重命名、导出和删除操作。

|  |  |
| --- | --- |
| 001.jpg | 002.jpg |

### 子项目

当前子项目主要分为以下三类：

- **扫描**：新建的扫描项目，即最常见的子项目类型，保存从扫描到网格到后处理（包含测量中的特征、导入的参考CAD模型等）的全部数据。
- **拼接**：基于多个点云拼接而成的项目，常来源于对同一个物体正反面扫描后通过模型拼接功能而来。其中的点云数据与其他子项目中点云数据不动态关联。
- **其他**：从外部导入的点云或者网格项目，用于单独的模型查看，或者参与点云拼接。

**所有的子项目均维护在项目列表中，以项目树的形式呈现。**

![003.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/project-system/zh/003.jpg)

## 新建子项目

### 新建扫描

扫描以及后处理阶段都可以选择“新建扫描”，新项目将按照 Scan1、Scan2 进行排序。

![004.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/project-system/zh/004.png)

### 新建拼接

当拥有两个或者多个点云文件时，可使用模型拼接功能，拼接生成子项目的子项目也会按序排列在左侧栏中。

![005.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/project-system/zh/005.png)

### 新建其他子项目

可以通过导入按钮，导入点云（\*.asc）或者网格（\*.obj、\*.stl、\*ply）进行导入，并生成对应的子项目。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/project-system/zh/006.jpg)

## 导出与导入

### 子项目的导出与导入

可在左侧栏中选择需要的子项目，右键导出后缀为 .bssub 的子项目文件。该文件对单个子项目中全部数据进行压缩，适用于需要传输单个子项目内容的场景。

![007.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/project-system/zh/007.png)

导入功能则支持更多文件，如 \*.bssub \*.asc \*.stl \*.ply \*.obj

![008.png](https://public-cdn.bblmw.com/wiki/new/software/bambu-scan/manual/project-system/zh/008.png)

### 项目的导出与导入

我们引入了\*.bsprz 文件作为完整项目的压缩导出格式，便于完整文件在不同 PC 间传输。可使用主界面右上角打开文件选项直接打开 \*.bsprz 文件进行导入。

|  |  |
| --- | --- |
| 009.jpg | 010.jpg |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
