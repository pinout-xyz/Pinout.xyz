<!--
---
name: ADC Differential Pi
manufacturer: AB Electronics UK
description: 8 channel Analogue to Digital Converter
url: https://www.abelectronics.co.uk/p/65/ADC-Differential-Pi-Raspberry-Pi-Analogue-to-Digital-converter
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/65/ADC-Differential-Pi-Raspberry-Pi-Analogue-to-Digital-converter
formfactor: Custom
pincount: 40
eeprom: no
power: 3v3,5v
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
#ADC Differential Pi

The ADC Differential Pi is an 8 channel 18 bit analogue to digital converter designed to work with the Raspberry Pi A+, Raspberry Pi B+ and Raspberry Pi 2 Model B. The ADC Differential Pi is based on two Microchip MCP3424 A/D converters each containing 4 analogue inputs.  The MCP3424 is a delta-sigma A/D converter with low noise differential inputs.

## Features ##

  - 8 x 18-bit differential inputs

  - Control via the Raspberry Pi I2C port

  - Stack up to 4 ADC Differential Pi boards on a single Raspberry Pi

  - Jumper selectable I2C addresses

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


We have Arduino, C, Windows 10 IOT, Python 2 and Python 3 libraries available for this expansion board.  You can download all of the libraries from github at:

[https://github.com/abelectronicsuk/](https://github.com/abelectronicsuk/)