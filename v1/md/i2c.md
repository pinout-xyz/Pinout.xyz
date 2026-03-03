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
# I2C - Inter Integrated Circuit

GPIO 2 and GPIO 3 - the Raspberry Pi's I2C1 pins - allow for two-wire communication with a variety of external sensors and devices.

The I2C pins include a fixed 1.8 kΩ pull-up resistor to 3.3v. They are not suitable for use as general purpose IO where a pull-up might interfere.

I2C is a multi-drop bus, multiple devices can be connected to these same two pins. Each device has its own unique I2C address.

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

GPIO 0 and GPIO 1 - I2C0 - can be used as an alternate I2C bus, but are typically used by the system to read the HAT EEPROM.
