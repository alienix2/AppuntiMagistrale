# Algorithms

## Three-based Algorithms

Sono dei tipi di algoritmi che funzionano bene per decisioni binarie. È una tecnica comune per gli algoritmi di supervised learning. Il punto è define un confine linear o non-linear.
Gli alberi che usiamo si chiamano **alberi di decisione**.  
L'idea di base è la stessa che si usa per i normali alberi di decisione, quindi puntano in ogni passaggio a dividere i dati in due split. *Es:* si considera l'età >= 10 o < 10.

**Gini index:** è un indice che serve per capire quanto sarebbe inaccurata una decisione su un datapoint se fosse fatta in modo completamente casuale. Si indica di solito con P_j la probabilità per la classe j.  
$GiniIndex = 1-\sum_j{p_j^2}$

**Entropy:** (entropia) this is a measure that indicates the disorder of the feature with the target. Come nel gini index anche qui si cerca di prendere come selezione l'elemento che ha **meno** entropia.  
$Entropy = -\sum_j{p_j * log_2(p_j)}$

*Esempio:* Devo valutare se giocherò oppure no una partita in base ad alcune caratteristiche del tempo atmosferico come situazione atmosferica, temperatura, umidità e vento.
![Tabella di partenza](../Screenshots/sunny_rainy_cloudy)
$Gini(sunny) = 1-((1/3)^2 + (2/3)^2) = 4/9$  
$Gini(cloudy) = 1-((1)^2) = 0$  
$Gini(rainy) = 1-((1/4)^2 + (3/4)^2) = 6/16$  
$Gini(weather) = p(sunny)*gini(sunny) + p(cloudy)*gini(cloudy) + p(rainy)*gini(rainy) = 3/10 * 4/9 + 3/10 * 0 + 4/10 * 6/16 = 2/15 + 3/20 = 14/60 = 7/30$  
Considerando solo **sunny** otteniamo il seguente albero di decisione :
![albero di decisione](../Screenshots/decision_tree)

### Random Forest

È un algoritmo di machine learning che si basa su un insieme di alberi di decisione. Ogni albero è costruito in modo indipendente dagli altri. Ogni albero ci da un risultato da cui poi occorre però arrivare ad una decisione univoca.  
In particolar modo quello che si fa di solito è fare una **votazione** tra i valori assegnati dagli alberi. Di solito la maggioranza vince.  
*Esempio:* pensando all'esempio precedente l'idea è che magari in ogni albero si considerino delle feature diverse per capire se e come cambiano la valutazione.

## Neighbours-based Algorithms

Questi algoritmi si basano sulla distanza tra i dati. L'idea è che un datapoint sia assegnato ad una classe basandoci su quale è la classe più frequente fra i suoi punti vicini. Questo tipo di algoritmi sono strettamente collegati con il concetto di distanza euclidea. Di solito si sceglie un intero k che indica quanti neighbour scegliere (vicini), a questo punto si fa una votazione dove vince la maggioranza.

Uno dei più usati come algoritmi è il **K-Nearest Neighbour** (kNN), che funziona proprio come descritto sopra. Ci sono algoritmi che valutano in modo diverso basati sempre sulla distanza euclidea. Notiamo che il valore di k va scelto in modo molto attento dato che poi la votazione può cambiare molto. *Esempio:* se scelgo k=2 potrei avere molti casi in cui ho un 50% per entrambe le scelte, mentre voglio essere il più possibile sicuro durante le scelte, non tirare a caso.

*Nota:* alcuni di questi algoritmi possono funzionare anche per dati non binari, tuttavia di solito non danno buoni risultati quindi risulta migliore andare a dividere i dati in due sole classi in qualche modo.

## Statistical Algorithms

Questi algoritmi si basano su modelli statistici. Di solito si usano per fare previsioni. Alcuni esempi di questo genere di algoritmi sono:

**Naive Bayes:**  
Questo algoritmo si basa sul teorema di Bayes. L'idea è di creare un modello che vada a minimizzare la probabilità di classificare male il datapoint.
![Naive Bayes](../Screenshots/naive_bayes)
*Esempio:* classificare se una persona è maschio o femmina in base ad alcune sue caratteristiche.
![Naive Bayes esempio](../Screenshots/male_female)
Si usa una distribuzione gaussiana per calcolare la probabilità di appartenenza ad una classe. *Più dettagli in [slides](/slides/DCML-CPS_6)*  
*Nota:* non andremo in dettaglio sugli algoritmi, è importante capire come funzionano, non sapere come derivarli.

**Linear Discriminant Analysis (LDA):**  
Questo algoritmo si basa su un modello lineare. L'idea è di trovare un iperpiano che separi i dati in due classi. Questo iperpiano è definito da una funzione lineare.
![LDA](../Screenshots/linear_discriminant)
Come si vede in questa foto la prima linea non è buona perchè i dati sono mescolati mentre nella seconda linea sono ben divisi fra loro.
![LDA esempio](../Screenshots/linear_discriminant_example)
La linea verde è detta **Fisher discriminant** e permette di separare i rossi dai blue e da lì calcolare la media per i blu e per i rossi. Quando dobbiamo valutare un nuovo punto lo proiettiamo rispetto a quella linea verde e guardiamo se è più vicino a blu o a rosso e in base a quello lo assegnamo a quella classe.

## Logistic regression

Questo algoritmo è usato per fare previsioni binarie. L'idea è di trovare una funzione che vada a minimizzare l'errore di classificazione. Questa funzione è di solito una funzione logistica. La differenza dalla linear regression in cui si cercano di predire valori piuttosto che assegnare classi.  
Si considerano più variabili e si definisce una value con valore 1 data dalla combinazione di specifici valori su queste variabili. La probabilità di questa variabile va da 0 ad 1. (*più in dettaglio nelle ![slides](/slides/DCML-CPS_6)*)

Usando la maximum likelihood possiamo trovare i valori da assegnare alle singole variabili per massimizzare (**MLE** maximum likelihood estimation)

