<!--
---
name: Unicorn HAT
class: board
type: Tutti
formfactor: HAT
manufacturer: Pimoroni
description: 64 LED RGB accecanti su un unico HAT
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
    name: Dati
    direction: output
    mode: pwm
    active: high
    description: WS2812 Dati
-->
#Unicorn HAT

64 LED accecanti montati su un HAT e controllati da una velocissima libreria in C, con cui puoi comunicare
via Python, rendono l'Unicorn HAT il fratello maggiore (e più luminoso) del PiGlow.

Nota: Unicorn HAT usa alcuni trucchetti col PWM, che sfruttano lo stesso hardware che ti permette di produrre
suoni tramite il jack audio (analogico), per cui non puoi usare entrambi allo stesso momento!

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

Importalo poi nel tuo script Python e inizia a smanettare:

```bash
import unicornhat
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
