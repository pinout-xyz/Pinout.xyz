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
-->
#Speaker Bonnet

El Speaker Bonnet (Gorro parlante) es un amplificador estéreo que se adapta al Raspberry Pi. Utiliza un bus I2S para mayor claridad en el sonido. Los datos digitales entran directo al amplificador por lo que no hay estática como con un enchufe de audífonos. Funciona con cualquier Raspberry Pi con conector 2x20 - A+, B+, Zero, Pi 2, Pi 3.

Una vez soldado, solo conecte un parlante entre 4Ω y 8Ω a los bloques terminal o unos parlantes Adafruit al conector JST.

Para instalar:

```bash
curl -sS https://raw.githubusercontent.com/adafruit/\
Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
```
