<!--
---
name: DAC Zero
class: board
type: audio
formfactor: pHAT
manufacturer: JustBoom
description: The JustBoom DAC Zero is a plug and play, high resolution, digital-to-analog converter for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-dac-zero-phat/
buy: https://www.justboom.co/product/justboom-dac-zero-phat/
image: 'justboom-dac-zero.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: BCKL (Bit Clock)
    mode: i2s
  '22':
    name: IR Receiver
  '23':
    name: Rotary Encoder
  '24':
    name: Rotary Encoder
  '35':
    name: LRCK (Left/Right Clock)
    mode: i2s
  '40':
    name: DOUT
    mode: i2s
-->
#DAC Zero

* Full high quality audio – 384kHz / 32bit
* Includes both a DAC and headphone amplifier
* Line-level RCA (optional) and headphone amplified 3.5mm jack outputs
* Hardware and software volume control from your Raspberry Pi
* Powered by the Raspberry Pi GPIO header
* Optional IR receiver via GPIO25
* Unused GPIO pins still accessible via unpopulated extension header
