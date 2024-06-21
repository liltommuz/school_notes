#### Introduzione ad AJAX
**AJAX** ,acronimo di Asincronous JavaScript and XML, **è una tecnica di sviluppo per la realizzazione di applicazioni web interattive.**
Ajax è un concetto utilizzato per sviluppare applicativi avanzati **limitando lo spreco di risorse**, **permette a un client di richiamare informazioni lato server in modo veloce e trasparente.**

Mediante AJAX **si puo aggiornare una sezione di pagina HTML senza che questa venga caricata di nuovo dal server** tramite richieste http effettuate in JS.
AJAX è stato creato per creare **applicazioni web interattive**, per **aggiornare in modo dinamico una pagina web** senza che l'utente debba ricaricarla.
Essendo chiamate **asincrone**, una volta fatta la richiesta **non è necessario aspettare la risposta per poter fare altre operazioni.**

L'unico **problema** è la presenza di molteplici browser, non tutti lo supportano direttamente.
**In alcuni è necessario effettuare un aggiornamento o scaricare un apposito add-on.**

##### Come funziona?

AJAX è un insieme di applicazioni web dinamiche, basate sull'interazione di diverse tecnologie:

- **HTML e CSS** per la visualizzazione della pagina
- **DOM**, modificato attraverso JS per offrire dinamicità alla pagina Web
- **XMLHttpRequest**, che consentono al browser e al server di comunicare senza che la pagina venga ricaricata - Il core di AJAX è rappresentato da questa classe, l'utilizzo di essa varia a seconda del browser che si utilizza.

#### BOM e DOM di javascript

##### DOM
**Document Object Model,** rappresenta la struttura in cui è organizzata ogni pagina web.
Un'**API** è un'**insieme di funzioni**, metodi e proprietà, che **i programmi possono richiamare al fine di delegare il lavoro al sistema sottostante**
Il **DOM è un'API**(Application Programming Interface), cioè un interfaccia per la programmazione di applicazioni, che consente di manipolare il contenuto di una pagina web.

Il DOM è **indipendente dalla piattaforma** e descrive la struttura di un documento HTML o XML.
##### BOM
**Browser Object Model**, rappresenta la struttua in cui è organizzata il browser.
Il **BOM** non ha standard ufficiali, è generalmente composto da una serie di oggetti che rappresentano il browser e i suoi componenti, esso permette di **interagire e manipolare il browser come se fosse composto da oggetti.**
L'oggetto principale nel **BOM è l'oggetto window**, che sarebbe la **finestra del browser.**
La **proprietà document di questo oggetto rappresenta il DOM** e permette di manipolare il contenuto della pagina.
####  I quattro stadi della comunicazione con AJAX
##### XMLHttpRequest

Questa classe **permette di effettuare, con HTTP, la richiesta ad una risorsa in modo indipendente dal browser**, nella richiesta, che è **asincrona**, si può **inviare informazioni sotto variabili GET o POST in maniera simile all'invio di un form.**

##### Flusso dei dati
Viene stravolto perciò il **flusso dei dati tipico di una pagina web** che è racchiuso in due passaggi:
- Richiesta dell'utente
- Risposta del server

Con AJAX si perde questo schema, poichè l'utente all'interno della stessa pagina può fare piu richiesta indipendenti, il problema di AJAX, per gli sviluppatori e gli utilizzatori, è che **non deve avere tempo di attesa sulla risposta.**
Gli **sviluppatori** potrebbero avere difficoltà quando la richiesta asincrona necessità per forza una risposta per poter completare altre operazioni.
I **navigatori** potrebbero non avere idea di cosa stia accadendo alla pagina, chiudendola, ignari di aver richiesto un'informazione.

##### I quattro stadi della comunicazione con AJAX
Una volta aperta la richiesta, AJAX passa attraverso quattro stadi:

- **Richiesta aperta**, ma i dati non sono ancora stati inviati (OPENED): il metodo open() è stato invocato;
- **Richiesta dati inviata**, cioe il metodo send() è stato invocato e sono stati ricevuti gli header della risposta;
- **I dati sono ricevuti e comincia la loro lettura** (**LOADING**: sta avvenendo il download del body della risposta Http);
- **Operazione completata** (**DONE**: l'operazione di fetch è terminata)
Il codice di stato è il valore che viene aggiornato nel suo attributo leggibile con **readyState()**.

Un esempio di tecnologia che utilizza AJAX è google suggest che **consente di ricercare una parola attraverso continui suggerimenti ricevuti in modo asincrono.**
