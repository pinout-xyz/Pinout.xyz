<!--
---
name: Inventor HAT Mini
class: board
type: adc,audio,io,motor,led
formfactor: pHAT
manufacturer: Pimoroni
description: A versatile motor, servo and audio driver HAT for Raspberry Pi
url: https://shop.pimoroni.com/products/inventor-hat-mini
github: https://github.com/pimoroni/inventorhatmini-python
buy: https://shop.pimoroni.com/products/inventor-hat-mini
image: 'pimoroni-inventor-hat-mini.png'
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
    name: I2C SDA
    mode: i2c
  '5':
    name: I2C SCL
    mode: i2c
  '7':
    name: I2C Int
    mode: input
  '8':
    name: UART TX / TRIG
    mode: uart
  '10':
    name: UART RX / ECHO
    mode: uart
  '12':
    name: PCM CLK
    mode: i2s
  '22':
    name: Amp Enable
    direction: output
    active: high
  '32':
    name: LED Data
    mode: pwm
    direction: output
  '35':
    name: PCM FS
    mode: i2s
  '37':
    name: User Button
    mode: input
  '40':
    name: PCM DOUT
    mode: i2s
i2c:
  '0x17':
    name: Super IO Expander
    device: MS51TC0AE
-->
# Inventor HAT Mini

Inventor HAT Mini is a versatile motor, servo and audio driver HAT for Raspberry Pi. Bring your mechanical inventions, creations and contraptions to life!
​
## Features

- Nuvoton microcontroller (MS51TC0AE) with built-in 16-bit PWM and 12-bit Analog to Digital Converter
  - 4 sets of header pins for connecting 3 pin hobby servos
  - 4 sets of header pins for GPIO (all of which are ADC capable)
  - Servo and GPIO pins all have their own power and ground pins
- Dual H-Bridge motor driver (DRV8833)
  - 2 JST-SH connectors (6 pin) for attaching motors with encoders
  - Alternate socket connector for attaching 2 standard (2 pin) motors
  - Per motor current limiting (425mA)
  - Per motor direction indicator LEDs
- MAX98357 3.2W I2S mono amplifier
  - 2 pin (Picoblade-compatible) connector for attaching speaker
- 8 x addressable RGB LEDs/Neopixels
- User button
- Qw/ST connector for attaching breakouts
- Pass-through 40 pin header
- Fully assembled - no soldering required
