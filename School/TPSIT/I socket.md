### Introduzione ai Socket

I socket sono un'interfaccia software che viene utilizzata nella comunicazione tra nodi all'interno delle reti o tra processi all'interno di un nodo.
Esistono due famiglie di socket:

- **Internet Socket**
    Per la comunicazione tra processi di macchine remote
- **Unix Domain Socket**
    Per la comunicazione tra processi della stessa macchina

In una rete di calcolatori, nella maggior parte dei casi si utilizza la comunicazione client-server.
Questa comunicazione avviene secondo alcune fasi:
- **Il client manda** un messaggio di richiesta al **server**. (**Request**)
- **Il server elabora** la risposta e la spedisce al **client**. (**Response**)

**I socket vengono utilizzati per identificare il protocollo che si vuole utilizzare (HTTP, FTP, ...) e con chi si vuole comunicare attraverso la rete.**

**Un nodo in una rete è identificato da un'indirizzo IP** (indirizzamento nel protocollo TCP/IP).
Esso **puo avere piu processi in esecuzione**, per questo motivo si utilizzano le **porte logiche**, che **servono a rilevare il processo in esecuzione su una macchina.**

Le porte sono rappresentate attraverso un numero compreso tra 0 e 65535 e rappresentano l'indirizzamento a **livello Transport**.

Un **server si mette in ascolto su un numero di porte ben preciso**, HTTP -> porta 80. HTTPS -> 443
che rappresentano il processo in esecuzione sulla macchina.
Un client per visitare la pagina web **deve rivolgersi ad un preciso processo e ad una precisa macchina.**
							**IndirizzoIP:Porta**
Dove:
- **L'indirizzio Ip è l'indirizzo di destinazione della macchina**
- **La porta rappresenta un processo in esecuzione in quella macchina**

**Un computer (il client) dovrà conoscere l'indirizzo IP del computer remoto** (ilserver) **specificando una particolare estensione definita Numero di Porta** (port number), che per semplicità viene spesso chiamata semplicemente porta.

Ad esempio si supponga che un client contatti un server remoto per visualizzare una data pagina
web.
Per stabilire la connessione il client dovrà risolvere l'hostname in un indirizzo IP e dovrà stabilire
con quest'ultimo una connessione su una ben specifica porta.
**Per stabilire questa connessione, quindi, il client dovrà utilizzare un socket composto dall'IP e dalla porta.**

### I socket e i protocolli per la comunicazione di rete

Un'**applicazione di rete è costtuita da un'insieme di programmi ceh vengno eseguiti su due o piu computer contemporaneamente.**
I programmi operano tra di loro **utilizzando risorse comuni, accedendo conccorrentemente al database.**
L'applicazione di rete si dice **applicazione distribuita, dato che non viene eseguita su un solo elaboratore ed è composta da piu elementi cooperanti che stanno in una rete di calcolatori.**

**I processi devono scambiarsi messaggi**, per comunicare devono mettersi "in contatto" **tramite i loro indirizzi e utilizzare i servizi offerti dal livello di applicazione.**
Essi **possono comunicare se sono collegati attraverso un sistema di comunicazione e utilizzano lo stesso protocollo di comunicazione.**

Un **protocollo di comunicazione è l'insieme delle regole che devono essere seguite affinche i due elaboratori possano comprendersi.**
I protocolli stabiliscono gli aspetti **fisici** (supporto fisico ,ecc ) e **logici** (meccanismo di commutazione, regole di codifica, ecc) della comunicazione.
Essi **sono organizzati secondo una gerarchia che prevede che ogni protocollo si appoggi a protocolli di livello piu basso per fornire un servizio di qualità superiore.**

##### Pila protocollare TCP/IP

La pila protocollare di Internet è costituita da 5 livelli.
L'unità di informazione viene gestita ad ogni livello ed assume forma e nome diverso, dato che ad ogni passaggio vengono aggiunte informazioni necessarie a ciascun protocollo.

