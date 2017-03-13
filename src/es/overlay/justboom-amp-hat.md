<!--
---
name: Amp HAT
class: board
type: audio
formfactor: HAT
manufacturer: JustBoom
description: The JustBoom Amp HAT is a high quality audio amplifier designed specifically for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-amp-hat/
buy: https://www.justboom.co/product/justboom-amp-hat/
image: 'justboom-amp-hat.png'
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
i2c:
  '0x4D':
    name: Amplifier
    device: TAS5756M
-->
#Amp HAT

* Audio de alta calidad – 192kHz / 32bit
* Máxima salida 2 x 55 Watt y 8 ohms (2 x 30 Watt RMS)
* Incluye DAC y amplificador
* Retroalimenta la Raspberry Pi a 2.5A por lo que sólo se necesita una fuente de alimentación
* Control de volumen mediante hardware y software con Raspberry Pi
* Control de ganancia incorporado con el jumper J5
* Silencia/permite el sonido con GPIO22 (sáltalo con jumper J4)
* Receptor infrarrojo opcional con GPIO25
* Los pones GPIO que no se usen son accesibles
