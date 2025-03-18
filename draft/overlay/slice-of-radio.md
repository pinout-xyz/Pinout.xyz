<!--
---
name: Slice of Radio
class: board
type: RF
formfactor: Custom
manufacturer: Ciseco
description: A two way RF transceiver for the Raspberry Pi
url: https://www.wirelessthings.net/slice-of-radio-wireless-rf-transciever-for-the-raspberry-pi
buy: https://www.wirelessthings.net/slice-of-radio-wireless-rf-transciever-for-the-raspberry-pi
image: 'slice-of-radio.png'
pincount: 26
eeprom: no
power:
  '1':
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
    name: Send
    direction: output
  '10':
    name: Receive
    direction: input
  '15':
    name: Program
    mode: output
-->
# Slice of Radio

The Slice of Radio is a two way secure wireless RF transceiver for the Raspberry Pi. Sending and recieving via the standard on board Raspberry Pi serial port, it is very easy to use and means you do not need any drivers or special software.

It supports 128bit AES encryption and Over The Air Micro Programming from the Arduino IDE (OTAMP).

The on board "chip" antenna gives good performance for such a small package and can be extended in range by soldering on an 8.2cm wire whip. For even greater range it is possible to fit an antenna using an SMA to u.fl pigtail lead.

Expected range would be around 200m in line of sight with chip antenna, and up to 1000m with an external antenna. It is able to communicate with a wide range of radio nodes such as XRF, SRF, URF, ERF.
