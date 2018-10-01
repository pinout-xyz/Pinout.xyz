
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

PiOLED es una pequeña pantalla OLED de 128x32 diseñada para colocarse en los seis primeros pines de Raspberry Pi. usa comunicación I2C por lo que quedan pines libres para botones, LEDs y sensores.

La pantalla OLED tiene un contraste muy alto por lo que da lugar a imágenes y texto nítidos, además al producir su propia luz consume muy poca energía.

La pantalla tiene una diagonal de 1" y se actualiza a 30FPS, permitiendo crear animaciones simples. Además, el chipset SSD1306 es fácil de controlar con un simple librería Python.

Para instalar usa los siguientes comandos:

```bash
sudo apt-get install git python-imaging python-smbus
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install
```
