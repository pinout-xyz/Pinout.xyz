<!--
---
name: PiGlow
class: board
type: led
formfactor: Otro
manufacturer: Pimoroni
description: Simply 18 LEDs in a spiral pattern controllable in Python
url: http://shop.pimoroni.com/products/piglow
github: https://github.com/pimoroni/piglow
buy: http://shop.pimoroni.com/products/piglow
image: 'piglow.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
  '17':
ground:
  '14':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
#PiGlow

PiGlow es una pequeña placa adicional para Raspberry Pi con 18 LEDs controlables individualmente.

La placa usa el chip de 8-bit y 18-canales PWM SN3218 para controlar los LEDs. La comunicación se realiza mediante I2C a través de los GPIO en el bus con dirección 0x54. Cada LED puede configurarse para un valor de PWM entre 0 y 255.

The board uses the SN3218 8-bit 18-channel PWM chip to drive surface mount LEDs. Communication is done via I2C over the GPIO header with a bus address of 0x54. Each LED can be set to a PWM value of between 0 and 255.

Para configurar el módulo  puedes utilizar el instalador online de una línea:

```bash
curl -sS get.pimoroni.com/piglow | bash
```

¡Y sigue las instrucciones!
