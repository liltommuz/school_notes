#### Introduzione ai sistemi distribuiti

Un **Sistema** è un insieme di elementi che **interagiscono tra di loro per funzionare come un elemento unico**.
Ne esistono diversi:

- **Sistema Informativo**
	Il quale è costituito dalle informazioni utilizzate, prodotte e trasformate durante l'esecuzione dei processi, dalle modalità in cui sono gestite e dalle **risorse sia umane sia tecnologiche coinvolte.**
- **Sistema informatico**
	Costituisce la **parte automatizzata ( Le risorse tecnologiche) del sistema informativo**, le **informazioni vengono raccolte e trattate digitalmente**.
	
Una **rete di elaborazione** è ottenuta connettendo diversi computer per realizzare **sistemi di calcolo piu potenti.**

Le architetture principali dei sistemi informativi sono centralizzate e distribuite, quest'ultime hanno sosituito le prime per varie esigenze:

- Nei **sistemi centralizzati** le applicazioni girano in **un solo processore o solo un host**, che costituisce **l'unico componente autonomo del sistema che è condiviso da vari host e tutte le risorse del nodo centrale sono sempre accessibili.**

- Nei **sistemi distribuiti** le applicazioni **sono costituite da più processi, cooperanti, eseguiti in parallelo su un insieme di unità di elaborazione autonome.**

Quindi la principale differenza è che **un sistema informatico è centralizzato se dati e applicazioni stanno in un unico nodo elaborativo o componente autonomo**, mentre è distrubuito se almeno una di queste condizioni è verificata:

- **Elaborazione distribuita**
	Le applicazioni sono in piu host che collaborano.
- **Base di dati distribuita**
    Il database sta in piu host.

Nei sistemi distibuiti l'insieme di diversi host appaiono all'utente come un singolo host, inoltre questi host comunicano e coordinano le azioni solo tramite lo scambio di messaggi.
In questi sistemi il fallimento di un nodo può rendere inutilizzabile un altro nodo.

Le applicazioni possono assumere un ruolo diverso:

- **Client**
	Quando utilizza i servizi messi a disposizione da altre applicazioni.
- **Server**
    Quando fornisce i servizi ad altre applicazioni.
- **Actor**
	Quando in diverse situazioni utilizza o fornisce servizi, sia server che client.

#### Classificazione, vantaggi e svantaggi

I **sistemi distribuiti sono un'insieme di computer indipendenti** mentre **i sistemi paralleli sono un'insieme di elementi di elaborazione**, entrambi puntano alla risoluzione di problemi ma i secondi hanno una potenza di calcolo maggiore.
I primi si possono classificare in tre famiglie:

1. **Sistemi di calcolo distribuiti** (previsioni metereologiche, costruzione automobile)
2. **Sistemi informativi distribuiti** (Internet)
3. **Sistemi distribuiti pervasivi** (TV,videosorveglianza, impianti antifurto, controllo del traffico)

1. I **sistemi di calcolo distribuito** sono configurati per svolgere calcoli complessi e si suddividono in:

	- **Cluster computing**
		Questi sono realizzati dalla **connessione di computer omogenei** allo scopo di parallelizzare l'operazione.
	- **Grid computing**
	    Questi **possono essere realizzati dalla connessione di computer eterogenei** per cooperare l'operazione di calcolo.
    
2. I sistemi informativi distribuiti possono essere:
	- **il web** che è il piu grande
	- **Le tecnologie mobile che integrano sistemi legacy** con nuove tecnologie di comunicazione, questi sono i piu moderni sistemi informativi distribuiti
	
	 I **sistemi legacy** sono sistemi solitamente presenti in azienda **basati su mainframe ai quali si collegano dei terminali con interfaccia a caratteri.**
	 Questi sono **sistemi obsoleti** che nelle aziende pero hanno dimensioni notevoli e spesso rivestono ruoli critici.
	 
**Tutti i sistemi informatici sono distribuiti** e presentano vantaggi e svantaggi:

