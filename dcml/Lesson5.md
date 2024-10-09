# Data analysis

Prima lezione di Muhammad Atif. Lui viene dal Pakistan.  
Insegnerà alcune tecniche basate sul machine learning, soprattutto per l'analisi dei dati in modo da fare intrusion detection e anomaly detection.

Per la data analysis si parte da una situazione in cui abbiamo già ottenuto dei dati dalle fasi precedenti (visto nelle altre lezioni).  
Quello che succede normalmente è che c'è una catena **fault** -> **error** -> **failure**. Noi vogliamo fare in modo che questa catena si possa rompere dato che spesso l'errore potrebbe essere catastrofico.

**fault** -> **error** -|> **failure**, di solito si vuole mettere una barriera fra error e failure. Per fare questo una tecnica che funziona molto bene è quella di predire dei possibili failure di modo da evitare che si verifichino prima ancora che si possano verificare. È noto in letteratura che questo è un tipico caso in cui il machine learning funziona molto bene.

## Machine learning
**Esempio fondamentale sul machine learning:**  
Consideriamo una persona che ascolta musica. Vedendo il tipo di musica che ascolta possiamo capire i gusti della sua musica (genere, tempo ecc.). In base alle canzoni che la persona ascolta e anche in base alle canzoni che invece salta subito, si può capire quali canzoni gli stanno piacendo e quali no. Se dividiamo la musica in due parti *like* e *dislike* come possiamo decidere a quali dei due insiemi apparterrà un nuovo brano? Un metodo consiste nell'usare il machine learning per confrontare quella canzone con tutte le altre di modo da capire in quali dei due insiemi è più probabile che finisca.

**Supervised vs unsupervised learning:**
- **Supervised learning:** si ha un insieme di dati di training e un insieme di dati di test. Si addestra il modello sui dati di training e si testa sul test set. Si sa già a priori quali sono le classi di appartenenza. Si sanno già quindi le **label** (etichette) che sono associate ai dati. *Es:* considero un caso di studio su come funzionano i soldi, ho già delle classi come euro, rupie e dollari.
- **Unsupervised learning:** non si sa a priori quali sono le classi di appartenenza. Si cerca di capire quali sono le classi di appartenenza. Occorre fare quello che è chiamato **clustering** per assegnare le label ai dati. *Es:* gioco del wicket (wtf?) ho informazioni sui giocatori e su quanti punti hanno fatto, potrei volerli distinguere in base ad alcune loro caratteristiche, per esempio coloro che fanno i battitori saranno quelli che hanno fatto più punti dato che in quel ruolo di solito si fanno più punti (boh, non so che gioco sia ma pare avere senso).
- **Reinforcement learning:** è un particolare tipo di unsupervised machine learning in cui si cerca di migliorare il modello di machine learning mentre lo si usa, dando feedback sul modo in cui sta facendo clustering. *Es:* si vogliono distinguere gatti e cani in un'immagine, se il sistema identifica un cane come cane, gli dico che ha fatto correttamente, mentre se identifica il cane come gatto gli vado ad indicare l'errore di modo che la prossima volta possa riconoscere meglio gli animali.

*Esempi nella vita reale:*
- Facebook che ti riconosce la faccia nelle foto di tuoi amici (supervised learning perché si basa sulle tue altre foto a cui tu metti l'etichetta in modo implicito quando le pubblichi)
- Netflix che ti consiglia i film in base alle tue preferenze (supervised perché si basa su quello che hai guardato e che ha già tutta una serie di metadati)
- identificazione di persone che stanno usando la tua carta clonandola (basato su posizione, attitudini di spesa ecc.) (unsupervised learning perché cerca di trovare alcuni outlier "caratteristiche" che sembrano tipiche di una fraud, ma non si ha la certezza).

**Rappresentazione dei dati in un dataset:**  
![Rappresentazione dei dati in un dataset](../Screenshots/dataset)

## Processo di data analysis
**Passi per il processo di data analysis:**
- Creare il dataset
- **Exploratory study:** in pratica si cerca di esplorare il dataset e capire se ha già dei label o se si possono aggiungere facilmente ecc.
- **Feature selection:** capire quali feature (caratteristiche) sono quelle da considerare, spesso questa cosa è integrata nell'algoritmo che decidiamo di utilizzare
- Scegliere l'algoritmo di machine learning
- Scelta delle metric per valutare se l'algoritmo che abbiamo scelto funziona bene oppure no. Partendo da quelle metriche segue chiaramente una discussione dei risultati ottenuti dall'algoritmo sulle stesse. *Es.* Ho un algoritmo che richiede un giorno per fare l'analisi e da dati perfetti e un altro che impiega un minuto ma è preciso nell'80% dei casi, quale uso? Dipende da altri fattori come se ho problemi di tempo o le risorse usate da ognuno dei due algoritmi.

**Dataset:** data strutturata in punti **DP** descritti da un insieme di feature **F**.  
Il dataset deve essere allenato utilizzando un **training set** (insieme di test). Dal processo di test otteniamo il modello dell'algoritmo. Il modello restituisce una valutazione che permette di capire le classi dei singoli data point. A quel punto se noi abbiamo dei label che sappiamo (ma che non abbiamo fornito all'algoritmo) possiamo vedere quanto bene si è comportato in base a delle metrics

### Selezione delle classification metrics

