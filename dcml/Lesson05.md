# Data analysis

#### Introduzione
Per la **data analysis**, si parte da una situazione in cui abbiamo già ottenuto dei dati dalle fasi precedenti (visti nelle altre lezioni).  
Normalmente, si verifica una catena:  
`fault -> error -> failure`. Noi vogliamo fare in modo che questa catena si possa rompere, dato che spesso l'errore potrebbe essere catastrofico.

**Fault -> Error -|> Failure**. Di solito si vuole mettere una barriera tra l'errore e il fallimento. Per fare questo, una tecnica che funziona molto bene è quella di **predire** dei possibili fallimenti in modo da evitarli prima che si possano verificare. È noto in letteratura che questo è un tipico caso in cui il **machine learning** funziona molto bene.

## Machine Learning

**Esempio fondamentale sul machine learning**: consideriamo una persona che ascolta musica. Vedendo il tipo di musica che ascolta, possiamo capire i suoi gusti musicali (genere, tempo, ecc.).  
In base alle canzoni che la persona ascolta e anche alle canzoni che salta subito, si può capire quali canzoni gli piacciono e quali no.  
Se dividiamo la musica in due categorie: **like** e **dislike**, come possiamo decidere a quale dei due insiemi apparterrà un nuovo brano? Un metodo consiste nell'usare il machine learning per confrontare quella canzone con tutte le altre di modo da capire in quale dei due insiemi è più probabile che finisca.
#### Supervised vs Unsupervised Learning:

- **Supervised learning**: si ha un insieme di dati di training e un insieme di dati di test. Si addestra il modello sui dati di training e si testa sul test set. Si sa già a priori quali sono le classi di appartenenza. Si sanno già quindi le **label** (etichette) che sono associate ai dati. *Es:* considero un caso di studio su come funzionano i soldi, ho già delle classi come euro, rupie e dollari.
  
- **Unsupervised learning**: non si sa a priori quali sono le classi di appartenenza, e dobbaimo cercare di capire quali sono. Occorre fare quello che è chiamato **clustering** per assegnare le label ai dati. *Es:* gioco del cricket ho informazioni sui giocatori e su quanti punti hanno fatto, potrei volerli distinguere in base ad alcune loro caratteristiche, per esempio coloro che fanno i battitori saranno quelli che hanno fatto più punti dato che in quel ruolo di solito si fanno più punti.
  
- **Reinforcement learning**: è un particolare tipo di unsupervised machine learning in cui si cerca di migliorare il modello di machine learning mentre lo si usa, dando feedback sul modo in cui sta facendo clustering. *Es:* si vogliono distinguere gatti e cani in un'immagine, se il sistema identifica un cane come cane, gli dico che ha fatto correttamente, mentre se identifica il cane come gatto gli vado ad indicare l'errore di modo che la prossima volta possa riconoscere meglio gli animali.

**Esempi nella vita reale**:
- **Facebook** che ti riconosce la faccia nelle foto dei tuoi amici (supervised learning, perché si basa sulle altre foto a cui metti etichette in modo implicito quando le pubblichi).
- **Netflix** che ti consiglia film in base alle tue preferenze (supervised learning, perché si basa su ciò che hai guardato e che ha già una serie di metadati).
- Identificazione di persone che stanno usando la tua carta clonandola (basato su posizione, attitudini di spesa, ecc.) (**unsupervised learning**, perché cerca di trovare alcuni outlier che sembrano tipici di una **fraud** ma non si ha la certezza).

## Rappresentazione dei dati in un dataset
![Rappresentazione dei dati in un dataset](../Screenshots/dataset)

Il processo di **data analysis** si compone di vari passaggi:
1. **Creare il dataset**.
2. **Exploratory study**: In pratica, si cerca di esplorare il dataset e capire se ha già delle labels o se possono essere aggiunte facilmente.
3. **Feature selection**: Capire quali features (caratteristiche) sono rilevanti. Spesso questa parte è integrata nell'algoritmo che decidiamo di utilizzare.
4. **Scegliere l'algoritmo di machine learning**.
5. **Scelta delle metriche** per valutare se l'algoritmo scelto funziona bene o no.  
   *Es*. Ho un algoritmo che richiede un giorno per fare l'analisi e fornisce risultati perfetti, e un altro che impiega un minuto ma è preciso nell'80% dei casi. Quale uso? Dipende da altri fattori come se ho problemi di tempo o le risorse utilizzate da ciascun algoritmo.

**Dataset**: data strutturata in punti **DP** descritti da un insieme di features **F**. 
Il dataset deve essere allenato utilizzando un **training set** (insieme di test). Dal processo di test otteniamo il modello dell'algoritmo, che restituisce una valutazione che permette di capire le classi dei singoli **data point**.  A quel punto se noi abbiamo dei label che sappiamo (ma che non abbiamo fornito all'algoritmo) possiamo vedere quanto bene si è comportato in base a delle metrics.

Una prima valutazione che bisogna fare sull'algoritmo è la valutazione che ha dato per ogni punto rispetto alla realtà che conosciamo. Ci sono 4 casi:

