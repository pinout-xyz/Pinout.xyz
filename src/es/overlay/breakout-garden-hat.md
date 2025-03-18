<!--
---
name: Breakout Garden HAT
class: board
type: io
formfactor: HAT
manufacturer: Pimoroni
description: Break out your i2c bus to 6 edge connectors.
url: https://shop.pimoroni.com/products/breakout-garden-hat
github: https://github.com/pimoroni/breakout-garden
buy: https://shop.pimoroni.com/products/breakout-garden-hat
image: 'breakout-garden-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
ground:
  '9':
  '25':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Interrupt
    mode: input
  '36':
    name: EEPROM WP
    mode: output
    active: low
-->
# Breakout Garden HAT

Breakout Garden HAT convierte el bus i2c de tu Raspberry Pi en 6 conectores válidos para placas de Pimoroni.

Esto significa que puedes utilizar tus diseños basados en estas placas sin soldar o sin tener problemas de conexión, programar y probar tu código antes de montar el modelo final.

La parte superior es un plano de tierra, por lo que sólo necesitarás utilizar un pin de tierra de tu Raspberry Pi (a elegir entre los señalados). La línea de 5V es regulada a 3V3. Los pines de 3v3 sólo se utilizan para la EEPROM por lo que puedes obviarlos.

Para realizar conexiones o utilizar con algo como Arduino puedes utilizar las conexiones incluidas de SDA, SCL, INT, GND y 5 V.

Para ponerlo en funcionamiento puedes utilizar el instalador de una línea:

```bash
curl -sS https://get.pimoroni.com/breakoutgarden | bash
```

¡y sigue las instrucciones!
