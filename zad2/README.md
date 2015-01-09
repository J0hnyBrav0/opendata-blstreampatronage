Wykorzystane moduły: sys, csv, json, getopt, pymongo, pprint

Nie korzytstałem z poprzedniego skryptu, ponieważ csv.DictReader() wydaje mi się bardziej sensowny - kod zyskuje na czytelności, jest krótszy.
Skrypt otwiera połaczenie z lokalna bazą danych mongoDB. Koniecze jest więc aby w systemie był zainstalowany mongoDB, oraz aby zainstalowany był moduł  pymongo (sudo pip install pymongo).

Aby użyć skryptu w lini komend uruchom polecenie:

	$ python csv2jmongo.py -i inputfile.csv
	$ python csv2jmongo.py -l
	$ python csv2mongo.py -h 
	

polecenie1) skrypt otowrzy plik wejściowy(inputfile.csv)  w formacie csv, przetworzy dane do formatu json i zapisze je do lokalnej bazy. 

polecenie 2) wylistuje baze danych.

polecenie 3) wyświetli komunikat pomocy


