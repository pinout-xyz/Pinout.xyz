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
