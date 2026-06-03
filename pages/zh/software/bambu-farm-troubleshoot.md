---
path: zh/software/bambu-farm-troubleshoot
title: "拓竹农场管家故障排除"
description: ""
tags: []
created: 2025-04-14T02:43:53.980Z
updated: 2026-01-08T08:47:54.574Z
source: https://wiki.bambulab.com/zh/software/bambu-farm-troubleshoot
---

## 无法发现打印机或无法成功添加打印

1. 请检查并升级到如下打印机固件版本：

|  |  |
| --- | --- |
| 机型 | 固件版本 |
| A1/A1 mini | v01.03.20.20 及更高版本 |
| P1P/P1S | v01.06.20.20 及更高版本 |
| X1C | v01.09.00.00 及更高版本 |

首次使用，您需要先绑定 Bambu Handy 来升级打印机固件，之后可以通过农场管家升级打印机固件。  
如果您打印机上未出现升级提示，请重启打印机，重启后打印机会自动同步一次固件信息。

2. 打印机上登出账号

因打印机将接入农场管家中，需要在打印机屏幕上登出账号。登出后打印机上显示为“未登录”状态。

![image_-_2024-11-12t114416.769.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t114416.769.png)

3. 使用指定 IP 范围查找

若打印机未出现在可添加列表中，可打印机屏幕上查看 IP 地址，然后在农场管家中配置对应的查找范围，指定网段扫描和添加。

![image_-_2024-11-12t114427.875.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t114427.875.png)

![image_-_2024-11-12t114430.896.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t114430.896.png)

4. 测试打印机与农场管家服务器 IP 通信

如果依然无法查找或添加打印机，需要测试打印机与农场服务器所在 PC 是否可 IP 通信。从打印机屏幕上获取打印机的 IP 地址，然后在安装农场管家服务器的电脑上执行 ping 操作。下图“192.168.3.105”为打印机 IP 地址。如果无法收到应答包，您需要检查打印机与服务器是否在一个局域网，及子网间的路由是否配置。

![image_-_2024-11-12t114432.954.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t114432.954.png)

5. 检查服务器电脑防火墙配置

如果 ping 测试没有问题，需要进一步检查服务器电脑的防火墙配置，可能是因为安装时没有允许农场管家程序使用网络。可按下面图配置，允许“bambu farm manager server”的 TCP/UDP 数据通过防火墙。

Windows：控制面板\系统和安全\Windows Defender 防火墙\高级设置  
![image_-_2024-11-12t114435.914.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t114435.914.png)

## 添加打印机后，打印机持续显示离线

![1762066207126.png](https://wiki.bambulab.com/software/bambu-farm-manager/1762066207126.png)  
握手阶段，打印机需与服务器 IP 建立长连接；若服务器 PC 的防火墙未放行入站报文，或 NAT 改写服务器源地址，均会导致连接建立失败。定位方法：  
打印机屏幕账号页的服务器IP = 服务器实际IP ： 本节“防火墙入站规则”。  
打印机屏幕账号页的服务器IP = VLAN 网关IP ： 本节“VLAN间NAT配置”。  
**防火墙入站规则：** 通常是安装过程中弹出的windows 安全提示时未选择“运行访问”，可以手动“新建规则”。

- 进入 Windows 的“控制面板\系统和安全\Windows Defender 防火墙\高级设置”, 点击“新建规则”。

![image_-_2025-01-14t095842.039.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2025-01-14t095842.039.png)

- 规则类型：程序。
- 程序路径：安装路径\Bambu Farm Manager Server\Bambu Farm Manager Server.exe。
- 操作：允许连接。
- 配置文件：可根据您实际网络连接情况选择或全部选择（“域”，“专用”，“公用”）。
- 名称：可自定义，如bambu farm。

![image_-_2025-01-14t095806.258.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2025-01-14t095806.258.png)

**VLAN 间 NAT 配置：**  
打印机位于 VLAN1，服务器位于 VLAN2。若添加打印机后，打印机侧显示的服务器 IP 并非 VLAN2 内的真实地址，而是 VLAN1 的网关地址，即表明 VLAN 间转发启用了 NAT，导致网关将服务器回包的源地址替换成了自身地址。解决方案：

1. 关闭 VLAN 间 NAT，仅保留公网出口 NAT，使服务器源地址原样到达打印机。
2. 若必须全局启用 NAT，则在 ACL/Route-Map 首行增加 deny 规则，禁止“服务器到打印机网段”流向做地址转换，并固定服务器 IP 以保证策略匹配。

## 部分打印机频繁离线

1. 请检查是否已达到或接近路由器最大可连接设备数。
2. 可能是 IP 地址冲突，有两个或多个打印机使用同一个 IP 地址。通常该类问题因为网络中配置了两个 DHCP 服务器导致。需要只使用一个 DHCP 服务器，并重启路由器与打印机。
3. 可能部分打印机距离路由器较远，或干扰原因到导致。可尝试更换 WIFI 信道或增加 WIFI 热点来改善无线网络质量。
4. 少数路由器可以设置单个设备或端口的 TCP 最大连接数，修改为不限制或设置一个较大值看是否可以解决。

## 电脑断电重启后，农场管家服务器激活信息丢失或打印机绑定信息丢失

通常该问题发生在电脑突然断电或服务器安装路径下的数据被破坏/删除时。服务器启动时无法正确加载到之前的数据信息。大部分情况软件启动时可以自动恢复，但部分场景依然需要手动处理。  
如下图错误举例，托盘提示农场管家服务器未激活。

![](https://wiki.bambulab.com/software/bambu-farm-faq/image.png)

或长时间大于5分钟，一直显示"start", 服务器没有启动成功

![](https://wiki.bambulab.com/software/bambu-farm-faq/image-1.png)

手动恢复方法为：

- 点击托盘服务器图标，选“stop”停止服务器运行。

![](https://wiki.bambulab.com/software/bambu-farm-faq/f9b79f6593c9e29417e077376a0071c.png)

- 服务器停止后，“Restore” 可以操作，点击“Restore” 选择最近一次数据库备份点。

![](https://wiki.bambulab.com/software/bambu-farm-faq/image-4.png)

可以选择最近一次服务器正常运行时的备份点进行备份。

![](https://wiki.bambulab.com/software/bambu-farm-faq/1743595997144.png)

- 选择数据库备份点后，服务器会进行自动恢复，30秒-1分钟后会切换到运行状态。

![](https://wiki.bambulab.com/software/bambu-farm-faq/image-3.png)

## P 系列打印机无法切换语言

- 对 P 系列机型，在 microSD 卡格式化或更换了新的SD卡后会无法切换语言。您可以通过农场管家执行一次升级操作，语言包会重新下载到打印机的 microSD 卡中，然后重新操作切换语言。

![image_-_2024-11-12t115053.360.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t115053.360.png)

- 另一种方法是将 microSD 卡中的“language”文件夹拷贝到其他 microSD 卡根目录中，再插入打印机使用后重启，再切换语言。

![image_-_2024-11-12t115056.009.png](https://wiki.bambulab.com/software/bambu-farm-faq/image_-_2024-11-12t115056.009.png)

## 农场管家登录账号时，点击登录按钮没有反应

该问题可能与浏览器的策略有关系，请尝试将默认浏览器设置成chrome浏览器观察能否解决问题。  
![农场登录.jpg](https://wiki.bambulab.com/software/bambu-farm-faq/%E5%86%9C%E5%9C%BA%E7%99%BB%E5%BD%95.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
