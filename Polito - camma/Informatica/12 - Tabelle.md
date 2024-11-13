Le tabelle possono essere rappresentate tramite l'utilizzo di due liste.

```python
tabella = [
	[1,1,1],
	[2,2,2],
	[3,3,3] 
		] #tabella
print(tabella[0][1]) #stamperà 1
```

Le tabelle hanno due indici, l'indice di riga e di colonna.
- L'indice di riga è il primo.
- L'indice di colonna è il secondo.

Per stamparle si possono utilizzare due cicli:
```python
for i in range(len(tabella)):
    for j in range(len(tabella[0])):
        print(tabella[i][j]," ", end="")
    print()

#1  1  1  
#2  2  2  
#3  3  3  
```

Es.
- Se giocassimo a tris?
```python
tabella = [
    ["","",""],
    ["","",""],
    ["","",""]
        ] #tabella

def print_campo():
    for i in range(len(tabella)):
        for j in range(len(tabella[0])):
            print(tabella[i][j]," ", end="")
        print()

def vinto():
    pass

#1  1  1  
#2  2  2  
#3  3  3  
```

##### Definire una tabella

```python
ROWS = 5
COLONNE = 10
table = []

for i in range(ROWS):
    row = [0]* COLONNE
    table.append(row)

print(table)
```

##### Elementi vicini ad un elemento in tabella

Solitamente attorno ad un elemento ci sono 8 elementi, a meno che non si è nei bordi della tabella.

```python
#1  1  1  
#2  2  2  
#3  3  3  

# Il 2 in mezzo ha 8 elementi attorno, mentre quello alla sua sinistra ne ha solo 3 vicini, 1,2,3
```

Con le tabelle si puo andare out of range sia con l'indice di riga che con quello di colonna.

Quando si passa una tabella ad una funzione, si passa l'alias non l'intera tabella.
Come fa la funzione a ricavare la grandezza della tabella?

```python
len(tabella) #Rappresenta le righe
len(tabella[0]) # Rappresenta le colonne
```

#### Copiare una tabella

Per copiare una tabella bisogna usare il metodo deepcopy().

```python
ROWS = 5
COLONNE = 10
table = []

for i in range(ROWS):
    row = [0]* COLONNE
    table.append(row)

print(table)

table2 = copy.deepcopy(table)
print(table2)
```

In questo modo crei copie differenti sia delle righe che delle colonne.
se io faccio solo copy(), creo una nuova "Riga", pero il riferimento alle colonne sono quelli di prima.