
Operatori numerici
--

Gli operatori sono:

- Addizione: +
- Sottrazione: -
- Moltiplicazione: *
- Divisione: /
- Potenza: **

La priorità è uguale a quella classica

Se provo ad usare un *operatore numerico* tra due variabili che non sono numeri, da errore.

```Python
num = 8
string = "babba"

print(num + string) # il risultato sara: TypeError
```

è possibile usare pero il + per le stringhe, per *concatenare* le due stringhe.

```Python
string  = "babba"
string2 = " besy"

print(string + string2) # Il risultato sara: babba besy
```

oppure è possibile *elencare*:

```Python
string  = "babba"
string2 = " besy"

print("Sei una", string, string2) # Il risultato sara: Sei una babba besy
```


Si puo usare anche il per con significato di *ripetizione*:

```Python
string  = "babba"

print("Sei una", string*3) # Il risultato sara: Sei una babbababbababba
```

Si possono scrivere valori grandi con la *mantissa* in notazione scientifica, sono valori reali:
1E3 = 1 * 10 alla terza = 1000

```Python
num  = 1E3

print(num) # Il risultato sara: 1000.0
```

Come tiro fuori il quoziente e il resto di una divisione??

```Python
a  = 7
b = 4

print(a/b) # Il risultato sara: 1.75

print("Il quoziente è", a//b) # Il risultato sara: 1

print("Il resto è ", a%b) # Il risultato sara: 3
```

Esercizio stupido:

Chiediamo all'utente un numero e diamo come risultato se il numero è pari o dispari:
```Python
try:
    a  = int(input("Introduci un numero intero:\n")) # Si chiede l'input all'utente
    COSTANTE = 2 # stabilisco la costante

    # Controllo se la divisione da resto 0
    if a%COSTANTE == 0:
        print("Il tuo numero è pari")

    else:
        print("Il tuo numero è dispari")

except ValueError as e:
    print("Errore:", e)
```

Funzioni
--
Le funzioni ricevono dei parametri ( argomenti ), separati tra loro da argomenti.
Uno dell'argomento di una funzione può essere il risultato di un'altra funzione.

Vengono eseguite prima le funzioni interne.

```Python
num  = -1E3

print(abs(num)) # Il risultato sara: 1000.0
```

Alcune funzioni incluse in python:

	abs():      restituisce il valore assouluto
	round(x):   arrotonda il parametro
	round(x,y): arrotonda il parametro x con numero cifre decimali pari ad y
	min(x,y,z): Trova il minimo tra i parametri x,y,z per valori numerici, per stringhe invece si usa l'ordine alfabetico
	max(x,y,z): Trova il massimo tra i parametri x,y,z per valori numerici, per stringhe invece si usa l'ordine alfabetico
	
```Python
print(min(4,6,8,9)) # Il risultato sara: 4
print(max(4,6,8,9)) # Il risultato sara: 9

print(min("malo","chico")) # Il risultato sara: chico
print(max("malo","chico")) # Il risultato sara: malo

#ATTENZIONE - Le maiuscole cambiano il risultato, Maiuscola < minuscola
print(min("Malo","chico")) # Il risultato sara: Malo
```

Una funzione di quelle incluse è len(), da come risultato la lunghezza della stringa.

```Python
nome = input("Inserisci il tuo nome: ")
print(nome)

cognome = input("Inserisci il tuo cognome: ")
print(cognome)

print("Ciao",nome,cognome)
print("Il tuo nome è lungo",len(nome))
print("Il tuo nome completo è lungo",len(nome+cognome))
```
##### Print()

Come faccio a scrivere una print senza andare a capo?

```Python

print("Il tuo nome completo è lungo ", end="")
print("7") # Il tuo nome completo è lungo 7
```
 al posto della ""  si puo inserire anche una serie di caratteri:

```Python

print("Il tuo nome completo è lungo ", end="7")
 # Il tuo nome completo è lungo 7
```

Pacchetti da importare
--

Quando si fa import le librerie vengono inserite in una particolare locazione di memoria.
### Pacchetti installati con python

Un esempio di questi moduli è #math.
Ci sono due modi per importare, si puo importare la funzione, per esempio:

```Python
from math import sqrt

num = 4

print(sqrt(4)) # Il risultato sara: 2.0
```

Si puo importare piu di una funzione, elencandole con la virgola:

```Python
from math import sin, cos, trunc, pi

print(pi) # Il risultato sara: 3.141592653589793
```

Importare tutto diventa pesante, quindi non bisogna fare from math import *. Ma solo quello che serve.

Cambio di notazione.

Si puo anche importare il pacchetto:

```Python
import math # si puo mettere as m

print(math.pi) # Il risultato sara: 3.141592653589793
```

In questo modo diremo a python che useremo le funzioni come se fossero oggetti.

Altri funzioni di math:

	-trunc(x):  Taglia la parte frazionaria
	-cos(x)
	-sin(x)
	-floor(x): Restituisce l'approssimazione per difetto
	-ceil(x): Restituisce l'approssimazione per eccesso

Esempi di differenza tra floor, ceil e trunc:

```Python
import math as m

a = 7.87

print(m.trunc(a)) # 7

print(m.floor(a)) # 7

print(m.ceil(a)) # 8
```

Si pens che floor e trunc funzionano allo stesso modo ma con i numeri negativi si nota la differenza:

```Python
import math as m

a = -7.87

print(m.trunc(a)) # -7

print(m.floor(a)) # -8

print(m.ceil(a))  # -7 
```

### Errori d'arrotondamento

```Python
price = 7.87
quantity = 100
total = price * quantity

#Il risultato dovrebbe essere 787.00
print(total) # 786.999999994
```

2 valori sono uguali in base ad una tolleranza, quando si vuole confrontare 2 valori molto simili, si usa math.isclose(a,b):

```Python
import math as m

price = 7.87
quantity = 100
total = price * quantity

#Il risultato dovrebbe essere 787.00
print(total) # 786.999999994
```
