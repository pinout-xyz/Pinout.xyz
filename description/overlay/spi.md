#SPI - Serial Peripheral Interface

###Known as the four-wire serial bus, SPI lets you daisy-chain multiple compatible devices off a single set of pins by assigning them different addresses.

A simple example of an SPI peripheral is the MCP23S17 digital IO expander chip Note the S in place of the 0 found on the I2C version. Using it in WiringPi2 is a doddle:

```python
import wiringpi2 as wiringpi
HIGH = 1
OUTPUT = 1
PIN_BASE = 65
SPI_ADDR = 0x20
wiringpi.wiringPiSetup()
wiringpi.mcp23S17Setup(PIN_BASE,SPI_ADDR)
# 16 pins including the starting pin
mcp23S17pins = range(PIN_BASE,PIN_BASE+15)
for pin in mcp23S17pins:
	wiringpi.pinMode(pin,OUTPUT)
	wiringpi.digitalWrite(pin,HIGH)
```

You can also use the SPI port to "Bit-Bang" an ATmega 328, loading Arduino sketches onto it with Gordon's modified version of AVRDude.

Hook up you Pi's SPI port to that of your ATmega, and power the ATmega from the 3.3v pin on the Pi. Make sure you're not running any SPI device drivers, and run "avrdude -p m328p -c gpio" to verify the connection.

See the individual pins to learn how to connect up your ATmega.