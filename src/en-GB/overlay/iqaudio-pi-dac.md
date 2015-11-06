<!--
---
name: "IQaudIO Pi-DAC+"
description: Program Arduino with Raspberry Pi SPI
pin:
  1:
  2:
  3:
  4:
  5:
  6:
  9:
  12:
    name: I2S
  14:
  16:
    name: Rotary Encoder
  18:
    name: Rotary Encoder
  22:
    name: Mute/Unmute
  25:
    name: IR Sensor
  27:
  28:
  35:
    name: I2S
  38:
    name: I2S
  39:
  40:
    name: I2S
-->
#IQaudIO Pi-DAC+

The Pi-DAC+ takes the digital audio signals (I2S) from the Raspberry Pi and through the
onboard Texas Instruments PCM5122 DAC delivers variable output (hardware volume
control) analog audio to the Pi-DAC+’s Phono connectors. The PI-DAC+ also, via the
Texas Instruments TPA6133A headphone amp, supports the direct use of headphones via
the Pi-DAC+’s 3.5mm audio jack.

The Pi Dac uses GPIO22 to mute/unmute the Pi-AMP+.

You can use GPIO25 to connect an IR sensor and GPIO23/24 for a rotary encoder. Both of
these parts are optional, but are broken out on the Pi-DAC+ for convinient access.
