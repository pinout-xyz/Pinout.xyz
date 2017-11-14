<!--
---
name: MDB2Pi HAT
class: board
type: IO,Power
formfactor: HAT
manufacturer: Abrantix
description: Multi-Drop-Bus MDB Converter Board for the Raspberry Pi
url: http://blog.abrantix.com/webshop/mdb-converter/
buy: http://blog.abrantix.com/webshop/product/mdb-to-raspberrypi
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

The MDB2Pi is a Raspberry Pi HAT which can serve as a MDB master (VMC), as MDB cashless peripheral, or as tracer for MDB Vending Machines. It takes care of the MDB specific 9-bit format, electrical and timing constraints. It forwards the MDB payload to the Raspberry Pi UART using a simple serial protocol. The MDB2Pi is powered through the MDB bus (10...42V regulated or unregulated supply) and back-powers the Raspberry Pi with up to 2.5A at 5V. Therefore, no separate power supply is required. Furthermore, the MDB2Pi contains a Real Time Clock (RTC), buffered by a super capacitor.

A housing for the MDB2Pi (and the MDB2Pi itself) is available at the Abrantix Web Shop: http://blog.abrantix.com/webshop/product/mdb-to-raspberrypi/. Alternatively, you can download a free 3D model here: http://www.thingiverse.com/thing:2209661



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

## RTC
A PCF8563 I2C chip in conjunction with a SuperCapacitor is used for Real-Time-Clock capability (no battery required). This allows buffering of the time up to 7 days when fully charged (or even more, depending on environment temperature and chip/capacitor variance).

Read the RTC:
```bash
pi@raspberrypi:~ $ sudo hwclock -r
Thu 04 May 2017 06:22:13 UTC  -0.310218 seconds
```
Write the RTC:
```bash
pi@raspberrypi:~ $ sudo hwclock -w
```
RTC Troubleshooting:
Check if the chip responds over I2C:
```bash
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- UU -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
Check dmesg for RTC
```bash
pi@raspberrypi:~ $ dmesg | grep rtc
[    2.937443] rtc-pcf8563 1-0051: chip found, driver version 0.4.4
[    2.943665] rtc-pcf8563 1-0051: rtc core: registered rtc-pcf8563 as rtc0
```

Hint: In case that the SuperCap has fully discharged, the daemon might be unable to talk to the RTC at first startup:

```bash
pi@raspberrypi:~ $ dmesg | grep rtc
[    2.900119] rtc-pcf8563 1-0051: chip found, driver version 0.4.4
[    2.900403] rtc-pcf8563 1-0051: pcf8563_write_block_data: err=-5 addr=0e, data=03
[    2.900428] rtc-pcf8563 1-0051: pcf8563_probe: write error
[    2.900459] rtc-pcf8563: probe of 1-0051 failed with error -5
```
In this case, please wait a few minutes to let the SuperCap recharge, then restart your pi so the RTC daemon can detect the chip again.
