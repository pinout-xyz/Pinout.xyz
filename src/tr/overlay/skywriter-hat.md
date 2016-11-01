<!--
---
name: Skywriter HAT
class: board
type: hepsi
formfactor: HAT
manufacturer: Pimoroni
description: 3 Boyutlu pozisyon ve hareket sensörü.
url: http://shop.pimoroni.com/products/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
image: 'skywriter-hat.png'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transfer
i2c:
  '0x42':
    name: Gesture sensor
    device: mgc3130
-->
#Skywriter HAT

Skywriter HAT X, Y ve Z ekseninde parmağınızın pozisyonunu algılamanızı, ve de bu değerleri Python Scriptinizde kullanmanızı sağlar.

Ayrıca kaydırma (tıpkı telefonlardaki "swipe" hareketi gibi) gibi hareketleri de algılama yeteneğine sahiptir.

```bash
curl -sS get.pimoroni.com/skywriter | bash
```
