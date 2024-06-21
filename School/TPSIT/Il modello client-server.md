### Introduzione al modello client server

Il **modello client-server** è costituio da un **insieme di host che gestiscono una o piu risorse**, i server, e da un **insieme di client che richiedono l'accesso ad alcune risorse** distribuite gestite dai server.
**Ogni processo server puo diventare client.**

**Non sono gli host ad essere client, ma i processi che sono in esecuzione su di essi, un programma**.
Visto che ci possono essere piu processi su un host, egli puo essere sia client che server.

#### Evoluzione del modello

Il modello client-server **permmette di gestire applicazioni molto complesse** che hanno:

- Molti utenti concorrenti che richiedono servizi
- Una logica applicativa complessa
- Archivi di grande dimensioni con organizzazione di dati complessa e distribuita
- Notevoli requisiti di sicurezza
- Sistemi transazionali

#### Alcuni servizi tipici client-server

- **Telnet**
  Mediante un tale programma client è possibile operare su un computer remoto come se fosse in locale, questo è possibile se sulla macchina remota è presente un programma server in grado di esaurire richieste del client Telnet
- **HTTP**
  Il browser è un client HTTP, che richiede pagine web ai computer su cui è installato un web server, il quale esaudisce le richieste spedendo le pagine desiderate.
- **FTP**
  tramite un client FTP è possibile copiare e cancellare file su un computer remoto, purchè sia presente in quella macchina un server FTP.
- **SMTP**
#### Unicast e multicast

- **Unicast**, il **server** comunica con un **solo client** alla volta accettando una richiesta di connessione solo se nessun altro client è gia connesso.

- **Multicast**, al **server** possono essere connessi **piu client** contemporaneamente.
  In questo tipo di connessione, se la richiesta di connessione va a buon fine, **prima di stabilire la connessione sposta la richiesta** dalla porta in cui è stata effettuata (**Port address**) **su una nuova porta** in modo da lasciare la prima porta in attesa di altre connessioni, e manda in esecuzione un thread che risolva la richiesta.
  Un esempio è la **comunicazione tra browser e web server,** infatti quest'ultimo deve garantire gli stessi servizi a piu utenti e deve sempre restare in ascolto sulla porta 80 in attesa di nuove connessioni.
### Livelli e strati

Le **architetture client-server**, sono organizzate in **livelli (tier)** dove ogni livello corrisponde a un gruppo di nodi di calcolo su cui è distribuito il sistema.
Ogni livello funziona da **server** per i suoi **client** nel livello precedente e da **client** per il livello successivo ed **è organizzato in base al servizio che fornisce.**

Spesso il modello client-server a livelli è combinato con quello a strati dove ogni strato viene definito dal punto di vista funzionale come un "livello di astrazione".
**Un sistema adotta un'architettura a livelli e il software in ciascun livelo è spesso organizzato internamente a strati.**

#### Funzionalità

In genere nelle applicazioni WEB ci sono 3 tipi di funzionalità:

- **Front-end**, l'interfaccia verso l'utente
- **logica applicativa**
- **Back-end**, accesso alle risorse e ai dati

In generale, la suddivisione in strati avviene in questi 3 livelli:

- **Presentation Layer**: composto dalle procedure o moduli dedicati all'acquisizione e alla presentazione dei dati all'utente.

- **Business Logic Layer** : è il corpo centrale dell'applicazione, comprende la lofica dell'elaborazione e la definizione delle relazioni esisteni tra diverse entità

- **Resource Management Layer**: composto dalle procedure che gestiscono i dati, memorizzano e recuperano le informazioni degli archivi di massa dei database

Nei sistemi WEB, il **Presentation Layer** è costituito dai moduli del web server che creano i documenti HTML, come le java servlet, gli script PHP mentre il client può essere identificato con il browser.
Il **Business Logic Layer** comprende l'algoritmo che implementa le operazioni legate ad un prelievo su un conto corrente bancario o la sequenza di azioni da compiere per fare un acquisto online.
Se il **Resource Management Layer** è implementato tramite un DBMS si chiama **Data Access Layer.**
#### Architettura ad un livello

