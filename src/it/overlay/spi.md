<!--
---
name: SPI
class: interface
type: pinout
description: Pin SPI del Raspberry
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/
pincount: 5
pin:
  '11':
    name: SPI1 CE1
  '12':
    name: SPI1 CE0
  '19':
    name: SPI0 MOSI
    direction: output
    active: high
    description: Master Out / Slave In
  '21':
    name: SPI0 MISO
    direction: input
    active: high
    description: Master In / Slave Out
  '23':
    name: SPI0 SCLK
    direction: output
    active: high
    description: Clock
  '24':
    name: SPI0 CE0
    direction: output
    active: high
    description: Chip Select 0
  '26':
    name: SPI0 CE1
    direction: output
    active: high
    description: Chip Select 1
  '35':
    name: SPI1 MISO
  '36':
    name: SPI1 CE2
  '38':
    name: SPI1 MOSI
  '40':
    name: SPI1 SCLK
  '27':
    name: SPI CE0
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '28':
    name: SPI MISO
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '3':
    name: SPI MOSI
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '5':
    name: SPI SCLK
    supported: Pi 4 (spi3) and Pi 5 (spi2)
  '7':
    name: SPI CE0
    supported: Pi 4 (spi4) and Pi 5 (spi3)
  '29':
    name: SPI MISO
    supported: Pi 4 (spi4) and Pi 5 (spi3)
  '31':
    name: SPI MOSI
    supported: Pi 4 (spi4) and Pi 5 (spi3)
  '32':
    name: SPI CE0
    supported: Pi 4 and Pi 5 (spi5)
  '33':
    name: SPI MISO
    supported: Pi 4 and Pi 5 (spi5)
  '8':
    name: SPI MOSI
    supported: Pi 4 and Pi 5 (spi5)
  '10':
    name: SPI SCLK
    supported: Pi 4 and Pi 5 (spi5)
-->
# SPI - Serial Peripheral Interface

### Conosciuto come il bus seriale "four-wire", l'SPI ti permette di concatenare una serie di periferiche compatibili su un solo set di pin assegnandogli dei diversi pin chip-select.

Un esempio efficace di una periferica SPI è l'MCP23S17, un chip IO expander digitale (nota la S al posto dello zero nella versione I2C).

Per comunicare con una periferica SPI, devi controllare il suo chip-select pin corrispondente. Di default, il Raspberry ha CE0 e CE1.

```python
import spidev

spi = spidev.SpiDev()
spi.open(0, CHIP_SELECT_0_OR_1)
spi.max_speed_hz = 1000000
spi.xfer([value_8bit])
```

Puoi utilizzare anche le porte SPI per fare "Bit-Bang" su un ATmega 328, caricando i progetti di Arduino tramite la versione modificata 
dell'AVRDude di Gordon Henderson.

Collega la porta SPI del Raspberry a quella dell'ATmega, ed alimenta l'ATmega dal pin a 3.3V sul Raspberry. 
Assicurati di non avere alcun driver SPI in esecuzione, ed esegui "avrdude -p m328p -c gpio" per verificare la connessione.

Controlla i pin individuali per imparare come collegare il tuo ATmega.
