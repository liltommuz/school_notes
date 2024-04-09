La clausola `WHERE` viene utilizzata per il filtraggio del risultato.
```sql
SELECT [colonna] FROM [tabella] WHERE [condizione];
```

Quando andiamo a scrivere una Query, solitamente si pensa di utilizzare il metodo più efficiente per recuperare le informazioni necessarie, quindi non possiamo selezionare tutti i dati presenti all'intero della tabella. Quindi è qui che entra in gioco la clausola `WHERE` e utilizzata come una `IF` in tutto e per tutto.

```sql
SELECT * FROM Alunno
	WHERE Nome = "Tommaso";
```

In questo esempio stiamo selezionando tutti gli alunni con il nome *Tommaso*, e non tutti gli alunni presenti all'intero del database.

> [!Caution]
> Non possiamo utilizzare le funzioni di aggregazione come `COUNT` o `MAX`.
> Gli unici operatori che possono funzionare sono i seguenti:
> `=`, `>`, `<`, `<=`, `>=`, `<> or !=`, `BETWEEN`, `LIKE`, `IN`
 