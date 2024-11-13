# Lezione 2 - Metrology e Monitoring

#### Metrology
**Definizione**: la metrologia è la scienza delle misure e dei pesi. Anche se è una disciplina con molti tecnicismi, in questo corso ci concentreremo sugli aspetti fondamentali senza approfondire i dettagli tecnici.

  - *Esempio*: una sonda caduta su Marte a causa di un errore nelle misure (due team usavano sistemi metrici diversi).
  
#### Misura
 **Definizione**: processo di ottenimento di una o più misure di una quantità, associabili ragionevolmente alla quantità stessa. Obiettivo: determinare la misura del **misurando** (oggetto della misura).

**Elementi necessari**:
  - **Descrizione del misurando**: importante definire cosa si misura specificamente.
  - **Metodo di misurazione**: la procedura per misurare.
  - **Strumento di misura affidabile**: deve essere ben utilizzato e calibrato.
  
  *Esempio*: misurazione della temperatura corporea - un termometro deve essere tarato per evitare errori (es. il termometro potrebbe raffreddare il corpo).

#### Intrusiveness
**Definizione**: la capacità di un metodo di misura di modificare il valore che intende misurare.

**Problematicità**: in un sistema complesso come un sistema operativo, è difficile evitare l'intrusiveness; anche un monitoraggio indiretto può alterare le misure.

**Risultato della Misura**: insieme di valori attribuiti a un misurando. Un risultato può includere informazioni aggiuntive sulla misura stessa.

Caratteristiche di una Misura:
- **Precision**: vicinanza tra misure ripetute dello stesso oggetto.
- **Accuracy**: vicinanza tra la misura effettuata e il valore vero.
- **Resolution**: la più piccola variazione di misura rilevabile.
- **Repetability**: facilità con cui una misura può essere ripetuta.
- **Time**: Tempo impiegato per eseguire la misura.

Un misura spesso ha problemi che possono portare a degli errori.
 - **Errore di Misura**: differenza tra la misura effettuata e il valore vero.
  - **Systematic Error**: errore costante o prevedibile, dovuto a strumenti mal calibrati. Può essere corretto.
  - **Random Error**: errore imprevedibile e non correggibile.

*Nota*: Gli errori casuali (random) rendono impossibile una misura 100% accurata. Tuttavia, in certi contesti (es. giochi) l'incertezza può essere vantaggiosa.

---
#### Monitoring
**Obiettivo**:  monitorare costantemente il sistema in esecuzione nel suo ambiente finale, verificando che il comportamento osservato e le performance rispettino regole ben definite.

Monitoring di solito è fatto sia online che offline. Ed è accostato con **verification** per analizzare i dati raccolti. Quest'ultimi sono raccolti quando il sistema è in esecuzione, tuttavia l'analisi dei dati può essere fatto anche a sistema spento

  - *Esempio*: La scatola nera di un aereo, analizzata offline dopo un incidente.

Il sistema su cui si esegue monitoring è definito **target system**
Questo si usa sia per capire cosa fare nel mio sistema, sia per capire il motivo per cui un sistema potrebbe essere fallito. Se non si esegue *monitoring* allora non si può imparare dai nostri errori. Attraverso la verification si può anche ottenere una valutazione delle **performance** e della **qualità del servizio** nel sistema.

Componenti del Monitoring:
- **Elementi da monitorare**
- **Misure ottenute**
- **Punto di monitoring**: unità centralizzata che processa (in automatico o con l'aiuto di un umano) i dati raccolti e ne estrae informazioni rilevanti.

*Nota*: in ogni sistema operativo ci sarà una forma di monitoring delle risorse. Questo è vero ad esempio per linux o per windows, ma anche per diversi sottosistemi, come il sistema bancario di quasi tutte le banche.

**Problemi Tecnici nel Monitoring**
Ci sono diversi problemi tecnici che possono accadere durante l'utilizzo di un sistema. Questi devono essere identificati e risolti. Ci sono alcuni tipi di problematiche
1. **Identificazione degli eventi e delle misure**
2. **Etichettatura dei dati**: Essenziale per creare banche dati future. Es. sistema sovraccarico: è un malfunzionamento o risponde a molte richieste?
3. **Trasmissione dei dati** al sistema centrale.
4. **Filtraggio e classificazione** dei dati.

**Black Box System**
- **Black Box**: Un sistema che non consente di vedere all'interno, quindi il suo funzionamento è sconosciuto (non monitorabile esternamente).
- **White Box**: Permette di vedere all'interno e monitorare le risorse utilizzate.

**Probes**
I *probe* sono dei processi che permettono di monitorare un sistema in esecuzione. Normalmente i probe in un sistema operativo si trovano a livello utente, possono eseguire system call ma non possono dialogare direttamente con i livelli più bassi rispetto al sistema operativo. Questo comportamento è ottimo, ad esempio, per evitare che un virus possa creare danni irreparabili in un sistema.
Il task manager (o `top`) è integrato nel sistema operativo quindi è in grado di fare alcune analisi più dettagliate sapendo esattamente tutte le chiamate di sistema ed essendo una **white box** rispetto al sistema operativo (ovvero se stesso).
Un sistema di monitoring di solito ha più di un probe, ognuno dei quali monitora una parte diversa.

Fino ad ora abbiamo visto tutti probe che erano a livello software, tuttavia esistono anche probe hardware oppure ibridi.
In alcuni ambiti risulta fondamentale utilizzare probe hardware o ibridi. I probes hardware dimiscono l'intrusività, ma si deve rifare ad un software per stampare i dati. Inoltre l'hardware utilizzato è block box.

 **Tipi di Software Monitoring**
1. **Nel processo monitorato**
2. **Nel sistema operativo**
3. **In un processo probe separato** (utile quando non è possibile accedere al codice sorgente).

*Pro*: Accesso a più informazioni rispetto agli hardware probes.  
*Contro*: Intrusivi nella maggior parte dei casi.
