<!--
---
name: IO Pi Zero
class: board
type: io
formfactor: pHAT
manufacturer: AB Electronics
description: 16 Channel Digital Expansion Board
url: https://www.abelectronics.co.uk/p/71/IO-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/71/IO-Pi-Zero
image: 'ab-io-pi-zero.png'
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
    name: MCP23017
    device: MCP23017
-->
#IO Pi Zero

IO Pi Zero es una placa de expansión digital de 16 canales diseñada para Raspberry Pi Zero. Está basada en el expansor I/o de 16-bit MCP23017 de Microchip Technology Inc.

IO Pi Zero Expander se alimenta a través del puerto GPIO de Raspberry Pi y además permite usar los puertos GPIO, pudiendo acoplarse con otras placas.

##Especificaciones

-  16 entradas/salidas digitales
-  Control a través del puerto I2C de Raspberry Pi
-  Permite acoplar hasta 8 placas IO en una sola Raspberry Pi
-  Dirección I2C seleccionable
-  Entrada de 5V externa con aislamiento
-  Basada en MCP23017 de Microchip Technologies Inc
-  Puertos de salida configurables como active-high, active-low o open-drain
-  INTA e INTB configurables para trabajar independientemente o juntos
-  Interrupciones configurables
-  Registro de inversión de polaridad

Librerias Arduino, C, Node.js, Windows 10 IOT, Python 2 y Python 3 disponibles GitHub.
