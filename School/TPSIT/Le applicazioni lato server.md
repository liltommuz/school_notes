#### Elaborazione server-side e programmazione server-side

La **programmazione server-side** si riferisce al **meccanismo mediante il quale tutto o parte del documento richiesto dal client viene generato in seguito a un'elaborazione che viene eseguita sul server**.
Il processo web server genera dinamicamente la risposta in funzione della richiesta e dei parametri inclusi con essa, per esempio:

- Il client chiede gli **orari dei treni** per una **certa** **destinazione** e **data**
- La **risposta del server sarà diversa,** la pagina che verrà generata e inviata al **client** dovrà essere **elaborata volta per volta per ogni caso specifico**

Il **web server** deve essere opportunamente **configurato** e **strutturato** per effettuare **l'elaborazione server-side**, ovvero **mandare in esecuzione uno specifico programma in modo che generi il contenuto 'dinamico' al momento della richiesta.**
#### Modello a codice separato e modello a codice embedded

**La programmazione server-side è la programmazione di componenti software che vengono elaborati sul server**, esistono diverse tecniche di programmazione che si differenziano per:

- Linguaggi di programmazione supportati;
- Web server supportati;
- Meccanismi di aggancio al Web server e il loro impatto sulle prestazioni;
- L'ambito applicativo per il quale sono concepite;

Una classificazione può essere fatta in base alla relazione che questi programmi hanno con HTML:

- **codice separato, asscoaito a una URL**:
	- Common Gateway Interface (CGI)
	- Java Servlet,
	- NSAPI, ASAPI, ISAPI
- **codice embedded in HTML**:
	- Server Side Includes (SSI) - Apache,
	- Active Sever Pages (ASP) - Microsoft,
	- PHP,
	- Java Server Pages (JSP)

##### Meccanismo dei form HTML

Questo meccanismo **consente di inviare informazioni da un web browser client-side a un programma in esecuzione server-side.**

Con il metodo get i dati vengono inviati attraverso la URL mediante una query string dove i parametri sono accodati con il carattere ? e separati dal carattere &
Stessa cosa con la post che permette di nascondere i dati alla vista di tutti.
			Altre info in HTTP->La codifica url, i codici di stato, la suite Chrome developer Tools-> la codifica URL
#### CGI

Una tecnica per **realizzare l'elaborazione server-side a codice separato** è quella di **invocare procedure remote indicando l'indirizzo di un programma CGI che viene eseguito sul server** e al quale vengono passati i dati letti nel form.
Le applicazioni che usano questo standard prendono il nome di **Programmi CGI** e sono scritte in un **qualunque linguaggio di programmazione che può leggere da standard input e scrivere su standard output.**

Un programma CGI **viene eseguito dinamicamente** in risposta alla chiamata e produce un output chesarebbe la risposta alla richiesta Http.
Le operazioni si svolgono nel seguente ordine:

- In una pagina HTML il **client** invia al server la richiesta di eseguire un programma CGI con alcuni parametri dati in ingresso, utilizzando Http;
- Il **server** attraverso l'interfaccia CGI chiama il programma indicato dal client, passandogli i dati del form;
- Il **programma CGI** esegue le operazioni opportune e **comunica i dati elaborati** in una pagina HTML al **server**, utilizzando l'interfaccia CGI;
- Il **server** invia al **client** i dati elaborati dal programma CGI tramite protocollo Http;

**Per comunicare con l'utente, il programma CGI produce una pagina HTML e la passa al web serverver che la invia all'utente che puo visualizzarla dal suo browser.**

#### Servlet

Le **servlet** sono classi particolari di **Java** e sono un'**alternativa al modello CGI.**

La principale **differenza** è che **gli script CGI sono eseguiti dal sistema operativo mentre le servlet vengono eseguite dalla JVM integrata nel Web server.**
Gli script CGI sono meno portabili delle servlet,infatti tutti i moderni Web server hanno integrata la JVM.

Una seconda differenza è legata **all'efficienza** :

- Gli **script CGI** vengono **caricati ed eseguiti una volta per ogni richiesta**, richiedono sempre un notevole tempo di latenza
- Le **servlet** vengono **caricate solo una volta e viene creato un thread per ogni ricihiesta**.

Una servlet una volta caricata rimane in memoria e può ottimizzare l'accesso alle risorse attraverso caching, pooling, ecc..

Un altra differenza è nella portabilità dei linguaggi:

- Gli **script CGI** possono utilizzare quasi **qualsiasi linguaggio**, a scelta del programmatore che lo decide in base all'applicazione che deve realizzare
- Le **servlet** sono **classi java** e di conseguenza devono essere scritte in Java
##### Struttura di una Servlet
Una **servlet** è una classe di Java ,gestita da un 'container', che **produce contenuto web dinamico.**
**Il container è un'applicazione Java che controlla e regola il ciclo di vita della servlet.**

Ogni **istanza di una servlet è un oggetto Java** che viene caricato ed eseguito dal Web server all'interno del processo di richiesta/risposta di servizi.

Il **Web server** **svolge la funzione di container** occupandosi della gestione del ciclo di vita delle servlet, passandogli dati dal client e restituendo al client i dati prodotti dall'esecuzione delle servlet.

Il container gestisce:

- La comunicazione con i client;
- La sicurezza;
- Il multithreading;
- L'attivazione della servlet;
- La terminazione della servlet;

Dato che la servlet viene caricata in memoria, durante la prima esecuzione, le inizializzazioni vengono eseguite una volta sola e consentono una condivisione dei dati tra le istanze di una servlet piu semplice.

##### Flusso di esecuzione della comunicazione response/request

1. Un **client invia una richiesta** per una servlet a un web application server;
2. Se si tratta di una **prima richiesta**, il server **istanzia e carica** la servlet;
3. Si attiva un **thread** che gestisce la comunicazione tra il client e la servlet stessa;
4. Il **server** invia al **thread-servlet** la richiesta pervenutagli dal **client**;
5. Il **thread-servlet** costruisce la **risposta** e la inoltra al **server**;
6. Il **server invia la risposta al client.**

**Nel caso in cui si verifichi una richiesta contemporanea di piu client vengono attivati nel servlet container più thread.**
##### TomCat
**Generalmente le applicazioni Web interagiscono con i database oppure con altre servlet.**

L'esecuzione delle servlet richiede inoltre che sul server sia installata una versione di Java.
Il **servlet container** open source più diffuso è TomCat di Apache.
**Tomcat è interamente scritto in Java ed è disponibile per diverse piattaforme e si integna con i piu diffusi Web server,** come Apache e IIS.
#### NSAPI e ASAPI 

Per il modello **NSAPI** non esiste uno standard formale, le applicazioni che usano **NSAPI possono non essere portabili in tutti i Web server.**
**Apache** ha sviluppato Apache API detto **ASAPI**, anche **Microsoft** ha creato le sue dette **ISAPI**.