# Machine Learning (ML) od početka

## Sadržaj
* [Uvod](#uvod)


## Uvod

Budući da je oblast ML-a relativno mlada i neistražena u okviru ovog projekat pokušat ću približiti ML ljudima koji imaju iskustva sa programiranjem, ali se nisu okušali u ovoj oblasti, ali i onima koji žele da počnu da se bave ML-om ili Data Sciencom.

Počet ćemo od najosnovnijih stvari kao što su manipulacija sa dataframe-ovima, numpy array-ima, prikazivanje podataka u obliku grafova i vizuelizacija, a nakon toga preći na koncepte Machine Learning pa sve do Deep Learning-a.

U okviru ovog projekta kod koji budem pisao bit će skroz od početka, znači da nećemo koristit već napisane algoritme kako bi došli do rezultata, već ćemo pisati naše algoritme, ali ćemo i da uključujemo već napisane algoritme kako bi mogli upoređivati naše napisane algoritme sa već postojećim.

Razlog zašto ćemo koristit naše algoritme jeste da bi shvatili kako radi jedan algoritam, kako ga možemo podešavati i sve to kako bi dobili bolje rezultate.

Da bi počeli bilo šta raditi potreban nam je neki alat, za početnike najpreporučivljiji alat je <a href="https://jupyter.org/install"><b>Jupyter Nootebook</b></a>, on dolazi u sklopu Anaconda distribucije. 

Uz ovo morate imati instaliran <a href="https://www.python.org/">Python</a> na svom računaru.

U ovom kursu za opreativni sistem koristit ću Linux, ali i za ostale sisteme je vrlo jednostavno jer je vrlo lako instalirati. Ukolikio ipak ne želite ništa na vašem računaru, možete koristiti: <a href="https://colab.research.google.com/">Google Colab</a>, ili ipak možete koristit <a href="kaggle.com">Kaggle</a>, koji omogućava istu funkcionalnost, ali na Kaggle možete da se takmičite sa drugim ljudima iz oblasti Data Scienc-a, te imate pristup raznim data setovima koje Vam omogućavaju da više primjenjujete Vaše znanje. Kada smo već kod baza podataka, još jedan resurs gdje možete pronaći razne data setove je <a href="https://datasetsearch.research.google.com/">Google Dataset</a> 


## Uvod u alate za manipulaciju podataka sa Pythonom
### Numpy, Pandas, Matplotlib

Folder u kojem će ovi tutorijali biti je Alati. U ovom poglavlju ćemo naučiti kako se koristiti osnovnim alatima za manipulaciju podataka koja će se odvijati u programskom jeziku Python. 

Kroz nekoliko primjera proći ćemo kroz ove alate jer će nam oni biti neophodni kada budemo radili sa algoritmima. Naravno da nećemo proći kroz sve njihove funkcije jer ne možemo predvidjeti sve situacije u kojima će te koristiti ove alate, za sva tri od ova alata odnosno biblioteke imamo fantastičnu dokumentaciju s kojom će te se svakodnevno koristiti.

Prva biblioteka, modul ili alat, zovite ih kako želite, je numpy, koji predstavlja osnovu svih podatkovnih struktura koje se koriste za puštanje podataka u neuralnu mrežu ili u algoritam za predikciju.

Nakon toga dolazi pandas koji se koristi za manipulaciju sa podacima, njega sebi predstavite kao Excel u Pythonu jer omogućava funkcionalnosti slične Excelu, te se koristi za učitavanje podataka.

Kada ljudi gledaju u brojeve teško mogu šta primjetiti, ali kada to prikažemo sa lijepom vizuelizacijom već se mogu primjetiti neki trendovi, poremećaji i druge pojave. Za ove procese koristit ćemo Matplotlib.

