<!--
---
name: ReSpeaker 2 Mics pHAT
class: board
type: audio
formfactor: phat
manufacturer: seeed
description: Dual-microphone expansion board for AI and voice applications
url: http://wiki.seeed.cc/Respeaker_2_Mics_Pi_HAT/
buy: https://shop.pimoroni.com/collections/raspberry-pi/products/respeaker-2-mics-phat
image: 'respeaker-2-mics-phat.png'
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
    name: GPIO12 pin 4
  '33':
    name: GPIO12 pin 3
  '11':
    name: Button
    mode: input
    external_pull: up
    active: low
  '19':
    mode: spi
    name: RGB LEDs Data
  '23':
    mode: spi
    name: RGB LEDs Clock
-->
# ReSpeaker 2 Mics pHAT

ReSpeaker 2-Mics Pi HAT is a dual-microphone expansion board for Raspberry Pi designed for AI and voice applications. This means that you can build a more powerful and flexible voice product that integrates Amazon Alexa Voice Service, Google Assistant, and so on.

The board is developed based on WM8960, a low power stereo codec. There are 2 microphones on both sides of the board for collecting sounds and it also provides 3 APA102 RGB LEDs, 1 User Button and 2 on-board Grove interfaces for expanding your applications. What is more, 3.5mm Audio Jack or JST 2.0 Speaker Out are both available for audio output.

* BUTTON: a User Button, connected to GPIO17
* MIC_Land MIC_R: 2 Microphones on both sides of the board
* RGB LED: 3 APA102 RGB LEDs, connected to SPI interface
* WM8960: a low power stereo codec
* Raspberry Pi 40-Pin Headers: support Raspberry Pi Zero, Raspberry Pi 1 B+, Raspberry Pi 2 B and Raspberry Pi 3 B
* POWER: Micro USB port for powering the ReSpeaker 2-Mics Pi HAT, please power the board for providing enough current when using the speaker.
* I2C: Grove I2C port, connected to I2C-1
* GPIO12: Grove digital port, connected to GPIO12 & GPIO13
* JST 2.0 SPEAKER OUT: for connecting speaker with JST 2.0 connector
* 3.5mm AUDIO JACK: for connecting headphone or speaker with 3.5mm Audio Plug