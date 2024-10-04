## Esercitazione sulla robustness

Il prof fornisce un file Java che contiene alcuni metodi per eseguire il sorting di array con diversi algoritmi. Occorre trovare i problemi negli algoritmi.  
**Cartella moodle:** https://e-l.unifi.it/mod/folder/view.php?id=1402793  
Nella cartella si trova anche il file di soluzione.  
L'unico algoritmo che in effetti non funziona del tutto è il wonky-sort, nel senso che non ordina l'array.
Vediamo alcuni altri algoritmi che falliscono in specifiche condizioni:
- Wonky-sort sembra funzionare con un numero di elementi pari e se non è presente uno 0. Tuttavia non ritorna mai nessun errore (se non con la null value). **silent**.
- Tutti tranne quicksort e mergesort con la null value ritornando una runtime exception. **Abort**.

