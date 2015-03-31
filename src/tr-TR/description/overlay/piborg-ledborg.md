###PiBorg LedBorg RGB LED Board

[PiBorg LedBorg](http://www.piborg.org/ledborg/), Raspberry Pi için oldukça hafif bir RGB LED board'udur. Bu board kendisine ait bir sürücü barındırır, bu yüzden ayrıca bir sürücü kurmanıza gerek yok.

Eğer daha fazla aralıkta renk istiyorsanız bunu WiringPi ile softPwm ile de yapabilirsiniz. Pin atamaları şu şekilde:

WiringPi pin 0: Kırmızı LED
WiringPi pin 2: Yeşil LED
WiringPi pin 3: Mavi LED

Python ile bunu yapmak neredeyse çocuk oyuncağı:

```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(0,0,100)
wiringpi.softPwmCreate(2,0,100)
wiringpi.softPwmCreate(3,0,100)

# mor!
wiringpi.softPwmWrite(3,100) # Full Blue
wiringpi.softPwmWrite(0,100) # Full Red
wiringpi.softPWMWrite(2,0)	 # No Green
```