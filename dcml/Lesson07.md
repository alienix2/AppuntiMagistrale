# Lezione 7 - Supervised Learning

### Tree-based Algorithms

Sono dei tipi di algoritmi che funzionano bene per decisioni binarie. È una tecnica comune per gli algoritmi di supervised learning. Il punto è define un confine linear o non-linear.

Gli alberi che usiamo si chiamano **alberi di decisione**.  
L'idea di base è la stessa che si usa per i normali alberi di decisione, quindi puntano in ogni passaggio a dividere i dati in due split. 
*Es:* si considera l'età >= 10 o < 10.

- **Gini Index**: è un indice che misura l'imprecisione di una decisione su un punto di dati, se fosse presa in modo casuale. Viene indicato con $P_j$, che rappresenta la probabilità della classe $j$. La formula è:

  $$ \text{Gini Index} = 1 - \sum_j P_j^2 $$

- **Entropy (Entropia)**: misura il disordine di una feature rispetto al target. Come nel Gini index, anche qui si cerca di selezionare l'elemento che ha meno entropia. La formula è:$$ \text{Entropy} = - \sum_j P_j \cdot \log_2 (P_j) $$

*Esempio*: se devo decidere se giocare una partita in base a fattori come il tempo atmosferico (soleggiato, nuvoloso, piovoso), la formula del Gini index per i diversi tipi di tempo è la seguente:
![Tabella di partenza](../Screenshots/sunny_rainy_cloudy)

- $Gini(\text{sunny}) = 1 - \left(\left(\frac{1}{3}\right)^2 + \left(\frac{2}{3}\right)^2\right) = \frac{4}{9}$
- $Gini(\text{cloudy}) = 1 - \left(1^2\right) = 0$
- $Gini(\text{rainy}) = 1 - \left(\left(\frac{1}{4}\right)^2 + \left(\frac{3}{4}\right)^2\right) = \frac{6}{16}$

Poi, calcoliamo l'indice Gini per tutto il tempo atmosferico:

$$ Gini(\text{weather}) = P(\text{sunny}) \cdot Gini(\text{sunny}) + P(\text{cloudy}) \cdot Gini(\text{cloudy}) + P(\text{rainy}) \cdot Gini(\text{rainy}) $$

$$ Gini(\text{weather}) = \frac{3}{10} \cdot \frac{4}{9} + \frac{3}{10} \cdot 0 + \frac{4}{10} \cdot \frac{6}{16} = \frac{2}{15} + \frac{3}{20} = \frac{14}{60} = \frac{7}{30} $$

In questo caso, l'indice Gini per "sunny" ci aiuta a costruire un albero di decisione per scegliere se giocare o meno.

![albero di decisione](../Screenshots/decision_tree)

### Random Forest

Il **Random Forest** è un algoritmo di machine learning che si basa su un insieme di alberi di decisione. Ogni albero è costruito in modo indipendente dagli altri. Ogni albero fornisce un risultato, ma alla fine si deve ottenere una decisione univoca. Solitamente, si fa una votazione tra i risultati ottenuti dagli alberi e la maggioranza vince.

*Esempio*: Nell'esempio precedente, ogni albero può considerare diverse **feature** per capire come cambiano le valutazioni.

### Neighbours-based Algorithms

Questi algoritmi si basano sulla distanza tra i dati. L'idea è che un **datapoint** venga assegnato a una classe in base alla classe più frequente tra i suoi vicini. Questi algoritmi sono strettamente legati al concetto di **distanza euclidea**. Di solito, si sceglie un valore $k$ che rappresenta quanti neighbours vicini considerare, e si fa una votazione dove vince la maggioranza.

Uno degli algoritmi più usati è il **K-Nearest Neighbours (kNN)**, che funziona come descritto sopra. Alcuni algoritmi simili valutano la distanza euclidea in modo diverso. È importante scegliere attentamente il valore di $k$, poiché la votazione può cambiare molto. 
*Es*: se scelgo $k=2$ potrei avere molti casi in cui ho un 50% per entrambe le scelte, mentre voglio essere il più possibile sicuro durante le scelte, non tirare a caso.

*Nota*: alcuni di questi algoritmi possono funzionare anche per dati non binari, tuttavia di solito non danno buoni risultati quindi risulta migliore andare a dividere i dati in due sole classi in qualche modo.

