<!--
---
name: I2C
class: interface
type: pinout
description: Pines de i2c de Rasberry Pi
url: http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
pin:
  '3':
    name: Datos
    direction: both
    active: high
  '5':
    name: Reloj
    direction: both
    active: high
  '27':
    name: Datos EEPROM
    direction: both
    active: high
  '28':
    name: Reloj EEPROM
    direction: both
    active: high
  '7':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c3) and Pi 5 (i2c2)
  '29':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c3) and Pi 5 (i2c2)
  '31':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c3)
  '26':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c3)
  '24':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c0)
  '21':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c4) and Pi 5 (i2c0)
  '19':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c1)
  '23':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c1)
  '32':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c2)
  '33':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c5) and Pi 5 (i2c2)
  '15':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 4 (i2c6) and Pi 5 (i2c3)
  '16':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 4 (i2c6) and Pi 5 (i2c3)
  '8':
    name: I2C SDA
    direction: both
    active: high
    supported: Pi 5 (i2c3)
  '10':
    name: I2C SCL
    direction: both
    active: high
    supported: Pi 5 (i2c3)
-->
# I2C - Inter Integrated Circuit

Los pines de I2C de Raspberry Pi son una manera extremadamente útil de comunicarse con distintos tipos de periféricos externos, desde el
expansor de puertos digital MCP23017, hasta un ATmega conectado.

Puedes verificar la dirección de los dispositivos I2C conectados con este simple comando:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```
