<!--
---
name: Audio DAC SHIM
class: board
type: audio
formfactor: Custom
manufacturer: Pimoroni
description: An I2S digital to line-level analog audio converter
buy: https://shop.pimoroni.com/products/audio-dac-shim-line-out
image: 'pimoroni-audio-dac-shim.png'
pincount: 40
eeprom: no
power:
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
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
-->
# Audio DAC SHIM

The PCM5100A DAC chip takes high quality digital audio from your Pi and pipes out crisp, line-level 24-bit / 192KHz stereo audio through the 3.5mm jack. Because Audio DAC SHIM adds no extra bulk to your Pi it's perfect for fitting inside sleek cases or hiding inside hi-fis, media centres or radiograms - letting you play music or stream digital radio through that still perfectly good sound system. It's also a handy way to add an an audio output to your Pi Zero or Pi 400!

## Features

* PCM5100A DAC chip
* Line-level digital audio (24-bit / 192KHz) over I2S
* 3.5mm stereo jack
* SHIM-format board with friction-fit connectors
* 2x mounting holes (M2.5) for if you want to secure everything together with bolts
* Fully-assembled
* No soldering required (*unless you're using a Pi that comes without a header)
* Compatible with all 40-pin header Raspberry Pi models
* Dimensions: 66.5 x 16.2 x 5.2mm (L x W x D, including 3.5mm jack)
