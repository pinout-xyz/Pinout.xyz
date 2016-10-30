<!--
---
name: Picon Zero
class: board
type: motor
formfactor: pHAT
image: '4tronix-picon-zero.png'
manufacturer: 4tronix
description: A robot controller board for the Raspberry Pi
url: http://4tronix.co.uk/piconzero/
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=552
pincount: 40
eeprom: no
power:
  '2':
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
  '38':
    name: Ultrasonic
    mode: input/output
i2c:
  '0x22':
    name: PiconZero
    device: ATMega328
-->
#Picon Zero

Picon Zero es una placa adicional para Raspberry Pi, con el mismo tamaño que Raspberry Pi Zero por lo que es ideal como pseudo-Hat (pHat) para Pi Zero. Sin embargo, se puede usar en cualquier Raspberry Pi con 40 pines GPIO.

Además de 2 controladores de motores H-Bridge, Picon Zero cuenta con pines de entrada y salida que pueden configurarse de distinta manera, permitiendo añadir entradas analógicas o salidas neopixel a Raspberry Pi, sin necesidad de software complicado o controladores específicos en el kernel. Cuenta además con una interfaz para un sensor HC-SR04 ultrasónico de distancia, permitiendo acceder a 5 pines GPIO de Raspberry Pi para el uso que quieras.
