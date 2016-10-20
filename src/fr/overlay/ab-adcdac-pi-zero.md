<!--
---
name: ADC-DAC Pi Zero
class: board
type: ADC-DAC
formfactor: pHAT
manufacturer: AB Electronics
description: 2 canaux Analogiques vers un Convertisseur Digital et 2 canaux Digitaux vers un Convertisseur Analogiques
url: https://www.abelectronics.co.uk/p/74/ADC-DAC-Pi-Zero-Raspberry-Pi-ADC-and-DAC-expansion-board
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/74/ADC-DAC-Pi-Zero-Raspberry-Pi-ADC-and-DAC-expansion-board
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
#ADC-DAC Pi Zero

Le **ADC-DAC Pi Zero** de **AB Electronics** est une carte chapeau de conversion de signaux Analogiques vers Digitaux sur 2 canaux 12 bit et Digitaux vers Analogiques sur 2 canaux 12 bit conçu pour fonctionner avec le Raspberry Pi. Taillé aux dimensions du Raspberry Pi Zero, la carte chapeau **ADC-DAC Pi Zero** est aussi compatible avec les autres modèles de Raspberry Pi.

The ADC-DAC Pi Zero is based on the Microchip MCP3202 A/D converter containing 2 analogue inputs with 12 bit resolution with a Microchip MCP4822 dual channel 12-bit DAC with internal voltage reference.

Max ADC Sample Rate: 100 ksamples/sec

Max ADC Sample Rate under Python: 12,000 samples per second.

Arduino, C, Node.js, Windows 10 IOT, Python 2 and Python 3 libraries are available on GitHub.
