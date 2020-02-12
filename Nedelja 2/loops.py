# stampa prvih 10 prirodnih brojeva
broj = 1
while broj <= 10:
    # print(broj)
    broj = broj + 1

# Zbir prvih deset prirodnih brojeva
suma = 0
broj = 1
while broj <= 10:
    suma = suma + broj
    broj = broj + 1

# print(suma)

# Zbir prvih deset parnih prirodnih brojeva
suma = 0
broj = 2
while broj <= 10:
    suma = suma + broj
    broj = broj + 2

# print(suma)

# Proizvod prvih n prirodnih projeva koji su djeljivi sa 3
n = int(input("Unesite prirodan broj:"))
proizvod = 1
broj = 3
while broj <= n:
    if broj % 3 == 0:
        proizvod = proizvod * broj
    broj = broj + 1
# print(proizvod)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    # print(i)


# Zadatak 4

'''
Napisati program koji vraća broj malih i broj velikih slova za zadati string.
Primjer: upper_lower("Hi Mr. Rober. How are you today?"), 
vraća (19, 4), 19 - broj malih slova, 4 - broj velikih slova. 
Pomoć: da provjeriti da li je karakter slovo koristiti isalpha metod.
'''
'''
recenica = "Hi Mr. Rober. How are you today?"
duzina_stringa = len(recenica)
indeks_karaktera = 0
broj_malih_slova = 0
broj_velikih_slova = 0
# print(duzina_stringa)
while indeks_karaktera < duzina_stringa:
    karakter = recenica[indeks_karaktera]
    if karakter.isalpha():
        if karakter.islower():
            broj_malih_slova += 1
        else:
            broj_velikih_slova += 1
    indeks_karaktera += 1

print(f"Broj malih slova je: {broj_malih_slova}, a broj velikih slova: {broj_velikih_slova}.")
'''
recenica = "Hi Mr. Rober. How are you today?"
broj_malih_slova = 0
broj_velikih_slova = 0
for karakter in recenica:
    if karakter.isalpha():
        if karakter.islower():
            broj_malih_slova += 1
        else:
            broj_velikih_slova +=1


# Zadatak 5
'''
Korisnik unosi tri broja.
Naći minimum i maksimum među unijetim brojevima i rezultat prikazati korisniku
'''

# Zadatak 6
'''
Napisati program koji racuna zbir parnih i proizvod neparnih brojeva od 1 do 15
Takodje, prikazati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta
'''