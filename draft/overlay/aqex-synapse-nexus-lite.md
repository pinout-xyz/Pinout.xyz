<!--
---
name: AQEX Synapse Nexus Lite
class: board
type: io
formfactor: HAT
manufacturer: AQEX
description: AQEX Synapse Nexus Lite - Essential Raspberry Pi IO Module for Simple Tasks
url: https://www.aqex.eu/synapse-nexus-lite-raspberry-pi-io-hat.html
github: https://github.com/aqexhu/piohat
buy: https://lectronz.com/products/aqex-qpio-10lite-io-hat-for-the-pi
image: 'aqex-synapse-nexus-lite.png'
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
  '8':
    name: Relay Output 1
    mode: output
    active: high
  '10':
    name: Relay Output 1
    mode: output
    active: high
  '11':
    name: Input 1
    mode: input
    active: high
  '13':
    name: Input 2
    mode: input
    active: high


-->


# Synapse Nexus Lite v1.0
### Industrial Compact I/O Module for Raspberry Pi (2 Input / 2 Output)
**Official Product Page:** [https://www.aqex.eu/synapse-nexus-lite-raspberry-pi-io-hat.html](https://www.aqex.eu/synapse-nexus-lite-raspberry-pi-io-hat.html)



## Product Concept & Strategic Advantages
The **Synapse Nexus Lite** is a cost-optimized industrial expansion board designed for applications that require a limited number of I/O points without compromising on electrical safety. While maintaining the standard Raspberry Pi HAT form factor, it offers a streamlined 2-in/2-out configuration, making it the most economical choice for simple automation and remote signaling tasks.


Strategic advantages:

* **Double Isolated Outputs:** Each relay output is protected by **dual isolation (Optocoupler + Mechanical Relay)**, ensuring the Raspberry Pi is completely decoupled from high-voltage loads.
* **SPDT Relay Configuration:** Features versatile **Single Pole Double Throw (SPDT)** relays, providing both Normally Open (NO) and Normally Closed (NC) contacts for maximum wiring flexibility.
* **Standard Voltage Inputs:** Features 2 opto-isolated digital inputs designed for **Voltage Level Sensing (3V-45V)**.
* **Cost-Efficient Industrial Build:** Focused on essential features and high-capacity (10A) switching to provide a more affordable industrial interface.
* **Industrial Connectivity:** Equipped with vibration-proof **Push-in (spring-type) terminal blocks** for rapid, tool-less field wiring.
* **Low GPIO Footprint:** Uses only 4 GPIO pins, leaving the rest of the 40-pin header free for other expansions.



## Comprehensive Technical Specifications

* **Input Voltage (Vcc):** 5.0V DC (Powered via Raspberry Pi 40-pin header)
* **Number of Outputs:** 2 (Double Isolated **SPDT** Relays)
* **Max Switching Current:** **10A** (Per relay (at 240V AC / 24V DC))
* **Number of Inputs:** 2 (Opto-isolated digital inputs)
* **Input Type:** **Voltage Level** (**Standard 3V – 45V DC sensing**)
* **Isolation (Output):** **Double Isolation** (**Optocoupler + Relay galvanic separation**)
* **Terminal Type:** **Push-in Spring** (Tool-less industrial terminal blocks)


## Input & Output Configuration

### Relay Outputs (2 Channels)
The module uses **SPDT** relays with full Changeover (CO) functionality. The logic side is protected by secondary opto-isolation.

* **Relay 1:** GPIO 14 (Pin 8) - Contact: SPDT (CO)
* **Relay 2:** GPIO 15 (Pin 10) - Contact: SPDT (CO)


### Digital Inputs (2 Channels)
Standard opto-isolated inputs for detecting industrial voltage levels.

* **Input 1** GPIO 17 (Pin 11)
* **Input 2** GPIO 27 (Pin 13)


## Hardware Interface

* **Industrial Terminals (Inputs, Outputs):** High-quality, vibration resistant spring terminals for field wiring.
* **Pass-through Header:** Allows stacking additional HATs (only the used 4 GPIOs are reserved).
* **3.3V Logic:** Internally compatible with the Raspberry Pi's 3.3V signaling level.


## Software Integration

* **Logic Level:**
    * **Output:** Setting GPIO to HIGH energizes the relay.
    * **Input:** The GPIO reads HIGH when the input is active (Voltage present).
* **Compatibility:** Fully compatible with all Raspberry Pi models and standard programming environments (Python, C++, Node.js, Codesys).


## Safety & Compliance

* **Galvanic Isolation:** The control side (Raspberry Pi) is completely separated from the load/sense side.
* **Overvoltage Protection:** Inputs are designed to withstand industrial transients up to the rated limits.

