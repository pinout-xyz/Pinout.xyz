<!--
---
name: I2C
description: Raspberry Pi pin i2c
pincount: 2
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

-->
#I2C - Inter Integrated Circuit

L'I2C del Raspberry è un modo estremamente utile per comunicare con molti tipi diversi di periferiche esterne, dall'expander digitale MCP23017, ad un ATmega collegato.

I pin I2C includono una resistenza pull-up da 1.8 KOhm a 3.3V, il che significa che non sono adatti ad un IO generico dove una resistenza pull-up non è richiesta.

Puoi controllare l'indirizzo delle periferiche I2C collegate con una singola riga di codice:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

Puoi accedere ad i2c da Python usando la libreria smbus:

```bash
sudo apt-get install python-smbus
```

E poi sempre in Python:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```