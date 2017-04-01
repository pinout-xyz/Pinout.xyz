<!--
---
name: DPI
class: interface
type: pinout
description: Raspberry Pi DPI pins
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/dpi/
pin:
  'bcm0':
    name: CLK
  'bcm1':
    name: DEN
  'bcm2':
    name: V-SYNC
  'bcm3':
    name: H-SYNC
  'bcm4':
    name: Blue 0
  'bcm5':
    name: Blue 1
  'bcm6':
    name: Blue 2
  'bcm7':
    name: Blue 3
  'bcm8':
    name: Blue 4
  'bcm9':
    name: Blue 5
  'bcm10':
    name: Blue 6
  'bcm11':
    name: Blue 7
  'bcm12':
    name: Green 0
  'bcm13':
    name: Green 1
  'bcm14':
    name: Green 2
  'bcm15':
    name: Green 3
  'bcm16':
    name: Green 4
  'bcm17':
    name: Green 5
  'bcm18':
    name: Green 6
  'bcm19':
    name: Green 7
  'bcm20':
    name: Red 0
  'bcm21':
    name: Red 1
  'bcm22':
    name: Red 2
  'bcm23':
    name: Red 3
  'bcm24':
    name: Red 4
  'bcm25':
    name: Red 5
  'bcm26':
    name: Red 6
  'bcm27':
    name: Red 7
-->
# DPI - Display Parallel Interface

One of the alternate functions selectable on bank 0 of the Raspbery Pi GPIO is DPI. DPI (Display Parallel Interface) is a 24-bit parallel interface with 28 clock and synchronisation signals.

This interface allows parallel RGB displays to be attached to the Raspberry Pi GPIO either in RGB24 (8 bits for red, green and blue) or RGB666 (6 bits per colour) or RGB565 (5 bits red, 6 green, and 5 blue). It is available as alternate function 2 (ALT2) on GPIO bank 0.

The pinout presented here is for the RGB24 mode, see url below for documentation of the RGB666 and RGB565 modes.
