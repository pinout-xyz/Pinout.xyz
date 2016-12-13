<!--
---
name: Android Things Rainbow HAT
class: board
type: multi
formfactor: HAT
manufacturer: Pimoroni
description: An array of sensors, inputs and outputs to explore Android Things
url: http://blog.pimoroni.com/android-things-launch/
github: https://github.com/pimoroni/rainbow-hat
buy: https://shop.pimoroni.com/products/rainbow-hat-for-android-things
image: 'pimoroni-rainbow-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '17':
ground:
  '9':
  '25':
  '30':
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
    name: Barometer
    device: BMP280
  '0x77':
    name: Matrix Driver
    device: HT16K33
-->
#AndroidThings: Rainbow HAT

Rainbow HAT has a buffet of sensors, inputs and displays to explore Android Things. Use it as a weather station, a clock, a timer or stopwatch, a mood light, or endless other things.

* Seven APA102 multicolour LEDs
* Four 14-segment alphanumeric displays (green LEDs)
* HT16K33 display driver chip
* Three capacitive touch buttons
* Atmel QT1070 capacitive touch driver chip
* Blue, green and red LEDs
* BMP280 temperature and pressure sensor
* Piezo buzzer
* Breakout pins for servo, I2C, SPI, and UART (all 3v3)