lista = [1, 2, 3, "abc", [1,2]]
for element in lista:
    print(element)

print(lista[::-1])

# Naci proizvod jednocifrenih brojeva unutar liste sastavljene od cijelih brojeva,
# Broj 0 preskociti.
lista = [1, 10, 2, 7, 23, -10]
proizvod = 1
for element in lista:
    if element < 10 and element > -10 and element != 0:
        proizvod *= element
print(proizvod)

# Naci proizvod kubova nepranih brojeva liste
lista = [2, 3, 7, 4]
proizvod = 1
for broj in lista:
    if broj % 2 != 0:
        proizvod = proizvod * broj ** 3

print(proizvod)

# Liste by val/by ref

list_a = [1,2,3,4]
# list_b = list_a
list_b = list_a.copy()
list_b[0] = 10
print(list_a)
print(list_b)

'''
    Napisati program koji racuna apsolutnu sumu svih negativnih parnih 
    elemenata za unijeti niz. Štampati sumu. 

    Primjer: 
    Input: [-2, 7, -5, 3, 1, -4]
    Output: 6 (|-2| + |-4|)

'''

lista = [-2, 7, -5, 3, 1, -4]
suma = 0

for broj in lista:
    if broj < 0 and broj % 2 == 0:
        suma += abs(broj)

# print(suma)


tuple = (1,2,3,4)
# tuple[0] = 10

def unos_korisnika():
    
    ime = input("Unesite ime korisnika:")
    prezime = input("Unesite prezime korisnika")
    godine = input("Unesite godine korisnika")
    return ime,prezime, godine

def unos_vise_korisnika(broj_korisnika):
    lista_korisnika = []
    for i in range(0, broj_korisnika):
        ime = input("Unesite ime korisnika:")
        prezime = input("Unesite prezime korisnika:")
        godine = input("Unesite godine korisnika:")
        lista_korisnika.append([ime, prezime, godine])   

    return lista_korisnika  

'''
ime1, prezime1, godine1 = unos_korisnika()
ime2, prezime2, godine2 = unos_korisnika()

'''

lista_korisnika = unos_vise_korisnika(3).copy()

for korisnik in lista_korisnika:
    print(korisnik)

for korisnik in lista_korisnika:
    if int(korisnik[2]) > 20:
        print(korisnik)

'''
ime1 = input("Unesite ime korisnika:")
prezime1 = input("Unesite prezime korisnika")
godine1 = input("Unesite godine korisnika")


ime2 = input("Unesite ime korisnika:")
prezime2 = input("Unesite prezime korisnika")
godine2 = input("Unesite godine korisnika")
'''