Un solo mainframe al quale erano collegati terminali stupidi.
Tutta l'elaborazione era effettuata dall'elaborazione centrale e i terminali servivano solo per le fasi di I/O.

Questa architettura non rientra nella tipologia client-server ed è la situazione prima dei sistemi distribuiti.

#### Architettura a due livelli

Architetture client-server, le funzionalità e responsabilità erano divise in due livelli:

- Livello server
- Livello client

Ci sono due sottocategorie di architetture a due livelli che sono:

- **Modello thin-client** -> il server svolge la logica applicativa e gestisce i dati e il client si occupa dell'esecuzione dei software di presentazione
- **Modello thick-client** -> il server gestisce i dati e il client si occupa sia della presentazione che della logica applicativa

Il limite delle architetture a due livelli è che sono **poco scalabili** dato che **il server deve gestire la connessione e lo stato della sessione di ciascun client.**
**Questo carico porta alla limitazione del numero limitato di client che possono essere gestiti contmporaneamente.**

#### Architettura a tre livelli

L'architettura client-server è a tre livelli, ad ogni livello corrisponde uno strato architetturale:

- **front-end o presentation layer**, interfaccia verso l'utente
- **logica applicativa o middle tier**
- **back-end** con accesso a risorse e dati

I vantaggi in termini di prestazioni sono notevoli, si favorisce la distribuzione della quantità de elaborazione a discapito dei tempi di comunicazione.
**Il sistema è facilmente scalabile**, all'aumentare delle richieste di un servizio **è possibile aggiungere qualche server in grado di compensare il carico di lavoro** ed è inoltre **più tollerante ai guasti.**
Ha dei vantaggi anche per la **sicurezza**, **rende possibile l'introduzione di sicurezza a livello di servizio e quindi più facilmente gestibile.**

I principali svantaggi sono la difficoltà di:

- **Progettazione**
- **Sviluppo**
- **Amministrazione**

#### Architettura a N livelli

Queste architetture sono una **generalizzazione del modello client-server a tre livelli** dove vengono scomposti e introdotti un numero qualunque di **livelli server intermedi.**
Questa scomposizione viene fatta per suddividere i compiti dei vari strati e prende il nome di **applicazione multi-tier**.
### Applicazioni web

Un **applicazione web** è un software sviluppato ed utilizzato con tecnologie web e linguaggi specifici.
Alla base di queste applicazioni ci sono:

- Tecnologie client-side e server-side
- linguaggi di mark-up e linguaggi di programmazione

Si possono distinguere le **tecnologie del web** in **2 gruppi, in base a dove avvengono le elaborazioni:**

- **Tecnologie client-side**: l'elaborazione avviene sul **client**, tipicamente nel browser
- **Tecnologie server-side**: l'elaborazione avviene sul **server**. tipicamente nel web server

##### Client-side

Per visualizzare una pagina che utilizza una tecnologia client-side **non è necessario utilizzare un web server, si può memorizzare e aprire la pagina web fornendo al browser il path sul file system** **locale**.
**Le parti di codice sorgente saranno visibili dal browser.**

##### Server-side

Per visualizzare una pagina che utilizza una tecnologia server-side **è necessario un web server che elabori il codice della pagina,** ed è opportuno connettersi e richiedere la pagina tramite un URL.
**Le parti di codice sorgente non sono visibili dal browser, poichè il server ha elaborato il codice e noi vediamo solo il risultato.**

##### Linguaggi del web

- **Linguaggi di mark-up** -> servono a scrivere docummenti strutturati, dove si trova in genere un contenuto testuale corredato di indicazioni (tag) che ne definiscono la struttura. come HTML e XML.
- **Linguaggi di programmazione** -> servono a scrivere programmi: una sequenza di istruzioni , Java e PHP.

Le distinzioni non sono piu cosi rigide, esistono approcci ibridi come **AJAX** ma **non sono una via di mezzo tra le tecnologie client e server side.**
In **HTML5** è possibile utilizzare **tag**(Mark-up) per scrivere **istruzioni**(programmi) rendendo piu difficile la differenza tra i due linguaggi.

