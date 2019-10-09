<!--
---
name: ADC Pi
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics UK
description: 8 channel Analogue to Digital Converter
url: https://www.abelectronics.co.uk/p/69/adc-pi-raspberry-pi-analogue-to-digital-converter
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-adc-pi.pdf
buy: https://www.abelectronics.co.uk/p/69/adc-pi-raspberry-pi-analogue-to-digital-converter
image: 'ab-adc-pi.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '14':
  '20':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x68':
    alternate: [ '0x69', '0x6A', '0x6B', '0x6C', '0x6D', '0x6E', '0x6F' ]
    name: MCP3424
    device: MCP3424
  '0x69':
    alternate: [ '0x68', '0x6A', '0x6B', '0x6C', '0x6D', '0x6E', '0x6F' ]
    name: MCP3424
    device: MCP3424
-->
#ADC Pi

ADC Pi es un convertidor analógico a digital de 8 canales y 17 bits diseñado para funcionar con la Raspberry Pi. El ADC Pi se basa en dos convertidores A / D Microchip MCP3424, cada uno de los cuales contiene 4 entradas analógicas. El MCP3424 es un convertidor A / D delta-sigma con entradas diferenciales de bajo ruido.

##Características

- 8 x 17 bits de 0 a 5 V entradas de terminación única
- Control a través del puerto Raspberry Pi I2C
- Combina hasta 4 placas ADC Pi en una sola Raspberry Pi
- Direcciones I2C seleccionables por puente (0x68 a 0x6F)
- Puerto I2C de 5V protegido
- Basado en el MCP3424 de Microchip Technologies Inc
- Rango de escala completa de un solo extremo de 5.0V
- Voltaje de referencia incorporado de 2.048 V (precisión ± 0.05%, deriva: 15 ppm / ° C)
- Amplificador de ganancia programable a bordo (PGA): ganancias de 1, 2, 4 u 8
- Opciones de velocidad de datos programables:
    - 3.75 SPS (17 bits)
    - 15 SPS (15 bits)
    - 60 SPS (13 bits)
    - 240 SPS (11 bits)
- Opciones de conversión única o continua

Python, C, C ++, Node.js y las bibliotecas IOT de Windows 10 están disponibles en GitHub.
