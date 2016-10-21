<!--
---
name: IO Pi Plus
class: board
type: io
formfactor: HAT
manufacturer: AB Electronics
description: 32 Channel Digital Expansion Board
url: https://www.abelectronics.co.uk/p/54/IO-Pi-Plus
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/54/IO-Pi-Plus
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
    name: MCP23017
    device: MCP23017
  '0x21':
    name: MCP23017
    device: MCP23017
-->
#IO Pi Plus

IO Pi Plus es una placa de expansión digital de 32 canales diseñada para funcionar con Raspberry Pi A+, B+ y 2 modelo B. La placa está basada en el I/O expander de 16-bit MCP23017 de Microchip Technology Inc.

La placa incluye dos MCP23017 que permiten conectar hasta 32 entradas o salidas digitales a Raspberry Pi. IO Pi Plus se alimenta a partir de los puertos GPIO de Raspberry Pi y permite además conectar otras placas.

##Especificaciones

-  32 entradas/salidas digitables
-  Control mediante el puerto I2C de Raspberry Pi
-  Acopla hasta cuatro placas en una sola Raspberry Pi
-  Selección de dirección I2C
-  Entrada de 5V externa con cable aislante
-  Basado en MCP23017 de Microchip Technologies Inc
-  Salidas configurables como active-high, active-low o open-drain
-  INTA e INTB configurables para trabajar independientemente o en conjunto
-  Fuente configurable para registrar cambios de pines o de valores predeterminados
-  Registro de inversión de polaridad para configurar la polaridad del puerto de entrada

Librerías Arduino, C, Windows 10 IOT, Python 2 and Python 3 disponibles en GitHub.
