<!--
---
name: ADC Pi
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics UK
description: 8 channel Analogue to Digital Converter
url: https://www.abelectronics.co.uk/p/69/adc-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/viewpdf/schematic-adc-pi
buy: https://www.abelectronics.co.uk/p/69/adc-pi
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
# ADC Pi

The ADC Pi is an 8-channel 17-bit analogue to digital converter designed to work with the Raspberry Pi and other compatible single-board computers. The ADC Pi is based on two Microchip MCP3424 A/D converters, each containing 4 analogue inputs. The MCP3424 is a delta-sigma A/D converter with low noise differential inputs.

## Features

- 8 x 17-bit 0 to 5V Single Ended Inputs
- Control via the Raspberry Pi I2C port
- Stack up to 4 ADC Pi boards on a single Raspberry Pi
- Jumper selectable I2C addresses (0x68 to 0x6F)
- Buffered 5V I2C port
- Based on the MCP3424 from Microchip Technologies Inc
- Single Ended full-scale range of 5.0V
- On-board 2.048V reference voltage (Accuracy  ± 0.05%, Drift: 15 ppm/°C)
- On-Board Programmable Gain Amplifier (PGA): Gains of 1, 2, 4 or 8
- Programmable Data Rate Options:
   - 3.75 SPS (17 bits)
   - 15 SPS (15 bits)
   - 60 SPS (13 bits)
   - 240 SPS (11 bits)
- One-Shot or Continuous Conversion Options

Python, MicroPython, C, C++, Node.js and .Net Core libraries are available on GitHub.