- Vantaggi
	- **Affidabilità** 
	- **Integrazione**
	- **Trasparenza**
	- **Economicità** -> miglior rapporto qualità/prezzo rispetto ai centralizzati
	- **Apertura** -> interoperabilità, portabilità e ampliabilità
	- **Prestazioni e scalabilità** -> Scalabilità orizzontale (Si aggiungono entità Hard o Soft -ware)
	- **Tolleranza ai guasti** -> Ritardo nel tempo di risposta senza blocco, si utilizza un sistema software di recupero che sistema il guasto.

- Svantaggi
	- **Produzione di software** -> Cambio da centralizzato a distribuito. Socket e Java.
	- **Complessità** ->Sono piu complessi dei centralizzati
	- **Sicurezza**
	- **Comunicazione**

VANTAGGI
- Affidabilità grazie alla **ridondanza**, ma si utilizzano anche algoritmi per **sostituire automaticamente l'unità guasta con una funzionante** per continuare l'elaborazione.
  Possono essere divisi anche in base all'utilizzo delle risorse informative ed elaborative:

	- **Accoppiamento debole**
	    Sono soggetti autonomi che cooperano per prestazioni migliori, le modifiche ad un componente non influenzano l'altro, come per esempio i computer client-server
	- **Accoppiamento forte**
	    Utilizzano risorse controllate da una o più unità organizzative che  fanno riferimento ad un'unica autorità, come per esempio gli sportelli pubblici delle banche.

- **L'integrazione è la capacità di un computer di integrare componenti spesso eterogenei tra di loro.** Ogni componente deve **interfacciarsi allo stesso modo con il sottosistema distribuito**, per fare ciò sono stati definiti dei linguaggi come **XML** (extendible Markup Language) e notazioni **JSON** (JavaScript Object Notation) che **favoriscono lo scambio di informazioni nel web e permettono un'agevole ed efficiente pubblicazione di dati coomplessi**.

- Con **trasparenza si intende il concetto di vedere il sistema distribuito come un unico sistema di elaborazione**, l'utente non deve accorgersi, deve avere la percezione di utilizzare un unico host.
  Esistono **8 forme di trasparenza**:
	- **accesso** ->accedere a risorse locali e remeto con le stesse operazioni in modo uniforme
	- **locazione** ->permettere di accedere ad una risorsa senza sapere dove si trova
	- **concorrenza** -> i processi operano in maniera concorrente, pero la risorsa resta disponib
	- **replicazione** -> operazioni di duplicazione delle risorse tenendo stessi nomi. +affidabilità.
	- **guasti** -> viene mascherato il guasto e il recovery di una risorsa
	- **migrazione** -> lo spostamento di una risorsa non interferisce sull'accesso ad essa
	- **prestazioni** -> le operazioni per migliorare le prestazioni del sistema rispetto al carico
	- **scalabilità** -> il sistema viene espanso senza interrompere o modificare il funzionamento

SVANTAGGI
- La **sicurezza** puo essere un problema in quanto **tutti gli host sono collegati tra di loro e quindi anche chi non ha il diritto puo accedere a dati e risorse.**
  Nei vecchi sistemi **bastava solo proteggere il sistema d'accesso fisico**, oggli l'accesso avviene via etere e quindi **aumenta il rischio di intercettazioni anche nelle comunicazioni, percio è necessario aumentare la tutela dei dati**.

- Il **trasferimento di dati a distanza richiede lo sviluppo di nuovi sistemi di telecomunicazioni, sia cablati che wireless, inoltre l'aumento degli utenti fa si che aumenti la richiesta di bande trasmissive** anche per migliorare la qualità del servizio.
  A volte l'**utilizzo di tecnologie sperimentali porta all'aumento della complessità** anche perchè l'analisi e la progettazione sono basate su vecchi metodi di sviluppo a monoprocesso, non adeguati ai sistemi distribuiti.

#### Evoluzione dei sistemi distribuiti

I sistemi distribuiti essendo legati ai computer hanno subito una **crescita notevole negli ultimi anni,** seguendo la **legge di moore le potenza raddoppiava ogni 2 anni,** ma ora non è piu cosi.

**Il problema principale è legato alla miniaturizzazione dei microprocessori e alla crescita della frequenza di lavoro**.
Ci sono anche dei limiti fisici, vicino i 2-3 nanometri non si riesce ad andare.
Inoltre non è neanche possibile superare la velocità della luce.

