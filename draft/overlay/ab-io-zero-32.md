<!--
---
name: IO Zero 32
class: board
type: io
formfactor: pHAT
manufacturer: AB Electronics UK
description: 16 Channel Digital Expansion Board
url: https://www.abelectronics.co.uk/p/86/io-zero-32
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/viewpdf/io-zero-32-schematic
buy: https://www.abelectronics.co.uk/p/86/io-zero-32
image: 'ab-zero-32.png'
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
    name: PCA9535
    device: PCA9535
-->
# IO Zero 32

The IO Zero 32 is a 32-channel digital expansion board designed for use on the Raspberry Pi and other compatible single-board computers. The board is based around the PCA9535 16-bit I/O expander from NXP. 

A pair of PCA9535 expanders are included on the board, allowing you to connect up to 32 digital inputs or outputs to the Raspberry Pi. The IO Zero 32 is powered through the host Raspberry Pi using the GPIO port, and extended pins on the GPIO connector allow you to stack the IO Zero 32 along with other expansion boards.

The I2C address bits are selectable using the onboard solder jumpers. The PCA9535 supports up to 8 different I2C addresses, so with two PCA9535 devices on each IO Zero 32, you can stack up to 4 IO Zero 32 boards on a single Raspberry Pi, giving a maximum of 128 I/O ports.

## Features

- 32 Digital Inputs/Outputs
- Control via the Raspberry Pi I2C port
- Stack up to 4 IO Zero 32 boards on a single Raspberry Pi
- Solder jumper selectable I2C addresses
- External 3.3V to 5V Voltage Input with an isolation solder jumper
- Based on the PCA9535 from NXP
- Interrupt pins - Open drain interrupt outputs trigger when an input pin changes state
- Polarity Inversion register to configure the polarity of the input port data

Python, MicroPython, C, C++ and Node.js libraries are available on GitHub.
