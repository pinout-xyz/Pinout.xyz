<!--
---
name: JustBoom Amp HAT
class: board
type: audio
formfactor: HAT
manufacturer: JustBoom
description: The JustBoom Amp HAT is a high quality audio amplifier designed specifically for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-amp-hat/
github:
schematic:
buy: https://www.pi-supply.com/product/justboom-amp-hat/?utm_source=JustBoom+Site&utm_medium=Link&utm_campaign=JustBoom+Referrals&utm_content=AMP_HAT_Product_Link
image: 'justboom-amp-hat.png'
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
    name: BCKL (Bit Clock)
    mode: i2s
  '15':
    name: Soft Mute
  '22':
    name: IR Receiver
  '23':
    name: Rotary Encoder
  '24':
    name: Rotary Encoder
  '27':
    mode: i2c
  '28':
    mode: i2c
  '35':
    name: LRCK (Left/Right Clock)
    mode: i2s
  '40':
    name: DOUT
    mode: i2s
-->
#JustBoom Amp HAT
* Full high quality audio – 192kHz / 32bit
* 2 x 55 Watt peak output at 8 ohms (2 x 30 Watt RMS)
* Includes both a DAC and power amplifier
* Back-powers the Raspberry Pi at 2.5A so only one power supply required
* Hardware and software volume control from your Raspberry Pi
* Onboard gain control using jumper J5
* Mute/enable with GPIO22 (override by using jumper J4)
* Optional IR receiver via GPIO25
* Unused GPIO pins still accessible via unpopulated extension header
