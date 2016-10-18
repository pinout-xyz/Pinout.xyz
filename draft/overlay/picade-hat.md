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
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
  '7':
    name: Shutdown
  '11':
    name: Power
  '13':
    name: Enter
  '15':
    name: Escape
  '16':
    name: Coin
  '18':
    name: Start
  '29':
    name: 'Button 1'
  '23':
    name: 'Button 2'
  '24':
    name: 'Button 3'
  '22':
    name: 'Button 4'
  '21':
    name: 'Button 5'
  '19':
    name: 'Button 6'
  '32':
    name: Up
  '31':
    name: Down
  '38':
    name: Left
  '36':
    name: Right
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
