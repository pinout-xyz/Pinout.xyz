<!--
---
name: SparkFun AVR Programmer HAT
class: board
type: mcu,io
formfactor: Custom
manufacturer: SparkFun
description: Arduino Programming on the Raspberry Pi
url: https://www.sparkfun.com/products/14747
github: https://github.com/sparkfun/SparkFun_Pi_AVR_Programmer_HAT
buy: https://www.sparkfun.com/products/14747
image: 'sparkfun-avr-programmer-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
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
  '8':
    mode: uart
  '10':
    mode: uart
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
  '7':
    name: Script LED
  '11':
    name: Flash HEX Fail LED
  '31':
    name: Flash HEX Pass LED
  '18':
    name: Serial Upload Fail LED
  '16':
    name: Serial Upload Pass LED
  '22':
    name: Lock Bits Fail LED
  '32':
    name: Lock Bits Pass LED
  '13':
    name: Fuse Bits Fail LED
  '15':
    name: Fuse Bits Pass LED
  '37':
    name: Reset
  '29':
    name: Shutdown
  '33':
    name: Capsense
  '36':
    name: Program Control
install:
  'devices':
    - 'spi'
-->
# SparkFun AVR Programmer HAT

The SparkFun AVR Programmer HAT lets you program AVR microcontrollers (the chips you'll find on Arduino boards, for example) directly from the SPI hardware pins on the Raspberry Pi.

It was originally an in-house solution for production programming, but has been tidied up into a programming tool for anyone.

It's fully open source and hackable, works directly with AVRDude and provides ISP programming which is great for deployment since it doesn't require a boot-loader, uploads code faster and allows you to set protection fuse bits. It's useful if you're programming many AVR chips either for hobby projects or small yield production.