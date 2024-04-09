La normalizzazione é una tecnica di design utilizzata per la progettazione logica di un database.
Essa si divide in 4 parti differenti, chiamate **Regole di Normalizzazione**.

Queste norme sono utili per evitare la ridondanza di dati e anomalie di inserimento, aggiornamento e cancellamento. Le tabelle vengono divise in tante tabelle più piccole unite dalle relazioni.

Adesso parliamo delle anomalie che possiamo incontrare lungo la creazione di un database.
Come esempio andremo ad utilizzare la seguente tabella:
![[TabellaAnomalie.png]]

- #### Anomalia di Inserimento
Prendendo come esempio un nuovo assunto, che deve essere allenato sul lavoro che dovrà svolgere in futuro, non avrà una mansione fissa, quindi nel caso la colonna `Emp_Dept` avesse come regola il `NOT NULL`, riscontreremo un'anomalia di inserimento. Quindi la corretta modalità di creazione della tabella, nello specifico della colonna `Emp_Dept` bisognerà omettere la regola che vieta di lasciare il campo vuoto.

- #### Anomalia di Aggiornamento
Le anomalie di aggiornamento avvengono quando proviamo a modificare alcuni dati all'interno del database, senza provocare l'inconsistenza dei dati. Nella tabella d'esempio l'impiegato `Rock` è stato inserito 2 volte, essendo che è assegnato a 2 dipartimenti differenti. Quindi se dovessimo aggiornare un suo qualsiasi dato, noi dovremmo aggiornare 2 righe al posto di una singola.

- #### Anomalia di Cancellamento
Questa anomalia si verifica quando proviamo a cancellare un dato che a noi non serve più, ma nel farlo cancelliamo altri dati significativi. 
Nel caso dell'esempio, se il dipartimento numero 12 dovesse cessare di esistere, e andando a cancellare dove nel database ci sia il dipartimento numero 12, andremo a cancellare anche dati utili di alcuni impiegati.

Per evitare queste anomalie esistono diverse regole che sono le seguenti:
- Prima Forma Normale
- Seconda Forma Normale
- Terza Forma Normale
- Boyce-Codd Forma Normale
- Quarta Forma Normale
- Quinta Forma Normale
- Sesta Forma Normale

Ora andremo ad analizzare nel dettaglio le prime 4 regole.

# Prima Forma Normale

La prima forma di normalizzazione consiste nel creare una tabella che contiene un solo valore per ogni dato e che ogni dato sia unico.
Nel caso andiamo a creare una tabella con la colonna `NomeCompleto`, questa regola verrebbe infranta, essendo che sono presenti 2 dati in un solo campo.
Un'altra regola della prima forma normale e quella che ogni riga deve contenere dati unici.

# Seconda Forma Normale

Per applicare questa forma, il database deve essere impostato secondo le norme della **Prima Forma Normale**, 