SDA, Raspberry Pi'deki I2C pinlerinden biri. [I2c hakkında detaylı bilgi](/pinout/i2c).

GPIO pinleri ile dijital HIGH ve LOW değerlerini okumak ve hazırlamak oldukça kolay, yalnız bazı hususlara dikkat etmeniz gerekmekte:

* Kodu çalıştıracak script'inizi root (süper yönetici) hakları ile çalıştırmalısınız.
* Pin'in modunu OUTPUT (1) olarak tanımlamalısınız.

Eğer WiringPi2-Pytgon kütüphanesini kurduysanız ( pip install wiringpi2 ) o zaman aşağıdaki kodu bir .py dosyası olarak kaydedip çalıştırabilirsiniz:

```python
import wiringpi2 as wiringpi
HIGH = 1
LOW = 0
OUTPUT = 1
INPUT = 0
wiringpi.wiringPiSetup()
wiringpi.pinMode(8,OUTPUT)
wiringpi.digitalWrite(8,HIGH)
```

Ardından şu komutla çalıştırabilirsiniz:

```bash
sudo python scriptadi.py
```