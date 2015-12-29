<!--
---
name: I2C
description: Raspberry Pi i2c pinleri
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

Raspberry Pi'nin I2C pinleri eğer pek çok harici bileşen ile çalışıyorsanız oldukça işinize yarayacaktır.

Bağlı olan I2C bileşenlerini tek satırlık bir kodla kontrol edebilirsiniz:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

I2c'ye Python'un smbus kütüphanesi ile erişebilirsiniz:

Önde gerekli paketi kurmalısınız:

```bash
sudo apt-get install python-smbus
```

Ardından Python ile aşağıdaki kodu çalıştırabilirsiniz:

```python
import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
```