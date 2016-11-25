<!--
---
name: JustBoom DAC pHAT
class: board
type: audio
formfactor: pHAT
manufacturer: JustBoom
description: The JustBoom DAC pHAT is a plug and play, high resolution, digital-to-analog converter for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-dac-hat/
github:
schematic:
buy: https://www.pi-supply.com/product/justboom-dac-hat/?utm_source=JustBoom+Site&utm_medium=Link&utm_campaign=JustBoom+Referrals&utm_content=DAC_HAT_Product_Link
image: 'justboom-dac-phat.png'
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
#JustBoom DAC pHAT
* Full high quality audio – 384kHz / 32bit
* Includes both a DAC and headphone amplifier
* Line-level RCA (optional) and headphone amplified 3.5mm jack outputs
* Hardware and software volume control from your Raspberry Pi
* Powered by the Raspberry Pi GPIO header
* Optional IR receiver via GPIO25
* Unused GPIO pins still accessible via unpopulated extension header
