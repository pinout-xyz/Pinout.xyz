<!--
---
type: board
name: PiBorg LEDBorg
manufacturer: PiBorg
description: A single RGB LED for your Raspberry Pi
url: https://www.piborg.org/ledborg-new/install
buy: https://www.piborg.org/ledborg
formfactor: '26-way'
pincount: 26
eeprom: no
pin:
  '11':
    name: Red LED
    direction: output
    active: high
    description: PiBorg Red LED
  '13':
    name: Green LED
    direction: input
    active: high
    description: PiBorg Green LED
  '15':
    name: Blue LED
    direction: output
    active: high
    description: PiBorg Blue LED
-->
###The PiBorg LedBorg is an ultra-bright RGB LED board for the Raspberry Pi.

the PiBorg Ledborg has its own driver, so you don't need to drive it manually.

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