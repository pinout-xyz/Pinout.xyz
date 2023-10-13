<!--
---
name: ADC Differential Pi
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics UK
description: 8 channel Analogue to Digital Converter
url: https://www.abelectronics.co.uk/p/65/adc-differential-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/viewpdf/schematic-adc-differential-pi
buy: https://www.abelectronics.co.uk/p/65/adc-differential-pi
image: 'ab-adc-differential-pi.png'
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
  '0x68':
    alternate: [ '0x69', '0x6A', '0x6B', '0x6C', '0x6D', '0x6E', '0x6F' ]
    name: MCP3424
    device: MCP3424
  '0x69':
    alternate: [ '0x68', '0x6A', '0x6B', '0x6C', '0x6D', '0x6E', '0x6F' ]
    name: MCP3424
    device: MCP3424
-->
# ADC Differential Pi

The ADC Differential Pi is an 8-channel 18-bit analogue to digital converter designed to work with the Raspberry Pi and other compatible single-board computers. The ADC Differential Pi is based on two Microchip MCP3424 A/D converters, each containing 4 analogue inputs. The MCP3424 is a delta-sigma A/D converter with low noise differential inputs.

## Features

- 8 x 18-bit differential inputs
- Control via the Raspberry Pi I2C port
- Stack up to 4 ADC Differential Pi boards on a single Raspberry Pi
- Jumper selectable I2C addresses (8 choices)
- Buffered 5V I2C port
- Based on the MCP3424 from Microchip Technologies Inc
- Input range of ±2.048V
- On-board 2.048V reference voltage (Accuracy  ± 0.05%, Drift: 15 ppm/°C)
- On-Board Programmable Gain Amplifier (PGA): Gains of 1, 2, 4 or 8
- Programmable Data Rate Options:
    - 3.75 SPS (18 bits)
    - 15 SPS (16 bits)
    - 60 SPS (14 bits)
    - 240 SPS (12 bits)
- One-Shot or Continuous Conversion Options

Python, MicroPython, C, C++, Node.js and .Net Core libraries are available on GitHub.
