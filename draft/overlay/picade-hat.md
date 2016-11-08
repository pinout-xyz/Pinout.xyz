<!--
---
name: Picade HAT
class: board
type: input
formfactor: HAT
manufacturer: Pimoroni
description: Arcade control inputs plus mono I2S digital audio
buy: https://shop.pimoroni.com/
image: 'picade-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
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
  '7':
    name: Shutdown
    mode: output
  '11':
    name: Power
    mode: output
  '12':
    name: I2S Clock
  '13':
    name: Enter
    mode: input
  '15':
    name: Escape
    mode: input
  '16':
    name: Coin
    mode: input
  '18':
    name: Start
    mode: input
  '19':
    name: 'Button 6'
    mode: input
  '21':
    name: 'Button 5'
    mode: input
  '22':
    name: 'Button 4'
    mode: input
  '23':
    name: 'Button 2'
    mode: input
  '24':
    name: 'Button 3'
    mode: input
  '29':
    name: 'Button 1'
    mode: input
  '31':
    name: Down
    mode: input
  '32':
    name: Up
    mode: input
  '35':
    name: I2S WS
  '36':
    name: Right
    mode: input
  '38':
    name: Left
    mode: input
  '40':
    name: I2S Data
install:
  'devices':
  - 'i2s'
-->
#Picade HAT

Picade HAT provides screw terminals for 10 arcade buttons and a joystick. It also includes a digital to analog audio converter and amplifier which outputs to a single speaker terminal.

All button inputs should be configured with their corresponding internal pull-ups. Buttons should be wired between an input and ground.

* 14 button terminals
* Stereo audio combined for a single speaker
* Support for an external power button and safe power shutdown
