<!--
---
name: Adafruit 16x2 Character LCD
class: board
type: display
formfactor: Custom
manufacturer: Adafruit
description: 16x2 Character LCD and Keypad
url: https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi
buy: https://www.adafruit.com/products/1109
image: adafruit-16x2-lcd.png
pincount: 26
eeprom: no
power:
  '2':
ground:
  '6':
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
#Adafruit 16x2 Character LCD

This plate makes it easy to use a 16x2 Character LCD. Most character LCDs use lots of GPIO pins, but since this uses I2C you only need two pins. 

The keypad gives you buttons to input to the display and it comes with a  python library to make it super easy to program.

Note that the same pinout applies to both positive, negative and normal LCD.

To install:

```bash
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip git
sudo pip install RPi.GPIO
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install
```
