<!--
---
name: Pirate Audio Line Out
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: I2S digital audio to amplified headphone output
buy: https://shop.pimoroni.com/products/pirate-audio-line-out
github: https://github.com/pimoroni/pirate-audio
image: 'pimoroni-pirate-audio-line-out.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '25':
  '39':
pin:
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
  '22':
    name: Amp Enable
    active: high
  '29':
    name: Button A
  '31':
    name: Button B
  '36':
    name: Button X
  '38':
    name: Button Y
  '33':
    name: LCD Backlight
  '21':
    name: LCD Data/Command
  '19':
    name: LCD SPI MOSI
    mode: SPI
  '23':
    name: LCD SPI SCLK
    mode: SPI
  '24':
    name: LCD SPI CS
    mode: SPI
install:
  'devices':
  - 'i2s'
-->
# Pirate Audio: Line-out

Fully supported by Mopidy plugins to create an album-art-displaying digital audio player based on the Raspberry Pi.

* I2C DAC
* Line-level 3.5mm output
* 240x240 LCD
* 4 Playback control buttons