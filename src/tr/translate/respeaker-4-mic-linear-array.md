<!--
---
name: ReSpeaker 4 Mic Linear Array
class: board
type: audio
formfactor: HAT
manufacturer: seeed
description: 4 mic linear array for Raspberry Pi to build AI and voice applications
url: http://wiki.seeedstudio.com/ReSpeaker_4-Mic_Linear_Array_Kit_for_Raspberry_Pi/
buy: https://www.seeedstudio.com/ReSpeaker-4-Mic-Linear-Array-Kit-for-Raspberry-Pi-p-3066.html
image: 'respeaker-4-mic-linear-array.png'
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
-->
# ReSpeaker 4 Mic Linear Array

This HAT comes with 4 microphones and is designed for AI and voice applications; integration with Amazon Alexa Voice, Google Assistant, and so on. It consists of two boards: the voice accessory HAT, and the four microphone linear array. It supports 8 input and 8 output channels in Raspbian/Raspberry Pi OS. The first 6 input channels are for microphone recording. Only the first 4 input channels are valid capture data, the remaining 2 input channels are an echo channel for playback. The first 2 output channels output stereo audio, the remaining 6 are unused.

* MIC: 4 Microphones
* AC108: 2 4-channels ADC
* AC101: a 2-channels DAC
* Raspberry Pi 40-Pin Header
* I2C: Grove I2C port, connected to I2C-1
* GP12: Grove digital port, connected to GPIO12 & GPIO13
* JST 2.0 SPEAKER OUT: for connecting speaker with JST 2.0 connector
* 3.5mm AUDIO JACK: for connecting headphone or speaker with 3.5mm Audio Plug