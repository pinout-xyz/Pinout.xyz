<!--
---
name: I2C
class: interface
type: pinout
description: Raspberry Pi pin i2c
url: http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
pin:
  '3':
    name: Dati
    direction: both
    active: high
  '5':
    name: Clock
    direction: both
    active: high
  '27':
    name: Dati EEPROM
    direction: both
    active: high
  '28':
    name: Clock EEPROM
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

L'I2C del Raspberry è un modo estremamente utile per comunicare con molti tipi diversi di periferiche esterne, dall'expander digitale MCP23017, ad un ATmega collegato.

I pin I2C includono una resistenza pull-up da 1.8 KOhm a 3.3V, il che significa che non sono adatti ad un IO generico dove una resistenza pull-up non è richiesta.

Puoi controllare l'indirizzo delle periferiche I2C collegate con una singola riga di codice:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