Se si vogliono avere frequenze di lavoro in GHz **non si puo superare la distanza di 20 cm di trasmissione** altrimenti si genererebbe un **ritardo** e se si **restringono i circuiti** avremmo **problemi di instabilità e di surriscaldamento** in quanto il calore non riesce a dissiparsi in cosi poco spazio.

L'Unica soluzione è perciò di andare verso architetture di elaborazione diverse sia dal punto di vista costruttivo (**Hardware**) sia logico (**Software**).

#### Classificazione di Flynn Hardware e SISD-MIMD

Dal punto di vista **Hardware** sono state realizzate **macchine e sistemi dotati di piu di una CPU** in modo da avere piu potenza di calcolo senza esasperare i limiti di velocità.
**Macchine parallele o macchine ad architetture parallela.**
Esistono diversi modi per classificare le architetture Hardware a seconda dei fattori di riferimento.
Una delle piu utili è quella di **Flynn** è basata su due flussi di informazioni che stanno nei calcolatori:

- **Flusso delle istruzioni**
- **Flusso dei dati**

A seconda di come si combinano i 2 flussi ci sono **4** possibilità:

- **Macchine SISD** (Single Instruction Single Data): flusso di istruzioni unico e flusso di dati unico.
- **Macchine SIMD** (Single Instruction Multiple Data): flusso di istruzi unico e flusso dati multiplo.
- **Macchine MISD** (Multiple Instruction Single Data): flusso di istruzi multiplo e flusso dati unico.
- **Macchine MIMD** (Multiple Instruction Multiple Data): flusso di istruzi multiplo e flusso di dati multiplo.

##### SISD

**Gli elaboratori vecchi, come la macchina di Von Neumann erano SISD.**
Tutte le macchine che hanno una **singola CPU**, come i personal computer, le workstation e i mainframe fanno parte di questa categoria.
Nelle macchine a singola CPU il **flusso di istruzioni è unico**, e quindi viene **eseguito un solo programma alla volta**: dopo la prima istruzione si passa alla seconda fino al termine del programma. Le istruzioni sono eseguibili in maniera **sequenziale.**

##### SIMD

Nelle macchine **SIMD** l'elaborazione avviene su **più flussi in contemporane ma con un singolo flusso di istruzioni,** generalmente ci sono **piu processori che eseguono la stessa istruzione** su flussi di dati diversi.
**Un elaboratore di questo tipo è adatto per realizzare calcoli vettoriali e matriciali soprattutto in ambito grafico.**

##### MISD

I **MISD** eseguono **più istruzioni sullo stesso flusso di dati.**
Esistono **piu processori,** ognuno con **una propria memoria**, la quale a sua volta ha un proprio flusso di istruzioni che verranno eseguite sullo stesso flusso di dati.
**Questa architettura non ha macchine commercializzate, anche se il modello ricorda le pipeline.**
Una macchina di questo tipo puo essere utile nell'ambito della **crittografia**, dove vengono **richieste elaborazioni simili da eseguirsi sugli stessi dati in parallelo.**

##### MIMD

Questo tipo di architettura comprende tutte le tipologie di elaboratori composti da più unità centrali di elaborazione indipendenti che possono lavorare su stream di dati indipendenti.

A queste macchine viene fatta un ulteriore classificazione in riferimento a come è suddivisa la memoria fisica:

- MIMD a memoria fisica condivisa (multiprocessor)
- MIMD a memoria privata (multicomputer)

È possibile fare un'**altra classificazione** a seconda di **come sono interconnesse le unità di elaborazione**, **se utilizzano un unico mezzo fisico condiviso o attraverso un canale diretto fisico tra coppie di unità centrale.**

###### Multiprocessore

i sistemi **multiprocessori** hanno **memoria condivisa,** la memoria è comune e quindi esiste un **unico spazio di indirizzamento condiviso tra tutti i processori.**
È necessario perciò **sincronizzare e regolare gli accessi in memoria per gestire la competizione alle risorse comuni.**
I processori **non devono per forza avere una singola memoria comune**, possono averne una propria e condividerne parte con altri, in modo da reallizare una **memoria condivisa distribuita.**

###### Multicomputer

Nei **multicomputer** non è presente una memoria condivisa a livello di architettura e quindi la comunicazione avviene tramite lo **scambio di messaggi**.
**Ogni Computer possiede una propria area di memoria privata**, non indirizzabile da parte dei processori remoti.

