<!--
---
name: Pi PoE Switch HAT
class: board
type: power
formfactor: Custom
manufacturer: Pi Supply
description: The Pi PoE Switch HAT is a power over ethernet add-on board for the Raspberry Pi
url: https://www.kickstarter.com/projects/pisupply/pi-poe-switch-hat-power-over-ethernet-for-raspberr
github: https://github.com/PiSupply/PiPoE
buy: https://www.pi-supply.com/product/pi-poe-switch-hat-power-over-ethernet-for-raspberry-pi/
image: 'pisupply-pi-poe.png'
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
  '11':
    name: Power Management
  '15':
    name: LED Green/Yellow
  '16':
    name: LED Green
  '18':
    name: LED Yellow/Green
-->
#Pi PoE Switch HAT

El Pi PoE Switch HAT es una placa añadida para Raspberry Pi que lleva la tecnología Switch de Pi Supply junto a PoE.

Ahora puedes alimentar tu Raspberry Pi y proporcionar una conexión Ethernet en cualquier lugar con un solo cable. Perfecto para eliminar el amasijo de cables y para poder utilizar en localizaciones remotas.

* PoE 802.3af (A y B) completo
* Circuito de regulación de corriente físico, presentándose como Class 0 device
* Modo de alimentación switch completamente aislado (SMPS) - aislamiento entrada a salida de 1500V
* Protección contra sobrecarga y cortocircuito
* Protección contra sobretemperatura
* Alta eficiencia (hasta 87 %) de salida regulada
* Voltaje de entrada de 36-56V, salida de 5V, corriente de salida 10-1300mA, potencia de salida máxima 6.5W
* Microcontrolador ATtiny 13A para controlar la alimentación
* Deja todos los GPIO sin utilizar disponibles para otras placas

El cable jumper opcional proporciona los siguientes modos:

* Conectado. Pi PoE se encenderá tras apretar el botón durante dos segundos
* Desconectado: Pi PoE se encenderá tan pronto como conectes la alimentación
