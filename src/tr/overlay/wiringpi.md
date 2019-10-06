<!--
---
name: WiringPi
class: interface
type: pinout
page_url: wiringpi
url: http://wiringpi.com
github: https://github.com/WiringPi/WiringPi-Python
pin:
  '3':
    name: WiringPi 8
  '5':
    name: WiringPi 9
  '7':
    name: WiringPi 7
  '8':
    name: WiringPi 15
  '10':
    name: WiringPi 16
  '11':
    name: WiringPi 0
  '12':
    name: WiringPi 1
  '13':
    name: WiringPi 2
  '15':
    name: WiringPi 3
  '16':
    name: WiringPi 4
  '18':
    name: WiringPi 5
  '19':
    name: WiringPi 12
  '21':
    name: WiringPi 13
  '22':
    name: WiringPi 6
  '23':
    name: WiringPi 14
  '24':
    name: WiringPi 10
  '26':
    name: WiringPi 11
  '27':
    name: WiringPi 30
  '28':
    name: WiringPi 31
  '29':
    name: WiringPi 21
  '31':
    name: WiringPi 22
  '32':
    name: WiringPi 26
  '33':
    name: WiringPi 23
  '35':
    name: WiringPi 24
  '36':
    name: WiringPi 27
  '37':
    name: WiringPi 25
  '38':
    name: WiringPi 28
  '40':
    name: WiringPi 29
-->
#Raspberry Pi WiringPi

###WiringPi, Arduino benzeri bir kablolama basitliğini Raspberry Pi'ye getirmeyi amaçlayan bir projedir.

WiringPi, Arduino kullanmış olanların hiç yabancılık çekmeyeceği, Arduino benzeri bir pinleme/klablolama sistemini Raspberry Pi'ye getirmeyi amaçlamış üçüncü parti bir kütüphanedir. Bu kütüphanenin amacı benzer ve ortak bir platform oluşturmak, ve de Raspberry Pi GPIO pinlerini farklı diller ile yönetebilmektir. WiringPi özünde C dili ile yazılmıştır, fakat hem Ruby hem de Python türevleri mevcuttur. Bunları sıra ile Ruby için "gem install wiringpi" veya Python için "pip install WiringPi" diyerek kurabilirsiniz.

Python kullanıcıları kütüphanenin adının sonundaki 2'ye dikkat etmiş olabilirler. Bu aslında WiringPi-Python kütüphanesidir. Bu kütüphane sonunda mevcut WiringPi kütüğhanesindeki özellikleri ve esnekliği Raspberry Pi'ye Python dilinde getirmeyi başarmış bir kütüphanedir.

##WiringPi'ye başlangıç

WiringPi [kendi pin numaralama şematiğini kullanıyor](http://wiringpi.com/pins/). Bu linkten WiringPi'nin GPIO pinlerinizi nasıl numaralandırdığını görebilir, pinlerin ne yaptığını inceleyebilir, ve de C, Python veya Ruby dilleri ile GPIO programlamaya başlayabilir, devre elemanlarınızı yönetebilirsiniz.

Python'a kurmak saniyelerinizi alacak:

```bash
sudo pip install WiringPi
```

Daha fazla bilgi için WiringPi resmi web sitesi ni ziyaret edebilirsiniz.
