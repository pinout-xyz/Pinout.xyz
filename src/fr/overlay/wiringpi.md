<!--
---
name: WiringPi
class: interface
type: pinout
page_url: wiringpi
url: http://wiringpi.com
github: https://github.com/WiringPi/WiringPi-Python
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
  '27':
    name: WiringPi 30
  '28':
    name: WiringPi 31
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
#WiringPi sur Raspberry Pi

###WiringPi est un concept proche de la façon dont Arduino adresse ses entrées et sorties, privilégiant la simplicité.

Le but avoué est de définir une librairie unique ainsi qu'un set de fonctions permettant l'accès au GPIO de la Raspberry Pi à partir de plusieurs languages de programmation.

En effet, bien que WiringPi soit une bibliothèque en C au départ, elle est aussi disponible en Ruby et Python. Pour l'installer, un simple "gem install wiringpi" ou "pip install WiringPi" fera l'affaire, pour l'environnement Ruby et Python respectivement.

Pour les usagers Python, noter bien le '2' suivant le 'wiringpi', cette nouvelle version est basée sur WiringPi 2 et incorpore la majorité des fonctionnalités de la version C.

##Premiers pas avec WiringPi

WiringPi présente son propre système de numérotation des broches GPIO, visible sur la gauche de cette page.

Installez la librairie sous Python est particulièrement simple:

```bash
sudo pip install WiringPi
```

Pour toute information supplémentaire, visitez le site officiel de WiringPi!
