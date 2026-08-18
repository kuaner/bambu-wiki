---
path: zh/software/bambu-connect
title: "Bambu Connect (beta)"
description: "一款能连接和发送打印到 Bambu Lab 3D 打印机的精简工具"
tags: []
created: 2025-01-16T07:42:12.664Z
updated: 2026-08-13T11:44:30.060Z
source: https://wiki.bambulab.com/zh/software/bambu-connect
---

Bambu Connect 是一款能连接和发送打印到 Bambu Lab 3D 打印机的精简工具。它能将已切片的 Bambu Lab gcode 3MF 文件安全地发送到打印机并打印。

## 功能

当前 Bambu Connect 发布的是 Beta 版本，它具备以下功能：

1. 登陆用户云端账号；
2. 查看用户云端绑定的打印机;
3. 发现和连接局域网模式下的打印机；
4. 导入Bambu Lab gcode 3MF，并发送到打印机执行打印；
5. 控制打印机轴移动等控制功能（暂不支持Liveview功能）。

## 下载

- Windows: [bambu-connect-v2.5.0-beta.15-win32-x64.exe](https://public-cdn.bblmw.cn/upgrade/bambu-connect/updates/versions/2.5.0-beta.15/bambu-connect-v2.5.0-beta.15-win32-x64.exe)
- macOS arm64 (Apple silicon): [bambu-connect-v2.5.0-beta.15-darwin-arm64.dmg](https://public-cdn.bblmw.cn/upgrade/bambu-connect/updates/versions/2.5.0-beta.15/bambu-connect-v2.5.0-beta.15-darwin-arm64.dmg)
- macOS x86\_64 (Intel): [bambu-connect-v2.5.0-beta.15-darwin-x64.dmg](https://public-cdn.bblmw.cn/upgrade/bambu-connect/updates/versions/2.5.0-beta.15/bambu-connect-v2.5.0-beta.15-darwin-x64.dmg)
- Linux: 开发中

## 版本说明

[版本说明](releases.md)

## 操作指南

1. 登录 Bambu Lab 账号，查看绑定在对于账号下的打印机。  
   ![登录账号1.png](https://wiki.bambulab.com/software/connect/%E7%99%BB%E5%BD%95%E8%B4%A6%E5%8F%B71.png)  
   ![20250117-164307.jpg](https://wiki.bambulab.com/software/connect/20250117-164307.jpg)
2. 点击软件右上角“发现局域网模式打印机”按钮，Bambu Connect就可以发现处于局域网模式下的打印机并连接。  
   ![20250117-164537.png](https://wiki.bambulab.com/software/connect/20250117-164537.png)  
   ![20250117-164719.png](https://wiki.bambulab.com/software/connect/20250117-164719.png)
3. 切换到“打印”选项卡，导入gcode 3MF文件。  
   ![20250117-164827.png](https://wiki.bambulab.com/software/connect/20250117-164827.png)  
   ![20250117-164932.png](https://wiki.bambulab.com/software/connect/20250117-164932.png)
4. 点击右上角“打印”按钮，发送打印。  
   ![20250117-165054.png](https://wiki.bambulab.com/software/connect/20250117-165054.png)  
   ![20250117-165200.png](https://wiki.bambulab.com/software/connect/20250117-165200.png)

## URL Scheme 导入 gcode 3MF

第三方程序如需告知 Bambu Connect 导入指定的 gcode.3mf 文件，可通过 URL scheme:`bambu-connect://import-file` 打开 Bambu Connect 并导入文件。

添加以下参数：

1. **path**: 指向 3mf 的文件系统绝对路径，比如 /tmp/cube.gcode.3mf，需要使用 [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)编码；
2. **name**: 文件名称，例如 Cube，需要使用 [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) 编码；
3. **version**: 1.0.0，固定值，用于不兼容改动的升级提示。

以下是一个合法的 URL scheme：  
`bambu-connect://import-file?path=%2Ftmp%2Fcube.gcode.3mf&name=Cube&version=1.0.0`
