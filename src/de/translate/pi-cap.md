<!--
---
name: Pi Cap
class: board
type: touch, capacitive, audio
formfactor: Custom
manufacturer: Bare Conductive
description: Add capacitive touch, distance sensing and high quality audio to the Raspberry Pi
url: https://www.bareconductive.com/shop/pi-cap/
buy: https://www.bareconductive.com/shop/pi-cap/
image: 'pi-cap.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '7':
    name: Button
    mode: input
    active: low
  '11':
    name: IRQ
    mode: input
    active: low
  '29':
    name: Green LED
    mode: output
    active: low
  '31':
    name: Red LED
    mode: output
    active: low
  '32':
    name: PWM0
    mode: output
    active: high
  '33':
    name: PWM1
    mode: output
    active: high
  '37':
    name: Blue LED
    mode: output
    active: low
i2c:
  '0x5C':
    name: MPR121
    device: MPR121
-->
# Pi-Cap

The Pi Cap adds precise capacitive touch, distance sensing and high quality audio to any Raspberry Pi with a 40 pin GPIO connector. The 12 electrodes can be connected to anything conductive to create a touch or proximity interface. Additionally the Pi Cap includes a user-programmable RGB LED and a multi-function button.

The Pi Cap software is in the official Raspbian repository, so to install the software simply enter:
```bash
sudo apt-get update
sudo apt-get dist-upgrade
```

Reboot the Raspberry Pi and enter:
```bash
sudo apt-get install picap
picap-setup
```

The Pi Cap provides 7 digital I/O pins, brought out from the 40-way Raspberry Pi GPIO connector – pins 12, 13, 15, 16, 18, 22, 36. The Pi Cap package contains plenty of code examples written in C++, Python and Node.js that are supported by the Pi Cap library.