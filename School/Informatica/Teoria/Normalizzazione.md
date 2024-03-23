
La tabella a cui faremo riferimento a questi appunti é la seguente:
![[TabellaAereoporto.png]]
#### Query per estrarre `citta` che sono servite da `Aereo` che possiedono il numero massimo di passeggeri.


Notiamo che all'interno di questo esercizio ci sono 2 Query differenti che formano una Query.
La parte di query che ci chiede di estrarre le `citta` é l'obiettivo dell'esercizio, mentre nella seconda parte, chiamata [*`SubQuery`*](SubQuery) , ci chiede di trovare il numero massimo dei passeggeri dell'aereo.

Per trovare il numero massimo di passeggeri utilizzeremo la `SELECT`:
```sql
SELECT MAX(NumPasseggeri) FROM Aereo;
```

Questa Query è quella che chiamiamo *`SubQuery`*.

La parte principale della Query invece sarà strutturata in questa maniera con l'utilizzo di una `Join`:
```sql
SELECT V.CittaPart AS Citta
	FROM Volo AS V JOIN Aereo AS A 
	ON A.TipoAereo = V.TipoAereo;
```

Adesso per unire queste 2 query basta utilizzare una `WHERE`:
```sql
SELECT V.CittaPart AS Citta
	FROM Volo AS V JOIN Aereo AS A 
	ON A.TipoAereo = V.TipoAereo
	WHERE A.NumPasseggeri = (
		SELECT MAX(NumPasseggeri) FROM Aereo
	);
```