- **Application layer**, viene eleborato il tipo di dato **messaggio**
- **Transport layer**, viene elaborato il tipo di dato **segmento**
- **Network layer**, viene elaborato il tipo di dato **datagram**
- **Data Link**, viene elaborato il tipo di dato **frame**
- **Physic layer**, viene elaborato un segnale fisico

Lo strato di trasporto della rete Internet offre alle applicazioni due distinti protocolli di trasporto ceh svolgono servizi diversi:
- **TCP** (Transmission Control Protocol)
- **UDP** (User Datagram Protocol)

Ogni applicazione prima di comunicare sceglie il protocollo da utilizzare.
La differenza fondamentale tra i due è:
- **Il protocollo TCP** è orientato alla connessione ed è affidabile dato che **consente il controllo dell'integrità dell'informazione contenuta nei pacchetti e dispone di un sistema per segnalare l'errore al mittente** (ACK-NOACK).
- **Il protocollo UDP** è senza connessione e quindi non affidabile.

##### Porte di comunicazione

Affinché un processo possa **inviare un messaggio a un qualsiasi altro host**, il processo mittente deve identificare il processo destinatario **univocamente**

Generalmente **ogni PC ha una sola porta fisica di connessione al network,** pero **possono esserci piu applicazioni che necessitano di comunicare utillizzando la rete**, per questo motivo si utilizzano le **porte logiche**, identificare da un numero detto **port address**.
Con queste porte **si possono instaurare contemporaneamente piu comunicazioni e far comunicare 2 applicazioni anche se il computer sta effettuando altre comunicazioni, basta utilizzare un'altra porta.**

- Le **porte da 0 a 1023 sono riservate ad applicazioni particolari,** che costituiscono i **well-known port numbers** e possono essere **utilizzati solo da server in apertura passiva.**
- Le **porte da 1024 a 49151 sono riservate a porte registrate** e possono essere utilizzate da alcunni servizi ma **soprattutto dai client per collegarsi a servizi da remoto**.
- Le **porte da 49152 a 65535 sono libere per essere assegnate dinamicamente dai processi applicativi.**

I **numeri di porta logica sono relativi soltanto al protocollo considerato.**
Una porta nel TCP e diversa nell'UDP.
Inoltre **il solo numero di porta non è abbastanza per descrivere univocamente una connessione**.
Si utilizzano i socket, si abbina la porta all'IP address.

Esempio:
-
Un caso tipico è quello rappresentato da un server sul quale sono disponibili più servizi, tra i quali:

**e-mail:** viene inviata usando il protocollo applicativo SMTP, quindi occorre inviare un messaggio opportunamente codificato alla porta TCP 25 del server;

**sito Web**: per richiedere una pagina Web si usa il protocollo applicativo HTTP, che invia un opportuno messaggio di richiesta alla porta TCP 80 del server;

**la trasformazione di un nome di un calcolatore in un indirizzo IP**: che consiste nell’inviare un’opportuna richiesta alla porta UDP 53 del server che offre il servizio DNS.

Se un client desidera richiedere uno di questi servizi offerti da questo server è necessario che specifichi non solo l’indirizzo dell’host ma anche il servizio desiderato.
Fine
-

L'dentificazione di un socket viene definito **meccanismo dei socket**.
**La comunicazione avviene dunque tramite il socket del mittente ed il socket del destinatario.**

Un socket permette perciò di comunicare attraverso la rete usando la pila TCP/IP ed è perciò parte del protocollo.

#### Applicazione di rete

L'applicazione di rete può essere vista come composta da due parti:

- Una **User Agent** che funge da interfaccia tra utente e gli aspetti comunicativi dell'applicazione
- L'**Implementazione dei protocolli**, che permettono all'app di integrarsi con la rete.

In un browser web, la **User Agent è l'interfaccia utente che serve a visualizzare i documenti ricevuti, a permettere la navigazione e richiedere nuovi documenti specificando il loro URL.**
L'**implementazione dei protocolli** avviene tramite il motore di ricerca che si **preoccupa di inviare le richieste ai vari server e di ricevere le risposta.**

