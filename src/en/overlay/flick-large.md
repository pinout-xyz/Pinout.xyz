<!--
---
name: My Add-on Board
class: board
type: gesture
formfactor: Custom
manufacturer: Pi Supply
description: Flick Large is a 3D tracking and gesture pHAT.
url: https://www.pi-supply.com/product/flick-large-standalone-3d-tracking-gesture-breakout/
github: https://github.com/PiSupply/Flick
buy: https://www.pi-supply.com/product/flick-large-standalone-3d-tracking-gesture-breakout/
image: 'flick-large.png'
pincount: 8
eeprom: no
power: 3v3
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
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: LED Red
  '11':
    name: Reset
  '13':
    name: TS
  '15':
    name: LED Green
i2c:
  '0x42':
    name: Gesture controller
    device: MGC3130
-->
#Flick Large
Integrate Flick into your I2C project to give you multiple ways of controlling it. Using the near field gesture technology, you’re able to hide your project behind non conductive material (wood/acrylic) and still use Flick.

* 3D tracking
* Gesture sensing up to 15cm
* Touch and Tap sensing
* Communicates with the Raspberry Pi via I2C
* No soldering required
* Level shifting chip to enable board to work with 3V3 or 5V0 power and logic
* Red/Green dual colour LED on board
* One line installer
* Fully CE and FCC tested and approved
