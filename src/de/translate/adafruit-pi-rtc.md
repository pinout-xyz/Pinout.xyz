<!--
---
name: Adafruit PiRTC 
class: board
type: rtc
formfactor: Custom
manufacturer: Adafruit
description: Add a simple RTC to your Pi
url: https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-up-and-test-i2c
buy: https://www.adafruit.com/products/3386
image: adafruit-pi-rtc.png
pincount: 6
eeprom: no
power:  
  '1':     
ground:
  '6':    
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x68':
    name: PCF8523
    device: PCF8523 
-->
#Adafruit PiRTC

This is a great battery-backed real time clock (RTC) that allows your Raspberry Pi project to keep track of time if the power is lost. Perfect for data-logging, clock-building, time-stamping, timers and alarms, etc. Equipped with PCF8523 RTC, it works great with the Raspberry Pi and has native kernel support.

This RTC will keep the time for about 5 years. The PCF8523 is simple and inexpensive but not a high precision device. It may lose or gain a second or two per day.
