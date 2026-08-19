<!--
---
name: MDB HAT
class: board
type: io
formfactor: HAT
manufacturer: Qibixx
collected: Other
description: Interfaz para el bus MDB (Machine Data Bus)
url: https://qibixx.com
buy: https://qiba.pt/
image: 'mdb-pi-hat.png'
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
    name: TxD
    mode: UART
    description: Serial TX > MDB Controller
  '10':
    name: RxD
    mode: UART
    description: Serial RX < MDB Controller
  '19':
    name: SPI_MOSI
    mode: spi
    description: MDB Controller - MOSI
  '21':
    name: SPI_MISO
    mode: spi
    description: MDB Controller – MISO
  '23':
    name: SPI_SCLK
    mode: spi
    description: MDB Controller - SCLK
  '24':
    name: SPI_CE0
    mode: spi
    description: MDB Controller – CS
  '27':
    name: ID_SD
    mode: I2C
    description: ID EEPROM DTA
  '28':
    name: ID_SC
    mode: I2C
    description: ID EEPROM CLK
  '29':
    name: IO2RPI
    mode: output
    description: IO MDB>RPi
  '31':
    name: MDB_RES
    mode: input
    description: MDB Controller Reset
  '33':
    name: IOfromRPi
    mode: input
    description: IO RPi>MDB
-->
# MDB HAT

El MDBHAT de [Qibixx](https://qibixx.com) es un HAT para Raspberry Pi que conecta la Pi con el MDB (Machine Data Bus), presente en máquinas expendedoras y periféricos como los receptores de monedas y billetes. Con su arquitectura avanzada, el MDB HAT admite aplicaciones MDB Master, MDB Peripheral y MDB Sniffing sin necesidad de configurar puentes.

El firmware del MDBHAT se puede actualizar desde la Pi.

Para una conectividad universal, el MDB HAT se conecta a la Pi mediante una interfaz serie o SPI.
El MDB HAT se alimenta desde la Pi, aunque también puede proporcionar hasta 15W (5V, 3A) y retroalimentar la Pi si hay alimentación MDB disponible. En la mayoría de las aplicaciones, el MDB HAT junto con la Pi e incluso otros periféricos se pueden usar sin una fuente de alimentación adicional.

La documentación completa del dispositivo y la información del protocolo están disponibles [aquí](https://docs.qibixx.com).

Se puede encontrar información general sobre MDB y una descripción general de la familia de dispositivos [aquí](https://mdb.technology).
