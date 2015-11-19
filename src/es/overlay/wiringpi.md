<!--
---
name: Pinout del GPIO WiringPi
page_url: wiringpi
github: https://github.com/WiringPi/WiringPi2-Python
url: http://wiringpi.com
pin:
  '3':
    name: WiringPi 8
  '5':
    name: WiringPi 9
  '7':
    name: WiringPi 7
  '8':
    name: WiringPi 15
  '10':
    name: WiringPi 16
  '11':
    name: WiringPi 0
  '12':
    name: WiringPi 1
  '13':
    name: WiringPi 2
  '15':
    name: WiringPi 3
  '16':
    name: WiringPi 4
  '18':
    name: WiringPi 5
  '19':
    name: WiringPi 12
  '21':
    name: WiringPi 13
  '22':
    name: WiringPi 6
  '23':
    name: WiringPi 14
  '24':
    name: WiringPi 10
  '26':
    name: WiringPi 11
  '29':
    name: WiringPi 21
  '31':
    name: WiringPi 22
  '32':
    name: WiringPi 26
  '33':
    name: WiringPi 23
  '35':
    name: WiringPi 24
  '36':
    name: WiringPi 27
  '37':
    name: WiringPi 25
  '38':
    name: WiringPi 28
  '40':
    name: WiringPi 29
-->
#Raspberry Pi WiringPi

###WiringPi es un intento de traer la simplicidad de Arduino a la Raspberry Pi

El objetivo es tener una única plataforma común y set de funciones para acceder a los GPIO's de la Rasberry Pi en distintos lenguajes. WiringPi es una librería hecha en C, pero está disponible tanto para usuarios de Ruby como de Python, que pueden ejecutar "gem install wiringpi" o "pip install wiringpi2" respectivamente.

Los usuarios de Python deben tener cuidado con el 2 al final; la librería WiringPi2-Python finalmente proporciona un montón de funcionalidades existentes a Python, y también incluyendo algunas completamente nuevas.

##Empezando con WiringPi

WiringPi utiliza su propio sistema de numeración de pines, aquí aprenderás como WiringPi los numera, que hacen esos pines y como hacer brillantes cosas con ellos desde Python o Ruby.

Instalar WiringPi en Python no puede ser más fácil, solo:

```bash
sudo pip install wiringpi2
```

Para más información sobre WiringPi deberías visitar la página oficial de WiringPi.
