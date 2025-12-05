<!--
---
name: PiJuice
class: board
type: power
formfactor: HAT
manufacturer: Pi Supply
description: PiJuice uninterruptible power supply for the Raspberry Pi.
url: https://uk.pi-supply.com/products/pijuice-standard
github: https://github.com/PiSupply/PiJuice
buy: https://uk.pi-supply.com
image: 'pijuice-hat.png'
pincount: 40
eeprom: yes
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
  '0x14':
    name: Control
    device: STM32F030CCT6
-->
# PiJuice

PiJuice is a fully uninterruptible / uninterupted power supply that will always keep your Raspberry Pi powered! It has a real time clock (RTC) for time tracking and scheduled tasks when the Pi is offline (as well as remote on/off of your Pi). It also has an integrated microcontroller (MCU) chip which will manage soft shut down functionality, a true low power deep sleep state and intelligent start up.

The tri-coloured RGB LEDs will allow you to keep track of the battery charge levels and other info (they are programmable). There are also three programmable buttons which will allow you to trigger events or customisable scripts aside from their predefined functions. PiJuice only uses five of the Pi's GPIO pins (just power and I2C), the rest are free and made available via the stacking header which allows for other boards to be used along side PiJuice. The board can be powered directly from the grid with the standard Raspberry Pi PSU, via an on board battery, via external batteries, solar panels, wind turbines and other renewable sources.

The board has a Raspberry Pi HAT compatible layout, with onboard EEPROM (you can disable the EEPROM if you want also). It has been designed for the Raspberry Pi A+, B+, 2B, 3B and 3B+ but it is also electrically compatible with the Raspberry Pi Zero v1.3 and Zero W v1.1 or any other Pi.

* Onboard 1820 mAh off the shelf Lipo / LiIon battery for ~4 to 6 hours in constant use (with support for larger Lipo Battery of 5000 or 10,000 mAH+ to last up to 24 hrs +)
* A Full Uninterruptible Power Supply solution
* Designed for the Raspberry Pi A+, B+, 2B, 3B and 3B+ but also compatible with Raspberry Pi Zero v1.3 and Raspberry Pi Zero Wireless.
* Integrated Real Time Clock
* Onboard intelligent on/off switch
* Low power deep-sleep state with wake on interrupt/calendar event
* Programmable multi-colored RGB led (x2) and buttons (x3) with super simple user-configurable options
* Hardware watchdog timer to keep your Raspberry Pi on and working in mission-critical remote applications
* Full power management API available to Raspberry Pi OS with auto shutdown capability when running low on batteries
* Low profile design to fit inside many existing Raspberry Pi cases
