<!--
---
name: Witty Pi
class: board
type: power,rtc
formfactor: HAT
manufacturer: UUGear
description: Realtime clock and power management for Raspberry Pi
url: http://www.uugear.com/product/witty-pi-realtime-clock-and-power-management-for-raspberry-pi/
github: https://github.com/uugear/Witty-Pi
buy: http://www.uugear.com/product/witty-pi-realtime-clock-and-power-management-for-raspberry-pi/
image: 'uugear-witty-pi.png'
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
    name: HALT
    mode: input
  '11':
    name: LED
    mode: output
  '8':
    name: TXD
    mode: other
i2c:
  '0x68':
    name: DS1307
    device: DS1307
-->
#Witty Pi

Witty Pi is an extension board that adds realtime clock and power management to your Raspberry Pi.

You can turn on/off your Raspberry Pi with a single tap on the button on Witty Pi, and the power supply for Raspberry Pi and all its USB peripherals will get fully cut after the shutdown.

Witty Pi has a CR2032 backed realtime clock (DS1337) on board, and can keep time for Raspberry Pi when it is off. You can schedule next shutdown/startup of your Pi via the software. A user-defined schedule script could be used for complex use case, which requires scheduling multiple shutdowns and startups at different moments.

You can use the two commands below to install software for Witty Pi:

```bash
wget http://www.uugear.com/repo/WittyPi/installWittyPi.sh

sudo sh installWittyPi.sh
```
After the installation is done, reboot your Raspberry Pi and your Witty Pi is ready to go.

Witty Pi supports all Raspberry Pi models that have 40-pin header, including A+, B+, 2B, 3B and Zero.
