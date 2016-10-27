<!--
---
name: Witty Pi 2
class: board
type: power,rtc
formfactor: HAT
manufacturer: UUGear
description: Realtime clock and power management for Raspberry Pi
url: http://www.uugear.com/product/wittypi2/
github: https://github.com/uugear/Witty-Pi-2
buy: http://www.uugear.com/product/wittypi2/
image: 'uugear-witty-pi-2.png'
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
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
  '7':
    name: HALT
    mode: input
  '11':
    name: LED
    mode: output
i2c:
  '0x68':
    name: DS3231
    device: DS3231
-->
# Witty Pi 2

Witty Pi 2 es la segunda generación de Witty Pi, añade reloj de tiempo real y gestión de alimentación a Raspberry Pi.

Puedes encender/apagar tu Raspberry Pi con un botón de Witty Pi 2, y se desconectarán la fuente de alimentación y los periféricos USB.

Witty Pi 2 tiene un reloj de tiempo real CR2032 (DS3231), que mantiene de manera precisa el tiempo de Raspberry Pi. Además, un sensor de temperatura mide la temperatura alrededor de Raspberry Pi.

Se puede programar el próximo encendido/apagado mediante software, incluso secuencias complejas mediante script.

Si utilizas un power bank como alimentación, puede mantener el power bank con carga debido a un bajo consumo de corriente. Los nuevos 6 pines hembra añaden opciones de integración/extensión.

Puedes usar estos dos comandos para instalar sofware para Witty Pi 2:

```bash
wget http://www.uugear.com/repo/WittyPi2/installWittyPi.sh

sudo sh installWittyPi.sh
```
Una vez realizada la instalación, reinicia tu Raspberry Pi y Witty Pi 2 estará listo.

Witty Pi 2 funciona con todos los modelos de Raspberry Pi de 40 pines A+/B+/2B/3B/Zero.
