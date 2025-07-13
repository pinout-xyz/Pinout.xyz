<!--
---
name: Explorer HAT
class: board
type: hepsi
formfactor: HAT
manufacturer: Pimoroni
description: Hepsi-bir-arada, hafif, hızlı, dokunma, giriş ve çıkış destekleyen eklenti
  kartı.
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat.png'
pincount: 40
eeprom: yes
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
 -->
# Explorer HAT

5V giriş ve çıkışları, dokunmatik paneli ve LEDler ile Explorer HAT, Raspberry Pi'de prototipleme için tam teşekkürlü bir araç olarak teşkil etmekte.

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Ardından Python scriptinize aşağıdaki kodları ekleyip prototipinizi kurcalamaya başlayabilirsiniz:

```bash
import explorerhat
explorerhat.light.on()
```
