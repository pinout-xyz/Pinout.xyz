<!--
---
description: E/S industrial para Raspberry Pi
-->
# Monarco HAT

Fabricado por Monarco Solutions Group / REX Controls s.r.o., el Monarco HAT es una solución todo en uno para usar la Raspberry Pi en la automatización industrial. Proporciona entradas y salidas analógicas y digitales, así como interfaces de comunicación RS-485 y 1-Wire. De hecho, convierte la Raspberry Pi en un PLC o en un mini PC industrial (IPC) listo para usar en tu proyecto de automatización.

Todas las entradas y salidas están diseñadas para conectarse directamente con sensores y dispositivos industriales estándar, eliminando la necesidad de hardware adicional.

## Características

- **Alimentación: 10-30 VDC**, alimenta también la Raspberry Pi
- **4x entrada digital, 3.5-30 VDC**, aislamiento óptico, GND común
    - 2x contador (pulso/DIR) o 2x encoder (A/B), hasta 200 kHz
    - Retención de los valores del contador con la alimentación apagada
- **4x salida digital**, drenador abierto, máx. 40 VDC, 1 A por canal en continuo
    - Todas con PWM de hasta 100 kHz
    - Protección contra cortocircuitos (continua)
- **2x entrada analógica**, 0-10 V / 0-20 mA, 12 bits
    - Conmutación electrónica del modo de medida de tensión/corriente
    - Protegidas contra sobretensión y polaridad inversa
    - Ancho de banda de 500 Hz, filtro configurable
- **2x salida analógica**, 0-10 V, tiempo de establecimiento de 0,5 ms, 12 bits
- **1x bus RS-485** con protección ESD
- **1x bus 1-Wire** con protección ESD
- **9x indicador LED**, asignados por defecto como indicadores de las entradas y salidas digitales y del estado del sistema, controlables por el usuario
- **Terminales push-in de alta calidad**, conector desmontable
- **Chip RTC con batería** para mantener la hora
- **Watchdog de hardware** para reiniciar la Raspberry Pi en caso de fallo
- Compatible con la **pantalla táctil oficial de 7" de Raspberry Pi** (conector integrado para alimentar la pantalla)
- **Probado en EMC, con marcado CE**
