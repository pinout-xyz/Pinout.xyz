<!--
---
name: Automation HAT Mini
class: board
type: adc,io,motor,relay,display
formfactor: pHAT
manufacturer: Pimoroni
description: An all-in-one home automation and control board with colour LCD
url: http://shop.pimoroni.com/products/automation-hat-mini
github: https://github.com/pimoroni/automation-hat
buy: http://shop.pimoroni.com/products/automation-hat-mini
image: 'pimoroni-automation-hat-mini.png'
pincount: 40
eeprom: no
power:
  '2':
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
  '19':
    mode: spi
  '21':
    name: D/C
    mode: output
  '22':
    name: Backlight
    mode: output
  '23':
    mode: spi
  '29':
    name: Output 1
    mode: output
    active: high
  '31':
    name: Output 3
    mode: output
    active: high
  '32':
    name: Output 2
    mode: output
    active: high
  '36':
    name: Relay 1
    mode: output
    active: high
  '37':
    name: Input 1
    mode: input
    active: high
  '38':
    name: Input 2
    mode: input
    active: high
  '40':
    name: Input 3
    mode: input
    active: high
i2c:
  '0x48':
    name: Analog Input
    device: ads1015
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
  'python':
    - 'automationhat'
  'python3':
    - 'automationhat'
-->
# Automation HAT Mini

Automation HAT Mini is a home monitoring and automation controller for the Raspberry Pi; with a relay, analog channels, powered outputs, and buffered inputs. All 24V tolerant. It also has a 0.96" mini display for status information.

To get Automation HAT Mini set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/automationhat | bash
```

Then import it into your Python script and start tinkering:

```bash
import automationhat
automationhat.relay.one.on()
```
