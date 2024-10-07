

Una *variabile* è una locazione di memoria
In python si inizializza con una assegnazione:

```Python
variabile = 10 #Definisce la var

variabile = 6 #Soovrascrive la var
```

Variabile VS Costante


Le costanti non dovrebbero mai cambiare durante il programma --> Sono scritte in maiuscolo in python

```Python
COSTANTE = 7
```

Le var non possono contenere alcuni valori, la scelta dell'identificatore è importante per l'intelliggibilità del codice.
Sarebbe meglio che le variabili e le costanti venissero definite in parti precise del codice.

```Python
#Input data
anno = 4
mese = 7

#Costanti
PI = 3.14
```

Tipi di dati
--
Si separano i numeri interi dalla parte Reale con il punto.


Le variabili possono cambiare tipo.

```Python
#Assegnazione a integer
anno = 2024

#Diventa stringa
anno = "2024"

# Diventa float
anno = 20.24
```
Ogni volta che si cambia tipo data, python occupa un altra zona di memoria, distrugge quella di prima e ne crea un'altra.  --> Non è sicuro che un int e una str stiano nello stesso spazio

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

#ATTENZIONE - Le maiuscole cambiano il risultato
print(min("Malo","chico")) # Il risultato sara: Malo
```

