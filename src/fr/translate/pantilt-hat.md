<!--
---
name: Pan Tilt HAT
class: board
type: motor,led
formfactor: HAT
manufacturer: Pimoroni
description: A camera pan/tilt and lighting driver
url: https://shop.pimoroni.com/products/pan-tilt-hat
github: https://github.com/pimoroni/pantilt-hat
docs: https://docs.pimoroni.com/pantilthat
buy: https://shop.pimoroni.com/products/pan-tilt-hat
image: 'pantilthat.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x15':
    name: Servo And Light Driver
    device: PIC16F1503
-->
#Pan Tilt HAT

Pan Tilt HAT is a two-channel servo driver designed to control a tiny servo-powered Pan/Tilt assembly. It also controls either PWM-dimmed lights or WS2812 pixels; up to 24 RGB or 18 RGBW.

Pan Tilt HAT uses a PIC16F1503 with custom firmware, and talks over i2c.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/pantilthat | bash
```

Then import it into your Python script and start tinkering:

```bash
import pantilthat
```
