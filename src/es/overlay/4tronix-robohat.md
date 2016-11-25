<!--
---
name: RoboHat
class: board
type: io,motor
formfactor: HAT
manufacturer: 4tronix
description: Robotics controller HAT
url: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=547
github:
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=547
image: '4tronix-robohat.png'
pincount: 40
eeprom: yes
power:
  '1':
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
  '32':
    name: MotorA_0
    mode: output
  '33':
    name: MotorA_1
    mode: output
  '35':
    name: MotorB_0
    mode: output
  '36':
    name: MotorB_1
    mode: output
  '18':
    name: out0
    mode: output
    active: high
  '22':
    name: out1
    mode: output
    active: high
  '12':
    name: out2
    mode: output
    active: high
  '31':
    name: out3
    mode: output
    active: high
  '7':
    name: in0
    mode: input
  '11':
    name: in1
    mode: input
  '29':
    name: in2
    mode: input
  '13':
    name: in3
    mode: input
  '15':
    name: in4
    mode: input
  '16':
    name: in5
    mode: input
  '38':
    name: Ultrasonic
    mode: input/output
-->
# RoboHat
RoboHat es un controlador completo para pequeños robots. Tiene dos H-bridge completos utilizando DRV8833 para proporcionar hasta 1.5A por canal, un regulador de 5V para general 5V para Raspberry Pi, 6 entradas regulables que aceptan desde 2.5V a 5.5V y los convierten a 3.3V además de 4 salidas de hasta 5V. Todas las entradas/salidas son a través de los 3 pines de tierra, corriente y señal por lo que es fácil conectar sensores de 3 pines o pequeños servos directamente. Además hay un conector para un sensor de distancia ultrasónico HC-SR04 y el circuito necesario para leer su estado con sólo un pin GPIO.
