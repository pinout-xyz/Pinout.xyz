<!--
---
name: RTC Pi Plus
class: board
type: rtc
formfactor: HAT
manufacturer: AB Electronics
description: Real-Time Clock Module for the Raspberry Pi
url: https://www.abelectronics.co.uk/p/52/RTC-Pi-Plus
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/52/RTC-Pi-Plus
image: 'ab-rtc-pi-plus.png'
pincount: 40
eeprom: no
power: 3v3,5v
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
#RTC Pi Plus

RTC Pi Plus es un módulo de reloj de tiempo real, con batería incluída, diseñado para funcionar con Raspberry Pi A+, B+ y 2 modelo B. Registra el tiempo mientras Raspberry Pi está apagada y permite a Raspberry Pi recuperar la fecha una vez encendida.

RTC Pi Plus se alimenta a partir de los pines GPIO de Raspberry Pi y permite añadir otras placas. RTC Pi Plus usa el reloj de tiempo real DS1307 RTC y una batería CR2032 para mantener la fecha cuando la fuente de alimentación principal no está disponible.

A diferencia de otros módulos RTC basados en DS1307, RTC Pi Plus addemás incluye un conversor de nivel lógico I2C que permite conectar otros dispositivos I2C de 5V a Raspberry Pi.

Liberías Python 2 and 3 libraries disponibles en GitHub.
