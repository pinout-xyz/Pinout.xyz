It's easy to get started writing a digital HIGH or LOW to a GPIO pin, but you've got to remember a few things:

* Run your script as root
* Set your pin's mode to OUTPUT (1)

Assuming you've installed WiringPi2-Python ( pip install wiringpi2 ) then try pasting the following into a .py file:

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

Then run it with:

```bash
sudo python myscript.py
```