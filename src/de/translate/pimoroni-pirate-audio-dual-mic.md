<!--
---
name: Pirate Audio Dual Mic
class: board
type: audio
formfactor: pHAT
manufacturer: Pimoroni
description: I2S digital audio input with dual microphones
buy: https://shop.pimoroni.com/products/pirate-audio-dual-mic
github: https://github.com/pimoroni/pirate-audio
image: 'pimoroni-pirate-audio-dual-mic.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '25':
  '39':
pin:
  '12':
    name: I2S - Serial Clock 
  '35':
    name: I2S - Word Select
  '38':
    name: I2S - Data Out
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
  '21':
    name: LCD Data/Command
  '19':
    name: LCD SPI MOSI
    mode: SPI
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
# Pirate Audio: Dual Mic

Dual SPH0645LM4H-B microphones, LCD and buttons for tiny stereo audio recording applications.

## Features

* 2x SPH0645LM4H-B microphones 
* 240x240 LCD
* 4 Playback control buttons
