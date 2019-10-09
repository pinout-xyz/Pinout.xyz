<!--
---
name: Waveshare Servo Driver Hat
class: board
type: io,motor
formfactor: pHAT
manufacturer: Waveshare
description: Servo Driver HAT for Raspberry Pi, 16-Channel, 12-bit, I2C Interface
url: https://www.waveshare.com/wiki/Servo_Driver_HAT
schematic: https://www.waveshare.com/w/upload/a/a2/Servo_Driver_HAT_Schematic_.pdf
buy: https://www.waveshare.com/servo-driver-hat.htm
image: 'waveshare-servo-driver-hat.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
  '4':
  '17':
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
  '0x40':
    alternate: [ '0x40','0x41','0x42','0x43','0x44','0x45','0x46','0x47','0x48','0x49','0x4A','0x4B','0x4C','0x4D','0x4E','0x4F','0x50','0x51','0x52','0x53','0x54','0x55','0x56','0x57','0x58','0x59','0x5A','0x5B','0x5C','0x5D','0x5E','0x5F' ]
    name: PCA9685
    device: PCA9685
-->
#Servo Driver HAT

Standard Raspberry Pi 40PIN GPIO extension header, supports Raspberry Pi series boards.
I2C controlled, using only 2 pins, up to 32 different addresses, enabling to stack the same number of boards. They are selectable by desoldering the resistances and solder on pins A0..A4. 

##Notes
* The PCA9685 A5 pin is soldered to GND so you can't use the  other 32 possible addresses offerred by PCA9685.
* Also the i2c 0x70 address is present, if you run `i2cdetect -y 1`. That's because the PCA9685 uses that address to send data to all the devices of the same model.

## Features
* stackable, up to 32x.
* Up to 16-Channel servo/PWM outputs, 12-bit resolution for each channel (4096 scales).
* Integrates 5V regulator, up to 3A output current, can be powered from battery through VIN terminal.
* Standard servo interface, supports common used servo such as SG90, MG90S, MG996R, etc.
* Available development resources and manual on wiki (examples in python like Bluetooth/WiFi remote control).
