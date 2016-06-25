<!--
---
name: MPR121 Cap Touch HAT
class: board
type: touch
image: 'adafruit-cap-mpr121.png'
manufacturer: Adafruit
description: Create electronics that can react to human touch with up to 12 individual sensors.
url: https://www.adafruit.com/products/2340
github: https://github.com/adafruit/Adafruit_Python_MPR121
buy: https://www.adafruit.com/products/2340
formfactor: 'HAT'
pincount: 40
eeprom: yes
power:
  '1':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x5A':
    name: Cap Touch
    device: mpr121
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
-->
#Explorer HAT

This Raspberry Pi add-on board provides 12 capacitive touch inputs and all the logic to read them over a simple I2C communication bus.

Baded on the MPR121 chip, this HAT allows you to create electronics that can react to human touch, with up to 12 individual sensors.