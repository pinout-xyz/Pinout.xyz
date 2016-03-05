<!--
---
name: RTC Pi Plus
class: board
type: other
manufacturer: AB Electronics UK
description: Real-Time Clock Module for the Raspberry Pi
url: https://www.abelectronics.co.uk/p/52/RTC-Pi-Plus
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/52/RTC-Pi-Plus
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
    name: DS1307
    device: DS1307
-->
#RTC Pi Plus

The RTC Pi Plus is a battery backed real-time clock module for the Raspberry Pi A+, Raspberry Pi B+ and Raspberry Pi 2 Model B. It keeps track of the time while the Raspberry Pi is switched off and allows the Raspberry Pi to retrieve the current date and time from the RTC Pi Plus  when it is switched back on.

The RTC Pi Plus is powered through the host Raspberry Pi using the GPIO port and extended pins on the GPIO connector allow you to stack the RTC Pi Plus along with other expansion boards. The RTC Pi Plus uses the DS1307 RTC real time clock and a CR2032 battery to maintain the date and time when the main system power is not available.

Unlike most other DS1307 based RTC modules the RTC Pi also includes an I2C logic level converter allowing you to connect other 5V I2C devices to your Raspberry Pi.

Python 2 and 3 libraries are available on GitHub.