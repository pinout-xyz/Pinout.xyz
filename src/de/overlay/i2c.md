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

Der I2C-Bus des Raspberry Pi ist sehr praktisch um mit vielen unterschiedlichen Bausteinen
zu kommunizieren - egal ob z.B. ein MCP23017 als digitale I/O-Erweiterung oder sogar ein ATmega. 

Die Adresse eines angeschlossenen I2C-Bausteins kann mit einem einfachen Einzeiler überprüft werden:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

GPIO0 und GPIO1 - I2C0 - können als alternativer I2C bus verwendet werden, typischerweise sind diese in Verwendung um das EEPROM von Hats zu lesen.
