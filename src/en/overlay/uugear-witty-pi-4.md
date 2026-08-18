<!--
---
name: Witty Pi 4
class: board
type: power,rtc
formfactor: HAT
manufacturer: UUGear
description: Realtime clock and power management for Raspberry Pi
url: https://www.uugear.com/product/witty-pi-4/
github: https://github.com/uugear/Witty-Pi-4
image: 'uugear-witty-pi-4.png'
pincount: 40
eeprom: no
power:
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
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
  '7':
    name: Power Button
    mode: input
  '8':
    name: TXD / Off detection
    mode: output
  '11':
    name: LED / SysUp detection
    mode: output
i2c:
  '0x08':
    name: ATtiny841
    device: ATtiny841
-->
# Witty Pi 4

Witty Pi is an add-on board that adds realtime clock and power management to your Raspberry Pi. It can define your Raspberry Pi’s ON/OFF sequence, and significantly reduce the energy usage. Witty Pi 4 is the fourth generation of Witty Pi and it has these hardware resources onboard:

- Factory calibrated and temperature compensated realtime clock with ±2ppm accuracy.
- Dedicated temperature sensor with 0.125 °C resolution.
- On-board DC/DC converter that accepts up to 30V DC.
- AVR 8-bit microcontroller (MCU) with 8 KB programmable flash.

## Virtual Registers for Temperature Sensor and Real-Time Clock

The temperature sensor and Real-Time Clock are accessible through the WittyPi 4 I2C device address (0x08), and are mapped to so called virtual adresses. The LM75B temperature sensor is mapped to #50 .. #53, while the PCF85063A Real-Time Clock is mapped to #54 .. #71. More details can be found in the [user manual](https://www.uugear.com/doc/WittyPi4_UserManual.pdf).

