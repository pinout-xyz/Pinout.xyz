<!--
---
name: I2C
class: interface
type: pinout
description: Raspberry Pi I2C pins
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
#I2C - Inter Integrated Circuit
---
###I2C pins in BCM mode are: 2, 3
###I2C pins in WiringPi are: 8, 9
---
The Raspberry Pi's I2C pins are an extremely useful way to talk to many different types of external peripheral; from the MCP23017 digital IO expander, to a connected ATmega.

The I2C pins include a fixed 1.8 kohms pull-up resistor to 3.3v. This means they are not suitable for use as general purpose IO where a pull-up is not required.

You can verify the address of connected I2C peripherals with a simple one-liner:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

You can then access I2C from Python using the smbus library:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```
