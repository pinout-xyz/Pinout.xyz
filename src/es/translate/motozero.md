<!--
---
name: MotoZero
class: board
type: motor
formfactor: pHAT
manufacturer: PiHut
description: Controla 4 motores desde tu Raspberry Pi
url: https://thepihut.com/products/motozero
buy: https://thepihut.com/products/motozero
image: 'motozero.png'
pincount: 40
eeprom: no
power:
  '2':
  '4':
ground:
  '20':
  '39':
pin:
  '11':
    name: "Motor 2 EN"
  '12':
    name: "Motor 4 -"
  '13':
    name: "Motor 1 -"
  '15':
    name: "Motor 2 -"
  '16':
    name: "Motor 3 +"
  '18':
    name: "Motor 1 +"
  '22':
    name: "Motor 4 EN"
  '29':
    name: "Motor 1 EN"
  '31':
    name: "Motor 2 +"
  '32':
    name: "Motor 3 EN"
  '33':
    name: "Motor 4 +"
  '36':
    name: "Motor 3 -"
-->
# MotoZero

El MotoZero es una sencilla placa controladora de motores para Raspberry Pi que te permite controlar hasta 4 motores de forma independiente.
Con un simple control por GPIO y su propia entrada en la biblioteca GPIO Zero, es una de las formas más fáciles de controlar muchos motores en tu Raspberry Pi.

Características:

* Controla 4 motores de forma independiente, tanto hacia adelante como hacia atrás
* Contrólalos con código GPIO básico de encendido/apagado, o usando la biblioteca GPIO Zero
* Los terminales llevan las salidas de los motores al borde de la placa
* Diodos integrados de protección contra la tensión de retorno
* Compatible con todos los modelos de Raspberry Pi de 40 pines
