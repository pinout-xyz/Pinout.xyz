<!--
---
name: Amp Zero
class: board
type: audio
formfactor: pHAT
manufacturer: JustBoom
description: The JustBoom Amp Zero is a high quality audio amplifier designed specifically for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-amp-zero-phat/
buy: https://www.justboom.co/product/justboom-amp-zero-phat/
image: 'justboom-amp-zero.png'
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
  '15':
    name: Soft Mute
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
-->
#Amp Zero

* Full high quality audio – 192kHz / 32bit
* 2 x 40 Watt peak output at 4 ohms (2 x 20 Watt RMS)
* Includes both a DAC and power amplifier
* Back-powers the Raspberry Pi so only one power supply required
* Hardware and software volume control from your Raspberry Pi
* Optional IR receiver via GPIO25
