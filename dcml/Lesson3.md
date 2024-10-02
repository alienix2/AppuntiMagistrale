## Introduzione sulle lezioni di laboratorio

A partire dalla prossima volta ci saranno delle **lezioni di laboratorio**. Dovrà comunque essere usato il laptop personale.
Il linguaggio che verrà usato è Java, tuttavia imparare il linguaggio non è l'obiettivo del corso. Ci saranno degli snippet di codice mostrato in python ma questo semplicemente perché è il linguaggio più utilizzato per machine learning.

# Monitoring (part 2)

Con questa lezione continuiamo con quello introdotto nella precedente lezione. Abbiamo parlato di monitoring per sistemi singoli ma oggi giorno è molto raro che i sistemi che vogliamo monitorare presentino un singolo computer o comunque dei computer isolati. Notiamo che spesso parliamo di dispositivi che sono anche in parti diverse del mondo ma devono essere monitorati come insieme.  
Ovviamente possiamo pensare a dei sistemi che permettono ai singoli dispositivi di monitorarsi in autonomia, tuttavia ci sono diverse problematiche in questo approccio.  
*Esempio:* considero due dispositivi, il primo è degradato all'80% e il secondo al 70%, sono entrambi vicini all'essere inutilizzabili ma sono entrambi ancora in utilizzo, tuttavia se consideriamo l'insieme la situazione è molto peggiore perchè a breve se entrambi si rompono non ci saranno più modalità semplici per recuperare il sistema  
*Altro esempio:* considero la web-security. Ho due dispositivi, il primo riceve un numero alto di ping e il secondo pure. Se i due non si controllano a vicenda potrebbero semplicemente pensare che ci sia un aumento di accessi mentre in realtà analizzando tutto il sistema si potrebbe dedurre che in effetti è in atto un attacco DDOS.  

## Monitoring di sistemi distribuiti

**Domande da farsi:**
- È semplice monitorare i sistemi distribuiti?
- È sempre permesso inserire dei probe nel sistema?
- dove analizzo i dati? (*Es.* li analizzo direttamente su una delle macchine in esame? Ne uso una aggiuntiva apposta?)
- Come faccio il mio decision making?

**Problematiche comuni:**
- Ci sono eventi che non possono essere osservati direttamente, a volte servono dei dispositivi che analizzano in dettaglio i dati per trarne informazioni
- Ci sono casi in cui si ottengono troppi pochi dati, e magari non se ne possono neanche ottenere di più. (*Es.* io uso Gmail nel mio sistema, ma essendo proprietario come software alcune parti rimangono una black box per me)
- I problemi di intrusiveness si moltiplicano
- I dati e le informazioni processate devono essere integrate fra sistemi molto diversi fra loro. I principali problemi generati da questo sono la necessità di sincronizzazione dei sistemi e la struttura dei dati che dovrebbe essere in comune o quantomeno interpretabile da tutti i dispositivi.

**Esempio ampio:**
Consideriamo un caso di questo tipo:  
google -|-> Unifi. Vediamo che c'è un muro fra google e Unifi, questo significa che in generale google fornisce delle API ma queste non permettono di accedere a tutti i dati. Solitamente le aziende forniscono dati sul normale utilizzo, non inviano informazioni sui failure all'interno del sistema. Inoltre, anche se Unifi riceve dei dati da google, e questi gli notificano un failure, come si comporta Unifi, come comunica a **tutti** gli utenti quello che sta accadendo? Se penso di usare un singolo dispositivo per analizzare i problemi, nel caso in cui questo abbia un failure, tutto il sistema potrebbe avere conseguenze catastrofiche.

## Strategie di Monitoring

Ci sono principalmente due strategie di monitoring:

**Selezione di un leader:**  
In questa opzione si sceglie un computer come **leader**. Questo leader dice agli altri come devono sistemare il loro sistema con i probe e dopodichè lui è in grado di accedere ai probe, analizzare i dati e costruire delle scelte basate sulle informazioni che ne estrapola.

**Distribuzione delle responsabilità:**  
Non c'è alcun leader. Tutti si accordano sulle minime informazioni di funzionamento che devono mettere a disposizione. Da qui per coordinarsi tutti i dispositivi devono anche trovare un modo per comunicare. Di solito alcuni sistemi si adeguano al modo usato da altri se questo risulta più comodo. *Es.* Unifi si adegua al modo che google ha di monitorare.

**Automatic failure reporting:**  
I primi esempi di report di failure automatici che ci vengono in mente sono i **blue screen of death** di Windows.

**Telemetry:**  
La Telemetry (**telemetria**) è una parte del sistema che sta diventando sempre più importante e inserita in modo ampio nei sistemi. Con telemetria intendiamo l'atto di monitorare i dati nel sistema. *Es.* nella formula-1 la macchina invia dati di telemetria al muretto, nel quale ci sono molti ingegneri che valutano se e quando fare un pit-stop (e anche se la macchina potrebbe esplodere)  
*Nota:* il tool che proveremo noi per questa parte è wire-shark, che si occupa delle interfacce di rete principalmente.

## Wire-shark

Official site: https://www.wireshark.org/
Vedere la documentazione per installazione e utilizzo.  
Su arch `sudo pacman -S wireshark-qt` per la versione con la GUI.
I dati ottenuti da wire-shark sono molto dettagliati e possono essere esportanti in diversi formati.  
Uno dei questi ad esempio è il .csv da cui poi possiamo analizzare i dati con un software di gestione di spreadsheet. Notiamo che alcune parti del traffico sono mostrate in formati non troppo comodi. Per esempio il campo *info* in wire-shark è pieno di informazioni difficile da leggere correttamente.  
Un altro formato è il semplice .txt contenente tutto il testo. Quello notiamo comparando con il .csv è che il .txt è molto più difficile da leggere, soprattutto per una lettura automatica, tuttavia contiene solitamente molto più informazioni, incluse anche quelle non strutturate che vanno perse nella conversione in .csv

**Il formato migliore:** il formato migliore e quello più comodo è il .json (o il .xml come alternativa). Nel file .json le informazioni non vanno perse ma vengono comunque tutte catalogate. Spesso nel .json troviamo anche molti dati inutili, ma il punto è che comunque di sicuro possiamo estrapolare le informazioni di cui abbiamo bisogno.
*Nota:* il .json non è facilissimo da leggere per un umano, ma è molto comodo per un computer. In più comunque è possibile convertire il .json in un .csv, magari con modalità custom da noi definite.

*Per spiegazione sulla GUI e funzionalità di wire-shark guardare anche le slide:* https://e-l.unifi.it/pluginfile.php/3265301/mod_resource/content/9/DCML-CPS_3_Monitoring_2.pdf

## Top

top è il prob incluso nei sistemi Unix. È facile utilizzarlo tramite CLI per monitorare il sistema in tempo reale. Permette di specificare il monitoraggio solo di specifiche parti.
