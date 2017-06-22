
<!--
---
name: PiOLED
class: board
type: Display
formfactor: Custom
manufacturer: Adafruit
description: A small 128x32 display for your Pi
url: https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi
github: https://github.com/adafruit/Adafruit_Python_SSD1306
buy: https://www.adafruit.com/product/3527
image: 'adafruit-pi-oled.png'
pincount: 6
eeprom: no
power:
  '1':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x3c':
    name: Display Driver
    device: ssd1306
-->
# PiOLED

The PiOLED is a small 128x32 OLED display designed to sit on top of just the first six pins of the Pi’s Header. It uses I2c to communicate which means there are plenty of spare pins for buttons, LED’s and sensors.

The OLED display has a very high contrast ratio leading to clear and crisp text and images and as the display produces it’s own light this also means the PiOLED is extremely low power.

The display is about 1” in diagonal and allows for 30FPS updates rates allowing for simple animations and the SSD1306 chipset is easily controlled using a simple python library.

To install the necessary software, use the following commands:

```bash
sudo apt-get install git python-imaging python-smbus
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install
```
