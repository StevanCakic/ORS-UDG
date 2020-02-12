# Zadatak 1
# Kreirati sledeće varijable:
    # ime koja sadrži vaše ime
    # prezime koja sadrži vaše prezime
    # godine koja sadrži vaše godine
    # email koja sadrži vašu email adresu
# Štampati rezultat u sledećem formatu:
    # Email adresa korisnika {ime} {prezime} ({godine}) je {email}.

ime = "Marko"
prezime = "Markovic"
godine = "22"
email = "marko.m@gmail.com"

# print(f"Email adresa korisnika {ime} {prezime} ({godine}) je {email}.")

'''
print(4 ** (1/2))
print(1)
'''

# Zadatak 2
# Ako je cijena računara 400e, štampati koliko treba odvojite za plaćanje PDVa
# Štampati rezultat u sledećem formatu:
    # Cijena računara je 400e. Iznos PDVa je {pdv}, 
    # a cijena računara bez PDVa je {cijena bez PDVa}

cijena = 400
pdv = 400 * 0.21

# print(f"Cijena racunara je {cijena}e. Iznos PDVa je {pdv}, a cijena racunara bez PDVa je {cijena - pdv}")

'''
a = "Unesimo neki tekst!"
print(a[1:7:2])
b = a.upper()
print(b)
print(a)

print(a[0:10:3])
print(a[-2])
'''

c = int(input("Unesite vase godine:"))

if c >= 18:
    print("Punoljetan!")
else:
    print("Maloljetan!")

a = 3
b = 5
if a > b:
    print("a je vece od b.")
elif b > a:
    print("b je vece od a.")
else:
    print("Brojevi su jednaki.")

