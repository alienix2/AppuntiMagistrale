# Model for attacks

## Adversary attacks

**Da fare** perchè avevo il PC scarico :( guardare slides

## Defense

### Adversarial training

In questo caso il punto è migliorare manualmente il modello in base a degli attacchi che si conoscono prendendo precauzioni in base a come si sa che l'attacco avversario funziona. Il problema di questa tecnica è che l'attaccante ha sempre un vantaggio dato che noi stiamo soltanto reagendo

### Randomization

In questo caso aumentiamo la robustezza eseguendo delle operazioni randomiche sul modello. Questo metodo è molto efficace ma ha un costo computazionale molto alto.

### Denoising

In questo caso si cerca di rimuovere il rumore dai dati in modo da rendere più difficile l'attacco. Si può cercare di togliere il rumore dalle immagini che l'attaccante ci manda oppure anche andare a rimuovere il rumore da specifiche feature.

**Esempio**: **Feature squeezing** in cui si cerca di ridurre la quantità di bit per pixel in un'immagine in modo da rendere più difficile l'attacco. Inoltre attraverso una verifica della prediction sia sull'immagine originale che sulla versione con squeezing è possibile cercare di capire se l'immagine è già stata attaccata e in qual caso si può ignorare o comunque agire di conseguenza.

### Adversarial autoencoder

In questo caso si cerca di creare un autoencoder che sia in grado di ricostruire l'immagine originale a partire dall'immagine attaccata. Nell'autoencoder si ha un modello a cui diamo in pasto sia la versione originale di x che una versione di x elaborata con l'autoencoder. L'autoencoder diminuisce la superficie dell'attacco il che vuol dire che qualunque tipo di attacco sia stato eseguito sarà meno evidente nell'immagine elaborata. A partire da questo si computa la kl loss. Se questa risulta essere maggiore di un certo valore vuol dire che l'immagine è stata attaccata e quindi non usiamo l'immagine x ma usiamo invece quella x' ricostruita, altrimenti possiamo usare tranquillamente la x dato che non è stata attaccata.

*Nota:* questo tipo di metodo è comodo soprattutto perchè funziona potenzialmente anche su attacchi che non conosciamo, e che non possiamo quindi cercare di difendere usando la tecnica dell'avversarial traning.

### Runtime detection

In questo caso si cerca di capire se l'immagine è stata attaccata vedendo come reagisce il modello alla stessa. Magari alcuni tipi di attacchi possono attivare specifici neuroni in modo particolare oppure molte più volte del normale proprio perchè l'attacco si basa sull'attivarli in modo errato. Questa tecnica consiste nell'inserire dei controlli per identificare queste situazioni.
