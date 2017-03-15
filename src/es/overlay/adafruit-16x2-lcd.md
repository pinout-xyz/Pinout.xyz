<!--
---
name: 16x2 Character LCD
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
#LCD 16x2 caracteres

Esta placa hace sencillo utilizar una pantalla LCD de 16x2 caracteres. La mayoría de LCDs utilizan muchos pines GPIO, pero como esta utiliza I2C sólo necesita dos pines.

El teclado permite introducir datos a la pantalla y viene con una librería Python que hace que sea muy fácil de programar.

El mismo diagrama de pines se aplica para LCD positivo, negativo y normal.

Para instalar:

```bash
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip git
sudo pip install RPi.GPIO
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install
```
