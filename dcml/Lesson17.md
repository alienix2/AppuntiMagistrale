# Parallel computing, usare le GPU

Perchè ha senso considerare queste architetture? Il motivo principale è che la potenza di calcolo richiesta per eseguire specifiche operazioni sale vertiginosamente e non si può pensare di usare architetture con un singolo core. Per quanto i singoli core migliorino ogni anno, non è niente rispetto all'aumento della richiesta di potenza in proporzione.

## CPU vs GPU

Le GPU sono oggetti inizialmente realizzate per il rendering della parte grafica. Sono fatte di molti core che lavorano in parallelo. Questo le rende molto adatte per il calcolo parallelo. Se le CPU di solito fanno largo uso di parallelismo **simulato** le GPU invece utilizzano il parallelismo reale.

Nella GPU abbiamo un numero elevato di processori che lavorano in parallelo. Ogni processore è molto più semplice di un core di una CPU, ma il fatto che siano molti e che lavorino in parallelo permette di ottenere prestazioni molto elevate per specifici ambiti. La memoria è disegnata che massimizzare il bandwidth.

## Evoluzione delle GPU

Negli ultimi anni è stato esplorato molto di più l'uso delle GPU per il calcolo generale. Questo ha portato a un aumento delle prestazioni e a una maggiore diffusione di queste architetture. Se in origine era usate soltanto come **graphic accelerators** sono invece state sempre più analizzate ed usate anche per processare le immagini.

*Nota:* una singola riga di codice può richiedere anche migliaia di operazioni parallele su una GPU.
*Nota:* sulle slides ci sono più informazioni ma sono tutte molto generali.
