<!--
---
name: Witty Pi 2
class: board
type: power,rtc
formfactor: HAT
manufacturer: UUGear
description: Realtime clock and power management for Raspberry Pi
url: http://www.uugear.com/product/wittypi2/
github: https://github.com/uugear/Witty-Pi-2
buy: http://www.uugear.com/product/wittypi2/
image: 'uugear-witty-pi-2.png'
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
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
  '7':
    name: HALT
    mode: input
  '11':
    name: LED
    mode: output
i2c:
  '0x68':
    name: DS3231
    device: DS3231
-->
# Witty Pi 2

Witty Pi 2 is the second generation of Witty Pi, which adds realtime clock and power management to your Raspberry Pi.

You can turn on/off your Raspberry Pi with a single tap on the button on Witty Pi 2, and the power supply for Raspberry Pi and all its USB peripherals will get fully cut after the shutdown.

Witty Pi 2 has a CR2032 backed realtime clock (DS3231) on board, and can accurately keep time for Raspberry Pi. The built-in temperature sensor can tell the temperature around your Raspberry Pi too.

You can schedule next shutdown/startup of your Pi via the software. Complex ON/OFF sequence for Raspberry Pi can be achieved by applying a user-defined schedule script.

If you are using power bank as power supply, the new dummy load feature can keep power bank alive with low current consumption. The newly added 6-pin female header breaks out some important signals for integration/extension.

You can use the two commands below to install software for Witty Pi 2:

```bash
wget http://www.uugear.com/repo/WittyPi2/installWittyPi.sh

sudo sh installWittyPi.sh
```
After the installation is done, reboot your Raspberry Pi and your Witty Pi 2 is ready to go.

Witty Pi 2 supports all Raspberry Pi models that have 40-pin header, including A+, B+, 2B, 3B and Zero.
