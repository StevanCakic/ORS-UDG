# Zadatak 6
'''
    Napisati program koji racuna zbir parnih i proizvod neparnih brojeva od 1 do 15
    Takodje, prikazati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta
'''

suma = 0
proizvod = 1
broj_parnih = 0
broj_neparnih = 0
i = 1
while i <= 15:
    print(i)
    if i % 2 == 0:
        suma += i
        broj_parnih += 1
    else:
        proizvod *= i
        broj_neparnih += 1
    i += 1
print(f"Broj parnih brojeva:{broj_parnih}")

for broj in range(1, 16):
    if broj % 2 == 0:
        suma += i
        broj_parnih += 1
    else:
        proizvod *= i
        broj_neparnih += 1

# Zadatak 7

'''
    Napisati program koji vraca zbir cifara unijetog broja
'''

n = 123
suma = 0
while n > 0:
    cifra = n % 10 # 3
    suma += cifra
    n = n // 10

n = str(123)
suma = 0
for cifra in n:
    suma = suma + int(cifra)