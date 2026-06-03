---
path: zh/p1/manual/extension-board-gcode-placeholder-reference
title: "Bambu Lab扩展板G-Code占位符使用说明"
description: ""
tags: ["扩展板"]
created: 2023-05-29T06:42:41.813Z
updated: 2024-05-28T10:49:21.026Z
source: https://wiki.bambulab.com/zh/p1/manual/extension-board-gcode-placeholder-reference
---

# 扩展板 G-Code 占位符总列表

|  |  |  |  |
| --- | --- | --- | --- |
| **名字** | **字段类型** | **定义** | **示例** |
| total\_layer\_count | int | 总层数 | ; layer num/total\_layer\_count: {layer\_num+1}/[total\_layer\_count] 展示层数 |
| previous\_extruder | int 0-16 | 前一个用料 | ;{ filament\_type[previous\_extruder]} 换料时，获取前一个用料的信息 |
| next\_extruder | int 0-16 | 下一个用料 | ;{ filament\_type[next\_extruder]} 换料时，获取下一个用料的信息 |
| layer\_num | int | 此时的层数 | ;{layer\_num} 展示层数 |
| layer\_z | float | 此时打印的层高 |  |
| max\_layer\_z | float | 最大层高 |  |
| x\_after\_toolchange | float | 换料后的坐标 |  |
| y\_after\_toolchange | float | 换料后的坐标 |  |
| z\_after\_toolchange | float | 换料后的坐标 |  |
| filament\_extruder\_id | int | 当前用料的ID | If 判断语句 |
| toolchange\_z | float | 此时总层高 | G1 Z{toolchange\_z} 移动挤出头 |

# 用法

## 从变量名获取数值

`layer_z` 直接使用变量名可以访问变量。

`{layer_z}` 获得其数值。

## 变量名[idex] 获取数组或vector类型占位符的数值

`cool_plate_temp_initial_layer[0]` 访问cool\_plate\_temp\_initial\_layer的第一个元素。

`{cool_plate_temp_initial_layer[0]}` 获取其数值。

## 条件判断语句

`{if scan_first_layer}`

`;=========register first layer scan=====`

`M977 S1 P60`

`{endif}`

## 三元运算符

`(<condition> ? <cond_true>:<cond_false>)`

## 组合gcode 指令

`S[next_extruder]`

`S{cool_plate_temp_initial_layer[0]}`

## string 类型使用"string" 表示

Strings

"Bambu PLA Basic @BBL X1C"

## 普通表达

`/regex/`

## 比较 <, >, ==, !=, <>, <=, >=

`toolchange_count > 1`

## 逻辑操作 &&, ||, !

`{if old_filament_temp > 142 && next_extruder < 255};dosomething{endif}`

## 四则运算 +，-， \*， /

**四则运算参数：**

`{layer_num+1}`

Float 做运算得到 float 类型, int 做运算得到 int 类型，若运算结果想要是小数，请在其中加入 float 类型参数。

例如，3/2=1 3.0/2=1.5

## 匹配

=~ matching !~不匹配

## 函数操作

`min(a,b)` 最小值。

`max(a,b)` 最大值。

`int(a)` 转换为整数类型。

`round(a)` 取整。

`digits(a,num_digits,num_decimals=0)` 小数部分四舍五入到整数，显示num\_digits位，使用空格填充，num\_decimals默认为0，可以不填。

`zdigits(a,num_digits,num_decimals=0)` 同上，用0填充。
