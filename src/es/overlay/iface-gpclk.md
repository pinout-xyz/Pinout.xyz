<!--
---
name: GPCLK
class: interface
type: pinout
description: Raspberry Pi General Purpose Clock
pin:
  'bcm4':
    name: GPCLK0
  'bcm5':
    name: GPCLK1
  'bcm6':
    name: GPCLK2
-->
#GPCLK - General Purpose CLock

Los pines de General Purpose Clock pueden programarse a una frequencia fija, sin sofware adicional.

Están disponibles los siguientes:

```
0     0 Hz     Tierra
1     19.2 MHz Oscilador
2     0 Hz     testdebug0
3     0 Hz     testdebug1
4     0 Hz     PLLA
5     1000 MHz PLLC (cambia con overclock)
6     500 MHz  PLLD
7     216 MHz  HDMI auxiliar
8-15  0 Hz     Tierra
```
