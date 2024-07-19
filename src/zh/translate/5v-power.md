<!--
---
name: 5v Power
class: interface
type: pinout
description: Raspberry Pi 5v Power Pins
pincount: 2
pin:
  '2':
  '4':
-->
# 5v 供电

5v 供电引脚直接接在树莓派的电源输入上，除去 Pi 自身消耗的电流外，该引脚可以提供电源适配器提供的全部电流。

如果电源适配器合格的话（比如树莓派官方电源适配器），该引脚可以输出 1.5A 左右的电流。不同的树莓派版本或者电源适配器能输出的电流也会不同。需要消耗大电流的器件，比如 LED 面板、大功率 LED 发光条、或者电机等，应该外接电源，不要用树莓派供电。
