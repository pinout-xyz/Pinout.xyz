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
# GPCLK - General Purpose CLock

Los pines de General Purpose Clock pueden programarse a una frequencia fija, sin sofware adicional.

Están disponibles los siguientes:

* 0 - Tierra, 0 Hz
* 1 - Oscilador de 19.2 MHz
* 2 - testdebug0, 0 Hz
* 3 - testdebug1, 0 Hz
* 4 - PLLA, 0 Hz
* 5 - PLLC, 1000 MHz, cambia con overclock
* 6 - PLLD, 500 MHz
* 7 - HDMI auxiliar, 216 MHz
* 8 a 15 - Tierra, 0 Hz
