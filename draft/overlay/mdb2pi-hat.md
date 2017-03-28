<!--
---
name: MDB2Pi HAT
class: board
type: IO,Power
formfactor: HAT
manufacturer: Abrantix
description: Multi-Drop-Bus MDB Converter Board for the Raspberry Pi
url: http://www.abrantix.com/MDBConverter.html
buy: http://blog.abrantix.com/webshop/
image: 'mdb2pi-hat.png'
pincount: 40
eeprom: yes
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
  '8':
    mode: UART
  '10':
    mode: UART
  '27':
    mode: i2c
  '28':
    mode: i2c
i2c:
  '0x50':
    name: HAT EEPROM on I2C0
    device: 24C32
  '0x51':
    name: RTC on I2C1
    device: PCF8563
-->
# MDB2Pi HAT

The MDB2Pi HAT can serve as a MDB master or as a peripheral MDB Device for Vending Machines (VMC). It takes care of the MDB specific 9-bit format, electrical and timing constraints. It forwards the MDB payload to the Raspberry Pi UART using a simple serial protocol.
The MDB2Pi HAT is powered from the MDB bus (10...42V regulated or unregulated supply) and backpowers the Raspberry Pi with up to 2.5A at 5V. Thus no separate power supply is required for the pi. Furthermore, the MDB2Pi HAT contains a Real Time Clock (RTC), buffered by a super capacitor.

## Configuration
Enable UART and RTC by adding the following lines to /boot/config.txt:
```bash
enable_uart=1
dtoverlay=i2c-rtc,pcf8563
```

disable serial console output:
```bash
sudo nano /boot/cmdline.txt
```
--> remove the "console=..." parameter

## MDB Master and Cashless Device Demo:
Install mono runtime:
```bash
sudo apt-get install mono-runtime
```

Get the Demo code:
```bash
wget https://secure.abrantix.com/downloads/MDBConverter/MDBConverter.zip
unzip MDBConverter.zip
```

How to run the Master Demo:

```bash
cd MDBConverter
mono MDBMasterSimulatorConsole.exe /dev/serial0 115200
```
-> For master operation, please make sure to set the DIP Switch to ON-OFF-OFF-ON-ON

How to run the Cashless Device Demo:
```bash
cd MDBConverter
mono MDBCashlessDeviceSimulatorConsole.exe /dev/serial0 115200
```
-> For slave operation, please make sure to set the DIP Switch to OFF-ON-ON-OFF-OFF

Hint: On newer raspbian releases, the serial port is available as /dev/serial0 - older releases may use dev/ttyAMA0.



