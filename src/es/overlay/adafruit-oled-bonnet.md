
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
image: 'adafruit-oled-bonnet.png'
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
  '7':
    name: Joystick center
  '13':
    name: Joystick left
  '16':
    name: Joystick right
  '11':
    name: Joystick up
  '15':
    name: Joystick down
  '29':
    name: Button A
  '31':
    name: Button B
i2c:
  '0x3c':
    name: Display Driver
    device: ssd1306
-->
# OLED Bonnet

El bonnet OLED es una simple pantalla de 128x64 para Raspberry Pi con un joystick de 5 direcciones y 2 botones.

La pantalla de 1.3"  está formada por pixels OLED blancos individuales, creando su propia luz por lo que no necesita iluminación trasera. Esto reduce la cantidad de energía necesaria y le da un alto contraste.

Para instalar usa los siguientes comandos:

```bash
sudo apt-get install git python-imaging python-smbus
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install
```
