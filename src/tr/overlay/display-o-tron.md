<!--
---
name: Display-o-Tron 3000
class: board
type: hepsi
formfactor: diğer
manufacturer: Pimoroni
description: 3 satır destekleyen, RGB renkli arka plana sahip bir LCD ve joystick
  butonları
url: https://shop.pimoroni.com/products/displayotron-3000
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/displayotron-3000
image: 'display-o-tron.png'
pincount: 26
eeprom: no
power:
  '2':
  '17':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Joystick Button
    mode: input
    active: low
  '11':
    name: Joystick Left
    mode: input
    active: low
  '13':
    name: Joystick Up
    mode: input
    active: low
  '15':
    name: Joystick Right
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick Down
    mode: input
    active: low
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '23':
    mode: spi
-->
# Display-o-Tron 3000

Aşağıdaki tek satır kodla Display-o-Tron 3000'u kurup kullanmaya başlayabilirsiniz. Yapmanız gereken tek şey terminalde şu komutu çalıştırmak,

```bash
curl -sS https://get.pimoroni.com/dot3k | bash
```

ve de karşınıza gelen yönergeleri takip etmek.