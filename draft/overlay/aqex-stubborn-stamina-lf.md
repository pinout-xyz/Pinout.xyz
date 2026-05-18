<!--
---
name: AQEX Stubborn Stamina LF
class: board
type: power
formfactor: Custom
manufacturer: AQEX
description: High-reliability LiFePO4 UPS engineered for long-term Raspberry Pi deployments. Zero-configuration design (no jumpers or settings) ensuring relentless uptime with superior thermal stability and extended cycle life over standard Li-ion.
url: https://www.aqex.eu/stubborn-stamina-lf-raspberry-pi-lfp-ups-hat.html
github: https://github.com/aqexhu/qups-guard
buy: https://lectronz.com/products/aqex-stubborn-stamina-lf-ups-hat-for-the-pi
image: 'aqex-stubborn-stamina-lf.png'
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
  '16':
    name: Power Good
    mode: input
    active: high
  '18':
    name: Limit Low
    mode: input
    active: high
  '22':
    name: Shutdown
    mode: output
    active: high
-->


# Stubborn Stamina LF v1.0

### Ultra-Durable Industrial LiFePo4 UPS HAT for Raspberry Pi
**Official Product Page:** [https://aqex.eu/stubborn-stamina-lf-raspberry-pi-lfp-ups-hat.html](https://aqex.eu/stubborn-stamina-lf-raspberry-pi-lfp-ups-hat.html)


## Product Concept & Strategic Advantages

The **Stubborn Stamina LF** is a high-reliability uninterruptible power supply specifically engineered for long-term industrial deployments. By utilizing **LiFePo4 (Lithium Iron Phosphate)** technology, it offers superior thermal stability and significantly higher cycle life compared to standard Li-ion solutions.

The device is available for purchase **with or without a battery cell**, allowing integrators to select the specific capacity required for their application.

Strategic advantages:

* **Industrial Longevity:** LiFePo4 chemistry ensures thousands of charge cycles and superior thermal stability.
* **Universal Battery Compatibility:** Supports various single-cell (1S) form factors. The modular design allows the use of **18650, 26650, or 32700** cells with matching holders.
* **Flexible Purchasing Options:** Available as a standalone unit or bundled with a **26650 LiFePo4 battery** as the current standard configuration.
* **High Power Delivery:** Specifically designed to handle the peak power demands of the Raspberry Pi 5 (up to 3.5A).
* **Extreme Reliability:** Hardware protection including reverse polarity, deep discharge, and overcharge management.


## Comprehensive Technical Specifications

* **Input Voltage (USB-C):** 5.0V – 5.2V (RPi 5 official power adapter compatible)
* **Output Voltage:** 5.0V DC (Precision regulated for Raspberry Pi)
* **Max Continuous Load:** **3.5A** (Enhanced current delivery for RPi 5 + Peripherals)
* **Max Battery Discharge:** 7.5A (High-rate discharge capability)
* **Charging Current:** 2A (Fast charging for 18650 LiFePo4 cells)
* **Battery Chemistry:** **LiFePo4 ONLY** (Nominal: 3.2V / Charging: 3.6V)
* **Switchover Time:** 100 – 300 μs (No-reboot guaranteed transition)

> **Design Note:** The **Offline topology** ensures almost zero power loss and heat generation during standard operation. A momentary (<1ms) voltage transient occurs during power failure; however, the Raspberry Pi's internal regulation easily filters this, ensuring zero system instability or reboot.


## Battery Management & Protection

* **Protection Circuit:** Deep discharge, Overcharge, Reverse Polarity
* **Thermal Monitoring:** Optional NTC connector (5) for temperature-aware charging
* **Charging Cut-off:** Integrated hardware-level voltage monitoring
* **Low Battery Limit:** Automatic load disconnection at critical voltage


> **Warning:** Use only LiFePo4 cells. Connecting standard 3.7V Li-ion batteries may result in incomplete charging or circuit mismatch.


## Mode Selection

* **OFF:** Complete power cut.
* **ON:** Immediate power-up when power (battery or external) is available.
* **AUTO:** Intelligent start-up logic; only boots the Pi when the battery reaches the "Min" energy level.

## GPIO Communication

The system utilizes a 3-pin GPIO interface for OS-level integration. The following pins are used on the 40-pin Raspberry Pi header:

* **PFO (Power Fail):** — Signals external power loss (HIGH = OK / LOW = Backup Mode).
* **LIM (Limit):** — Signals that the battery has reached the critical low threshold.
* **SHD (Shutdown):** — Handshake signal. The UPS cuts power after the OS pulls this pin LOW (or the daemon signals a halt).


## Visual Diagnostics (LED Indicators)

* **External Power (6)** [Green]: Primary 5V power source detected.
* **Bad Polarity (9)** [Red]: **CRITICAL:** Battery installed backwards!
* **Full** [Green]: Battery fully charged (>3.5V).
* **Min** [Green]: Sufficient energy for a safe boot-shutdown cycle.
* **Safe** [Yellow]: Sufficient energy for a safe shutdown cycle.
* **Low** [Red]: **Critical level.** Immediate shutdown required.


## Intelligent Power Management (IPM)

* **Safe-Start Logic:** Prevents "brown-out" loops by ensuring the Pi only starts when the battery can support the peak current of the boot process.
* **Shutdown Guard:** Monitors the Pi's state and ensures power is only cut after the operating system has safely unmounted the filesystem.
* **Input Threshold Tuning:** Onboard potentiometer allows adjustment for voltage drops caused by long input cables.


## Estimated Runtimes (4000mAh LiFePo4)

* **Raspberry Pi 2:** No Load: 535 min / 100% Load: 285 min
* **Raspberry Pi 3:** No Load: 428 min / 100% Load: 172 min
* **Raspberry Pi 4:** No Load: 413 min / 100% Load: 124 min
* **Raspberry Pi 5:** No Load: 261 min / 100% Load: 109 min

*\*Note: Final runtimes are dependent on battery capacity, age, and ambient temperature.*


## Software Support

* **qups-guard:** Native daemon for automated monitoring and safe shutdown.
* **Compatibility:** Fully compatible with Raspberry Pi OS (Debian-based).
* **Repository:** [github.com/aqexhu/qups-guard](https://github.com/aqexhu/qups-guard)

