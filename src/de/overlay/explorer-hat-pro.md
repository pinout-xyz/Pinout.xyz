<!--
---
name: Explorer HAT Pro
class: board
type: alle
formfactor: HAT
manufacturer: Pimoroni
image: 'image.png'
url: https://github.com/pimoroni/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
description: Eine Platine mit LEDs, Ein- und Ausgängen, Motorsteuerung, Sensor-Tasten und Steckbrett.
install:
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'explorerhat'
  'examples': 'examples/'
pincount: 40
i2c:
  '0x28':
    name: Cap Touch
    device: cap1208
  '0x48':
    name: Analog Input
    device: ads1015
pin:
  '3': {}
  '5': {}
  '7':
    name: LED 1
    mode: output
    active: high
  '8': {}
  '10': {}
  '11':
    name: LED 2
    mode: output
    active: high
  '12': {}
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
  '19': {}
  '21': {}
  '22':
    name: Input 4
    mode: input
    active: high
  '23': {}
  '24': {}
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
  '35':
    name: Motor 1 +
    mode: output
    active: high
  '36':
    name: Output 4
    mode: output
    active: high
  '37':
    name: Motor 2 -
    mode: output
    active: high
  '38':
    name: Motor 1 -
    mode: output
    active: high
  '40':
    name: Motor 2 +
    mode: output
    active: high
-->
#Explorer HAT und Explorer HAT Pro

Der Explorer HAT Pro besteht aus 5V Ein- und Ausgängen, Sensor-Tasten, LEDs, analogen Eingängen und einem H-Bridge Motor-Treiber. 
Perfekt für alle möglichen Ideen auf dem Raspberry Pi auszuprobieren.

```bash
sudo apt-get install python-pip
sudo pip install explorer-hat
```

Anschliessend die Libraries in Dein Python-Skript importieren und anfangen zu basteln:

```bash
import explorerhat
explorerhat.light.on()
```
