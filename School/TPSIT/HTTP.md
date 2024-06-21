#### Introduzione HTTP

I **client** sono **elementi attivi** che:

- Utilizzano il **protocollo HTTP** per connettersi ai server.
- Usano un **URL** per identificare le risorse
- Richiedono **pagine web** ai server e ne **visualizzano il contenuto.**

I **server** sono **elementi passivi** che:

- Rimangno in ascolto di eventuali connessioni di nuovi client su una **determinata porta TCP** .
- Utilizzano il **protocollo HTTP** per interagire con i client.
- Forniscono ai client le **pagine web o le risorse richieste**.
#### La comunicazione nel web con protocollo HTTP

**HTTP è utilizzato per trasmettere risorse.**
Una risorsa è identificata da un **URI o URL** e può essere:

- Un **file**
- Il **Risultato di una query**
- L'**uscita** di uno script CGI
- Un **documento disponibile** in diversi linguaggi
- **altro**
#### Il protocollo HTTP: client-server, HTTP 1.0, HTTP 1.1. Tipi di risorse. Come avviene la comunicazione tra client e server

Ci sono 2 versioni di HTTP, 1.0 e 1.1, la differenza è che il secondo permette di specificare una **connessione permanente** oltre a consentire il **criptaggio** di alcuni dati.
La connessione permanente è una **richiesta e la risposta all'interno della stessa connessione.**

Definizioni del W3C (World Wide Web Consortium):

- **URI** (Uniform Resource Identifier), sequenza di caratteri che identifica universalmente una risorsa tramite il nome e la posizione
- **URL** (Uniform Resource Locator), sequenza di caratteri che identifica universalmente la posizione di una risorsa
- **URN** (Uniform Resource Name), sequenza di caratteri che identifica universalmente il nome di una risorsa.

L'**URL** è un URI che identifica una risorsa e lascia intendere che quest'ultima è ottenibile da un host di rete chiamato www.ferrari.com .
L'**URN** è un URI che mappa universalmente e univocamente una risorsa mediante il suo identificativo, o nome.

Le sessioni HTTP sono basate sul protocollo TCP.
Sia le richieste inviate al server sia le risposte sono trasmesse mediante i seguenti passaggi:

1. Il **server rimane in ascolto sulla porta 80**
	1. Il **client apre una connessione TCP** sulla porta 80;

2. Il **server accetta la connessione**
	2. Il client invia una **richiesta**;
	
3. Il **server invia la risposta al client;**
4. Alla **fine della sessione il server chiude la connessione**;


#### Tipi di connessioni

Esistono 2 principali tipi di connessione http 1.0 e http 1.1

Nell' 1.0 la connessione viene attivata dal client tramite lo scambio di 3 pacchetti TCP con il server
Una volta poi soddisfatta la richiesta la **connessione viene chiusa.**

Nell'1.1, di tipo **permanente**, il **server invece lascia aperta la connessione TCP dopo aver spedito la risposta.**
Le successive risposte fra client e server, utilizzeranno la stessa connessione.
**La connessione viene perciò chiusa all'esaurimento dell'intervallo di timeout.**


Esistono 2 tipi di connessione permanente:

- **Incanalata:** Le richieste vengono aggiunte a una coda chiamata pipeline, mentre le risposte vengono processate ed inviate nello stesso ordine delle richiesta.
- **Non incanalata**: Il client passa ad una nuova richiesta solo quando la risposta alla precedente è stata ricevuta.

HTTP 1.1 utilizza la connessione incanalata.

#### messaggi HTTP Request e Response

Durante la comunicazione server e client si scambiano dei messaggi, formati da:

- Una **riga iniziale**
- Un'**intestazione (Header)**
- Una **riga vuota**
- Un **corpo del messaggio(body)** , non obbligatorio
##### HTTP Request

Il messaggio di richiesta è inviato dal client ed è formato da:

- **riga di richiesta**
- **Intestazione HTTP**
- Una **riga vuota**
- **Corpo del messaggio**

In genere la prima riga contiene la versione del protocollo HTTP utilizzato.
Nella riga di richiesta c'è anche il metodo (GET,POST,DELETE,PUT, ecc...) e l'URI.

Gli header piu comuni che si possono trovare nelle richieste sono:

- La **versione del Browser (User-Agent)**
- **L'host** presente nell'URL

Gli Header si concludono con una riga vuota, la quale può essere seguita da qualsiasi dato da inviare al server. La dimensione massima del dato è stabilita nell'**Header Content Length**.
##### HTTP Response

