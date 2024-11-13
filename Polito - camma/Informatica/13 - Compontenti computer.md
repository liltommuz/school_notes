

Leggi le slide alla fine manca qualcosa. :(

Un processore normale anche quando non fa nulla consuma energia, poiche essendo un sistema sincrono necessità di generare la funzione d'onda del clock, che quando non fa niente è impostate a 1 Hz.

Se si puo i calcoli li faccio sui numeri interi.
I dati vanno tenuti in memoria, non tenuti nel file.

Tempo di esecuzione di un programma, non deve essere infinito : >
### Memoria

Raggruppa dispositivi etergogenei con caratterstiche molto diverse tra loro.

- Indirizzamento
- Parallelismo (Quanti byte contiene una cella di memoria)
- Accesso (sequenziale o casuale)
- Struttura gerarchica 

##### Indirizzamento
Ogni cella di memoria ha un indirizzo univoco, non c'è ambiguità.

##### Parallelismo
Ogni cella può memorizzare una quantità fissa di bit (Si usano i byte)

- 2 byte -> Word
- 4 Byte -> Double Word
- 8 Byte -> Quad Word

A quanti dati posso accedere con un'unica istruzione.

##### Gerarchia di memoria

Idealmente una memoria dovrebbe essere:

- Il piu grande possibile
- Veloce
- Economica
- Memoria non volatile, persistente.

La memoria è organizzata in livelli, che si distinguono a seconda della distanza dalla cpu.
- Piu sono vicini, piu la memoria è piccola e veloce
	- Registri
	- Cache on Chip
	- Cache di secondo livello
	- RAM
	- dischi o ssd (Memorie di sistema)

Piu mi allontano, piu sono lente e meno capienti e dunque meno costose.
###### Ram statica vs dinamica (Sempre volatili)

Nella statica scrivo qualcosa, e l'informazione è mantenuta finchè non la cambio.
Nelle dinamiche, l'informazione col tempo si perde anche se non la cambio.
>Necessità di cicli di rinfresco, per non perdere l'informazione

###### Cache

Il lavoro della cache è quello di avvicinare le informazioni al processore, informazioni che stanno nei dischi o nella ram, si occupa di questo processo il SO.
Il SO porta al processore nella cache ciò che serve al processore piu frequentemente.

###### Dischi

Sono scritti magneticamente, la testina si avvicina alla superficie del disco e legge le informazioni codificate come campi magnetici.
Nei dischi moderni, le velocità di rotazione sono intorno alle 1000 rpm, cio comporta:
- Avere un motore che tiene in funzione i dischi, consuma tanta energia.
- I punti dell'oggetto hanno la stessa velocità angolare, ma non tangenziale, i punti vicino ai bordi vanno piu veloci - a volte le informazioni non erano piu leggibili
	- è piu facile leggere i settori interni rispetto ai settori esterni.
- Un oggetto in movimento crea un momento torcente non banale, che rende difficile tentare di ruotarlo di 90°

Inoltre quando salta la corrente, le testine si abbassano sui piatti, è molto probabile che il settore sopra viene rovinato.

nelle ssd invece non succede questi problemi.

#### BUS

Che tipo di connessioni ci possono essere?
A livello teorico, n componenti si connettono ad n componenti.
- Una connessione punto punto non è gestibile, poiche non scalare.
- Si utilizza un bus unico, e tutti si attaccano al bus, ogni componente ha una freccia direzionale che indica l'Input o l'output, puo essere anche bidirezionale.

![BUS](https://i.ytimg.com/vi/cu7V2XgapCA/maxresdefault.jpg)

>La risorsa piu importanti in un sistema è il BUS,

Il BUS dipende dal chipset, il chipset comanda il BUS, se scarso i trasferimenti saranno lenti e quindi il sistema andrà piano.
Quando due componenti parlano, gli altri non possono parlare e devono aspettare che gli altri finiscono di comunicare.

La scheda video ha un bus dedicato, al quale si collega solo lei.
La CPU comanda e gestisce le comunicazioni, è il master e gli altri sono slave.

I bus vanno alla velocità dei GHz, e non hanno angoli retti (Poichè costituiscono delle antenne).

Svantaggi:
- Essendo un dispositivo condiviso, può diventare un collo di bottiglia

##### Bus di sistema

Il bus di sistema è diviso in 3 parti.
- **Data bus** - Bus che permette di trasferire da e verso memorie varie i dati.
- **Address bus** - Bus che permette di indirizzare univocamente i dispositivi e le celle di memoria
- **Control bus** - Serve al master per controllare lo stato dei dispostivi, ma anche verificare l'esito delle operazioni: se sono andate a buon fine o no e agire di conseguenza

Tutti i periferici vengono visti come indirizzi in memoria di alcune celle, indirizzi univoci.
L'indirizzo che si usa per accedere al disco sono diversi da quelli della RAM o altri dispositivi.


#### Massima memoria interna

Abus ha tot fili
Dbus ha tot fili

Qual è la massima memoria installabile sul sistema? (Qual è la massima indirizzabile?)

>Esempio.

Abus = 20
Dbus = 16

mem = 2^20
max mem = 2^20 x 2 byte = 2 MB (Cella di memoria ha lo stesso parallelismo del Dbus)

>Esempio

Memoria = 15 Mb

quanti fili di indirizzi ho bisogno per indirizzare una memoria di 15 Mb ?

- Ogni cella ha lo stesso numero di parallelismo del databus percio:
	- log in base 2 della memoria = Abus
	- e allora i fili saranno (parte intera (Abus)+ 1)

#### Sistema Operativo

Gestisce le risorse Hardware e Software della macchina.
Permette all'utente di poter usare le risorse.

Servizi tipici SO:
- Interprete dei comandi
- Gestione dei processi (Un processo richiede CPU, memoria mentre un programma non necessita niente) Il gestore dei processi è lo scheduler.
	[Programma in esecuzione = processo]
- Gestione della memoria principale e secondaria
- Gestione dei dispositivi I/O
- Gestione file e filesystem
- Implementazione dei meccanismi di protezione
- Gestione delle reti e sistemi distribuiti

