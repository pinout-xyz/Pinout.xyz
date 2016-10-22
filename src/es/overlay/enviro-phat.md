<!--
---
name: Enviro pHAT
class: board
type: adc,sensor
formfactor: pHAT
manufacturer: Pimoroni
description: A package of environmental sensors for IoT projects
url: https://shop.pimoroni.com/products/enviro-phat
github: https://github.com/pimoroni/enviro-phat
buy: https://shop.pimoroni.com/products/enviro-phat
image: 'enviro-phat.png'
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
    mode: i2c
  '5':
    mode: i2c
  '7':
    mode: output
    name: LEDs
i2c:
  '0x1d':
    name: Motion Sensor
    device: LSM303D
  '0x29':
    name: Light/Colour Sensor
    device: TCS3472
  '0x49':
    name: 4-Channel Analog Input
    device: ADS1015
  '0x77':
    name: Temp/Pressure Sensor
    device: BMP280
-->
#Enviro pHAT

Junto con una Pi Zero, Enviro pHAT es un conjunto de sensores asequible, ideal para monitorizar habitáculos de servidores, habitaciones o cualquier cosa que quieras observar. Además incluye una entrada ADC de 4-canales para añadir sensores. Funciona con cualquiera de las versiones de Raspberry Pi de 40 pines - 3/2/B+/A+/Zero.

Especificaciones:

Sensor de temperatura/presión BMP280 (0x77 en el bus i2c)
Sensor de luz y color RGB TCS3472 (0x29 en el bus i2c)
(con dos LEDs para iluminación)
Sensor acelerómetro/magnetómetro LSM303D (0x1d en el bus i2c)
ADC de 12-bit, 4-canales y 3.3v ADS1015 (0x48 en el bus i2c)

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/envirophat | bash
```
Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
from envirophat import light, motion, weather, analog, leds
```
