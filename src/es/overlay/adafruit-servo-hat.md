<!--
---
name: Servo/PWM HAT
class: board
type: io,motor
formfactor: HAT
manufacturer: Adafruit
description: A 16-Channel Servo / PWM HAT for Raspberry Pi
url: https://www.adafruit.com/product/2327
github: https://github.com/adafruit/Adafruit_Python_PCA9685
buy: https://www.adafruit.com/product/2327
image: 'adafruit-servo-hat.png'
pincount: 40
eeprom: yes
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
i2c:
  '0x40':
    name: PWM Controller
    device: pca9685
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
-->
#Servo/PWM HAT

El Servo/PWM HAT de Adafruit permite controlar 16 salidas servo o PWM a través de I2C con sólo 2 pines.
El controlador PWM incluido en la placa controlará los 16 canales simultáneamente sin ningún procesamiento adicional por parte de Raspberry Pi. Utilizando un sistema de direcciones binaria, mediante cables soldados al PCB, es posible acoplar hasta 62 HATs para controlar hasta 992 servos, utilizando solo el puerto I2C.

Nota importante: los servos pueden utilizar mucha energía y no es buena idea utilizar el puerto de 5V de Raspberry Pi para alimentarlos. Interferencias eléctricas y apagones debido al excesivo consumo eléctrico pueden dar lugar a un comportamiento extraño de Raspberry Pi, reinicios y/o sobrecalentamiento. ¡Mantén la alimentación de Raspberry Pi y la de los servos separadas!
