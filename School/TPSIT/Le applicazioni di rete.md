
#### Protocollo di comunicazione

Un **protocollo di comunicazione** è inteso come l'insieme delle regole di un **sistema di comunicazione che consente lo scambio di informazioni tra due o piu entità.**

La comunicazione fra due entità  può essere scomposta e rappresentata attraverso strati o livelli.
**Si suddivide la complessità della comunicazione in funzionalità piu semplicie e si assegnano queste funzioni a strati diversi.**

#### Il modello ISO/OSI

È composto da 7 livelli:

7. **Applicazione** : browser, FTP, ecc..
6. **Presentazione**: criptaggio e decriptaggio dei messaggi e comprensione o decompressione dei dati;
5. **Sessione**: Una volta instaurata la connessione, i due dispositivi si accertano attraverso dei messaggi handshake che l'altro dispositivo sia in ascolto
4. **Trasporto**: Ha il compito di garantire l'efficienza del trasferimento dati (corretta ricezione pack)
3. **Rete**: Gestisce gli indirizzi del mittente e del destinatario
2. **Collegamento (link)**: Gestisce l'indirizzo fisico MAC che identifica univocamente la scheda di rete di ogni dispositivo
1. **Fisico**: Stabilisce come devono essere i segnali elettrici che rappresentano i dati che sono inviati fisicamente in rete.

**Ogni strato esegue una serie di operazioni specifiche, scambiando dati esclusivamente con gli strati adiacenti.**

Il **livello di applicazione si occupa di implementare le applicazioni di rete che vengono usate dall'utente.**
Il programmatore non si deve preoccupare dei livelli inferiori ma solo di utilizzare le primitive messe a disposizione dai diversi protocolli degli altri strati.
**Il principale scopo delle reti è condividere dati mediante applicazioni.**

#### Differenze tra TCP e UDP

##### TCP 

**Il protocollo TCP ha il compito di trasmettere in modo affidabile i dati tra due nodi della rete.**

Quando si carica una pagina web, **il computer invia pacchetti TCP all'indirizzo del server web** chiedendo di vedere la pagina.
**Il web risponde inviando un flusso di pacchetti TCP**, che il browser web mette insieme per formare la pagina web e mostrarla sullo schermo.

Il protocollo TCP garantisce che il destinatario riceva i pacchetti.

##### UDP

È un altro protocollo del transport layer che si occupa della trasmissione dei dati.
Questo protocollo è connectionless, **non viene creata nessuna sessione di comunicazione**.
UDP si **limita ad inviare pacchetti sulla rete senza richiesta della conferma di ricezione.**

I pacchetti vengono inviati velocemente, senza attendere e continuando ad inviare.
**Se il destinatario perdesse dei pacchetti, il destinatario non avrebbe nessun modo di chiederli di nuovo.**
**Viene utilizzato quando la velocità di rete è elevata e può essere superfluo il controllo degli errori, è spesso utile per i video in diretta streaming e per i giochi online.**

#### Protocolli del livello di applicazione

**Il livello di applicazione è lo strato che mette a disposizione i protocollo che permettono alle applicazioni di comunicare con host remoti.**
Principali protocolli sono:

- **HTTP**
- **DNS**
- **FTP**
- **SMTP**
- **POP3** Post Office Protocol 
  
 Questi protocolli vengono utilizzati da tutte le applicazioni di rete generali, come la **posta elettronica, il web**, la **condivisione di file p2p**, la **messaggistica istantanea, lo streaming di video memorizzati**.
 Oltre alle applicazioni generali offerte al pubblico di internet, esistono quelle **private**; come per esempio il **collegamento tra filiali remote di una società commerciale.**

#### Applicazione di Rete

**Un'applicazione di rete (o applicazione distribuita) è costituita da un insieme di programmi che vengono eseguiti su due o piu computer contemporaneamente.**
I programmi operano interagendo tra di loro utilizzando risorse comuni, accedendo in maniera concorrente agli archivi, mediante la rete che li connette.

I processi **hanno la necessità messaggiare con altri processi della stessa applicazione: per comunicare tra loro questi processi devono utilizzare i loro indirizzi e i servizi offerti dal livello di applicazione.**

Altre informazioni sono in I socket->I socket e i protocolli per la comunicazione di rete

#### Scelta dell'architettura per l'applicazione di rete

Le principali architetture utilizzate sono:

- **Client-server**
- **peer-to-peer**
- **architetture ibride** (P2P e client-server)

##### Architettura Client-server

In queste architetture deve esserci un **server attivo** che offre un servizio, **restando in attesa che qualche client si connetta per poter rispondere alle richieste.**
Deve perciò **possedere un indirizzo IP fisso** statico, mentre i client avranno generalmente indirizzo dinamico.

Un **client non è in grado di comunicare con altri client**, ma solo con il **server**.
Se un server viene consultato contemporaneamente da molti client potrebbe non riuscire a risolvere le richieste ed **entrare in stato di congestione**: è necessario virtualizzare la risorsa realizzando una **server farm.**
La **server farm è una serie di server con un unico hostname ma con più indirizzi IP, trasparenti al client, sui quali vengono dirottate le richieste di connessione.**
##### Architettura P2P

