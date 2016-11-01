<!--
---
name: RTC Pi Zero
class: board
type: rtc
formfactor: pHAT
manufacturer: AB Electronics
description: Real-Time Clock Module for the Raspberry Pi
url: https://www.abelectronics.co.uk/p/70/RTC-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/70/RTC-Pi-Zero
image: 'ab-rtc-pi-zero.png'
pincount: 40
eeprom: no
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
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x68':
    name: DS1307
    device: DS1307
-->
#RTC Pi Zero

RTC Pi Zero es una reloj de tiempo real con batería para Raspberry Pi Zero. mantiene el tiempo de Raspberry Pi mientras está apagada y permite recuperar la fecha actual una vez encendida de nuevo

RTC Pi Zero se alimenta a través de los pines GPIO de Raspberry Pi, además permite conectar otros dispositivos. RTC PI Zero utiliza el reloj de tiempo real DS1307 y la batería CR2032 par amanetner la fecha cuando la alimentación no está disponible.

A diferencia de otros modulos RTC basados en DS1307, RTC Pi Zero además incluye un conversor I2C lógico que permite conectar otros dispositivos I2C de 5V a Raspberry Pi.

Librerias Arduino, C, Node.js, Windows 10 IOT, Python 2 y Python 3 librerías disponibles en GitHub.
