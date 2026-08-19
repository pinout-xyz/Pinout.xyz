<!--
---
name: Pibrella
class: board
type: multi,io
formfactor: Custom
manufacturer: Cyntech
collected: Other
description: Hepsi-bir-arada, hafif, ses, giriş ve çıkış destekleyen eklenti kartı.
url: http://pibrella.com
github: https://github.com/pimoroni/pibrella
buy: https://shop.cyntech.co.uk/products/pibrella?variant=581387897
image: 'pibrella.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '7':
    name: Green LED
    direction: output
    active: high
  '11':
    name: Yellow LED
    direction: output
    active: high
  '12':
    name: Buzzer
    direction: output
    active: high
  '13':
    name: Red LED
    direction: output
    active: high
  '15':
    name: Output E
    direction: output
    active: high
  '16':
    name: Output F
    direction: output
    active: high
  '18':
    name: Output G
    direction: output
    active: high
  '19':
    name: Input D
    direction: output
    active: high
  '21':
    name: Input A
    direction: input
    active: high
  '22':
    name: Output H
    direction: output
    active: high
  '23':
    name: Button
    direction: input
    active: high
  '24':
    name: Input C
    direction: input
    active: high
  '26':
    name: Input B
    direction: input
    active: high
-->
# Pibrella

Pibrella Pimoroni tarafından hazırlanmış hepsi-bir-arada, hafif, ses, giriş ve çıkış destekleyen bir eklenti kartı. Cyntech çok fazla IO pini kullanmakta, fakat hem Serial, hem de I2C pinleri boşta kalmakta. Bu sebeple eğer yaratıcı olursanız bu kartla birlikte eklenti kartları için pek çok yer kalmakta.

Pibrella'yı kullanmak çok kolay. Öncelikle terminalden aşağıdaki komutları çalıştırıp kurulumu gerçekleştirin:

```bash
curl -sS https://get.pimoroni.com/pibrella | bash
```

Ardından Python kodunuzda aşağıdaki gibi modülü ekleyip kurcalamaya başlayabilirsiniz:

```bash
import pibrella
pibrella.light.red.on()
```
