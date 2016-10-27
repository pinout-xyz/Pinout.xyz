<!--
---
name: Pi-DigiAMP+
class: board
type: audio
formfactor: HAT
manufacturer: IQaudIO
description: A combined DAC and 35w amplifier board
url: http://www.iqaudio.co.uk/home/9-pi-digiamp-0712411999650.html
buy: http://www.iqaudio.co.uk
image: 'iqaudio-pi-digiamp.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: I2S
  '15':
    name: Mute/Unmute
  '16':
    name: Rotary Encoder
    description: (optional)
  '18':
    name: Rotary Encoder
    description: (optional)
  '22':
    name: IR Sensor
    description: (optional)
  '35':
    name: I2S
  '38':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2c'
-->
#Pi-DigiAMP+

The Pi-DigiAMP+ is an add-on board that includes a Digital to Analog Converter (DAC) and powerful 35w stereo amplifier. If you want to turn your Raspberry Pi into a working Hi Fi stereo, just add speakers and you're off.

You can use GPIO25 to connect an IR sensor and GPIO23/24 for a rotary encoder. Both of these parts are optional, but are broken out on the Pi-DAC+ for convenient access.
Note: pins reserved for the rotary encoder and IR sensor can be used for other purposes if those add-ons have not been fitted and enabled by software.
