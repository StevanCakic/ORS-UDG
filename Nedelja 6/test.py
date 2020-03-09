# Zadaci sa prvog prakticnog testa

def vrati_suglasnike(string):
    samoglasnici = "aeiou"
    rezultat = ""
    for karakter in string:
        if karakter not in samoglasnici and karakter.isalpha():
            rezultat += karakter
    return rezultat
rezultujuci_string = vrati_suglasnike("string koji sadrzi suglasnike!")
print(rezultujuci_string)

def izdvoji_igrice(lista_igrica):
    minimalna_ocjena = float(input("Unesite minimalnu ocjenu igre:"))
    maksimalna_godina = int(input("Unesite maksimalnu godinu izlaska igre:"))
    rezultat = [naslov for (naslov, izdavac, godina, ocjena) in lista_igrica 
                    if godina <= maksimalna_godina and ocjena >= minimalna_ocjena]
    return rezultat

# print(izdvoji_igrice([("gta5", "rockstar", 2011, 9.3), ("gta4", "rockstar", 2007, 9)]))

def kvadratna_jednacina(a, b, c):
    x1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)
    return x1, x2

print(kvadratna_jednacina(2,3,1))