Dopo che ha elaborato la risposta, il server deve inviarla al client.
La response è simile alla request, la differenza è che queste iniziano con una riga di stato e non di richiesta:

- **Riga iniziale, con stato e versione del protocollo
- **Intestazione** facoltativa
- **Corpo** facoltativo

Gli header, **come nella request,** sono formati da **insiemi di coppie**, formate da **un nome separato dal valore dai due punti**, che specificano le caratteristiche del messaggio.

Esistono vari tipi di Header
1. **Header generali della trasmissione:**
	- MIME-Version 
	- Transfer-Encoding -> compressione dei dati trasmessi e si riferisce a tutto il messaggio

2. **Header relativi all'entità trasmessa:**
	- Content-Type -> Indica il MIME e specifica il tipo di contenuto (testo, immagine, ecc)
	- Expires -> Indica la data di validità della risorsa

3. **Header riguardo alla Richiesta effettuata:**
	- User-Agent -> Versione e il tipo di browser oltre alla versione e al sistema operativo client
	- Host -> Indica il nome  e il dominio del server e la porta TCP su cui il server è in ascolto

4. **Header della risposta generata:**
	- Server -> Una stringa che descrive il server (tipo,sistema operativo e versione)
	- WWW-Authenticate -> indica il **tipo di autenticazione** e le credenziali per autenticarsi

La sezione **body** contiene in genere **la pagina HTML richiesta dal client.**
L'**entity body** è quasi sempre presente nella risposta.


####  La codifica url, i codici di stato, la suite Chrome developer Tools
##### Codifica URL
Nella **codifica URL,** i dati di un form HTML vengono codificati per essere **impacchettati in una trasmissione GET o POST**.
Questa codifica viene utilizzata nelle Querystring per inserire all'interno delle URL delle stringhe di testo in modo sicuro e conforme allo standard previsto dalle URL.

La stringa da inviare è sempre costituita da una **coppia** **nome campo : valore**.
**Tutti i caratteri non sicuri presenti nella stringa in simboli formati dalla percentuale e dal codice ASCII relativo** e altri caratteri non stampabili vanno **convertiti**; e tutti **gli spazi vuoti vanno eliminati sostituendoli** con il carattere %20;3.
I nomi e i valori vanno uniti con = e i nomi separati da &.
Esempio:
					nome1=valore1&nome2=valore2&nome3=valore3
##### Le rappresentazioni HTTP
 Durante una comunicazione sia la richiesta che la risposta contengono una **rappresentazione della risorsa.**
Le **rappresentazioni HTTP** sono informazioni che riguardano la risorsa intesa come indirizzo di localizzazione, il formato e lo stato della risorsa attuale e nella sua evoluzione futura.
I due elementi cardine della rappresentazione sono:
- **Intestazione** (Header) del messaggio
- **Corpo** (Body) del messaggio

L'H**eader HTTP** contiene informazioni chiamate metadati, definite strettamente dalle specifiche HTTP, contengono del testo e vanno formattate.
Il **body HTTP** contiene informazioni che rappresentano dati in qualunque formato.

La **risposta HTTP deve specificare il tipo del contenuto del body attraverso l'intestazione, nel campo content-type.**

##### Codici di stato

I **codici di stato sono restituiti dal server HTTP per indicare al client l'esito di una richiesta.**
Esistono circa 50 codici di stato. La maggior parte non corrisponde con esattezza al comportamento delle moderne app web, alcune sono state pensate per usi futuri.

- codici 100-199 (**Information**), forniscono informazioni temporanee alla richiesta, utilizzo sconsigliato
-  codici 200-299 (**Successful**), completamento di una richiesta con successo
-  codici 300-399 (**Redirection**), comunicare una varietà di stati che richiedono un trattamento particolare del browser.
-  codici 400-499 (**Client Error**), indicano le condizioni di errore provocate dal comportamento del client
-  codici 500-599 (**Successful**), sono prodotti da problemi verificatisi sul server

##### Google Chrome developer suite

Sono dei tool inclusi nel browser che hanno delle funzionalità specifiche e permettono:
- **La navigazione all'interno del DOM** (Document Object Model) delle pagine web
- L'**analisi** e la **modifica** dell'**HTML** e dei fogli di stile in tempo reale
- Il **monitoraggio**, il **debug** e le **modifiche** del codice JavaScript in tempo reale

