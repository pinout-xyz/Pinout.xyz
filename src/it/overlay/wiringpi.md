<!--
---
name: Mappa pin GPIO WiringPi
description: Mappa pin GPIO WiringPi
pincount: 40
pin:
  '3':
    name: WiringPi 8
  '5':
    name: WiringPi 9
  '7':
    name: WiringPi 7
  '8':
    name: WiringPi 15
  '10':
    name: WiringPi 16
  '11':
    name: WiringPi 0
  '12':
    name: WiringPi 1
  '13':
    name: WiringPi 2
  '15':
    name: WiringPi 3
  '16':
    name: WiringPi 4
  '18':
    name: WiringPi 5
  '19':
    name: WiringPi 12
  '21':
    name: WiringPi 13
  '22':
    name: WiringPi 6
  '23':
    name: WiringPi 14
  '24':
    name: WiringPi 10
  '26':
    name: WiringPi 11
  '29':
    name: WiringPi 21
  '31':
    name: WiringPi 22
  '32':
    name: WiringPi 26
  '33':
    name: WiringPi 23
  '35':
    name: WiringPi 24
  '36':
    name: WiringPi 27
  '37':
    name: WiringPi 25
  '38':
    name: WiringPi 28
  '40':
    name: WiringPi 29
-->
#Raspberry Pi WiringPi

###WiringPi è un tentativo di portare la semplicità di connessione dell'Arduino sul Raspberry.

L'idea è di avere un'unica piattaforma comune e un insieme di funzioni per accedere alle porte GPIO da diversi linguaggi. 
WiringPi ha il cuore in una libreria C, ma è disponibile sia per Ruby che per Python; gli utenti possono installarla usando 
rispettivamente "gem install wiringpi" e "pip install wiringpi2".

Gli utenti Python noteranno il 2 alla fine del pacchetto; la libreria WiringPi2-Python finalmente porta tutta una serie di 
funzionalità preesistenti di WiringPi a Python, incluse le ultime presenti in WiringPi 2.

##Primi passi con WiringPi

WiringPi usa il suo sistema di numerazione dei pin; qui imparerai come WiringPi indicizza i pin GPIO, cosa fanno tali pin e 
come realizzare progetti interessanti con Python o Ruby.

Installarla in Python non potrebbe essere più semplice. Semplicemente:

```bash
sudo pip install wiringpi2
```

Per maggiori informazioni su WiringPi, dai un'occhiata al loro sito ufficiale.
