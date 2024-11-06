# Metrology

Dobbiamo ottenere informazioni dal sistema. Apparentemente semplice *Esempio:* apro il task manager e guardo le informazioni, tuttavia, sono in grado di carpire correttamente tutte le informazioni? Cosa vogliono dire le parti che leggo sullo schermo?

**Metrology** è la scienza di misure e pesi.
Ci sono molti tecnicismi dietro la metrology ma in questo corso noi cercheremo di capire di cosa si occupa senza entrare nello specifico.
*Esempio:* Video sulla sonda che è caduta su Marte perchè le due parti che dovevano comunicare non usavano lo stesso sistema metrico per catalogare le loro informazioni. Video sull'utilizzo delle misure nel S.I in un mondo in cui i diversi paesi avevano altre misure.

**Misura:** processo di ottenimento di una o più misure di quantità che possono essere associate in modo ragionevole alla quantità stessa.
**Obiettivo:** determinare la misura del misurando.

**Cosa serve per fare la misura:**
- una descrizione del misurando (può sembrare scontato ma se non si capisce cosa si sta misurando specificamente diventa difficile)
- un metodo di misurazione
- uno strumento di misura affidabile (che deve essere usato correttamente)

*Esempio:* voglio misurare la mia temperatura corporea. Devo definire un sistema di misura e un metodo di misura. Ci sono alcune problematica da tenere di conto, ad esempio se uso un termometro e lo avvicino al mio corpo, ovviamente il corpo diventerà più freddo perchè raffreddato dal termometro, quindi se questo non è ben tarato, mi riferirà una misura errata.
*Esempio:* uso il task manager, il task manager stesso consuma delle risorse quindi può essere che la misura eseguita sul sistema non rifletta quella che è vera a task manager chiuso.

**Intrusiveness** è la proprietà di un metodo di misura di cambiare il valore della misura che vorrebbe effettuare. Ci sono casi in cui questo è impossibile da evitare, in qual caso occorre fare attenzione nella valutazione del risultato letto (*eventualmente compensare in qualche modo*).

*Nota:* in un sistema complesso come un sistema operativo è difficile che una misura possa non avere alcun tipo di intrusiveness anche solo in modo indiretto.
*Other examples:* on the slides examples about measuring power, potential difference, temperature etc.

**Risultato della misura:** insieme di valori attribuiti ad un misurando (uno **o più**)
Un risultato può contenere anche informazioni aggiuntive sulla misura che sta venendo misurata.

**Caratteristiche di una misura:**
- **precision:** vicinanza fra la misura effettuata e la misura effettuata nel passato dello stesso oggetto (non è detto che se la precisione è alta allora sia anche accurata, vedi sotto)
- **accuracy:** vicinaza fra la misura effettuata e la misura vera
- **resolution:** più piccola variazione di misura misurabile (in italiano è precisione, da non confondere con la precision)
- **repetability:** indica quando è facile ripetere la misura. (in alcuni casi ci sono misure impossibili da ripetere del tutto)
- **time:** tempo impiegato per eseguire la misura, a volte ci sono fattori che potrebbero essere influenzati dal tempo.

**Measurement error:** una misura spesso ha problemi che possono portare ad errori di misura. Il punto è che l'errore si misura come differenza fra la misura effettuata e il vero valore dell'oggetto. In questo senso non si riesce a capire qual è l'errore, anche se questo è direttamente legato alla resolution dello strumento.
**Measurement error = Systematic error + random error**
**Systematic error:** è l'errore che non cambia mai fra le differenti misure effettuate con uno strumento o cambia in modo prevedibile. Può essere causato da uno strumento calibrato male oppure errori nella lettura (o in generale dalla resolution dello strumento). L'errore sistematico può essere calcolato quindi può essere stimato e corretto.
**Random error:** come dice il nome è l'errore che cambia in modo imprevedibile quindi non è calcolabile e correggibile.

Per colpa degli errori random, ci sono diversi casi in cui non si può fare una misura 100% accurata.

A volte è positivo perchè ci sono casi in cui l'incertezza è voluta e può portare a vantaggi. Ad esempio in un gioco si vuole che ci siano delle cose incerte così che il giocatore possa divertirsi meglio.

# Monitoring

**Obiettivo:** monitorare costantemente il sistema in esecuzione nel suo ambiente finale, verificando che il comportamento osservato e le performance rispettino regole ben definite.

Monitoring di solito è fatto sia online che offline. Ed è accostato con **verification** per analizzare i dati raccolti. I dati sono sempre raccolti quando il sistema è in esecuzione tuttavia l'analisi dei dati può essere fatto anche a sistema spento. *Esempio:* scatola nera di un aeroplano, si osserva ad aereo spento, anche se questo è caduto.

