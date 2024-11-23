# Lezione 3 - Monitoring (part 2)

# Introduzione alle Lezioni di Laboratorio
# Monitoring (Parte 2)

In questa lezione, continuiamo a esplorare il concetto di **monitoring** introdotto nella lezione precedente. Fino a poco tempo fa, era comune monitorare sistemi composti da **singoli computer**, ma oggi, nella maggior parte dei casi, i sistemi sono **distribuiti** e comprendono **dispositivi** sparsi in tutto il mondo. Di conseguenza, il monitoraggio deve considerare non solo il singolo dispositivo, ma l'intero sistema distribuito.

Esempi di Problemi nel Monitoraggio di Sistemi Distribuiti:

- **Dispositivi degradati**: considero due dispositivi, il primo è degradato all'80% e il secondo al 70%, sono entrambi vicini all'essere inutilizzabili ma sono entrambi ancora in utilizzo. Tuttavia, se consideriamo nell'insieme la situazione non è ottimale, perchè a breve, se entrambi si rompessero, non ci saranno più modalità semplici per recuperare il sistema.

- **Sicurezza Web**: ho due dispositivi, il primo riceve un numero alto di ping e il secondo pure. Se i due non si controllano a vicenda potrebbero semplicemente pensare che ci sia un aumento di accessi, mentre in realtà, analizzando tutto il sistema, si potrebbe dedurre che in effetti è in atto un attacco DDOS.

### Monitoring di Sistemi Distribuiti

**Domande da farsi:**
1. È semplice monitorare i sistemi distribuiti?
2. È sempre permesso inserire dei **probe** nel sistema?
3. Dove analizzo i dati? (Es. li analizzo direttamente su una delle macchine in esame o uso una macchina aggiuntiva apposta?)
4. Come prendo le decisioni basate sui dati raccolti?

 **Problematiche Comuni**
- **Eventi non osservabili direttamente**: alcuni eventi possono non essere rilevabili direttamente e richiedono dispositivi che analizzano in dettaglio i dati.
- **Dati insufficienti**: a volte si raccolgono pochi dati e, in alcuni casi, non è possibile ottenere informazioni più dettagliate (ad esempio, nell'uso di software proprietari come **Gmail**, alcune informazioni rimangono una **black box**).
- **Problemi di intrusiveness**: l'intrusività dei sistemi di monitoraggio può aumentare.
- **Integrazione dei dati**: i dati provenienti da sistemi molto diversi devono essere sincronizzati e strutturati in modo comprensibile per tutti i dispositivi.

**Esempio**:
Immagina un caso in cui **Google** e **Unifi** devono collaborare (Google -|-> Unifi). Google fornisce API, ma queste non permettono di accedere a tutte le informazioni, come i dati sui **failure** del sistema. Se Unifi riceve un avviso di failure da Google, come gestisce e comunica Unifi l'incidente agli utenti? Se si usa un singolo dispositivo per monitorare, il fallimento di quel dispositivo può causare problemi a tutto il sistema.

### Strategie di Monitoring

Esistono principalmente due strategie di monitoring:

1. **Selezione di un Leader**: Si sceglie un computer come **leader**. Questo leader coordina gli altri dispositivi, gestendo i **probe** e analizzando i dati per prendere decisioni basate sulle informazioni raccolte.

2. **Distribuzione delle Responsabilità**: Tutti si accordano sulle minime informazioni di funzionamento che devono mettere a disposizione. Da qui per coordinarsi tutti i dispositivi devono anche trovare un modo per comunicare. Di solito alcuni sistemi si adeguano al modo usato da altri se questo risulta più comodo. *Es.* Unifi si adegua al modo che google ha di monitorare.

#### Automatic Failure Reporting
I primi esempi di report di failure automatici che ci vengono in mente sono i **blue screen of death** di Windows.

#### Telemetria
La Telemetry (**telemetria**) è una parte del sistema che sta diventando sempre più importante e inserita in modo ampio nei sistemi. Con telemetria intendiamo l'atto di monitorare i dati nel sistema. *Es.* nella formula-1 la macchina invia dati di telemetria al muretto, nel quale ci sono molti ingegneri che valutano se e quando fare un pit-stop (e anche se la macchina potrebbe esplodere).

*Nota:* il tool che proveremo noi per questa parte è wire-shark, che si occupa delle interfacce di rete principalmente.

### Wire-shark

Official site: https://www.wireshark.org/
Vedere la documentazione per installazione e utilizzo.  
Su arch `sudo pacman -S wireshark-qt` per la versione con la GUI.
I dati ottenuti da wire-shark sono molto dettagliati e possono essere esportanti in diversi formati.  
Uno dei questi ad esempio è il .csv da cui poi possiamo analizzare i dati con un software di gestione di spreadsheet. Notiamo che alcune parti del traffico sono mostrate in formati non troppo comodi. Per esempio il campo *info* in wire-shark è pieno di informazioni difficile da leggere correttamente.  
Un altro formato è il semplice .txt contenente tutto il testo. Quello notiamo comparando con il .csv è che il .txt è molto più difficile da leggere, soprattutto per una lettura automatica, tuttavia contiene solitamente molto più informazioni, incluse anche quelle non strutturate che vanno perse nella conversione in .csv

**Il formato migliore:** il formato migliore e quello più comodo è il .json (o il .xml come alternativa). Nel file .json le informazioni non vanno perse ma vengono comunque tutte catalogate. Spesso nel .json troviamo anche molti dati inutili, ma il punto è che comunque di sicuro possiamo estrapolare le informazioni di cui abbiamo bisogno.
*Nota:* il .json non è facilissimo da leggere per un umano, ma è molto comodo per un computer. In più comunque è possibile convertire il .json in un .csv, magari con modalità custom da noi definite.

*Per spiegazione sulla GUI e funzionalità di wire-shark guardare anche le slide:* https://e-l.unifi.it/pluginfile.php/3265301/mod_resource/content/9/DCML-CPS_3_Monitoring_2.pdf

Su **Arch Linux**:
```bash
sudo pacman -S wireshark-qt

