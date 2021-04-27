<!--
---
name: TV HAT
class: board
type: other
formfactor: pHAT
manufacturer: Rasbperry Pi
description: Receives digital DVB-T2 TV streams on your Raspberry Pi to view them or stream them over a network to other devices.
url: https://www.raspberrypi.org/products/raspberry-pi-tv-hat/
github:
schematic: https://www.raspberrypi.org/app/uploads/2018/10/Raspberry-Pi-TV-HAT-Product-Brief.pdf
buy: https://www.raspberrypi.org/products/raspberry-pi-tv-hat/
image: 'tv-hat.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
  '4':
  '17': (not connected)
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
  '27':
    mode: i2c
  '28':
    mode: i2c
-->
# TV HAT

The Raspberry Pi TV HAT has a DVB-T2 and DVB-T tuner on board, which allows you to receive and decode digital television streams on your Raspberry Pi.

 * Sony CXD2880 TV tuner
 * Supported TV standards:
   * Reception frequency: VHF III, UHF IV, UHF V