Esiste una struttura chiamata **association**, che permette di identificare ogni connessione in modo univoco e contiene:

			**Protocollo, Socket Locale, Socket Remoto**
			
Un esempio di association è: **TCP, 192.168.1.2,1500, 192.168.1.14, 21**.

#### Processi client-server e i socket

Il modello client-server è organizzato in 2 moduli.
Il client **deve conoscere l'indirizzo IP e il port number usati dal Server per potersi collegare al socket di destinazione.**
**Allo stesso server arrivano piu richieste da client diversi** che potrebbero utilizzare anche la stessa prota infatti la **comunicazione avviene tramite socket.**

### La connessione tramite Socket e vari tipi

Ogni sistema Operativo mette a disposizione nelle API i meccanismi per realizzare l'interfacciamento tra diversi protocolli.
Le **Socket API** sono delle API di protocollo che hanno origine in UNIX e sono disponibili oggi in windows, Solaris e Linux.
Le principali funzioni in java e in c sono:

- **Socket()**: Crea un nuovo socket;
- **close()**: termina l'utilizzo di un socket;
- **bind()**: collega un indirizzo di rete a un socket;
- **listen()**: aspetta messaggi in ingresso;
- **accept()**: comincia ad utilizzare una connessione in ingresso;
- **connect()**: crea una connessione con un host remoto;
- **send/write()**: trasmette dati su una connessione attiva;
- **recv/read()**: riceve dati da una connessione attiva;

#### Famiglie di Socket

Esistono varie **famiglie di Socket**, chiamate anche domini dove ognuna di queste riunisce i socket che utilizzano glis tessi protocolli.
Ogni famiglia supporta un sottoinsieme di stili di comunicazione e ha un proprio formato di indirizzamento (**Address family**).
Tra queste:

- **Internet Socket**(AF_INET) -> IP + Porta
    Permette il trasferimento di dati tra i processi posti su macchine remote connesse tramite una LAN o Internet.
- **Unix Domain Socket**(AF_UNIX) -> pathname valido nel file system della macchina
    Permette il trasferimento di dati tra i processi sulla stessa macchina UNIX

#### Tipi di Socket

I socket sono fondamentalmente di 3 tipi, ognuno con una diversa modalità di connessione:

- **Stream socket;**
- **Datagram Socket;**
- **Raw Socket;**

I primi 2 sono utilizzati a livello applicativo, mentre i Raw Socket sono utiilizzati nello sviluppo di protocolli.

##### Stream Socket

Con gli **Stream Socket** si realizza una connessione sequenziale tipicamente asimmetrica, affidabile e full-duplex basata su stream di byte di lunghezza variabile.
Ogni processo crea il proprio endpoint - Socket() e successivamente:

- Il **server** si mette in ascolto quando gli arriva una richiesta la esaudisce tramite l'accept() che **crea un nuovo socket dedicato alla connessione.**
  Crea perciò un **canale virtuale** tra il client e il nuovo socket, in **modo da lasciare libero il primo libero per le ulteriori richieste da parte dei client**.
- Il **client** si pone in coda su socket e quando viene accettato dal **server** crea il binding con la porta locale.

Tra i processi **server** e **client**, quello **server è quello che ha maggiore controllo** poichè crea inizialmente il socket.
Piu **client** possono comunicare attraverso lo stesso socket ma solo un server puo essere assciato ad un socket.
Il server acquisisce le informazioni del client solo dopo che si è stabilita la connessione.

**Il protocollo TCP è basato su questo tipo di Socket.**
In un server TCP ci sono 2 tipi di Socket:

- **Connection Socket**
    Accetta le connessioni ed è condiviso                                          porta
    Per crearlo in Java si utilizza la seguente sintassi: ServerSocket(int port)
- **Data Socket** 
    Per le operazioni send() e receive().                                      Indirizzo,                 porta
    Per crearlo in Java si utilizza la seguente sintassi: Socket(InetAddressaddress, int port)



##### Datagram Socket

