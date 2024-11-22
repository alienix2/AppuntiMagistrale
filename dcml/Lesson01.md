# Lezione 1 - Concetti di Base

## Sistema

**Definizione Generica**: In questo corso, considereremo un **sistema generico**, con un focus particolare sui **sistemi cyber-fisici**. Tuttavia, per ora, manteniamo il discorso generale.

Il sistema si trova tra l'hardware e l'applicazione. La gestione dei driver può variare in base al sistema operativo: a volte i driver sono inclusi nel sistema operativo, altre volte no.

**Applicazioni Tolleranti ai Fallimenti**: 
  - Alcune applicazioni possono fallire senza creare problemi gravi (es. un gioco sul telefono).
  - Altre applicazioni non possono fallire in nessun caso (es. il controllo automatico della velocità su un aeroplano). In questo secondo caso, è essenziale che il software sia progettato per evitare problemi o, se accadono, per limitarne le conseguenze.

**Requisiti Critici**: Esistono requisiti che riguardano la capacità di un'applicazione di evitare il fallimento. Altri, invece, riguardano altri aspetti come confidenzialità, sicurezza, ecc. Questo insieme di requisiti prende il nome di **dependabilities del software**.

- **Validazione**: Processo di controllo per verificare se ciò che è stato realizzato corrisponde alle aspettative. (*Il sistema rispetta le specifiche?*)
- **Verifica**: Processo di verifica che il sistema funzioni correttamente. (*Il sistema è realizzato bene?*)

- **Specifica**: descrizione di ciò che il sistema dovrebbe fare.
- **Realizzazione**: descrizione di ciò che il sistema effettivamente fa.

Elementi da validare:
  - **Proprietà funzionali**
  - **Dependability**: Capacità del sistema di evitare fallimenti e, se presenti, di limitarne le conseguenze. 
    - *Esempio*: In un sistema ferroviario, si cerca di garantire che i treni non si guastino frequentemente. E anche se un treno si guasta, il sistema deve evitare conseguenze catastrofiche, come incidenti gravi.

### Funzionamento del Sistema

**Servizio Corretto → Servizio Errato → Ripristino**: Idealmente, il sistema passa dal servizio corretto al servizio errato, ma deve essere in grado di riprendersi (es. ripristino).

  - *Esempio*: In un server con dischi in RAID, se un disco si guasta, viene sostituito con uno nuovo, mentre il sistema continua a funzionare grazie al disco di backup.

**Livelli di Funzionamento**: La definizione di "corretto funzionamento" varia:
  - *Esempio 1*: Un treno è considerato "funzionante" se parte in orario e si ferma dove necessario, o solo se nessuno si fa male a bordo?
  - *Esempio 2*: Un protocollo di rete può essere valutato in base alla gestione dei casi di fallimento, ai tempi di risposta, alla gestione degli errori del disco, ecc. Alcuni aspetti richiedono alti livelli di successo (es. 99.9999%), altri no.
### Proprietà di un Sistema Dependable

- **Availability**: Disponibilità continua del servizio corretto.
- **Reliability**: Continuità del servizio senza interruzioni (es. un aereo non può permettersi neanche un secondo di inattività).
- **Confidentiality**: Garanzia che nessun utente non autorizzato possa accedere alle informazioni.
- **Integrity**: Garanzia che il sistema rimanga integro e inalterato da utenti non autorizzati.
- **Maintainability**: Facilità di modifica e riparazione del sistema.
- **Coverage**: Probabilità che il sistema possa tollerare un problema e continuare a funzionare correttamente. Dipende da alcune delle proprietà precedenti.
- **Safety**: Verrà approfondita più avanti.

Come si ottiene la dependability:
1. **Prevenzione dei Faults**: Se alcuni input possono causare problemi, cerchiamo di prevenirli già durante i test (es. non acquistare software non testato).
2. **Rimozione dei Faults**: Se vedo che degli errori ci sono, li testo e li risolvo.
3. **Tolleranza ai Faults**: Esempio: se ho un incontro importante, imposto più di una sveglia per evitare di non svegliarmi.

Threats, ci sono tre tipi di minacce:
1) **Fault**: Causa uno o più errori.
2) **Error**: Porta a uno o più fallimenti (failure).
3) **Failure**: La conseguenza finale di uno o più errori.
  - *Esempio*: Salta la corrente (fault), provo a riaccendere ma non ci riesco (error), inciampo e cado nel buio (failure).

**Safety**: esistono **failures** che creano pochi problemi e **failures catastrofici**. Un sistema **safety-critical** deve prevenire i fallimenti catastrofici, garantendo la sicurezza di persone, infrastrutture e ambiente.
  - *Esempio*: Se un sistema evita danni alle persone ma causa la distruzione di un bosco, è comunque considerato catastrofico.

**Safety e Availability**

- È possibile ottenere un alto livello di safety senza availability, ma il sistema risulterebbe inutile.
  - *Esempio*: Un treno può fermarsi per motivi di sicurezza, ma così si riduce la sua disponibilità (availability) pur mantenendo alta la safety.


