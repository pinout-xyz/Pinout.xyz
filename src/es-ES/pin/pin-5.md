SCL es uno de los pines i2c en la Pi, [aprende más sobre i2c](/pinout/i2c).

```python
require 'wiringpi2'
HIGH = 1
LOW = 0
OUTPUT = 1
INPUT = 0
io = WiringPi::GPIO.new
io.pin_mode(9,OUTPUT)
io.digital_write(9,HIGH)
```
