<!--
---
name: SPI
description: Raspberry Pi SPI Anschlüsse
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
-->
#SPI - Serial Peripheral Interface - Serielle Schnittstelle für Erweiterungen

###Bekannt als der 4-Draht serielle Bus, kannst Du mit SPI mehrere Erweiterungen and nur 4 Pins hintereinander schalten.

Ein gutes Beispiel für eine SPI-Erweiterung ist der MCP23S17 Baustein zur Erweiterung der digitalen Ein-/Ausgänge. Beachte das 'S' anstelle der '0' bei der I2C-Version.

