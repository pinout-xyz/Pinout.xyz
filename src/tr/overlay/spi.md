<!--
---
name: SPI
class: interface
type: pinout
description: Raspberry Pi SPI pinleri
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

### four-wire serial bus olarak da bilinen SPI, bir pin setinden birden fazla adresteki birden fazla uygun cihazı [papatya zinciri](https://tr.wikipedia.org/wiki/Papatya_zinciri) yapıp yönetmenizi sağlar.

SPI portunuz ayrıca Gordon Henderson'un modifiye AVRDude'una Arduino skeçleri yükleyerek ATmega 328'ye "[bit banging](http://en.wikipedia.org/wiki/Bit_banging)" de yapabilirsiniz.

Raspberry Pi'nizin SPI port'unu ATmega'nıza bağlayın ve ATmega'yı Raspberry Pi'nin 3.3v gücüyle besleyip açın. SPI sürücüleri çalıştırmadığınızdan emin olduktan sonra "`avrdude -p m328p -c gpio`" komutu ile bağlantıyı kontrol edin.

ATmega'nız varsa her bir pin için ayrı ayrı tıklayarak nasıl bağlayabileceğinizi öğrenebilirsiniz.
