<!--
---
name: Unicorn pHAT
class: board
type: led
formfactor: pHAT
manufacturer: Pimoroni
description: 32 blindingly bright RGB LEDs on a single pHAT
url: http://shop.pimoroni.com/products/unicorn-phat
github: https://github.com/pimoroni/unicornhat
buy: http://shop.pimoroni.com/products/unicorn-phat
image: 'unicorn-phat.png'
pincount: 40
eeprom: yes
power:
  '2':
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
  '12':
    name: Data
    direction: output
    mode: pwm
    active: high
    description: WS2812 Data
install:
  'apt':
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'unicornhat'
  'python3':
    - 'unicornhat'
-->
#Unicorn pHAT

32 blindingly bright LEDs packed into a pHAT and driven with an ultra-fast, C library that you can talk to from Python make Unicorn HAT PiGlow's bigger, brighter brother.

Note: Unicorn pHAT uses some special PWM trickery, performed with the same hardware that lets your Pi produce sound through the audio jack ( analog audio ) so you can't use both at the same time!

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

Then import it into your Python script and start tinkering:

```bash
import unicornhat
unicorn.set_layout(unicorn.PHAT)
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
