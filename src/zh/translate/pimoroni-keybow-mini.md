<!--
---
name: Keybow Mini
class: board
type: io
formfactor: phat
manufacturer: Pimoroni
description: Add illuminated tactile keyboard keys to Raspberry Pi
url: https://shop.pimoroni.com/products/keybow-mini-3-key-macro-pad-kit
github: https://github.com/pimoroni/keybow-firmware
buy: https://shop.pimoroni.com/products/keybow-mini-3-key-macro-pad-kit
image: 'pimoroni-keybow-mini.png'
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
  '15':
    name: Key 2
  '31':
    name: Key 3
-->
# Pimoroni Keybow

Add three mechanical keyboard keys to your Pi. Keybow mini has three hot-swappable mechanical switches plus illumination provided by APA102 LEDs.

## Features

* Per-key RGB LEDs (APA102)
* Kailh hot-swap switch sockets (for Cherry MX-compatible switches)
* 40-pin female header
* I2C and SPI breakout header for add-ons
* Custom Keybow OS
* Compatible with Raspberry Pi 3B+, 3, 2, B+, A+, Zero, and Zero W
* No soldering required
