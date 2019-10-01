<!--
---
name: UART
class: interface
type: pinout
description: Raspberry Pi UART pinleri
url: http://elinux.org/RPi_Serial_Connection
pin:
  '8':
    name: TXD / Transmit
    direction: output
    active: high
  '10':
    name: RXD / Receive
    direction: input
    active: high
-->
#UART - Universal Asenkron Verici/Alcı

###WiringPi'deki 2 UART pini Pin 15 ve 16'dır

UART Arduino, veya bootload edilmiş bir ATmega ile kolayca iletişim kurmanızı sağlayacak bir arayüzdür. Yalnız bu iletişimi kurarken dikkat etmeniz gereken bazı hususlar var. Raspberry Pi 3.3v iken Arduino 5v'tur. Bunları akımları eşitlemeden bağlarsanız cihazlarınızdan dumanlar tütmeye başlayabilir

Örneğin Arduino bootload edilmiş ATmega 328 devresini breadboard'a kurup bir akım regülatörü ile Raspberry Pi'nin 5v yolunu 3.3 v'a dönüştürebilirsiniz. Bu sayede 3.3v logic'ine sahip bir Arduino klonunuz olacak.

WiringPi-Python modülünü yükledikten sonra, Aşağıdaki Python örneği ile Raspberry Pi'nin UART'ını 9600baud'da açabilir ve 'merhaba dunya' yazabilirsiniz.

```python
import wiringpi
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
wiringpi.serialPuts(serial,'merhaba dunya')
```
