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

General Purpose Clock pins can be set up to output a fixed frequency without any ongoing software control.

The following clock sources are available:

* 0 - Ground, 0 Hz
* 1 - 19.2 MHz oscillator
* 2 - testdebug0, 0 Hz
* 3 - testdebug1, 0 Hz
* 4 - PLLA, 0 Hz
* 5 - PLLC, 1000 MHz, changes with overclock settings
* 6 - PLLD, 500 MHz
* 7 - HDMI auxiliary, 216 MHz
* 8 to 15 - Ground, 0 Hz

Other frequencies can be achieved by setting a clock-divider in the form of `SOURCE/(DIV_I + DIV_F/4096)`. Note, that the [BCM2835 ARM Peripherals](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2835/BCM2835-ARM-Peripherals.pdf) document contains an error and states that the denominator of the divider is 1024 instead of 4096.