### Statistical Algorithms

Gli **algoritmi statistici** si basano su modelli statistici e vengono usati principalmente per fare previsioni. Alcuni esempi di questi algoritmi sono:

- **Naive Bayes**: si basa sul teorema di Bayes. L'idea è creare un modello che minimizzi la probabilità di classificazione errata del datapoint. In genere si utilizza una distribuzione gaussiana per calcolare la probabilità di appartenenza a una classe.
$$\hat{y} = argmax_{k \in {1, ... , k}} \ p(C_k) \prod^{n}_{i=1}p(x_i \mid C_k)$$

*Esempio:* classificare se una persona è maschio o femmina in base ad alcune sue caratteristiche.

- **Linear Discriminant Analysis (LDA)**: Questo algoritmo si basa su un modello lineare, cercando un iperpiano che separi i dati in due classi. L'iperpiano è definito da una funzione lineare. Quando dobbiamo valutare un nuovo punto, lo proiettiamo rispetto a quella linea e lo assegnamo alla classe più vicina.
![Naive Bayes esempio](../Screenshots/male_female)
Si usa una distribuzione gaussiana per calcolare la probabilità di appartenenza ad una classe. *Più dettagli in [slides](./slides/DCML-CPS_6.pd)*  
*Nota:* non andremo in dettaglio sugli algoritmi, è importante capire come funzionano, non sapere come derivarli.

**Linear Discriminant Analysis (LDA):**  
Questo algoritmo si basa su un modello lineare. L'idea è di trovare un iperpiano che separi i dati in due classi. Questo iperpiano è definito da una funzione lineare.
![LDA](../Screenshots/linear_discriminant)
Come si vede in questa foto la prima linea non è buona perchè i dati sono mescolati mentre nella seconda linea sono ben divisi fra loro.
![LDA esempio](../Screenshots/linear_discriminant_example)
La linea verde è detta **Fisher discriminant** e permette di separare i rossi dai blue e da lì calcolare la media per i blu e per i rossi. Quando dobbiamo valutare un nuovo punto lo proiettiamo rispetto a quella linea verde e guardiamo se è più vicino a blu o a rosso e in base a quello lo assegnamo a quella classe.

- **Logistic regression**: questo algoritmo è usato per fare previsioni binarie. L'idea è di trovare una funzione che vada a minimizzare l'errore di classificazione. Questa funzione è di solito una funzione logistica. La differenza dalla linear regression in cui si cercano di predire valori piuttosto che assegnare classi.  Si considerano più variabili e si definisce una value con valore 1 data dalla combinazione di specifici valori su queste variabili. La probabilità di questa variabile va da 0 ad 1. (*più in dettaglio nelle [slides](./slides/DCML-CPS_6.pdf)*)

Usando la maximum likelihood possiamo trovare i valori da assegnare alle singole variabili per massimizzare (**MLE** maximum likelihood estimation).  
Questo tipo di modelli devono prima essere allenati per poi poter esser utilizzati.

### Neural Networks

Le **reti neurali artificiali (ANNs)** sono classificatori basati su un modello matematico che simula il funzionamento del cervello degli animali. Questi modelli sono composti da neuroni connessi da **edge** (connessioni), che trasmettono informazioni da un neurone all'altro. Ogni connessione ha un valore di peso.

I neuroni sono divisi in **layer**, e ogni layer ha pesi diversi. Il segnale passa dal primo layer (input layer) all'ultimo layer (output layer), attraversando eventualmente più di un layer nascosto (hidden layers).

Allenare una rete neurale significa assegnare i pesi corretti agli edge. Questo processo inizia con valori casuali e poi si affina attraverso diverse **epoch** (iterazioni) per trovare i pesi ottimali.

Nota: Le reti neurali possono essere difficili da classificare come deterministiche o indeterministiche, ma in generale possono essere considerate deterministiche, anche se il prof. Atif ha delle riserve.

### Multilayer Perceptron

Un **Multilayer Perceptron (MLP)** è una rete neurale che ha almeno un layer nascosto. Questo tipo di rete è in grado di approssimare qualsiasi funzione continua. La caratteristica distintiva dell'MLP è l'uso della **back-propagation** per l'allenamento, che permette ai layer precedenti di imparare dai successivi.