- **TP** (True Positive): Era vero, è stato predetto vero.
- **TN** (True Negative): Era falso, è stato predetto falso.
- **FP** (False Positive): Era falso, è stato predetto vero.
- **FN** (False Negative): Era vero, è stato predetto falso.

Alcuni di questi casi sono più problematici di altri. In particolare, i **FN** (False Negative) possono portare a conseguenze catastrofiche, mentre i **FP** (False Positive) solitamente portano soltanto ad un eccesso di sicurezza e verifiche successive non realmente necessarie.  
*Esempio*: Il modello dice ad una persona che ha alte probabilità di avere il cancro, ma in realtà sta bene -> la persona non si cura e muore.  
*Esempio inverso*: Il modello dice ad una persona sana che potrebbe avere il cancro, lei fa ulteriori analisi e scopre che tutto è a posto. Al massimo, si è presa uno spavento evitabile.

![Diagramma delle metriche basate su TP, TN, FP, FN](../Screenshots/metrics_diagram)  
Partendo da questo diagramma, ci sono altre metriche che si possono ottenere combinando più di una di queste. Ad esempio:

$$Fscore(\beta) = \frac{(1 + \beta²) \cdot P \cdot R}{(\beta² \cdot P + R)}$$

Soprattutto nei dataset sbilanciati, le metriche sopra descritte potrebbero avere dei problemi.  

*Esempio*: Se consideriamo un campione preso da una sala di urgenza di un ospedale, dove quasi tutte le persone hanno il cancro, e poi un algoritmo dice che tutte le persone hanno il cancro. Questo algoritmo potrebbe avere una **accuracy**, **precision** e **recall** molto alta e un **FP** bassissimo, ma in realtà non è un buon algoritmo e non ha senso esistere. Il problema è che il dataset di test non era stato creato correttamente.

Un'altra metrica:$$MCC = \frac{TP \times TN-FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$
In questa metrica:
- **1** significa che l'algoritmo ha catalogato tutto correttamente.
- **-1** significa che l'algoritmo ha catalogato tutto in modo errato.
- **0** significa che l'algoritmo ha praticamente tirato a indovinare.

*Nota:* questa metrica è molto utile per dataset sbilanciati infatti se prendiamo l'esempio sopra descritto questo algoritmo darebbe 0.
*Nota:* questi algoritmi come si può notare vanno bene solo per classificazioni binarie.

### Signature vs Anomalies

Gli algoritmi basati sulla **signature** (signature-based) cercano di identificare una "firma" per un particolare tipo di dato. Questo significa che un dato diventa identificabile rispetto a tutti gli altri in base alla sua composizione.  

Gli algoritmi basati sulle **anomalie** (anomaly-based) cercano di identificare i dati che sono diversi da tutti quelli considerati "normali".  
Questo significa che in base a come un dato è diverso da tutti gli altri diventa identificabile.  
*Nota:* questi algoritmi non forniscono una firma ma soltanto un'indicazione di anomalia.

*Esempio*: Le persone usano **YouTube** principalmente la sera, ma se i server ricevono molto traffico al mattino, questo sarà identificato come anomalia.

##### Predire fault o attacchi mai visti
Cosa succede se ci troviamo di fronte a un fault mai visto prima o un attacco nuovo?  Occorre che il modello sia in grado di identificarli e predire che stiano per succedere. Gli algoritmi basati sulla **signature** non sono in grado di fare questa predizione, poiché non hanno dati per assegnare una firma. Gli algoritmi basati sulle **anomalie**, invece, possono rendersi conto che qualcosa non va, anche senza dati specifici per la firma. Un algoritmo basato su un anomalia invece può rendersi conto che qualcosa non va ed evitare anche questo tipo di attacchi. (Es. Zero-day)

Categorie di anomalie:

1. **Point anomalies**: Un singolo punto è anomalo rispetto a tutti gli altri.  
   *Es*: Un utente che fa 1000 download in un giorno, mentre tutti gli altri ne fanno 10.
   
2. **Contextual anomalies**: Un punto è anomalo rispetto a un certo contesto.  
   *Es*: Un utente che fa 1000 download in un giorno, ma se è un amministratore di sistema, non è anomalo.

3. **Collective anomalies**: Un insieme di punti è anomalo rispetto a tutti gli altri.  
   *Es*: Un gruppo di utenti che fa 1000 download, mentre gli altri ne fanno solo 10.

Tipi di algoritmi di anomaly detection:
1. **Classic algorithms**: basati su dati ottenuti nel tempo.  Di solito utilizza tutti i dati che ha a disposizione.
2. **Sliding windows**: considerano solo i dati ottenuti in una finestra temporale specifica. Di solito utilizza solo gli ultimi dati che ha a disposizione.

Ognuna di queste due categorie ha pro e contro. Gli algoritmi **sliding windows** usano solitamente meno memoria ma hanno meno dati su cui lavorare, e lo stato dell'arte non è così ben definito come per gli algoritmi classici.  
*Esempio di sliding window*: **SPS**, basato su concetti di **lower threshold** e **upper threshold**, è spesso usato sul web.
