<!--
---
name: Duino
class: board
type: mcu,io
formfactor: Otro
manufacturer: RasPiO
description: Arduino Programming on the Raspberry Pi
url: http://rasp.io/duino/
github: https://github.com/raspitv/raspio_duino
buy: https://ryanteck.uk/add-ons/58-raspio-duino.html
image: 'raspio-duino.png'
pincount: 26
eeprom: no
power:
  '1':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '8':
    mode: uart
  '10':
    mode: uart
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
install:
  'devices':
    - 'spi'
-->
#Duino

RasPiO Duino es una pequeña placa adicional para Raspberry Pi. Tiene funciones similares a Arduino Uno, con un ATMega 328P-PU como corazón, pero es completamente programable desde Raspberry Pi. Una vez programado, puede desconectarse de Raspberry Pi y usarse de manera independiente.

Los pines del ATMega están dividido es grupos de tres. El ATMega328 tiene un conversor analógico a digital de 6 canales, y 14 pines digitales I/O, 6 de los cuales pueden utilizarse para PWM. Los puertos GPIO de Raspberry Pi también están disponibles además de un área de prototipado de 72 puntos raíles con tierra, 3V3 ty 5V, en los que puedes añadir tus componentes.

Nota: RasPiO Duino funciona a 3v3 y 12 MHz (no 5V y 16 MHz como Uno).
