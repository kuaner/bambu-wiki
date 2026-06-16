---
path: zh/software/bambu-studio/failed-to-get-network-plugin
title: "无法获取网络插件"
description: "本文介绍 Bambu Studio 提示「无法获取网络插件」的常见原因与解决方法。"
tags: ["bambu studio", "studio"]
created: 2023-08-03T06:42:59.101Z
updated: 2026-06-15T08:21:31.036Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/failed-to-get-network-plugin
---

## Windows

请按以下步骤逐项排查：

### 步骤1. 关闭其他 Bambu Studio 窗口

确认所有 **Bambu Studio** 窗口均已**关闭**。

### 步骤2. 检查是否能访问插件服务器

使用浏览器打开以下链接，**检测是否能访问插件服务器**：

<https://public-cdn.bambulab.cn/upgrade/studio/plugins/01.07.01.04/win_01.07.01.04.zip>

- 如果浏览器**开始下载或打开**一个 `zip` 压缩包，说明可以正常访问。
- 如果提示找不到网页，则可能无法访问，请**检查你的网络连接**。

### 步骤3. **确认没有其他程序占用网络插件**

**关闭 Bambu Studio**，**打开**文件夹 `C:\Users\your_user_name\AppData\Roaming\BambuStudio`，**删除**其中的 `plugins` 文件夹。

- **若删除成功**，重新打开 Bambu Studio，它会自动重试安装插件。
- **若删除失败**，说明该文件夹被其他程序占用。请**查明占用程序**并将其关闭后重试；通常**重启电脑**后即可删除。文件夹删除后，重新打开 Bambu Studio 即可重试安装插件。

> ℹ️ 已知会占用网络插件的应用：
>
> - **Microsoft Teams**
> - **Microsoft Agent**
> - **Skype**
> - **Nvidia Broadcast**

### 步骤4. **确认杀毒软件没有阻止网络插件下载**

如果完成以上步骤后仍无法安装，请检查**杀毒软件**是否拦截或删除了网络插件。若是，请将网络插件加入杀毒软件的**白名单**。

### 步骤5. 手动安装网络插件

若以上方法均无效，可尝试手动安装网络插件。操作步骤如下：

1. 用 Bambu Studio 的**版本号**替换下方网址中的 `AA.BB.CC`：

`https://api.bambulab.cn/v1/iot-service/api/slicer/resource?slicer/plugins/cloud=AA.BB.CC.00`

> **说明：**
>
> - `AA.BB.CC` 对应 Bambu Studio 版本号的**前三位**。
> - 例如，版本号为 `01.07.03.50`，则 `AA.BB.CC` 对应前三位 `01.07.03`，替换后的网址为：  
>   `https://api.bambulab.cn/v1/iot-service/api/slicer/resource?slicer/plugins/cloud=01.07.03.00`（示例）。

2. 将替换后的网址粘贴到浏览器地址栏并访问，浏览器会返回如下 json 字符串：(注意：请以实际返回结果为准，不要直接使用以下示例中的字符串和地址。)

```
       {"message":"success","code":null,"error":null,"software":{"type":null,"version":"01.07.03.50","description":"###https://wiki.bambulab.com/en/software/bambu-studio/release/release-note-1-7-3###","url":"https://public-cdn.bambulab.cn/upgrade/studio/software/01.07.03.50/Bambu_Studio_win-v01.07.03.50.exe","force_update":false},"guide":null,"resources":[{"type":"slicer/plugins/cloud","version":"01.07.03.02","description":"","url":"https://public-cdn.bambulab.cn/upgrade/studio/plugins/01.07.03.02/win_01.07.03.02.zip","force_update":false}]}
```

3. 在json 字符串中，找到类型为 **“slicer/plugins/cloud”** 的资源，并找出它对应的 url（以 `.zip` 结尾的网址），例如 `https://public-cdn.bambulab.cn/upgrade/studio/plugins/01.07.03.02/win_01.07.03.02.zip`。
4. 将该 url 复制到浏览器地址栏并访问，即可下载正确的网络插件。
5. 将下载的 zip 包解压到 `C:\Users\your_user_name\AppData\Roaming\BambuStudio\plugins` 目录，然后重启 Bambu Studio 即可完成安装。

  

### 步骤 6. 若曾安装过 VPN / 代理相关软件，请清除系统中残留的代理 / VPN 配置

> **适用场景**：你能正常上网，第 2 步可访问插件服务器，但安装插件仍失败，**电脑上曾安装过 VPN 软件或者代理相关的应用**。  
> **风险提示**：以下操作会清除系统代理设置。若你的工作网络依赖代理，请先记录原有配置以便恢复。

#### 6.1 关闭局域网（LAN）代理设置

- **路径**：控制面板 → 网络和 Internet → Internet 选项 → 连接 → 局域网设置
- 取消勾选"**为 LAN 使用代理服务器**""**自动检测设置**"选项。

|  |  |
| --- | --- |
|  |  |

#### 6.2 删除代理相关的环境变量

- **路径**：此电脑(右键)→ 属性 → 高级系统设置 → 环境变量
- 在【用户变量】和【系统变量】中查找并删除：  
  `ALL_PROXY` / `HTTP_PROXY` / `HTTPS_PROXY`

|  |  |
| --- | --- |
|  |  |

#### 6.3 检查并修正注册表

- **Win+R** 输入 **regedit**  
  ![check_and_fix_registry_1.png](https://wiki.bambulab.com/software/bambu-studio/bambu-studio-common/check_and_fix_registry_1.png)
- **定位**：`HKEY_CURRENT_USER\Software\Microsoft\Windows\ CurrentVersion\Internet Settings`
- 确认 **ProxyEnable = 0**，**ProxyServer 为空**  
  ![check_and_fix_registry_2.png](https://wiki.bambulab.com/software/bambu-studio/bambu-studio-common/check_and_fix_registry_2.png)

#### 6.4 卸载 VPN / 代理软件并重启

- 在"设置 → 应用"中卸载 VPN / 代理类软件
- 重启电脑使所有更改生效，重新打开 Bambu Studio 重试

## macOS

此类问题通常由网络原因引起，部分 VPN 或安全软件会阻止 Bambu Studio 下载网络插件，常见的有：

- **Cisco AnyConnect**
- **iCloud Private Relay**
- **AVG Security**

  

### **禁用 Cisco AnyConnect 的步骤**

1. 运行以下命令，停止「**Cisco Anyconnect Socket Filter**」： `/Applications/Cisco/Cisco\AnyConnect\Socket\Filter.app/Contents/MacOS/Cisco\ AnyConnect\Socket\Filter -deactivateExt`
2. 在「**System Preferences → Network**」页面禁用「**Cisco Anyconnect Socket Filter**」。
3. 卸载「**Cisco Anyconnect Socket Filter**」。
4. 重新安装 Cisco AnyConnect 时，尝试只安装「**VPN**」相关的组件。

![](https://wiki.bambulab.com/software/bambu-studio/bambu-studio-common/wiki-printer-failed-17.png)

  

### **禁用 AVG Security 的步骤**

在系统设置的网络页面中禁用 AVG Security。

![](https://wiki.bambulab.com/software/bambu-studio/bambu-studio-common/wiki-printer-failed-16.png)

  
> **⚠️ 注意：** **获取或使用网络插件即视为您同意并接受 Studio 的[**用户条款**](https://bambulab.cn/zh-cn/policies/terms)。如不同意，请勿下载或使用本插件及任何相关功能。**

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
