<!--
---
name: LCD+Keypad Kit
class: board
type: display
formfactor: Custom
manufacturer: Adafruit
description: 16x2 character LCD with 5 buttons and RGB backlight
url: https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi
github: https://github.com/adafruit/Adafruit_Python_CharLCD
schematic: https://learn.adafruit.com/assets/3861
buy: https://www.adafruit.com/categories/808
image: 'adafruit-lcd-keypad-kit.png'
pincount: 26
eeprom: no
power:
  '2':
  '4':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x20':
    name: MCP23017
    device: MCP23017
-->
#LCD+Keypad Kit

Features
* 16x2 character LCD with HD44780 controller chip
* 5 buttons (Select, Up, Down, Left, Right)
* RGB or monochrome LED backlight (depending on model)
* all of the above connected to I2C via an MCP23017 Port Expander
* I2C address configurable via solder pads on back (default 0x20)
* works with any model of Raspberry Pi

This board is sold as a kit and requires soldering.

Besides the official [Python library](https://github.com/adafruit/Adafruit_Python_CharLCD),
there is also an unofficial [Haskell library](https://hackage.haskell.org/package/pi-lcd).