Le **LAN** di personal computer sono cosi, poichè hanno una memoria privata e sono tra loro interconnessi con mezzo condiviso.


#### Cluster e Grid Computing

Come detto in precedenza,  i **sistemi di calcolo distribuito** sono configurati per svolgere calcoli complessi e si suddividono in:

- **Cluster computing**
	Questi sono realizzati dalla **connessione di computer omogenei** allo scopo di parallelizzare l'operazione.
- **Grid computing**
	Questi **possono essere realizzati dalla connessione di computer eterogenei** per cooperare l'operazione di calcolo.
###### Cluster computing
 Con **cluster computing,** si intende **un sistema distribuito costituito da un insieme di nodi ad alte prestazioni interconnessi tramite una rete locale ad alta velocità:**
 
- Devono essere **omogenei**, i nodi hanno stesso sistema operativo
- Devono avere **Hardware molto simile**
- **Sono connessi attraverso la stessa rete**

Un cluster PC ha potenza di calcolo uguale alla somma di quelle dei singoli computer che lo costituiscono, **differisce da una rete di PC** da:

- **Potenza di elaborazione ad alte prestazioni** (High Performance Computer)
- **Velocità di trasferimento dei dati** (oltre 1 Gbit/s)
- **Centralizzazione fisica delle macchine**, tutti i PC sono sullo stesso Rack
- **Presenza di un'applicazione di Management**, che sta su un singolo PC e permette di lanciare processi su altri PC, monitorare il loro comportamento , ecc...

Ci sono 2 possibili architetture:

- **Organizzazione Gerarchica** con **singolo nodo principale** dove spesso sono usate librerie di message passing per il calcolo parallelo
- **Organizzazione Single System Image** per esempio MOSIX che effettua un bilanciamento automatico del carico effettuando se serve una migrazione di processi

Un sistema Cluster PC appartiene alle macchina **MIMD a memoria privata , multicomputer.**
**Il vantaggio dei Cluster PC è quello di affrontare calcoli particolarmente onerosi che sarebbero molto lunghi con un solo computer.**

###### Grid computing
 Con **Grid Computing** si intende **un sistema distribuito di calcolo decentralizzato composto da un gran numero di nodi disposti a griglia e caratterizzati da un grado elevato di eterogeneità** sia per hardwware per il software, politiche di sicurezza, ecc...
Il vero **problema** è la **condivisione coordinata delle risorse all'interno di una dinamica e multi-istituzionale organizzazione virtuale.**
La condivisione **si estende all'accesso diretto a computer, al software, in generale a tutto l'hardware necessarrio alla risoluzione di un problema.**

**Architettura Service-oriented**, dove tutte le risorse computazionali, sono dei servizi.
In questo tipo di architettura (SOA), **i servizi funzionano in modo indipendente e forniscono funzionalità o scambi di dati ai propri utenti**.
L'Utente richiede informazioni e invia i dati di input al servizio, il servizio elabora i dati, esegue l'attività e invia una risposta.


#### Sistemi distribuiti Pervasivi

In questi sistemi distribuiti, i nodi sono piccoli, mobii, con connessione di rete wireless e spesso facenti parte di un sistema piu grande:

- **Sistemi domestici** (TV, smartphone, videosorveglianaza e climatizzazione integrati in un solo sistema)
- **Sistemi elettronici** **per l'assistenza sanitaria** 
- **Reti di sensori** (controllo del traffico, centraline meteo)

Alcuni requisiti per sistemi pervasivi:

- **Cambi di contesto:** il sistema è parte di un ambiente che può cambiare in ogni momento;
- **Composizione ad hoc:** ogni nodo può essere usato in modi diversi da utenti differenti;
- **Richiesta la facilitò di integrazione**
- **Condivisione come Default:** i nodi vanno e vengono, fornendo dati e servizi da condividere;

#### Reti Domestiche

Queste reti sono caratterizzate dall'**assenza di un amministratore di sistema** e solitamente **sono sistemi auto-configurabili e autogestiti** in quanto gli utenti non hanno conoscenze di connettività.

