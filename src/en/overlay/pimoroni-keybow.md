<!--
---
name: Keybow
class: board
type: io
formfactor: phat
manufacturer: Pimoroni
description: Add illuminated tactile keyboard keys to Raspberry Pi
url: https://shop.pimoroni.com/products/keybow
github: https://github.com/pimoroni/keybow-firmware
buy: https://shop.pimoroni.com/products/keybow
image: 'pimoroni-keybow.png'
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
  '19':
    name: LEDs data
    mode: spi
  '23':
    name: LEDs clock
    mode: spi
  '11':
    name: Key 1
  '13':
    name: Key 2
  '16':
    name: Key 3
  '15':
    name: Key 4
  '18':
    name: Key 5
  '29':
    name: Key 6
  '31':
    name: Key 7
  '32':
    name: Key 8
  '33':
    name: Key 9
  '38':
    name: Key 10
  '36':
    name: Key 11
  '37':
    name: Key 12
-->
# Pimoroni Keybow

Add twelve mechanical keyboard keys to your Pi. Keybow has twelve hot-swappable mechanical switches plus illumination provided by APA102 LEDs.

## Features

* Per-key RGB LEDs (APA102)
* Kailh hot-swap switch sockets (for Cherry MX-compatible switches)
* 40-pin female header
* I2C and SPI breakout header for add-ons
* Custom Keybow OS
* Compatible with Raspberry Pi 3B+, 3, 2, B+, A+, Zero, and Zero W
* No soldering required
