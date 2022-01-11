<!--
---
name: Joy Bonnet
class: board
type: io
formfactor: pHAT
manufacturer: Adafruit
description: Handheld Arcade Controller for Raspberry Pi
url: https://learn.adafruit.com/adafruit-joy-bonnet-for-raspberry-pi
github: https://github.com/adafruit/adafruit-retrogame
buy: https://www.adafruit.com/product/3464
image: 'adafruit-joybonnet.png'
pincount: 40
eeprom: no
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '15':
    name: Player 1
  '16':
    name: Player 2
  '31':
    name: Button B
  '32':
    name: Button A
  '33':
    name: Button Y
  '36':
    name: Button X
  '37':
    name: Start
  '38':
    name: Select
i2c:
  '0x48':
    name: ADC
    device: ADS1015
-->
# Joy Bonnet

This add on board fits perfectly on top of your Raspberry Pi Zero (any kind) and gives you hand-held arcade controls.
The controls will act like a keyboard, for easy-to-use operation within any emulator or media player.

The Joy Bonnet works best with RetroPie/EmulationStation. You can emulate NES and MAME game controllers easily, but any emulator should work.

To install:
```bash
curl -O https://raw.githubusercontent.com/adafruit/\
Raspberry-Pi-Installer-Scripts/master/joy-bonnet.sh
sudo bash joy-bonnet.sh
```
