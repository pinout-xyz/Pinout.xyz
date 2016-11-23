<!--
---
name: ZeroBorg
class: board
type: motor
formfactor: Custom
manufacturer: PiBorg
description: A PiZero robot controller
url: https://www.piborg.org/zeroborg
buy: https://www.piborg.org/zeroborg
image: 'piborg-zeroborg.png'
pincount: 6
eeprom: no
power:
  '1':
  '2':
  '4':
ground:
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
-->
#ZeroBorg

The PiBorg ZeroBorg is a 4 channel motor controller for the Raspberry Pi Zero.

It supports configurable i2c slave addresses from 3 (0x03) to 119 (0x77), meaning that while it uses i2c it can potentially co-exist with *any* other i2c board. See the "Multiple Boards" section of the ZeroBorg install guide for more details.

* 4 full H-Bridges
* Drives 4 motors or 2 stepper motors
* 2A peak or 1.5A RMS per bridge
* Onboard fast blow fuse at 5A
* Designed to run off a 9V power source
* 2 analogue inputs
* I2C communication