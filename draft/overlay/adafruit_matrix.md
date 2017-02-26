<!--
 ---
 name: Adafruit RGB Matrix HAT + RTC
 class: board
 type: LED
 formfactor: HAT
 manufacturer: Adafruit
 description: Run large HUB75 matrices of a Raspberry Pi
 url: https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi
 buy: https://www.adafruit.com/products/2345
 image: adafruit_matrix.png 
 pincount: 40
 eeprom: yes
 power:
   '1':
   '2':
 ground:
   '6': 
 pin:
   '3':
     mode: I2C
   '5':
     mode: I2C
   '29': 
   '33':
   '31':
   '32':
   '36':
   '16':
   '7':
   '11': 
   '40':
   '15':
   '37':
   '13':
   '38':

i2c:
  '0x68':
    name: DS1307
    device: DS1307
 -->
#Adafruit RGB Matrix HAT + RTC
 
 
This HAT plugs into your Pi and makes it super easy to control RGB matrices such as those you see in the likes of Times square enabling you to create a colorful scrolling display or mini LED wall with ease. A 5V power supply is also required, not included, for powering the matrix itself. The Pi cannot do it due to the high currents. To calculate the max current of your matrix set up, multiply the width of all the chained matrix by 0.12 : A 32 pixel wide matrix needs 32*0.12 = 3.85A so pick up a 5V 4A power supply. Please note: this HAT is only for use with HUB75 type RGB Matrices. Not for use with NeoPixel, DotStar, or other 'addressable' LEDs.

Features:

Simple design - plug in power, plug in IDC cable, run our Python code!
Power protection circuitry - you can plug a 5V 4A wall adapter into the HAT and it will automatically protect against negative, over or under-voltages! Yay for no accidental destruction of your setup.
Onboard level shifters to convert the RasPi's 3.3V to 5.0V logic for clean and glitch free matrix driving
DS1307 Real Time Clock can keep track of time for the Pi even when it is rebooted or powered down, to make for really nice time displays
 
To install:
 ```bash
sudo apt-get update
sudo apt-get install python-dev python-imaging
wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip
unzip master.zip
cd rpi-rgb-led-matrix-master/
make
 ```
