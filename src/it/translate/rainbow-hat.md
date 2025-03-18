<!--
---
name: Rainbow HAT
class: board
type: display,led,multi,sensor,touch
formfactor: HAT
manufacturer: Pimoroni
description: Sensors and IO for Android Things
url: http://blog.pimoroni.com/android-things-launch/
github: https://github.com/pimoroni/rainbow-hat
buy: https://shop.pimoroni.com/products/rainbow-hat-for-android-things
image: 'rainbow-hat.png'
pincount: 40
eeprom: yes
power:
  '4':
  '17':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '33':
    name: Buzzer
    mode: pwm
  '31':
    name: Red/Left LED
    mode: output
    active: high
  '35':
    name: Green/Middle LED
    mode: output
    active: high
  '37':
    name: Blue/Right LED
    mode: output
    active: high
  '40':
    name: Touch A
    mode: input
    active: low
  '38':
    name: Touch B
    mode: input
    active: low
  '36':
    name: Touch C
    mode: input
    active: low
i2c:
  '0x70':
    name: Matrix Driver
    device: HT16K33
  '0x77':
    name: Barometer
    device: BMP280
-->
# Rainbow HAT for Android Things™

Rainbow HAT has a buffet of sensors, inputs and displays to explore Android Things™. Use it as a weather station, a clock, a timer or stopwatch, a mood light, or endless other things.

Features:

* Seven APA102 multicolour LEDs
* Four 14-segment alphanumeric displays
* HT16K33 display driver chip
* Three capacitive touch buttons
* Atmel QT1070 capacitive touch driver chip
* BMP280 temperature and pressure sensor
* Blue, green and red LEDs
* Piezo buzzer

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl https://get.pimoroni.com/rainbowhat | bash
```
