def add(a=0, b=0):
    return a + b


zbir = add(2, 3)
print(zbir)
print(add(b=2,a=1))

def unos_vise_korisnika(broj_korisnika):
    lista_korisnika = []
    for i in range(0, broj_korisnika):
        ime = input("Unesite ime korisnika:")
        prezime = input("Unesite prezime korisnika:")
        godine = input("Unesite godine korisnika:")
        lista_korisnika.append({"ime": ime, "prezime": prezime,"godine": godine})   

    return lista_korisnika 

'''
lista_korisnika = unos_vise_korisnika(3).copy()
for korisnik in lista_korisnika:
    if int(korisnik["godine"]) > 20:
        print(korisnik)

'''

lista = [10, 20, 30]
for index, value in enumerate(lista):
    print(index, value)
    
print("************************")

person = {"ime": "Boris", "prezime": "Borkovic"}
for key, value in person.items():
    print(key, value)

person["ime"] = "Novo ime"
print(person)

person1 = person
person1["ime"] = "Neko novo"
print(person)
print(person1)