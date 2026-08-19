<!--
---
name: SPI
class: interface
type: pinout
description: Pines SPI Raspberry Pi
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

### Conocido como el bus serial de cuatro cables, SPI te permite encadenar múltiples dispositivos desde un solo set de pines, asignando a cada chip un pin distinto de Chip Select.

Un útil ejemplo de un periférico SPI es el MCP23S17, expansor de puertos digital. Fíjate en la S en lugar del 0 encontrado en la versión I2C

Para comunicarse con un dispositivo SPI, es necesario encender el pin de Chip Select correspondiente al chip. Por defecto la Pi tiene CE0 y CE1.

```python
import spidev

spi = spidev.SpiDev()
spi.open(0, CHIP_SELECT_0_OR_1)
spi.max_speed_hz = 1000000
spi.xfer([value_8bit])
```

También puedes usar el puerto SPI para cargar programas en un ATmega328 (Arduino), con el AVRDude modificado de Gordon Henderson.

Conecta el puerto SPI de la Pi al del ATmega, y alimenta el ATmega desde el pin de 3.3v de la Pi. Asegúrate de que ningún controlador SPI está en ejecución, y ejecuta "avrdude -p m328p -c gpio" para verificar la conexión.

Observa los pines individuales para aprender como conectar tu ATmega.
