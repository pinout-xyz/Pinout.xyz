<!--
---
name: DI6acDQ6rly I2C-HAT
class: board
type: io, relay
formfactor: Custom
manufacturer: Raspihats
description: 6 isolated digital input channels and 6 relay output channels add-on board for the Raspberry Pi 
url: http://raspihats.com/product/di6acdq6rly-i2c-hat
buy: http://raspihats.com/product/di6acdq6rly-i2c-hat
image: 'raspihats-i2c-hat-di6acdq6rly.png'
pincount: 40
eeprom: no
power:
  '2':
  '4':
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
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x60-0x6F':
    device: raspihats
-->
#DI6acDQ6rly I2C-HAT

The DI6acDQ6rly I2C-HAT is a 6 isolated digital input channels and 6 relay output channels Raspberry Pi add-on board that uses the I2C bus for communication. The input channels can be used as edge counters, every input channel has an two 32-bit counters attached, one for counting rising edges and the other for counting falling edges. The DI6acDQ6rly also has 6 LED indicators for digital inputs status monitoring and 6 LED indicators for power relay outputs status monitoring.

Users can stack up to 16 DI6acDQ6rly I2C-HATs on one Raspberry Pi by using the on-board address jumpers to select a unique I2C bus address.
I2C address range is [0x60 .. 0x6F].

## Features
* 6 isolated digital input channels(sink/source)
* 32-bit counters for all digital input channels
* 6 relay output channels(5A@250VAC)
* configurable relay PowerOnValue
* configurable relay SafetyValue
* dual watchdog(system and communication)
* Form A power relay
* 2000 VAC isolation voltage
* temperature operating range: -25 ~ +75°C
* stackable, up to 16x

##Integration
* [Python](https://pypi.python.org/pypi/raspihats)
* [Node-RED](https://www.npmjs.com/package/node-red-contrib-raspihats) - Flow-based programming for the IoT
* [HomeAssistant](https://home-assistant.io/components/raspihats) - Home automation platform
* [RobotFramework](https://github.com/raspihats/raspihats/blob/master/raspihats/i2c_hats/robot.py) - Generic test automation framework