Il sistema su cui si esegue monitoring è definito **target system**
Questo si usa sia per capire cosa fare nel mio sistema sia per capire il motivo per cui un sistema potrebbe essere fallito. Se non si esegue monitoring allora non si può imparare dai nostri errori. Attraverso la verification si può anche ottenere una valutazione delle **performance** e della **qualità del servizio** nel sistema.

Quindi quello che abbiamo sono:
- **gli elementi da monitorare**
- **le misure ottenute**
- **un punto di monitoring** che è centralizzato e processa (in automatico o con l'aiuto di un umano) i dati raccolti, estrapolando le informazioni di nostro interesse.

*Nota:* in ogni sistema operativo ci sarà una forma di monitoring delle risorse. Questo è vero ad esempio per linux o per windows, ma anche per diversi sottosistemi, come il sistema bancario di quasi tutte le banche.

*Esempio:* Monitor delle persone nella classe, voglio sapere:
- quante persone ci sono
- % delle persone che si mettono il cappotto/la giacca (perchè è presumibilmente freddo)

Devo definire le seguenti cose:
- monitored devices
- misure e sistemi di misurazione per tutti gli aspetti
- analisi dei dati

*Nota: discusso in classe con diverse proposte da alcuni gruppi con vantaggi e svantaggi di ogni opzione.*

**Technical problems:**
ci sono diversi problemi tecnici che possono accadere durante l'utilizzo di un sistema. Questi devono essere identificati e risolti. Ci sono alcuni tipi di problematiche:
- **identificare gli eventi e le misure**
- **etichettare i dati** (spesso questo può risultare utile anche per il futuro per creare delle banche dati utili in un futuro anche molto avanti nel tempo) questa parte è probabilmente la più complessa perchè non è facile mettere delle etichette sui dati in modo corretto (*Esempio:* il sistema è utilizzato con un'alta percentuale ma non riesco a capire perchè: sta funzionando male? Sta rispondendo correttamente a tante richieste?)
- **trasmettere i dati** al sistema centrale dove verranno analizzati per ricavare delle informazioni in effettivo
- **filtraggio e classificazione dei dati**

**Black box system:**
un sistema si dice una black box (scatola nera) se non si può vedere al suo interno. Questo vuol dire che il sistema funziona (almeno all'apparenza) ma non permette di vedere cosa sta facendo al suo interno. Questo è un problema perchè in molti casi le black box non permettono neanche di monitorarle dall'esterno quindi in pratica non si riesce ad avere un'idea su cosa sta avvenendo dentro di loro.
Le black box potrebbero avere dei metodi di controllo integrati.
Al contrario le **white box** permettono di guardare al loro interno e vedere quante risorse stanno usando e come.

**Probes:**
i probe sono dei processi che permettono di monitorare un sistema in esecuzione. Normalmente i probe in un sistema operativo si trovano a livello utente, possono eseguire system call ma non possono dialogare direttamente con i livelli più bassi rispetto al sistema operativo. Questo comportamento è ottimo, ad esempio, per evitare che un virus possa creare danni irreparabili in un sistema.
Il task manager (o top) è integrato nel sistema operativo quindi è in grado di fare alcune analisi più dettagliate sapendo esattamente tutte le chiamate di sistema ed essendo una **white box** rispetto al sistema operativo (ovvero se stesso).
Un sistema di monitoring di solito ha più di un probe, ognuno dei quali monitora una parte diversa.

**Software e hardware probes:**
fino ad ora abbiamo visto tutti probe che erano a livello software, tuttavia esistono anche probe hardware oppure ibridi.
In alcuni ambiti risulta fondamentale utilizzare probe hardware o ibridi. Non sono argomento specifico di questo corso. *Esempio:* utilizzo dell'hardware aggiuntivo per monitorare un computer di modo da evitare di usare gli stessi componenti che devo monitorare per il monitoraggio.  
Usare probe hardware **NON** è intrusivo di solito.
*Esempio:* SMART per gli hard drive per verificare quali settori non funzionano e avvertire anche nel caso in cui un settore fallirà a breve. È presente una parte hardware che legge i dati e una parte software che che analizza i dati e permette di stampare effettivamente le informazioni. Di solito la parte hardware è una black box, quindi colui che vende gli hard disk deve fornire un'interfaccia.

**Pro e contro degli hardware probe:**
Pro: diminuisce l'intrusività
Contro: deve rifarsi ad un software per stampare i dati e solitamente l'hardware usato è black box (o comunque difficile da usare se non tramite l'interfaccia fornita)

**Tipi di software monitoring:**
- nel processo che si vuole monitorare
- nel sistema operativo
- in un processo probe separato (è l'unica alternativa se non posso accedere al sorgente ne del sistema operativo e ne del processo)

**Pro e contro del software probe:**
Pro: a volte hanno accesso a più informazioni rispetto alle soluzioni hardware
Contro: sono quasi sempre intrusivi.

*ToDo at home:* guardare video in fondo alle slide. Dura un'ora ma la parte importante sono i primi 19 minuti.
