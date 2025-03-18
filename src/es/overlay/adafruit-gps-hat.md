<!--
---
name: Ultimate GPS HAT
class: board
type: gps,rtc
formfactor: HAT
manufacturer: Adafruit
description: Add precision time and location to your Raspberry Pi
url: https://learn.adafruit.com/adafruit-ultimate-gps-hat-for-raspberry-pi
schematic: https://learn.adafruit.com/assets/21938
buy: https://www.adafruit.com/products/2324
image: 'adafruit-gps-hat.png'
pincount: 40
eeprom: no
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
  '7':
    name: PPS
  '8':
    mode: UART
  '10':
    mode: UART
-->
# Ultimate GPS HAT

Ultimate GPS HAT (Sombrero definitivo de GPS) de Adafruit le proporciona a tu Raspberry Pi una ubicación y tiempo precisos.

Características:

* Sensibilidad: 165 dBm, Tasa de refresco: 10 Hz, Canales: 66 
* Consumo de potencia de sólo 20mA 
* Reloj de tiempo real integrado (RTC)
* Señal PPS al obtener la ubicación
* Funciona hasta una altitud de ~32Km
* Antena de conexión interna + conexión U.FL para una antena exterior activa
* LED que indica cuando el GPS obtiene la ubicación actual
* Conexiones para todos los pins extra del Raspberry Pi
* Área para prototipos que permite agregar LEDs, sensores y más
