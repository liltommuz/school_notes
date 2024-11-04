
### Le funzioni

Le funzioni permettono di dividere i problemi in sottoproblemi piu piccoli, che sono risolvibili.
Esistono funzioni gia pronte ma le funzioni possiamo scriverle anche noi.
#### Invocare una funzione

Quando invochiamo una funzione, il codice si interrompe ed inizia il codice della funzione invocata, quando la funzione termina il codice riprende esattamente al punto successivo all'invocazione della funzione.

```python
price = round(6.8725 , 2) # 6.88
```

#### Argomenti

>_Una funzione puo ricevere n argomenti, non è detto che il numero sia fisso a priori._
  _Gli argomenti possono anche non essere presenti._


#### Funzioni built-in

Sono installate insieme all'interprete python.

- abs
- max
- min
- str
- int
- boolean
- input

ecc...

>Le uniche che non bisogna usare sono quelle legate alla OOP, classmethod per esempio.

#### Funzioni in libreria

Le devi installare tramite pip.

#### Procedure

>Le procedure sono **funzione che non restituiscono risultati.**

### Realizzare e collaudare funzioni

Ogni funzione ha nell'header un nome che deve essere coerente e dei parametri (side_length) che la funzione si deve aspettare in input, e termina con i ":".
I parametri side_lenght possono essere utilizzati all'interno della funzione.

- Esempio:

Calcolare il cubo di un numero:
```python
def cube_volume(side_lenght):
	return side_lenght**3

n = float(input("Inserisci il lato del cubo:\n"))
Volume = cubeVolume(n)

print(Volume)
```

Creare funzioni è utile per organizzare il codice e anche per definire codice riutilizzabile.

>_Nota_: I parametri che vengono passati si chiamano **Parametri formali**, i parametri vengono passati per copiatura, 
>
>side_lenght = n, -> n viene copiato.

Cambiando il valore formale della funzione io non cambio il valore del chiamante.

```python
def cube_volume(n):
	return n**3

lato = float(input("Inserisci il lato del cubo:\n"))
Volume = cubeVolume(n)

print(Volume)
```
Anche se lo chiamo n, funzionerà lo stesso.
Se modifico n, lato rimarrà invariato poichè n è un alias. 

#### Commenti

All'esame non c'è necessità di scrivere i commenti.
I commenti sono utili poichè chi lavora sul codice capisce cosa si è fatto e quali erano le intenzioni.

```python
#Funzione che calcola il volume di un cubo
# @param side_length spigolo del cubo
# @return restituisce il valore del volume del cubo
#
def cube_volume(n):
	return n**3

lato = float(input("Inserisci il lato del cubo:\n"))
Volume = cubeVolume(n)

print(Volume)
```

