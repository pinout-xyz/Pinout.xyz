<!--
---
name: I2C
class: interface
type: pinout
description: Raspberry Pi I2C Anschlüsse
url: http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
pin:
  '3':
    name: Data
    direction: both
    active: high
  '5':
    name: Clock
    direction: both
    active: high
  '27':
    name: EEPROM Data
    direction: both
    active: high
  '28':
    name: EEPROM Clock
    direction: both
    active: high

-->
# I2C - Inter Integrated Circuit

Der I2C-Bus des Raspberry Pi ist sehr praktisch um mit vielen unterschiedlichen Bausteinen
zu kommunizieren - egal ob z.B. ein MCP23017 als digitale I/O-Erweiterung oder sogar ein ATmega. 

Die Adresse eines angeschlossenen I2C-Bausteins kann mit einem einfachen Einzeiler überprüft werden:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

Den I2C-Bus kann man von Python aus über die smbus-Library ansteuern:

```bash
sudo apt-get install python-smbus
```

...und dann in Python:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```
