<!--
---
name: Snake Eyes Bonnet
class: board
type: display
formfactor: pHAT
manufacturer: Adafruit
description: Two 128x128 pixel OLED or TFT LCD for the Raspberry Pi
url: https://learn.adafruit.com/animated-snake-eyes-bonnet-for-raspberry-pi/
buy: https://www.adafruit.com/products/3356
image: adafruit-animated-eyes-bonnet.png
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '9':
  '25':
  '39':
  '34':
  '30':
  '20':
  '14':
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '33':
    name: ADC Alert
  '15':
    name: Button Wink Left
  '16':
    name: Button Wink Both
  '18':
    name: Button Wink Right
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '29':
    name: DC
  '31':
    name: Reset
  '36':
    mode: spi
  '38':
    mode: spi
  '40':
    mode: spi
  '24':
    mode: spi
i2c:
  '0x48':
    name: Analog Input
    device: ads1015
-->
# Snake Eyes Bonnet
The Snake Eyes Bonnet is a Raspberry Pi accessory for driving two 128x128 pixel OLED or TFT LCD displays, and also provides four analog inputs for sensors.

It's perfect for making cosplay masks, props, spooky sculptures for halloween, animatronics, robots...anything where you want to add a pair of animated eyes!

It's a follow-on of sorts to another project: Electronic Animated Eyes Using Teensy 3.2. The Teensy 3.2 is a very capable microcontroller, and the code for that project squeezed every bit of space and performance from it. So why not convert over to a Pi?

To install:

```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pi-eyes.sh
sudo bash pi-eyes.sh
```
