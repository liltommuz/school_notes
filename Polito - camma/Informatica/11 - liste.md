Lista sono **strutture dinamiche mutabili che possono contenere un numero variabile di elementi di ogni tipo,** a differenza delle stringhe che hanno dati omogenei e non sono mutabili

## Inizializzare una lista

Le liste possono essere inizializzate con le [], oppure con il metodo list().

```python
lista = [] #vuota
lista = [1, 2, 3, 4] #inizializzata con elementi

i = 0 # Le liste partono dalla posizione 0
lista[i] = 123 #posso modificare gli elementi attraverso indicizzazione

print(lista[0]) # -> 123
print(lista) # -> [123, 2, 3, 4]
```

Le variabili "normali" vengono dette "scalari". Le liste sono liste

## Liste vs stringhe

Entrambe sono sequenze, ma le **liste possono essere eterogenee**. Tuttavia non è una buona idea costruire liste con elementi eterogenei, perchè diviene tutto molto complesso

Potrebbe servire se definisco un pattern nella lista. Ad esempio gli indici dispari potrebbero contenere dei numeri mentre quelli pari delle stringhe, ma questo si può fare con un dizionario.
In generale le liste **dovrebbero contenere un solo tipo di elemento.**

- Le liste sono mutabili, le stringhe no.

>Se con le liste uso un indice che è fuori la lunghezza della stringa genero un'eccezione `IndexError`. Per sapere quanti elementi contiene una lista uso `len()`

## Iterare su una lista

Usando un indice:

```python
lista = [1, 2, 3, 4]
i = 0
while i < len(lista):
	print(i, lista[i])
	i += 1

for i in range(len(lista)):
	print(i, lista[i])
```

Iterando direttamente sugli elementi:

```python
lista = [1, 2, 3, 4]

for elem in lista:
	print(elem)
```

Oppure posso iterare sia sugli elementi che sugli indici con `enumerate()`

```python
lista = [1, 2, 3, 4]

for elem, idx in enumerate(lista):
	print(idx, elem)
```

Il nome di una lista altro non è che un alias che si riferisce a una posizione di memoria. 

>L'interprete associa ogni alias a un indirizzo di memoria, in questo modo sa dove trovare i dati.

### Indici negativi

Posso indicizzare una lista con indici negativi, dove a partire da -1, gli indici si riferiranno all'ultimo per poi arrivare al primo.

```python
	lista = [1, 2, 3, 4]
	
	print(lista[::-1])
```
## Aliasing

L'aliasing si verifica quando due variabili puntano alla stessa zona di memoria:

```python
lista = [1, 2, 3, 4]

lista2 = lista #entrambi gli alias punteranno alla stessa lista

lista[0] = "mhanz"
lista2[0] = 23

print(lista) # -> [23, 2, 3, 4]
```

Quando passo una lista a una funzione essa riceve una copia del puntatore alla lista, e può quindi modificare tale lista. 
Per creare un duplicato di una lista si usa `list()`:

```python
lista = [1, 2, 3]
lista2 = list(lista)

lista2[0] = 0

print(lista) # -> [1, 2, 3] 
print(lista2) # -> [0, 2, 3]
```

>Si puo anche utilizzare lo slicing, lista[:].
## Operazioni con le liste

Come ogni struttura dati le liste hanno i loro metodi, che permettono di svolgere diverse operazioni.
### Aggiungere elementi

Alla fine della lista si fa con `append()`:

```python
lista = [1, 2, 3]
lista.append(5)

print(lista) # -> [1, 2, 3, 5] 
```

 Se voglio inserire un elemento in un indice specifico uso  `insert()`:

```python
lista = [1, 2, 3]
lista.insert(1, 5)

print(lista) # -> [1, 5, 2, 3] 
```
### Rimuovere elementi

Per rimuovere l'ultimo elemento della lista uso `pop()`:

```python
lista = [1, 2, 3]
lista.pop()

print(lista) # -> [1, 2] 
```

Se voglio rimuovere un elemento a un indice specifico lo passo alla `pop()`:

```python
lista = [1, 2, 3]
lista.pop(0)

print(lista) # -> [2, 3] 
```
### Minimo di una lista

```python
lista = [1, 2, 3]

print(min(lista)) # -> 1 
```
 
 Con liste che hanno stringhe il minimo corrisponde alla stringa che precede le altre in ordine alfabetico
### Massimo di una lista

```python
lista = [1, 2, 3]

print(max(lista)) # -> 3 
```

Con liste che hanno stringhe il massimo corrisponde alla stringa che antecede le altre in ordine alfabetico

