<!--
---
name: Picade X HAT
class: board
type: io,power
formfactor: HAT
manufacturer: Pimoroni
description: Arcade inputs & digital amp
buy: https://shop.pimoroni.com/products/picade
github: https://github.com/pimoroni/picade-hat
image: 'picade-x-hat.png'
pincount: 40
eeprom: setup
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
    name: Shutdown
    mode: output
    active: low
  '8':
    name: 'Button 8'
    mode: input
    active: low
  '10':
    name: 'Button 7'
    mode: input
    active: low
  '11':
    name: Power Button
    mode: input
    active: low
  '12':
    name: I2S Clock
  '13':
    name: Enter
    mode: input
    active: low
  '15':
    name: Escape
    mode: input
    active: low
  '16':
    name: Coin
    mode: input
    active: low
  '18':
    name: Start
    mode: input
    active: low
  '19':
    name: 'Button 6'
    mode: input
    active: low
  '21':
    name: 'Button 5'
    mode: input
    active: low
  '22':
    name: 'Button 4'
    mode: input
    active: low
  '23':
    name: 'Button 2'
    mode: input
    active: low
  '24':
    name: 'Button 3'
    mode: input
    active: low
  '29':
    name: 'Button 1'
    mode: input
    active: low
  '31':
    name: Down
    mode: input
    active: low
  '32':
    name: Up
    mode: input
    active: low
  '33':
    name: 'Power LED'
    mode: output
    active: high
  '35':
    name: I2S WS
  '36':
    name: Right
    mode: input
    active: low
  '38':
    name: Left
    mode: input
    active: low
  '40':
    name: I2S Data
install:
  'devices':
  - 'i2s'
-->
# Picade X HAT

Picade X HAT supercedes Picade HAT, providing push-in headers for 10 arcade buttons and a joystick.

It also includes a digital to analog audio converter and amplifier which outputs to a single push-fit speaker terminal.

All button inputs should be configured with their corresponding internal pull-ups. Buttons should be wired between an input and ground.

## Features

* 10 button terminals
* 4 terminals for joystick
* Stereo audio combined for a single speaker
* Support for an external power button and safe power shutdown
* External power LED support
* Heck header for extra buttons and i2c connectivity

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/picadehat | bash
```
