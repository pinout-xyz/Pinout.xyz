<!--
---
name: ADC Pi Zero
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics
description: 8 channel Analogue to Digital Converter
url: https://www.abelectronics.co.uk/p/69/ADC-Pi-Zero-Raspberry-Pi-Analogue-to-Digital-converter
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/69/ADC-Pi-Zero-Raspberry-Pi-Analogue-to-Digital-converter
image: 'ab-adc-pi-zero.png'
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
    name: MCP3424
    device: MCP3424
  '0x69':
    name: MCP3424
    device: MCP3424
-->
#ADC Pi Zero

The ADC Pi Zero is an 8 channel 17 bit analogue to digital converter designed to work with the Raspberry Pi Zero. The ADC Pi Zero is based on two Microchip MCP3424 A/D converters each containing 4 analogue inputs.  The MCP3424 is a delta-sigma A/D converter with low noise differential inputs.

##Features

- 8 x 17-bit 0 to 5V Single Ended Inputs
- Control via the Raspberry Pi I2C port
- Stack up to 4 ADC Pi Zero boards on a single Raspberry Pi
- Jumper selectable I2C addresses
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

Arduino, C, Node.js, Windows 10 IOT, Python 2 and Python 3 libraries are available on GitHub.