<!--
---
name: Voice HAT
class: board
type: audio,io
formfactor: HAT
manufacturer: AIY
collected: Other
description: A voice kit made for Google Assistant
url: https://aiyprojects.withgoogle.com/voice
github: https://github.com/google/aiyprojects-raspbian
image: 'voice-hat.png'
pincount: 40
eeprom: yes
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
  '7':
    name: Driver 0 Breakout
  '11':
    name: Driver 1 Breakout
  '12':
    name: I2S Clock
  '13':
    name: Driver 2 Breakout
  '15':
    name: Driver 3 Breakout
  '16':
    name: Button
    mode: input
    active: low
  '18':
    name: Servo 5 Breakout
  '22':
    name: LED
    mode: output
    active: high
  '29':
    name: Servo 3 Breakout
  '31':
    name: Servo 1 Breakout
  '32':
    name: Servo 4 Breakout
  '33':
    name: Servo 2 Breakout
  '35':
    name: I2S WS
  '36':
    name: Amp Shutdown
  '37':
    name: Servo 0 Breakout
  '40':
    name: I2S Data
install:
  'devices':
  - 'i2s'
-->
# Voice HAT

Voice HAT descrition TBA