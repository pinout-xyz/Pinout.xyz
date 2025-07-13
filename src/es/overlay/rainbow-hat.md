<!--
---
name: Rainbow HAT
class: board
type: cap,display,led,multi,sensor
formfactor: HAT
manufacturer: Pimoroni
description: Sensors and IO for Android Things
url: http://blog.pimoroni.com/android-things-launch/
github: https://github.com/pimoroni/rainbow-hat
buy: https://shop.pimoroni.com/products/rainbow-hat-for-android-things
image: 'rainbow-hat.png'
pincount: 40
eeprom: yes
power:
  '4':
  '17':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '33':
    name: Buzzer
    mode: pwm
  '31':
    name: Red/Left LED
    mode: output
    active: high
  '35':
    name: Green/Middle LED
    mode: output
    active: high
  '37':
    name: Blue/Right LED
    mode: output
    active: high
  '40':
    name: Touch A
    mode: input
    active: low
  '38':
    name: Touch B
    mode: input
    active: low
  '36':
    name: Touch C
    mode: input
    active: low
i2c:
  '0x70':
    name: Matrix Driver
    device: HT16K33
  '0x77':
    name: Barometer
    device: BMP280
-->
# Rainbow HAT para Android Things™

Rainbow HAT tiene varios sensores, entradas y displays para explorar Android Things™. Utilízalo como estación meteorológica, reloj, cronómetro, efectos de luz o muchas otras cosas.

* Siete LEDs APA102 multicolor
+ Cuatro displays de 14 segmentos alfanuméricos (LEDs verdes)
* Controlador HT16K33 para los displays
* Tres botones táctiles capacitivos
* Controlador capacitivo Atmel QT1070
* Sensor de temperatura y presión BMP280
* LEDs azul, verde y rojo
* Piezo zumbador

Para poner el HAT en funcionamiento puedes utilizar nuestro instalador de una línea:

```bash
curl https://get.pimoroni.com/rainbowhat | bash
```
