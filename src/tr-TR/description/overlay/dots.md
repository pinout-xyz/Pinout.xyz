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