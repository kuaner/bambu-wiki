---
path: zh/software/cyberbrick-app
title: "CyberBrick 软件"
description: ""
tags: []
created: 2025-05-12T03:50:44.499Z
updated: 2026-06-03T06:03:43.204Z
source: https://wiki.bambulab.com/zh/software/cyberbrick-app
---

## 下载链接

点击[此处](https://bambulab.com/zh/download/cyberbrick-apps)进行下载。

## PC 和移动端功能对比

| **功能** | **Desktop App** | **Mobile App** |
| --- | --- | --- |
| 浏览 CyberBrick 项目 | 无，需在浏览器访问MW网页 | 支持，可直接打开 |
| 从 MakerWorld 打开项目 | 无，仅手动导入 | 支持，扫码 |
| 创建新项目 | 支持 | 不支持 |
| 导入JSON | 支持 | 支持 |
| 蓝牙连接主控板 | 支持 | 支持 |
| 配对主从控制板 | 支持 | 支持 |
| 读取板端项目 | 支持 | 支持 |
| 修改通道映射 | 支持 | 支持 |
| 添加额外零件 | 支持 | 不支持 |
| 修改零件参数（例如限位、限速、方向） | 支持 | 支持 |
| 实时读取传感器输入（例如摇杆读数） | 支持 | 支持 |
| 编辑自定义代码块 | 支持 | 不支持 |
| 导出 JSON 文件 | 支持 | 支持 |

## CyberBrick 桌面软件

### 快速入门教程

#### 更改客户端的语言

在主页左下方点击设置图标，进入设置页面，切换语言。

![1_更改界面语言.png](https://wiki.bambulab.com/cyberbrick/1_%E6%9B%B4%E6%94%B9%E7%95%8C%E9%9D%A2%E8%AF%AD%E8%A8%80.png)

![更换语言界面_cn_2.jpeg](https://wiki.bambulab.com/cyberbrick/%E6%9B%B4%E6%8D%A2%E8%AF%AD%E8%A8%80%E7%95%8C%E9%9D%A2_cn_2.jpeg)

#### 创建新配置

点击主页“新建项目”或选择任意模板创建项目。对于使用通用遥控器的项目，建议从官方遥控器开始，这可以帮助您减少配置工作量。

![1_创建新配置.png](https://wiki.bambulab.com/cyberbrick/1_%E5%88%9B%E5%BB%BA%E6%96%B0%E9%85%8D%E7%BD%AE.png)

![2_创建新配置.png](https://wiki.bambulab.com/cyberbrick/2_%E5%88%9B%E5%BB%BA%E6%96%B0%E9%85%8D%E7%BD%AE.png)

#### 为遥控器添加输入元件

点击接口上的【+】为对应接口添加元器件

> 具体的元器件介绍和配置方法请参照：[CyberBrick 技术手册-输入模块](https://wiki.bambulab.com/zh/cyberbrick/components/component-list#%E8%BE%93%E5%85%A5%E6%A8%A1%E5%9D%97)

![为遥控器添加输入元件.png](https://wiki.bambulab.com/cyberbrick/%E4%B8%BA%E9%81%A5%E6%8E%A7%E5%99%A8%E6%B7%BB%E5%8A%A0%E8%BE%93%E5%85%A5%E5%85%83%E4%BB%B6.png)

#### 添加接收机

点击左侧【+添加接收机】创建新的接收机  
![1_添加接收机.png](https://wiki.bambulab.com/cyberbrick/1_%E6%B7%BB%E5%8A%A0%E6%8E%A5%E6%94%B6%E6%9C%BA.png)

按照带接收机的模型名称为接收机配置命名

![2_添加接收机.png](https://wiki.bambulab.com/cyberbrick/2_%E6%B7%BB%E5%8A%A0%E6%8E%A5%E6%94%B6%E6%9C%BA.png)

添加第二个接收机时，选择控制模式为同时控制还是切换控制。

![3_添加接收机.png](https://wiki.bambulab.com/cyberbrick/3_%E6%B7%BB%E5%8A%A0%E6%8E%A5%E6%94%B6%E6%9C%BA.png)

如需要切换控制，需要指定控制器用于切换的元器件，并指定切换设置

![4_添加接收机.png](https://wiki.bambulab.com/cyberbrick/4_%E6%B7%BB%E5%8A%A0%E6%8E%A5%E6%94%B6%E6%9C%BA.png)

#### 为接收机添加输出元件

点击接口上的【+】为对应接口添加元器件。

> 具体的元器件介绍和配置方法请参照：[CyberBrick 技术手册-输出模块](https://wiki.bambulab.com/zh/cyberbrick/components/component-list#%E8%BE%93%E5%87%BA%E6%A8%A1%E5%9D%97)

![为接收机添加输出元件.png](https://wiki.bambulab.com/cyberbrick/%E4%B8%BA%E6%8E%A5%E6%94%B6%E6%9C%BA%E6%B7%BB%E5%8A%A0%E8%BE%93%E5%87%BA%E5%85%83%E4%BB%B6.png)

#### 保存配置文件

完成编辑后，在右上角点【保存配置】确认保存

![1_保存配置文件.png](https://wiki.bambulab.com/cyberbrick/1_%E4%BF%9D%E5%AD%98%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.png)

如果有未保存的设置更改时退回主页，也可以进行确认

![2_保存配置文件.png](https://wiki.bambulab.com/cyberbrick/2_%E4%BF%9D%E5%AD%98%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.png)

#### 导出JSON配置文件到本地

为了分享项目文件给他人或上传至MakerWorld，可以在首页或开发页面，将项目导出为JSON文件。

![1_导出json配置文件到本地.png](https://wiki.bambulab.com/cyberbrick/1_%E5%AF%BC%E5%87%BAjson%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%88%B0%E6%9C%AC%E5%9C%B0.png)

![2_导出json配置文件到本地.png](https://wiki.bambulab.com/cyberbrick/2_%E5%AF%BC%E5%87%BAjson%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%88%B0%E6%9C%AC%E5%9C%B0.png)

### 页面功能导航

首页：您可以在此浏览近期编辑过的项目，创建新项目，或导入项目。

![1_页面功能导航.png](https://wiki.bambulab.com/cyberbrick/1_%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E5%AF%BC%E8%88%AA.png)

我的项目：您可在此查看所有项目，也可对项目进行批量管理。  
![2_页面功能导航.png](https://wiki.bambulab.com/cyberbrick/2_%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E5%AF%BC%E8%88%AA.png)

我的设备：您可在此添加设备，或更改设备名称、pin码等信息。  
![3_页面功能导航.png](https://wiki.bambulab.com/cyberbrick/3_%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E5%AF%BC%E8%88%AA.png)

创客手册：您可在此查看Wiki、API文档等创作支持。  
![4_页面功能导航.png](https://wiki.bambulab.com/cyberbrick/4_%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E5%AF%BC%E8%88%AA.png)

模型库：您可点击前往MakerWorld查看更多模型。  
![5_页面功能导航.png](https://wiki.bambulab.com/cyberbrick/5_%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E5%AF%BC%E8%88%AA.png)

## CyberBrick 移动应用

![cn-app-1.png](https://wiki.bambulab.com/cyberbrick/cn-app-1.png)

![cn-app-2.png](https://wiki.bambulab.com/cyberbrick/cn-app-2.png)

![cn-app-3.png](https://wiki.bambulab.com/cyberbrick/cn-app-3.png)

![cn-app-4.png](https://wiki.bambulab.com/cyberbrick/cn-app-4.png)

![cn-app-5.png](https://wiki.bambulab.com/cyberbrick/cn-app-5.png)

![component_1.png](https://wiki.bambulab.com/software/cyberbrick/cyberbrick-software/component_5.png)

![component_1.png](https://wiki.bambulab.com/software/cyberbrick/cyberbrick-software/component_6.png)

![cn-app-6.png](https://wiki.bambulab.com/cyberbrick/cn-app-6.png)

![cn-app-7.png](https://wiki.bambulab.com/cyberbrick/cn-app-7.png)

![cn-app-8.png](https://wiki.bambulab.com/cyberbrick/cn-app-8.png)

![cn-app-9.png](https://wiki.bambulab.com/cyberbrick/cn-app-9.png)

![cn-app-10.jpg](https://wiki.bambulab.com/cyberbrick/cn-app-10.jpg)

![cn-app-11.png](https://wiki.bambulab.com/cyberbrick/cn-app-11.png)

![cn-app-12.png](https://wiki.bambulab.com/cyberbrick/cn-app-12.png)

![cn-app-13.png](https://wiki.bambulab.com/cyberbrick/cn-app-13.png)

## 上传配置时，提示更新固件/应用

在最新版本的软件中，您可以在CyberBrick 模型详情页 通过跳转按钮进入 PC 或 APP， 一键将项目配置上传到设备。

在上传配置的过程中，由于**CyberBrick 新增了「自定义项目」功能**， 系统可能会提示 **更新固件/应用**。这属于正常现象，请耐心等待上传完成即可。

### PC：

![软件_上传时更新固件_2_cn.gif](https://wiki.bambulab.com/cyberbrick/%E8%BD%AF%E4%BB%B6_%E4%B8%8A%E4%BC%A0%E6%97%B6%E6%9B%B4%E6%96%B0%E5%9B%BA%E4%BB%B6_2_cn.gif)

![软件_上传时更新固件_1_cn.gif](https://wiki.bambulab.com/cyberbrick/%E8%BD%AF%E4%BB%B6_%E4%B8%8A%E4%BC%A0%E6%97%B6%E6%9B%B4%E6%96%B0%E5%9B%BA%E4%BB%B6_1_cn.gif)

### APP：

![ch-upload_journey.gif](https://wiki.bambulab.com/cyberbrick/ch-upload_journey.gif)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