Oppure: (Commenti multilinea """)

```python
def cube_volume(n):
"""
Funzione che calcola il volume di un cubo
:paramside_length spigolo del cubo
:return restituisce il valore del volume del cubo
"""
	return n**3

lato = float(input("Inserisci il lato del cubo:\n"))
Volume = cubeVolume(n)

print(Volume)
```

### Parametri posizionali o nominali

```python
def complex(real, imag):
	reale = real
	immaginario = imag
	print(f"{reale} + {immaginario}j")

x = complex(3,5) #3+5j -> Positional parameters


x = complex(real = 3, imag = 5) #3+5j -> Nominal parameters
```

Se uso i parametri nominali, non è piu importante la posizione.
I parametri posizionali devono sempre precedere i caratteri nominali.

>Se passiamo ad una funzione piu parametri o meno di quelli che si aspetta il codice darà errore.

>Se nessuno passa i parametri, si possono impostare di default i parametri formali.

La #print ha sia parametri posizionali che nominali:

```python
"""
Parametri nominali
"""
print(8,5) # 8 5
print(8,5, sep="$$$$") #8$$$$5

print(8,5 end="") # Non va a capo

print(file = sys.stdout) # Puoi dire di stampare su un file

print(flush = False) # Se flush = True, qualunque byte anche se non c'è un terminatore di riga, questo verrà stampato.
```
#### Parametri multipli

Il numero di parametri puo non essere definito:

```python
"""
Parametri non definiti in numero
"""
def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument :", arg)

myFun('Hello','Welcome','to','Politecnico')
```

La dimensione di argv si adatta a seconda del numero di parametri passati dal chiamante.
Questo se si definisce una struttura preceduta dall'asterisco.

#### Valori restituiti

La funzione restituisce qualcosa con la parola chiave #return.

Si puo fare in modo che return restituisca un unico oggetto che restituisca piu valori:

```python
def my_square(lato):
	return (lato**2, lato*4)

lato = float(input("Inserisci il lato del cubo:\n"))
quadrato = my_square(n)

print(quadrato[0], quadrato[1])
```

#### Eccezioni

Conviene avere sempre un unico punto di uscita, e quindi un solo return.

```python
def my_square(lato):
	if lato < 0:
		lato = 0
	return (lato**2, lato*4)

lato = float(input("Inserisci il lato del cubo:\n"))
quadrato = my_square(n)

print(quadrato[0], quadrato[1])
```

#### Funzioni che non restituiscono nulla

In realtà python restituisce sempre qualcosa, che è il valore None.
Anche se non c'è l'istruzione return, arrivati alla fine, la funzione restituisce il comando al chiamante.

```python
def box_string(string):
	n = len(string)
	print("-" * (n+2))
	print("!" + string + "!")
	print("-" * (n+2))

string = input("Inserisci il tuo nome:\n")
box_string(string)

```


### Organizzazione del codice

#### Funzione Main

**Rappresenta l'inizio di ogni codice.**
Soprattutto in c o in java. In python non è importante, pero per la leggibilità del codice (convenzione) è meglio chiamarlo #main.

```python
def main():
    lato = float(input("Inserisci il lato del cubo:\n"))
    volume = cube_volume(lato)
    print(f"Il volume del cubo è: {volume}")

def cube_volume(lato):
        return lato**3

# Il codice comincia qui
main()
```

In questo modo qualsiasi sia l'ordine delle funzioni, non da errore; L'importante è mettere la chiamata al #main in fondo.

Per far comprendere al meglio, che l'unico file che puo essere eswguito stand_alone è il main, sarebbe meglio scrivere:

```python
def main():
    lato = float(input("Inserisci il lato del cubo:\n"))
    volume = cube_volume(lato)
    print(f"Il volume del cubo è: {volume}")

def cube_volume(lato):
        return lato**3

if __name__ == '__main__':
    # Call the main if we are running in standalone mode
    #
    main()
```

##### Le variabili __ var __

Sono **variabili di sistema (dunder) di python** che verificano certe situazioni.
Ci sono dei programmi, ambienti di sviluppo (PyCharm), 

#### Funzione parametrizzata

Quando in un codice, si trova una ripetizione, conviene creare una funzione.
Funzioni con parametri variabili.

#### Scope delle variabili (Local vs Global)

- Variabili locali, definiti all'interno di una funzione.
- Variabili globali, definite al di fuori di una funzione.

Lo scope della variabile è dove è visibile nel codice per le funzioni.

>Esempio:

```python
def main():
    lato = float(input("Inserisci il lato del cubo:\n"))
    volume = cube_volume(lato)
    print(f"Il volume del cubo è: {volume}")

def cube_volume(lato):
        return lato**3

# Il codice comincia qui
main()
```

In questo esempio, io non posso utilizzare direttamente il lato, poichè è stato definito in main(), e perciò necessito di passare un parametro alla funzione che corrisponderà al lato.

>Oppure:

```python
lato = float(input("Inserisci il lato del cubo:\n"))
def main():
	global lato
	
    volume = cube_volume()
    print(f"Il volume del cubo di lato {lato} è: {volume}")

def cube_volume():
	global lato
     
    return lato**3

# Il codice comincia qui
main()
```

Inserendo global lato, possiamo utilizzarla globalmente.

>**_NOTA_** : Le variabili globali è meglio non utilizzarle.
>_Queste variabili occupano memoria per tutta la durata del programma_, le variabili locali invece vengono distrutte quando non vengono utilizzate.
>
>Inoltre, se la funzione modifica la variabile, modificherà anche l'originale.

**L'eccezione sono le costanti.**

### Funzione ricursiva

Esempio:

```python
def fact(n):
    if n != 1:
        n = n * fact(n-1)
    return n

print(fact(3)) # 6
```