<!--
---
name: I2C
description: Pines de i2c de Rasberry Pi
pin:
  '3':
    name: Datos
    direction: ambas
    active: alto (encendido)
  '5':
    name: Reloj
    direction: ambas
    active: alto (encendido)
  '27':
    name: Datos EEPROM
    direction: ambas
    active: alto (encendido)
  '28':
    name: Reloj EEPROM
    direction: ambas
    active: alto (encendido)

-->
#I2C - Inter Integrated Circuit

Los pines de I2C de Raspberry Pi son una manera extremadamente útil de comunicarse con distintos tipos de periféricos externos, desde el
expansor de puertos digital MCP23017, hasta un ATmega conectado.

Puedes verificar la dirección de los dispositivos I2C conectados con este simple comando:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```
Puedes acceder al bus i2c desde Python usando la librería smbus:

```bash
sudo apt-get install python-smbus
```

Y entonces en Python:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```
