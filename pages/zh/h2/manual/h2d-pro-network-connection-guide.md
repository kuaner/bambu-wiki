---
path: zh/h2/manual/h2d-pro-network-connection-guide
title: "H2D Pro网络连接指南"
description: ""
tags: []
created: 2025-08-08T11:58:24.815Z
updated: 2026-02-11T08:50:06.499Z
source: https://wiki.bambulab.com/zh/h2/manual/h2d-pro-network-connection-guide
---

## 引言

H2D pro可以通过有线和无线方式连接到网络，您可以同时连接有线网络和无线网络，当有线和无线都连接到网络时，优先使用有线与外界进行数据交换。此外，您还可以使用独立的无线物理开关来控制无线网络的连接。

![无线物理开关-新_结果.jpg](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_001.jpg)

H2D pro当前固件支持以下三种联网方式，并且支持自定义IP和DNS等其他设置：

1. 企业无线网络证书认证联网
2. 无线网络账号密码直连（非认证网络）（与H2D相同）
3. 有线网络直连

为了简化开箱流程，我们不支持在开箱过程中使用无线网络证书进行联网。只支持通过无线账号密码直接连接或使用有线网络进行连接。如果您需要连接到需要认证的企业无线网络，请在开箱阶段跳过网络设置。当然，其他两种联网方式也可以在开箱阶段跳过，在初始化完成后，您可以在网络设置页面上进行联网操作。

本文将介绍如何进行上述三种联网方式的操作，并提供IP和DNS自定义设置的入口。

## **适用场景**

请在以下情况下参考本文档：

- **首次将 H2D Pro 打印机连接至网络时。**
- **需要更改或重新配置打印机网络设置时。**

## **适用机型**

**H2D Pro**

## 支持的网络方式与模式

1. **Wi-Fi（无线网络）**：在打印机上选择您的 SSID，并在屏幕上输入密码。
2. **企业级 Wi-Fi（802.1X）**：支持 WPA2-Enterprise；可通过将证书复制到 USB/SD 卡的 `/certificate` 文件夹中，然后在打印机上安装证书。
3. **有线以太网**：支持 100 Mbps 有线连接；如果同时连接 Wi-Fi，则有线连接优先。

## 联网操作方法

## 1. 企业无线网络证书认证联网操作指引

#### 准备工作：在电脑上准备证书和网络连接相关信息

> 💡 温馨提示：准备证书的过程因情况不同而有所差异，本文仅供演示之用。  
> 如果您对操作步骤不熟悉，请咨询您的 IT 部门。

- 与 IT 部门沟通，获取企业／校园网所需的 CA 根证书及域名、认证方式等信息。  
  CA 证书应为 `.cer` 格式。
- 若连接方式采用 TLS 或需要客户端验证，还需申请并导出用户证书，格式为 `.pfx`。  
  是否需要用户证书取决于网络认证方式。
- 若认证方式不需用户证书或您已拥有用户证书，可跳过该步骤。

---

### 申请并导出用户证书（请根据具体情况决定是否执行此步骤）

运行 `certmgr.msc` → 证书 → 当前用户 → 个人 → 证书 → 所有任务 → 申请新证书 →  
选择 **Active Directory 注册策略** → 选择“用户”并注册。

1. 按 **Windows + R**，输入 `certmgr.msc`，然后按 **Enter**。

![申请用户证书-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_002.png)

2. 证书注册流程：

![证书注册流程-1-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_003.png)  
![证书注册流程-2-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_004.png)  
![证书注册流程-3-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_005.png)

3. 导出证书：  
   运行 `certmgr.msc` → 操作 → 查找证书 → 导出私钥。

> ⚠️ 请务必记住用户证书的密码，后续在打印机上安装证书时需要输入此密码。

![导出用户证书-1-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_006.png)  
![导出用户证书-2-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_007.png)  
![导出用户证书-3-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_008.png)  
![导出用户证书-4-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_009.png)  
![导出用户证书-5-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_010.png)  
![导出用户证书-6-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_011.png)

---

### 在打印机上安装证书

将所需证书复制到 U 盘 `/certificate` 目录，并插入打印机

|  |  |
| --- | --- |
|  |  |

完成上述步骤后，打印机将自动扫描位于 U 盘 `/certificate` 目录下的证书文件。  
在此页面中，选择准备好的证书并点击 **安装**，即可将证书成功导入打印机。

> 若存在以 `.pfx` 格式存储的用户证书，在安装过程中需要输入先前设置的导出密码。

![安装证书-2-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_014.jpg)  
![安装证书-3-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_015.png)  
![移除证书-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_016.png)

---

### 删除证书（如有需要）

若不再需要某个证书，可在证书页面中选择对应项目并点击 **卸载**。

![连接企业网-1-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_017.png)

---

### 连接企业网络

#### 第一步：在设置页面点击 “Wi-Fi”，找到需要连接的企业网络

> ⚠️ 请确保打印机的 **无线物理开关已打开**。  
> 若无线物理开关关闭，将无法扫描到任何 Wi-Fi 网络。

![连接企业网-2-en.jpg](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_018.png)  
![配置网络信息-1-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_019.jpg)

---

#### 第二步：填写认证配置信息并确认连接

根据企业网络的实际情况填写相应信息（如认证方式、EAP 类型、匿名身份、用户身份、密码、CA 证书等），  
完成后点击 **确认** 以建立连接。

![配置网络信息-2-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_020.png)  
![8种认证方式-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_021.png)

---

##### 支持的 8 种认证方法介绍

- “—” 表示在该认证方式下不需要该选项内容，不可输入。
- “\*” 表示该项可填可不填。
- CA 证书支持 `.cer` 格式，客户端（用户）证书支持 `.pfx` 格式。
- 匿名身份为进一步保障企业网络连接中用户身份的安全性，可选填，视网络需求而定。

---

![连接普通网络-1-en.jpg](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_022.png)

## 2. 无线网络账号密码直连（非认证网络）（同X1/X1C and P1 series）

##### 第一步：在设置页面，点击"Wi-Fi"，找到要连接的无线网络

![连接普通网络-2-en.jpg](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_023.png)

##### 第二步：根据具体情况填写网络密码，以成功建立网络连接

![连接普通网络输入密码-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_025.png)

## 3. 有线网口联网操作指引

##### 第一步：根据图示，连上网线后，打印机将自动连接到网络

|  |  |
| --- | --- |
|  |  |
|

##### 第二步：检查状态，如果出现“已连接”，则表示联网成功

![手动ip-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_028.jpg)

### 自定义ip等网络信息操作指引

有线网络和无线网络都支持自定义IP等网络信息设置，并且设置方法一致。下文将以有线网络自定义IP等网络信息为例，演示如何进行操作。

##### 第一步：点击ip旁边的编辑按键即可进入，选择自定义的页面，默认是“自动模式”

![手动ip-2-en.png](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_029.png)

##### 第二步：选择“自定义”，即可根据需要变更网络设置

![dm_20250808192504_030_(5).jpg](https://wiki.bambulab.com/h2/manual/h2d-pro-network-connection-guide/dm_20250808192504_030_(5).jpg)

> 注：随着固件更新，UI界面可能会出现细微变化

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！
>
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
