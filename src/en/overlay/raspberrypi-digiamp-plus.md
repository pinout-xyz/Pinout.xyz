<!--
---
name: DigiAMP+
class: board
type: audio
formfactor: HAT
manufacturer: Raspberry Pi
description: An I2S DAC HAT with a 2x35w stereo amplifier for passive speakers
page_url: digiamp_plus
url: https://www.raspberrypi.com/products/digiamp-plus/
image: 'raspberrypi-digiamp-plus.png'
pincount: 40
eeprom: setup
power:
  '1':
  '2':
  '4':
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
    mode: i2s
    name: I2S BCLK
  '13':
    name: Encoder Switch
    description: (optional)
  '15':
    mode: output
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
    mode: i2s
    name: I2S LRCLK
  '38':
    mode: i2s
    name: I2S SDIN
  '40':
    mode: i2s
    name: I2S SDOUT
i2c:
  '0x4c':
    name: DAC
    device: tas5756m
-->
# DigiAMP+

The DigiAMP+ pairs a Texas Instruments TAS5756M PowerDAC with a stereo amplifier, driving two sets of screw terminals at up to 35w per channel with variable output. It is intended for traditional passive hi-fi speakers.

The DigiAMP+ must be powered from an external 12-24V DC supply through a 5.5mm x 2.5mm centre-positive barrel connector, and delivers 5.1V at 2.5A back to the Raspberry Pi over the GPIO header. Do not apply power to the Raspberry Pi's own power input at the same time. P5 is an alternative power input for hard-wired installations, and observes polarity.

The amplifier is muted at power-on, with the mute LED illuminated. Software drives GPIO22 to control the mute state and the LED. GPIO23/24 (rotary encoder), GPIO25 (IR receiver) and GPIO27 (encoder switch) are broken out for optional use.

The DigiAMP+ is electrically equivalent to the IQaudIO Pi-DigiAMP+. The green Raspberry Pi boards carry an EEPROM that Raspberry Pi OS detects and configures automatically; the older black IQaudIO boards need a dtoverlay line in config.txt.
