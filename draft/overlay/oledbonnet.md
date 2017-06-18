
<!--
---
name: OLED Bonnet
class: board
type: Display
formfactor: pHAT
manufacturer: Adafruit
description: A 128x64 display with jostick and buttons for your Pi
url: https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi
github: https://github.com/adafruit/Adafruit_Python_SSD1306
buy: https://www.adafruit.com/product/3531
image: 'oledbonnet.png'
pincount: 40
eeprom: no
power:
  '1': 
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
  
  ’27’: 
    
    name: left
  
  ’23’: 
    
    name: right
  
  ‘4’: 
    name:center
  
  ’17’: 
    name:up
  
  ’22’: 
    name:down  
  
  ‘5’: 
    name:Button A
  
  ‘6’: 
    name:Button B
 

i2c:
  '0x3c':
    name: Display Driver
    device: ssd1306

-->
# OLED Bonnet

The OLED Bonnet is a simple 128x64 display for Raspberry pi with a 5-way joystick and 2 pushbuttons.

The 1.3" screen is made of 128x64 individual white OLED pixels and because the display makes its own light, 
no backlight is required. This reduces the power required to run the OLED and is why the display has such high contrast

```bash
sudo apt-get install python-imaging python-smbus
sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
```



