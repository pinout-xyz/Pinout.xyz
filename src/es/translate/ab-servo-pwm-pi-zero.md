<!--
---
name: Servo PWM Pi Zero
class: board
type: io,motor
formfactor: pHAT
manufacturer: AB Electronics UK
description: 16-channel, 12-bit PWM Controller
url: https://www.abelectronics.co.uk/p/72/servo-pwm-pi-zero
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-servopi-zero.pdf
buy: https://www.abelectronics.co.uk/p/72/servo-pwm-pi-zero
image: 'ab-servo-pwm-pi-zero.png'
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
    alternate: [ '0x40', '0x41', '0x42', '0x43', '0x44', '0x45', '0x46', '0x47', '0x48', '0x49', '0x4A', '0x4B', '0x4C', '0x4D', '0x4E', '0x4F','0x50', '0x51', '0x52', '0x53', '0x54', '0x55', '0x56', '0x57', '0x58', '0x59', '0x5A', '0x5B', '0x5C', '0x5D', '0x5E', '0x5F','0x60', '0x61', '0x62', '0x63', '0x64', '0x65', '0x66', '0x67', '0x68', '0x69', '0x6A', '0x6B', '0x6C', '0x6D', '0x6E', '0x6F','0x70', '0x71', '0x72', '0x73', '0x74', '0x75', '0x76', '0x77', '0x78', '0x79', '0x7A', '0x7B', '0x7C', '0x7D', '0x7E', '0x7F' ]
    name: PCA9685
    device: PCA9685
-->
#Servo PWM Pi Zero

Servo PWM Pi Zero es un controlador PWM de 16 canales y 12 bits para Raspberry Pi, adecuado para controlar LED y servos de control de radio. La placa se basa en el IC del controlador LED PCA9685 PWM I2C de NXT y puede controlar cada una de las 16 salidas con un ciclo de trabajo de 12 bits (4096 pasos) del 0% al 100%.

La frecuencia de salida es programable desde un típico valor de 40Hz a 1000Hz. Cada controlador de salida está programado para ser de drenaje abierto con una capacidad de sumidero de corriente de 22 mA a 5 V o tótem con un sumidero de 22 mA, capacidad de fuente de 10 mA a 5 V. Las resistencias limitadoras de corriente 220R se utilizan en cada canal, lo que le permite conecte servos o LED directamente a las salidas.

Python, C, C ++, Node.js y las bibliotecas IOT de Windows 10 están disponibles en GitHub.
