<!--
---
name: "Pi-DAC+"
manufacturer: IQaudIO
buy: http://www.iqaudio.co.uk
description: An I2S digital to analog audio converter HAT for the Pi
install:
  'devices':
    - 'i2c'
pincount: 40
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  12:
    name: I2S
  15:
    name: Mute/Unmute
    description: Pi-AMP+ only (optional) 
  16:
    name: Rotary Encoder
    description: (optional) 
  18:
    name: Rotary Encoder
    description: (optional) 
  22:
    name: IR Sensor
    description: (optional) 
  35:
    name: I2S
  38:
    name: I2S
  40:
    name: I2S
-->
#IQaudIO Pi-DAC+

The Pi-DAC+ takes the digital audio signals (I2S) from the Raspberry Pi and through the
onboard Texas Instruments PCM5122 DAC delivers variable output (hardware volume
control) analog audio to the Pi-DAC+ Phono connectors. The PI-DAC+ also, via the
Texas Instruments TPA6133A headphone amp, supports the direct use of headphones via
the Pi-DAC+ 3.5mm audio jack.

The Pi Dac uses GPIO22 to mute/unmute the Pi-AMP+.

You can use GPIO25 to connect an IR sensor and GPIO23/24 for a rotary encoder. Both of
these parts are optional, but are broken out on the Pi-DAC+ for convenient access.

Note: pins marked as optional can be used for general purpose if those add-ons are not enabled by software.
