<!--
---
name: Unicorn HAT
class: board
type: hepsi
formfactor: HAT
manufacturer: Pimoroni
description: Tek bir HAT kart üzerinde 64 adet programlanabilir parlak led modülü.
url: http://shop.pimoroni.com/products/unicorn-hat
github: https://github.com/pimoroni/unicornhat
buy: http://shop.pimoroni.com/products/unicorn-hat
image: 'unicorn-hat.png'
pincount: 40
eeprom: detect
power:
  '2':
ground:
  '9':
pin:
  '12':
    name: Data
    direction: output
    mode: pwm
    active: high
    description: WS2812 Data
-->
#Unicorn HAT

64 adet parlak LEDe sahip bu HAT kart'ı bir C kütüphanesi ile çok hızlı çalışacak bir şekilde yönetebilir, LEDlerin daha parlak veya sönük yanmasını sağlayabilirsiniz.

Not: Unicorn HAT bazı PWM kurnazlıkları kullanmakta. Bunun içnde analog ses çıkışından Raspberry Pi'nin ses çıkartmasını sağlayan şeyler de olduğundan ikisini aynı anda kullanamazsınız!

Kurulumu çok basit, sadece aşağıdaki komutu çalıştırın:

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

Ardından Python scriptinize modülü ekleyip kurcalamaya başlayabilirsiniz:

```bash
import unicornhat
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
