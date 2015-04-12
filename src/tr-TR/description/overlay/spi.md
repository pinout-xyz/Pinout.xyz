#SPI - Serial Peripheral Interface

###four-wire serial bus olarak da bilinen SPI, bir pin setinden birden fazla adresteki birden fazla uygun cihazı [papatya zinciri](https://tr.wikipedia.org/wiki/Papatya_zinciri) yapıp yönetmenizi sağlar.

Buna örnek olarak MCP23S17 digital IO expander çipini verebiliriz. 0 yerine S'in bulunduğu versiyon I2C versiyonudur. WiringPi2 ile çok kolay bir şekilde kullanlabilir:

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

SPI portunuz ayrıca Gordon'un modifiye AVRDude'una Arduino skeçleri yükleyerek ATmega 328'ye "[bit banging](http://en.wikipedia.org/wiki/Bit_banging)" de yapabilirsiniz.

Raspberry Pi'nizin SPI port'unu ATmega'nıza bağlayın ve ATmega'yı Raspberry Pi'nin 3.3v gücüyle besleyip açın. SPI sürücüleri çalıştırmadığınızdan emin olduktan sonra "`avrdude -p m328p -c gpio`" komutu ile bağlantıyı kontrol edin.

ATmega'nız varsa her bir pin için ayrı ayrı tıklayarak nasıl bağlayabileceğinizi öğrenebilirsiniz.