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

* Audio de alta calidad – 348kHz / 32bit
* Incluye DAC y amplificador
* Salidas RCA (opcional) y jack de 3.5mm
* Control de volumen mediante hardware y software con Raspberry Pi
* Alimentado mediante el pin GPIO de Raspberry Pi
* Receptor infrarrojo opcional con GPIO25
* Los pones GPIO que no se usen son accesibles
