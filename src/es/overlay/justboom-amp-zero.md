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
#Amp Zero

* Audio de alta calidad – 192kHz / 32bit
* Máxima salida 2 x 40 Watt y 4 ohms (2 x 20 Watt RMS)
* Incluye DAC y amplificador
* Retroalimenta la Raspberry Pi a 2.5A por lo que sólo se necesita una fuente de alimentación
* Control de volumen mediante hardware y software con Raspberry Pi
* Receptor infrarrojo opcional con GPIO25
