# Lezione 4 - Perché fare Monitoring
## Perché fare monitoring
Nella lezione precedente abbiamo visto come funziona il monitoring. Tuttavia, occorre notare che nessuno ci paga per fare la parte di monitoring, questo significa che dobbiamo farla soprattutto per noi stessi.  
Nella pratica si esegue il monitoring per capire se c'è qualcosa di pericoloso che potrebbe succedere (o sta già succedendo) nel nostro sistema.  

*Es*: si considera qualcosa tipo `top` in cui si vedono diversi processi, la quantità di CPU che utilizzano e il loro PID. Posso capire che se la CPU va sopra una certa soglia c'è qualcosa che non va, però questo non è detto. In una situazione reale non c'è modo di capire quando c'è un attacco da parte di un virus in corso. La prima cosa che potrei pensare è di vedere come si comporta il sistema durante un attacco e, a quel punto, imparare dalla situazione ed evitare che si verifichi di nuovo.

**Problema dall'esempio precedente**: potrebbe succedere che tu non venga attaccato per un lungo periodo. Puoi aspettare per anni? Di solito no.

**Soluzione**: fare accadere i problemi manualmente. **Fault Injection** (iniezione di fault).  
Grazie allo studio del sistema ottengo un **fault model**.  
*Nota*: il fault model può essere ottenuto sia analizzando dei reali attacchi che utilizzando la fault injection, perché entrambe le metodologie permettono di ottenere dati.

### Fault Injection

È chiamato così l'atto di inserire manualmente dei fault nel sistema. Il punto fondamentale è che devono già essere presenti dei sistemi di monitoring prima che si inizi a fare questo processo, altrimenti non si ottengono informazioni.

Tipologie di fault injection:

- **Hardware fault injection**: si iniettano fault a livello hardware.  
  Esempio: costringo un registro ad avere uno specifico valore.
  
- **Software fault injection**: si iniettano fault a livello software.  
  Esempio: modifico un software che utilizza il mio software in modo che lo utilizzi male, e osservo cosa questo causa.

*Nota*: quando si parla di fault injection, può anche capitare di pensare ad alcuni fault da iniettare che in realtà non hanno senso.  
*Es*: non uso il mio computer per fare coding, ma testo cosa succede se Eclipse si comporta male e ruba tutte le risorse.  
*Es*: devo capire perché Firefox crasha, non ha senso che io decida di modificare qualcosa al livello hardware.

**Fasi della fault injection**:
Per prima cosa occorre premurarsi di analizzare un caso in cui il fault causa effettivamente un errore. Se questo non succede, la mia injection non mi permette di testare cosa succede in caso di errore.  
*Ricordiamo*: esempio della corrente che non va, se nessuno entra nella stanza, di sicuro nessuno si farà male per colpa di quella luce.

Schema di un esempio di fault injection:

![Fault Injection](../Screenshots//2024-10-04-145939_hyprshot.png)
Schema di un esempio di fault injection:
![FaultAnalysis](../Screenshots/software_fault)
Si è notato che la distribuzione vedeva le seguenti percentuali:
![FaultAnalysis](../Screenshots/software_fault_distribution)
Da tutti i possibili fault, si è notato che i 12 fault più comuni in effetti coprivano il 50% dei bug totali.

**Essere sicuri che il mio Fault Injection funzioni**
Il modo più facile per capire se la mia injection sta funzionando è iniettare il codice e controllare quali linee del codice vengono chiamate, iniettando specificamente in quelle linee.  
Ci sono casi in cui questo non è però possibile, perché come abbiamo detto, a volte il software da monitorare è una **black box**.  
In questo caso, occorre forzare dall'esterno il componente in uno stato di errore.

**Error Injection**: nel caso sopra descritto si parla di **error injection** perché sto direttamente andando ad inserire un errore, non un fault.  
Qualunque tipo di errore io consideri, comunque devo analizzare come reagisce il mio sistema.

## Robustness Testing

Il **robustness testing** si fa nei sistemi che sono basati su componenti, e l'**error injection** può corrompere in qualche modo anche le interfacce. Questo è l'unico modo per testare i sistemi che sono delle **black box**.
#### Robustness Testing vs Fault Injection:
Il punto fondamentale è che di solito nella fault injection si cambiano gli output (e anche gli input, volendo), mentre nel **robustness test** si cambiano solitamente gli input per vedere cosa succede negli altri componenti.

Il punto fondamentale del robustness testing è cercare di capire se ci sono alcuni input che possono effettivamente causare problemi al sistema e che simulano degli input che in effetti qualcuno di malevolo potrebbe decidere di inviare al nostro sistema.  
*Es*: il sistema si aspetta un **integer**, io provo a mandare un **NAN** oppure una **stringa** e vedo se si comporta in modo corretto per rispondere a questo input errato (e magari malevolo).

Alcuni esempi di *robustness testing*:
- **Fuzz testing**: si mandano input random al sistema per vedere come si comporta. Questo è un test molto semplice ma che può dare risultati molto interessanti.
- **Bit-flip**: si cambiano uno (o più) bit in modo casuale per vedere cosa succede. Questo è un test molto interessante perché può simulare un errore hardware.
- **Data based type**: si mandano dati che non sono del tipo corretto per vedere cosa succede.  
  *Es*: se il sistema si aspetta un intero, io mando una stringa.

Questi test utilizzano una scala (**crash scale**) per decidere quanto è importante il crash che viene causato:

- **Catastrophic**: il sistema non funziona più, l'app diventa corrotta o la macchina si riavvia da sola.
- **Restart**: l'applicazione si pianta e deve essere riavviata.
- **Abort**: l'applicazione termina in modo anomalo.
- **Silent**: l'applicazione continua a funzionare ma non fa quello che dovrebbe fare.
- **Hindering**: l'errore ritornato non è quello che ci si aspettava.

*Nota*: se viene ritornato l'errore corretto, allora il test è passato e non c'è alcun tipo di crash da misurare nella **crash scale**.

Esempio di input che si usa per robust testing:
- **SQL injection**: La vulnerabilità di sicurezza di base si trova cercando di iniettare delle **SQL injection** e vedendo come si comporta il sistema in risposta.
