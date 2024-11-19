### Cicli

while, esempi:

- Stampa tutti i caratteri ASCII dal 32 al 127:
```Python
#codice a carattere chr(2)
i = 32

while i <= 127:
    print(f'{i}: ',chr(i))
    i+=1
```

- con la sleep, riesci a leggere meglio:
```Python
#codice a carattere chr(2)
from time import sleep
i = 32

while i <= 127:
    # print(f'{i} hex {i}: ',chr(i))
    print("codice %d hex %x carattere %s" % (i,i,chr(i)))
    i+=1
    sleep(0.5)
   ```

- Ricevi una stringa, stampa ogni carattere per riga
```Python
stringa = input("Inserisci una stringa:\n")
i=0

while i < len(stringa):
    print(stringa[i])
    i+=1
```

##### Cicli con espressioni booleane

```Python
# si possono inserire 5 valori: null o > 0, se il valore è negativo vuoldire che vuole interrompere. media dei voti
i = 0
n = 5
end = False
somma = 0

while i < n and not end:

    voto = int(input("Inserisci il voto da sommare o -1 per terminare: "))
    if voto <= 0:
        end = True
    else:
        somma += voto
        i += 1

#Controllare che non si divida per 0
if i != 0:
    print("La media è: %.2f\n" % (somma/i))
else:
    print("Nessun voto inserito\n")
```

**Non usare break e continue.**

#### Hand-Tracing dei cicli

- Dato un numero in decimale, trasformalo in binario
```python
#Binaria
n = 1729
total = ""
binario = ""

while n > 0:
    digit = n % 2
    total = total + str(digit)
    n = n // 2

print(total)
print(total[::-1])

#OPPURE
i = len(total) -1

while i >=0:
    print(total[i], end="")
    i -= 1
```

#### Variabili sentinella

È una variabile che si usa per controllare il numero di iterazioni di un ciclo.
una variabile sentinella puo anche essere una 'flag'.

### Somma e Media di n valori

### Contare n valori

Quante lettere maiuscola ci sono, quante lettere minuscole ci sono, cifre e caratteri di spaziatura.
In fondo stampa una statistica con l'etichetta e il valore.

```python
string = input("Inserisci una stringa qualsiasi:\n")
lettereG = 0
lettereg = 0
cifre = 0
spazi = 0
i = 0

while i < len(string):
    if string[i].islower():
        lettereG +=1
    elif string[i].isupper():
        lettereg +=1
    elif string[i].isdigit():
        cifre += 1
    elif string[i].isspace():
        spazi += 1
    i += 1
  
# Nelle f-string si usa < > per allineare a destra o a sinistra
etichetta = "Lettere minuscole:"
etichetta1 = "Lettere maiuscole:"

print("La tua stringa contiene:\n")
print(f"{etichetta:<20s} \t{lettereg:3}")
print(f"{etichetta1:<20s} \t{lettereG:3}")
print("%-20s \t%3d" % ("Cifre:", cifre))
print("%-20s \t%3d" % ("Spazi:", spazi))
```

## Ciclo for

Funziona solo sui dati di tipo container, permette di estrarre un dato alla volta, in funzione della posizione del dato nel container.
- Esistono diversi tipi di cicli:
### For i in range
```python
# Si puo creare un contenitore anche con range, che contiene numeri da 0 al numero compreso
for i in range(10):
    print(i)
```

Puo ricevere 2 valori, in quel caso il primo sarebbe il primo da cui parte.
Nel caso in cui inserisco 3 valori indico anche il passo.

```python
# Stampa i numeri dispari
for i in range(1,11,2):
    print(i)
```
### For item in list

```python
stringa = "Stringa"

for i in stringa:
    print(i, end="")
```

### For i , item in enumerate(list)

```python
# enumerate permette di vedere anche l'indice dell'elemento
for pos,stringa in enumerate(stringa):
    print(pos,stringa)
```
