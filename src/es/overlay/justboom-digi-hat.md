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
  '0x3B':
    name: Digital Interface Transceiver
    device: WM8804G
-->
#Digi HAT

* Interfaz S/PDIF de salida dedicada, compatible con 192kHz / 24bit
* Salida de sonido digital mediante conector óptico (TOSLINK) o coaxial (RCA electrical)
* Pocas variaciones, salida digital bit perfecta
* Transformador a la salida para aislamiento galvánico
* Control de volumen mediante hardware y software con Raspberry Pi
* Alimentado mediante el pin GPIO de Raspberry Pi
* Receptor infrarrojo opcional con GPIO25
* Los pones GPIO que no se usen son accesibles
