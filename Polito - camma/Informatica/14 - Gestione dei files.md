Un file serve a mantenere informazioni. Il file system si occupa dei file.
I file con una estensione si dividono in:
- File binari
- File di testo

>Nei **file di testo** viene salvata la codifica dei caratteri
>**I file binari** contengono i valori che corrispondono alla relativa codifica

_Esempio_:

	Devo scrivere -10,
	
	Nel file di testo scriverò:
	- codice ASCII(o UNICODE) del casattere meno
	- codice ASCII(o UNICODE) del carattere 1
	- codice ASCII(o UNICODE) delcarattere 0
	occupando 3 byte.
	
	
	Nel file binario invece scriverò:
	- complemento a 2 del numero -10.
	
	parto da +10, 00001010
	scambio 0 ed 1 e sommo 1.
	-10 = 01110110
	Questo è l'unico byte che scrivo nel file binario.

I file binari occupano meno spazio.
La codifica di testo è visibile a tutti coloro che hanno un editor di testo.

---
### File di testo

Si dividono in testo libero e testo strutturato.
#### Testo libero

Parole libere.
#### Testo strutturato

Organizzato per record, dove i record possono essere su una singola riga o sparpagliati su piu righe, la struttura è nota.
##### Record per riga

##### Markdown, HTML

Utilizza i tag per scrivere. che descrivono come viene presentato il testo, l'informazione.

---
### leggere e scrivere file

Non puoi leggere o scrivere un file se prima non lo hai aperto, nel caso in cui non sia possibile aprirlo bisogna gestire l'errore.

###### Leggere un file

In python è possibile interagire con i file di testo:

```Python
infile = open("input.txt", "r")
```

Se ci riesce, la open() restituisce un oggetto file che va memorizzato in una variabile, in questo modo sarà possibile interagire con il file.
>È un contenitore di righe.

###### Scrivere un file

Nel caso in cui si voglia scrivere si utilizza il metodo open con il parametro "w".

```Python
infile = open("input.txt", "w")
```

Se in questo caso il file non esiste, ne viene creato uno nuovo.
Se il file esiste già il suo contenuto viene cancellato.
>Viene restituito anche in questo caso un oggetto file

>_NOTA:_
>Dopo che un file è stato utilizzato, esso va chiuso.

```Python
infile.close()
outfile.close()
```

I file si chiudono al termine del codice, ma se nel caso mancasse corrente e tengo i file aperti, le informazioni vengono perse.
Perciò bisogna chiuderli appena si ha la possibilità.

##### Descrittori

Permettono di fare cose con i file all'internod ella open():

	"r" -> 
	"w" -> 
	"x" -> 
	"a" -> 
	"q" -> 
	"w" -> 
---
### Esempio

```Python
FILENAME = "story.txt"

file = open(FILENAME,"r")
```
---
### Attenzione a windows
Windows prova ad aprire il file con una codifica proprietaria, tutte le lettere accentate o comunque non presenti nella codifica di windows non verranno riconosciute.

perciò bisogna costringere a utilizzare la utf-8 (UNICODE):

```Python
file = aopen("file.txt","r",encoding="utf-8")
```
---
### Leggere da un file su python

Si puo leggere un file una riga per volta oppure tutto in una volta.
Nel secondo caso, se io non ho spazio a sufficienza mi crusha la macchina non il programma.

```Python
FILENAME = "story.txt"
file = open(FILENAME,"r")


carattere = file.read(1)
print(carattere)

carattere = file.read(1)
print(carattere)

carattere = file.read(1)
print(carattere)

###
#M
#a
#r
```

Mi accorgo di essere alla fine del file se la read mi restituisce la stringa vuota "".

Leggere un file carattere per carattere:

```python
FILENAME = "story.txt"

file = open(FILENAME,"r")

carattere = file.read(1)
print(carattere, end="")

while carattere != "":
    carattere = file.read(1)
    print(carattere, end="")
    
file.close()
```

Leggere un file carattere n caratteri consecutivamente:

```python
FILENAME = "story.txt"

file = open(FILENAME,"r")

carattere = file.read(10)
while carattere != "":
    print(carattere, end="")
    carattere = file.read(10)
```

Leggere per righe:

- Ci sono 2 possibilità, readline:

```python
FILENAME = "story.txt"

file = open(FILENAME,"r")
  
riga = file.readline()

while riga != "":
    print(riga, end="")
    riga = file.readline
```
ATTENZIONE - Questo codice non funziona.

- Utilizzare il ciclo for
```python
FILENAME = "story.txt"

file = open(FILENAME,"r")  

for row in file:
    print(row,end="")
```

Esercizio:
- Quante parole per ogni riga:

```python
FILENAME = "story.txt"
file = open(FILENAME,"r")

for i,row in enumerate(file):
    parole = row.split()
    print(i+1, len(parole))
```

- Quante vocali per ogni riga

```python
FILENAME = "story.txt"
vocali = "aeiouAEIOU"
file = open(FILENAME,"r")

for i,row in enumerate(file):
    parole = row.split()
    counter = 0

    for parola in parole:
        for vocale in vocali:
            counter += parola.count(vocale)
  
    print(i+1, counter)
```

#### Cosa da non fare

Brutta poichè legge e crea una stringa che contiene tutto il testo, bisogna avere abbastanza memoria per fare una cosa del genere.

```python
file.readlines()
```

#### Esercizio:

Leggi i voti da un file e fai la media.

```python
FILENAME = "voti.txt"
file = open(FILENAME,"r")
  
voti = [float(row) for row in file ]

if len(voti) != 0:
    print("La media è ", sum(voti)/len(voti))
file.close()
```