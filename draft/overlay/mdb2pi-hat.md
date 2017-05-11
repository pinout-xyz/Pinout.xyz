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
    name: HAT EEPROM
    device: 24C32
-->
#MDB2Pi HAT

The MDB2Pi HAT can serve as an MDB master or as a peripheral MDB Device for Vending Machines (VMC). It takes care of the MDB specific 9-bit format, electrical and timing constraints. It forwards the MDB payload to the Raspberry Pi UART using a simple serial protocol.
The MDB2Pi HAT is powered from the MDB bus (10...42V regulated or unregulated supply) and backpowers the Raspberry Pi with up to 2.5A@5V. Thus no separate power supply is required for the pi.

##Configuration
1. Enable UART and HAT detection by adding the following lines to /boot/config.txt:
```bash
enable_uart=1
dtparam=i2c_vc=on
```

2. disable serial console output by editing :
```bash
sudo nano /boot/cmdline.txt
```
--> remove the "console=..." parameter

##MDB Master Demo:
1. Install mono runtime:
```bash
sudo apt-get install mono-runtime
```

2. Get the Demo code:
```bash
wget https://secure.abrantix.com/downloads/MDBConverter/MasterSimulatorConsole.zip
unzip MasterSimulatorConsole.zip
```

3. Run the Demo:
```bash
cd MasterSimulatorConsole
mono MDBMasterSimulatorConsole.exe /dev/serial0 115200
```
Hint: On newer raspbian releases, the serial port is available as /dev/serial0 - older releases may use dev/ttyAMA0.



