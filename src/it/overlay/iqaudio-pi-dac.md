<!--
---
description: Un convertitore audio I2S da digitale ad analogico per il Raspberry
pin:
  '15':
    name: Muto/Non-muto
  '22':
    name: Sensore IR
-->
# IQaudIO Pi-DAC+

Il Pi-DAC+ prende i segnali audio digitali (I2S) dal Raspberry Pi e tramite l'integrato 
Texas Instruments PCM5122 DAC restituisce un audio analogico con output variabile 
(controllo volume hardware) ai connettori Pi-DAC+ Phono. Tramite l'amplificatore per cuffia 
Texas Instruments TPA6133A, il Pi-DAC+ supporta direttamente le cuffie tramite il jack audio 
da 3.5mm.

Il Pi Dac usa il GPIO22 per attivare o disattivare il muto sul Pi-AMP+.

Puoi usare il GPIO25 per collegare un sensore infrarossi e il GPIO23/24 per un rotary encoder
(trasduttore di posizione angolare). Entrambe queste parti sono opzionali, ma sono a parte nel 
Pi-DAC+ per un accesso più comodo.

Nota: i pin riservati per l'encoder e il sensore infrarossi possono essere usati per altri scopi 
se gli addon menzionati non sono stati adattati ed abilitati dal software.