### Elemento in una lista

Per controllare se un elemento è presente in una lista si usa `in`:

```python
lista = [1, 2, 3]

if 2 in lista:
	print("C'è un mhanz")
else:
	print("Assente")
```

### Indice di un elemento

Per sapere in quale indice si trova un elemento uso `index()`:

```python
lista = [1, 2, 3]

print(lista.index(2)) # -> 1
```

>Se un elemento non è presente però si genera l'eccezione `ValueError: element not in list`,  quindi per evitarlo controllo prima che l'elemento sia presente con `in`

### Concatenazione di liste

Avviene allo stesso modo delle stringhe:

```python
lista = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista + lista2) # -> [1, 2, 3, 4, 5, 6]
```

**Le due liste vengono "unite".** L'ordine, ovviamente, conta. 

>Usando `+` si crea una nuova lista diversa dalle precedenti

Se voglio che una lista venga semplicemente estesa, senza crearne una nuova, uso `extend()`:

```python
lista = [1, 2, 3]

print(lista.extend([4, 5, 6])) # -> [1, 2, 3, 4, 5, 6]
```

### Replicazione di una lista `n` volte

Se uso moltiplico una lista per un numero intero `n` ottengo la stessa lista moltiplicata `n` volte:

```python
lista = [1, 2, 3]

print(3 * lista) # -> [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Confronto tra liste

Due liste per essere uguali devono avere la stessa lunghezza e gli stessi elementi con la stessa posizione:

```python
lista = [1, 2, 3]

print(lista == [1, 2, 3]) # -> True
print(lista == [3, 2, 1]) # -> False
print(lista == [3, 2]) # -> False
print(lista == [1, 2]) # -> False
```

### Ordinamento di stringhe

Se voglio ordinare una lista uso `sort()` o `sorted()`:

```python
lista = [3, 1, 2]

lista.sort() # -> [1, 2. 3]
lista2 = sorted(lista) # -> [1, 2. 3]
lista3 = sorted(lista, reverse=True) [3, 2, 1]
```

La differenza risiede nel fatto che `sorted()` crea una lista nuova ordinata, mentre `sort()` ordina quella già esistente

### Slicing

Anche per le liste funziona lo slicing. In particolare posso modificare elementi in sequenza:

```python
lista = [3, 1, 2]

lista2 = lista[:] #crea una copia della lista

lista[0:1] = [5, 6] 
print(lista) # -> [5, 6, 1, 2]

lista[0:1] = [] #posso anche restringere una lista in questo modo
print(lista) # -> [6, 1, 2]
```

> _Nota:_ Il primo numero nello slicing è incluso, mentre il secondo è escluso.

---
### list comprehension

creare una lista con le lunghezze dei giorni della settimana.

```python
giorni = ['lunedi','martedi']
lunghezza = []

for giorno in giorni:
	lunghezza.append(len(giorno))
```

- Con la comprehension, quando si deve definire una struttura si puo fare in una linea di codice.

```python
giorni = ['lunedi','martedi']
lunghezza = [len(giorno) for giorno in giorni] # prende la lunghezza dei giorni per ogni giorno
```

Puo esserci anche una condizione:

```python
giorni = ['lunedi','martedi']
accentati = [giorno for giorni if giorno[-1] = "'"] # Diciamo che prende solo gli apostrofi
```

>La comprension funziona con qualsiasi struttura dati di tipo ordinato.

- Insiemi
- Dizionari
- Tuple

---
### Esercizi con algoritmi

Es.
- Stampa la media di questa lista di valori eliminando il piu basso prima di farlo.

```python
voti = [1,2,3,4,5]

voti.remove(min(voti))
if len(voti) > 0:
	media = sum(voti)/len(voti)
```

Es.
- Vogliamo capire se un dado è truccato, si lancia il dado un tot di volte e si vede se uno dei valori esce con frequenza anomala.

```python
from random import randint

LANCI = 100
VALORI = 6
lista = [0]*VALORI

for i in range(LANCI):
    valore = randint(1,VALORI)
    lista[valore-1] += 1

for i in range(VALORI):
    print(f"valore {i+1}: è uscito {lista[i]} volte")
```

Es.
- Vogliamo scambiare la posizione degli elementi di un vettore:

```python
def scambio(lista):
    meta = len(lista)//2
    return lista[meta:] + lista[:meta]

oggetti = [i for i in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
oggetti2 = scambio(oggetti) #[5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
oggetti3 = scambio(oggetti2) #La lista ritorna normale
```
---
