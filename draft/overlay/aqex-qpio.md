<!--
---
name: AQEX qPIO
class: board
type: io
formfactor: HAT
manufacturer: AQEX
description: qPIO HAT - 4 Relays, 8 Isolated Inputs - The Raspberry Pi I/O Solution. 
url: https://aqex.eu/qpio-raspberry-pi-io-module-with-8-input-4-output.html
github: 
buy: https://lectronz.com/products/aqex-qpio-4-relays-8-input-hat-raspberry-pi
image: 'aqex-qpio.png'
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
  '11':
    name: Input 2
    mode: input
    active: high
  '13':
    name: Input 1
    mode: input
    active: high
  '15':
    name: Input 3
    mode: input
    active: high
  '29':
    name: Input 4
    mode: input
    active: high
  '31':
    name: Input 8
    mode: input
    active: high
  '32':
    name: Input 7
    mode: input
    active: high
  '33':
    name: Input 6
    mode: input
    active: high
  '35':
    name: Relay 1
    mode: output
    active: high
  '36':
    name: Input 5
    mode: input
    active: high
  '37':
    name: Relay 2
    mode: output
    active: high
  '38':
    name: Relay 3
    mode: output
    active: high
  '40':
    name: Relay 4
    mode: output
    active: high

-->



# AQEX qPIO v1.0
### Industrial I/O Expansion Module for Raspberry Pi (8 Input / 4 Output)
**Official Product Page:** [https://aqex.eu/qpio-raspberry-pi-io-module-with-8-input-4-output.html](https://aqex.eu/qpio-raspberry-pi-io-module-with-8-input-4-output.html)


## Product Concept & Strategic Advantages
The **qPIO** is a professional industrial interface expansion board designed to bridge the gap between the Raspberry Pi’s low-voltage logic and high-voltage industrial environments. It provides robust, isolated control and sensing capabilities, making it an ideal choice for building automation, PLC replacements, and industrial monitoring systems.

Strategic advantages:

* **High-Density I/O Capacity:** Combines 4 relay outputs and 8 isolated inputs on a single, standard HAT footprint.
* **Full Optical Isolation:** All 12 channels (8 inputs and 4 relays) feature optocouplers to safeguard the Pi from noise and spikes.
* **Versatile Input Channels:** Divided into 4 contact-driven and 4 voltage-level channels supporting a wide 3-45V range.
* **Direct GPIO Connection:** Pure hardware-driven design with no I2C or firmware overhead, ensuring instant and reliable execution.
* **Toolless Spring Terminals:** Equipped with high-quality, vibration-resistant spring terminals for quick and secure wiring without tools.
* **Robust Stackable Layout:** Features a solid soldered pin header with extended pins to keep all Raspberry Pi contacts accessible.


## Comprehensive Technical Specifications

* **Input Voltage (Vcc):**  5.0V DC (Powered via Raspberry Pi 40-pin header)
* **Number of Outputs:**  4 (Double Isolated with OMRON Relays)
* **Max Switching Current:**  **10A** (Per relay (at 250V AC))
* **Number of Inputs:**  8 (Opto-isolated digital inputs)
* **Input Versatility:** **Per-channel config** (**Voltage or Dry Contact (Factory-set)**)
* **Input Voltage Range:** 3V – 45V (Applies to "Voltage Level" configured channels)
* **Isolation (Output):** **Double Isolation** (**Optocoupler + Relay galvanic separation**)
* **Isolation (Input):** Opto-isolation (Full protection against industrial transients)


## Input & Output Configuration

### Relay Outputs (4 Channels)
The relays are controlled via the Raspberry Pi's internal GPIO pins.
The relays feature Changeover (CO) contacts (Common, NO, NC) with secondary opto-isolation on the logic side. The outputs are wired to high-quality spring terminals.

* **Relay 1:** GPIO 19 (Pin 35)
* **Relay 2:** GPIO 26 (Pin 37)
* **Relay 3:** GPIO 20 (Pin 38)
* **Relay 4:** GPIO 21 (Pin 40)


### Digital Inputs (8 Channels)
Each input channel (I1-I8) is factory-set to one of the following types:

* **Voltage Level Sensing:** Detects 3V-45V AC/DC signals.
* **Dry Contact Sensing:** Detects the state of potential-free contacts/switches.

* **Input 1:** GPIO 27 (Pin 13) 
* **Input 2:** GPIO 17 (Pin 11)
* **Input 3:** GPIO 22 (Pin 15)
* **Input 4:** GPIO 05 (Pin 29)
* **Input 5:** GPIO 16 (Pin 36)
* **Input 6:** GPIO 13 (Pin 33)
* **Input 7:** GPIO 12 (Pin 32)
* **Input 8:** GPIO 06 (Pin 31)


## Hardware Interface

* **Industrial Terminals (Inputs, Outputs):** High-quality, vibration resistant spring terminals for field wiring.
* **Pass-through Header:** Allows stacking additional HATs (only the used 12 GPIOs are reserved).
* **3.3V Logic:** Internally compatible with the Raspberry Pi's 3.3V signaling level.


## Visual Diagnostics (Status LEDs)
The qPIO features status LEDs for every relay channel, allowing for rapid field diagnostics without software tools:

* **Relay LEDs:** Lights up when the corresponding relay is energized (Active).


## Software Integration

* **Universal Compatibility:** Since it uses standard GPIO pins, it is compatible with any programming language (Python, C++, Node.js, Codesys).
* **Logic Level:**
    * **Output:** Set GPIO to HIGH to energize the relay.
    * **Input:** GPIO will read HIGH when voltage is present on the terminal.


## Safety & Compliance

* **Galvanic Isolation:** The control side (Raspberry Pi) is completely separated from the load/sense side.
* **Overvoltage Protection:** Inputs are designed to withstand industrial transients up to the rated limits.




