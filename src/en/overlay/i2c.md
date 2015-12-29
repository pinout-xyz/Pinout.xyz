<!--
---
type: info
name: I2C
description: Raspberry Pi i2c pins
pincount: 2
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
#I2C - Inter Integrated Circuit

The Raspberry Pi's I2C pins are an extremely useful way to talk to many different types of external peripheral; from the MCP23017 digital IO expander, to a connected ATmega.

The i2c pins include a fixed 1.8 kohms pull-up resistor to 3.3v. This means they are not suitable for use as general purpose IO where a pull-up is not required.

You can verify the address of connected I2C peripherals with a simple one-liner:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

You can access i2c from Python using the smbus library:

```bash
sudo apt-get install python-smbus
```

And then in Python:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```
