<!--
---
class: interface
type: pinout
name: DPI
description: Raspberry Pi DPI pins
pincount: 22
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
    name: Blue 2
  'bcm5':
    name: Blue 3
  'bcm6':
    name: Blue 4
  'bcm7':
    name: Blue 5
  'bcm8':
    name: Blue 6
  'bcm9':
    name: Blue 7
  'bcm10':
    name: Green 2
  'bcm11':
    name: Green 3
  'bcm12':
    name: Green 4
  'bcm13':
    name: Green 5
  'bcm14':
    name: Green 6
  'bcm15':
    name: Green 7
  'bcm16':
    name: Red 2
  'bcm17':
    name: Red 3
  'bcm18':
    name: Red 4
  'bcm19':
    name: Red 5
  'bcm20':
    name: Red 6
  'bcm21':
    name: Red 7
-->
#DPI - Display Parallel Interface

###DPI (Display Parallel Interface) is a 24-bit parallel interface with 28 clock and synchronisation signals. The Pi uses a cut-down, 6-bit, 22 pin version omitting the least significant R, G and B colour bits.

DPI, combined with a simple adaptor consisting of 20 resistors, allows you to add a VGA connector to the Pi which supports resolutions from 640 x 480 up to 1920 x 1024 at 60fps and 6bits per channel.