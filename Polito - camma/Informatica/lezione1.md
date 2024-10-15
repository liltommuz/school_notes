Introduzione alla programmazione

i sistemi di elaborazione rappresentano l'informazione e la manipolano in forma digitale -- si trasforma l'informazione in sequenze di bit

Binary Digit  - bit

I calcolatori sono costituiti da circuiti elettronici, con componente base un transistor che funziona da interruttore -- 
Questi componenti sono semiconduttori, aperto o chiuso (non conduce)
Questi due stati fisici vengono mappati in 0 e 1.

Bisogna digitalizzare le informazioni in input

Il sistema operativo è quel componente software che permette di interfacciarsi con l'hardware

CPU -- Central Process Unit
RAM -- Random Access Memory --> Volatile
ROM -- Read Only Memory     
Memorie di massa:           --> Permanente
- HDD -- Hard Disk Drive
- SSD -- Solid State Drive --> Utilizzano Silicio per memorizzare

avvia il Bootstrap
Carica il sistema operativo in RAM
I dati per essere elaborati devono essere passati in memoria RAM --> La RAM è molto piu veloce, bisogna accedere alla memoria di massa il meno possibile

Bus di sistema -- Serie di connessioni elettriche - Sulla Motherboard sono disegnate delle piste elettriche
SI divide logicamente in 3 parti
- Bus dati          --> Permette di scambiare i dati
- Bus indirizzi     --> Permette alla CPU di indirizzare la cella di memoria o il dispositivo che vuole lei, solo la CPU indirizza gli altri
- Bus di controllo  --> Controlla se la richiesta è andata a buon fine, se non ci sei riuscito si crea un errore che va processato

Al bus di controllo si collegano altri dispositivi, la CPU può leggere e scrivere in RAM

- Scheda Grafica , GPU Graphic Process Unit
Fa i calcoli sulle primitive grafiche : Punti, Linee e poligoni
- Scheda audio
- Scheda di rete
- Porte -> permette di collegare tramite un interfaccia unificata vari output -- Solitamente usb e sue varianti

Quando la CPU parla con qualcuno gli altri si mettono in stati IDLE, perciò questa architettura va bene per un numero di CPU limitato, Personal Computer.

Software
--
Microsoft Word è un esempio software, anche i giochi elettronici i sistemi operativi e i relativi driver.
I driver sono quei moduli software dei sistemi operativi che permettono di interfacciare la nostra macchina con dispositivi diversi, Hardware non standard. Non plug and play.

Il programma è l'insieme delle istruzioni semplice messe insieme per risolvere un problema complesso, programmare vuol dire mettere insieme le istruzioni.

Ci sono 4 stadi per programmare le cui difficoltà vanno in ordine decrescente.
1. Capire il problema e stabilire i requisiti
2. Definire una soluzione informale --> Anche a parole dire cosa deve fare il programma
3. Soluzione formale -> Specificare le azioni mediante digrammi di flusso o una pseudo-codice
4. Generare il codice

Da ogni stadio si puo tornare indietro nei precedenti

```python
#Considerando studenti un array di oggetti studente
eta_max = 0

for studente in studenti:
    
    if studente.age > eta_max:
        eta_max = studente.age
        studente_vecchio = studente

studente_vecchio.name
```

Algoritmo: qualsiasi cosa che aiuta a rappresentare come ordine di operazioni il lavoro da fare per il risultato.
Ogni operazione può avere delle sotto operazioni e a volte possono dover eseguite piu volte.

Descrizione passo-passo di un procedimento.
--
I passi devono essere:
- Deterministiche           -> Dato lo stesso stream di dati in ingresso produce sempre lo stesso output
- Devono essere eseguibili  -> Devono produrre un output diretto
- Deve terminare in un tempo finito


Formalizzazione della soluzione
-- 
SI possono utilizzare pseudo-codice o flowchart.

Pseudo-codice:
Pro
 - Molto vicino al codice
Contro
 - Poco astratto

Flowchart:
Pro
- Piu intuitivo
- Descrizione più astratta

Contro
- Troppe cose da scriver (0 sbatta)


Pseudo-codice:
- Dividere il problema in sotto problemi
- metti le formule e i procedimenti logici

```python
saldo = 10000
anno  = 0

while saldo < 20000:
	anno  += 1
	saldo += (saldo * 5)/100
	
print(anno)
```


Tipi di linguaggi
--
Alto livello
- Molto simile al linguaggio umano, livello di astrazione altissimo

```Python
if x > 3:
	x +=1
```

Basso livello
- Molto simile al linguaggio macchina

```assembly
LOAD Reg1, Mem[1000]
ADD  Reg1, 10
```

Astrazione dei dati

livello alto
- x; integer; value = 3

livello basso
- Indirizzo di memoria dove inserisco il valore, e per alcuni dati una sola cella di memoria potrebbe non bastare.

----------
Istruzioni
--

Pseudo-istruzioni, non operative:

```Python
#Prima operazione non operativa
```

Istruzioni elementari, corrispondono a delle azioni:

```Python
anno = 0
print(anno)
```

Istruzioni di controllo del flusso, scelta e cicli:

```Python
if x > 9:
	print(x)
else:
	for i in range(2)
		print(x)
```