Una prima valutazione che bisogna fare sull'algoritmo è la valutazione che ha dato di un data point rispetto alla realtà che noi conosciamo, ci sono 4 casi:
- TP **true positive**, was true, predicted true
- TN **true negative**, was false, predicted false
- FP **false positive**, was false, predicted true
- FN **false negative**, was true, predicted false

Alcuni di questi casi sono più problematici di altri. In particolar modo i FN possono portare a conseguenze catastrofiche mentre i FP solitamente portano soltanto ad un eccesso di sicurezza e verifiche successive che non erano veramente necessarie. *Es.* il modello dice ad una persona che ha alte probabilità di avere il cancro che in realtà sta bene -> la persona non si cura e muore. *Esempio inverso:* il modello dice ad una persona sana che potrebbe avere il cancro, lei va a fare ulteriori analisi e scopre che tutto e apposto, al più si è presa uno spavento evitabile.

**Diagramma delle metriche basate su TP, TN, FP, FN:**
![Diagramma delle metriche basate su TP, TN, FP, FN](../Screenshots/metrics_diagram)
Partendo da questo diagramma ci sono altre metriche che si posson ottenere combinando più di una di questa. Ad esempio **F-score(B)**=$\frac{(1 + B^2)*PR}{(B^2P)R}$

**Problemi di queste metriche:**  
soprattutto se si parla di dataset che sono sbilanciati le metriche sopra descritte potrebbero avere dei problemi.  
*Es:* si considera un campione preso da una sala di urgenza di un ospedale dove quasi tutte le persone hanno il cancro. Si considera poi un algoritmo che dice che tutte le persone hanno il cancro. Questo algoritmo può arrivare ad avere un accuracy, precision e recall molto alta e un FP bassissimo, ma ciononostante non è un buon algoritmo, non ha senso di esistere ed è inutile. Il problema è che il dataset di test non era stato creato correttamente.

**Un'altra metrica:**
![Un'altra metrica](../Screenshots/MCC)
In questa metrica:
- -1 significa che l'algoritmo ha catalogato tutto correttamente
- 1 significa che l'algoritmo ha catalogato tutto in modo errato.
- 0 significa che l'algoritmo ha praticamente tirato ad indovinare.

*Nota:* questa metrica è molto utile per dataset sbilanciati infatti se prendiamo l'esempio sopra descritto questo algoritmo darebbe 0.
*Nota:* questi algoritmi come si può notare vanno bene solo per classificazioni binarie.

## Signature vs Anomalies
Gli algoritmi basati sulla **signature** (**signature-based**) cercano di identificare una firma da assegnare ad un particolare tipo di dato. Questo significa che in base a come un dato è composto in realtà diviene identificabile rispetto a tutti gli altri.

Gli algoritmi basati sulle **anomalies** (**anomaly-based**) cercano di identificare i dati che sono diversi da tutti quelli che sono ritenuti "normali". Questo significa che in base a come un dato è diverso da tutti gli altri diviene identificabile.  
*Nota:* questi algoritmi non forniscono una firma ma soltanto un'indicazione di anomalia. *Es:* la gente usa youtube di solito nella sera perchè sono a scuola/lavoro durante il giorno. Sapendo questo i server di youtube si aspettano molto traffico negli orari serali, se ricevono molto traffico nella mattina, questo sarà identificato come anomalia.

**Predire fault o attacchi mai visti:**  
Cosa succede nel caso in cui si parli di fault con cui non abbiamo mai avuto a che fare oppure nuovi attacchi? Occorre che il mio modello sia in grado di identificarli e predire che stiano per succedere.  
Gli algoritmi basati sulla signature non sono in grado di fare questo tipo di predizione perché non hanno dati per assegnare una firma. Un algoritmo basato su un anomalia invece può rendersi conto che qualcosa non va ed evitare anche questo tipo di attacchi. (Es. Zero-day)

**Categorie di anomalie:**
- **Point anomalies:** un singolo punto è anomalo rispetto a tutti gli altri. *Es:* un utente che fa 1000 download in un giorno mentre tutti gli altri ne fanno 10.
- **Contextual anomalies:** un punto è anomalo rispetto ad un certo contesto. *Es:* un utente che fa 1000 download in un giorno mentre tutti gli altri ne fanno 10, ma se si considera che l'utente è un amministratore di sistema allora il comportamento non è anomalo, anche se pare essere una point anomaly non è quindi una contextual anomaly.
- **Collective anomalies:** un insieme di punti è anomalo rispetto a tutti gli altri. *Es:* un gruppo di utenti che fa 1000 download in un giorno mentre tutti gli altri ne fanno 10.

**Tipi di algoritmi di anomaly detection:**
- **Classic algorithms:** basati su dati ottenuti nel tempo. Di solito utilizza tutti i dati che ha a disposizione
- **Sliding windows:** considera solo i dati ottenuti in una specifica finestra di tempo. Di solito utilizza solo gli ultimi dati che ha a disposizione

Ognuna di queste due categorie ha pro e contro. In particolare gli algoritmi sliding windows usano di solito meno memoria ma hanno anche meno dati su cui lavorare e lo stato dell'arte non è così ben definito come per gli algoritmi classici.
*Esempio di sliding window:* SPS, si basa sul concetto di lower treshold and upper treshold ed è usato spesso sul web.
