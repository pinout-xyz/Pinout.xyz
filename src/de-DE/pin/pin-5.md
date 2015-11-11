SCL ist der Clock oder Tackt Anschluss des I2C-Bus des Pi. [mehr über I2C](/pinout/i2c).

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