<!--
---
name: Analog Zero
class: board
type: adc
formfactor: pHAT
manufacturer: RasPiO
description: A 10-bit 8-channel ADC for Raspberry Pi
url: http://rasp.io/analogzero/
github: https://github.com/raspitv/analogzero
buy: http://rasp.io/analogzero/
image: 'analog-zero.png'
pincount: 40
eeprom: no
power:
  '1':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
install:
  'devices':
    - 'spi'
-->
#Analog Zero

The RasPiO Analog Zero offers a compact, inexpensive, easy way to add eight analogue channels to your Raspberry Pi. RasPiO Analog Zero uses an MCP3008 analog to digital converter. It's an SPI driven, 10-bit, 8-channel ADC.

With RasPiO Analog Zero you can:

* read up to 8 analog inputs at once
* make a weather station
* make a digital thermometer
* make a voltmeter
* use potentiometer dials for control and display
* read analog sensors or voltages
* make your own embedded device with minimal footprint

## Code

```python
from gpiozero import MCP3008
from time import sleep

left_pot = MCP3008(0)
light = MCP3008(1)
temperature = MCP3008(2)
right_pot = MCP3008(3)

while True:
    print("Left pot value is {}".format(left_pot.value))
    print("Light sensor value is {}".format(light.value))
    print("Temperature sensor value is {}".format(temperature.value))
    print("Right pot value is {}".format(right_pot.value))
    sleep(1)
```

[GPIO Zero docs: MCP3008](http://gpiozero.readthedocs.io/en/v1.3.1/api_spi.html#gpiozero.MCP3008)
