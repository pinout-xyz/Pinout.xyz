<!--
---
name: ZeroSeg
class: board
type: display
formfactor: pHAT
manufacturer: PiHut
description: 8 character 7 segment display for the Raspberry Pi
url: https://thepihut.com/products/zeroseg
github: https://github.com/AverageManVsPi/ZeroSeg
buy: https://thepihut.com/products/zeroseg
image: 'zeroseg.png'
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
  '19':
    mode: DIN
  '24':
    mode: CS
  '23':
    name: CLK
  '11':
    name: SW1
  '37':
    name: SW2
-->
# ZeroSeg

The ZeroSeg is an easy to use 8-character 7-segment display add-on board for your Raspberry Pi Zero or any other 40-pin Raspberry Pi model.

ZeroSeg has the ability to display 8 characters, data such as the time, date, counters, stock prices, sports scores and more making it very
useful for projects of all shapes and sizes.

The displays are controlled by a MAX7219CNG integrated circuit, which manages each LED segment, requiring very few GPIO pins to run the board. This board's circuit is wired in the exact same way as generic 7-segment modules, allowing the use of existing code and libraries to easily create Pi Zero projects with 8-character displays.

To install first enable SPI and update your pi then:

```bash
sudo apt-get install build-essential python-dev python-spidev
git clone https://github.com/AverageManVsPi/ZeroSeg.git
cd ZeroSeg && sudo python setup.py install
```