Con i **Datagram Socket** viene creata la comunicazione che permette di scambiare dati senza connessione mediante il trasferimento di datagrammi che inoltrano **messaggi di dimensione variabile, senza garantire ordine o arrivo dei pacchetti, quindi si ha una comunicazione inaffidabile**.
Permettono perciò di inviare da un Socket a piu destinazioni e di ricevere da piu sorgenti.
In genere sono supportate nel dominio Internet dal **Protocollo UDP**.

Ogni processo crea il proprio **endpoint** ->Socket e poi:

- I**l server si mette in attesa di ricevere i dati e alla loro ricezione puo invaire una risposta**
- Il **client invia il pacchetto di dati al server e puo mettersi in attesa di una risposta con le stesse primitive che ha utilizzato il server.**

Al termine il Socket viene **chiuso**.

Il vantaggio di questi Socket è che sono in grado di **trasferire i dati velocemente e non esistono differenze tra le chiamate effettuate dai vari processi.**
**Decade perciò il concetto di Client-Server**, entrambi infatti utilizzano le stesse primitive (Funzioni) solo il loro **ordine stabilisce nell'app quale processo ha funzione di server e quale di client.**


##### Trasmissione Unicast e Multicast

L'**Unicast** è la situazione in cui un mittente invia e un destinatario riceve con eventualmente l'inversione dei ruoli, relazione **one-to-one**.

Il **Multicast** è utilizzato per trasmettere informazioni a piu host contemporaneamente, relazione **one-to-many**.

Il **TCP** è orientato alla connessione ed è sempre **Unicast**.
L'**UDP** è senza connessione, viene utilizzato a livello di trasporto ed utilizza spesso il **Multicast**.

Nella comunicazione di tipo **Multicast** un insieme di processi crea un **Gruppo multicast** ed un messaggio spedito da un processo a quel gruppo arriva a tutti i partecipanti.
Esempi di applicazioni multicast sono:

- **DNS**(Domain Name System): aggiornamenti delle tabelle di naming inviati a gruppi di DNS.
- **Videoconferenza**: Ogni host genera un segnale audio video che viene ricevuto da coloro presenti nella chiamata.
- **Altre applicazioni**: Come per esempio quelle di messaggistica

Per implementare un sistema multicast è necessario:

- Poter definire uno schema di indirizzamento dei gruppi
- Un supporto che registri la corrispondenza tra un gruppo e i partecipanti
- La possibilità di ottimizzare l'uso della rete nel caso di invio di pacchetti a un gruppo.

Il **protocollo piu utilizzato per il multicast** in internet è l'**IGMP** (Internet Group Management Prot.)
che garantisce la trasmissione, tra host e multicast router, dei messaggi relativi alla creazione dei gruppi.

Le API multicast devono contenere primitive per:

- **Unirsi** a un gruppo di multicast: identificare e indiririzzare univocamente un gruppo
- **Lasciare** un gruppo di multicast
- **Spedire** messaggi a un gruppo, cioè a tutti i processi che fanno parte del gruppo.
- **Ricevere** messaggi indirizzati ad un gruppo del quale l'host fa parte.

**La gestione dei gruppi è di tipo dinamico, infatti un host puo esser parte di piu gruppi allo stesso tempo, puo inviare messaggi anche se non fa parte di quel gruppo e i membri del gruppo possono essere sia nella stessa rete che in due reti fisiche differenti.**

Come indirizzo di multicast si utilizza un indirizzo IP di **classe D**. 224.0.0.0 - 239.255.255.255

Gli indirizzi possono essere:
- **Permanenti**: L'indirizzo viene assegnato dalla **IANA** e rimane assegnato anche se non ci sono piu partecipanti connessi - questi indirizzi sono detti well-known.
- **Temporanei**: Richiedono la definizione di un protocollo per evitare conflitti nell'attribuzione degli indirizzi ai gruppi ed esistono fino al momento in cui esiste almeno un partecipante.

Il **broadcast** può essere considerato un caso estremo di multicast in cui:
- La comunicazione avviene da uno a tutti.
- Per la sua realizzazione viene normalmente usato un indirizzo speciale per identificare tutte le possibili destinazioni.
