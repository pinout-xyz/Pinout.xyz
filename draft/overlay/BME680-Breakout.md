<!--
---
name: BME680 Breakout
class: board
type: other
formfactor: Custom
manufacturer: Pimoroni
description: Use this breakout to monitor every aspect of your indoor environment.
url: https://shop.pimoroni.com/products/bme680
github: https://github.com/pimoroni/bme680
buy: https://shop.pimoroni.com/products/bme680
image: 'bme680.png'
pincount: 5
eeprom: no
power:
  '1':
ground:
  '9':
pin:
  '3':
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
  '7':
    name: O
i2c:
  '0x76':
    name: BME680
    device: BME680
-->
#BME680 Breakout

Use this breakout to monitor every aspect of your indoor environment. Its gas resistance readings will react to changes in volatile organic compounds and can be combined with humidity readings to give a measure of indoor air quality.
