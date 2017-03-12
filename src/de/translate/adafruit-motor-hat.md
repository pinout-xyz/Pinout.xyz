<!--
---
name: DC & Stepper Motor HAT 
class: board
type: motor
formfactor: HAT
manufacturer: Adafruit
description: Drive 4 DC Motors or 2 Stepper Motors with a Raspberry Pi
url: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi
buy: https://www.adafruit.com/products/2348
image: adafruit-motor-hat.png
pincount: 40
eeprom: yes
power:
  '17':
  '1': 
ground:
  '9':
  '25':
  '39':
  '34':
  '30':
  '20':
  '14':
  '6':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
 '0x20':
   name: TB6612
   device: TB6612    
-->
#DC & Stepper Motor HAT 

Let your robotic dreams come true with the new DC+Stepper Motor HAT from Adafruit. This Raspberry Pi add-on is perfect for any motion project as it can drive up to 4 DC or 2 Stepper motors with full PWM speed control.

Since the Raspberry Pi does not have a lot of PWM pins, we use a fully-dedicated PWM driver chip onboard to both control motor direction and speed. This chip handles all the motor and speed controls over I2C. Only two pins (SDA & SCL) are required to drive the multiple motors, and since it's I2C you can also connect any other I2C devices or HATs to the same pins. In fact, you can even stack multiple Motor HATs, up to 32 of them, for controlling up to 64 stepper motors or 128 DC motors (or a mix of the two)

Specs:

4 H-Bridges: TB6612 chipset provides 1.2A per bridge with thermal shutdown protection, internal kickback protection diodes.

Can run motors on 4.5VDC to 13.5VDC.
Up to 4 bi-directional DC motors with individual 8-bit speed selection (so, about 0.5% resolution)

Up to 2 stepper motors (unipolar or bipolar) with single coil, double coil, interleaved or micro-stepping.

Polarity protected 2-pin terminal block and jumper to connect external 5-12VDC power

To install:

```bash
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
sudo apt-get install python-dev
sudo python setup.py install
```
