ASCII
--
American Standard for Coding Information Interchange.
Tutti gli strumenti che utilizzano ascii si capiscono.

32 caratteri di controllo, non stampabili, servono per formattare la stampa.
Gli altri sono caratteri che comprendono tante altre cose, ma non lettere accentate ed altre cose.

```Python
print("ok")
```

chr() e ord() servono ad ottenere i codici ascii o al contrario:

```Python
print(chr(64))  # stampa: @

print(ord("@")) # stampa: 64
```
---
#### Utilizzare gli oggetti python

Tutti i valori in python sono oggetti, ogni oggetto ha i suoi metodi.
Metodi delle stringhe:

```Python
name = "John Smith"

uppercase_name = name.upper() # Lo rende uppercase

lowercase_name = name.lower() # Lo rende lowercase

replaced_name = name.replace("S","O") # Lo rende: "John Omith"
```
Cosa fanno upper e lower?

Trasformo la lettera in codice con chr() , controllo se il carattere è tra le lettere in minuscolo, se è cosi, allora sommo la differenza tra i 2, continuo per ogni carattere.

---
##### Funzioni e Metodi

Le #funzioni sono generiche e accettano argomenti di diverso tipo, i #metodi sono specifici rispetto all'oggetto.
Non si puo fare questo:

```Python
num = 9

uppercase_name = name.upper() # ERRORE
```
Le #Funzioni sono chiamate direttamente, con un elenco di parametri mentre i #metodi sono chiamate nome_oggetto.metodo().
Sia le #funzioni che i #metodi possono ritornare un valore.

#### Sequenze di escape

Il carattere successivo viene interpretato diversmìamente.

```Python
print("He said \ "Hello\"") # He said "Hello"
```

Ci sono differenze tra codici a 32 bit e a 16 bit.

---
#### Output Formattato

Inserire valori all'interno delle stringhe:

- **Concatenazione di stringhe**
- **f-String**
- *%*
- *.format()*

```Python
int = 2

print("IL numero è" +str(int))
print(f"IL numero è {int}")
print('IL numero è %f' % (int)) # %d -> Interi, %f -> Float, %s -> stringa
print("IL numero è {a}".format(a=int))

#Output uguale

print(f"{int=}") # int=2
```
---
#### Specificatori di formato

è possibile modificare il formato in cui vengono stampati i valori con gli specificatori di formato.

- : , serve a separare il valore
- Allineamento , < sinistra, > destra, ^ accentra
- + o - o spazio ,  serve a rappresentare il segno degli operandi
- #, formato in codice alternativo
- Ampiezza, stampa su 20 caratteri
- Carattere di raggruppamento delle migliaia: , oppure _
- "." o "precisione"

```Python
a = 123.454

# stampa 10 caratteri, se non ci sono riempe con spazi vuoti
print(f"a vale {a:10.3f}") 123.454

```
###### Stampare un valore con un certo numero di cifre

```Python
a = 7.000

print(round(a,3)) #Restituisce la cifra ma gli 0 non li fa vedere, 7

print(f'{a:8.3f}') # In questo caso farebbe vedere anche gli 0, 7.000, 8 caratteri di cui 3 dopo la virgole.
```

##### Forma alternativa

**%#x** --> stampa in modo alternativo il valore

```Python
b = 170

print("%#x"%(b)) # In esadecimale, 0xaa, 0x significa esadecimale

```

##### Placeholder

```Python
a = 7.000

b = 170

print("Il valore intero vale %d, il valore float vale %f"%(b,a))

print("%x"%(b)) # In esadecimale

#Il valore intero vale 170, il valore float vale 7.000000
#aa
```
---
### Decisioni

#### Istruzione if

Costrutto di scelta, istruzione di controllo di flusso, permette di eseguire un blocco o un altro a seconda che si verifiche una certa condizione.

- If
- Else

Esempio #Ascensore

```Python
piano = int(input("Inserire il numero del piano\n"))

#while piano == 13:
#	piano = int(input("Reinserire il numero del piano\n"))

if piano == 13:
	print("Il piano 13 non esiste")
else:
	# Non esiste il tasto 13, percio se si clicca 14 si va al 13 e cosi via
	if piano > 13:
		piano += -1

print(f"Arriverai al piano {piano}")
```

Esiste anche la if che fa solo una cosa senza else.

### Approssimazione

Epsilon sara un valore estremamente piccolo che decido io.

math.isClose() -> Ti dice che sono simili fino a 10^-9

```Python
import math

#Se mettessi == sarebbe sbagliato
r = math.sqrt(2.0)
if math.isclose(r*r, 2.0)
	print("sqrt(2.0) al quadrato è uguale a 2")
else:
	print("sqrt(2.0) al quadrato non è uguale a 2")
```

Ordinare alfabeticamente in ordine crescente 3 nomi introdotti da tastiera

```Python
nomi = []
Nrichieste = 3

for i in range(Nrichieste):

    nome = input(f"Inserisci il {i+1} nome da tastiera\n")
    while nome.isdigit():
        nome = input(f"Reinserisci il {i+1} nome da tastiera\n")

    nome = nome.lower()
    nomi.append(nome)

nomi.sort()

print("\nElenco ordinato alfabeticamente\n")
for i in range(Nrichieste): print(f"{i+1}: " + nome)
```

