<!--
---
name: Traffic HAT
class: board
type: multi
formfactor: HAT
manufacturer: Ryanteck
description: A quick and easy way to learn the basics of GPIO on a budget
url: https://ryanteck.uk/hats/1-traffichat-0635648607122.html
buy: https://ryanteck.uk/hats/1-traffichat-0635648607122.html
image: 'traffic-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
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
  '15':
    name: LED1 / Green
    direction: output
    active: high
  '16':
    name: LED2 / Amber
    direction: output
    active: high
  '18':
    name: LED3 / Red
    direction: output
    active: high
  '22':
    name: Button
    direction: input
    active: high
  '29':
    name: Buzzer
    direction: output
    active: high
-->
#Traffic HAT

###A quick and easy way to learn the basics of GPIO on a budget. All in a nice HAT.

```python
from gpiozero import TrafficHat
from time import sleep
from signal import pause

hat = TrafficHat()

# control components individually
hat.lights.green.on()
sleep(1)
hat.lights.amber.on()
sleep(1)
hat.lights.red.on()
sleep(1)
hat.buzzer.on()
sleep(1)
hat.off()  # turn everything off

# set up events on button press/release
hat.button.when_pressed = hat.lights.blink
hat.button.when_released = hat.lights.off

pause()
```
