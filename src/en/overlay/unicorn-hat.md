<!--
---
name: Unicorn HAT
class: board
type: led
formfactor: HAT
manufacturer: Pimoroni
description: 64 blindingly bright RGB LEDs on a single HAT
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
install:
  'apt':
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'unicornhat'
  'python3':
    - 'unicornhat'
-->
#Unicorn HAT

64 blindingly bright LEDs packed into a HAT and driven with an ultra-fast, C library that you can talk to from Python make Unicorn HAT PiGlow's bigger, brighter brother.

Note: Unicorn HAT uses some special PWM trickery, performed with the same hardware that lets your Pi produce sound through the audio jack ( analog audio ) so you can't use both at the same time!

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

Then import it into your Python script and start tinkering:

```bash
import unicornhat
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
