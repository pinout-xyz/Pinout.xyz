<!--
---
name: GertVGA 666
class: board
type: other
formfactor: Custom
manufacturer: Pi Supply
description: The Gert VGA 666 is a breakout/add on board for the Raspberry Pi for using a VGA monitor.
url: https://www.kickstarter.com/projects/pisupply/gert-vga-666-kit-hardware-vga-for-raspberry-pi
github: https://github.com/PiSupply/Gert-VGA-666
schematic: https://github.com/fenlogic/vga666/blob/master/documents/vga_manual.pdf
buy: https://www.pi-supply.com/product/gert-vga-666-hardware-vga-raspberry-pi/
image: 'gertvga-666.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    name: V-SYNC
  '5':
    name: H-SYNC
  '7':
    name: Blue 2
  '8':
    name: Green 6
  '10':
    name: Green 7
  '11':
    name: Red 3
  '12':
    name: Red 4
  '19':
    name: Green 2
  '21':
    name: Blue 7
  '23':
    name: Green 3
  '24':
    name: Blue 6
  '26':
    name: Blue 5
  '29':
    name: Blue 3
  '31':
    name: Blue 4
  '32':
    name: Green 4
  '33':
    name: Green 5
  '35':
    name: Red 5
  '36':
    name: Red 2
  '38':
    name: Red 6
  '40':
    name: Red 7
-->
# GertVGA 666

The Gert VGA 666 (6 bits per colour channel, hence 666) is a breakout/add on board for the Raspberry Pi. It is an open source hardware design released publicly by Gert van Loo.

It is a neat and very useful solution for using a VGA screen/monitor with your Raspberry Pi and is far cheaper than an HDMI to VGA adapter or similar. The VGA connection is driven natively in hardware over the GPIO pins (using a parallel interface) and uses around the same CPU load as the HDMI connection on board. It is capable of displaying 1080p60 VGA video with no CPU load.
