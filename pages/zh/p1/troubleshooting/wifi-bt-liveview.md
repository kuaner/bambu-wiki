---
path: zh/p1/troubleshooting/wifi-bt-liveview
title: "P1 系列打印机 WIFI/蓝牙/实况摄像头故障排查"
description: "本指南 介绍 P1 系列打印机出现 WIFI/蓝牙/实况摄像头故障时的排查方法。"
tags: ["蓝牙", "故障排查", "摄像头", "wifi"]
created: 2022-12-15T10:32:20.647Z
updated: 2026-04-07T02:24:24.776Z
source: https://wiki.bambulab.com/zh/p1/troubleshooting/wifi-bt-liveview
---

## 屏幕扫码后未发现 BBLPrinter

1 请检查 APP 版本，需要 1.0.6 或之后的版本

2 检查手机设备管理器中蓝牙已打开

3 部分机型要求授权访问位置信息（虽然 APP 并不需位置信息，但手机系统默认要求开启该权限才能使用低功耗蓝牙服务）

![](https://wiki.bambulab.com/p1/troubleshooting/1280x1280_phone_location_access.png)

开启位置信息

## APP 主动添加设备时，无法扫描到 BBLPrinter

1 打印机仅在未配置 WIFI 或 logout，并保持蓝牙功能开启的状态下，此时 APP 可执行添加绑定

2 打印机固件 01.0.0.0，在遗忘 WIFI 或 logout 后，需要重启打印机后执行 APP 绑定

3 打印机固件 01.01.00.00，遗忘 WIFI 和 logout 后会自动开启蓝牙，不需要重起打印机

## APP 扫描到多个 BBLPrinter

APP 显示设备名称的后 15 个字符为设备串号，打印机屏幕上可以查看串号进行比较

![](https://wiki.bambulab.com/p1/troubleshooting/app_sn_display.png)
![](https://wiki.bambulab.com/p1/troubleshooting/device_ui_sn.png)

## 为什么 APP 上绑定设备时没有提示 BT 对频

1. 打印机固件 01.01.00.00 之前的版本，APP 与打印机绑定不需要 BT 对频
2. 从 01.01.00.00 版本开始，为了提高 BT 安全性，执行 BT 对频流程

## APP 与设备 BT 对频失败处理

![](https://wiki.bambulab.com/p1/troubleshooting/pair_failure_case.png)

1. 手机设备管理器中遗忘已配对的 BBLPrinter 设备
2. 手机设备管理器中关闭，再打开一次蓝牙
3. 尝试重新触发APP-打印机绑定

## WIFI 列表中未包含目标热点

1 WIFI 列表信息是打印机反馈给 APP 的，仅支持 2.4G 上的设备

2 可尝试点击空白处， 重新执行“确定绑定”, 打印机会尝试重新扫描一次周围热点

3 如果打印机距离路由器较远，或信号干扰大，有一定概率会扫描不到热点，需要将打印机靠近热点

## Wi-Fi NOT FOUND

![](https://wiki.bambulab.com/p1/troubleshooting/wifi_not_found.png)

通常该问题由 SSID 过长导致，P1P SSID 长度限制是小于等于 31 个字节

## 手机移动网络做热点，进行 APP 与打印机绑定失败

1 开启移动热点前需要关闭 WIFI（大部分手机 移动热点 和 WIFI 不能同时工作）

2 开机启动热点需要选择 2.4G band

## 打印机是否正在录像

1 打印机屏幕上有图标显示摄像头是否已连接，图标中心点闪烁表示正在录像

2 Studio 有图标表示是否在录像

![](https://wiki.bambulab.com/p1/troubleshooting/ui_camera.png)
![](https://wiki.bambulab.com/p1/troubleshooting/studio_camera_on.png)

## APP/Studio 无法播放视频

- **检查相机连接是否正常**

![](https://wiki.bambulab.com/p1/troubleshooting/ui_camera_install.png)

出现上面图标，标识相机已经被打印机主板识别。

- **检查打印机/STUDIO/APP 的版本**

1 打印机1.1.0.0开始，图像数据进行加密传输，需要将APP版本升级到1.0.6 或之后的版本，studio 01.04.00.00 或之后的版本

2 版本升级后需要重新操作一次APP与打印机绑定

3 P1P 当前版本（1.1.0.0）仅支持在局域网传输图像

- **Studio 视频播放时获取不到IP地址，Initialize failed (Missing LAN IP of printer) on studio**

![](https://wiki.bambulab.com/p1/troubleshooting/miss_ip.png)

       P1P 打印机周期性发送广播包用于通知设备在线，路由器仅在局域网内转发广播包，因此要求 Studio/APP 也工作在同一局域网内。Studio/APP 接收到广播包后，可识别出打印机的IP地址，然后与该IP地址建立 TCP-TLS 连接，用于图像数据传输。有多种原因可能导致获取不到打印机的 IP 地址 ，做如下检查。

1. 检查 Studio/Printer 是否在同一局域网内，PC 和 Printer 的 IP 地址应该有相同的子网掩码，比如 192.168.2.X（IP 地址的 4 段数字中仅最后一个不同）
2. 检查 PC 侧防火墙配置，如果关闭 PC 侧网络防火墙后可解决问题，可尝试在修改或添加防火墙规则。UDP 广播地址：239.255.255.250 port 1990(SSDP) 或  255.255.255.255 port 2021。TCP-TLS 打印机侧端口： 6000。
3. 升级 Bambu Studio 到 01.04.02.00 或更新的版本，该版本解决了一处 IP 地址识别失败的问题
4. 检查路由器配置，如果路由器中有“UpnP” 和“IPv4 Multicast Streams” 选项，启用这些选项

- **APP 侧播放视频提示“找不到打印机” 或“设备连线失败”**

1. 检查 APP 版本 1.0.6 或之后的版本
2. 检查 APP Printer  是否在同一局域网内，手机与打印机在同一个无线路由器下
3. 检查路由器配置，如果路由器中有“UpnP” 和“IPv4 Multicast Streams” 选项，启用这些选项。

- **当下载 3mf 或日志上传时图传无法正常播放**

      当下载 3mf 或进行日志上传过程中，图像传输被临时关闭，增强传输的稳定性。传输完成后图传恢复。
