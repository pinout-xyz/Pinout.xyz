<!--
---
name: 7-port USB hub
class: board
type: usb
formfactor: USB
manufacturer: UUGear
description: 7-port USB hub for Raspberry Pi
url: http://www.uugear.com/product/7-port-usb-hub-for-raspberry-pi/
buy: http://www.uugear.com/product/7-port-usb-hub-for-raspberry-pi/
image: 'uugear-7port-usb-hub.png'
pincount: 7
eeprom: no
power:
  '2':
ground:
  '39':
-->
#7-port USB hub for Raspberry Pi

This is a 7-Port USB hub designed for Raspberry Pi. It extends one USB port on Raspberry Pi to 7 usable USB ports, which allows you to connect much more USB devices to your Raspberry Pi. There is a red LED on board as the power indicator, and seven green LEDs aside the USB ports as transaction indicators.

This USB hub is compatible with all versions of Raspberry Pi, including the old A/B model, A+/B+ model, compute module (with development kit), Raspberry Pi 2 (B model), Raspberry Pi Zero and Raspberry Pi 3 (B model). The board size of this USB hub is the same with Raspberry Pi B+ or Raspberry Pi 2/3 (B model). The old Raspberry Pi A and B model also have the same size, except that they don’t have those rounded corners. This USB hub has 6 mounting holes at correct positions and could be mounted under any Raspberry Pi model except the compute module.

For different models of Raspberry Pi, this USB hub uses different approaches to (optionally) back-power the Raspberry Pi, which significantly simplifies your wiring and allows you to power both the USB hub and Raspberry Pi with only one power supply.

There are also 7 digital output pins on board, which can tell whether a USB port is in used. These output pins are in 3.3V level and can be directly connected to Raspberry Pi’s GPIO pin, or connected to an external microcontroller.
