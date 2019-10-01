<!--
---
name: IO Pi Plus
class: board
type: io
formfactor: Custom
manufacturer: AB Electronics UK
description: 32 Channel Digital Expansion Board
url: https://www.abelectronics.co.uk/p/54/io-pi-plus
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-iopiplus-2-1.pdf
buy: https://www.abelectronics.co.uk/p/54/io-pi-plus
image: 'ab-io-pi-plus.png'
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
i2c:
  '0x20':
    alternate: [ '0x21', '0x22', '0x23', '0x24', '0x25', '0x26', '0x27' ]
    name: MCP23017
    device: MCP23017
  '0x21':
    alternate: [ '0x20', '0x22', '0x23', '0x24', '0x25', '0x26', '0x27' ]
    name: MCP23017
    device: MCP23017
-->
#IO Pi Plus

IO Pi Plus es una placa de expansión digital de 32 canales diseñada para su uso en Raspberry Pi. La placa se basa en el expansor de E / S de 16 bits MCP23017 de Microchip Technology Inc.

Se incluyen un par de expansores MCP23017 en la placa que le permiten conectar hasta 32 entradas o salidas digitales a la Raspberry Pi. IO Pi Plus Expander se alimenta a través de Raspberry Pi utilizando el puerto GPIO y los pines extendidos en el conector GPIO le permiten combinar IO Pi Plus junto con otras placas de expansión.

##Características

- 32 entradas / salidas digitales
- Control a través del puerto Raspberry Pi I2C
- Combina hasta 4 placas IO Pi en una sola Raspberry Pi
- Direcciones I2C seleccionables por puente
- Entrada externa de 5 V con puente de aislamiento
- Basado en el MCP23017 de Microchip Technologies Inc
- Pines de salida de interrupción configurables - Configurable como activo-alto, activo-bajo o drenaje abierto
- INTA e INTB se pueden configurar para operar de manera independiente o en conjunto
- Fuente de interrupción configurable - Interrupción al cambiar desde valores predeterminados de registro configurados o cambios de pin
- Registro de inversión de polaridad para configurar la polaridad de los datos del puerto de entrada

Python, C, C ++, Node.js y las bibliotecas IOT de Windows 10 están disponibles en GitHub.
