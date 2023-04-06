<!--
---
name: Inventor HAT Mini
class: board
type: adc,audio,io,motor,led
formfactor: pHAT
manufacturer: Pimoroni
description: A ...
url: https://shop.pimoroni.com/products/inventor-hat-mini
github: https://github.com/pimoroni/inventorhatmini-python
buy: https://shop.pimoroni.com/products/inventor-hat-mini
image: 'pimoroni-inventor-hat-mini.png'
pincount: 40
eeprom: no
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
    name: I2C SDA
    mode: i2c
  '5':
    name: I2C SCL
    mode: i2c
  '7':
    name: I2C Int
    mode: input
  '8':
    name: UART TX / TRIG
    mode: uart
  '10':
    name: UART RX / ECHO
    mode: uart
  '12':
    name: I2S
  '22':
    name: Amp Enable
    active: high
  '32':
    name: LED Data
    mode: pwm
    direction: output
  '35':
    name: I2S
  '37':
    name: User Button
    mode: input
  '40':
    name: I2S
install:
  'devices':
  - 'i2c'
  - 'i2s'
-->
# Pimoroni Inventor HAT Mini

Inventor HAT Mini is an...

The unit comes fully-assembled, with ...

To get Inventor HAT Mini up and running, you can use the one-line product installer:

```bash
git clone https://github.com/pimoroni/inventorhatmini-python
cd inventorhatmini-python
./install.sh
```

Then import it into your Python script and start tinkering:

```bash
from inventorhatmini import InventorHATMini
board = InventorHATMini()
```
