<!--
---
name: Explorer HAT
class: board
type: io,touch
formfactor: HAT
manufacturer: Pimoroni
description: Eine Platine mit LEDs, Ein- und Ausgängen, Sensor-Tasten und Steckbrett.
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat.png'
pincount: 40
eeprom: yes
power:
  '2':
  '17':
ground:
  '6':
  '9':
  '14':
  '25':
  '30':
  '39':
pin:
  '7':
    name: LED 1
    mode: output
    active: high
  '11':
    name: LED 2
    mode: output
    active: high
  '13':
    name: LED 3
    mode: output
    active: high
  '15':
    name: Input 2
    mode: input
    active: high
  '16':
    name: Input 1
    mode: input
    active: high
  '18':
    name: Input 3
    mode: input
    active: high
  '22':
    name: Input 4
    mode: input
    active: high
  '29':
    name: LED 4
    mode: output
    active: high
  '31':
    name: Output 1
    mode: output
    active: high
  '32':
    name: Output 2
    mode: output
    active: high
  '33':
    name: Output 3
    mode: output
    active: high
  '36':
    name: Output 4
    mode: output
    active: high
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'explorerhat'
  'python3':
    - 'explorerhat'
-->
# Explorer HAT und Explorer HAT Pro

Der Explorer HAT Pro besteht aus 5V Ein- und Ausgängen, Sensor-Tasten, LEDs, analogen Eingängen und einem H-Bridge Motor-Treiber. 
Perfekt für alle möglichen Ideen auf dem Raspberry Pi auszuprobieren.

```bash
sudo apt-get install python-pip
sudo pip install explorer-hat
```

Anschliessend die Libraries in Dein Python-Skript importieren und basteln:

```bash
import explorerhat
explorerhat.light.on()
```
