<!--
---
name: Codec Zero
class: board
type: audio
formfactor: pHAT
manufacturer: Raspberry Pi
description: A Zero-sized audio codec board with a built-in mic and speaker driver
url: https://www.raspberrypi.com/products/codec-zero/
image: 'raspberrypi-codec-zero.png'
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
    mode: input
    name: Button
  '16':
    mode: output
    name: Green LED
  '18':
    mode: output
    name: Red LED
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
  '0x1a':
    name: Codec
    device: da7212
-->
# Codec Zero

The Codec Zero is a Raspberry Pi Zero-sized board carrying a Dialog Semiconductor DA7212 codec, which handles bi-directional I2S audio at 24-bit and sample rates from 8kHz to 96kHz. Unlike the DAC boards it is a clock consumer, driving the I2S clocks itself.

Inputs are a built-in MEMS microphone (Mic2), a 3.5mm socket for a mono electret microphone that automatically disables the MEMS mic on insertion, and a stereo auxiliary input on P1 at up to 1V RMS. Outputs are a stereo auxiliary output on P2 and a screw terminal for a single 1.2W 8 ohm mono speaker. The codec provides analogue and digital mixing, automatic level control and a five-band EQ.

A tactile button on GPIO27 and green and red LEDs on GPIO23 and GPIO24 are fitted to the board. There is no mute pin, rotary encoder or IR receiver.

The Codec Zero is electrically equivalent to the black IQaudIO codec board. The green Raspberry Pi boards carry an EEPROM that Raspberry Pi OS detects and configures automatically; the older black IQaudIO boards need a dtoverlay line in config.txt.
