<!--
---
name: Duino
class: board
type: mcu,io
formfactor: Custom
manufacturer: RasPiO
description: Arduino Programming on the Raspberry Pi
url: http://rasp.io/duino/
github: https://github.com/raspitv/raspio_duino
buy: https://ryanteck.uk/add-ons/58-raspio-duino.html
image: 'raspio-duino.png'
pincount: 26
eeprom: no
power:
  '1':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '8':
    mode: uart
  '10':
    mode: uart
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
install:
  'devices':
    - 'spi'
-->
#Duino

The RasPiO Duino is a small plug-on board for Raspberry Pi. It has similar functionality to an Arduino Uno, with an ATMega 328P-PU at its heart, but is fully programmable from the Raspberry Pi. Once programmed, it can be removed from the Pi and used on its own.

Pins on the ATMega are broken out to a cluster of three holes. The ATMega328 features a 6 channel analog to digital converter and 14 digital I/O pins, 6 of which can also be used for PWM. The Pi’s GPIO ports are also broken out on the board as well and there is a 72 point prototyping area, with GND, 3V3 and 5V rails, where you can add your own components.

Note: the RasPiO Duino runs on 3v3 at 12 MHz (not 5V at 16 MHz like the Uno).