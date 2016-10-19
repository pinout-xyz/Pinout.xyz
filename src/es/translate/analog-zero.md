<!--
---
name: Analog Zero
class: board
type: adc
formfactor: pHAT
manufacturer: RasPiO
description: A 10-bit 8-channel ADC for Raspberry Pi
url: http://rasp.io/analogzero/
github: https://github.com/raspitv/analogzero
buy: http://rasp.io/analogzero/
image: 'analog-zero.png'
pincount: 40
eeprom: no
power: 3v3
pin:
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
install:
  'devices':
    - 'spi'
-->
#Analog Zero

Analog Zero de RasPiO ofrece una manera fácil, compacta y barata de añadir ocho canales analógicos a Raspberry Pi. Analog Zero de RasPiO utiliza el conversor analógico a digital MCP3008. Es un ADC de 8  canales, 10-bit controlado por SPI.

Con Analog Zero de RasPiO puedes:

* Leer 8 entradas analógicas simultáneamente
* Hacer una estación meteorológica
* Hacer un termómetro digital
* Hacer un potenciómetro
* Usar los diales del potencómetro para controlar y mostrar
* Leer sensores analógicos o voltajes
* Hacer tu propio dispositivo incrustado con el mínimo espacio
