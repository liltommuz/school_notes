### Notazione in modulo e segno (MES)

MSB Rappresenta il segno.
	0 -> +
	1 -> -
n-1 bit -> Modulo

#Esempio

N = 5
$01011_{MES}$
Lo 0 iniziale significa +. il numero sarà $2^3 + 2^1 + 2^0= +11$

---
_Problemi_

- ** Problema 1**
N = 6 

100000        000000

Il primo è -0, il secondo è +0. 

 > Doppia rappresentazione dello 0

- ** Problema 2**
N = 5

A = 01010
B = 00111

	0|0010 +
	0|0111 = 
	0|1001

Sommando due valori positivi anche il risultato dovrà essere positivo.
E poi si somma il modulo

Nel caso in cui uno è positivo ed uno è negativo, dovrò prima capire quanto è grande il modulo per capire il segno finale.
L'operazione in questo caso è la sottrazione, ma all'interno del modulo.
$$
{\text {-2 e 7 --> }} |2-7| * {\text {segno del numero piu grande in modulo}}
$$
> Operazioni complesse
> 
> Nota: Qual è l'intervallo di rappresentabilità?
> 
> 	Il numero piu grande è: +2^n-1 -1
> 	Il numero piu piccolo è: -2^n-1 -1
> 	
> L'intervallo di rappresentazione è 31, perchè una rappresentazione è sprecata per il doppio 0.

---
### Codifica in complemento a 2

