<!--
---
name: ADC-DAC Pi Zero
class: board
type: adc
formfactor: pHAT
manufacturer: AB Electronics UK
description: 2 channel Analogue to Digital Converter and 2 channel Digital to Analogue Converter
url: https://www.abelectronics.co.uk/p/74/adc-dac-pi-zero-raspberry-pi-adc-and-dac-expansion-board
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-adc-dac-pi-zero.pdf
buy: https://www.abelectronics.co.uk/p/74/adc-dac-pi-zero-raspberry-pi-adc-and-dac-expansion-board
image: 'ab-adcdac-pi-zero.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
install:
  'devices':
    - 'spi'
-->
# ADC-DAC Pi Zero

The ADC-DAC Pi Zero is a 2 channel 12 bit analogue to digital converter and 2 channel 12 bit digital to analogue converter designed to work with the Raspberry Pi.   Designed for the same footprint as the Raspberry Pi Zero the ADC-DAC Pi Zero is also compatible with full size Raspberry Pi models.

The ADC-DAC Pi Zero is based on the Microchip MCP3202 A/D converter containing 2 analogue inputs with 12 bit resolution with a Microchip MCP4822 dual channel 12-bit DAC with internal voltage reference.

Max ADC Sample Rate: 100 ksamples/sec

Max ADC Sample Rate under Python: 12,000 samples per second.

Python, C, C++, Node.js and Windows 10 IOT libraries are available on GitHub.
