# Files

f = open("test.txt")
'''
print(f.read())
print(f.read())

f.seek(0)
print(f.read())
'''
f.seek(0)
for line in f:
    print(line)

f.seek(0)
lines = f.readlines()
for line in lines:
    print(line)

f.seek(0)
lines_without_newline = f.read().split("\n")
for line in lines_without_newline:
    print(line)

f.close()

with open("test.txt") as f:
    print(f.read())

with open("novi_fajl.txt", mode="w") as file:
    file.write("Upis u fajl iz Pythona")

# Zadatak 1
# Iz fajlova brojevi.txt izdvojiti sve dvocifrene i trocifrene brojeve
# i upisati ih u novi fajl odabrani_brojevi.txt

nova_lista = []
with open("brojevi.txt") as file:
    brojevi = file.read().split("\n")
    for broj in brojevi:
        if 1 < len(broj) < 4:
            nova_lista.append(broj)

print(nova_lista)
with open("odabrani_brojevi.txt", mode="w") as file:
    for broj in nova_lista:
        file.write(broj + "\n")

# Zadatak 2
# U fajlu studenti nalazi se lista studenata sa ocjenama za zadati predmet.
# (A - 10, B - 9, C - 8, D - 7, E - 6, F - 5)
# Napisati funkciju koja vraca prosjecnu ocjenu ostvarenu na ispitu.
# E [6 - 6.5), D [6.5, 7.5), C [7.5, 8.5), B [8.5, 9.5), A [9.5, 10]
# Studente koji su dobili ocjenu F ne ukljucivati u prosjek
