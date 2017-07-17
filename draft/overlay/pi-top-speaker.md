<!--
---
name: pi-topSPEAKER
class: board
type: audio
formfactor: Custom
manufacturer: pi-top
description: pi-top/pi-topCEED compatible speaker add-on board
url: http://pi-top.com/products/speaker
github: https://github.com/pi-top/pi-topSPEAKER
buy: http://pi-top.com/products/speaker
image: 'pi-top-speaker.png'
pincount: 2
eeprom: no
pin:
  '3':
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
i2c:
  '0x71':
    name: Left Channel I2C Interface
    device: TCA9543A
  '0x72':
    name: Mono Mix I2C Interface
    device: TCA9543A
  '0x73':
    name: Right Channel I2C Interface
    device: TCA9543A
install:
  'devices':
    - 'i2c'
  'apt':
    - 'pt-speaker'
    - 'python-pt-speaker'
    - 'python3-pt-speaker'
-->
#pi-topSPEAKER

The pi-topSPEAKER is a modular pi-top/pi-topCEED compatible speaker add-on board, which can form part of a chain of up to 3.
NOTE: this means that it requires a pi-topHUB to function.

The pi-topSPEAKER needs to be initialised each time after power up in order to function; as the device is software-controlled and highly customisable, the Pi is responsible for initialising default settings.

It contains a 3-position hardware switch which changes the primary I2C address of the pi-topSPEAKER on an I2C MUX (TCA9543A) which sits between the Raspberry Pi I2C bus and the DAC+AMP \[digital-to-analog converter and amplifier\](TAS2505) of the pi-topSPEAKER. This I2C address determines the output: left channel, mono mix or right channel.

Audio output on the Raspberry Pi needs to be set to HDMI. This HDMI audio (containing 2-channel audio data) is converted by pi-topHUB into SPDIF data (BCM format). The SPDIF receiver then converts this to 24-bit I2S format. Mixed digital audio data is input to TAS2505's mono DAC Signal Processor via I2C MUX, and finally audio is amplified through a 2W D-class audio amplifier and output to the 2W (3W peak), 4Ω speaker.