In queste architetture ci sono **coppie di host chiamati peer che dialogano tra di loro.**
Queste entità sono **autonome, capaci di organizzarsi e condividono un insieme di risorse distribuite presenti all'interno di una rete**. Il sistema utilizza quelle risorse per fornire una funzionalità in modo decentralizzato.

Nei **sistemi P2P gli host sono una comunità che collabora con il binomio dare e ricevere.**
Ogni **peer mette a disposizione una risorsa e ne ottiene in cambio altre.** (Emule e Gnutella)

Un **peer può anche decidere di offrire gratuitamente risorse**, magari per iniziative benefiche o di solidarietà o per ricerca scientifica o sanitaria, per esempio donazioni o la ricerca sul cancro.
##### Architetture Ibride

###### P2P Decentralizzato
Nell'**architettura completamente decentralizzata un peer ha sia funzionalità di client che di server ed è impossibile localizzare una risorsa con un indirizzo IP statico.**
Vengono eseguiti nuovi meccanismi di indirizzamento, definiti a livelli superiori dell'IP.

Il sistema P2P è **capace di adattarsi a un continuo cambiamento dei nodi partecipanti** mantenendo connettività e prestazioni accettabili senza richiedere l'intervento di entità centralizzate.
###### P2P Centralizzato
Il P2P centralizzato è un **compromesso tra il determinismo del modello client-server e la scalabilità del P2P.**

Ha un **server centrale (directory server)** che conserva informazioni sui peer e **risponde alle richieste effettuando la ricerca in modalità centralizzata.**
I **peer** sono responsabili di:

- Conservare i dati e le informazioni
- Informare il **server** del contenuto del file che intendono condividere
- Permettere ai **peer** che lo richiedono di scaricare le risorse condivise

L'esempio piu famoso è **napster**, gli utenti si collegano ad un server centrale nel quale pubblicano i nomi delle risorse che condividono.
###### P2P Ibrido

Questo tipo di architettura è **parzialmente decentralizzata** dove **sono presenti alcuni peer determinati dinamicamente** che hanno anche la funzione di indicizzazione.
Gli altri nodi sono chiamati **leaf peer.**
#### Servizi offerti dallo strato di trasporto alle applicazioni

Tutti i protocolli hanno in comune il **trasferire messaggi da un punto ad un altro.**
Ogni applicazione **deve scegliere tra i protocolli di trasporto quale deve adottare per realizzare un protocollo applicativo** in base ai servizi che necessità e alle esigenze che possono essere:

- Trasferimento dati affidabile -> Servizio che **garantisce la consegna completa e corretta.**
- Ampiezza di banda
- Temporizzazione
- Sicurezza

##### Trasferimento dati affidabile
Servizio che **garantisce la consegna completa e corretta.**
Come detto prima ci sono due protocolli, TCP e UDP.
Il primo stabilisce una connessione, è perciò **affidabile**. Effettua il **controllo di flusso** in quanto se il ricevente è piu lento del mittente esso rallenterà, esegue anche il **controllo della congestione** limitando il mittente se la rete è sovraccarica, **ma non da garanzie di banda minima.**
Il secondo invece non solo non da **banda minima, ma non ha neanche nessun tipo di controllo,** per questo è più veloce.

##### Ampiezza di Banda

Ci sono applicazioni che **necessitano una garanzia sulla larghezza di banda minima dispoibile,** richiedono un troughput garantito, come la trasmissione di un evento in web-tv.
Altre invece **utilizzano in modo elastico la bandwidth che è disponibile, come la posta elettronica e i sistemi FTP.**

Internet ha una natura eterogenea, **i protocolli di trasporto non sono in grado di garantire la presenza di una certa quantità di banda per tutta la durata di trasmissione di un messaggio.**

##### Temporizzazione

Alcune applicazioni, come la **telefonia VoIP gli ambienti virtuali ammettono solo piccoli ritardi per essere efficaci.**

Lo strato di **trasporto non è in grado di garantire i tempi di risposta** perchè le temporizzazioni presenti assicurano un certo ritardo end-to-end tra le applicazioni.
**Il protocollo TCP garantisce la consegna del pacchetto ma non il tempo impiegato e neppure il protocollo UDP.**

La soluzione è quella di utilizzare un **protocollo di trasporto in tempo reale**, come **RTP** (Real Time Protocol), che **è in grado di studiare i ritardi di rete e calibrare gli apparati e i collegamenti per garantire di restare nei limiti prefissati.*, scegliendo quando utilizzare UDP o TCP.

##### Sicurezza

Un' applicazione può richiedere la **cifratura di tutti i dati trasmessi** in modo che non si perdi la riservatezza in caso di intercettazioni.
Possono essere richiesti **servizi di sicurezza** per **garantire l'integrità dei dati e l'autenticazione end-to-end.**

Il problema della sicurezza nelle reti è molto importante, poiche **le reti di natura sono insicure.**
Garantire la sicurezza di un sistema informativo significa **impedire a soggetti attaccanti l'accesso** o **l'uso non autorizzato di informazioni o risorse.**

