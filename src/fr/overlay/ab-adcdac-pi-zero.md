<!--
---
name: ADC-DAC Pi Zero
class: board
type: a/n
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

Le **ADC-DAC Pi Zero** est basé sur la micro-puce de conversion **MCP3202 A/D** qui comporte 2 entrées analogiques 12 bit et sur une micro-puce **MCP4822 D/A**  qui comporte 2 entrées digitales avec tension de référence interne.

Débit de conversion ADC max: 100 ksamples/sec

Débit de conversion ADC max (sous Python): 12,000 samples per second.

Les librairies **Arduino**, **C**, **Node.js**, **Windows 10 IOT**, **Python 2** et **Python 3** sont disponibles sur GitHub.
