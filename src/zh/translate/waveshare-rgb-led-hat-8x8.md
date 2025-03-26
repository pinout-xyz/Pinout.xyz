<!--
---
name: True Color RGB LED HAT
class: board
type: led
formfactor: HAT
manufacturer: Waveshare
description: True color RGB LED HAT with 8x8 pixels
url: http://www.waveshare.com/wiki/RGB_LED_HAT
buy: https://www.waveshare.com/product/mini-pc/raspberry-pi/hats/rgb-led-hat-b.htm
schematic: https://www.waveshare.com/w/upload/b/bf/RGB_LED_HAT_Schematic_.pdf
image: 'waveshare-rgb-led-hat-8x8.png'
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
-->
# Waveshare True Color RGB LED HAT 8x8

This RGB LED HAT (B) can be easily attached on top of the Raspberry Pi to display colourful effect, and controlled by only one signal pin.

* Supports any revision of Raspberry Pi (directly-pluggable)
* Onboard 8 × 8 RGB LED (WS2812B)
* Control pin is configurable via jumpers (0Ω resistor) (BCM 18, 12, 13 or 19)
* Break out control pins, easy for working with other MCUs
* Comes with development resources and manual (examples in Python and Web control)