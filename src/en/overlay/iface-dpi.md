<!--
---
class: interface
type: pinout
name: DPI
description: Raspberry Pi DPI pins
pincount: 22
pin:
  '0':
    name: CLK
  '1':
    name: DEN
  '2':
    name: V-SYNC
  '3':
    name: H-SYNC
  '4':
    name: Blue 2
  '5':
    name: Blue 3
  '6':
    name: Blue 4
  '7':
    name: Blue 5
  '8':
    name: Blue 6
  '9':
    name: Blue 7
  '10':
    name: Green 2
  '11':
    name: Green 3
  '12':
    name: Green 4
  '13':
    name: Green 5
  '14':
    name: Green 6
  '15':
    name: Green 7
  '16':
    name: Red 2
  '17':
    name: Red 3
  '18':
    name: Red 4
  '19':
    name: Red 5
  '20':
    name: Red 6
  '21':
    name: Red 7
-->
#DPI - Display Parallel Interface

###DPI (Display Parallel Interface) is a 24-bit parallel interface with 28 clock and synchronisation signals. The Pi uses a cut-down, 6-bit, 22 pin version omitting the least significant R, G and B colour bits.

DPI, combined with a simple adaptor consisting of 20 resistors, allows you to add a VGA connector to the Pi which supports resolutions from 640 x 480 up to 1920 x 1024 at 60fps and 6bits per channel.