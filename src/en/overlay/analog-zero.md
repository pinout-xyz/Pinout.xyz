<!--
---
name: Analog Zero
class: board
type: adc
formfactor: pHAT
image: 'analog-zero.png'
manufacturer: RasPiO
description: A 10-bit 8-channel ADC for Raspberry Pi
url: http://rasp.io/analogzero/
github: https://github.com/raspitv/analogzero
buy: http://rasp.io/analogzero/
pincount: 40
eeprom: no
power: 3v3
pin:
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
#Analog Zero

The RasPiO Analog Zero offers a compact, inexpensive, easy way to add eight analog channels to your Raspberry Pi. RasPiO Analog Zero uses an MCP3008 analog to digital converter. It's an SPI driven, 10-bit, 8-channel ADC.

With RasPiO Analog Zero you can:

* read up to 8 analog inputs at once
* make a weather station
* make a digital thermometer
* make a voltmeter
* use potentiometer dials for control and display
* read analog sensors or voltages
* make your own embedded device with minimal footprint