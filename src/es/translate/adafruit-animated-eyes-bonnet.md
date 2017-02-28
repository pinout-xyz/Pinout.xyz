<!--
---
name: Animated Eyes Bonnet
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
-->
Snake Eyes Bonnet (Gorro ojos de serpiente) es un accesorio para Raspberry Pi que permite controlar dos pantallas OLED o TFT LCD de 128x128 píxeles y cuenta con cuatro entradas analógicas para sensores.

Es perfecto para hacer máscaras de cosplay, utilería, esculturas escalofriantes en halloween, animatrónicos, robots... ¡Cualquier cosa que necesite un par de ojos animados!

Surgió como la continuación de otro proyecto: Ojos Animados Electrónicos Usando Teensy 3.2. El Teensy 3.2 es un microcontrolador bastante capaz y el código de ese proyecto le exprimió cada gota de espacio y desempeño. Así que, ¿por qué no convertirlo al Pi?

Para instalar:

```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pi-eyes.sh
sudo bash pi-eyes.sh
```
