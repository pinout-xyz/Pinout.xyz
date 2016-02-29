<!--
---
class: interface
type: pinout
name: GPCLK
description: Raspberry Pi General Purpose Clock
pincount: 4
pin:
  'bcm4':
    name: GPCLK0
  'bcm5':
    name: GPCLK1
  'bcm6':
    name: GPCLK2
-->
#GPCLK - General Purpose CLock

###General Purpose Clock pins can be set up to output a fixed frequency without any ongoing software control.

The following clock sources are available:

```
0     0 Hz     Ground
1     19.2 MHz oscillator
2     0 Hz     testdebug0
3     0 Hz     testdebug1
4     0 Hz     PLLA
5     1000 MHz PLLC (changes with overclock settings)
6     500 MHz  PLLD
7     216 MHz  HDMI auxiliary
8-15  0 Hz     Ground
```