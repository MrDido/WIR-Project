PRIMA DI COMPILARE I FILE METTERE I FILE .JAR DI LUCENE IN %JAVA_HOME/LIB
POI AGGIUNGERE VARIABILE D'AMBIENTE CLASSPATH INSERENDO %JAVA_HOME/LIB/*; (RICORDARSI DI METTERE IL ; ALLA FINE)
(SU WINDOWS)


PRIMA DI COMPILARE I FILE MODIFICARE I FILE .JAVA CAMBIANDO LA VARIABILE "path"
PER COMPILARE I FILE JAVA ANDARE NELLA CARTELLA DOVE STANNO E COMPILARE CON IL COMANDO "javac Nomefile.java"
PER ESEGUIRE POI SCRIVERE "java Nomefile".

Indexer.java prende in input come primo argomento il titolo della pagina:
ESEMPI: Tea oppure nel caso di titolo da più parole mettere dentro "" come ad esempio "Information retrieval"
Come secondo argomento invece prende in input -full (per creare il full index) oppure -short (per creare il short index)

ShortSearcher.java prende in input solo il titolo della pagina

FinalRanking.java prende in input solo il titolo della pagina.

ORDINE ESECUZIONE
1) Indexer per creare full index (-full)
2) ShortSearcher per creare short repr
3) Indexer per creare short index (-short)
4) FinalRanking per creare final ranking

ESEMPIO 
1) java Indexer "Information retrieval" -full
2) java ShortSearcher "Information retrieval" 
3) java Indexer "Information retrieval" -short
4) java FinalRanking "Information retrieval" 

