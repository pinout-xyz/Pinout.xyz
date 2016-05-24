Cette broche correspond à la ligne de transmission UART, TXD.

UART est communément appelé le bus 'série' (asynchrone). Les données transmises (et reçues) peuvent être facilement consultées depuis la console série. Moyennant un cable de liaison approprié il est également très simple de contrôler votre machine depuis un terminal.

Conseil: le protocol UART est souvent utilisé pour prendre en charge les RasPi sans écran/clavier, et les relier à un réseau.

le bus série est aussi extrêmement pratique pour communiquer avec des microprocesseurs de type Arduino ou Propeller, mais il est important alors de déactiver la console série à l'aide de raspi-config!

[référence UART](/pinout/uart)