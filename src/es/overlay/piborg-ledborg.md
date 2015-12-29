<!--
---
name: PiBorg LEDBorg
description: Un único LED RGB para tu Raspberry Pi
pincount: 26
pin:
  '11':
    name: Red LED
    direction: salida
    active: alto (encendido)
    description: LED Rojo PiBorg
  '13':
    name: Green LED
    direction: entrada
    active: alto (encendido)
    description: LED Verde PiBorg
  '15':
    name: Blue LED
    direction: salida
    active: alto (encendido)
    description: LED Azul PiBorg
-->
###El PiBorg LedBord es una placa con un LED RGB ultra-brillante para la Rasberry Pi.

PiBorg tiene su propio controlador, así que no necesitas controlarlo manualmente.

Si quieres un mucho, mucho mayor rango de colores, puedes controlarlo manualmente utilizando softPwm en WiringPi. Los pines para esto son los siguientes:

WiringPi pin 0: LED Rojo
WiringPi pin 2: LED Verde
WiringPi pin 3: LED Azul

Esto es fácil usando WiringPi en Python:


```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(0,0,100)
wiringpi.softPwmCreate(2,0,100)
wiringpi.softPwmCreate(3,0,100)

# Violeta!
wiringpi.softPwmWrite(3,100) # Azul al máximo
wiringpi.softPwmWrite(0,100) # Rojo al máximo
wiringpi.softPWMWrite(2,0)	 # No verde
```
