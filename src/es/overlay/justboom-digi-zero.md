<!--
---
name: Digi Zero
class: board
type: audio
formfactor: pHAT
manufacturer: JustBoom
description: The JustBoom Digi Zero is a high resolution digital audio output add on board for the Raspberry Pi.
url: https://www.justboom.co/product/justboom-digi-zero-phat/
buy: https://www.justboom.co/product/justboom-digi-zero-phat/
image: 'justboom-digi-zero.png'
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
#Digi Zero

* Interfaz S/PDIF de salida dedicada, compatible con 192kHz / 24bit
* Salida de sonido digital mediante conector óptico (TOSLINK) o coaxial (RCA electrical)
* Pocas variaciones, salida digital bit perfecta
* Transformador a la salida para aislamiento galvánico
* Control de volumen mediante hardware y software con Raspberry Pi
* Alimentado mediante el pin GPIO de Raspberry Pi
* Receptor infrarrojo opcional con GPIO25
* Los pones GPIO que no se usen son accesibles
