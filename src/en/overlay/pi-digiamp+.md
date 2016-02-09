<!--
---
class: board
type: multi
name: "Pi-DigiAMP+"
manufacturer: IQAudIO
description: A combined DAC and 35w amplifier board.
url: http://www.iqaudio.co.uk/home/9-pi-digiamp-0712411999650.html
formfactor: 'HAT'
pincount: 40
eeprom: yes
pin:
  '15':
    name: ID_SD
-->
#Pi-DigiAMP+

The Pi-DigiAMP+ is an add-on board that includes a Digital to Analog Converter (DAC) and powerful 35w stereo amplifier. If you want to turn your Raspberry Pi into a working Hi Fi stereo, just add speakers and you're off.

The Pi-DigiAMP+ exposes some of the Pi's pins via a header.

Pin | Name | Name | Pin
--- | --- | --- | ---
1 | GPIO23 (Rotary encoder) | GPIO22 (Mute) | 2
3 | GPIO24 (Rotary encoder) | GPIO25 (IR)   | 4
5 | 5v                      | 3v3           | 6
7 | I2C SCL1                | Ground (0v)   | 8
9 | I2C SDA1                | Ground (0v)   | 10


These can be used for whatever you like but some are used by some additional software the IQAudIO provide to easily support a rotary encoder for physically controlling volume, a hardware mute switch and IR control.

The official documentation can be found on the [IQAudIO website](http://www.iqaudio.com/downloads/IQaudIO.pdf).