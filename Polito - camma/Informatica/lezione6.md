#### Operatori logici booleani

#and Prodotto logico --> ha precedenza sull'or
#or   Somma logica
#not Negazione logica --> Precede gli altri 2

nand e nor sono legati agli altri. sono i complementari della or e della and.
##### ex-or
or esclusivo,
questo operatore restituisce vero solo quando gli operandi in ingresso sono diversi.
ex-nor, è la ex-or negata, la complementare.
##### espressioni booleane

combinazione di proposizioni e condizioni booleane.
Esempio di #and:

```Python
temperatura = float(input("Inserire la temperatura attuale:\n"))

#AND
if 100 > temperatura > 0: # si puo scrivere cosi: temperatura > 0 and temperatura < 100
    state = "liquida"

elif temperatura >= 100:
    state = "gassosa"

else:
    state = "solida"

print(f"L'acqua è {state}\n")
```

##### Proprietà

- Commutativa

A and B = B and A

- Associativa

A and B and C = (A and B) and C = A and (B and C)

- distributiva

A and (B or C) = (A and B) or (A and C)

- Legge di Demorgan

not(A and B) = not A or not B
not(A or B) = not A and not B
```Python
country = "USA"
state = "AK"

#Non stamperà
if country != "USA" and state != "AK" and state != "HI":
    print("20")
```

esempio di funzione bool()
```Python
# equivale a bool()

def boolean(num):

    return False if num == 0 else True

  

print(boolean(0))

print(boolean(10))
```

#### Metodi stringhe che restituiscono valori

- endswith("somethin") -> Controlla con cosa finisce una stringa.
- s.count("Some") -> Conta quante volte la stringa è contenuta in un nome s
- startswith("Somethin") -> Uguale alla end ma controlla l'inizio
- s.find("Some") -> Cerca la stringa e restitusice l'indice rispetto alla prima occorrenza che trova, se non lo trova restituisce -1

##### Altri metodi

- s.isalnum -> Contiene solo lettere o cifre e non è vuota?
- s.isalpha() -> Contiene
- s.isdigit() -> Contiene un numero?
- s.islower() ->
- s.isspace() ->
- s.isupper() ->



