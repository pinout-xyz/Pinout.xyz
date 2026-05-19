<!--
---
name: AQEX qReCon Flex
class: board
type: relay
formfactor: Custom
manufacturer: AQEX
description: qRecon Flex - Raspberry Pi HAT with Variable & Replaceable Relay Type
url: https://aqex.eu/qrecon-flex-raspberry-pi-relay-module-with-4-output.html
github: https://github.com/aqexhu/qReCon
buy: https://lectronz.com/products/aqex-qrecon-flex-variable-relay-hat-raspberry-pi
image: 'aqex-qrecon-flex.png'
pincount: 40
eeprom: no
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
  '29':
    name: Relay 4 - Bank 1
    mode: output
    active: high,low
  '31':
    name: Relay 4 - Bank 2
    mode: output
    active: high,low
  '33':
    name: Relay 3 - Bank 2
    mode: output
    active: high,low
  '35':
    name: Relay 2 - Bank 2
    mode: output
    active: high,low
  '36':
    name: Relay 3 - Bank 1
    mode: output
    active: high,low
  '37':
    name: Relay 1 - Bank 2
    mode: output
    active: high,low
  '38':
    name: Relay 2 - Bank 1
    mode: output
    active: high,low
  '40':
    name: Relay 1 - Bank 1
    mode: output
    active: high,low

-->


# AQEX qReCon Flex v1.0
###  Raspberry Pi HAT with Variable & Replaceable Relay Type
**Official Product Page:** [https://www.aqex.eu/qrecon-flex-raspberry-pi-relay-module-with-4-output.html](https://www.aqex.eu/qrecon-flex-raspberry-pi-relay-module-with-4-output.html)


## Product Concept & Strategic Advantages
The **qReCon Flex** is a versatile 4-channel relay output module designed for Raspberry Pi and other microcomputers. Its unique **socketed design** allows you to choose and easily replace the relays based on your specific project needs. 
Featuring **optical isolation**, **configurable GPIOs**, and **Active High/Low control**, the qReCon Flex provides professional-grade reliability and ultimate flexibility for controlling AC/DC loads.


## Strategic Advantages

* **Modular Relay Flexibility:** Swappable, mixable relay channels allow easy customization or replacement for different workloads.
* **Tailored Switching:** Supports various relay brands and specs per channel to match your exact voltage needs.
* **Galvanic & Optical Isolation:** Integrated optocouplers fully protect the Raspberry Pi from voltage spikes and noise.
* **Zero-Firmware Reliability:** Pure hardware design works instantly out of the box without software configuration.
* **Configurable GPIO Selection:** Onboard DIP switches allow easy selection of control pins to avoid conflicts with other HATs.
* **Selectable Active High/Low Logic:** Hardware-selectable trigger logic via DIP switches for native software compatibility.
* **Robust Hardware Layout:** Standard HAT footprint with heavy-duty screw terminals and a solid soldered header.
* **Excellent Stackability:** Extended header pins keep all Raspberry Pi contacts accessible for further expansion.




## Comprehensive Technical Specifications

* **Number of Channels:** 4 independent relay sockets
* **Relay Compatibility:** Standard industrial relays (e.g., Finder 40 series, Omron G2RL)
* **Socket Type:** Easy-swap sockets (no soldering required for relay replacement)
* **Isolation.** Double isolation (Opto-isolators + Relay)
* **Control Logic:** 3.3V or 5V DC
* **Power Supply:** 5V DC via Raspberry Pi header


## Hardware Configuration
The qReCon Flex features a **2-circuit DIP switch** for hardware-level customization:

### GPIO Selection (GPIO_SEL)
You can choose between two sets of GPIO pins for control to avoid conflicts with other HATs:

* **Relay 1**
    * OFF (B1): GPIO21 (P40)
    * ON (B2): GPIO26 (P37)
* **Relay 2**
    * OFF (B1): GPIO20 (P38)
    * ON (B2): GPIO19 (P35)
* **Relay 3**
    * OFF (B1): GPIO16 (P36)
    * ON (B2): GPIO13 (P33)
* **Relay 4**
    * OFF (B1): GPIO5 (P29)
    * ON (B2): GPIO6 (P31)


### Active Level Setup (POLARITY)
Defines whether the relay activates on a HIGH (1) or LOW (0) signal:

* **OFF (Active High Mode)**
    * GPIO 0 (False): COM-NC
    * GPIO 1 (True): COM-NO
* **ON (Active Low Mode)**
    * GPIO 0 (False): COM-NO
    * GPIO 1 (True): COM-NC



## Compatible Relay Models
The **qReCon Flex** is designed to work with a wide range of standard industrial relays. The following is a **non-exhaustive list** of models that have been tested and are guaranteed to be compatible. Many other brands and models with the same footprint and 5V coil voltage may also work.

* **Schrack:** RT1 (e.g., RT314005), RT2 (e.g., RT424005)
* **Finder:** 40.51.9.005.xxxx, 40.52.9.005.xxxx, 40.61.9.005.xxxx
* **Omron G2RL series:** G2RL-1A-E, G2RL-1A4-E, G2RL-1-E, G2RL-14-E, G2RL-2A, G2RL-2
* **Omron G5RL series:** G5RL-1A-E-LN, G5RL-1A-E-HR, G5RL-1A-E-TV8
* **Critical Requirement:** Always ensure the replacement relay coil voltage is exactly **5V DC**.


## Safety and Installation

* **Relay Selection:** Always ensure the relay coil voltage is **5V DC**. Using relays with different coil voltages may damage the HAT or the Pi.
* **High Voltage Warning**: If using relays for AC switching (up to 250V), touching any part of the high-voltage section during operation is life-threatening.
* **Isolation Zone**: The high-voltage area is clearly demarcated on the PCB with a **thick polygon outline**, **High Voltage icons**, and **"Danger"** labels.
* **Boot Phase Note**: Relay 4 (GPIO5/6) may trigger during boot due to Raspberry Pi default pull-ups. Use `gpio=X=mode,state` in `config.txt` to manage this.

## Resources and Software
Full support and documentation are available on our official **[GitHub repository](https://github.com/aqexhu/qReCon)**:

* **C++ and Shell Utilities:** Ready-to-use tools for controlling the relays.
* **Full User Manual:** Including setup and socket installation guides.