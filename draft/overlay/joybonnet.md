<!--
---
name: Joy Bonnet
class: board
type: io
formfactor: phat
manufacturer: Adafruit
description: Handheld Arcade Controller for Raspberry Pi
url: https://learn.adafruit.com/adafruit-joy-bonnet-for-raspberry-pi
github: https://github.com/adafruit/adafruit-retrogame
buy: https://www.adafruit.com/product/3464
image: 'joybonnet.png'
pincount: 40
eeprom: no
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
  '3'
    mode: i2c    
  '5': 
    mode:i2c   
  '38': 
    name: Select 
  '37': 
    name: Start 
  '15':
    name: Player1
  '16':   
    name: Player2 
  '32':  
    name: A
  '33':
    name: Y
  '36':
    name: X
  '31':
    name: B 
  
    
i2c:
  
  '0x48':
    name: ADC
    device: ADS1015
-->
# Joy Bonnet


This add on board fits perfectly on top of your Raspberry Pi Zero (any kind) and gives you hand-held arcade controls. 
Once you install our script onto your Pi, the controls will act like a keyboard, for easy use with any emulator or media player.


The Joy Bonnet works best with RetroPie/EmulationStation. On a Pi Zero you can emulate NES and MAME game but other emulators that 
don't require more than 1GHz speeds will work OK too, e.g. a N64 emulator won't work, it needs way more power!


To install:
```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/joy-bonnet.sh
sudo bash joy-bonnet.sh
```
