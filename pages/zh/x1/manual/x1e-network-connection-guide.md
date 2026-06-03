---
path: zh/x1/manual/x1e-network-connection-guide
title: "X1E 网络连接指南"
description: "介绍了 X1E 接入网络的几种方法"
tags: ["x1e", "指南", "网络连接"]
created: 2023-10-20T09:24:33.537Z
updated: 2025-07-23T01:13:09.818Z
source: https://wiki.bambulab.com/zh/x1/manual/x1e-network-connection-guide
---

## 1.引言

X1E 可以通过有线和无线方式连接到网络，您可以同时连接有线网络和无线网络，当有线和无线都连接到网络时，优先使用有线与外界进行数据交换。此外，您还可以使用两个独立的物理开关来控制有线网网络和无线网络的连接。如果您同时连接了有线和无线网络，但想使用无线网络，您可以拔掉网线或关闭有线连接的物理开关。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/物理开关.png)

X1E 当前固件支持以下三种联网方式，并且支持自定义 IP 和 DNS 等其他设置：

1. 企业无线网络证书认证联网。目前仅 X1E 支持此功能。
2. 无线网络账号密码直连（非认证网络）（与 X1、X1C 和 P1 系列相同）。
3. 有线网络直连。

为了简化开箱流程，我们不支持在开箱过程中使用无线网络证书进行联网。只支持通过无线账号密码直接连接或使用有线网络进行连接。如果您需要连接到需要认证的企业无线网络，请在开箱阶段跳过网络设置。当然，其他两种联网方式也可以在开箱阶段跳过，在初始化完成后，您可以在网络设置页面上进行联网操作。

本文将介绍如何进行上述三种联网方式的操作，并提供 IP 和 DNS 自定义设置的入口。

## 2.三种联网操作方法

### 2.1 企业无线网络证书认证联网操作指引

#### 2.1.1 安装/删除证书（请根据具体情况决定是否执行此步骤）

##### 第一步：在电脑上准备证书和网络连接相关信息

**温馨提示：准备证书的过程因情况不同而有所差异，本文仅供演示之用。如果您对操作步骤不熟悉，请咨询您的IT部门。**

与IT部门联系，获取连接企业/校园网所需的CA根证书以及与网络兼容的连接方式和域名等相关信息。CA证书的格式应为cer。如果使用TLS连接，则还需要额外申请用户证书，并将其导出为pfx格式。是否需要证书取决于您的网络认证方式，请参考下文的联网认证方式。接下来，我将举一个例子来说明如何使用CA证书导出用户证书。如果您所使用的认证方式不需要用户证书，或者您已经拥有用户证书，则可以跳过申请和导出用户证书的步骤。

###### 申请用户证书（请根据具体情况决定是否执行此步骤）：

运行 certmgr.msc --证书-当前用户-个人-证书-所有任务-申请新证书-- Active Directory 注册策略略-用户-注册

1.Windows键+R弹出“运行”对话框，输入 certmgr.msc ，进入 certmgr.msc 界面

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/run.png)

2.证书注册流程

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-申请证书-1.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-申请证书-2.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-申请证书-3.png)

###### 导出用户证书（请根据具体情况决定是否执行此步骤）：

运行 certmgr.msc -操作-查找证书-导出私钥

温馨提示：请记住用户证书的密码，后面在打印机上安装用户证书时需要输入此密码。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-导出证书-1.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-导出证书-2.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-导出证书-3.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-导出证书-4.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-导出证书-5.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第一步-导出证书-6.png)

##### 第二步：将所需的证书复制到 micro SD 卡 / certificate 目录下，并将 micro SD 卡插入打印机。

|  |  |
| --- | --- |
|  |  |

##### 第三步：进入打印机的网络设置界面，点击证书安装选项。

在完成上述步骤后，打印机将自动扫描位于 SD 卡/证书目录下符合格式要求的证书。在这一步骤中，您需要选择事先准备好的证书，并点击安装，以成功将证书安装到打印机中。如果存在以 pfx 格式存储的用户证书，在安装过程中需要输入之前设置的导出密码。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第三步-1.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第三步-2.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第三步-3.png)

##### 第四步：如果您不再需要某个证书，您可以在该页面上卸载已安装的证书。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.1-第四步.png)

#### 2.1.2 连接企业网

##### 第一步：在网络设置页面，点击"切换无线网络"，找到要连接的企业网络。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.2-第一步-1.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.2-第一步-2.png)

##### 第二步：根据具体情况填写和选择认证所需的配置信息，在页面上点击连接按钮，以成功建立网络连接。

温馨提示：我们支持下文所介绍的8种联网方式，请根据您的实际情况选择相应的认证方式，并输入相应的信息。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.1.2-第二步.png)

##### 所支持的8种认证方法介绍：

"-"表示在对应的认证方式下,不需要该选项内容,不能输入;\*表示该项可填可不填

CA 证书目前支持 cer 格式,客户端证书(用户证书)支持pfx格式

匿名身份是进一步保障企业网连接中用户身份的安全性,可填可不填，取决于你的企业网需求。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/表格.jpg)

### 2.2 无线网络账号密码直连（非认证网络）（同 X1 / X1C and P1 series）

##### 第一步：在网络设置页面，点击"切换无线网络"，找到要连接无线网络。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.2-第一步-1.png)
![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.2-第一步-2.png)

##### 第二步：根据具体情况填写和网络密码，以成功建立网络连接。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.2-第二步.png)

### 2.3 有线网口联网操作指引

> **注意**：在 X1E 设备上，如果您在设备通电运行时热插拔（插拔）网线，可能会导致设备的 IP 地址发生变化。但 Bambu Studio 软件可能仍尝试使用原来的旧 IP 地址进行连接，这样就会导致无法正常连接设备。
>
> 为了解决这个问题，您需要在热插拔网线之后，**先在 Bambu Studio 中解除（解绑）当前设备的连接**，然后再重新连接设备。这样， Bambu Studio 才能获取并使用设备的最新 IP 地址，确保连接顺利。

##### 第一步：根据图示，连上网线后，打印机将自动连接到网络。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/2.3-step1.png)

##### 第二步：检查图标，如果出现“已连接”，则表示联网成功。

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/2.3-第二步.png)

## 3.自定义 IP 等网络信息操作指引

有线网络和无线网络都支持自定义IP等网络信息设置，并且设置方法一致。下文将以有线网络自定义 IP 等网络信息为例，演示如何进行操作。

### 3.1 点击 IP 旁边的编辑按键即可进入，选择自定义的页面，默认是“自动模式”

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/3-第一步.png)

### 3.2 选择“自定义”，即可根据需要变更网络设置

![](https://wiki.bambulab.com/x1/manual/x1e-network-connection-guide/cn-version/3-第二步.png)

后文：随着固件更新，UI 界面可能会出现细微变化。
