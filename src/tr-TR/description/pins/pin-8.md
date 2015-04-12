Bu pin, [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver/transmitter) transmit (gönderici) pin'i, TXD olarak çalışır.

Bu pin, daha genel adı ile "Serial" olarak da bilinir ve standart olarak Raspberry Pi'niz serial komutları bu pin üzeriden alır ve de konsola iletir. Bu da bir serial kablo ile komut satırından Raspberry Pi'nizi yönetmenizi sağlar.

Ayrıca, UART eğer Arduino veya Propeller gibi kartlar ile konuşacaksanız oldukça elverişlidir, ama önce raspi-config içinde Serial Console'u kapatmanız gerekmekte (disable).

[UART hakkında detaylı bilgi](/pinout/uart)