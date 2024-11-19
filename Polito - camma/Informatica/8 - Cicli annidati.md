#### Matrici

Le matrici sono strutture a piu dimensioni, quella piu semplice è bidimensionale.

```Python
i = 32

while i <= 127:
    print(f'{i}: ',chr(i))
    i+=1
```

## Cicli annidati

Dentro i cicli si possono costruire altri cicli, si utilizzano bene per controllare tabella, come le matrici.

Stampa l'albero:
```python
x = 1
k = 10
COST = 5

for i in range(k):
    s = f"x^{i +1 }"
    print(f"{s:^{k}}|", end="")

print()

for i in range(COST * k):
    print("-", end = "")

print()

for i in range(k):
    for j in range(k):
        s = x**(j+1)
        print(f"{s:>{k}}|", end="")

    print()
    x += 1
```

- Disegna un cerchio di asterischi
chiedi il raggio, e in base al raggio provi ad apporossimare la forma circolare con asterischi:

\esercizio


### Numeri casuale e simulazioni

Non si calcolano tutte le possibili soluzioni, ma campionano lo spazio delle possibili soluzioni cercando di stimare il valore della soluzione.
Serve qualcosa che generi dei valori casuali.
- si usa la libreria random.
#### Random()

Genera un numero compreso tra 0 ed 1 esclusi.

```python
import random

n = random.random() # restituisce un numero tra 0 ed 1 esclusi

```
#### Randint()

Genera un numero intero nell'intervallo dato.

```python
import random

n = random.randint(1,6) # Dara un numero intero tra 1 e 6 compresi.
```

#### Approssimazione pi greco

```python
import random

TRIES = 1000
hits = 0

for i in range(TRIES):

    r = random.random()
    x = -1 + 2*r

    r = random.random()
    y = -1 + 2*r
    
    #OPPURE 
    # x = random.uniform()

    if x * x + y * y <=1:
        hits += 1

pi_estimate = 4.0 * hits/TRIES
print("Estimate for pi: ", pi_estimate)
```

#### BlackJack

Abbiamo solo carte da 1 a 10, l'asso vale sempre 1, c'è solo un giocatore contro il banco.
Se fai piu di 21 vince il banco e vince anche se fa piu di te.
Se la somma è < 17 il computer non sta mai, se la somma è = 17, il computer si ferma, se fa piu di 21 vince l'utente.
Il banco da una carta e la fa vedere, il banco ti da una seconda carta te le fa vedere e tu scegli se andare avanti.

```python
#BlackJack
import random

carta_banco = random.randint(1,10)
totale_banco = carta_banco
print("Carta_banco: ", carta_banco)

carta_player_1 = random.randint(1,10)
carta_player_2 = random.randint(1,10)
totale_player = carta_player_1 + carta_player_2

print(f"Carta 1: {carta_player_1}, carta 2: {carta_player_2}\nTotale: {totale_player}")

perso = False
carta = input("Vuoi una carta? Y/N\n")

if carta == "Y":
    carta = True

else:
    carta = False


while not perso and carta:

    new_card = random.randint(1,10)
    totale_player += new_card
    print(f"New_card: {new_card}\nTotale {totale_player}")

    if totale_player > 21:
        perso = True

    else:
        carta = input("Vuoi una carta? Y/N\n")
        if carta == "Y":
            carta = True

        else:
            carta = False

  

if not perso:
    while totale_banco <= 17:
        new_card = random.randint(1,10)
        totale_banco += new_card

        print(f"New_card: {new_card}\nTotale {totale_banco}")

    if totale_banco > 21:
        print("HAI VINTO")

    elif totale_player > totale_banco:
        print("HAI VINTO")

    elif totale_player <= totale_banco:
        print("HAI PERSO")
else:
    print("HAI PERSO")
```
