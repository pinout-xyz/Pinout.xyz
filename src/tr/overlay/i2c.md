<!--
---
description: Raspberry Pi i2c pinleri
-->
# I2C - Inter Integrated Circuit

Raspberry Pi'nin I2C pinleri eğer pek çok harici bileşen ile çalışıyorsanız oldukça işinize yarayacaktır.

Bağlı olan I2C bileşenlerini tek satırlık bir kodla kontrol edebilirsiniz:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

