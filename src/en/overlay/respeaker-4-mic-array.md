<!--
---
name: ReSpeaker 4 Mic Array
class: board
type: audio
formfactor: phat
manufacturer: seeed
description: 4 mic array for Raspberry Pi to build AI and voice applications
url: http://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/
buy: https://www.seeedstudio.com/ReSpeaker-4-Mic-Array-for-Raspberry-Pi-p-2941.html
image: 'respeaker-4-mic-array.png'
pincount: 40
eeprom: no
power:
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    mode: i2s
  '19':
    mode: i2s
  '35':
     mode: i2s
  '38':
     mode: i2s
  '40':
     mode: i2s
  '32':
    name: GP12 pin 4
  '33':
    name: GP12 pin 3
  '19':
    mode: spi
    name: RGB LEDs Data
  '23':
    mode: spi
    name: RGB LEDs Clock
  '29':
    name: RGB LEDs enable pin
    mode: output
    external_pull: up
    active: high
-->
# ReSpeaker 4 Mic Array

ReSpeaker 4 Mic Array for Raspberry Pi is a quad-microphone expansion board for Raspberry Pi designed for AI and voice applications. This means that you can build a more powerful and flexible voice product that integrates Amazon Alexa Voice Service, Google Assistant, and so on.

The board is developed based on AC108, a highly integrated quad-channel ADC with I2S/TDM output transition for high definition voice capture. Besides, it provides a super cool LED ring, which contains 12 APA102 programmable LEDs. With that 4 microphones and the LED ring, Raspberry Pi would have ability to do VAD (Voice Activity Detection), estimate DOA (Direction of Arrival) and show the direction via LED ring, just like Amazon Echo or Google Home.

## Features

* MIC: 4 Microphones on the corners of the square board
* RGB LED: 12 APA102 RGB LEDs, connected to SPI interface
* AC108: a 4-channels ADC
* Raspberry Pi 40-Pin Headers: support Raspberry Pi Zero, Raspberry Pi 1 B+, Raspberry Pi 2 B and Raspberry Pi 3 B
* I2C: Grove I2C port, connected to I2C-1
* GP12: Grove digital port, connected to GPIO12 & GPIO13