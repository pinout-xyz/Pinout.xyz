<!--
---
name: I-CubeX PiShield 
class: board
type: adc
formfactor: Custom
manufacturer: Infusion Systems 
description: 5V Analog to Digital Converter and 5V I2C level shifter 
url: https://infusionsystems.com/pishield/
github: https://github.com/icubex
buy: http://infusionsystems.com/pishield/?page_id=8
image: 'icubex-pishield.png'
pincount: 26 
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '20':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
install:
  'devices':
    - 'spi'

-->
#I-CubeX PiShield

The I-CubeX PiShield is a 5V sensor interface board that supports 8 channels of 10 bit ADC input via SPI as well as 5V I2C devices. Level conversion to/from 5V is provided for both analog as well as digital sensors.

Features:

- Designed for [I-CubeX Sensors](http://infusionsystems.com/catalog/index.php/cPath/24), but works with any 5V analog sensor via a standard 3-pin header (VCC, SIG, GND)
- ADC performed using MCP3008 chip, and works with existing libraries and applications (including wiringPi)
- Supports up to 8 analog sensors via 3-pin headers, and 4 digital sensors via 2x3-pin headers. For pinout and board schematics, click [here](https://infusionsystems.com/pishield/?page_id=137)
- Enough header protrusion to allow another 26 pin header to be stacked on top
