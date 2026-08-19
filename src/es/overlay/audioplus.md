 
# Audio +


RaspiAudio habilita tu Raspberry Pi (Pi 3, 2, B +, A + y Zero) con un DAC de audio de vanguardia.

Ideal para sistemas de sonido de audio para el hogar, una radio por Internet o cualquier proyecto con audio.

## Especificaciones:


1. Audio DAC I2 de 24 bits a 96 kHz con calidad de muestreo de estudio

2. Incluye conector estéreo RCA dual con salida de línea estéreo (se requiere soldadura)

3. Salida de línea estéreo jack 3.5mm

4. Cabezal hembra 2x20 (requiere soldadura)

5. Compatible con Raspberry Pi 3, 2, B +, A + y Zero

## Instalación para usuarios de Raspbian:

* Asegúrate que el conector jack está conectado al amplificador:

* Abre terminal y ejecuta:

```bash
sudo wget -O - script.raspiaudio.com | bash
```

* Responda que sí para reiniciar
* Si todo fue bien, debería escuchar un sonido de prueba al escribir este comando:

```bash
sudo speaker-test -l5 -c2 -t wav
```

* ¡NUEVO! : En el próximo reinicio, podrá controlar el volumen desde su escritorio o mediante la herramienta de línea de comandos `alsamixer`
