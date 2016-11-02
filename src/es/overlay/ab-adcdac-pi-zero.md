<!--
---
name: ADC-DAC Pi Zero
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics
description: 2 channel Analogue to Digital Converter and 2 channel Digital to Analogue Converter
url: https://www.abelectronics.co.uk/p/74/ADC-DAC-Pi-Zero-Raspberry-Pi-ADC-and-DAC-expansion-board
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/stock/raspberrypi/adcdacpizero/adcdacpizero-schematic.pdf
buy: https://www.abelectronics.co.uk/p/74/ADC-DAC-Pi-Zero-Raspberry-Pi-ADC-and-DAC-expansion-board
image: 'ab-adcdac-pi-zero.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
install:
  'devices':
    - 'spi'
-->
#ADC-DAC Pi Zero

ADC-DAC Pi Zero es un conversor analógico digital de 2 canales y 12 bit, además de un conversor digital a analógico de las mismas especificaciones, diseñado para funcionar con Raspberry Pi. Pese a ser del mismo tamaño que Pi Zero, funciona con cualquier Raspberry Pi.

ADC-DAC Pi Zero está basada ene l Microchip MCP3202 A/D, con dos entradas analógicas de 12 bit de resolución y un Microchip MCP4822 de doble canal 12-bit DAC con referencia de voltaje interna.

Máx frecuencia de muestreo de ADC: 100 kmuestras/seg

Más frecuencia de muestreo ADC en Python: 12000 muestras/s

Librerias Arduino, C, Node.js, Windows 10 IOT, Python 2 y Python 3 disponibles en GitHub.
