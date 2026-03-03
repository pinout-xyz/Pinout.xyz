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
# 3v3 Power

All Raspberry Pi models since the B+ can provide up to 500mA on the 3v3 pins, thanks to a switching regulator. In some cases it may be possible to draw more but, due to lack of documentation and testing on the actual limits, 500mA is given as a rule of thumb.

The 3v3 supply pin on the early Raspberry Pi had a maximum available current of only 50mA.

The 5v supply coupled with a 3v3 regulator is recommended for powering 3.3v projects.

The Piversify blog has [an exploration of the 3v3 supply rail on the Raspberry Pi B+](https://raspberrypise.tumblr.com/post/144555785379/exploring-the-33v-power-rail)
