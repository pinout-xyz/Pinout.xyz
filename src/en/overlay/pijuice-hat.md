<!--
---
name: PiJuice
class: board
type: power,rtc
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
  '4':
  '17':
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
#PiJuice

PiJuice is a fully uninterruptable / uninterupted power supply that will always keep your Raspberry Pi powered! It has a real time clock (RTC) for time tracking and scheduled tasks when the Pi is offline (as well as remote on/off of your Pi). It also has an integrated microcontroller (MCU) chip which will manage soft shut down functionality, a true low power deep sleep state and intelligent start up.

The tri-coloured RGB LEDs will allow you to keep track of the battery charge levels and other info (they are programmable). There are also three programmable buttons which will allow you to trigger events or customisable scripts aside from their predefined functions. PiJuice only uses five of the Pi's GPIO pins (just power and I2C), the rest are free and made available via the stacking header which allows for other boards to be used along side PiJuice. The board can be powered directly from the grid with the standard Raspberry Pi PSU, via an on board battery, via external batteries, solar panels, wind turbines and other renewable sources.

The board has a Raspberry Pi HAT compatible layout, with onboard EEPROM (you can disable the EEPROM if you want also). It has been designed for the Raspberry Pi A+, B+, 2B, 3B, 3B+ and 4B, Raspberry Pi Zero v1.3, Raspberry Pi Zero Wireless, and any other Raspberry Pi with 40 GPIO pins.

* Onboard 1820 mAh off the shelf Lipo / LiIon battery for ~4 to 6 hours in constant use (with support for larger Lipo Battery of 5000 or 10,000 mAH+ to last up to 24 hrs +)
* A Full Uninterruptable Power Supply solution
* Designed for the Raspberry Pi A+, B+, 2B, 3B, 3B+ and 4B but also compatible with Raspberry Pi Zero v1.3 and Raspberry Pi Zero Wireless.
* Integrated Real Time Clock
* Onboard intelligent on/off switch
* Low power deep-sleep state with wake on interrupt/calendar event
* Programmable multi-colored RGB led (x2) and buttons (x3) with super simple user-configurable options
* Hardware watchdog timer to keep your Raspberry Pi on and working in mission-critical remote applications
* Full power management API available to Raspberry Pi OS with auto shutdown capability when running low on batteries
* Low profile design to fit inside many existing Raspberry Pi cases

##Technical Information

* BP7X battery - original battery from Motorola Droid 2 (A955) - 1820mAh battery
* Microcontroller is an ST Micro STM32F030CCT6 ARM Cortex-M0, 48MHz, F64KB, R8KB, I2C, SPI, USART, 2.4-3.6V
* Charge IC - BQ24160RGET Charger IC Lithium-Ion/Polymer, 2.5A, 4.2-10V
* Fuel gauge IC - LC709203FQH-01TWG Battery Fuel Gauge, 1-Cell Li-ion, 2.8%
* EEPROM - CAT24C32WI-GT3 EEPROM, I2C, 32KBIT, 400KHZ, 1V7-5V5
* Optional spring pin - Mil-Max 0929-7-15-20-77-14-11-0
* Compatible with any 4 pin battery on board that can be used with 00-9155-004-742-006 battery contacts from AVX including the BP7X, BP6X, and any compatible batteries including the 1600mAh and 2300mAh ones from CameronSino (CS-MOA853SL and CS-MOA855XL)
* There is an on board 4 pin screw terminal block for larger off board batteries. Any single cell LiPo / LiIon is compatible. However, you use your own sourced battery at your own risk. We HIGHLY RECOMMEND using a battery with an internal protection circuit and a NTC (temp sensor)
* Optional header for offboard button - connected to same output as SW1
* 6 pin breakout header - with two GPIO from the ARM Cortex-M0, Vsys, 5v0, 3v3, GND connections
* Header for optional off board solar panel / wind turbine etc.
* Optional RF Shield attachment - Harwin S02-20150300 (can also double as an inexpensive heatsink)
* Input voltage range - 4.2V 10V
* Output voltage - 3.3V and 5V
* Output amperage - maximum current at 5V gpio is 2.5A and at VSYS output 2.1A, but also this depends heavily on battery capacity. For BP7X have measured around 1.1A at 5V GPIO and around 1.6A at VSYS output. Obviously, this also depends heavily on the current draw demanded by the Raspberry Pi/device itself. To achieve a maximum of 2.5A it will need battery over 3500mAh.
