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
# IO Pi Plus

The IO Pi Plus is a 32 channel digital expansion board designed for use on the Raspberry Pi. The board is based around the MCP23017 16-bit I/O expander from Microchip Technology Inc. 

A pair of MCP23017 expanders are included on the board allowing you to connect up to 32 digital inputs or outputs to the Raspberry Pi.  The IO Pi Plus Expander is powered through the host Raspberry Pi using the GPIO port and extended pins on the GPIO connector allow you to stack the IO Pi Plus along with other expansion boards.

## Features

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

Python, C, C++, Node.js and Windows 10 IOT libraries are available on GitHub.
