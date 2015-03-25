###The PiBorg LedBorg is an ultra-bright RGB LED board for the Raspberry Pi.

PiBorg has its own driver, so you don't need to drive it manually.

If you want a much, much wider range of colours, though, you can drive it manually using softPwm in WiringPi. The pin assignments for this are as follows:

WiringPi pin 0: Red LED
WiringPi pin 2: Green LED
WiringPi pin 3: Blue LED

This is easy using WiringPi in Python:


```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(0,0,100)
wiringpi.softPwmCreate(2,0,100)
wiringpi.softPwmCreate(3,0,100)

# Purple!
wiringpi.softPwmWrite(3,100) # Full Blue
wiringpi.softPwmWrite(0,100) # Full Red
wiringpi.softPWMWrite(2,0)	 # No Green
```