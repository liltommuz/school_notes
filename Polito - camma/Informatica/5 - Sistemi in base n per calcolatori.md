Sistemi in base n per calcolatori
--

base elevata alla sua posizione.

10000000 in binario = 1 * 2^8 = 256 in decimale

252 = 2 * 10^2  + 5 * 10^1 + 2 * 10^0

Se la cifra meno significativa è 1 allora è dispari, se è 0 è pari

---
In informatica:

Kilo    = 2^10
Mega = 2^20
Giga   = 2^30

201 in base $5 = 2 * 5^2 + 0* 5^1 + 1 * 5^0 = 25 + 0 + 1 = 26$

1 byte = 8 bit = 256
1 word = 2 byte = 16 bit = 65 536
### Trasfomare un valore da decimale ad altra base

divido ripetutamente per la base di cui voglio, prendo i resti delle divisioni in senso inverso mi fermo quando il numero è nullo, quindi non piu divisibile.

#Esempio

11 in decimale = $11/2$ = 5 resto *1*, $5/2$ = 2 resto *1*, $2/2$ = 1 resto *0* , $1/2$ resto *1*

percio in binario sarà uguale a 1011

Esercizi:
- 19 decimale -> rappresentazioni in base 2 e 5

*Base 2* = 19/2 = 9 resto 1, 9/2 = 4 resto 1, 4/2 = 2 resto 0, 2/2 = 1 resto 0, 1/2 resto 1 = 10011
*Base 5* = 19/5 = 3 resto 4, 3/5 resto 3 = 34

---
###### Per convertire da base qualunque si passa da base 10.

Se avessi 34 in base 5 e lo volessi portare in base 2 dovrei:

- 34 -> 19 in base 10 -> 10011 in base 2

---
#### MSB e LSB

Data una sequenza di bit, il bit piu a sinistra si chiama #MSB e quello piu a destra #LSB.

- LSB = Least Significant Bit
- MSB = Most Significant Bit

---
#### Somma in Binario

0 + 0 = 0
1 + 0 = 1
0 + 1 = 1
1 + 1 = 0 + riporto sulla cifra di peso superiore

0011 + 0110 = 1001 -> 0011 = 3, 0110 = 6 --> 1001 = 9

	0011 +
	0110 =  --> 0 + 1 = 1, 1 + 1 = 0, 1+1 = 0, 1+0 = 1
	1001

---
#### Sottrazione in Binario

0 - 0 = 0
1 - 0 = 1
0 - 1 = 1
1 - 1 = 0 + prestito dalla cifra di peso superiore

	   1000 -
	    1 =  --> 0 - 1 = 1, 0 - 1 = 1, 0 - 1 = 1, 1-1 = 0
	   0111

---
#### Risultati delle operazioni

#Overflow L'impossibilità di rappresentare il risultato sul numero di bit dati.

N = 4

	1010 +
	1000 = 
	0010 --> Il risultato sarebbe 10010, un bit in più
	
In C gli interi occupano in genere 32 bit, = $2^{31} -1$ = 2147483647, se sommo 1 si azzera la variabile, il processore ha un registro dei flag, si alza quella di overflow.

In python non c'è questo problema, adatta in automatico in modo che non ci sia overflow.

--- 
#### Sistema Ottale ed Esadecimale

101001101100 in binario, *se bisogna convertirlo in base 8 non è necessario passare dalla base 10*

La base 8 utilizza le cifre da 0 a 7.
8 = 2^3
Posso passare dalla base 2 alla base 8 raggruppando le cifre in gruppi di 3.

101 001 101 100 -> Ognuno di questi blocchi rappresenta una cifra della rappresentazione ottale

101 = 5
001 = 1
101 = 5
100 = 4

in ottale equivale a 5154.

se manca una cifra o 2 aggiungo 2 0 a sinistra 1010 -> 001 010

##### Operazione contraria

6528 ottale in decimale 

6 = 110
5 = 101
2 = 010
8 = 110

##### Esadecimale

Si mette il pedice #h
per convertire da base 2 a base 16 si raggruppano le cifre a blocchi di 4, se mancano cifre si aggiungono 0 a sinistra.
In esadecimale le cifre da 10 a 15 sono : 

- A -> 1010
- B -> 1011
- C -> 1100
- D -> 1101
- E -> 1110
- F -> 1111

101001101100

101 001 101 100 -> Ognuno di questi blocchi rappresenta una cifra della rappresentazione ottale

1010 = A
0110 = 6
1100 = C