SCL est la broche fournissant le signal d'horloge du bus i2c de la Raspberry Pi, [référence i2c](/pinout/i2c).

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