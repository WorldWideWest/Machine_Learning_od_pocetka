# Tradicionalne metode u ML-u

## Linearna regresija

Linearna regresija je najednostavnija metoda u predikciji varijabli, imamo dva metoda predikcija varijabli u linearnoj regresiji, a to su:

* Predikcija jedne zavisne varijable sa jednom ne zavisnom varijablom
* Predikcija jedne zavisne varijable sa više ne zavisnom varijablom 

Prvo primjer će biti jedna nezavisna varijabla i jedna zavisna varijabla, napisat ćemo našu metodu riješavanja linearne regresije, a nakon toga ćemo je komparirati sa linearnom regresijom koja dolazu u paketu sa <b>sklearn</b>

Formula za jednostavnu linearnu regresiju glasi:

<b style="font-size: 50px">y = a + bx</b>

<b style="font-size: 50px">b - nagib regresione linije</b>

<b style="font-size: 50px">b = r * (Sy / Sx)</b>

<b style="font-size: 30px">r - koeficijent linearne korleacije</b>

<b style="font-size: 30px">Sy - Standardna devijacija y</b>

<b style="font-size: 30px">Sx - Standardna devijacija x</b>

<b style="font-size: 50px">a - presijek regreisone linije</b>

<b style="font-size: 50px">a = y - bx</b>

<b style="font-size: 30px">y - prosijek vrijednosti y</b>

<b style="font-size: 30px">b - nagib regresione linije</b>

<b style="font-size: 30px">x - prosijek vrijednosti x</b>

