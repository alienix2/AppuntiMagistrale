# Unsupervised learning

**Miglior dettaglio:** <https://github.com/fpinell/mlsa/tree/main/notebooks>

Le capacità dell'unsupervised learning sono egualmente buone per identificare dati che sono nel dataset e che non sono nel dataset. (al contrario del supervised che non funziona bene su dati ignoti). Il punto è che se non hai i labels non puoi proprio usare il supervised learning.
![supervised_unsupervised](../Screenshots/supervised_unsupervised)

## Clustering

Il processo di clustering consiste nel dividere i dati in gruppi omogenei. Si vogliono identificare i dati in modo da trovare dei gruppi di dati simili fra loro. I dati che che sono lontani da tutti i cluster sono definiti come **anomalies** (anomalie). *Nota:* le anomalies devono comunque essere inserite all'interno di uno dei cluster per questo motivo potrebbe essere che siano inserite nel cluster sbagliato.  
*Es.*
![clustering_anomalies](../Screenshots/clustering_anomalies)
Le X sono mal classificate mentre le V sono ben classificate, di base si può vedere che sarebbe molto difficile classificare i punti all'esterno dei cluster ai quali sembrano appartenere.

### K-means

k-means è un metodo di clustering che si basa su un numero di cluster k. L'idea è di trovare k **centroidi** che rappresentano i cluster.  
K-means si basa sul numero di centroidi passati per poi andare ad identificare dei centroidi calcolare la distanza dei diversi punti dal centroide più vicino. Nel metodo si tentano più iterazioni che partono da centroidi diversi (ma sempre in stesso numero) per poi andare a prendere la scelta migliore in basa alla **mean**, ovvero la distanza media dei punti dal centroide più vicino.

#### Finding the number of K

Ci sono diversi modi per capire il numero migliore di cluster da considerare, ad esempio l'algoritmo G-Means è un estensione di k-means che oltre ad eseguire la tecnica k-means calcola anche il numero di cluster secondo alcune euristiche. Un altro metodo utilizzato è quello dell **elbow plot** che consiste nell'andare ad identificare di quanto varia la precisione del metodo al variare di k e prendendo il punto in cui la varianza diventa molto piccola. **N.B:** in generale se io prendo tanti cluster quanti sono i punti chiaramente la distanza di ogni punto dal centroide più vicino diventa 0, ma questo **NON** è un buon clustering.

## Density-based

Questo tipo di catalogazione si basa sulla densità dei dati. L'idea è di trovare dei cluster in cui i dati sono molto vicini fra loro. Se un punto è lontano da tutti gli altri allora viene considerato una anomaly.

La principale differenza coi metodi di clustering classici è che un punto che si trova al centro rispetto ad altri punti che gli stanno intorno viene considerato un'anomaly mentre coi metodi di clustering classici sarebbe stato considerato proprio come centroide.

Con questi metodi di solito si scelgono dei punti chiamati **observer points** che permettono di capire se un punto è un anomaly oppure no. Se un punto è "troppo" lontano è un anomaly.

### Density-Neighbourhood

Questo metodo si basa sul concetto di **neighbourhood** (vicinato). Di solito questa tecnica si usa nel supervised ML ma in questo caso possiamo anche applicarlo all'unsupervised.

Un esempio di questo metodo è **ODIN** che usa un grafo kNN:

- i nodi sono datapoint
- gli archi sono costruiti in modo che i nodi A e B siano collegati se B è un è nel kNN di A o viceversa.

In questo modo se un nodo ha pochi vicini allora sarà un anomaly. Di solito si sceglie un valore di treshold per capire se un nodo è un anomaly o no.  
*Es. di ODIN applicato all'esempio di prima:*
![ODIN](../Screenshots/odin)  
Come si può vedere questo algoritmo si è comportato meglio del k-means nell'identificare le anomalies.

## Angle-Based

Questo metodo si basa sull'angolo tra i punti. Se due punti sono molto vicini allora l'angolo tra i due è grande. Se un punto ha un angolo molto piccolo rispetto agli altri allora è un anomaly.

Un esempio di questo è **ABOD** (Angle-Based Outlier Detection) che si basa sull'angolo tra i punti. Se un punto ha un angolo molto piccolo rispetto agli altri allora è un anomaly.  
*Es. di ABOD applicato all'esempio di prima:*
![ABOD](../Screenshots/abod)  
Come si può vedere in questo caso il comportamento è peggiore rispetto ad ODIN e alla pari con K-means.

## Statistical

L'idea di base è usare delle analisi statistiche per creare una distribuzione e poi capire se un punto è aderente a quella distribuzione oppure no.

Un esempio di questo è **HBOS** (Histogram-Based Outlier Score) che si basa su un istogramma. Gli istogrammi si creano basandosi sulle frequenze dei dati. Se un punto appartiene ad una colonna bassa vuol dire che il punto è un'anomaly.  
$HBOS(p) = \sum_{i=0}^d{log(\frac{1}{hist_i(p)})}$  
*Es. di HBOS applicato all'esempio di prima:*
![HBOS](../Screenshots/hbos)  

## Neural networks

Sono già state viste in precedenza. Un esempio specifico di neural network per l'unsupervised learning è **SOM** (Self organizing maps) che si basa su una rete neurale.
The blue blob is the distribution of the training data, and the small white disc is the current training datum drawn from that distribution.

- All'inizio (sinistra) i nodi SOM sono posizionati arbitrariamente nello spazio dei dati.
- Il nodo (evidenziato in giallo) che è più vicino al datum di training è selezionato. Viene spostato verso il datum di training, come succede per i suoi vicini nella griglia
- Dopo molte iterazioni la griglia tende ad approssimare la distribuzione dei dati (destra)
![SOM](../Screenshots/som)

*Es. di SOM applicato all'esempio di prima:*
![SOM](../Screenshots/som_example)

*Nota:* video interessante: **DA TROVARE :(**
