# Servo/PWM HAT

El Servo/PWM HAT de Adafruit permite controlar 16 salidas servo o PWM a través de I2C con sólo 2 pines.
El controlador PWM incluido en la placa controlará los 16 canales simultáneamente sin ningún procesamiento adicional por parte de Raspberry Pi. Utilizando un sistema de direcciones binaria, mediante cables soldados al PCB, es posible acoplar hasta 62 HATs para controlar hasta 992 servos, utilizando solo el puerto I2C.

Nota importante: los servos pueden utilizar mucha energía y no es buena idea utilizar el puerto de 5V de Raspberry Pi para alimentarlos. Interferencias eléctricas y apagones debido al excesivo consumo eléctrico pueden dar lugar a un comportamiento extraño de Raspberry Pi, reinicios y/o sobrecalentamiento. ¡Mantén la alimentación de Raspberry Pi y la de los servos separadas!
