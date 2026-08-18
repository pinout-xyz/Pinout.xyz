<!--
---
name: AQEX qReCon
class: board
type: relay
formfactor: HAT
manufacturer: AQEX
description: qRecon - Configurable 4-Channel Relay HAT for Raspberry Pi IO Expansion. 
url: https://www.aqex.eu/qrecon-raspberry-pi-relay-module-with-4-output.html
github: https://github.com/aqexhu/qReCon
buy: https://lectronz.com/products/aqex-qrecon-quality-relay-hat-raspberry-pi
image: 'aqex-qrecon.png'
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


# AQEX qReCon v2.2/v2.3
###  Configurable 4-Channel Relay HAT for Raspberry Pi IO Expansion
**Official Product Page:** [https://www.aqex.eu/qrecon-raspberry-pi-relay-module-with-4-output.html](https://www.aqex.eu/qrecon-raspberry-pi-relay-module-with-4-output.html)


## Product Concept & Strategic Advantages
The **qReCon** is a high-quality 4-channel relay output module designed specifically for Raspberry Pi and other microcomputers. Featuring **premium Schrack relays**, **optical isolation**, and **configurable GPIOs** and **Active High and Active Low control**, it gives you the confidence and reliability your projects deserve. It allows low-voltage logic devices to control high-voltage and high-current external AC/DC loads with maximum safety.


## Strategic Advantages

* **Premium Switching Hardware:** High-end Austrian SCHRACK relays ensure long operational lifespan for critical workloads.
* **Galvanic & Optical Isolation:** Integrated optocouplers fully protect the Raspberry Pi from voltage spikes and noise.
* **Zero-Firmware Reliability:** Pure hardware design works instantly out of the box without software configuration.
* **Configurable GPIO Selection:** Onboard DIP switches allow easy selection of control pins to avoid conflicts with other HATs.
* **Selectable Active High/Low Logic:** Hardware-selectable trigger logic via DIP switches for native software compatibility.
* **Robust Hardware Layout:** Standard HAT footprint with heavy-duty screw terminals and a solid soldered header.
* **Excellent Stackability:** Extended header pins keep all Raspberry Pi contacts accessible for further expansion.


## Comprehensive Technical Specifications

* **Number of Channels:** 4 independent relay circuits
* **Relay Type:** SPDT (Toggle switch: COM, NC, NO)
* **Relay Brand:** Schrack (Premium quality)
* **Max. AC Voltage:** 250V AC
* **Max. DC Voltage:** 28V DC (10A)
* **Max. Current (NO):** 10A
* **Max. Current (NC):** 3A
* **Isolation:** Double isolation (Opto-isolators + Relay)
* **Control Logic:** 3.3V or 5V DC
* **Feedback:** 4x Status LEDs (one per channel)


## Hardware Configuration
The qReCon features a **2-circuit DIP switch** for hardware-level customization:

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


## Safety and Installation
* **High Voltage Warning**: The relay outputs can carry up to 250V AC. Touching terminals during operation is life-threatening.
* **Isolation Zone**: For safety identification, the high-voltage areas on the PCB are clearly marked with a **thick polygon outline**, including a **High Voltage icon** and **"Danger"** / **"High Voltage"** labels.
* **Boot Phase Note**: Relay 4 (GPIO5/6) may be active at boot due to Raspberry Pi's internal pull-up resistors. This can be modified in `/boot/firmware/config.txt` using the `gpio=X=mode,state` command.


## Resources and Software
To support your development, the following resources are available on our official **[GitHub repository](https://github.com/aqexhu/qReCon)**:

* **C++ Sample Program:** A ready-to-use example to help you integrate the qReCon into your software environment quickly.
* **Full User Manual:** Detailed documentation including  safety instructions.

