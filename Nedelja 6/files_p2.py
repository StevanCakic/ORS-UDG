# Zadatak 2
# U fajlu studenti nalazi se lista studenata sa ocjenama oblika
# ime, prezime, ocjena za zadati predmet. Svaki student se cuva u novom redu
# Ocjene: 10, 9, 8, 7, 6, 5

# Napisati funkciju koja vraca prosjecnu ocjenu ostvarenu na ispitu.
# E [6 - 6.5), D [6.5, 7.5), C [7.5, 8.5), B [8.5, 9.5), A [9.5, 10]
# Studente koji su dobili ocjenu F ne ukljucivati u prosjek

# Zadatak 3
'''
(Rad sa fajlovima) Sledeće zadatke potrebno je implementirati kao posebne
funkcije u fajlu pod nazivom zad3.py

a) Kreirati funkciju append_to_file koja ima jedan parametar
list_of_products (lista proizvoda gdje je svaki proizvod dictionary
oblika {"naziv": ime_proizvoda, "opis": opis_proizvoda, "godina":
godina_proizvodnje, "kolicina": broj_dostupnih_proizvoda, "cijena":
cijena_proizvoda} ), a dodaje proizvode u fajl products.txt
(pretpostaviti da fajl već postoji i da je prazan) i to u formatu:
Naziv, Opis, Godina, Kolicina, Cijena. Pretpostaviti da su unosi ispravni
(ne treba raditi validaciju)
Primjer:
Input:
[{“naziv”: ”Televizor”, “opis”: ”LG televizor 43inc”, “godina”: 2019,
“kolicina”: 10, “cijena”: 300}, {“naziv”: ”Televizor”, “opis”:” Samsung
televizor 39inc”, “godina”: 2017, “kolicina”: 5, “cijena”: 250}]
Output: (products.txt):
Naziv, Opis, Godina, Kolicina, Cijena
Televizor, LG televizor 43inc, 2019, 10, 300
Televizor, Samsung televizor 39inc, 2017, 5, 250

b) Kreirati funkciju get_products_older_than koja ima jedan parametar i
to godinu koja predstavlja proizvode novije od zadate godine 
koje želite da izdvojite iz fajla.
Input: 2018 (izdvoji sve proizvode iz fajla products.txt čija je
vrijednost ključa “godina” veća ili jednaka godini 2018)
Output (ako posmatrate fajl products.txt iz primjera pod a):
Televizor, LG televizor 43inc, 2019, 10, 300

c) Kreirati funkciju max_possible_revenue koja računa koliki je
maksimalni prihod ako se proda svaki proizvod (posmatrati fajl
products.txt)
Input: Svi proizvodi učitani kao lista dictionary-a iz fajla products.csv
Output: 4250 (10 * 300 + 5 * 250)
'''