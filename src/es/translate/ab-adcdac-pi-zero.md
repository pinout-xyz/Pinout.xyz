<!--
---
name: ADC-DAC Pi Zero
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics UK
description: 2 channel Analogue to Digital Converter and 2 channel Digital to Analogue Converter
url: https://www.abelectronics.co.uk/p/74/adc-dac-pi-zero-raspberry-pi-adc-and-dac-expansion-board
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-adc-dac-pi-zero.pdf
buy: https://www.abelectronics.co.uk/p/74/adc-dac-pi-zero-raspberry-pi-adc-and-dac-expansion-board
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

ADC-DAC Pi Zero es un convertidor analógico a digital de 2 canales y 12 bits y un convertidor digital a analógico de 2 canales y 12 bits diseñado para funcionar con la Raspberry Pi. Diseñado para la mismo tamaño que la Raspberry Pi Zero, ADC-DAC Pi Zero también es compatible con los modelos Raspberry Pi de tamaño completo.

ADC-DAC Pi Zero se basa en el convertidor A / D Microchip MCP3202 que contiene 2 entradas analógicas con resolución de 12 bits con un DAC de 12 bits Microchip MCP4822 de doble canal con referencia de voltaje interno.

Velocidad máxima de muestreo de ADC: 100 k muestras / seg.

Velocidad máxima de muestra de ADC en Python: 12,000 muestras por segundo.

Python, C, C ++, Node.js y las bibliotecas IOT de Windows 10 están disponibles en GitHub.
