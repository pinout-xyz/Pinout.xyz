<!--
---
name: I2C Switch
class: board
type: io
formfactor: pHAT
manufacturer: AB Electronics UK
description: 4-channel bidirectional I2C switch
url: https://www.abelectronics.co.uk/p/84/i2c-switch
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/viewpdf/schematic-i2cswitch
buy: https://www.abelectronics.co.uk/p/84/i2c-switch
image: 'ab-i2c-switch.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
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
  '0x70':
    alternate: [ '0x71', '0x72', '0x73', '0x74', '0x75', '0x76', '0x77' ]
    name: PCA9546A
    device: PCA9546A
-->
# I2C Switch

The I2C Switch from AB Electronics UK is a 4-channel bidirectional I2C switch controlled via the I2C bus. It is designed for all Raspberry Pi models and other compatible single-board computers with the 40-pin GPIO connector. Using our mounting kit pack, the I2C Switch can be securely fitted to your Raspberry Pi.  

The I2C Switch is based on a PCA9546A controller from NXP. The PCA9546A provides quad bi-directional communication between the I2C port on the Raspberry Pi and any attached I2C devices. Each channel can be individually enabled or disabled, allowing you to connect I2C devices that share the same address to your Raspberry Pi.  

Powered through the host Raspberry Pi using the GPIO port and extended pins on the GPIO connector allowing you to stack the I2C Switch along with other expansion boards.

## Features

-  4 I2C channels  
-  Channel selection via I2C-bus, in any combination  
-  3 address pins allowing up to 8 devices on the I2C bus  
-  Allows voltage level translation between 2.7 V, 3.3 V and 5 V buses  
-  0 Hz to 400 kHz clock frequency  


Python, MicroPython C, C++ and Node.js libraries are available on GitHub.
