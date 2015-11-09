<!--
---
name: I2C
description: broches i2c de la Raspberry Pi
pin:
  '3':
    name: Données
    direction: both
    active: high
  '5':
    name: Horloge
    direction: both
    active: high
  '27':
    name: EEPROM Données
    direction: both
    active: high
  '28':
    name: EEPROM Horloge
    direction: both
    active: high

-->
#I2C (Inter Integrated Circuit)

I2C est un moyen très pratique pour communiquer avec de multiples périphériques, un MCP23017 IO expander digital, un microprocesseur ATmega connecté à la Raspberry Pi, etc.

Pour vérifier la présence d'un périphérique sur le bus i2c, exécutez simplement les commandes suivantes:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

Et pour un accès depuis Python (en passant par la bibliothèque logicielle externe 'smbus'):

```bash
sudo apt-get install python-smbus
```

Puis:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```