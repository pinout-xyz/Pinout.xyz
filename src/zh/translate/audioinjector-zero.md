<!--
---
name: Audio Injector Zero Sound Card
class: board
type: audio,sensor
formfactor: pHAT
manufacturer: Audio Injector
collected: Other
description: A soundcard with stereo input and output, phones amplifier and electret microhpone input.
url: https://www.audioinjector.net/rpi-zero
github: https://github.com/Audio-Injector/stereo-and-zero
image: 'audioinjector-zero.png'
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
    name: I2S BCLK
  '35':
    mode: i2s
    name: I2S LRCLK
  '38':
    mode: i2s
    name: I2S SDIN
  '40':
    mode: i2s
    name: I2S SDOUT
-->
# Audio Injector Zero sound card

A sound card with full functionality, inputs, outputs, headphone amp. and an electret microphone connector. Small enough to fit a Zero!

The zero includes hardware to facilitate stereo audio capture and playback, headphone playback and electret microphone capture. It includes IO breakout boards, cables, headers, audio connectors and the microphone. The headers aren't populated so that you can integrate this small sound card into your designs and wire at will.
