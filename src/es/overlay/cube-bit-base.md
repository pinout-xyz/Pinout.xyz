<!--
---
name: cube:bit Base
class: board
type: other
formfactor: Custom
manufacturer: 4tronix
description:  Base for your Cube:Bit allowing easy connection of power and signal and directly able to plug in a Raspberry Pi Zero.
url: https://shop.4tronix.co.uk/products/cube-bit-base-for-power-microbit-and-raspberry-pi-cubebit
buy: https://shop.4tronix.co.uk/products/cube-bit-base-for-power-microbit-and-raspberry-pi-cubebit
image: 'cube-bit-base.png'
pincount: 40
eeprom: no

pin:

power:
  '2':

pin:
  '12':
    name: Data
    direction: output
    mode: pwm
    description: WS2812 Data

-->
# cube:bit Base

Basse para tu Cube:Bit permitiendo una conexión fácil de corriente y señal, que se puede conectar directamente a tu Raspberry Pi Zero.

Tiene un conector de 40 pines GPIO al que se le puede conectar una Raspberry Pi que será alimentada por los 5V y conectada en el GPIO 12 (pin 18) al array neopixel. Este es el pin estándar para controlar neopixels en Raspberry Pi. No hay espacio para conectar una Raspberry Pi de tamaño completo, pero podría hacerse con un cable.
