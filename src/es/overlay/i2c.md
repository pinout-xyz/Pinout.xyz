<!--
---
description: Pines de i2c de Rasberry Pi
pin:
  '3':
    name: Datos
  '5':
    name: Reloj
  '27':
    name: Datos EEPROM
  '28':
    name: Reloj EEPROM
-->
# I2C - Inter Integrated Circuit

Los pines de I2C de Raspberry Pi son una manera extremadamente útil de comunicarse con distintos tipos de periféricos externos, desde el
expansor de puertos digital MCP23017, hasta un ATmega conectado.

Puedes verificar la dirección de los dispositivos I2C conectados con este simple comando:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```
