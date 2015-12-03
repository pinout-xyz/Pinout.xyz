<!--
---
name: Raspberry Pi Dots
description: Noktaları birleştirerek bir devre oluşturun
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
pincount: 38
pin:
  bcm0:
    name: 'Color: Blue'
    direction: input
  bcm1:
    name: Dot 7
    direction: input
  bcm2:
    name: Dot 22
    direction: input
  bcm3:
    name: Dot 21
    direction: input
  bcm4:
    name: Dot 2
    direction: input
  bcm5:
    name: Dot 9
    direction: input
  bcm6:
    name: Dot 14
    direction: input
  bcm7:
    name: Dot 6
    direction: input
  bcm8:
    name: Dot 18
    direction: input
  bcm9:
    name: Dot 17
    direction: input
  bcm10:
    name: 'Color: Green'
    direction: input
  bcm11:
    name: Dot 8
    direction: input
  bcm12:
    name: Dot 10
    direction: input
  bcm13:
    name: Cloud
    direction: input
  bcm14:
    name: Dot 1
    direction: input
  bcm15:
    name: Dot 3
    direction: input
  bcm16:
    name: Dot 13
    direction: input
  bcm17:
    name: Dot 4
    direction: input
  bcm18:
    name: Dot 20
    direction: input
  bcm19:
    name: 'Color: Orange'
    direction: input
  bcm20:
    name: Bear
    direction: input
  bcm21:
    name: Dot 12
    direction: input
  bcm22:
    name: Dot 15
    direction: input
  bcm23:
    name: Dot 16
    direction: input
  bcm24:
    name: Dot 19
    direction: input
  bcm25:
    name: Dot 5
    direction: input
  bcm26:
    name: Dot 11
    direction: input
  bcm27:
    name: 'Color: Red'
    direction: input
-->
#Raspberry Pi Dots

###Dots, Raspberry Pi için Dot to Dot HAT (Noktadan-noktaya, Raspberry Pi üzerine tam bağlanıp oturabilen), uçları tanımlamak ve de birleştirmek için sadece bir iletken kalem boya kullanılamn bir devredir.

Bu devre üzerindeki tüm noktalar "akıcı" bir metal olmakla birlikte toprağa bağlamak ve devreyi tamamlamak için sadece modülle gelen bir adet iletken boya ile (gazlı kaleme benziyor) toprağa bir çizgi çizilmesi yeterlidir. Bu sayede lehimle uğraşmadan kolaylıkla devreler tamamlanabilir.

Bir *nokta*yı okuyabilmek için bağlandığı pin'i (örnekte `dot_pin`) INPUT (giriş) olarak tanımlamalısınız:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM )
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.input(dot_pin)
```

Bu pin'i sadece okumak istediğinizde PULLUP konumuna getirmek iyi bir alışkanlık olacakıtr. Aşağıdaki yol pini okumak için önerilen bir yoldur:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.input( dot_pin )
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```

Dots hakkında detaylı bilgi için [buraya](http://www.raspberrypi.org/dots/), HATS hakkında detaylı bilgi için de buraya [tıklayın](http://www.raspberrypi.org/introducing-raspberry-pi-hats/).