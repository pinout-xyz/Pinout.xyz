<!--
---
name: DAC HAT
class: board
type: audio
formfactor: HAT
manufacturer: JustBoom
description: The JustBoom DAC HAT is a plug and play, high resolution, digital-to-analog converter for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-dac-hat/
buy: https://www.justboom.co/product/justboom-dac-hat/
image: 'justboom-dac-hat.png'
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
    name: BCKL (Bit Clock)
    mode: i2s
  '16':
    name: Rotary Encoder
  '18':
    name: Rotary Encoder
  '22':
    name: IR Receiver
  '35':
    name: LRCK (Left/Right Clock)
    mode: i2s
  '40':
    name: DOUT
    mode: i2s
i2c:
  '0x4D':
    name: DAC
    device: PCM5122
-->
#DAC HAT

* Full high quality audio – 384kHz / 32bit
* Includes both a DAC and headphone amplifier
* Line-level RCA and headphone amplified 3.5mm jack outputs
* Hardware and software volume control from your Raspberry Pi
* Powered by the Raspberry Pi GPIO header
* Optional IR receiver via GPIO25
* Compatible with the JustBoom Amp which can easily stack on top of the DAC HAT
* All Raspberry Pi GPIO pins still accessible via 40pin unpopulated
