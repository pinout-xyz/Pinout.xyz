<!--
---
name: Digi HAT
class: board
type: audio
formfactor: HAT
manufacturer: JustBoom
description: The JustBoom Digi HAT is a high resolution digital audio output add on board for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-digi-hat/
buy: https://www.justboom.co/product/justboom-digi-hat/
image: 'justboom-digi-hat.png'
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
  '35':
    name: LRCK (Left/Right Clock)
    mode: i2s
  '40':
    name: DOUT
    mode: i2s
-->
#Digi HAT

* Dedicated S/PDIF output interface chip supports up to 192kHz / 24bit
* Digital audio output over either optical (TOSLINK) or coaxial (RCA electrical) connectors
* Low jitter, bit perfect digital output
* Output transformer for galvanic isolation
* Software volume control from your Raspberry Pi
* Powered by the Raspberry Pi GPIO header
* Optional IR receiver via GPIO25
* All Raspberry Pi GPIO pins still accessible via 40pin unpopulated 
