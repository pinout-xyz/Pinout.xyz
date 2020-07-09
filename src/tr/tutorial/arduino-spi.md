<!--
---
name: Arduino SPI
description: Raspberry Pi SPI ile Arduino programlama
pin:
  '19':
    name: SDO
    direction: output
    active: high
    description: Serial Data Out
  '21':
    name: SDI
    direction: input
    active: high
    description: Serial Data In
  '23':
    name: SCK
    direction: output
    active: high
    description: Serial Clock
  '24':
    name: CE0
    direction: output
    active: high
    description: Arduino Reset
-->
#SPI üzerinden ATmega 328p / Arduino

###Raspberry pi'nizin doğrudan ATmega 328p/Arduino'yu besleyip onunla programlama yapmanıza olanak sağladığını biliyor muydunuz? Bunu sadece birkaç kablo, bir breadboard, bir 16MHZ kristal with nothing but a few wires, a breadboard, a 16Mhz crystal osilatör ve de birkaç 22pF kondansatör ile yapabilirsiniz!

Öncelikle [Pico PiDuino makalesi](http://pi.gadgetoid.com/article/building-the-pico-piduino)'ni takip edin / etmenizi öneririz, bunu sıfırdan uygulamak sadece &pound;5 gibi bir masraf çıkaracak.

Bunun ardından [Gordon Henderson'un modifiye AVRDude](https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/)'unu kurmalısınız.

8/CEO'yu ATmega'nuzun Reset/RST pin'ine bağlayın, 9/SDI'yu da ATmega'nın SDI pin'ine (D12) bağlayın, 10'u da onun SDO pin'ine (D11) bağlayın. Son olarak 11/SCLK'yı da onun SCLK pin'ine (D13) bağlayın.

ATmega'nızı Raspberry Pi'den aldığınız 3.3v ile besleyin, GND Pinini de Pi'ye bağlayarak düzeneği tamamlayın ve de cihazı açın.

Askıda kalmış bir SPI cihazı kalmadığına emin olun, ve de cihazın bağlandığını kontrol edin. Bunu aşağıdaki komutlar ile yapabilirsiniz:

```bash
avrdude -p m328p -c gpio
```

Arduino skeçlerini (sketch) derlemeye aşağıdaki komut ile başlayabilirsiniz:

```bash
sudo apt-get install arduino arduino-mk
```

[Bu basit makefile dosyası](http://pi.gadgetoid.com/arduino/Makefile) ([alternatif link](http://paste.debian.net/111092/)) başlamanız için yeterli olacaktır.Yeni bir sketch oluşturup adına mysketch.ino diyin ve de çalıştırın:


```bash
export BOARD=atmega328
make
avrdude -p m328p -c gpio -e -U flash:w:build-cli/Arduino.hex
```
