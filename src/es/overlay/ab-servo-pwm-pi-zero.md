<!--
---
name: Servo PWM Pi Zero
class: board
type: io,motor
formfactor: pHAT
manufacturer: AB Electronics
description: 16-channel, 12-bit PWM Controller
url: https://www.abelectronics.co.uk/p/72/Servo-PWM-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/72/Servo-PWM-Pi-Zero
image: 'ab-servo-pi-zero.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '14':
  '20':
  '30':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: OE
    mode: output
    active: high
i2c:
  '0x40':
    name: PCA9685
    device: PCA9685
-->
#Servo PWM Pi Zero

Servo PWM Pi Zero es un controlador PWM de 16-canales, 12-bit par Raspberry Pi, útil para controlar LEDs o servos a distancia. Basado en el controlador PCA9685 PWM I2C LED de NXT, puede controlar hasta 16 salidas con 12 bit (4096 pasos) en diclos de 0 % a 100 %.

La frecuencia de salida se puede programar desde 40Hz a 1000Hz. Cada controlador de salida se puede programar para ser open-drain con una corriente de 22mA y 5V o como polo con 22 mA, capacidad de fuente de 10 mA y 5 V. Se utilizan resistencias de 220R en cada canal para permitir conectar servos o LEDs, directamente a las salidas.

Librerias Arduino, C, Node.js, Windows 10 IOT, Python 2 y Python 3 disponibles en GitHub.
