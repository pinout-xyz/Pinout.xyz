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

The IO Pi Plus is a 32 channel digital expansion board designed for use on the Raspberry Pi. The board is based around the MCP23017 16-bit I/O expander from Microchip Technology Inc. 

A pair of MCP23017 expanders are included on the board allowing you to connect up to 32 digital inputs or outputs to the Raspberry Pi.  The IO Pi Plus Expander is powered through the host Raspberry Pi using the GPIO port and extended pins on the GPIO connector allow you to stack the IO Pi Plus along with other expansion boards.

##Features

-  32 Digital Inputs/Outputs
-  Control via the Raspberry Pi I2C port
-  Stack up to 4 IO Pi boards on a single Raspberry Pi
-  Jumper selectable I2C addresses
-  External 5V Input with isolation jumper
-  Based on the MCP23017 from Microchip Technologies Inc
-  Configurable interrupt output pins - Configurable as active-high, active-low or open-drain
-  INTA and INTB can be configured to operate independently or together
-  Configurable interrupt source  - Interrupt-on-change from configured register defaults  or pin changes
-  Polarity Inversion register to configure the polarity of the input port data

Arduino, C, Node.js, Windows 10 IOT, Python 2 and Python 3 libraries are available on GitHub.