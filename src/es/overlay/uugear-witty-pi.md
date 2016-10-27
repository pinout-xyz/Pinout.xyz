<!--
---
name: Witty Pi
class: board
type: power,rtc
formfactor: HAT
manufacturer: UUGear
description: Realtime clock and power management for Raspberry Pi
url: http://www.uugear.com/product/witty-pi-realtime-clock-and-power-management-for-raspberry-pi/
github: https://github.com/uugear/Witty-Pi
buy: http://www.uugear.com/product/witty-pi-realtime-clock-and-power-management-for-raspberry-pi/
image: 'uugear-witty-pi.png'
pincount: 40
eeprom: no
power:
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
  '8':
    name: TXD
    mode: other
i2c:
  '0x68':
    name: DS1307
    device: DS1307
-->
#Witty Pi

Witty Pi es una placa adicional que añade reloj de tiempo real y gestión de alimentación a Raspberry Pi..

Puedes encender/apagar tu Raspberry Pi con un botón de Witty Pi, y se desconectarán la fuente de alimentación y los periféricos USB.

Witty Pi tiene un reloj de tiempo real CR2032 (DS1337), que mantiene el tiempo de Raspberry Pi. Se puede programar el próximo encendido/apagado mediante software, incluso secuencias complejas mediante script.

Puedes usar estos dos comandos para instalar sofware para Witty Pi:

```bash
wget http://www.uugear.com/repo/WittyPi/installWittyPi.sh

sudo sh installWittyPi.sh
```
Una vez realizada la instalación, reinicia tu Raspberry Pi y Witty Pi 2 estará listo.

Witty Pi funciona con todos los modelos de Raspberry Pi de 40 pines A+/B+/2B/3B/Zero.
