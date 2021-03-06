## Uvod u alate za manipulaciju podataka sa Pythonom

Prvi alat kao što smo već rekli je <b>numpy</b>. Ukoliko numpy nije instaliran možete ga instalirati na svim opreativnim sistemima uz par komandi, ukoliko koristite neke od prethodno navedeni alata kao što su Google Colab ili Kaggle onda vi ne morate instalirati i možete preskočiti ovaj dio:

Ukoliko ćete koristiti Jupyter Notebook:

    conda install numpy

    conda install pandas

    conda install matplotlib

Ukoliko ćete koristiti Python skriptu:
    
    pip install numpy
    (Linux) pip3 install numpy

    pip install pandas
    (Linux) pip3 install pandas

    pip install matplotlib
    (Linux) pip3 install matplotlib

### Prvi koraci

Da bi krenuli sa radom u Jupyter Notebook na lokalnom računaru moramo prvo da pokrenemo Jupyter server, a kako ćemo to uraditi? 

Odite u folder u kojem želite da sačuvate vašu datoteku npr. Dokumenti, pritisnete Shift i desni klik miša i odaberite otvori sa PowerShell, kada to uradite pojavit će se prozor u kojem ćete upisati Jupyter Notebook, nakon toga ćete dobiti link koji izgleda ovako:

        http://localhost:8888/?token=i mnogo brojeva i slova u ovom dijelu

Kopirajte taj link i zalijepite u link bar vašeg preglednika (Google Chrome, Edge, FireFox)

<img src="slike/Screenshot 2020-12-06 181358.png">

Trebali bi sada imati ovakvu sliku bez ova dva fajla, da bi kreirali novi fajl odite na "New", a zatim odaberite "Python 3", Nakon što ste kreirali vašu svesku i ušli u nju trebate imati ovakvu sliku:

<img src="slike/Screenshot 2020-12-06 181709.png">

Sada prelazimo u notebook kako bi mogli raditi, svi ostali primjeri će biti u notebook, nazvanim po alatima (numpy.ipynb, pandas.ipynb, matplotlib.ipynb)

Kroz instalacione procese sve tri biblioteke smo prošli, ono što sada slijedi je pandas, koji se najčešće koristi kod čišćenja podataka i modeliranja data setova, razlog tome je njegova fleksibilnost, te njegova jednostavnost. 

Često sam dobijao pitanje pa zašto ne koristiš Excel za čišćenje podataka? Oni koji nisu toliko upućeni i nemaju širok pogled na sve stvari, Excel je jako spor što se tiče čišćenja podataka i ograničen je sa brojem redova koji može da čuva u jednom fajlu. Mislim da je oko 16 miliona redova maksimalni kapacitet, ali nemojte me držati za riječ.

Neko bi rekao da je 16 miliona unosa mnogo, ali kada živite u svijetu gdje je krenula revolucija u smislu prikupljanja podataka gdje se na svakom koraku u vašem pregledniku prikupljaju podaci uz tzv. kolačiće, a sve u smislu kako bi vam servirali prilagođen oglašivački program.

Ali dosta priče, hajmo mi krenuti na pandas, u ovoj sekciji ću ući malo dublje i u Python, kako bih vam malo približio objektno orijentisano programiranje, te njegov značaj kada čistimo podatke.