<!--
---
name: RTC Pi
class: board
type: rtc
formfactor: pHAT
manufacturer: AB Electronics UK
description: Real-Time Clock Module for the Raspberry Pi
url: https://www.abelectronics.co.uk/p/70/rtc-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/viewpdf/schematic-rtcpi-v3
buy: https://www.abelectronics.co.uk/p/70/rtc-pi
image: 'ab-rtc-pi.png'
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
    name: DS1307
    device: DS1307
-->
# RTC Pi

The RTC Pi is a battery-backed real-time clock module for the Raspberry Pi and other compatible single-board computers. It keeps track of the time while the Raspberry Pi is switched off and allows it to retrieve the current date and time from the RTC Pi when it is switched back on.

The RTC Pi is powered through the host Raspberry Pi using the GPIO port and extended pins on the GPIO connector allow you to stack the RTC Pi along with other expansion boards. The RTC Pi uses the DS1307 RTC real time clock and a CR2032 battery to maintain the date and time when the main system power is not available.

Unlike most other DS1307 based RTC modules the RTC Pi also includes an I2C logic level converter allowing you to connect other 5V I2C devices to your Raspberry Pi.

Python, MicroPython, C, C++, Node.js and Windows 10 IOT libraries are available on GitHub.
