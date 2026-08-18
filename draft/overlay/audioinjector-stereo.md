<!--
---
name: Audio Injector Stereo Sound Card
class: board
type: audio
formfactor: HAT
manufacturer: Audio Injector
description: A soundcard with stereo input and output, phones amplifier and electret microhpone input.
url: https://www.audioinjector.net/rpi-hat
github: https://github.com/Audio-Injector/stereo-and-zero
buy: https://shop.audioinjector.net/detail/Sound_Cards/Original+Pi+Sound+Card
image: 'audioinjector-stereo.png'
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
# Audio Injector Stereo sound card

A sound card with full functionality

## Features

* inputs (RCA)
* outputs (RCA)
* headphone amp. connector
* electret microphone connector
* potentiometers for RCA input and output trimming
* male header on top of the board for more HAT stacking
* accessories (knobs, plastic fittings)
* fully assembled ready to go!

## Its yours !

The stereo soundcard includes hardware to facilitate stereo audio capture and playback, headphone playback and electret microphone capture. It is fully populated with RCA audio connectors and the microphone. There are potentiometers to trim audio input and output levels. Headphone trimming is dont using the audio level in the alsa mixer. The top of the board has male pins sticking up allowing you to stack other hats (This image shows the male pins with their plastic shipping protector mounted).
