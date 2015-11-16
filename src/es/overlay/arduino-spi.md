<!--
---
name: Arduino SPI
description: Programa un Arduino con el SPI de Raspberry Pi
pin:
  '19':
    name: MOSI
    direction: salida
    active: alto (encendido)
    description: Master Out / Slave In
  '21':
    name: MISO
    direction: entrada
    active: alto (encendido)
    description: Master In / Slave Out
  '23':
    name: SCKL
    direction: salida
    active: alto (encendido)
    description: Reloj
  '24':
    name: CE0
    direction: salida
    active: alto (encendido)
    description: Arduino Reset
-->
#ATmega 328p / Arduino sobre SPI

###¿Sabías que tu Pi puede alimentar y programar un ATmega 328p/Arduino directamente, con solo unos pocos cables, una placa de pruebas, un cristal de 16Mhz y algunos condensadores de 22pF?

Lee mi [tutorial completo de Pico PiDuino (en inglés)](http://pi.gadgetoid.com/article/building-the-pico-piduino), para empezar por solamente un poco más de &pound;5

Necesitarás instalar el [AVRDude modificado de Gordon](https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/).

Conecta 8/CE0 al pin de Reset/RST de tu ATmega, 9/MISO al pin D12, 10/MOSI al pin D11 y 11/SCLK al pin D13.

Alimenta el ATmega con los pines de 3.3v y GND de tu Pi, y estás listo para empezar.

Asegúrate de no tener funcionando ningún controlador travieso de algún dispositivo SPI, y comprueba que está bien conectado usando:

```bash
avrdude -p m328p -c gpio
```

Para empezar a compilar programas de Arduino desde la terminal:

```bash
sudo apt-get install arduino arduino-mk
```

Este Makefile básico debería ayudarte a empezar. Crea un programa básico, llámalo mysketch.ino y ejecuta:

```bash
export BOARD=atmega328
make
avrdude -p m328p -c gpio -e -U flash:w:build-cli/Arduino.hex
```
