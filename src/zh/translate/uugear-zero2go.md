<!--
---
name: Zero2Go
class: board
type: power
formfactor: pHAT
manufacturer: UUGear
description: Wide Input Range Power Supply for Raspberry Pi
url: http://www.uugear.com/product/zero2go/
buy: http://www.uugear.com/product/zero2go/
image: 'uugear-zero2go.png'
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
  '7':
    name: HALT
    mode: input
-->
# Zero2Go

Zero2Go is a Pi-Zero sized power supply that accepts DC 5~26V and output DC 5V/2.6A max. It allows you to turn on/off your Raspberry Pi (Zero or other models) with a single tap.

Zero2Go can connect to a Raspberry Pi Zero without soldering via pogo pins. It also supports other Raspberry Pi models with 40-pin header, including A+, B+, 2B, 3B.

You can use the two commands below to install software for Zero2Go:

```bash
wget http://www.uugear.com/repo/Zero2Go/installZero2Go.sh
sudo sh installZero2Go.sh
```
After the installation is done, reboot your Raspberry Pi and your Zero2Go is ready to go.
