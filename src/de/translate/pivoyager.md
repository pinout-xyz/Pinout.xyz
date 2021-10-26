<!--
---
name: PiVoyager, the smart UPS pHAT 
class: board
type: power
formfactor: pHAT
manufacturer: Omzlo
collected: Other
description: PiVoyager, the smart UPS for the Raspberry Pi
url: https://www.omzlo.com/articles/pivoyager-the-smart-ups-for-the-raspberry-pi
github: https://github.com/omzlo/pivoyager-hardware
buy: https://shop.omzlo.com/products/pivoyager-the-smart-ups-for-the-raspberry-pi
image: 'pivoyager.png'
pincount: 40
eeprom: no
power:
  '2':
  '4':
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
  '37':
    name: optional watchdog
    mode: output
    active: low
i2c:
  '0x65':
    name: Controller
    device: STM32F030C6T6
-->
#PiVoyager UPS

**The PiVoyager is a UPS with a programmable watchdog, wake-up and a real-time calendar for the Raspberry-Pi.**

The **PiVoyager** is uninterruptible power supply (UPS) for the Raspberry Pi designed to work with standard Li-Ion or LiPo batteries, featuring a programmable watchdog, automatic restart, and a real-time calendar. 
The **PiVoyager** is designed as a Pi Zero pHAT, but works on any Raspberry-Pi with a 40 pin header, including the Raspberry Pi 3B+ and 4. 

When the **PiVoyager** is plugged to a USB power source (USB micro-B) and a Li-Ion/LiPo battery, it will both power your Raspberry Pi and charge the battery if needed, with a selectable charge current of 1000mA (default) or 500mA. If USB power is removed, the **PiVoyager** automatically switches to the battery and continues to power the Raspberry Pi at 5V (2.1A max), thanks to a boost converter.

The **PiVoyager** features a Real-Time Calendar (RTC), which can be configured to store the current date and time. The content of the RTC will be maintained for as long as there is a power source connected, even if the Raspberry Pi is powered down. 

Thanks to provided software the user can fully control and monitor the **PiVoyager**:

- Monitor power status and battery voltage,
- Force the Raspberry Pi to fully shutdown after a specified delay,
- Act as a watchdog, powering down the Raspberry Pi if it becomes inactive,
- Power up the Raspberry Pi at a certain date/time (alarm),
- Power up the Raspberry Pi after a certain delay following a shutdown. 
- Update the firmware through I2C thanks to a built-in bootloader.

For more details, including software download instructions, [see our documentation](https://www.omzlo.com/articles/pivoyager-installation-and-tutorial).

The **PiVoyager** is open-source/open-hardware.
