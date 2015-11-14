<!--
---
name: Explorer HAT Pro
manufacturer: Pimoroni
url: https://github.com/pimoroni/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
description: Hepsi-bir-arada, hafif, hızlı, dokunma, giriş ve çıkış destekleyen eklenti
  kartı.
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
#Explorer HAT Pro

5V giriş ve çıkışları, dokunmatik paneli, LEDler, analog girişler ve bir H-Bridge motor ile Explorer HAT Pro, Raspberry Pi'de prototipleme için tam teşekkürlü bir araç olarak teşkil etmekte.

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Ardından Python scriptinize aşağıdaki kodları ekleyip prototipinizi kurcalamaya başlayabilirsiniz:

```bash
import explorerhat
explorerhat.light.on()
```
