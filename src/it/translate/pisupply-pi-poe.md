<!--
---
name: Pi PoE Switch HAT
class: board
type: power
formfactor: Custom
manufacturer: Pi Supply
description: The Pi PoE Switch HAT is a power over ethernet add-on board for the Raspberry Pi
url: https://www.kickstarter.com/projects/pisupply/pi-poe-switch-hat-power-over-ethernet-for-raspberr
github: https://github.com/PiSupply/PiPoE
buy: https://www.pi-supply.com/product/pi-poe-switch-hat-power-over-ethernet-for-raspberry-pi/
image: 'pisupply-pi-poe.png'
pincount: 40
eeprom: setup
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
  '11':
    name: Power Management
  '15':
    name: LED Green/Yellow
  '16':
    name: LED Green
  '18':
    name: LED Yellow/Green
-->
#Pi PoE Switch HAT
The Pi PoE Switch HAT is an add on board for the Raspberry Pi that brings the Pi Supply Switch technology together with PoE all in one fantastic package!

You can now power your Raspberry Pi and provide an Ethernet connection in any location with just a single cable. Perfect for removing the clutter of wires and for reliable use in remote locations.

* Fully 802.3af (mode A and B) compliant active power over Ethernet
* Contains physical layer power negotiation circuitry, presenting itself as a Class 0 device
* Fully isolated switched mode power supply (SMPS) - 1500V isolation input to output
* Overload and short circuit protection
* Over temperature protection
* High efficiency (up to 87%) regulated output
* Input voltage 36-56V, output voltage 5V, output current 10-1300mA, max output power 6.5W
* Onboard ATtiny 13A microcontroller for power management functionality
* Leaves all unused GPIO free for use with other add on boards

The onboard optional jumper toggles the power functionality:
* Jumper on. The Pi PoE will power on after holding the power button for two seconds
* Jumper off. The Pi PoE will power on as soon as you apply power from your injector