La soluzione più semplice è quella di una **home box** centralizzata alla quale si collegano tutte le periferiche ed eventuali "ospiti".

#### Domotica

La **domotica** si occupa delle **tecnologie capaci di migliorare la qualità di vita** all'interno di una casa. È un sistema che aiuta le persone nella loro vita.

Questa tecnologia, permette di **incrementare le prestazione degli impianti presenti**, ottimizzando i consumi e permettendo varie funzioni come controllo, risparmio energetico, comfort, sicurezza.
Generalmente una rete domestica è senza fili e comunica con tutti i dispositivi compatibili.

#### Wearable computing

Questi sistemi sono principalmente utilizzati per **l'assistenza sanitaria** ed effettuano il monitoraggio di parametri biologici o memorizzando i dati in un computer palmare PDA  o trasmettendo i dati a un sistema di archiviazione remoto.

I principali problemi sono, la memorizzazione dei dati e dunque la prevenzione dalla perdita di dati cruciali, la gestione della sicurezza e la modalità di propagazione di avvisi e allarmi.

I dati raccolti vengono solitamente 
elaborati e memorizzati i una base di dati centralizzata, a volte invece neigli stessi apparecchi realizzando una base di dati distribuita.

#### Architetture distribuitive software

Anche per il **software** l'evoluzione delle architetture distribuite è arrivata, e spesso ha anticipato i cambiamenti delle architetture hardware e dei loro sistemi operativi.
Esistono vari tipi di architetture distribuite software:

- **Architettura a terminali remoti**
- **Architettura client-server**
- **Architettura Web-Centric**
- **Architettura cooperativa**
- **Architettura completamente distribuita**

##### Architettura a terminali remoti

**Tutte le operazioni vengono effettuate da un'unica unità centrale** alla quale sono collegati terminali privi di capacità di elaborazione che all'utente permettono di inviare e ricevere le informazioni all'unità centrale.

In questi sistemi i **terminali sono omogenei** e quindi il software di gestione non fa fatica, **replica per ognuno di essi un area di memoria riservata e facendo evolvere singolarmente i singoli task avviati dalle diverse unità remote.**

##### Architettura client-server

I **client** **hanno una loro capacità di elaborazione**, essi richiedono un servizio a un **server** che è in grado di esaurire la richiesta, elaborarla e inviarla al **client**.
Possono esserci più server con servizi diversi, o piu client che chiedono lo stesso servizio.
**Inoltre un server può anche essere contemporaneamente client.**

**Client e server possono essere tecnologicamente diversi, sia hardware che software; per questo motivo questa architettura è quella più adatta a far comunicare e cooperare unità eterogenee.**

##### Architettura web-centric

A causa delle **piattaforme mobili**, la necessità di un terminale stupido è tornata, i sistemi mobili sono utilizzati come interfaccia grafica verso l'utente.
**Molte applicazioni sono state convertite al web rendendo il web-server il centro distribuito al quale i client accedono per ottenere servizi, tutta la computazione avviene sul server.**

I componenti di un'applicazione web sono simili ad un'app client-server.
**Il web è un sistema distribuito composto da client e server** che accedono a documenti collegati.

I **server** **gestiscono insiemi di documenti,** mentre i **client** **forniscono agli utenti un'interfaccia facile da usare** per accedere e presentare questi documenti.

- Architetture web tradizionali
- Architetture web multilivello
##### Architettura cooperativa

Questa architettura si basa su **entità autonome** che esportano e richiedono servizi secondo il modello di sviluppo a componenti lato server della **programmazione ad oggetti.**
È stato preso un concetto principale della OOP, **l'incapsulamento**, applicandolo all'abbattimento delle differenze tra i prodotti usati (Hardware, Software, programmazione, rete) di un sistema distribuito.

##### Architettura completamente distribuita

Questo tipo di architettura è tipico di **sistemi dove è necessaria la cooperazione di entità paritarie.**
Le tecnologie più importanti sono:

- **OMG** (Object Management Group): Consorzio tra varie aziende allo scopo di creare sistemi di gestione di architetture distribuite

- **RMI** (Remote Method Invocation): Consente a processi java distribuiti di comunicare attraverso una rete.

- **DCOM** (Distributed Component Object Model): È basato sull'estensione in rete della precedente tecnologia COM