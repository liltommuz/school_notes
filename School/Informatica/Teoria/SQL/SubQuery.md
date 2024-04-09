Le *`SubQuery`* sono delle Query che vengono utilizzate all'intero delle `WHERE`.
Esse sono utili per utilizzare il risultato della **SubQuery**, come in questo esempio.

Voglio trovare trovare la `città` dove atterrerà l'aereo che possiede il numero maggiore di passeggeri.
```sql
SELECT V.CittaPartenza AS Citta
	FROM Volo AS V JOIN Aereo AS A 
	ON A.TipoAereo = V.TipoAereo
	WHERE A.NumeroPasseggeri = (
		SELECT MAX(NumeroPasseggeri) FROM Aereo -- Questa è una SubQuery
	);
```

La *`SubQuery`* può essere utilizzata all'interno delle `SELECT`, `WHERE`, `UPDATE` e `DELETE`.
Si possono utilizzare anche gli operatori di comparazione \[`<`, `>`, `=`,`IN`, `ANY`, `ALL`]
