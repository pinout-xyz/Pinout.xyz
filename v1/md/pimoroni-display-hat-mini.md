<!--
---
name: Display HAT Mini
class: board
type: display
formfactor: custom
manufacturer: Pimoroni
description: 320x240 2.0" LCD, RGB LED & 4 Buttons
buy: https://shop.pimoroni.com/products/display-hat-mini
github: https://github.com/pimoroni/displayhatmini-python
image: 'pimoroni-display-hat-mini.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
  '4':
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
  '11':
    name: LED Red
  '13':
    name: LED Green
  '15':
    name: LED Blue
  '22':
    name: LCD TE
  '29':
    name: Button A
  '31':
    name: Button B
  '36':
    name: Button X
  '18':
    name: Button Y
  '33':
    name: LCD Backlight
  '19':
    name: LCD SPI MOSI
    mode: SPI
  '21':
    name: LCD Data/Command
  '23':
    name: LCD SPI SCLK
    mode: SPI
  '26':
    name: LCD SPI CS
    mode: SPI
install:
  'devices':
  - 'i2s'
-->
# Pimoroni Display HAT Mini

A 2.0" 320x240 ST7789V2-based LCD display for your Raspberry Pi. Featuring 4 face buttons and an RGB LED for controlling and monitoring your projects.

## Features

* 2.0" 320x240 SST7789V2-based LCD
* LCD TE (Tear Effect) pin connected
* 4 tactile buttons
* Breakout Garden Header
* Qw'St (Qwiic/Stemma) connector
* RGB LED
* Use with Python
* Mirror desktop with fbcp
