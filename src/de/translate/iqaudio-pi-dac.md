<!--
---
name: Pi-DAC+
class: board
type: audio
formfactor: HAT
manufacturer: IQaudIO
description: An I2S digital to analog audio converter HAT for the Pi
url: http://www.iqaudio.co.uk/audio/8-pi-dac-0712411999650.html
buy: http://www.iqaudio.co.uk
image: 'iqaudio-pi-dac.png'
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
    description: Pi-AMP+ only (optional)
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
#Pi-DAC+

The Pi-DAC+ takes the digital audio signals (I2S) from the Raspberry Pi and through the
onboard Texas Instruments PCM5122 DAC delivers variable output (hardware volume
control) analog audio to the Pi-DAC+ Phono connectors. The PI-DAC+ also, via the
Texas Instruments TPA6133A headphone amp, supports the direct use of headphones via
the Pi-DAC+ 3.5mm audio jack.

The Pi-DAC+ uses GPIO22 to mute/unmute the Pi-AMP+.

You can use GPIO25 to connect an IR sensor and GPIO23/24 for a rotary encoder. Both of
these parts are optional, but are broken out on the Pi-DAC+ for convenient access.

Note: pins reserved for the rotary encoder and IR sensor can be used for other purposes if those add-ons have not been fitted and enabled by software.