il MSB ha peso negativo (-2^N-1

#Esempio 

N = 5 bit

01011 CA2 ->$-0 * 2^4 +2^3+2+1 = + 11$

10110 CA2 -> $-1 * 2^4 + 2^2 + 2  = - 10$

>Nota: Qual è l'intervallo di rappresentabilità?
> 
> 	Il numero piu grande è: $+(2^{N-1})  -1$
> 	Il numero piu piccolo è: $-2^{N-1}$
>
>		 $-2^{N-1} <= x <= +(2^{N-1})  -1$
>
> L'intervallo di rappresentazione è 32.

---
### Convertire in complemento a 2

Convertire da base 10 a complemento a 2, si usa la stessa regola che permette di convertire da base 10 a base 2.

+9 --> 1001
-9 come si rappresenta?

- si parte dal corrispettivo positivo, 
- si prende la rappresentazione in base 2
- si scambiano gli 0 e gli 1
- si somma 1

1. Passo 1-2
		+9 --> 01001
		
2. Passo 3
		10110
		
3. Passo 4
		10110 +
			1 =
		10111 CA2

#Esercizio

*Consegna*
>N = 6 bit
>(-17) = CA2

	+17 -> 010001
	poi 101110 + 1 = 101111 CA2
	percio -17 = 101111 CA2

Controlliamo:

	-2^5 + 2^3+ 2^2 + 2 + 1 = -32 + 8 + 4 + 2 + 1 = -17


>In complemento a 2, che tu stia facendo una somma o una sottrazione, consideri sempre la somma di tutti i bit.
>
>	A - B -> A + CA2 (B)


>**Nota**: Si ottiene overflow, quando sommando due operandi di segno concorde, si ottiene un operando di segno discorde.
	 15 + 1.        *Esempio sotto*

---
### Rappresentazione a Virgola fissa

01011, 011 --> dopo la virgola c'è la parte frazionaria
5 bit per la parte intera e 3 per la parte frazionaria.

01011 -> $2^3 + 2^1 + 2^0$ 
011     -> $2^{-2} + 2^{-3}$

#Esempio 

1101,01 = 13,25
poichè la parte intera è 1101 = 13 e la parte frazionaria 01 = $0 * 2^{-1}+1 * 2^{-2} = 1/4$ 

> E al contrario??

A = 7,125

la parte intera è uguale, 111
la parte frazionaria invece bisogna moltiplicare per 2, e bisogna prendere le cifre che stanno dopo la , ripeto finche non ottengo 0 nella parte dietro la virgola.

0,125 * 2 = 0,250

prendo lo 0.

0,250 * 2 = 0,500

prendo lo 0

0,500 * 2 = 1,000

Mi fermo e ottengo 001

7,125 = 111,001

>*Problemi*

Ci sono alcuni valori reali, che non sono rappresentabili in binario su un numero finito di cifre.
per esempio 0,3.

>Da qui derivano alcuni errori di approssimazione, poiche i calcolatori lavorano con numeri finiti di cifre.

- La **Virgola Fissa** non è flessibile
	- Il valore più piccolo è tutti 0
	- Il valore più grande è tutti 1
---
### Rappresentazione a Virgola mobile

Serve un segno, l'esponente e la mantissa.
- Float    -> Singola precisione, 32 bit = 1 per il segno, 8 per l'esponente e 32 per la mantissa
- double -> Doppia precisione 64 bit = 1 per il sergno, 11 per l'esponente, 52 bit per la mantissa

La mantissa decide la precisione.
L'esponente cambia l'intervallo, più grandi a 64 bit.

>I calcoli in doppia precisione sono piu lenti ed occupano molto spazio.
>I valori float di #python sono in **doppia precisione**.

In python se vado nell'intervallo di overflow diventa + o meno infinito, mentre se vado nell'underflow rappresenta 0.

--- 
### IEEE-754 SP

standard in singola precisione, permette di rappresentare valori fino a $-10^{38}$ e $10^{38}$, con una precisione di $10^{-38}$.

- OVERFLOW (NaN)
	Avviene l'overflow quando il valore è troppo grande o troppo piccolo per essere rappresentato.

Inoltre i valori che stanno all'interno della precisione, si chiamano #Underflow.

>Underflow (0) si verifica se sto facendo un'operazione ed il risultato di un'operazione A+B = A con B diverso da 0.
>Il numero è talmente piccolo che viene ignorato.

*Problema*

>Nelle zone underflow e overflow, le proprietà delle operazioni non sono più valide.

---
Esercizio su Complemento a 10:

- N = 5 bit, A = 13, B = 7

A - B =  A + CA2(B)

A = 01101
B = 00111
CA2(B) = 11001

	01101 +
	11001 = 
	100110 --> Pero essendo che lavoro su 5 cifre, la prima non la prendo
	
	= 00110

00110 = 6

---
Esempio di overflow:

- 5 bit, A = 15, B =1

A + B

	01111 +
	00001 =
	10000

Ho ottenuto -16, sommando due valori positivi, +15 e +1.

*Oppure*

 5 bit, A = -16, B =-1

A + B

	10000 +
	11111 =
	01111

Ho ottenuto +15, sommando due valori negativi, -16 e -1.

---
Esercizi fatti nell'intervallo:

1. Elemento rappresentato maggiore in modulo, controllando MES e CA2.

N = 5 bit

A = 10011
B = 11001
C = 00001

- MES
	A = -3
	B = -9
	C = 1
Il più alto in modulo è B.

- CA2
	A = -13
	B = -16 + 8 + 1 = -7
	C = 1
Il più alto in modulo è A.

2. Converti prima in MES e poi in CA2

N = 5 bit

A = 01001
B = 10110

- MES
	A = + 9
	B =  - 6
Convertito in MES.

- CA2
	A = +9
	B = -16 + 6 = - 10
Convertito in CA2.


3.  Somma e sottrai in CA2

N = 5 bit

A = 00011 CA2
B = 01111 CA2
C = A + B
D = A - B

- CA2
	C
	
		00011 +
		01111 =
		10010
	C = 10010 = - 16 + 2 = -14
	
	D

		10000 +
		    1 =
		10001
CA2(B) = 01101

		00011 +
		10001 =
		10100
D = -16 + 4 = -12
Il primo è overflow, il secondo no.

# Allegati

link utile: https://float.exposed/0x44bf9400
