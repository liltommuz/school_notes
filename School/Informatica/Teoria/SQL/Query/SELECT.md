La `SELECT` é utilizzata per prendere i dati dal database.

La sua sintassi é la seguente:

```sql
SELECT [Colonna_1, Colonna_2, ...]
	FROM [Tabella_1, Tabella_2, ...];
```

Dopo `SELECT` possono inserire i nomi delle colonne delle quali desidero ricavare i dati ad esempio

```sql
SELECT Nome, Cognome FROM Alunno;
-- Output
-- | Nome    | Cognome     |
-- | Tommaso | Fatticcioni |
```

In questo caso mi interessava conoscere solamente il nome e il cognome degli alunni registrati nel database. Però prendiamo come esempio il caso noi abbiamo la necessità di conoscere tutti i dati degli alunni, ovviamente non andremo a scrivere il nome di ogni colonna, sarebbe una perdita di tempo e un lavoro inutile, quindi andremo ad utilizzare il simbolo *`*`* che indica tutte le colonne presenti nella tabella.

```sql
SELECT * FROM Alunno;
-- Output
-- | Nome    | Cognome     | Data_Nascita | Eta |
-- | Tommaso | Fatticcioni | 05-04-05     | 18  |
```

