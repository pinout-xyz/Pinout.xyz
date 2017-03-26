<!--
---
name: PiRTC
class: board
type: rtc
formfactor: Otro
manufacturer: Adafruit
description: Add a simple RTC to your Pi
url: https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-up-and-test-i2c
buy: https://www.adafruit.com/products/3386
image: adafruit-pi-rtc.png
pincount: 6
eeprom: no
power:  
  '1':     
ground:
  '6':    
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x68':
    name: PCF8523
    device: PCF8523
-->
#PiRTC

Es un gran reloj de tiempo real (RTC) respaldado por batería que permite mantener la hora de Raspberry Pi incluso sin corriente, para muestreo de datos, construir relojes, etc. Equipado con el RTC PCF8523, funciona bien con Raspberry Pi y tiene soporte nativo a nivel de kernel.

Mantendrá la hora durante unos 5 años. PCF8523 es simple y barato, pero no tiene gran precisión. Puede perder un segundo o dos por día.
