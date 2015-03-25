#Raspberry Pi Dots

###Dots is a Dot to Dot HAT board for the Raspberry Pi that lets you join-the-dots with BARE Conductive Paint!

Every Dot on the Dots board is a "floating" metal contact just waiting to be pulled down to ground with a dab of paint.

To read a Dot you should set its corresponding pin as an INPUT and make sure it's pulled up like so:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM )
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.input(dot_pin)
```

It's good practise to only turn on the PULLUP when you actually want to read the Dot, so a method like
this is recommended for reading:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.input( dot_pin )
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```

