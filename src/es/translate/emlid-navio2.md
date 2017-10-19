<!--
---
name: Navio2 Autopilot
class: board
type: gps,motor,sensor
formfactor: HAT
manufacturer: Emlid
collected: Other
description: Full drone controller for Raspberry Pi
url: https://docs.emlid.com/navio2/
github: https://github.com/emlid/Navio2
buy: https://emlid.com/shop/navio2/
image: 'emlid-navio2.png'
pincount: 40
eeprom: setup
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
  '3':
    name: MS5611 Data
    mode: i2c
  '5':
    name: MS5611 Clock
    mode: i2c
  '7':
    name: Red LED
    mode: output
    active: high
  '13':
    name: Green LED
    mode: output
    active: high
  '15':
    name: LSM9DS1 Magneto CS
    mode: chipselect
    active: high
  '16':
    name: MPU9250 Interrupt
    mode: output
    active: high
  '18':
    name: RCIO PC10
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: LSM9DS1 Accel/Gyro CS
    mode: chipselect
    active: high
  '23':
    mode: spi
  '24':
  '26':
    name: MPU9250 Chip Select
    mode: chipselect
    active: high
  '29':
    name: RCIO PC11
  '31':
    name: Blue LED
    mode: output
    active: high
  '32':
    name: RCIO Clock
  '33':
    name: RCIO Data
  '35':
    name: RCIO MISO
    mode: spi
  '36':
    name: RCIO Chip Select
    mode: chipselect
    active: high
  '38':
    name: RCIO MOSI
    mode: spi
  '40':
    name: RCIO SCLK
    mode: spi
i2c:
  '0x77':
    name: Barometer
    device: MS5611
-->
# Navio2 Autopilot

Navio2 Autopilot está diseñado tanto para tus propios proyectos de robótica como para la versión Linux de AMP (ArduPilot).

Navio2 elimina la necesidad de múltiples controladores para hacer más sencillo el desarrollo y aumentar la robustez del proyecto. Aumenta la conectividad y permite controlar todo tipo de robots que se desplacen: coches, barcos, multirrotores, aviones.

Para un conocimiento preciso de la posición y la orientación Navio2 está equipado con doble IMU y receptor GPS/Glonass/Beidou. PWM, ADC, SBUS y PPM están integrados en Linux sysfs gracias al coprocesador RC I/O incluído en la placa, permitiendo acceder fácilmente con cualquier lenguaje de programación.

Especificaciones:

* MS5611 barómetro (I2C1)
* MPU9250 9DOF IMU (SPI0)
* LSM9DS1 9DOF IMU (SPI0)
* Ublox M8N Glonass/GPS/Beidou (SPI0)
* 14 PWM salidas servo (RCIO/SPI1)
* PPM/S.Bus entrada (RCIO/SPI1)
* 6-canales ADC (RCIO/SPI1)
* Integrado RGB LED
* UART, I2C terminales para conexiones
* Conector de corriente
* Fuente de alimentación triple 
