<!--
---
name: DAC Pro
class: board
type: audio
formfactor: HAT
manufacturer: Raspberry Pi
description: A high-fidelity I2S DAC HAT with phono line and balanced XLR output
url: https://www.raspberrypi.com/products/dac-pro/
image: 'raspberrypi-dac-pro.png'
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
    name: Mute/Unmute
    description: Amplifier only (optional)
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
    device: pcm5242
-->
# DAC Pro

The DAC Pro uses a Texas Instruments PCM5242 to deliver variable-level analogue audio (0-2V RMS) to a pair of phono/RCA connectors, and drives headphones up to 80/90 ohm through a dedicated headphone amplifier and 3.5mm jack. Two three-pin headers, P7 and P9, expose a differential/balanced output (0-4V RMS) for the optional XLR board, which mounts above the Raspberry Pi's USB and Ethernet ports.

The board is powered from the Raspberry Pi through the GPIO header, and re-exposes the header so that other boards and sensors can be stacked above it. The I2S and EEPROM pins are for its exclusive use; the I2C bus can be shared.

GPIO22 (amplifier mute), GPIO23/24 (rotary encoder), GPIO25 (IR receiver) and GPIO27 (encoder switch) are broken out for optional use, and are free for other purposes if those parts are not fitted and enabled in software.

The DAC Pro is electrically equivalent to the IQaudIO Pi-DAC PRO. The green Raspberry Pi boards carry an EEPROM that Raspberry Pi OS detects and configures automatically; the older black IQaudIO boards need a dtoverlay line in config.txt.
