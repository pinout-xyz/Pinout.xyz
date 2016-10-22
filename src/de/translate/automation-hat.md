<!--
---
name: Automation HAT
class: board
type: adc,io,motor
formfactor: HAT
manufacturer: Pimoroni
description: An all-in-one home automation and control board
url: http://shop.pimoroni.com/products/automation-hat
github: https://github.com/pimoroni/automation-hat
buy: http://shop.pimoroni.com/products/automation-hat
image: 'automation-hat.png'
pincount: 40
eeprom: yes
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
  '33':
    name: Relay 1
    mode: output
    active: high
  '35':
    name: Relay 2
    mode: output
    active: high
  '36':
    name: Relay 3
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
  '0x54':
    name: LED Driver
    device: sn3218
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
#Automation HAT

Automation HAT is a home monitoring and automation controller for the Raspberry Pi; with relays, analog channels, powered outputs, and buffered inputs. All 24V tolerant.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/automationhat | bash
```

Then import it into your Python script and start tinkering:

```bash
import automationhat
automationhat.relay.one.on()
```
