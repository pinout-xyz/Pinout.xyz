<!--
---
name: RTC Pi Zero
class: board
type: rtc
formfactor: pHAT
manufacturer: AB Electronics UK
description: Real-Time Clock Module for the Raspberry Pi
url: https://www.abelectronics.co.uk/p/70/RTC-Pi-Zero
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/stock/raspberrypi/rtcpizero/rtcpi-zero-schematic.pdf
buy: https://www.abelectronics.co.uk/p/70/RTC-Pi-Zero
image: 'ab-rtc-pi-zero.png'
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
# RTC Pi Zero

The RTC Pi Zero is a battery backed real-time clock module for the Raspberry Pi Zero. It keeps track of the time while the Raspberry Pi is switched off and allows the Raspberry Pi to retrieve the current date and time from the RTC Pi Zero when it is switched back on.

The RTC Pi Zero is powered through the host Raspberry Pi using the GPIO port and extended pins on the GPIO connector allow you to stack the RTC Pi Zero along with other expansion boards. The RTC Pi Zero uses the DS1307 RTC real time clock and a CR2032 battery to maintain the date and time when the main system power is not available.

Unlike most other DS1307 based RTC modules the RTC Pi Zero also includes an I2C logic level converter allowing you to connect other 5V I2C devices to your Raspberry Pi.

Arduino, C, Node.js, Windows 10 IOT, Python 2 and Python 3 libraries are available on GitHub.
