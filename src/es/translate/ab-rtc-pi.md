<!--
---
name: RTC Pi
class: board
type: rtc
formfactor: pHAT
manufacturer: AB Electronics UK
description: Real-Time Clock Module for the Raspberry Pi
url: https://www.abelectronics.co.uk/p/70/rtc-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-rtcpi-v3.pdf
buy: https://www.abelectronics.co.uk/p/70/rtc-pi
image: 'ab-rtc-pi.png'
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
#RTC Pi

RTC Pi es un módulo de reloj en tiempo real respaldado por batería para Raspberry Pi. Realiza un seguimiento de la hora mientras Raspberry Pi está apagado y permite que Raspberry Pi recupere la fecha y hora actuales del RTC Pi cuando se vuelve a encender.

RTC Pi se alimenta a través de Raspberry Pi utilizando el puerto GPIO y los pines extendidos en el conector GPIO le permiten combinar RTC Pi junto con otras placas de expansión. RTC Pi utiliza el reloj de tiempo real RTC DS1307 y una batería CR2032 para mantener la fecha y la hora cuando la alimentación del sistema principal no está disponible.

A diferencia de la mayoría de los otros módulos RTC basados en DS1307, RTC Pi también incluye un convertidor de nivel lógico I2C que le permite conectar otros dispositivos I2C de 5V a su Raspberry Pi.

Python, C, C ++, Node.js y las bibliotecas IOT de Windows 10 están disponibles en GitHub.
