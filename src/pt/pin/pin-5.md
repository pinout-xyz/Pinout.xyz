SCL (i2c Clock) is one of the i2c pins on the Pi, [learn more about i2c](/pinout/i2c).

SCL includes a fixed, 1.8 kohms pull-up to 3.3v, which means this pin is not suitable for use as a general purpose IO where no pullup resistor is desired.