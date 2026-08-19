<!--
---
name: I2C
class: interface
type: pinout
description: Raspberry Pi i2c pinleri
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

Raspberry Pi'nin I2C pinleri eğer pek çok harici bileşen ile çalışıyorsanız oldukça işinize yarayacaktır.

Bağlı olan I2C bileşenlerini tek satırlık bir kodla kontrol edebilirsiniz:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

