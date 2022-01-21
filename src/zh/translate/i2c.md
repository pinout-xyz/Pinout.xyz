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
# I2C - 集成电路总线

GPIO 2 和 GPIO 3 是树莓派 I2C1 的引脚。它们可以与各种支持两线制的外设传感器连接。

树莓派的 I2C 引脚自带一个 1.8kΩ 的上拉电阻，上拉到 3.3V。因此，如果把这个引脚当成普通 GPIO 来用的话，要注意这个上拉电阻是否有影响。

I2C 是一个多节点的总线，这两根引脚上可以连接多个设备，每个设备有唯一的 I2C 地址。

你可以通过下面的代码快速检测连在树莓派 I2C 总线上的设备地址：

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

如果用 Python 的话，可以通过 smbus 库来实现 I2C 访问：

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```

GPIO 0 和 GPIO 1 是 I2C0 的引脚，可以作为另一个 I2C 总线来用，但它们通常用来读写树莓派盖板上的 EEPROM。
