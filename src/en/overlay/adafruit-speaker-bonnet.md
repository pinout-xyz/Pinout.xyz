<!--
---
name: Speaker Bonnet
class: board
type: audio
formfactor: pHAT
manufacturer: Adafruit
description: 3W Stereo Amplifier Bonnet for Raspberry Pi
url: https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi
schematic: https://learn.adafruit.com/assets/37882
buy: https://www.adafruit.com/products/3346
image: 'adafruit-speaker-bonnet.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
pin:
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
-->
#Speaker Bonnet

The Speaker Bonnet is a 3W stereo amplifier add-on for the Raspberry Pi. It uses I2S, so you get really crisp audio. The digital data goes right into the amplifier so there's no static like you hear from the headphone jack. It works with any and all Raspberry Pi computers with a 2x20 connector - A+, B+, Zero, Pi 2, Pi 3.

Once soldered just plug in any 4Ω to 8Ω speakers through the terminal blocks or Adafruit’s speaker set through the JST.

To install:
```bash
curl -sS https://raw.githubusercontent.com/adafruit/\
Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
```
