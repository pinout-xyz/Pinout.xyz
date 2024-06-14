<!--
---
name: 3v3 Power
class: interface
type: pinout
description: Raspberry Pi 3v3 Power Pins
pincount: 2
pin:
  '1':
  '17':
-->
# 3v3 供电

由于添加了开关稳压器，所以从树莓派 1 代 B+ 开始的所有型号，3v3 供电引脚都支持输出高达 500mA 的电流。在某些情况下也许可以输出更大的电流，但是我们并没有找到相关文档，也没有实际测试过，所以 500mA 是根据经验给出的合理值。

早期树莓派的 3v3 引脚最大只支持输出 50mA 的电流。

如果想给 3.3v 的设备供电，建议使用 5v 供电引脚并配合 3v3 稳压器输出。

Piversify 博客 [对树莓派 B+ 的 3v3 输出做了深入的探索](https://raspberrypise.tumblr.com/post/144555785379/exploring-the-33v-power-rail)
